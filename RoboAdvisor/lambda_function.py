<!DOCTYPE html>
<html class="" lang="en">
<head prefix="og: http://ogp.me/ns#">
<meta charset="utf-8">
<link as="style" href="https://uwa.bootcampcontent.com/assets/application-bf1ba5d5d3395adc5bad6f17cc3cb21b3fb29d3e3471a5b260e0bc5ec7a57bc4.css" rel="preload">
<link as="style" href="https://uwa.bootcampcontent.com/assets/highlight/themes/white-0678dba52a34ddc3b009cf294c54cfbddb9bac5991d6377ab811afe156e5a0cb.css" rel="preload">
<link as="font" href="https://uwa.bootcampcontent.com/assets/fontawesome-webfont-2adefcbc041e7d18fcf2d417879dc5a09997aa64d675b7a3c4b6ce33da13f3fe.woff2?v=4.7.0" rel="preload" type="font/woff2">

<meta content="IE=edge" http-equiv="X-UA-Compatible">

<meta content="object" property="og:type">
<meta content="GitLab" property="og:site_name">
<meta content="13-AWS-Cloud/Homework/Instructions/Starter_Files/lambda_function.py · master · UWA-Bootcamp / UW-BLV-FIN-PT-11-2020-U-C" property="og:title">
<meta content="GitLab Community Edition" property="og:description">
<meta content="https://uwa.bootcampcontent.com/assets/gitlab_logo-7ae504fe4f68fdebb3c2034e36621930cd36ea87924c11ff65dbcb8ed50dca58.png" property="og:image">
<meta content="64" property="og:image:width">
<meta content="64" property="og:image:height">
<meta content="https://uwa.bootcampcontent.com/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/blob/master/13-AWS-Cloud/Homework/Instructions/Starter_Files/lambda_function.py" property="og:url">
<meta content="summary" property="twitter:card">
<meta content="13-AWS-Cloud/Homework/Instructions/Starter_Files/lambda_function.py · master · UWA-Bootcamp / UW-BLV-FIN-PT-11-2020-U-C" property="twitter:title">
<meta content="GitLab Community Edition" property="twitter:description">
<meta content="https://uwa.bootcampcontent.com/assets/gitlab_logo-7ae504fe4f68fdebb3c2034e36621930cd36ea87924c11ff65dbcb8ed50dca58.png" property="twitter:image">

<title>13-AWS-Cloud/Homework/Instructions/Starter_Files/lambda_function.py · master · UWA-Bootcamp / UW-BLV-FIN-PT-11-2020-U-C · GitLab</title>
<meta content="GitLab Community Edition" name="description">
<link rel="shortcut icon" type="image/png" href="/assets/favicon-7901bd695fb93edb07975966062049829afb56cf11511236e61bcf425070e36e.png" id="favicon" data-original-href="/assets/favicon-7901bd695fb93edb07975966062049829afb56cf11511236e61bcf425070e36e.png" />

<link rel="stylesheet" media="all" href="/assets/application-bf1ba5d5d3395adc5bad6f17cc3cb21b3fb29d3e3471a5b260e0bc5ec7a57bc4.css" />

<link rel="stylesheet" media="all" href="/assets/application_utilities-4a0a7fb4b050255fc637b897e541f513df1cdf23cb1518fabc4323f2d0b78866.css" />
<link rel="stylesheet" media="all" href="/assets/themes/theme_indigo-1e3c170ae7fd24d137960957cba8221abf63a78f8b108e77f131b0fed6a659c7.css" />

<link rel="stylesheet" media="all" href="/assets/highlight/themes/white-0678dba52a34ddc3b009cf294c54cfbddb9bac5991d6377ab811afe156e5a0cb.css" />


<script>
//<![CDATA[
window.gon={};gon.api_version="v4";gon.default_avatar_url="https://uwa.bootcampcontent.com/assets/no_avatar-849f9c04a3a0d0cea2424ae97b27447dc64a7dbfae83c036c45b403392f0e8ba.png";gon.max_file_size=10;gon.asset_host=null;gon.webpack_public_path="/assets/webpack/";gon.relative_url_root="";gon.shortcuts_path="/help/shortcuts";gon.user_color_scheme="white";gon.gitlab_url="https://uwa.bootcampcontent.com";gon.revision="eaa194f15e6";gon.gitlab_logo="/assets/gitlab_logo-7ae504fe4f68fdebb3c2034e36621930cd36ea87924c11ff65dbcb8ed50dca58.png";gon.sprite_icons="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg";gon.sprite_file_icons="/assets/file_icons-c13caf2f3ca00cc2c02b11d373ac288c200b9b4dcddbb52a5027dc07b3eece19.svg";gon.emoji_sprites_css_path="/assets/emoji_sprites-289eccffb1183c188b630297431be837765d9ff4aed6130cf738586fb307c170.css";gon.test_env=false;gon.disable_animations=null;gon.suggested_label_colors={"#0033CC":"UA blue","#428BCA":"Moderate blue","#44AD8E":"Lime green","#A8D695":"Feijoa","#5CB85C":"Slightly desaturated green","#69D100":"Bright green","#004E00":"Very dark lime green","#34495E":"Very dark desaturated blue","#7F8C8D":"Dark grayish cyan","#A295D6":"Slightly desaturated blue","#5843AD":"Dark moderate blue","#8E44AD":"Dark moderate violet","#FFECDB":"Very pale orange","#AD4363":"Dark moderate pink","#D10069":"Strong pink","#CC0033":"Strong red","#FF0000":"Pure red","#D9534F":"Soft red","#D1D100":"Strong yellow","#F0AD4E":"Soft orange","#AD8D43":"Dark moderate orange"};gon.first_day_of_week=0;gon.ee=false;gon.current_user_id=1365;gon.current_username="nospmah";gon.current_user_fullname="Brian Hampson";gon.current_user_avatar_url="https://secure.gravatar.com/avatar/3c5baba6ee99fee9883e223b78a7b038?s=80\u0026d=identicon";gon.features={"webperfExperiment":false,"snippetsBinaryBlob":false,"usageDataApi":true,"securityAutoFix":false,"startupCss":false,"gitlabCiYmlPreview":false};gon.experiments={"suggestPipeline":false};
//]]>
</script>



<script src="/assets/webpack/runtime.8fce4aa0.bundle.js" defer="defer"></script>
<script src="/assets/webpack/main.e89d0618.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-globalSearch-pages.admin.abuse_reports-pages.admin.groups.show-pages.admin.projects-pages.ad-c08b40ef.a8bba176.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.groups.boards-pages.groups.details-pages.groups.show-pages.projects-pages.projects.act-5eeff683.eaa04149.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.admin.application_settings-pages.admin.application_settings.general-pages.admin.applic-5753b007.27b564d8.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.groups.milestones.edit-pages.groups.milestones.new-pages.projects.blame.show-pages.pro-77e8c306.37c1e60d.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects.blame.show-pages.projects.blob.edit-pages.projects.blob.new-pages.projects.bl-c6edf1dd.8ca8706d.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.shared.web_ide_link-pages.projects.show-pages.projec-cf300cc3.f4db049e.chunk.js" defer="defer"></script>
<script src="/assets/webpack/pages.projects.blob.show.d06c9cb3.chunk.js" defer="defer"></script>

<script>
//<![CDATA[
window.uploads_path = "/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/uploads";



//]]>
</script>
<meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="CTCsocQt8Au8sYTaRPAWrnnzDRcCw7aZMa/2PZgxrPJWjRwWUFkXo+j3iz+9yOLopwzbO1cAEtaK3RaTtKCjeA==" />
<meta name="csp-nonce" />
<meta name="action-cable-url" content="/-/cable" />
<meta content="width=device-width, initial-scale=1, maximum-scale=1" name="viewport">
<meta content="#474D57" name="theme-color">
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/touch-icon-iphone-5a9cee0e8a51212e70b90c87c12f382c428870c0ff67d1eb034d884b78d2dae7.png" />
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/touch-icon-ipad-a6eec6aeb9da138e507593b464fdac213047e49d3093fc30e90d9a995df83ba3.png" sizes="76x76" />
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/touch-icon-iphone-retina-72e2aadf86513a56e050e7f0f2355deaa19cc17ed97bbe5147847f2748e5a3e3.png" sizes="120x120" />
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/touch-icon-ipad-retina-8ebe416f5313483d9c1bc772b5bbe03ecad52a54eba443e5215a22caed2a16a2.png" sizes="152x152" />
<link color="rgb(226, 67, 41)" href="/assets/logo-d36b5212042cebc89b96df4bf6ac24e43db316143e89926c0db839ff694d2de4.svg" rel="mask-icon">
<meta content="/assets/msapplication-tile-1196ec67452f618d39cdd85e2e3a542f76574c071051ae7effbfde01710eb17d.png" name="msapplication-TileImage">
<meta content="#30353E" name="msapplication-TileColor">




</head>

<body class="ui-indigo tab-width-8  gl-browser-edge gl-platform-windows" data-find-file="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/find_file/master" data-group="UWA-Bootcamp" data-namespace-id="3" data-page="projects:blob:show" data-page-type-id="master/13-AWS-Cloud/Homework/Instructions/Starter_Files/lambda_function.py" data-project="uw-blv-fin-pt-11-2020-u-c" data-project-id="190">

<script>
//<![CDATA[
gl = window.gl || {};
gl.client = {"isEdge":true,"isWindows":true};


//]]>
</script>


<header class="navbar navbar-gitlab navbar-expand-sm js-navbar" data-qa-selector="navbar">
<a class="sr-only gl-accessibility" href="#content-body" tabindex="1">Skip to content</a>
<div class="container-fluid">
<div class="header-content">
<div class="title-container">
<h1 class="title">
<span class="gl-sr-only">GitLab</span>
<a title="Dashboard" id="logo" href="/"><svg width="24" height="24" class="tanuki-logo" viewBox="0 0 36 36">
  <path class="tanuki-shape tanuki-left-ear" fill="#e24329" d="M2 14l9.38 9v-9l-4-12.28c-.205-.632-1.176-.632-1.38 0z"/>
  <path class="tanuki-shape tanuki-right-ear" fill="#e24329" d="M34 14l-9.38 9v-9l4-12.28c.205-.632 1.176-.632 1.38 0z"/>
  <path class="tanuki-shape tanuki-nose" fill="#e24329" d="M18,34.38 3,14 33,14 Z"/>
  <path class="tanuki-shape tanuki-left-eye" fill="#fc6d26" d="M18,34.38 11.38,14 2,14 6,25Z"/>
  <path class="tanuki-shape tanuki-right-eye" fill="#fc6d26" d="M18,34.38 24.62,14 34,14 30,25Z"/>
  <path class="tanuki-shape tanuki-left-cheek" fill="#fca326" d="M2 14L.1 20.16c-.18.565 0 1.2.5 1.56l17.42 12.66z"/>
  <path class="tanuki-shape tanuki-right-cheek" fill="#fca326" d="M34 14l1.9 6.16c.18.565 0 1.2-.5 1.56L18 34.38z"/>
</svg>

<span class="logo-text d-none d-lg-block gl-ml-3">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 617 169"><path d="M315.26 2.97h-21.8l.1 162.5h88.3v-20.1h-66.5l-.1-142.4M465.89 136.95c-5.5 5.7-14.6 11.4-27 11.4-16.6 0-23.3-8.2-23.3-18.9 0-16.1 11.2-23.8 35-23.8 4.5 0 11.7.5 15.4 1.2v30.1h-.1m-22.6-98.5c-17.6 0-33.8 6.2-46.4 16.7l7.7 13.4c8.9-5.2 19.8-10.4 35.5-10.4 17.9 0 25.8 9.2 25.8 24.6v7.9c-3.5-.7-10.7-1.2-15.1-1.2-38.2 0-57.6 13.4-57.6 41.4 0 25.1 15.4 37.7 38.7 37.7 15.7 0 30.8-7.2 36-18.9l4 15.9h15.4v-83.2c-.1-26.3-11.5-43.9-44-43.9M557.63 149.1c-8.2 0-15.4-1-20.8-3.5V70.5c7.4-6.2 16.6-10.7 28.3-10.7 21.1 0 29.2 14.9 29.2 39 0 34.2-13.1 50.3-36.7 50.3m9.2-110.6c-19.5 0-30 13.3-30 13.3v-21l-.1-27.8h-21.3l.1 158.5c10.7 4.5 25.3 6.9 41.2 6.9 40.7 0 60.3-26 60.3-70.9-.1-35.5-18.2-59-50.2-59M77.9 20.6c19.3 0 31.8 6.4 39.9 12.9l9.4-16.3C114.5 6 97.3 0 78.9 0 32.5 0 0 28.3 0 85.4c0 59.8 35.1 83.1 75.2 83.1 20.1 0 37.2-4.7 48.4-9.4l-.5-63.9V75.1H63.6v20.1h38l.5 48.5c-5 2.5-13.6 4.5-25.3 4.5-32.2 0-53.8-20.3-53.8-63-.1-43.5 22.2-64.6 54.9-64.6M231.43 2.95h-21.3l.1 27.3v94.3c0 26.3 11.4 43.9 43.9 43.9 4.5 0 8.9-.4 13.1-1.2v-19.1c-3.1.5-6.4.7-9.9.7-17.9 0-25.8-9.2-25.8-24.6v-65h35.7v-17.8h-35.7l-.1-38.5M155.96 165.47h21.3v-124h-21.3v124M155.96 24.37h21.3V3.07h-21.3v21.3"/></svg>

</span>
</a></h1>
<ul class="list-unstyled navbar-sub-nav">
<li id="nav-projects-dropdown" class="home dropdown header-projects qa-projects-dropdown" data-track-label="projects_dropdown" data-track-event="click_dropdown" data-track-value=""><button data-toggle="dropdown" type="button">
Projects
<svg class="s16 caret-down" data-testid="chevron-down-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#chevron-down"></use></svg>
</button>
<div class="dropdown-menu frequent-items-dropdown-menu">
<div class="frequent-items-dropdown-container">
<div class="frequent-items-dropdown-sidebar qa-projects-dropdown-sidebar">
<ul>
<li class=""><a class="qa-your-projects-link" href="/dashboard/projects">Your projects
</a></li><li class=""><a href="/dashboard/projects/starred">Starred projects
</a></li><li class=""><a href="/explore">Explore projects
</a></li></ul>
</div>
<div class="frequent-items-dropdown-content">
<div data-project-id="190" data-project-name="UW-BLV-FIN-PT-11-2020-U-C" data-project-namespace="UWA-Bootcamp / UW-BLV-FIN-PT-11-2020-U-C" data-project-web-url="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c" data-user-name="nospmah" id="js-projects-dropdown"></div>
</div>
</div>

</div>
</li><li id="nav-groups-dropdown" class="d-none d-md-block home dropdown header-groups qa-groups-dropdown" data-track-label="groups_dropdown" data-track-event="click_dropdown" data-track-value=""><button data-toggle="dropdown" type="button">
Groups
<svg class="s16 caret-down" data-testid="chevron-down-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#chevron-down"></use></svg>
</button>
<div class="dropdown-menu frequent-items-dropdown-menu">
<div class="frequent-items-dropdown-container">
<div class="frequent-items-dropdown-sidebar qa-groups-dropdown-sidebar">
<ul>
<li class=""><a class="qa-your-groups-link" href="/dashboard/groups">Your groups
</a></li><li class=""><a href="/explore/groups">Explore groups
</a></li></ul>
</div>
<div class="frequent-items-dropdown-content">
<div data-user-name="nospmah" id="js-groups-dropdown"></div>
</div>
</div>

</div>
</li><li class="header-more dropdown">
<a data-qa-selector="more_dropdown" data-toggle="dropdown" href="#">
More
<svg class="s16 caret-down" data-testid="chevron-down-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#chevron-down"></use></svg>
</a>
<div class="dropdown-menu">
<ul>
<li class="d-md-none">
<a class="dashboard-shortcuts-groups" data-qa-selector="groups_link" href="/dashboard/groups">Groups
</a></li>
<li class=""><a class="dashboard-shortcuts-activity" data-qa-selector="activity_link" href="/dashboard/activity">Activity
</a></li><li class=""><a class="dashboard-shortcuts-milestones" data-qa-selector="milestones_link" href="/dashboard/milestones">Milestones
</a></li><li class=""><a class="dashboard-shortcuts-snippets" data-qa-selector="snippets_link" href="/dashboard/snippets">Snippets
</a></li><li class="dropdown">

</li>
</ul>
</div>
</li>
<li class="hidden">
<a class="dashboard-shortcuts-projects" href="/dashboard/projects">Projects
</a></li>

</ul>

</div>
<div class="navbar-collapse collapse">
<ul class="nav navbar-nav">
<li class="header-new dropdown" data-track-event="click_dropdown" data-track-label="new_dropdown" data-track-value="">
<a class="header-new-dropdown-toggle has-tooltip qa-new-menu-toggle" id="js-onboarding-new-project-link" title="New..." ref="tooltip" aria-label="New..." data-toggle="dropdown" data-placement="bottom" data-container="body" data-display="static" href="/projects/new"><svg class="s16" data-testid="plus-square-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#plus-square"></use></svg>
<svg class="s16 caret-down" data-testid="chevron-down-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#chevron-down"></use></svg>
</a><div class="dropdown-menu dropdown-menu-right">
<ul>
<li class="dropdown-bold-header">
This project
</li>
<li><a href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/issues/new">New issue</a></li>
<li><a href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/snippets/new">New snippet</a></li>
<li class="divider"></li>
<li class="dropdown-bold-header">GitLab</li>
<li><a class="qa-global-new-project-link" href="/projects/new">New project</a></li>
<li><a href="/groups/new">New group</a></li>
<li><a class="qa-global-new-snippet-link" href="/-/snippets/new">New snippet</a></li>
</ul>
</div>
</li>

<li class="nav-item d-none d-lg-block m-auto">
<div class="search search-form" data-track-event="activate_form_input" data-track-label="navbar_search" data-track-value="">
<form class="form-inline" action="/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" /><div class="search-input-container">
<div class="search-input-wrap">
<div class="dropdown" data-url="/search/autocomplete">
<input type="search" name="search" id="search" placeholder="Search or jump to…" class="search-input dropdown-menu-toggle no-outline js-search-dashboard-options" spellcheck="false" tabindex="1" autocomplete="off" data-issues-path="/dashboard/issues" data-mr-path="/dashboard/merge_requests" data-qa-selector="search_term_field" aria-label="Search or jump to…" />
<button class="hidden js-dropdown-search-toggle" data-toggle="dropdown" type="button"></button>
<div class="dropdown-menu dropdown-select js-dashboard-search-options">
<div class="dropdown-content"><ul>
<li class="dropdown-menu-empty-item">
<a>
Loading...
</a>
</li>
</ul>
</div><div class="dropdown-loading"><i aria-hidden="true" data-hidden="true" class="fa fa-spinner fa-spin"></i></div>
</div>
<svg class="s16 search-icon" data-testid="search-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#search"></use></svg>
<svg class="s16 clear-icon js-clear-input" data-testid="close-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#close"></use></svg>
</div>
</div>
</div>
<input type="hidden" name="group_id" id="group_id" value="3" class="js-search-group-options" data-group-path="UWA-Bootcamp" data-name="UWA-Bootcamp" data-issues-path="/groups/UWA-Bootcamp/-/issues" data-mr-path="/groups/UWA-Bootcamp/-/merge_requests" />
<input type="hidden" name="project_id" id="search_project_id" value="190" class="js-search-project-options" data-project-path="uw-blv-fin-pt-11-2020-u-c" data-name="UW-BLV-FIN-PT-11-2020-U-C" data-issues-path="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/issues" data-mr-path="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/merge_requests" data-issues-disabled="false" />
<input type="hidden" name="scope" id="scope" />
<input type="hidden" name="search_code" id="search_code" value="true" />
<input type="hidden" name="snippets" id="snippets" value="false" />
<input type="hidden" name="repository_ref" id="repository_ref" value="master" />
<input type="hidden" name="nav_source" id="nav_source" value="navbar" />
<div class="search-autocomplete-opts hide" data-autocomplete-path="/search/autocomplete" data-autocomplete-project-id="190" data-autocomplete-project-ref="master"></div>
</form></div>

</li>
<li class="nav-item d-inline-block d-lg-none">
<a title="Search" aria-label="Search" data-toggle="tooltip" data-placement="bottom" data-container="body" href="/search?project_id=190"><svg class="s16" data-testid="search-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#search"></use></svg>
</a></li>
<li class="user-counter"><a title="Issues" class="dashboard-shortcuts-issues" aria-label="Issues" data-qa-selector="issues_shortcut_button" data-toggle="tooltip" data-placement="bottom" data-track-label="main_navigation" data-track-event="click_issues_link" data-track-property="navigation" data-container="body" href="/dashboard/issues?assignee_username=nospmah"><svg class="s16" data-testid="issues-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#issues"></use></svg>
<span class="badge badge-pill green-badge hidden issues-count">
0
</span>
</a></li><li class="user-counter"><a title="Merge requests" class="dashboard-shortcuts-merge_requests" aria-label="Merge requests" data-qa-selector="merge_requests_shortcut_button" data-toggle="tooltip" data-placement="bottom" data-track-label="main_navigation" data-track-event="click_merge_link" data-track-property="navigation" data-container="body" href="/dashboard/merge_requests?assignee_username=nospmah"><svg class="s16" data-testid="git-merge-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#git-merge"></use></svg>
<span class="badge badge-pill hidden merge-requests-count">
0
</span>
</a></li><li class="user-counter"><a title="To-Do List" aria-label="To-Do List" class="shortcuts-todos" data-qa-selector="todos_shortcut_button" data-toggle="tooltip" data-placement="bottom" data-track-label="main_navigation" data-track-event="click_to_do_link" data-track-property="navigation" data-container="body" href="/dashboard/todos"><svg class="s16" data-testid="todo-done-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#todo-done"></use></svg>
<span class="badge badge-pill hidden js-todos-count todos-count">
0
</span>
</a></li><li class="nav-item header-help dropdown d-none d-md-block">
<a class="header-help-dropdown-toggle" data-toggle="dropdown" href="/help"><span class="gl-sr-only">
Help
</span>
<svg class="s16" data-testid="question-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#question"></use></svg>
<svg class="s16 caret-down" data-testid="chevron-down-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#chevron-down"></use></svg>
</a><div class="dropdown-menu dropdown-menu-right">
<ul>

<li>
<a href="/help">Help</a>
</li>
<li>
<a href="https://about.gitlab.com/getting-help/">Support</a>
</li>
<li>
<a target="_blank" class="text-nowrap" rel="noopener noreferrer" data-track-event="click_forum" data-track-property="question_menu" href="https://forum.gitlab.com/">Community forum</a>

</li>
<li>
<button class="js-shortcuts-modal-trigger" type="button">
Keyboard shortcuts
<span aria-hidden class="text-secondary float-right">?</span>
</button>
</li>
<li class="divider"></li>
<li>
<a href="https://about.gitlab.com/submit-feedback">Submit feedback</a>
</li>
<li>
<a target="_blank" class="text-nowrap" href="https://about.gitlab.com/contributing">Contribute to GitLab
</a>
</li>

</ul>

</div>
</li>
<li class="dropdown header-user js-nav-user-dropdown nav-item" data-qa-selector="user_menu" data-track-event="click_dropdown" data-track-label="profile_dropdown" data-track-value="">
<a class="header-user-dropdown-toggle" data-toggle="dropdown" href="/nospmah"><img width="23" height="23" class="header-user-avatar qa-user-avatar lazy" alt="Brian Hampson" data-src="https://secure.gravatar.com/avatar/3c5baba6ee99fee9883e223b78a7b038?s=46&amp;d=identicon" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" />

<svg class="s16 caret-down" data-testid="chevron-down-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#chevron-down"></use></svg>
</a><div class="dropdown-menu dropdown-menu-right">
<ul>
<li class="current-user">
<div class="user-name bold">
Brian Hampson
</div>
@nospmah
</li>
<li class="divider"></li>
<li>
<button class="btn menu-item js-set-status-modal-trigger" type="button">
Set status
</button>
</li>
<li>
<a class="profile-link" data-user="nospmah" href="/nospmah">Profile</a>
</li>
<li>
<a data-qa-selector="settings_link" href="/profile">Settings</a>
</li>


<li class="divider d-md-none"></li>
<li class="d-md-none">
<a href="/help">Help</a>
</li>
<li class="d-md-none">
<a href="https://about.gitlab.com/getting-help/">Support</a>
</li>
<li class="d-md-none">
<a target="_blank" class="text-nowrap" rel="noopener noreferrer" data-track-event="click_forum" data-track-property="question_menu" href="https://forum.gitlab.com/">Community forum</a>

</li>
<li class="d-md-none">
<a href="https://about.gitlab.com/submit-feedback">Submit feedback</a>
</li>
<li class="d-md-none">
<a target="_blank" class="text-nowrap" href="https://about.gitlab.com/contributing">Contribute to GitLab
</a>
</li>

<li class="divider"></li>
<li>
<a class="sign-out-link" data-qa-selector="sign_out_link" rel="nofollow" data-method="post" href="/users/sign_out">Sign out</a>
</li>
</ul>

</div>
</li>
</ul>
</div>
<button class="navbar-toggler d-block d-sm-none" type="button">
<span class="sr-only">Toggle navigation</span>
<svg class="s12 more-icon js-navbar-toggle-right" data-testid="ellipsis_h-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#ellipsis_h"></use></svg>
<svg class="s12 close-icon js-navbar-toggle-left" data-testid="close-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#close"></use></svg>
</button>
</div>
</div>
</header>
<div class="js-set-status-modal-wrapper" data-current-emoji="" data-current-message=""></div>

<div class="layout-page page-with-contextual-sidebar">
<div class="nav-sidebar">
<div class="nav-sidebar-inner-scroll">
<div class="context-header">
<a title="UW-BLV-FIN-PT-11-2020-U-C" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c"><div class="avatar-container rect-avatar s40 project-avatar">
<div class="avatar s40 avatar-tile identicon bg2">U</div>
</div>
<div class="sidebar-context-title">
UW-BLV-FIN-PT-11-2020-U-C
</div>
</a></div>
<ul class="sidebar-top-level-items qa-project-sidebar">
<li class="home"><a class="shortcuts-project rspec-project-link" data-qa-selector="project_link" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c"><div class="nav-icon-container">
<svg class="s16" data-testid="home-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#home"></use></svg>
</div>
<span class="nav-item-name">
Project overview
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c"><strong class="fly-out-top-item-name">
Project overview
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="Project details" class="shortcuts-project" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c"><span>Details</span>
</a></li><li class=""><a title="Activity" class="shortcuts-project-activity" data-qa-selector="activity_link" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/activity"><span>Activity</span>
</a></li><li class=""><a title="Releases" class="shortcuts-project-releases" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/releases"><span>Releases</span>
</a></li></ul>
</li><li class="active"><a class="shortcuts-tree" data-qa-selector="repository_link" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/tree/master"><div class="nav-icon-container">
<svg class="s16" data-testid="doc-text-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#doc-text"></use></svg>
</div>
<span class="nav-item-name" id="js-onboarding-repo-link">
Repository
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item active"><a href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/tree/master"><strong class="fly-out-top-item-name">
Repository
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class="active"><a href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/tree/master">Files
</a></li><li class=""><a id="js-onboarding-commits-link" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/commits/master">Commits
</a></li><li class=""><a data-qa-selector="branches_link" id="js-onboarding-branches-link" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/branches">Branches
</a></li><li class=""><a data-qa-selector="tags_link" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/tags">Tags
</a></li><li class=""><a href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/graphs/master">Contributors
</a></li><li class=""><a href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/network/master">Graph
</a></li><li class=""><a href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/compare?from=master&amp;to=master">Compare
</a></li>
</ul>
</li><li class=""><a class="shortcuts-issues qa-issues-item" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/issues"><div class="nav-icon-container">
<svg class="s16" data-testid="issues-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#issues"></use></svg>
</div>
<span class="nav-item-name" id="js-onboarding-issues-link">
Issues
</span>
<span class="badge badge-pill count issue_counter">
0
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/issues"><strong class="fly-out-top-item-name">
Issues
</strong>
<span class="badge badge-pill count issue_counter fly-out-badge">
0
</span>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="Issues" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/issues"><span>
List
</span>
</a></li><li class=""><a title="Boards" data-qa-selector="issue_boards_link" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/boards"><span>
Boards
</span>
</a></li><li class=""><a title="Labels" class="qa-labels-link" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/labels"><span>
Labels
</span>
</a></li><li class=""><a title="Service Desk" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/issues/service_desk">Service Desk
</a></li>
<li class=""><a title="Milestones" class="qa-milestones-link" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/milestones"><span>
Milestones
</span>
</a></li>
</ul>
</li><li class=""><a class="shortcuts-merge_requests" data-qa-selector="merge_requests_link" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/merge_requests"><div class="nav-icon-container">
<svg class="s16" data-testid="git-merge-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#git-merge"></use></svg>
</div>
<span class="nav-item-name" id="js-onboarding-mr-link">
Merge Requests
</span>
<span class="badge badge-pill count merge_counter js-merge-counter">
0
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><a href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/merge_requests"><strong class="fly-out-top-item-name">
Merge Requests
</strong>
<span class="badge badge-pill count merge_counter js-merge-counter fly-out-badge">
0
</span>
</a></li></ul>
</li>
<li class=""><a class="shortcuts-pipelines qa-link-pipelines rspec-link-pipelines" data-qa-selector="ci_cd_link" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/pipelines"><div class="nav-icon-container">
<svg class="s16" data-testid="rocket-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#rocket"></use></svg>
</div>
<span class="nav-item-name" id="js-onboarding-pipelines-link">
CI / CD
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/pipelines"><strong class="fly-out-top-item-name">
CI / CD
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="Pipelines" class="shortcuts-pipelines" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/pipelines"><span>
Pipelines
</span>
</a></li><li class=""><a title="Jobs" class="shortcuts-builds" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/jobs"><span>
Jobs
</span>
</a></li><li class=""><a title="Schedules" class="shortcuts-builds" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/pipeline_schedules"><span>
Schedules
</span>
</a></li>
</ul>
</li>
<li class=""><a class="shortcuts-operations" data-qa-selector="operations_link" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/environments/metrics"><div class="nav-icon-container">
<svg class="s16" data-testid="cloud-gear-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#cloud-gear"></use></svg>
</div>
<span class="nav-item-name">
Operations
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/environments/metrics"><strong class="fly-out-top-item-name">
Operations
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="Metrics" class="shortcuts-metrics" data-qa-selector="operations_metrics_link" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/metrics"><span>
Metrics
</span>
</a></li>
<li class=""><a title="Error Tracking" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/error_tracking"><span>
Error Tracking
</span>
</a></li><li class=""><a title="Incidents" data-qa-selector="operations_incidents_link" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/incidents"><span>
Incidents
</span>
</a></li><li class=""><a title="Environments" class="shortcuts-environments qa-operations-environments-link" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/environments"><span>
Environments
</span>
</a></li></ul>
</li><li class=""><a data-qa-selector="packages_link" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/container_registry"><div class="nav-icon-container">
<svg class="s16" data-testid="package-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#package"></use></svg>
</div>
<span class="nav-item-name">
Packages &amp; Registries
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/container_registry"><strong class="fly-out-top-item-name">
Packages &amp; Registries
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a class="shortcuts-container-registry" title="Container Registry" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/container_registry"><span>Container Registry</span>
</a></li></ul>
</li>
<li class=""><a data-qa-selector="analytics_anchor" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/value_stream_analytics"><div class="nav-icon-container">
<svg class="s16" data-testid="chart-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#chart"></use></svg>
</div>
<span class="nav-item-name" data-qa-selector="analytics_link">
Analytics
</span>
</a><ul class="sidebar-sub-level-items" data-qa-selector="analytics_sidebar_submenu">
<li class="fly-out-top-item"><a href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/value_stream_analytics"><strong class="fly-out-top-item-name">
Analytics
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="CI / CD" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/pipelines/charts"><span>CI / CD</span>
</a></li><li class=""><a class="shortcuts-repository-charts" title="Repository" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/graphs/master/charts"><span>Repository</span>
</a></li><li class=""><a class="shortcuts-project-cycle-analytics" title="Value Stream" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/value_stream_analytics"><span>Value Stream</span>
</a></li></ul>
</li>
<li class=""><a class="shortcuts-wiki" data-qa-selector="wiki_link" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/wikis/home"><div class="nav-icon-container">
<svg class="s16" data-testid="book-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#book"></use></svg>
</div>
<span class="nav-item-name">
Wiki
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><a href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/wikis/home"><strong class="fly-out-top-item-name">
Wiki
</strong>
</a></li></ul>
</li>
<li class=""><a class="shortcuts-snippets" data-qa-selector="snippets_link" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/snippets"><div class="nav-icon-container">
<svg class="s16" data-testid="snippet-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#snippet"></use></svg>
</div>
<span class="nav-item-name">
Snippets
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><a href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/snippets"><strong class="fly-out-top-item-name">
Snippets
</strong>
</a></li></ul>
</li><li class=""><a title="Members" class="qa-members-link" id="js-onboarding-members-link" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/project_members"><div class="nav-icon-container">
<svg class="s16" data-testid="users-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#users"></use></svg>
</div>
<span class="nav-item-name">
Members
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><a href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/project_members"><strong class="fly-out-top-item-name">
Members
</strong>
</a></li></ul>
</li><a class="toggle-sidebar-button js-toggle-sidebar qa-toggle-sidebar rspec-toggle-sidebar" role="button" title="Toggle sidebar" type="button">
<svg class="s16 icon-chevron-double-lg-left" data-testid="chevron-double-lg-left-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#chevron-double-lg-left"></use></svg>
<svg class="s16 icon-chevron-double-lg-right" data-testid="chevron-double-lg-right-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#chevron-double-lg-right"></use></svg>
<span class="collapse-text">Collapse sidebar</span>
</a>
<button name="button" type="button" class="close-nav-button"><svg class="s16" data-testid="close-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#close"></use></svg>
<span class="collapse-text">Close sidebar</span>
</button>
<li class="hidden">
<a title="Activity" class="shortcuts-project-activity" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/activity"><span>
Activity
</span>
</a></li>
<li class="hidden">
<a title="Network" class="shortcuts-network" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/network/master">Graph
</a></li>
<li class="hidden">
<a class="shortcuts-new-issue" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/issues/new">Create a new issue
</a></li>
<li class="hidden">
<a title="Jobs" class="shortcuts-builds" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/jobs">Jobs
</a></li>
<li class="hidden">
<a title="Commits" class="shortcuts-commits" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/commits/master">Commits
</a></li>
<li class="hidden">
<a title="Issue Boards" class="shortcuts-issue-boards" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/boards">Issue Boards</a>
</li>
</ul>
</div>
</div>

<div class="content-wrapper">
<div class="mobile-overlay"></div>

<div class="alert-wrapper">













<nav class="breadcrumbs container-fluid container-limited" role="navigation">
<div class="breadcrumbs-container">
<button name="button" type="button" class="toggle-mobile-nav"><span class="sr-only">Open sidebar</span>
<svg class="s16" data-testid="hamburger-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#hamburger"></use></svg>
</button><div class="breadcrumbs-links js-title-container" data-qa-selector="breadcrumb_links_content">
<ul class="list-unstyled breadcrumbs-list js-breadcrumbs-list">
<li><a class="group-path breadcrumb-item-text js-breadcrumb-item-text " href="/UWA-Bootcamp">UWA-Bootcamp</a><svg class="s8 breadcrumbs-list-angle" data-testid="angle-right-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#angle-right"></use></svg></li> <li><a href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c"><span class="breadcrumb-item-text js-breadcrumb-item-text">UW-BLV-FIN-PT-11-2020-U-C</span></a><svg class="s8 breadcrumbs-list-angle" data-testid="angle-right-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#angle-right"></use></svg></li>

<li>
<h2 class="breadcrumbs-sub-title"><a href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/blob/master/13-AWS-Cloud/Homework/Instructions/Starter_Files/lambda_function.py">Repository</a></h2>
</li>
</ul>
</div>

</div>
</nav>

</div>
<div class="container-fluid container-limited ">
<div class="content" id="content-body">
<div class="flash-container flash-container-page sticky">
</div>

<div class="js-signature-container" data-signatures-path="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/commits/15a183b595b8db73e36248faab7a4720bcd3c087/signatures?limit=1"></div>

<div class="tree-holder" id="tree-holder">
<div class="nav-block">
<div class="tree-ref-container">
<div class="tree-ref-holder">
<form class="project-refs-form" action="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/refs/switch" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="destination" id="destination" value="blob" />
<input type="hidden" name="path" id="path" value="13-AWS-Cloud/Homework/Instructions/Starter_Files/lambda_function.py" />
<div class="dropdown">
<button class="dropdown-menu-toggle js-project-refs-dropdown qa-branches-select" type="button" data-toggle="dropdown" data-selected="master" data-ref="master" data-refs-url="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/refs?sort=updated_desc" data-field-name="ref" data-submit-form-on-click="true" data-visit="true"><span class="dropdown-toggle-text ">master</span><i aria-hidden="true" data-hidden="true" class="fa fa-chevron-down"></i></button>
<div class="dropdown-menu dropdown-menu-paging dropdown-menu-selectable git-revision-dropdown qa-branches-dropdown">
<div class="dropdown-page-one">
<div class="dropdown-title gl-display-flex"><span class="gl-ml-auto">Switch branch/tag</span><button class="dropdown-title-button dropdown-menu-close gl-ml-auto" aria-label="Close" type="button"><svg class="s16 dropdown-menu-close-icon" data-testid="close-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#close"></use></svg></button></div>
<div class="dropdown-input"><input type="search" id="" class="dropdown-input-field qa-dropdown-input-field" placeholder="Search branches and tags" autocomplete="off" /><svg class="s16 dropdown-input-search" data-testid="search-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#search"></use></svg><svg class="s16 dropdown-input-clear js-dropdown-input-clear" data-testid="close-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#close"></use></svg></div>
<div class="dropdown-content"></div>
<div class="dropdown-loading"><i aria-hidden="true" data-hidden="true" class="fa fa-spinner fa-spin"></i></div>
</div>
</div>
</div>
</form>
</div>
<ul class="breadcrumb repo-breadcrumb">
<li class="breadcrumb-item">
<a href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/tree/master">uw-blv-fin-pt-11-2020-u-c
</a></li>
<li class="breadcrumb-item">
<a href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/tree/master/13-AWS-Cloud">13-AWS-Cloud</a>
</li>
<li class="breadcrumb-item">
<a href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/tree/master/13-AWS-Cloud/Homework">Homework</a>
</li>
<li class="breadcrumb-item">
<a href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/tree/master/13-AWS-Cloud/Homework/Instructions">Instructions</a>
</li>
<li class="breadcrumb-item">
<a href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/tree/master/13-AWS-Cloud/Homework/Instructions/Starter_Files">Starter_Files</a>
</li>
<li class="breadcrumb-item">
<a href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/blob/master/13-AWS-Cloud/Homework/Instructions/Starter_Files/lambda_function.py"><strong>lambda_function.py</strong>
</a></li>
</ul>
</div>
<div class="tree-controls gl-children-ml-sm-3"><a class="btn shortcuts-find-file" rel="nofollow" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/find_file/master">Find file
</a><a class="btn js-blob-blame-link" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/blame/master/13-AWS-Cloud/Homework/Instructions/Starter_Files/lambda_function.py">Blame</a><a class="btn" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/commits/master/13-AWS-Cloud/Homework/Instructions/Starter_Files/lambda_function.py">History</a><a class="btn js-data-file-blob-permalink-url" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/blob/acc06971330ce963753782bac758d3eb36f8c28e/13-AWS-Cloud/Homework/Instructions/Starter_Files/lambda_function.py">Permalink</a></div>
</div>

<div class="info-well d-none d-sm-block">
<div class="well-segment">
<ul class="blob-commit-info">
<li class="commit flex-row js-toggle-container" id="commit-15a183b5">
<div class="avatar-cell d-none d-sm-block">
<a href="/amermahyoub"><img alt="Amer Mahyoub&#39;s avatar" src="https://secure.gravatar.com/avatar/67f9e6d21ad96391a41c6059368e1e55?s=80&amp;d=identicon" class="avatar s40 d-none d-sm-inline-block" title="Amer Mahyoub" /></a>
</div>
<div class="commit-detail flex-list">
<div class="commit-content qa-commit-content">
<a class="commit-row-message item-title js-onboarding-commit-item " href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/commit/15a183b595b8db73e36248faab7a4720bcd3c087">AWS sllides and homeworks</a>
<span class="commit-row-message d-inline d-sm-none">
&middot;
15a183b5
</span>
<div class="committer">
<a class="commit-author-link js-user-link" data-user-id="1344" href="/amermahyoub">Amer Mahyoub</a> authored <time class="js-timeago" title="Feb 18, 2021 11:24am" datetime="2021-02-18T11:24:48Z" data-toggle="tooltip" data-placement="bottom" data-container="body">Feb 18, 2021</time>
</div>

</div>
<div class="commit-actions flex-row">

<div class="js-commit-pipeline-status" data-endpoint="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/commit/15a183b595b8db73e36248faab7a4720bcd3c087/pipelines?ref=master"></div>
<div class="commit-sha-group d-none d-sm-flex">
<div class="label label-monospace monospace">
15a183b5
</div>
<button class="btn btn btn-default" data-toggle="tooltip" data-placement="bottom" data-container="body" data-title="Copy commit SHA" data-class="btn btn-default" data-clipboard-text="15a183b595b8db73e36248faab7a4720bcd3c087" type="button" title="Copy commit SHA" aria-label="Copy commit SHA"><svg class="s16" data-testid="copy-to-clipboard-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#copy-to-clipboard"></use></svg></button>

</div>
</div>
</div>
</li>

</ul>
</div>


</div>
<div class="blob-content-holder" id="blob-content-holder">
<article class="file-holder">
<div class="js-file-title file-title-flex-parent">
<div class="file-header-content">
<svg class="s16" data-testid="doc-text-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#doc-text"></use></svg>
<strong class="file-title-name">
lambda_function.py
</strong>
<button class="btn btn-clipboard btn-transparent" data-toggle="tooltip" data-placement="bottom" data-container="body" data-class="btn-clipboard btn-transparent" data-title="Copy file path" data-clipboard-text="{&quot;text&quot;:&quot;13-AWS-Cloud/Homework/Instructions/Starter_Files/lambda_function.py&quot;,&quot;gfm&quot;:&quot;`13-AWS-Cloud/Homework/Instructions/Starter_Files/lambda_function.py`&quot;}" type="button" title="Copy file path" aria-label="Copy file path"><svg class="s16" data-testid="copy-to-clipboard-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#copy-to-clipboard"></use></svg></button>
<small class="mr-1">
4.08 KB
</small>
</div>

<div class="file-actions"><button name="button" type="submit" class="btn btn-primary js-edit-blob ml-2  js-edit-blob-link-fork-toggler" data-action="edit" data-fork-path="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/forks?continue%5Bnotice%5D=You%27re+not+allowed+to+make+changes+to+this+project+directly.+A+fork+of+this+project+has+been+created+that+you+can+make+changes+in%2C+so+you+can+submit+a+merge+request.&amp;continue%5Bnotice_now%5D=You%27re+not+allowed+to+make+changes+to+this+project+directly.+A+fork+of+this+project+is+being+created+that+you+can+make+changes+in%2C+so+you+can+submit+a+merge+request.&amp;continue%5Bto%5D=%2FUWA-Bootcamp%2Fuw-blv-fin-pt-11-2020-u-c%2F-%2Fedit%2Fmaster%2F13-AWS-Cloud%2FHomework%2FInstructions%2FStarter_Files%2Flambda_function.py&amp;namespace_key=1368">Edit</button><button name="button" type="submit" class="btn btn-primary ide-edit-button ml-2 btn-inverted js-edit-blob-link-fork-toggler" data-action="edit" data-fork-path="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/forks?continue%5Bnotice%5D=You%27re+not+allowed+to+make+changes+to+this+project+directly.+A+fork+of+this+project+has+been+created+that+you+can+make+changes+in%2C+so+you+can+submit+a+merge+request.&amp;continue%5Bnotice_now%5D=You%27re+not+allowed+to+make+changes+to+this+project+directly.+A+fork+of+this+project+is+being+created+that+you+can+make+changes+in%2C+so+you+can+submit+a+merge+request.&amp;continue%5Bto%5D=%2F-%2Fide%2Fproject%2Fnospmah%2Fuw-blv-fin-pt-11-2020-u-c%2Fedit%2Fmaster%2F-%2F13-AWS-Cloud%2FHomework%2FInstructions%2FStarter_Files%2Flambda_function.py&amp;namespace_key=1368">Web IDE</button><div class="btn-group ml-2" role="group">

<button name="button" type="submit" class="btn btn-default js-edit-blob-link-fork-toggler" data-action="replace" data-fork-path="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/forks?continue%5Bnotice%5D=You%27re+not+allowed+to+make+changes+to+this+project+directly.+A+fork+of+this+project+has+been+created+that+you+can+make+changes+in%2C+so+you+can+submit+a+merge+request.+Try+to+replace+this+file+again.&amp;continue%5Bnotice_now%5D=You%27re+not+allowed+to+make+changes+to+this+project+directly.+A+fork+of+this+project+is+being+created+that+you+can+make+changes+in%2C+so+you+can+submit+a+merge+request.&amp;continue%5Bto%5D=%2FUWA-Bootcamp%2Fuw-blv-fin-pt-11-2020-u-c%2F-%2Fblob%2Fmaster%2F13-AWS-Cloud%2FHomework%2FInstructions%2FStarter_Files%2Flambda_function.py&amp;namespace_key=1368">Replace</button>
<button name="button" type="submit" class="btn btn-default js-edit-blob-link-fork-toggler" data-action="delete" data-fork-path="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/forks?continue%5Bnotice%5D=You%27re+not+allowed+to+make+changes+to+this+project+directly.+A+fork+of+this+project+has+been+created+that+you+can+make+changes+in%2C+so+you+can+submit+a+merge+request.+Try+to+delete+this+file+again.&amp;continue%5Bnotice_now%5D=You%27re+not+allowed+to+make+changes+to+this+project+directly.+A+fork+of+this+project+is+being+created+that+you+can+make+changes+in%2C+so+you+can+submit+a+merge+request.&amp;continue%5Bto%5D=%2FUWA-Bootcamp%2Fuw-blv-fin-pt-11-2020-u-c%2F-%2Fblob%2Fmaster%2F13-AWS-Cloud%2FHomework%2FInstructions%2FStarter_Files%2Flambda_function.py&amp;namespace_key=1368">Delete</button>
</div><div class="btn-group ml-2" role="group">
<button class="btn btn btn-sm js-copy-blob-source-btn" data-toggle="tooltip" data-placement="bottom" data-container="body" data-class="btn btn-sm js-copy-blob-source-btn" data-title="Copy file contents" data-clipboard-target=".blob-content[data-blob-id=&#39;e07ddb064aa7381ea114c4159141158d706536b7&#39;]" type="button" title="Copy file contents" aria-label="Copy file contents"><svg class="s16" data-testid="copy-to-clipboard-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#copy-to-clipboard"></use></svg></button>
<a class="btn btn-sm has-tooltip" target="_blank" rel="noopener noreferrer" aria-label="Open raw" title="Open raw" data-container="body" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/raw/master/13-AWS-Cloud/Homework/Instructions/Starter_Files/lambda_function.py"><svg class="s16" data-testid="doc-code-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#doc-code"></use></svg></a>
<a download="13-AWS-Cloud/Homework/Instructions/Starter_Files/lambda_function.py" class="btn btn-sm has-tooltip" target="_blank" rel="noopener noreferrer" aria-label="Download" title="Download" data-container="body" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/raw/master/13-AWS-Cloud/Homework/Instructions/Starter_Files/lambda_function.py?inline=false"><svg class="s16" data-testid="download-icon"><use xlink:href="/assets/icons-1e863578ceb6844cc6941dadfd4b07001aed5876dc579fe61ea58ffd1458e7e8.svg#download"></use></svg></a>

</div></div>
</div>
<div class="js-file-fork-suggestion-section file-fork-suggestion hidden">
<span class="file-fork-suggestion-note">
You're not allowed to
<span class="js-file-fork-suggestion-section-action">
edit
</span>
files in this project directly. Please fork this project,
make your changes there, and submit a merge request.
</span>
<a class="js-fork-suggestion-button btn btn-grouped btn-inverted btn-success" rel="nofollow" data-method="post" href="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/blob/master/13-AWS-Cloud/Homework/Instructions/Starter_Files/lambda_function.py">Fork</a>
<button class="js-cancel-fork-suggestion-button btn btn-grouped" type="button">
Cancel
</button>
</div>



<div data-blob-data="### Required Libraries ###
from datetime import datetime
from dateutil.relativedelta import relativedelta

### Functionality Helper Functions ###
def parse_int(n):
    &quot;&quot;&quot;
    Securely converts a non-integer value to integer.
    &quot;&quot;&quot;
    try:
        return int(n)
    except ValueError:
        return float(&quot;nan&quot;)


def build_validation_result(is_valid, violated_slot, message_content):
    &quot;&quot;&quot;
    Define a result message structured as Lex response.
    &quot;&quot;&quot;
    if message_content is None:
        return {&quot;isValid&quot;: is_valid, &quot;violatedSlot&quot;: violated_slot}

    return {
        &quot;isValid&quot;: is_valid,
        &quot;violatedSlot&quot;: violated_slot,
        &quot;message&quot;: {&quot;contentType&quot;: &quot;PlainText&quot;, &quot;content&quot;: message_content},
    }


### Dialog Actions Helper Functions ###
def get_slots(intent_request):
    &quot;&quot;&quot;
    Fetch all the slots and their values from the current intent.
    &quot;&quot;&quot;
    return intent_request[&quot;currentIntent&quot;][&quot;slots&quot;]


def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message):
    &quot;&quot;&quot;
    Defines an elicit slot type response.
    &quot;&quot;&quot;

    return {
        &quot;sessionAttributes&quot;: session_attributes,
        &quot;dialogAction&quot;: {
            &quot;type&quot;: &quot;ElicitSlot&quot;,
            &quot;intentName&quot;: intent_name,
            &quot;slots&quot;: slots,
            &quot;slotToElicit&quot;: slot_to_elicit,
            &quot;message&quot;: message,
        },
    }


def delegate(session_attributes, slots):
    &quot;&quot;&quot;
    Defines a delegate slot type response.
    &quot;&quot;&quot;

    return {
        &quot;sessionAttributes&quot;: session_attributes,
        &quot;dialogAction&quot;: {&quot;type&quot;: &quot;Delegate&quot;, &quot;slots&quot;: slots},
    }


def close(session_attributes, fulfillment_state, message):
    &quot;&quot;&quot;
    Defines a close slot type response.
    &quot;&quot;&quot;

    response = {
        &quot;sessionAttributes&quot;: session_attributes,
        &quot;dialogAction&quot;: {
            &quot;type&quot;: &quot;Close&quot;,
            &quot;fulfillmentState&quot;: fulfillment_state,
            &quot;message&quot;: message,
        },
    }

    return response


### Intents Handlers ###
def recommend_portfolio(intent_request):
    &quot;&quot;&quot;
    Performs dialog management and fulfillment for recommending a portfolio.
    &quot;&quot;&quot;

    first_name = get_slots(intent_request)[&quot;firstName&quot;]
    age = get_slots(intent_request)[&quot;age&quot;]
    investment_amount = get_slots(intent_request)[&quot;investmentAmount&quot;]
    risk_level = get_slots(intent_request)[&quot;riskLevel&quot;]
    source = intent_request[&quot;invocationSource&quot;]

    if source == &quot;DialogCodeHook&quot;:
        # Perform basic validation on the supplied input slots.
        # Use the elicitSlot dialog action to re-prompt
        # for the first violation detected.

        ### YOUR DATA VALIDATION CODE STARTS HERE ###

        ### YOUR DATA VALIDATION CODE ENDS HERE ###

        # Fetch current session attibutes
        output_session_attributes = intent_request[&quot;sessionAttributes&quot;]

        return delegate(output_session_attributes, get_slots(intent_request))

    # Get the initial investment recommendation

    ### YOUR FINAL INVESTMENT RECOMMENDATION CODE STARTS HERE ###

    ### YOUR FINAL INVESTMENT RECOMMENDATION CODE ENDS HERE ###

    # Return a message with the initial recommendation based on the risk level.
    return close(
        intent_request[&quot;sessionAttributes&quot;],
        &quot;Fulfilled&quot;,
        {
            &quot;contentType&quot;: &quot;PlainText&quot;,
            &quot;content&quot;: &quot;&quot;&quot;{} thank you for your information;
            based on the risk level you defined, my recommendation is to choose an investment portfolio with {}
            &quot;&quot;&quot;.format(
                first_name, initial_recommendation
            ),
        },
    )


### Intents Dispatcher ###
def dispatch(intent_request):
    &quot;&quot;&quot;
    Called when the user specifies an intent for this bot.
    &quot;&quot;&quot;

    intent_name = intent_request[&quot;currentIntent&quot;][&quot;name&quot;]

    # Dispatch to bot&#39;s intent handlers
    if intent_name == &quot;RecommendPortfolio&quot;:
        return recommend_portfolio(intent_request)

    raise Exception(&quot;Intent with name &quot; + intent_name + &quot; not supported&quot;)


### Main Handler ###
def lambda_handler(event, context):
    &quot;&quot;&quot;
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    &quot;&quot;&quot;

    return dispatch(event)
" data-is-ci-config-file="false" id="js-blob-toggle-graph-preview"></div>
<div class="blob-viewer" data-path="13-AWS-Cloud/Homework/Instructions/Starter_Files/lambda_function.py" data-type="simple" data-url="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/blob/master/13-AWS-Cloud/Homework/Instructions/Starter_Files/lambda_function.py?format=json&amp;viewer=simple">
<div class="text-center gl-mt-4 gl-mb-3">
<span class="gl-spinner gl-spinner-orange gl-spinner-md qa-spinner" aria-label="Loading"></span>
</div>

</div>


</article>
</div>

<div class="modal" id="modal-upload-blob">
<div class="modal-dialog modal-lg">
<div class="modal-content">
<div class="modal-header">
<h3 class="page-title">Replace lambda_function.py</h3>
<button aria-label="Close" class="close" data-dismiss="modal" type="button">
<span aria-hidden>&times;</span>
</button>
</div>
<div class="modal-body">
<form class="js-quick-submit js-upload-blob-form" data-method="put" action="/UWA-Bootcamp/uw-blv-fin-pt-11-2020-u-c/-/update/master/13-AWS-Cloud/Homework/Instructions/Starter_Files/lambda_function.py" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="put" /><input type="hidden" name="authenticity_token" value="DI6PKOaz5ms46NFC2B2GwQ4o+IzjSX6oaXNHk+dpDRdTMz+fcscBw2yu3qchJXKH0NcuoLaK2ufSAac9y/gCnQ==" /><div class="dropzone">
<div class="dropzone-previews blob-upload-dropzone-previews">
<p class="dz-message light">
Attach a file by drag &amp; drop or <a class="markdown-selector" href="#">click to upload</a>
</p>
</div>
</div>
<br>
<div class="dropzone-alerts gl-alert gl-alert-danger gl-mb-5 data" style="display:none"></div>
<div class="form-group row commit_message-group">
<label class="col-form-label col-sm-2" for="commit_message-63f55baeca1491797d734a0db9d958d9">Commit message
</label><div class="col-sm-10">
<div class="commit-message-container">
<div class="max-width-marker"></div>
<textarea name="commit_message" id="commit_message-63f55baeca1491797d734a0db9d958d9" class="form-control js-commit-message" placeholder="Replace lambda_function.py" required="required" rows="3">
Replace lambda_function.py</textarea>
</div>
</div>
</div>

<input type="hidden" name="branch_name" id="branch_name" />
<input type="hidden" name="create_merge_request" id="create_merge_request" value="1" />
<input type="hidden" name="original_branch" id="original_branch" value="master" class="js-original-branch" />

<div class="form-actions">
<button name="button" type="button" class="btn gl-button btn-success btn-upload-file" id="submit-all"><i aria-hidden="true" data-hidden="true" class="fa fa-spin fa-spinner js-loading-icon hidden"></i>
Replace file
</button><a class="btn gl-button btn-cancel" data-dismiss="modal" href="#">Cancel</a>
<div class="inline gl-ml-3">
A new branch will be created in your fork and a new merge request will be started.
</div>

</div>
</form></div>
</div>
</div>
</div>

</div>


</div>
</div>
</div>
</div>


<script>
//<![CDATA[
if ('loading' in HTMLImageElement.prototype) {
  document.querySelectorAll('img.lazy').forEach(img => {
    img.loading = 'lazy';
    let imgUrl = img.dataset.src;
    // Only adding width + height for avatars for now
    if (imgUrl.indexOf('/avatar/') > -1 && imgUrl.indexOf('?') === -1) {
      const targetWidth = img.getAttribute('width') || img.width;
      imgUrl += `?width=${targetWidth}`;
    }
    img.src = imgUrl;
    img.removeAttribute('data-src');
    img.classList.remove('lazy');
    img.classList.add('js-lazy-loaded', 'qa-js-lazy-loaded');
  });
}

//]]>
</script>

</body>
</html>

