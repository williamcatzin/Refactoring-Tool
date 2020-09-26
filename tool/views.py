from django.shortcuts import render
from tool.models import Commit
from tool.forms import CommitForm
from tool.mlModels import MLmodels

def tool_detail(request):
    """ if request is GET, tool_detail returns html format to
        display text field for user input. Otherwise, commit message
        is classified as SAR or non-SAR. If message is SAR, then
        the type of SAR and the intention is determined and returned
        as a list from sarClassification() and displays the reults.
        Otherwise, notify user message was not SAR.
    """
    if request.method == 'POST':
        form = CommitForm(request.POST)
        if form.is_valid:
            classifier = MLmodels(request.POST.get('body'))
            results = classifier.sarClassification()
            if len(results) == 3:
                mod = form.save(commit=False)
                mod.SAR_nonSAR = results[0]
                mod.type_of_SAR = results[1]
                mod.intention = results[2]
                mod.save()
                form.cleaned_data['body']
                return tool_results(request)
            else:
                mod = form.save(commit=False)
                mod.SAR_nonSAR = results[0]
                mod.type_of_SAR = "none"
                mod.intention = "none"
                mod.save()
                form.cleaned_data['body']
                form = CommitForm()
                message = "Commit message did not pertain to self-admitted refactoring."
                return render(request, 'tool_detail.html', {'form': form, 'msg':message})
    else:
        form = CommitForm()
        message = " "
        return render(request, 'tool_detail.html', {'form':form, 'msg':message})


def tool_results(request):
    """ returns the html format to display results after
        submitting commit message.
    """
    msg = Commit.objects.latest('id')
    return render(request, 'tool_results.html', {'message':msg})
