<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">
                <img src="https://getbootstrap.com/docs/5.0/assets/brand/bootstrap-logo.svg" alt="" width="30" height="24"
                    class="d-inline-block align-text-top">
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent" style="justify-content: center; padding-right: 60px;">
                <ul class="navbar-nav mb-2 mb-lg-0">
                    <li class="nav-item nav-link">
                        <router-link to="/">Home</router-link>
                    </li>
                    <li class="nav-item nav-link">
                        <router-link to="/about">About</router-link>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>