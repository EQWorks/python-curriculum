# Outro

From Part 00 to 03, we have gone through a short (7 weeks) and a rather unconventional path to learning Python programming.

This outro serves as another background introduction for the journey onward.

## Open-source

The open-source software movement started in the 80s, initially as the _free software movement_. Throughout its [evolutionary timeline](https://en.wikipedia.org/wiki/Open-source-software_movement#Brief_history), many have contributed to its conceptualization and formulation to tackle many legal, business, technical, and societal challenges.

The immediate face-value of open-source software is already appealing to its consumers. These programs are usually free to use. Users can also change the software behaviors with some knowledge of programming to suit individual needs.

For the providing party, open-source brings benefits of open scrutiny to the program's quality and security measures, a showcase of confidence, and a public statement of styles and opinions.

With some well-defined governance models, open-source software communities can promote a collaborative environment and onboard collaborators with little to no effort from the original authors required by conventional settings. With a mature license, the users understand the provider's limits and liabilities, greatly simplifying the usage contracts and limitations. Lastly, with proper financial backing, the software makers who pursue these projects as passions of their own tend to consistently innovate and push the boundaries.

### Transparency

While open-source software communities and projects present in many shapes and forms, even when they are for-profit, the one prominent trait in common is the transparency of the software source code.

The transparency of the source code and its timeline of code changes lead to other aspects such as the software issue/feedback tracking, feature discussions, code peer-review, product distribution, etc., to be open to public examination. While much of those aspects get increasingly automated, the overall transparency allows the software development process to be more socially inclusive, encouraging participants to contribute to the various parts of the development lifecycle. Even those from the public who cannot code get to raise usage issues or suggest feature/documentation improvements.

Empowered by transparency, open-source communities often devise methodologies that are pragmatic and objective-focused, eliminating as many middle-people and manual processes as possible. More importantly, these methodologies are highly fluid that adapts to the dynamics and changes of the software makers and consumers instead of the rigid models seen from the conventional corporate world.

### Hacking culture

One implication of transparency is that it provides an organic counter-balance to two common problems that plague many software projects by assisting and justifying hacking -- or creative workaround of constraints.

The first is the under-documentation problem, where software development often prioritizes feature development and bug fixes and leaves minimal to no bandwidth to write documentation. From the openly available source code, one can have a fallback to find answers that are not apparent from the software manual and figure out a suitable solution for their custom needs based on the insights derived from understanding the source code. Furthermore, this may lead to documentation improvements by reacting to a case in point.

The second is a phenomenon known as [leaky abstraction](https://en.wikipedia.org/wiki/Leaky_abstraction), where an abstraction leaks details that it is supposed to abstract away. The phenomenon exhibits almost everywhere in software with sufficient complexity, and to eliminate them usually does not make economic sense. With proprietary software, one has to involve tedious (and usually illegal) reverse-engineering to take an inside look. In the case of open-source software, one can openly examine the leak's cause and hack around it.

The hacking culture groomed by open-source software communities virtually eliminates productivity bottlenecks caused by proprietary software practices. Developers become hyper-productive with sufficient time and effort to research the source code as long as the action is economically justified.

## git

Among many tools that support the open-source software ecosystem, one of the most important pieces would be a version control system (VCS). A version control system allows software project management to be simpler on aspects of source code change examination (diffing), versioning and rollback, etc.

Among these VCS, `git` is the most popular one. Though not the first of its kind, known as a distributed version control system (DVCS), `git` allows efficient distribution of source code. Every user has full access to the working copy and the entire change history and references to code derivatives (through branches and tags). Thus the collaboration presents in a peer-to-peer fashion embracing the essence of decentralization.

When unresolvable disagreements break out, one can _fork_ the project to evolve the software to another trajectory without impacting other collaborators. And when the opportunity strikes, forks could also consolidate back to one. The practice of forking is why we have a diverse number of distributions of Linux operating systems (OS). For a similar reason, Android OS would not enjoy its fast development and evolution if it wasn't for a DVCS like `git`.

The implication of `git` and its contribution toward open-source communities further pushes their workflow toward a decentralized direction.

## GitHub (the company)

However, due to a barrier to converting from a centralized mindset to a decentralized one from its users, `git` was notoriously convoluted and hard to utilize. Toward the end of 2007, a group of software developers who enjoyed `git` but envisioned better ways to use it started a company to tackle these problems.

They started building what's known as GitHub today, which makes `git` usages a pleasant experience even for people who are not software developers. They created GitHub using `git` and GitHub itself, a practice known as [dogfooding](https://en.wikipedia.org/wiki/Eating_your_own_dog_food).

What's fascinating about this company is that it started as profitable (or with a convincing model to be so) from day one, refrained from taking external funding until [July 2012](https://www.reuters.com/article/github-fundraising/github-raises-100-mln-from-andreessen-horowitz-idUSL2E8I9AV320120709), and stayed as a flat and fluid organization with 234+ employees until [17 July 2014](https://en.wikipedia.org/wiki/Timeline_of_GitHub).

### Optimize for Happiness

Perhaps the root of the many fascinating factors of GitHub is due to their mindset and a culture that emphasizes [people's happiness, as opposed to money](https://tom.preston-werner.com/2010/10/18/optimize-for-happiness.html).

They leverage the learnings from open-source communities with tools they use (and build) to build toward simpler and better products, without conventional management methodologies and investors getting in their way. The mindset and culture reflect in their ability to [develop quality products and features rapidly](https://github.blog/changelog/).

Their product development is self-initiated based on one's interest and passion, at times even from community volunteers simply because they love using their products. Quality assurance goes through peer-reviews and automation. Manual processes, once identified, are automated away instead of resorting to often error-prone and inefficient bureaucracy. They work entirely as a big open-source project. Not surprisingly, they are also a large contributor to various open-source software projects, with an adopted [Open Source (Almost) Everything](https://tom.preston-werner.com/2011/11/22/open-source-everything.html) mindset.

Such emphasis on people's happiness allows the company to attract top talents worldwide, and it reflects in their products to be enjoyed by their users.

### Asynchronous

GitHub employees use and build tools to collaborate and communicate asynchronously in many different time zones. GitHub employees have treated tools as their primary workplace (though they have offices to support various needs and preferences once they could afford it) and follow the open-source model of transparency to make all information accessible.

The problem of blocking (or being blocked by) others is mitigated or resolved through the creative use of tools and automation, giving employees more quality time to be in "the zone" that often leads to more innovations. The lack of indoctrination of work hours combined with no fixed locations also allows employees to worry less about things that do not matter to their core work subjects and objectives.

Perhaps to no one's surprise, the asynchronous model works well with an increasingly distributed workforce (and our society at large) that we have been transitioning into, where more and more have a choice as to where they would like to work under normal circumstances.

## EQ Works (us)

The open-source social movement's key idea is to leverage the open-source software communities' learnings to make information and curation more transparent. This social movement coincides with the phenomenon of the internet-driven information explosion and the increasing realization of how closed platforms could [manipulate the information's flow and shape and unethically profit from it](https://en.wikipedia.org/wiki/Facebook%E2%80%93Cambridge_Analytica_data_scandal).

As a part of the workspace meta shift, more organizations start to realize the benefits of open-source software and their community practices. Since around the beginning of 2014, our dev team has started to embrace and evolve based on open-source communities' learnings.

### Round-table wisdom

Instead of on-paper seniority, experimental merits become the only valid argument between project maintainers in the event of discussions and debate. We employ requests to code change (pull/merge requests) to demonstrate points in a verifiable way, rapidly iterate based on feedback, and make frequent releases with the help of peer-review and automation that capture rudimentary errors through various quality-assurance measures.

The practice allowed us to eliminate hierarchy and processes to boost productivity and innovation opportunities while maintaining a flat and fluid team.

### Respect of (Others') Time

When information did not flow as freely and quickly as the era of the internet that we live and experience today, the conventional wisdom usually dictates that one should engage in a quick meeting/call with relevant parties to help with decision making. The efficiency of the traditional way to communicate is quickly diminishing in the era of information that we live and experience. In other words, such a form of communication would not scale.

The conventional hierarchal model, which requires grunt work to sift and curate information and report up, suffers a similar scalability problem.

The norm of today's internet is more opt-in based, such as subscribing to a mailing list, follow POTUS on social media, or join group chat channels of relevant subjects. These practices have been fundamentally reshaping how people interact with each other, and the impact is [more profound in younger and upcoming generations](https://www.forbes.com/sites/larryalton/2017/05/11/how-do-millennials-prefer-to-communicate/?sh=39d85bb06d6f).

The opt-in and asynchronous model of information consumption and working leads to more practical information sifting and an interesting new mindset of not expecting immediate responses. Or, in another way of looking at it, respect of others' time. The abundance of tools and services, combined with a hacking culture, gives us ways to automate away conventional chores and time-blocking events to direct our time and efforts for more valuable tasks.
