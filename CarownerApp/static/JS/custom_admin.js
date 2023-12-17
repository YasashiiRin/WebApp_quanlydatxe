window.onload = function () {
    var parent_expired_schedule = document.querySelectorAll('.info1.expired')
    var data_list_schedule = document.querySelectorAll('.info1')
    var parent_almost_expired_schedule = document.querySelectorAll('.info1.almost_expired')
    var block_note = document.querySelectorAll('.block_note')
    console.log(parent_expired_schedule)
    parent_expired_schedule.forEach(item => {
        console.log(listparent)
        var listparent = item.parentElement;
        if(listparent){
            listparent.style.borderLeft = '4px solid rgb(253 98 63)'
            listparent.style.borderBottom = '1px solid rgb(253 98 63)'
        }
    })
    parent_almost_expired_schedule.forEach(item => {
        console.log(listparent)
        var listparent = item.parentElement;
        if(listparent){
            listparent.style.borderLeft = '4px solid rgb(254 187 4)'
            listparent.style.borderBottom = '1px solid rgb(254 187 4)'
        }
    })
    data_list_schedule.forEach(item => {
        var data_l = item.parentElement
        if (data_l){
            data_l.addEventListener('click',function(){
                const data = item.getAttribute('data-id-schedule')
                console.log('id schedule: ',data)
                var newUrl = `http://127.0.0.1:8000/admin/CarownerApp/schedules/${data}/change/`;
                window.location.href = newUrl
            })
        }else{
            console.error("Parent element not found!")
        }
    })
    block_note.forEach(item => {
        var pr = item.parentElement
        if (pr){
            pr.style.background = '#fefff6'
            pr.style.borderLeft = 'none'
            pr.style.paddingLeft = '46px'
            pr.style.paddingRight = '66px'
        }else{
            console.error("Parent element not found!")
        }
    })
  };
  