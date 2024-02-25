const loadMoreBtn = document.querySelector("#portfolio__cta");
const projectsList = document.querySelector(".portfolio__list");
const projectsInfo = document.querySelector(".project__info");

let visibleProjects = 4;
const handleGetProjects = () => {
    $.ajax({
        url: `/portfolio/portfolio-json/${visibleProjects}/`,
        type: 'GET',
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        },
        dataType: 'json',
        success: (response) => {
            max_size = response.max;
            min_size = response.min
            const data = response.data;
            data.map(project => {
            const newPost = document.createElement('li');
            newPost.classList.add('portfolio__card');
            newPost.innerHTML = `
                <a href="${project.slug}">
                    <div class="portfolio__image-container">
                        <img src="../../../media/${project.cover}" alt="photo: Super project" class="portfolio__image">
                    </div>
                    <h3 class="portfolio__title">${project.name}</h3>
                </a>
            `;

            projectsList.appendChild(newPost);

            setTimeout(() => {
                    newPost.classList.add('appear');
                    loadMoreBtn.classList.add("is-visible");
                }, 10);
            });
            if (max_size){
                loadMoreBtn.classList.add("not-visible");
            }
            if (min_size === 0){
                projectsInfo.classList.add("is-visible");
            }
        },
        error: (error) => {
            console.log(error);
        }
    });
}
handleGetProjects();
loadMoreBtn.addEventListener('click', () => {
    visibleProjects += 4
    handleGetProjects();
});