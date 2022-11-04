  // 좋아요 비동기
  const likeBtn = document.querySelector('#like-btn')
  likeBtn.addEventListener('click', function(event) {
    console.log('됩니다')
    axios({
      method: 'post',
      url: `/bars/${event.target.dataset.restaurantId}/restaurant_like/`,
    })
    .then(response => {
      if (response.data.isLiked === true) {
        event.target.classList.add('bi-heart-fill')
        event.target.classList.remove('bi-heart')
      } else {
        event.target.classList.add('bi-heart')
        event.target.classList.remove('bi-heart-fill')
      }
      const likeCount = document.querySelector('#like-count')
      likeCount.innerText = response.data.likeCount
    })
  })
