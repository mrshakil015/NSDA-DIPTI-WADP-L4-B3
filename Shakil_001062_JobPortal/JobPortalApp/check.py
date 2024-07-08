def searchpage(request):
    
    # search option 
    search=request.GET.get('search')
    # jobs = JobModel.objects.filter(job_title=search)
    jobs = JobModel.objects.filter(
        Q(job_title__icontains=search)|
        Q(deadline__icontains=search)|
        Q(created_by__username__icontains=search)
        )
    # change apply button for seeker when already applied 
    job_filtered=[]
    for i in jobs:
        already_applied=ApplyJobModel.objects.filter(applicant=request.user,applied_job=i)
        job_filtered.append(
            (i,already_applied),
        )
    jobDict={
        'job_filtered':job_filtered
    }
    return render(request,'common/searchpage.html',jobDict)