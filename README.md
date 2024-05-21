[![Contributors][contributors-shield]][contributors-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]

<div align="center">
  <a href="#">
    <img src="https://cdn.technologyreview.jp/wp-content/uploads/sites/2/2019/08/21125432/datalabor3slow.gif" alt="Logo" width="400">
  </a>
  <h3 align="center">UniTech</h3>
  <p align="center">AI API</p>

</div>

## 🔰 Getting Started

This project was created to hold an API on Flask (Python).

<br/>

### 💾 Tools Used

[![VsCode][VsCode]][VsCode-url]

### 🤖 Technologies Used

[![Python][Python]][Python-url]
[![Flask][Flask]][Flask-url]
[![Docker][Docker]][Docker-url]
[![DevContainers][DevContainers]][DevContainers-url]

### 📋 Pre-requisites

- 🐋Docker
- 💻VsCode

<br/>

>💡 Attention
>
>This project employs Docker Dev Containers, ensuring that all operations occur within containers. Therefore, it is imperative to have Docker installed on your system.
>
>It is highly recommended to utilize Visual Studio Code (VsCode), as the MS Dev Container plugin facilitates seamless integration with the development environment. Please ensure that you have Docker installed and consider installing the VsCode Dev Containers plugin for an enhanced experience.
>
>Since Docker and Dev Containers are in use, there is no need to directly install Python on your local machine. The Dev Container for this project is preconfigured to install Python, Poetry, and all necessary dependencies internally.
>
>Sit back and let the informagic work its magic.


<br/>

## 🎨 Features
The application has the following functionality:

### 👓 Google's Gemini @ /gmni

#### [POST] @ /multiple_choice_question
This enpoint retrieves a multiple choice question in the following structure:
```
{
  question_statement:'question statement that AI will generate', 
  alternatives:[
    {a:'alternative'},
    {b:'alternative'}, 
    {c:'alternative'}, 
    {d:'alternative'}, 
    {e:'alternative'}
  ], 
  correct_answer:'correct_alternative_letter'
}
```
It takes as **payload** the following:
```
{
  "subject":"Science discipline like: Maths, Geography, etc.",
  "academic_level":"Academic level like: First Grader, etc.",
  "theme":"A theme within the chosen subject, like: Algebra, Captalism, etc.",
  "locale":"Locale in which the prompt will be retrieved, like: pt-br, en-us, etc."
}
```

### 🤖 OpenAi's GPT @ /opai

lorem

<br/>

## 📑 Licenses

Distributed under the MIT License. See `LICENSE` for more information.

<br/>

## 🧻 TODOs
- [X] 1 - Gemini
- [⠀] 2 - OpenAI

<!-- ASSETS -->

<!-- BADGE - Contributors -->

[contributors-shield]: https://img.shields.io/github/contributors/toledkrw/api-unitech.svg?style=for-the-badge
[contributors-url]: https://github.com/toledkrw/api-unitech/graphs/contributors

<!-- BADGE - Issues -->

[issues-shield]: https://img.shields.io/github/issues/toledkrw/api-unitech.svg?style=for-the-badge
[issues-url]: https://github.com/toledkrw/api-unitech/issues

<!-- BADGE - License -->

[license-shield]: https://img.shields.io/github/license/toledkrw/api-unitech.svg?style=for-the-badge
[license-url]: https://github.com/toledkrw/api-unitech/blob/main/LICENSE

<!--  -->
<!-- TECHNOLOGIES -->
<!--  -->

<!-- BADGE - VsCode -->
[VsCode]: https://img.shields.io/badge/Visual%20Studio%20Code-14354C.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white
[VsCode-url]: https://code.visualstudio.com/

<!-- BADGE - Python -->
[Python]: https://img.shields.io/badge/Python-c29200?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

<!-- BADGE - Docker -->
[Docker]: https://img.shields.io/badge/Docker-0078d7.svg?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/products/docker-desktop/

<!-- BADGE - DevContainer -->
[DevContainers]: https://img.shields.io/badge/Dev%20Containers-73059e.svg?style=for-the-badge&logo=linuxcontainers&logoColor=white
[DevContainers-url]: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers

<!-- BADGE - Flask -->
[Flask]: https://img.shields.io/badge/Flask-000000.svg?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com
