const pagination = () => {
  //初期設定
  let page = 1; //今何ページにいるか
  const STEP = 5; //ステップ数（１ページに表示する項目数）
  //全ページ数 channelsリストの総数/ステップ数のあまりの有無で場合分け
  //余りがある場合はページを1つ余分に追加する
  const TOTAL =
    channels.length % STEP == 0
      //余りがない場合
      ? channels.length / STEP
      //余りがある場合
      : Math.ceil(channels.length / STEP) ;

  //<ul class="pagination"></ul>の中身(li)を書き換える
  const paginationUl = document.querySelector(".pagination");
  let pageCount = 0;
  while (pageCount < TOTAL) {
    let li = document.createElement("li");
    li.innerText = pageCount + 1;
    paginationUl.appendChild(li);
    pageCount++;
  };

  //<ul class="channel-box"></ul>の中身<li>を書き換える
  const show = (page, STEP) => {
    const ul = document.querySelector(".channel-box");
    //一度リストを空にする
    ul.innerHTML = "";

    const first = (page - 1) * STEP + 1;
    const last = page * STEP;
    console.log(uid);
    channels.forEach((item, i) => {
      if (i < first - 1 || i > last - 1) return;
      const a = document.createElement("a");
      const li = document.createElement("li");
      const url = `/detail/${item.id}`;
      a.innerText = item.name;
      a.setAttribute("href", url);
      li.appendChild(a);
      //サンプルの削除ボタンはchat画面にて表示のため未定義
      ul.appendChild(li);
    });
  };//const show 閉じタグ

  //pagination内で現在選択されているページの番号に色を付ける
  const colorPaginationNum = () => {
    //<ul class="paination"></ul>内の<li></li>を全て取得し、配列に入れる
    //ループさせて一度全ての<li></li>からclass="colored"を削除
    const paginationArr = [...document.querySelectorAll(".pagination li")];
    paginationArr.forEach((page) => {
      page.classList.remove("colored");
    });
    //選択されているページにclass="colored"を追加（背景色が変わる）
    paginationArr[page - 1].classList.add("colored");
  };//const colorPaginationNum閉じタグ

  //最初に１ページ目を表示
  show(page, STEP);

  //前ページ遷移
  document.querySelector("#prev").addEventListener("click", () => {
    if (page <= 1) return;
    page = page - 1;
    show(page, STEP);
    colorPaginationNum();
  });

  //次ページ遷移
  document.querySelector("#next").addEventListener("click", () => {
    if (page >= channels.length / STEP) return;
    page = page + 1;
    show(page, STEP);
    colorPaginationNum();
  });
};//const pagination閉じタグ

window.onload = () => {
  pagination();
};