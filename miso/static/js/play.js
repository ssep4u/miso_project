var quiz = 'ㅁㅅ'
var letters = []

window.onload = function() {
  $('#inputWord').attr("placeholder",quiz)
}
function play() {
    //입력한 값 가져오자
    var word = $('#inputWord').val()

    //글자수 세자
    //  원하는게 아니면 나가자
    if (word.length != quiz.length) {
      $('#result').html("incorrect")
      return
    }

    //String을 글자 배열로 자르자
    letters = word.split('')
    var correct = 0
    for (var i = 0; i < quiz.length; i++) {
        console.log(quiz[i] + " : " + word[i])
        if (isJaeumToLetter(quiz[i], letters[i])) {
            //자음에 맞는 단어인지 확인하자
            correct++
        }
    }

    if (correct == quiz.length) {
        //  맞으면 서버에 보내자
        //  다르면 다시 원래대로
        //값 초기화
        $('#result').html("correct "+new Date().toLocaleString('ko-KR'))
    } else {
      $('#result').html("incorrect")
    }
}

function isJaeumToLetter(jaeum, letter) {
    //자음에 맞는 단어인지 확인
    switch (jaeum) {
        case 'ㄱ':
            if ('가' <= letter && letter <= '깋') {
                return true
            }
            break
        case 'ㄴ':
            if ('나' <= letter && letter <= '닣') {
                return true
            }
            break
        case 'ㄷ':
            if ('다' <= letter && letter <= '딯') {
                return true
            }
            break
        case 'ㄹ':
            if ('라' <= letter && letter <= '맇') {
                return true
            }
            break
        case 'ㅁ':
            if ('마' <= letter && letter <= '밓') {
                return true
            }
            break
        case 'ㅂ':
            if ('바' <= letter && letter <= '빟') {
                return true
            }
            break
        case 'ㅅ':
            if ('사' <= letter && letter <= '싷') {
                return true
            }
            break
        case 'ㅇ':
            if ('아' <= letter && letter <= '잏') {
                return true
            }
            break
        case 'ㅈ':
            if ('자' <= letter && letter <= '짛') {
                return true
            }
            break
        case 'ㅊ':
            if ('차' <= letter && letter <= '칳') {
                return true
            }
            break
        case 'ㅋ':
            if ('카' <= letter && letter <= '킿') {
                return true
            }
            break
        case 'ㅌ':
            if ('타' <= letter && letter <= '팋') {
                return true
            }
            break
        case 'ㅍ':
            if ('파' <= letter && letter <= '핗') {
                return true
            }
            break
        case 'ㅎ':
            if ('하' <= letter && letter <= '힣') {
                return true
            }
            break

        default:
            break
    }

    return false
}
