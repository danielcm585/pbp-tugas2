$(document).ready(() => {
  $.get('/todolist/json', (tasks) => {
    $('#tasks-section').append(`
      <h1 id="num-of-tasks">
        ${tasks.length} tasks
      </h1>
    `)
    tasks.forEach((task) => {
      $('#tasks-section').append(`
        <div data-aos="flip-up" class="mt-2 py-4 px-6 bg-gray-100 items-center justify-between rounded-md flex transition ease-in-out hover:scale-105 hover:bg-gray-200">
          <div class="flex items-center">
            <div class="transition ease-in-out hover:scale-110">
              <a href="/todolist/mark-done/${task.pk}">
                ${task.fields.done ? 
                  `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M10.041 17l-4.5-4.319 1.395-1.435 3.08 2.937 7.021-7.183 1.422 1.409-8.418 8.591zm-5.041-15c-1.654 0-3 1.346-3 3v14c0 1.654 1.346 3 3 3h14c1.654 0 3-1.346 3-3v-14c0-1.654-1.346-3-3-3h-14zm19 3v14c0 2.761-2.238 5-5 5h-14c-2.762 0-5-2.239-5-5v-14c0-2.761 2.238-5 5-5h14c2.762 0 5 2.239 5 5z"/></svg>` :
                  `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M5 2c-1.654 0-3 1.346-3 3v14c0 1.654 1.346 3 3 3h14c1.654 0 3-1.346 3-3v-14c0-1.654-1.346-3-3-3h-14zm19 3v14c0 2.761-2.238 5-5 5h-14c-2.762 0-5-2.239-5-5v-14c0-2.761 2.238-5 5-5h14c2.762 0 5 2.239 5 5z"/></svg>`
                }
              </a>
            </div>
            <div class="pl-6">
              <h2 class="font-bold">
                ${task.fields.title}
              </h2>
              <p class="text-blue-600">
                ${task.fields.date}
              </p>
              <p class="text-gray-500">
                ${task.fields.description}
              </p>
            </div>
          </div>
          <form action="/todolist/delete/${task.pk}">
            <button class="text-red-600 p-2 rounded-md transition ease-in-out hover:scale-110" type="submit">
              Delete
            </button>
          </form>
        </div>
      `)
    })
  })

  $('#drawer-open-button').click(() => {
    $('#drawer').removeClass('right-[-250px]')
    $('#drawer').addClass('right-0')
  })

  $('#drawer-close-button').click(() => {
    $('#drawer').removeClass('right-0')
    $('#drawer').addClass('right-[-250px]')
  })

  $('#new-task-open-button').click(() => {
    $('#new-task-modal').removeClass('hidden')
    $('#drawer').removeClass('right-0')
    $('#drawer').addClass('right-[-250px]')
  })
  
  $('#new-task-close-button').click(() => {
    $('#new-task-modal').addClass('hidden')
  })

  $('#new-task-form').submit((e) => {
    e.preventDefault()
    $.ajax({
      url: '/todolist/create',
      type: 'POST',
      dataType: 'json',
      data: $('#form').serialize(),
      success: (resp) => {
        console.log(resp)
        $('#tasks-section').append(`
          <div data-aos="flip-up" class="mt-2 py-4 px-6 bg-gray-100 items-center justify-between rounded-md flex transition ease-in-out hover:scale-105 hover:bg-gray-200">
            <div class="flex items-center">
              <div class="transition ease-in-out hover:scale-110">
                <a href="/todolist/mark-done/${task.pk}">
                  ${task.fields.done ? 
                    `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M10.041 17l-4.5-4.319 1.395-1.435 3.08 2.937 7.021-7.183 1.422 1.409-8.418 8.591zm-5.041-15c-1.654 0-3 1.346-3 3v14c0 1.654 1.346 3 3 3h14c1.654 0 3-1.346 3-3v-14c0-1.654-1.346-3-3-3h-14zm19 3v14c0 2.761-2.238 5-5 5h-14c-2.762 0-5-2.239-5-5v-14c0-2.761 2.238-5 5-5h14c2.762 0 5 2.239 5 5z"/></svg>` :
                    `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M5 2c-1.654 0-3 1.346-3 3v14c0 1.654 1.346 3 3 3h14c1.654 0 3-1.346 3-3v-14c0-1.654-1.346-3-3-3h-14zm19 3v14c0 2.761-2.238 5-5 5h-14c-2.762 0-5-2.239-5-5v-14c0-2.761 2.238-5 5-5h14c2.762 0 5 2.239 5 5z"/></svg>`
                  }
                </a>
              </div>
              <div class="pl-6">
                <h2 class="font-bold">
                  ${task.fields.title}
                </h2>
                <p class="text-blue-600">
                  ${task.fields.date}
                </p>
                <p class="text-gray-500">
                  ${task.fields.description}
                </p>
              </div>
            </div>
            <form action="/todolist/delete/${task.pk}">
              <button class="text-red-600 p-2 rounded-md transition ease-in-out hover:scale-110" type="submit">
                Delete
              </button>
            </form>
          </div>
        `)
      }
    })
  })
})