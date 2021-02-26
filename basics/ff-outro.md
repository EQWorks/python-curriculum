# Outro

From Part 00 to 03, we have gone through a short (7 weeks) and a rather unconventional path to learning Python programming.

This outro serves as another background introduction for the journey onward.

## Open-source

The _open-source software movement_ started in the 80s, initially as the _free software movement_. Since then, we have enjoyed a constant improvement in working, living, learning, communicating, and more.

![open-swiss-knife](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/121212_2_OpenSwissKnife.png/800px-121212_2_OpenSwissKnife.png)

(By Johannes Spielhagen, through [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:121212_2_OpenSwissKnife.png))

The immediate values of open-source software are apparent. They are usually free to use. Users can change software behaviors without waiting for the providers to do it for them. For the provider, open-source allows better quality and security through public scrutiny. It shows their confidence and opinions to attract a fanbase and create an ecosystem. For organizations using open-source technologies, hiring and onboarding become much simpler without expensive training and obtaining certificates from the proprietary counterparts.

![profitable](https://user-images.githubusercontent.com/2837532/108421910-d80b0000-7203-11eb-8e0d-bf92446a6283.png)

(From [Wikipedia](https://en.wikipedia.org/wiki/Open-source_model) as of early 2021)

In-depth, the open-source community has qualities and practices that impact our workplace and society in profound ways.

### Transparency by default

While open-source projects come in all shapes and sizes, they all have in common the transparency of code and its timeline of changes. As a result, other aspects are out in the open such as issue tracking, feature discussions, peer-review, and product deployment. This transparency makes the software development process more socially inclusive by encouraging participants to contribute to various parts of the process.

![sdlc](https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/SDLC_-_Software_Development_Life_Cycle.jpg/596px-SDLC_-_Software_Development_Life_Cycle.jpg)

(Software Development Life Cycle from [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:SDLC_-_Software_Development_Life_Cycle.jpg))

Empowered by transparency, the open-source community often devises pragmatic and objective-focused methodologies, eliminating as many intermediaries and manual processes as possible. Contributors can infer as much as possible from available information before involving others. These methodologies continuously evolve to adapt to the people who make and use the software instead of the conventional corporate world's rigid models. The transparency also generates more data that drives more opportunities to help make data-driven decisions.

### Asynchronous and Decentralized Workforce

Open-source contributors form a workforce that is asynchronous and decentralized. With an abundance of information, minimal processes, and a growingly sophisticated set of tools and automation, open-source contributors can collaborate efficiently at any time and in any location.

This asynchronous workforce model defies the conventional way practically unchanged from the First Industrial Revolution. It better embraces the Information Age, especially with the catalyst known as the internet.

![social](https://upload.wikimedia.org/wikipedia/commons/9/9b/Social_Network_Analysis_Visualization.png)

(Social Network Analysis Visualization, [source](https://www.cairn.info/resume.php?ID_ARTICLE=LCN_103_0037) through [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Social_Network_Analysis_Visualization.png))

The synchronous forms of communication do not entirely vanish. They become more scarce and thus more treasured by each other. When most issues and discussions happen asynchronously, the calls and meetings can become laser-focused on what's unresolved, preserving time and effort. Equally importantly, the in-person times serve a great socialization purpose to remind us that we are still humans.

### Automation and Hacking

![automation](https://1.cms.s81c.com/sites/default/files/2018-10-24/automation_OG_1200x630.png)

(By [IBM](https://www.ibm.com/products/robotic-process-automation))

To sustain an asynchronous and decentralized workforce with massive amounts of information open to the public, open-source participants frequently make and improve automation to optimize or abstract away processes. This mindset drives people to continually lookout for new ways to adapt and improve their workflow.

But it is rare for existing tools and automation to provide a perfect fit for everyone's use-cases. People resort to hacking, or creative workarounds, to bend tools to their will.

The hacking culture also provides an organic counter-balance to some problems that plague many software projects, such as under-documentation, lack of testing, and [leaky abstractions](https://en.wikipedia.org/wiki/Leaky_abstraction).

## git

Among many tools that support the open-source software ecosystem, `git` is the most popular one that provides efficient ways to distribute and manage source code. Its decentralized nature allows every contributor to access the entire working copy and change history.

The collaboration happens in a peer-to-peer fashion. Collaborators branch out the source code to implement new features or issue fixes. Once satisfied with the implementation, the contributor sends a request to add their changes to the mainstream working copy and get others to review and offer suggestions - similar to Google Docs in the suggesting mode. When enough contributors reach a consensus, the implementation gets merged back to the mainstream. During this process, automation allows contributors to not waste time on trivial problems such as code-style differences and logical flaws. After the merge, it is common to see automated deployment or release of the software to a designated audience.

![branching](https://user-images.githubusercontent.com/2837532/108411648-e0107300-71f6-11eb-8148-d66dbd4d19d5.png)

(From [Understanding the GitHub flow](https://guides.github.com/introduction/flow/))

When unresolvable disagreements break out, one can maintain a branch as a permanent _fork_ to evolve the project to a different trajectory. The practice of forking is why we have a diverse number of Linux distributions.

![linux distros](https://specials-images.forbesimg.com/imageserve/5dc1a7ccca425400079c78c4/960x0.jpg?fit=scale)

(By Eric Adams through [Forbes](https://www.forbes.com/sites/jasonevangelho/2019/11/05/my-search-for-the-perfect-linux-os-just-ended--with-an-unexpected-surprise/?sh=2798c7045cd6))

### GitHub

However, due to a barrier to converting from a centralized mindset to a decentralized one from its users, `git` was notoriously convoluted and hard to utilize. Toward the end of 2007, a group of software developers who enjoyed `git` but envisioned better ways to use it started building what's known as GitHub today, making the usage pleasant for more. They have been building GitHub using `git` and GitHub itself, a practice known as [dogfooding](https://en.wikipedia.org/wiki/Eating_your_own_dog_food).

The company started as profitable from day one, refrained from taking external funding until [July 2012](https://www.reuters.com/article/github-fundraising/github-raises-100-mln-from-andreessen-horowitz-idUSL2E8I9AV320120709), and stayed as a flat organization with 234+ employees until [17 July 2014](https://en.wikipedia.org/wiki/Timeline_of_GitHub).

Perhaps the root of their success is a culture that emphasizes [people's happiness instead of money](https://tom.preston-werner.com/2010/10/18/optimize-for-happiness.html). The culture reflects in their ability to [develop quality products](https://github.blog/changelog/) that embrace and encourage the best practices from the open-source community and benefit even proprietary developments. Not surprisingly, they are also a large contributor to various open-source software projects, with an adopted [Open Source (Almost) Everything](https://tom.preston-werner.com/2011/11/22/open-source-everything.html) mindset.

Such an interpretation of open-source practices allows the company to attract top talents worldwide to collaborate on a service platform enjoyed by their users. By 2010 (a little over three years since inception), GitHub has claimed to be the largest host of source code in the world until today.

## EQ Works - our adaptation of open-source

A key idea behind the open-source movement is to leverage their learnings to make information and curation more transparent and efficient. This social movement coincides with increasing amounts of information online and a growing realization of how closed platforms could [unethically profit from manipulating the information flow and shape](https://en.wikipedia.org/wiki/Facebook%E2%80%93Cambridge_Analytica_data_scandal).

As a part of the workspace meta shift, more organizations start to realize the benefits of open-source software and their community practices. Since around the beginning of 2014, our dev team has started to build products using open-source technologies and evolve our culture by adapting the open-source ways.

### Round-table wisdom

Instead of on-paper seniority, materialized merits become the only valid argument between project contributors in discussions and debates. We demonstrate cases in a verifiable way, rapidly iterate based on feedback, and make frequent releases with peer-review and automation that capture trivial issues.

The practice allows us to eliminate hierarchy and processes to enable productivity and innovation through a flat and fluid team. We minimize constraints to give everyone the freedom to pursue after their interest and the ability to develop, test and deploy their implementations without waiting for others.

### Respect Time - Work Alone, Together

The transparent and asynchronous model of information distribution allows our collaboration and communication to be in a manner that respects each other's time. With the information availed to us, each team member infers and summarizes on their own time to form most decisions without bothering or getting blocked by others.

We encourage team members to learn and transparently utilize shared calendars, to-do lists, group chat, etc. This way, we retain information as a raw and searchable form of a knowledge base. With the help of tools and automation built on top of the services we use, we distill the knowledge into well-formed documentation for future reference. We create bots to collect status and updates from where work happens, then curate and share them across the board regularly. The automation allows us to [focus more time on unresolved problems and minimize synchronous debriefings](https://github.com/EQWorks/common/blob/master/communications/meetings.md).

## Prospects

As a natural progression, more organizations have started taking an open stance toward software and data. The increasingly sophisticated open-source tools and automation that help gather and curate data establish a new baseline that redefines much of the professional landscape. The cost-saving factor from utilizing open-source technologies is also making it cheaper and easier to experiment with ideas formerly impossible without extensive training.

### Redefinition of developers

![venn](https://user-images.githubusercontent.com/2837532/108427203-d0028e80-720a-11eb-889c-0cac4394a726.png)

Professional developers no longer need to solely focus on software development implementation and start internalizing other aspects that formerly required dedicated roles. These include (but are not limited to) software architecting, designing, testing, documenting, and [even marketing](https://basecamp.com/handbook/01-basecamp-is-you). Such change gives developers better perspectives and a higher sense of ownership, allowing them to think and act more strategically.

As most programming languages are already in the open-source ecosystem, they are getting ever more accessible. More people can easily acquire and utilize these technologies to automate and simplify their jobs. As a result, it further moves programming toward the skillset spectrum's essential direction for more fields and industries, thus further blurring the line between developers and non-developers.

### Acceleration through Machine Learning

Open-source projects such as [TensorFlow](https://www.tensorflow.org/) and [PyTorch](https://pytorch.org/) offer a set of sophisticated implementation of modern machine-learning algorithms that accelerate the path from AI model research to production.

There are also open-source AI models that accelerate the elimination of many chore-like job functions. Such as [comprehending text and elaborating](https://openai.com/blog/better-language-models/) from seeding phrases or [categorizing software changes](https://medium.com/locus-engineering/road-to-automation-release-notes-d1c49cc97d9). Some technologies can procedurally generate video game stages and contents to offer a unique and challenging experience or learn to [beat](https://github.com/tensorflow/minigo) real [players](https://openai.com/projects/five/).

## What's next?

From here on, we will gradually adopt some open-source technologies (including machine-learning subjects) in the following series. Our focus will be on practical use-cases and perspectives that hopefully help you connect dots for your path.
