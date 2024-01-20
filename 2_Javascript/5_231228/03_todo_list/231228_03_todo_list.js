const todoList = document.getElementById("todo-list");
const todoForm = document.getElementById("todo-form");
let todoArr = [];

// 로컬 저장소에 저장
function saveTodos() {
  const todoString = JSON.stringify(todoArr);
  localStorage.setItem("myTodos", todoString);
}

// 로컬 저장소에서 가져오기
function loadTodos() {
  const myTodos = localStorage.getItem("myTodos");
  if (myTodos !== null) {
    todoArr = JSON.parse(myTodos);
    displayTodos();
  }
}
loadTodos();

// 할일 삭제
function handleTodoDelBtnClick(todoClickedId) {
  todoArr = todoArr.filter((item) => {
    return item.todoId !== todoClickedId;
  });
  displayTodos();
  saveTodos();
}

// 할일 완료
function handleTodoItemClick(todoClickedId) {
  todoArr = todoArr.map((item) => {
    if (item.todoId === todoClickedId) {
      return {
        ...item,
        todoDone: !item.todoDone,
      };
    } else {
      return item;
    }
  });
  displayTodos();
  saveTodos();
}

// 할일 출력
function displayTodos() {
  todoList.textContent = "";
  todoArr.forEach((item) => {
    const todoItem = document.createElement("li");
    const todoLabel = document.createElement("span");
    const todoCheck = document.createElement("span");
    const todoDelBtn = document.createElement("span");
    todoLabel.setAttribute("class", "todo-label");
    todoCheck.setAttribute("class", "todo-check");
    todoDelBtn.setAttribute("class", "todo-del");
    todoCheck.innerHTML = "<i class='fa-solid fa-paw'></i>";
    todoLabel.textContent = item.todoText;
    todoDelBtn.innerHTML = "&#9003;";
    todoList.appendChild(todoItem);
    todoItem.appendChild(todoLabel);
    todoItem.prepend(todoCheck);
    todoItem.appendChild(todoDelBtn);

    todoItem.addEventListener("click", () => {
      handleTodoItemClick(item.todoId);
    });

    if (item.todoDone) {
      todoItem.classList.add("done");
    } else {
      todoItem.classList.add("undone");
    }

    todoDelBtn.addEventListener("click", () => {
      handleTodoDelBtnClick(item.todoId);
    });
  });
}

// 할일 추가
todoForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const toBeAdded = {
    todoText: todoForm.todo.value,
    todoId: new Date().getTime(),
    todoDone: false,
  };
  todoForm.todo.value = "";
  todoArr.push(toBeAdded);
  displayTodos();
  saveTodos();
});
