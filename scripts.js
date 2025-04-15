document.addEventListener("DOMContentLoaded", () => {
    const tg = window.Telegram.WebApp;
    tg.expand();

    const form = document.getElementById("task-form");
    form.addEventListener("submit", (e) => {
        e.preventDefault();
        const data = {
            specialist: document.getElementById("specialist").value,
            module: document.getElementById("module").value,
            description: document.getElementById("description").value,
            priority: document.getElementById("priority").value,
            department: document.getElementById("department").value,
            deadline: document.getElementById("deadline").value,
            created_by: tg.initDataUnsafe.user.username || tg.initDataUnsafe.user.first_name
        };
        tg.sendData(JSON.stringify(data));
        tg.close();
    });
});
