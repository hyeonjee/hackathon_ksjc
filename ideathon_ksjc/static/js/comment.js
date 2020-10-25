$(function() {
    $('.create-comment-button').on("click", function(e) {
        e.preventDefault();  //sumit stop
        contentData = $(this).data('content-object'); // response.html submit 버튼에서 data 설정 해줌
        contentIdentity = $(this).data('content-identity'); // response.html submit 버튼에서 data 설정 해줌
        csrfToken = $(this).data('token');
        message = $(`#comment-input-${contentIdentity}`).val();

        // window.contentData = contentData;   // 이거는 브라우져 콘솔에서 입력해서 확인할 수 있게 해줌
        $.ajax({
            type: "POST",
            url: `/contents/${contentIdentity}/create_comment/`,
            data: {
                'csrfmiddlewaretoken': csrfToken,
                'content': contentData,
                'message': message,
            },
            success: function (response) {
                //window.location.reload();
                const { content, message } = response;
                $('.comment-list').append(`
                    <li>\
                        ${message}\
                    </li>\
                `);
                $(`#comment-input-${contentIdentity}`).val('');
                //console.log("success ajax");
                //ajax를 사용해서 api 통신을 시도했으나, 외부로 빼는 것에 실패했다는 의미로 받아들임.
                //console.log("response data", response);

            }
        });
    })
})

