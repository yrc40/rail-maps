<template>
  <header id="main-header" class="main-header main-header-large">
    <div class="main-header-perspective">
    <div class="main-header-front">
    <h1><span>0801 Test</span></h1>
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> |
      <router-link to="/test">Test</router-link>
    </nav>
    </div>
    </div>
  </header>
  <router-view/>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}

.main-header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  padding: 0;
  z-index: 50;
  -webkit-transform: translateY(0%);
  -moz-transform: translateY(0%);
  transform: translateY(0%);
  -webkit-transition: all 0.5s;
  -moz-transition: all 0.5s;
  transition: all 0.5s;
}

.main-header-perspective {
  width: 100%;
  height: 100%;
  position: relative;
  -webkit-perspective: 1000px;
  -moz-perspective: 1000px;
  perspective: 1000px;
  -webkit-perspective-origin: 50% 0;
  -moz-perspective-origin: 50% 0;
  perspective-origin: 50% 0;
}

.main-header-perspective > div {
  background: #fff;
  text-align: left;
  padding: 0 7%;
  height: 50%;
width: 100%;
margin: 0 auto;
position: relative;
text-align: justify;
-webkit-backface-visibility: hidden;
-moz-backface-visibility: hidden;
backface-visibility: hidden;
-webkit-transition: all 0.5s;
-moz-transition: all 0.5s;
transition: all 0.5s;
overflow: hidden;
}

.main-header-front {
z-index: 2;
-webkit-transform-origin: 50% 100%;
-moz-transform-origin: 50% 100%;
transform-origin: 50% 100%;
}

/* Justify inline-block elements (h1 on left side, nav on right) */
.mian-header-perspective > div::after {
  content: '';
  display: inline-block;
  width: 100%;
}

.main-header h1,
.main-header h1::before,
.main-header h1 span,
.main-header nav,
.main-header nav::before {
display: inline-block;
vertical-align: middle;
text-align: left;
}

.main-header h1 {
font-weight: 300;
font-size: 3.0em;
margin: 0;
padding: 0 1em 0 0;
color: #2d383f;
cursor: default;
height: 100%;
z-index: 1;
-webkit-transition: all 0.5s;
-moz-transition: all 0.5s;
transition: all 0.5s;
}

.main-header h1::before,
.main-header nav::before {
content: '';
height: 100%;
}

.main-header h1::after {
content: '';
width: 100px;
height: 96px;
background: #fff;
position: absolute;
z-index: 100;
top: 0;
left: 0;
cursor: pointer;
box-shadow: inset 0 8px #2d383f, inset 0 16px #fff, inset 0 24px #2d383f, inset 0 32px #fff, inset 0 40px #2d383f, inset 0 48px #fff, inset 0 56px #2d383f;
opacity: 0;
border: 20px solid #fff;
-webkit-transition: opacity 0.5s;
-moz-transition: opacity 0.5s;
transition: opacity 0.5s;
}

.main-header nav {
height: 100%;
}

// nav 標題字
.main-header nav a {
display: inline-block;
text-transform: uppercase;
letter-spacing: 1px;
font-weight: 700;
padding: 0.2em 0.4em;
margin: 0.2em 0.4em 0;
font-size: 0.8em;
cursor: pointer;
color: #42b983;
outline: none;
text-decoration: none;
}

.main-header nav a:hover {
color: #2c3e50;
}

.main-header nav a:last-child {
    margin-right: 0;
}

/*.main-header .main-header-front nav a:first-child,
.main-header .main-header-front nav a:last-child {
border: 2px solid #42b983;
}*/

/*.main-header .main-header-front nav a:first-child:hover,
.main-header .main-header-front nav a:last-child:hover {
border: 2px solid #2c3e50;
}*/
</style>
