// モーダルを表示させる
const addChannelModal = document.querySelector("#add-channel-modal");
const deleteChannelModal = document.querySelector("#delete-channel-modal");

const addPageButtonClose = document.querySelector("#add-page-close-btn");
const deletePageButtonClose = document.querySelector("#delete-page-close-btn");

const addChannelBtn = document.querySelector("#add-channel-btn");

const addChannelConfirmBtn = document.querySelector("#add-channel-confirmation-btn");
const deleteChannelConfirmBtn = document.querySelector("#delete-channel-confirmation-btn");

// モーダルを開く
// <button id="add-channel-btn">チャンネル追加</button>ボタンがクリックされた時
addChannelBtn.addEventListener("click", () => {
  modalOpen("add");
});

function modalOpen(mode) {
  if (mode === "add") {
    addChannelModal.style.display = "block";
  } else if (mode === "delete") {
    deleteChannelModal.style.display = "block";
  } else if (mode === "update") {
    updateChannelModal.style.display = "block";
  }
}

// モーダル内のバツ印がクリックされた時
addPageButtonClose.addEventListener("click", () => {
  modalClose("add");
});
deletePageButtonClose.addEventListener("click", () => {
  modalClose("delete");
});

function modalClose(mode) {
  if (mode === "add") {
    addChannelModal.style.display = "none";
  } else if (mode === "delete") {
    deleteChannelModal.style.display = "none";
  } else if (mode === "update") {
    updateChannelModal.style.display = "none";
  }
}

// モーダルコンテンツ以外がクリックされた時
addEventListener("click", outsideClose);
function outsideClose(e) {
  if (e.target == addChannelModal) {
    addChannelModal.style.display = "none";
  } else if (e.target == deleteChannelModal) {
    deleteChannelModal.style.display = "none";
  }
}