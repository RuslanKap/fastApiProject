<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="FastAPI_Search_App_0"></a>FastAPI Search App</h1>
<p class="has-line-data" data-line-start="2" data-line-end="4">This repository contains code for asynchronous search and delete data from CSV file(<a href="http://posts.py">posts.py</a>).<br>
Web search  avalible at <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a></p>
<h2 class="code-line" data-line-start=6 data-line-end=7 ><a id="Installation_method_1_Run_application_locally_6"></a>Installation method 1 (Run application locally)</h2>
<ol>
<li class="has-line-data" data-line-start="9" data-line-end="11">Clone this Repo</li>
</ol>
<pre><code class="has-line-data" data-line-start="12" data-line-end="14" class="language-sh">git <span class="hljs-built_in">clone</span> https://github.com/RuslanKap/fastApiProject
</code></pre>
<ol start="2">
<li class="has-line-data" data-line-start="14" data-line-end="16">Move into the root folder</li>
</ol>
<pre><code class="has-line-data" data-line-start="17" data-line-end="19" class="language-sh"><span class="hljs-built_in">cd</span> fastApiProject
</code></pre>
<ol start="3">
<li class="has-line-data" data-line-start="19" data-line-end="21">Create a virtualenv</li>
</ol>
<pre><code class="has-line-data" data-line-start="22" data-line-end="24" class="language-sh">python3 -m virtualenv env
</code></pre>
<ol start="4">
<li class="has-line-data" data-line-start="24" data-line-end="26">Activate virtualenv</li>
</ol>
<pre><code class="has-line-data" data-line-start="27" data-line-end="29" class="language-sh"><span class="hljs-built_in">source</span> env/bin/activate
</code></pre>
<ol start="5">
<li class="has-line-data" data-line-start="29" data-line-end="31">Install the required packages</li>
</ol>
<pre><code class="has-line-data" data-line-start="32" data-line-end="34" class="language-sh">python -m pip install -r requirements.txt
</code></pre>
<ol start="6">
<li class="has-line-data" data-line-start="34" data-line-end="36">Run script import_csv.py for upload data from CSV to postgres DB</li>
</ol>
<pre><code class="has-line-data" data-line-start="37" data-line-end="39" class="language-sh">python import_csv.py
</code></pre>
<ol start="7">
<li class="has-line-data" data-line-start="39" data-line-end="41">Start the app using Uvicorn</li>
</ol>
<pre><code class="has-line-data" data-line-start="42" data-line-end="44" class="language-sh">uvicorn app.main:app --reload --workers <span class="hljs-number">1</span> --host <span class="hljs-number">0.0</span>.<span class="hljs-number">0.0</span> --port <span class="hljs-number">8000</span>
</code></pre>
<ol start="8">
<li class="has-line-data" data-line-start="44" data-line-end="46">Ensure you have a Postgres Database running locally. Additionally create a Fast_api_dev db with user fast_api having required priviledges OR Change the DATABASE_URL variable in the .env file to reflect db settings (user:password/db)</li>
</ol>
<h2 class="code-line" data-line-start=46 data-line-end=47 ><a id="Installation_method_2_Docker_46"></a>Installation method 2 (Docker)</h2>
<p class="has-line-data" data-line-start="48" data-line-end="49">Installation method 2 (Run Locally using Docker)</p>
<ol>
<li class="has-line-data" data-line-start="50" data-line-end="52">
<p class="has-line-data" data-line-start="50" data-line-end="51">Ensure Docker is installed.</p>
</li>
<li class="has-line-data" data-line-start="52" data-line-end="54">
<p class="has-line-data" data-line-start="52" data-line-end="53">Ensure Docker Compose is installed.</p>
</li>
<li class="has-line-data" data-line-start="54" data-line-end="55">
<p class="has-line-data" data-line-start="54" data-line-end="55">Clone this Repo</p>
</li>
</ol>
<pre><code class="has-line-data" data-line-start="56" data-line-end="58" class="language-sh">git <span class="hljs-built_in">clone</span> (https://github.com/RuslanKap/fastApiProject)
</code></pre>
<ol start="4">
<li class="has-line-data" data-line-start="58" data-line-end="59">Change into the directory</li>
</ol>
<pre><code class="has-line-data" data-line-start="60" data-line-end="62" class="language-sh"><span class="hljs-built_in">cd</span> fastApiProject
</code></pre>
<ol start="5">
<li class="has-line-data" data-line-start="62" data-line-end="63">Use Docker-Compose to spin up containers</li>
</ol>
<pre><code class="has-line-data" data-line-start="64" data-line-end="66" class="language-sh">docker-compose up <span class="hljs-operator">-d</span> --build
</code></pre>
<ol start="6">
<li class="has-line-data" data-line-start="66" data-line-end="68">
<p class="has-line-data" data-line-start="66" data-line-end="67">If everything completes should be available on notes</p>
</li>
<li class="has-line-data" data-line-start="68" data-line-end="70">
<p class="has-line-data" data-line-start="68" data-line-end="69">Docs are generated on docs</p>
</li>
</ol>
<h2 class="code-line" data-line-start=70 data-line-end=71 ><a id="Documentation_70"></a>Documentation</h2>
<p class="has-line-data" data-line-start="71" data-line-end="72">Open API Documentation is provided by Redoc</p>
