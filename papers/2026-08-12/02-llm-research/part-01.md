# 🧠 大模型相关研究 | 2026年08月12日

> 本类共 **438** 篇论文：已确认 **404** 篇，待复核 **34** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-438](./part-09.md)

---

### 1. [Determinization in Structure Theories: A Unified Framework via Closure, Comparability, and Joint Admissibility](https://arxiv.org/abs/2608.07476)

**<font color=#1a73e8>作者：</font>** Hai Hai Fu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We develop a formal framework for constructing canonical interpretations from plural structure theories. A structure theory is a triple T = ({\Sigma}, A, I) consisting of a signature, axioms, and an inference policy, whose admissible interpretation family collects all globally consistent assignments of structural conclusions.
We distinguish three levels of canonicalization: closure stabilization (per-seed convergence), global completion (seed-independent convergence), and determinization (a unique admissible interpretation). Non-determinism is classified into epistemic plurality (Type E) and structural plurality (Type S), with a refined Type S-strong subclass characterized by the absence of common upper bounds.
Two canonicalization mechanisms arise: operator-based completion and selector-based construction. We provide sufficient structural conditions under which these mechanisms exist, and show that pure inference-based completion reduces to a saturated closure operator under positive, non-retractive rules with an additional soundness condition. For Type E theories, closure stabilization is established, while full determinization depends on a global confluence property that remains open. For Type S-strong theories, determinization is achieved via canonical selection.
We further show that multi-level canonicalization forms a structurally non-commutative system via staged operators, and provide a conditional classification theorem reducing theory-intrinsic mechanisms to closure or selection. The framework also applies to LLM-assisted reasoning, where hallucination can be viewed as unsupported canonicalization.

---


### 2. [PragyaDoc: A Universal Document Intelligence Framework for Multilingual Medical Document Understanding in Low-Resource Settings](https://arxiv.org/abs/2608.07478)

**<font color=#1a73e8>作者：</font>** Jagpal Singh Jhala  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> India's 22 official languages create a critical accessibility barrier: the majority of medical documentation exists exclusively in English, yet the patients who most urgently require this information - rural populations, ASHA workers, and patient families - are functionally excluded from understanding it. This paper presents PragyaDoc, a Universal Document Intelligence Framework that addresses this gap through a four-layer pipeline: a parallel ensemble OCR extraction layer, a geometric-lexical fusion layer, a deterministic domain structuring layer, and a dual-LLM medical reasoning and localization layer

---


### 3. [Cross-Model Humor Preference Modeling with Cards Against Humanity](https://arxiv.org/abs/2608.07481)

**<font color=#1a73e8>作者：</font>** Victor Winter, Farhan Lakhany  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper investigates whether one large language model can approximate the humor preferences of another in a controlled Cards Against Humanity-style task. Two models - GPT-4o as Czar and Claude Opus-4.5 as Player - are evaluated on a binary humor-selection task constructed so that success cannot follow from self-preference. A reflected-cell stability procedure isolates 244 hands on which the two models hold deterministic but opposite preferences, partitioned into a 97-hand context pool and a 147-hand held-out test pool. The Player is then evaluated across five graded conditions: default self-preference, generic Czar-modeling instruction, model-identified Czar, prior Czar selections, and prior Czar selections with rationales. This gradient is designed to separate two sources of improvement: framing effects, in which the Player is told to attend to a Czar without seeing any of the Czar's behavior, and direct behavioral evidence, in which the Player is shown the Czar's prior choices. Player accuracy increased from 0.7% in Condition 1 to 19.0% and 25.9% in the framing-only conditions, and then rose to 72.8% and 82.3% once behavioral evidence and rationales were provided. An omnibus Cochran's Q test and pairwise McNemar tests confirmed that each step in the gradient produced a significant improvement. The results indicate that role instruction and model identity yield only modest gains, while behavioral evidence - especially when accompanied by rationales - supports substantial cross-model preference modeling. The findings are interpreted as theory-of-mind-like behavior in an operational rather than representational sense: the Player shifts away from self-preference toward another agent's demonstrated preferences, without any claim about an underlying representation of mental states.

---


### 4. [From Human-Centered Design to Human-AI Collaboration: Why the Future of HCI Still Starts With People](https://arxiv.org/abs/2608.07482)

**<font color=#1a73e8>作者：</font>** Issam Alzouby  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI is reshaping HCI work by accelerating brainstorming, writing, prototyping, and interface generation. However, faster production does not automatically produce human-centered design. This position paper argues that GenAI should be treated not as a replacement for human-centered methods, but as a co-thinking partner driven by human goals, ethics, cognition, and accountability. After reflecting on HCI coursework, design activities, and AI-assisted workflows, I argue that traditional HCD principles become more important as AI systems become more capable. Users still bring limited attention, mental models, trust issues, and cognitive biases into interaction, while GenAI introduces new risks around over-reliance, de-skilling, shallow reasoning, hallucination, unclear authorship, and reduced accountability. The future of HCI should therefore focus on human-AI collaboration that preserves human agency, critical thinking, and responsibility.

---


### 5. [Generative AI as Support, Not Replacement, in Human-Centered Design](https://arxiv.org/abs/2608.07483)

**<font color=#1a73e8>作者：</font>** Amir Talakoob  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Traditional human-centered design is grounded in human needs, behaviors, and experiences, especially throughout the development of products and services. Recent advances in artificial intelligence and machine learning, accelerated by the public launch of ChatGPT in November 2022, have created a wave of AI adoption across research, industry, and design practice. While some of this rapid adoption reflects the current enthusiasm and overuse surrounding AI tools, it has also introduced lasting changes to how designers and researchers understand users, generate ideas, evaluate systems, and make design decisions. This position paper examines how AI is reshaping human-centered design and argues that some of these changes are likely to extend beyond short-term hype. It also considers the risks and limitations introduced by this shift, including over-reliance on AI, reduced human judgment, bias, data security concerns, and unclear accountability. Finally, the paper suggests that AI literacy, careful ethical judgment, and clearer boundaries for AI use are necessary for preserving the human-centered focus of design.

---


### 6. [Large Language Models Explain Experts Better Than Experts Themselves](https://arxiv.org/abs/2608.07488)

**<font color=#1a73e8>作者：</font>** Mina Cho, Russell J. Funk, Alok Gupta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Tacit knowledge, or the "know-how" embedded in experience, is difficult to articulate, making its transfer a challenge in organizations. Tacit knowledge is hard to externalize (transform into explicit knowledge), and expertise is often poorly documented and lost when experts leave. This study examines whether LLMs can externalize tacit knowledge from experts' behaviors and whether such externalized knowledge supports downstream decision-making and transfer to novices. Across two studies, we show that LLM-externalized tacit knowledge improves decision quality and enables novices to approach expert-level performance, often outperforming knowledge articulated by human experts. These findings provide empirical support for Polanyi's Paradox -- that we can know more than we can tell -- and highlight the potential of LLMs as scalable tools that can help overcome human experts' articulation bottleneck. Mechanism analyses and robustness checks show that LLMs meaningfully learn and extract knowledge from expert conversations, and findings generalize across models and retrieval methods.

---


### 7. [Experience-Sensitive Game Learning: A Behavioral Study of Humans and Language Agents](https://arxiv.org/abs/2608.07490)

**<font color=#1a73e8>作者：</font>** Yingying Guo, Zhuoxuan Ju, Ruibo Ming 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language model agents are increasingly evaluated through games, but most benchmarks emphasize final outcomes rather than how players learn from repeated interaction. We study experience-sensitive game learning: how gameplay experience changes the decision-making behavior of humans and language agents. We formulate experience-sensitive game learning as a framework for analyzing behavioral change across repeated gameplay, rather than only final score or win rate. We introduce a suite of interactive games with reusable strategic structure, together with cross-game greedy-to-global metrics and game-specific behavioral diagnostics that make experience-driven change observable from action traces. We also collect repeated-game trajectories from human players and evaluate recent self-evolving language agents in the same behavioral metric space. Our results show that human players exhibit interpretable and relatively stable shifts from locally greedy heuristics toward more global strategic decisions. In contrast, current self-evolving agents often show noisy and transient gains, suggesting that existing self-evolution methods remain limited in converting gameplay experience into durable changes in decision-making behavior.

---


### 8. [How to Ask the AI: A User Perspective Survey for Large Language Model Prompting](https://arxiv.org/abs/2608.07494)

**<font color=#1a73e8>作者：</font>** Yiqun Zhang, Yunfan Zhang, Mingjie Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI tools like ChatGPT and DeepSeek, powered by Large Language Models (LLMs), allow users to obtain instant and effective content responses simply by typing requests, such as ``plan a three-day Vienna trip'', ``solve the attached mathematical problem'', ``draft an email to inquire review progress'', etc., which are also known as LLM prompts. Crafting clear and well-structured prompts leads to more appropriate LLM feedback, which effectively bridges human-LLM interaction. Although prompting appears accessible to non-expert users, precisely organizing effective prompts is a highly systematic and skillful process, presenting potential challenges even for experienced users. This survey explores the principles, taxonomy, and organization of prompts from a user-centered perspective. Differing from the existing surveys that primarily focus on technical principles and application scenarios of LLMs, this paper provides actionable guidelines for formulating effective LLM prompts across diverse real-world tasks and specifically contributes by: 1) developing an intuitive evaluation strategy for prompt efficacy, 2) providing prompting workflow demonstrations on representative applications, and 3) maintaining a dynamically updated open-source project to ensure the core takeaways remain up-to-date. These measures lower the threshold for users to correctly understand and craft prompts that align with evolving application scenarios. This work will be maintained as a living GitHub project \href{this https URL}{\textcolor{blue}{here}}.

---


### 9. [EmoPatient: An Emotion-Directed Patient Simulator for Realistic Palliative Care Communication Training](https://arxiv.org/abs/2608.07495)

**<font color=#1a73e8>作者：</font>** Yining Wu, Tianshu Du, Jinrui Fang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Effective communication during palliative care discussions is a critical clinical skill, yet training clinicians to manage complex patient emotions remains challenging. Large language model (LLM)-based patient simulators provide a scalable approach for communication training, but most existing systems treat patient emotion as static and fail to capture the dynamic emotional shifts observed in clinical interactions. We present EmoPatient, an emotion-directed patient simulator designed to generate evolving emotional responses during palliative care discussions. The system introduces an Emotion Director agent that estimates the patient's emotional state and generates turn-level control signals for emotional intensity, regulatory stability, and interactional guidance. We evaluate EmoPatient through controlled multi-turn physician-patient dialogue simulations and compare it with baseline simulators. Results show improvements across four theory-informed emotional realism metrics and robustness across conversational personality variants, suggesting that modeling emotional dynamics can improve the realism of LLM-based patient simulators for palliative care communication training.

---


### 10. [Human-Simulation Interaction: From Prediction to Exploration in LLM Agent Simulations for Policy](https://arxiv.org/abs/2608.07496)

**<font color=#1a73e8>作者：</font>** Huanxing Chen  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Agent-based models have historically served as tools for generative explanation, constructing testbeds in which candidate micro-level behavioral rules can be tested for their capacity to produce observed macro-level phenomena. The integration of Large Language Models into agent-based simulation has expanded what these models can represent, but it has also introduced an unexamined shift in how users engage them. We argue that current generative agent-based models (GABMs) inherit the dominant interaction metaphor of conversational LLM interfaces - a question-answer pattern that positions users as consumers of system output rather than explorers of a possibility space. In the context of policy, where problems are wicked and ground truth is unknowable in advance, this metaphor produces a trust deficit that cannot be resolved through improved model accuracy alone. We open a design space we call human-simulation interaction, and argue that warranted trust requires interaction metaphors that restore the exploratory capacity simulation has historically supported.

---


### 11. [EvalConvoLearn: An Open-Source Framework for Evaluating Grounded Learner Simulations in Tutoring Conversations](https://arxiv.org/abs/2608.07497)

**<font color=#1a73e8>作者：</font>** Baptiste Moreau-Pernet  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Conversational learner simulations are valuable tools for testing learning theories, evaluating instructional materials and automated tutors, or powering teachable agents. Recently, large language models (LLM) have enabled richer, more naturalistic interactions with simulated learners; however, no open framework exists for evaluating whether such simulations faithfully reproduce real learner behavior. We introduce EvalConvoLearn, an open-source framework that assesses learner simulations along two axes: learning behavior (skill-conditioned mastery outcomes) and conversational quality (talk moves, error type distributions, question rate, turn length). EvalConvoLearn measures how closely a simulated learner approximates answer distributions observed in data by grounding metrics in authentic tutoring conversation datasets, and anchoring generated tutor responses in existing tutor utterances. The framework is demonstrated on a dataset of tutoring dialogues, including results for two LLM-based learner simulations, and the published GitHub code.

---


### 12. [Knowing You Is Everything: LLM Agents Achieve Near-Perfect Profile-Consistent Reaction Prediction in Social Media Simulation](https://arxiv.org/abs/2608.07498)

**<font color=#1a73e8>作者：</font>** Ljubisa Bojic, Ljiljana Matic, Joerg Matthes 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Autonomous AI agents in social media present concrete risks to democratic discourse and platform governance, while also offering tools for pre-deployment recommender system testing. A central open question is whether persona-prompted LLMs can simulate individual-level social media reactions with sufficient accuracy to support either application, and how accuracy depends on profile completeness, model selection, and the generalization challenge posed by novel post content. This study benchmarks twelve LLM configurations on binary like/dislike prediction across 296 survey-based agent profiles and 26 ground-truth-mapped posts under three profile conditions, with leave-post-out machine learning classifiers as baselines. Across full-profile conditions, accuracy ranges from 75.54% to 96.68%, with a 30-point spread attributable primarily to model selection and confirmed by paired McNemar tests with agent-level bootstrap intervals. GPT-5.5 Pro accuracy degrades monotonically from 96.68% under a full profile to 62.32% under a reduced profile and to 51.00% with demographics alone, the last indistinguishable from the majority-class baseline, which confirms that demographic inference provides negligible predictive signal. Supervised classifiers collapse to 15.4% under leave-post-out, while LLMs sustain genuine zero-shot generalization unavailable to trained methods. Adaptive reasoning improves accuracy substantially for some models. Inter-model agreement is nearly double for posts with direct profile anchors (mean \k{appa} = 0.44) than for posts without them (\k{appa} = 0.23), and the least heterogeneous configuration homogenizes 34% of simulated population reactions. Results validate LLM-based simulation for recommender system stress-testing while documenting the behavioral accuracy that makes large-scale synthetic agent swarms a credible threat to public opinion.

---


### 13. [Evaluation of Motivational Interviewing Counsellors with Task-Aware Multi-Stage LLM-Based Simulated Clients](https://arxiv.org/abs/2608.07499)

**<font color=#1a73e8>作者：</font>** Jiading Zhu, Xinyu Cindy Wang, Thomas Nguyen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The development and benchmarking of Large Language Model (LLM)-based Motivational Interviewing (MI) counsellors now often rely on LLM-based simulated clients. Prior work on simulated clients, however, has not aligned with the specific tasks fundamental to the MI therapy approach. A key task is evoking, in which the counsellor first elicits the client's ambivalence and then strengthens the client's motivation for change. We present Evoke-Sim, a task-aware, multi-stage LLM-based client simulation framework for evaluating MI counsellors in smoking cessation, designed specifically for the evoking MI task. Evoke-Sim employs structured client profiles, an evoking-specific three-stage conversation flow, and a reveal policy that regulates which client profile information might be disclosed at each stage. We show that compared to existing profile-grounded simulated clients, Evoke-Sim is better at differentiating levels of MI quality using task-aware evaluation metrics, while reducing non-grounded client statements and premature disclosure of client information, setting a higher standard for the evaluation of LLM-based MI counsellors.

---


### 14. [Exploring AI-Supported Disciplinary Mediation in Student Project Teams' Text-Based Communication](https://arxiv.org/abs/2608.07503)

**<font color=#1a73e8>作者：</font>** Ching-Jung Cheng, Yu-Chan Chung, Bing-Chen Chiu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Interdisciplinary project-based learning requires students to negotiate differences in language, assumptions, priorities, and working practices. These differences are difficult to surface in text-based team communication, where discussions can become fragmented and AI tools are often used as private side channels rather than shared supports for collective sensemaking. We present Spritz, a Discord-based LLM technology probe that explores how AI might mediate disciplinary boundaries in student project teams. Spritz monitors group chat for signals of semantic or pragmatic boundaries, prompts members to articulate their perspectives through private channels, and returns anonymized syntheses to the shared discussion. We conducted a technology probe study and co-design workshop with 12 university students from technical, business, and design backgrounds. Participants experienced Spritz during a simulated interdisciplinary resource-allocation task and reflected on AI's role in collaboration. Findings show that participants valued AI mediation not only as cognitive support for boundary crossing, but also as a relational buffer. Spritz helped organize fragmented discussion, surface implicit expectations, and clarify divergent interpretations, while softening interpersonal pressure around disagreement and concession. Participants further imagined future AI mediators as switchable roles, including strategic advisors, cross-domain translators, and perspective challengers. However, these expanded roles introduced a central design tension: the neutrality that made AI acceptable as a mediator became unstable when AI began to advise, challenge, or influence team decisions. We contribute empirical insights and design considerations for AI systems that mediate interdisciplinary collaboration in text-based communication while preserving human agency, trust, privacy, and accountability.

---


### 15. [Innovating with Generative AI: A Human Bottleneck Framework](https://arxiv.org/abs/2608.07504)

**<font color=#1a73e8>作者：</font>** Julian De Freitas, Ayelet Israeli, Gideon Nave 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We propose a human bottleneck perspective for understanding how generative AI transforms the innovation process. The central premise is that many constraints traditionally plaguing the innovation process are cognitive and social in origin, rooted in how people generate ideas, evaluate novelty, and communicate through social systems. Generative AI does not act uniformly on these constraints. At each stage, it can deepen some bottlenecks while alleviating others, and predicting these outcomes requires understanding the underlying mechanisms of the constraint itself. We identify bottlenecks in four stages of the innovation process: ideation, screening and testing, preference measurement and consumer insight, diffusion, and market learning. By grounding analysis in human behavior rather than rapidly changing AI capabilities, we offer a framework for assessing whether new developments alleviate or intensify the bottlenecks that matter most at each stage. We also distinguish bottlenecks likely to narrow as capabilities improve from those rooted in enduring human constraints. We further discuss AI-related issues that cut across the entire innovation pipeline, challenging the very existence and structure of the traditional innovation process.

---


### 16. [What We Risk Losing When Creating Gets Easy: Friction, Judgment, and Critical Reflective Practice with Generative AI in Creative Work](https://arxiv.org/abs/2608.07506)

**<font color=#1a73e8>作者：</font>** Shehryar Saharan, Shehroze Saharan, Roxanne Ziman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> GenAI in creative practice can help narrow the gap between intention and output, but in so doing changes the very nature of that creative process. In this position paper, we argue that the friction of making is not overhead to be removed, but essential to creative work: the resistance through which judgment is built and refined. Rejecting both outright refusal and uncritical adoption, we call for critical reflective practice: the deliberate, ongoing, and situated weighing of when to use or refuse GenAI in creative work, treating the formation of judgment as an epistemic virtue that design and pedagogy should (continue to) uphold. Two voices, the GenAI Skeptic and GenAI Enthusiast, drawn from our professional and personal experiences, argue with each other and with us throughout. We close with open questions for researchers, educators, and practitioners navigating the grey areas of GenAI in creative practice.

---


### 17. [Visual Reconstruction as Memory Negotiation: An Iterative Generative AI-Mediated Framework for Oral History](https://arxiv.org/abs/2608.07507)

**<font color=#1a73e8>作者：</font>** Yigeng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Oral history and community memory are core resources for historical inquiry, yet spatial and material aspects of remembered scenes can be difficult to externalize and compare when they circulate primarily through verbal exchange. This poster proposes an Iterative AI-Assisted Framework for Visual Reconstruction and Memory Negotiation that uses generative AI not to verify memory or produce definitive reconstructions but to create provisional visual 'probes' that support discussion, revision, and comparison. Grounded in oral history and memory studies and informed by digital humanities critiques of visual authority, the workflow proceeds in five stages: (1) narrative elicitation; (2) generative visual prototyping; (3) participant-led iterative revision (human-in-the-loop); (4) multi-narrator comparison and negotiation; and (5) a negotiated reconstruction archive that preserves final images, intermediate iterations, and records of agreement, uncertainty, and disagreement. A vignette illustrates the method through two elders recalling a no-longer-extant building. The poster highlights ethical and methodological constraints, especially the tendency of compelling images to anchor interpretation, and treats outputs as interpretive artifacts rather than evidence. By archiving negotiation traces alongside visual outputs, the approach supports reflexive public-history engagement and responsible documentation in contexts of visual archive scarcity.

---


### 18. [JaleesBench: Are AI Assistants Good Spiritual Company?](https://arxiv.org/abs/2608.07508)

**<font color=#1a73e8>作者：</font>** M. Waleed Kadous, Benjamin Olsen  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models are already advisors to millions of people of faith who bring them real decisions. The pressing question for a person of faith is not what a model knows or professes but what its counsel does to the person who receives it. We introduce JaleesBench, which measures whether an AI agent is a righteous companion, judged by the residue an exchange leaves on the user, in the manner of the perfume-seller and the blacksmith. It comprises 140 two-turn scenarios drawn from a classical compilation organized by virtue (Riyad al-Salihin), under six adversarial pressures and three framings, scored by two frontier judges against each scenario's own supporting texts. Across eight systems: (1) generic frontier models are only middling companions out of the box but a one-page guide makes them genuinely good ones, on par with the domain-tuned assistant: the frontier APIs climb from +0.28/+0.23 to a Guided +0.84-0.87, so most of the expert's edge is companionship instruction that fits in a prompt; (2) every system caves under relational pressure, insistence and personal appeal; (3) the domain-tuned assistant's advantage is overwhelmingly its retrieval-and-prompting layer, not its base model (+0.74 over the identical underlying model); and (4) it can be used to improve existing systems: guided by its diagnosis, a single steadfastness instruction lifts a deployed Islamic assistant from +0.48 to +0.84 (Faith unstated, after pressure), matching the best guided frontier systems while preserving first-response quality. The construct is faith-general; we instantiate it for Islam as the first of a planned cross-tradition family. Code, scenario bank, and rubric are open source (this http URL), with an interactive results browser at this http URL.

---


### 19. [PIVOT: Preference-based Intervention Vectors for Pedagogical Tutor Steering](https://arxiv.org/abs/2608.07509)

**<font color=#1a73e8>作者：</font>** Fares Fawzi, Jiaxu Zhao, Tanya Nazaretsky 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly used for conversational tutoring, but effective tutoring requires more than correct answers. Tutors must choose when to scaffold reasoning, hint, give feedback, explain, or invite reflection. Existing prompting and training methods improve pedagogical alignment, but lack reliable inference-time control over pedagogical strategies. We introduce PIVOT, an activation-steering framework that learns preference-based intervention vectors online for frozen LLM tutors. PIVOT uses a seven-category tutor-move taxonomy and a generate-label-optimise loop, where a human-validated LLM judge identifies target and confusable non-target moves to construct preference pairs for multi-layer residual-stream steering. Across held-out and out-of-domain tutoring data, PIVOT controls tutor moves while preserving relevance and fluency, and its directions can be scaled, transferred, and composed at inference time. In a user study with 30 teachers, 73.3% of participants preferred steered conversations over neutral baseline interactions using the same prompt, and rated the controls as clear, usable, and pedagogically meaningful.

---


### 20. [How sensitive do we want AI to be? Socio-communicative competencies of large language models in healthcare](https://arxiv.org/abs/2608.07511)

**<font color=#1a73e8>作者：</font>** Dorothee Amelung, Andrew M. Bean, Sabine C. Herpertz 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Background. Effective clinical practice relies heavily on the socio-communicative skills of medical professionals. Large language models (LLMs) have been proposed for tasks such as triaging patients, report drafting or translating medical jargon to support informed decision-making. These applications require both factual and social competence. This study evaluates dialogues between LLMs and participants to assess the current state of socio-communicative competencies displayed in LLM-generated texts.
Methods. We extracted a subset of extended dialogues from the HELP-Med dataset, comprising 1800 conversation transcripts of interactions between human participants seeking medical information and three different LLMs, GPT 4o, Llama 3 and Command R+. Two experts coded the transcripts for demonstrations of socio-communicative behaviours (non-hostility, sensitivity, structuring, non-intrusiveness) using the IC-MD instrument, originally designed to evaluate interactional competencies in medical student admissions.
Results. The LLMs in our study showed strength in non-hostility, mixed results in sensitivity and non-intrusiveness and performed poorly in structuring.
Conclusion. Current LLMs lack the consistent and reliable socio-communicative skills needed for safe and effective use as healthcare advisors. While existing frameworks for assessing interactional competencies may support the development of more socially responsive LLMs, they will require adaptation to account for the differences in desirable behaviour between humans and LLMs.

---


### 21. [EMMR: Emotion-Mediated Multimodal Reasoning for Personality Assessment in Asynchronous Video Interviews](https://arxiv.org/abs/2608.07512)

**<font color=#1a73e8>作者：</font>** Dongsheng Hu, Tianyi Zhang, Chuang Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Asynchronous Video Interviews (AVIs) have become increasingly popular for personality assessment. Recent large language models (LLMs) have shown potential for personality assessment from transcribed interview responses. However, text-centered methods may overlook non-verbal behavioral cues conveyed through visual and audio modalities, even though such cues are highly relevant to personality assessment. In particular, emotion-related cues provide important social and affective evidence for understanding candidates' behavior related to personality traits. Thus, we propose EMMR (Emotion-Mediated Multimodal Reasoning), a two-stage framework for MLLMs-based personality assessment for AVIs. EMMR extracts emotion-related cues from multimodal interview data and incorporates them into personality assessment through structured reasoning as auxiliary social and behavioral evidence. Experiments on two AVIs datasets, OPVA and AVI-6, show that EMMR improves MAE, MSE, and PCC compared with baselines. Further analysis indicates that semantic descriptions of emotion cues enhance personality assessment, while their quality affects personality assessment reliability. These results suggest that integrating emotion-related cues into multimodal reasoning is a promising direction for more interpretable MLLMs-based personality assessment in AVIs.

---


### 22. [Catch the Patient, Not the AI: Collective Sensemaking in an Online Health Community](https://arxiv.org/abs/2608.07516)

**<font color=#1a73e8>作者：</font>** Feng He  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Patients and caregivers increasingly use artificial intelligence (AI) tools to interpret medical reports, weigh care decisions, and seek emotional support. Yet most research treats patient-facing AI as a private exchange between a user and a system. This study examines how AI-related content is taken up once users carry it back into the peer communities, using data from House086, China's largest online community for lymphoma patients and caregivers. We identified roughly 400 publicly accessible threads (2014-2026) through keyword searches and manual screening, extracted them into structured case profiles using a schema-prompted large language model, and conducted mixed-method analysis. After quality control, the verified analytic sample comprised 337 post-ChatGPT records. Members most often reported using AI for informational support, followed by second opinions and psychosocial support. Although members often introduced AI favorably, roughly one in six described feeling overwhelmed by AI output. When other members responded, they frequently engaged the poster's underlying medical or emotional intent while leaving the AI dimension unaddressed. This tendency persisted even in threads seeking triangulation between AI output and other information sources. When members did discuss the AI, they were more often cautious than endorsing. Rather than systematically auditing AI output, the community more often worked to deflate the false certainty it produced, placing a single AI answer back among multiple sources of judgment. This study argues that AI does not replace the interpretive work of online health communities, nor is it systematically audited by them. Instead, it shifts the locus of sensemaking downstream, so that the community continues to catch the person even when it does not catch the AI.

---


### 23. [The Judge Knows When It Knows: Calibrated Abstention for LLM-Based A/B-Test Prediction](https://arxiv.org/abs/2608.07517)

**<font color=#1a73e8>作者：</font>** Tyler Dooskin, Squoosh Technical Staff  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Can a multimodal LLM predict which version of a web page will win a real A/B test from screenshots alone? We report the most complete answer we are aware of, from six weeks of pre-registered experiments on real conversion tests: mostly no -- and the exceptions are identifiable in advance. On 330 real A/B tests a Gemini 3 Flash judge reaches Cohen's kappa = 0.14, but on the trustworthy (statistically significant) half of the labels the evidence is inconclusive (kappa = 0.11, CI includes zero). We show that 44% of the "ground-truth" labels in a leading CRO agency's catalog come from non-significant tests, and that the judge agrees more with the unreliable labels than the reliable ones -- a shared prior between labeler and model, not prediction. Every standard improvement lever (a 2.8x more expensive frontier model, prompt redesign, stimulus fidelity, change-type priors) fails its pre-registered gate. The judge's confident calls are different: a vote-margin gate isolates a subset (49% coverage) reaching kappa = 0.31 on significant labels. We measure the mechanism directly -- judges differing in model or prompt agree with each other at kappa = 0.74-0.88 while agreeing with real outcomes at only ~0.2, so a 16-vote panel carries about 2 effective independent votes -- and we reproduce it in humans: 15 CRO experts agree with each other (inter-rater kappa = 0.53) but score at chance against real outcomes (kappa ~ 0). Consensus, human or model, is reproducible, persuasive, and not evidence. We release our pre-registrations, locked gates, negative results, statistical harness, human responses, and a claims ledger in which every number carries an evidence tier.

---


### 24. [CyberSelf: Embodied Self-Distancing for Emotional Support in Virtual Reality](https://arxiv.org/abs/2608.07521)

**<font color=#1a73e8>作者：</font>** Bing Li, Dr Yan Hu, Tinghui Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Self-distancing is an effective emotion regulation strategy; however, it may fail during personal crises due to its cognitive demands. Virtual Reality (VR) provides a novel approach to externalizing psychological distance by enabling embodied self-representation. In this paper, we present CyberSelf, a VR system for emotional support that integrates a visually self-resembling avatar, a cloned self-voice, and Large Language Model (LLM)-driven real-time dialogue. The system enables users to engage in multi-turn conversations with their self-representations in immersive VR, enabling embodied self-distancing while maintaining a strong sense of self-relevance. We evaluated CyberSelf in a short-term study that compares three levels of self-representation richness (Text, Text+Voice, and Text+Voice+Appearance). The results demonstrated robust pre-post improvements across affective and coping measures, specifically increased valence, arousal, hope, and resilience, as well as reduced anxiety and simulator sickness. Richer representations increased conversational engagement, and full embodiment produced the strongest physiological indicators of emotional regulation. A subsequent four-week long-term study demonstrated that these benefits are both sustainable and cumulative. Additionally, users rated the reconstructed avatar and the cloned voice as highly recognizable and acceptable. Collectively, these findings suggest that embodied, self-resembling conversational agents provide a viable mechanism for externalizing self-distancing and supporting emotional regulation in VR.

---


### 25. [Unified Hallucination Fuzzing for Multimodal Large Language Models](https://arxiv.org/abs/2608.07525)

**<font color=#1a73e8>作者：</font>** Pengfei Zhou, Jiajun Song, Zhiwei Tang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hallucination remains a persistent challenge for Multimodal Large Language Models (MLLMs), severely limiting their reliability in high-stakes applications. Existing evaluations, predominantly based on static benchmarks, suffer from narrow taxonomical coverage and rapid performance saturation, failing to reflect model robustness in evolving real-world scenarios. To bridge this gap, we present a systematic evaluation framework integrating a comprehensive benchmark with self-evolving stress testing. First, we introduce UniHall, a fine-grained dataset grounded in a unified taxonomy spanning Object, Instruction, and Knowledge dimensions. Second, to address benchmark saturation, we propose Self-Adaptive Multimodal Fuzzing (SAMF), a self-adaptive framework that employs evolutionary mutation strategies to explore the boundaries of model hallucinations. Crucially, to ensure reliable assessment of dynamic inputs, SAMF incorporates a structured metric suite driven by an ensemble of multi-modal oracles. Our extensive experiments reveal that state-of-the-art MLLMs exhibit significant performance degradation under fuzzing compared to conventional settings, exposing a dissociation between reasoning capabilities and factual grounding. Furthermore, we identify a helpfulness-hallucination trade-off, where reinforcement learning alignment inadvertently exacerbates sycophancy in instruction-following tasks. The framework, code and benchmark are available at this https URL.

---


### 26. [DocAtlas: Long-Document Understanding as Mutable-State Interaction](https://arxiv.org/abs/2608.07527)

**<font color=#1a73e8>作者：</font>** Hongchen Wei, Yuanzhe Wang, Bei Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-document understanding requires models to find and combine evidence across many pages, layouts, tables, figures, and charts. Existing retrieval-augmented systems usually select evidence from a static index before generation, while recent agentic systems add multi-turn tool use but often rely on frozen proprietary backbones whose behavior is set by prompts. We present DocAtlas, a system that treats long-document understanding as a mutable-state information-seeking process. We instantiate DocAtlas as a mutable document harness: an external environment that determines what document information is searched, read, stored, reviewed, and shown to the model at each step. Given a document and question, the harness exposes search, reading, note-taking, and review tools, maintains a hierarchical tree and note store, and updates both as the agent records evidence. DocAtlas combines self-improving retrieval, selective evidence access, and active working memory under a fixed context budget. The same harness supports inference-time use with large VLMs and end-to-end reinforcement learning for compact VLM agents. With GPT-5.4, DocAtlas reaches 71.4\% on MMLongBench-Doc, exceeding the human-expert reference of 65.8\%. A Qwen3.5-4B VLM trained with end-to-end RL in the DocAtlas environment reaches 63.7\%, compared with a 54.4\% direct-input baseline, showing that mutable document-harness design can improve compact document agents by a large margin.

---


### 27. [The Knowing-Saying Gap: When Probes See Errors that Confidence Misses](https://arxiv.org/abs/2608.07528)

**<font color=#1a73e8>作者：</font>** Jyotin Goel, Ipshita Bandyopadhyay, Justin Shenk  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Linear probes detect corrupted context in language models with near-perfect accuracy, yet this does not translate into reliable failure prediction. The result is a dissociation with direct implications for deployment monitoring. Across multi-hop arithmetic chains, probes that detect corruption turn out to be uninformative about final answer correctness; models forced into structured confidence formats collapse to two values with indistinguishable error rates; and probe persistence across hops fails to separate correct from incorrect outcomes, refuting our pre-registered "persistence beats peak" hypothesis. This pattern of knowing but not saying generalises across model families including reasoning models. As a real-time monitor, probe-based interventions are sharply model and error-type dependent: branch-and-pick is net-positive across models and uniquely non-breaking on Llama-3.1-8B (4 rescued, 0 broken), while reprompt and replace-prior break correct traces at roughly the rate they rescue wrong ones. Probe-based monitoring is a necessary complement to verbalised confidence, but no single intervention dominates, and the deployable answer is model-aware, error-type-aware routing.

---


### 28. [WuYuEval: A Multi-Level Benchmark for Large Language Models in Solid Waste Management](https://arxiv.org/abs/2608.07529)

**<font color=#1a73e8>作者：</font>** Yi Zhang, Hongyang Wang, Zheng Hao Leong 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as technical assistants, but their competence in solid waste management (SWM) remains difficult to assess because existing benchmarks emphasize general knowledge rather than professional decisions under engineering, environmental, and policy constraints. We introduce WuYuEval, a multi-level benchmark for evaluating LLMs in SWM across foundational knowledge, domain reasoning, and expert decision-making. After quality auditing, WuYuEval contains a Foundation Module with 4,590 closed-ended multiple-choice questions across six task types and eight domain categories, together with an Expert Module with 247 scenario-based open-ended questions involving multi-objective optimization, constraint trade-offs, and system design. For expert tasks, we combine anchor-calibrated LLM-as-a-Judge scoring with Elo-based pairwise comparison. Across 33 LLMs, performance varied widely. The leading model reached 94.64\% accuracy on the Foundation Module, but average accuracy still fell from 84.14\% on easy questions to 42.50\% on hard questions, with lower performance concentrated in calculation, experimental design, urban planning, and open-ended expert tasks. Reasoning-oriented Thinking modes improve most matched model pairs after auditing, but the gains depend on baseline capability and are not uniformly positive. These results suggest that visible deliberation helps only when it remains anchored to units, assumptions, and engineering constraints; otherwise, it may drift from decisive answer boundaries. WuYuEval therefore provides both an evaluation resource and an empirical basis for developing SWM-oriented foundation models with professional reasoning chains and explicit constraint control.

---


### 29. [NL2SHACL-Bench: A Benchmark Suite for Natural Language to SHACL Translation](https://arxiv.org/abs/2608.07530)

**<font color=#1a73e8>作者：</font>** Yuchen Zhou, Niels Bobet, Maribel Acosta  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> SHACL is a core technology for validating the conformance of RDF knowledge graphs (KGs). Yet, authoring SHACL shapes requires technical expertise that most domain experts lack. Translating natural language requirements into SHACL (NL2SHACL) would lower this barrier. However, there is no dedicated benchmark for NL2SHACL, and evaluating generated shapes requires methods beyond string comparison, as semantically equivalent shapes can differ in serialisation and structure. To tackle these challenges, we present NL2SHACL-Bench, a benchmark suite for natural language to SHACL translation. Using NL2SHACL-Bench, we evaluate four state-of-the-art large language models (LLMs) for this task. Our results show that current LLMs are highly capable of generating syntactically valid SHACL, but still struggle to produce semantically equivalent constraints for complex logical and structural patterns. This indicates that NL2SHACL-Bench provides a meaningful basis for measuring advances in the NL2SHACL state of the art.

---


### 30. [Search-G1: Grounded Search Agents via Representation-Based Intrinsic Rewards](https://arxiv.org/abs/2608.07531)

**<font color=#1a73e8>作者：</font>** Cheng Ruoxi, Ma Haoxuan, Zhang Hongyi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Search-augmented language agents should retrieve external information only when necessary and ground their answers in retrieved evidence. Existing external rewards provide either sparse outcome supervision or richer feedback from process annotations and LLM judges. Outcome rewards scale readily but cannot distinguish grounded retrieval from redundant search, whereas richer signals require costly annotation or inference during training. Internal rewards based on policy-side signals such as entropy, likelihood, or information gain are graded and inexpensive to evaluate, yet mainly reflect model confidence rather than evidence grounding. We propose Search-G1, a representation-based intrinsic reward framework that measures the operational grounding of an agent's answers through two intervention-calibrated readouts. A prompt-state readout predicts closed-book sufficiency, whose complement defines policy-relative retrieval necessity; an answer-commit readout estimates evidence reliance from answer-stage sensitivity to evidence deletion. Together, they provide additional credit to correct searched trajectories when retrieval is estimated necessary and the answer is evidence-sensitive, favor correct direct answers when closed-book knowledge suffices, and penalize repeated search. After calibration, reward scoring requires neither process annotations nor LLM-as-judge inference during policy optimization. Because reinforcement learning changes policy representations, Search-G1 periodically refits both readouts on trajectories from the latest checkpoint, allowing the reward to co-evolve with the policy. Experiments across multiple search-based question-answering benchmarks and two model scales show that Search-G1 improves the grounding--search-cost trade-off, producing shorter response-side trajectories at competitive task accuracy. Code is available at this https URL.

---


### 31. [Dynamic Coalition Formation and Communication Pricing in Skill-Based Agentic AI Systems](https://arxiv.org/abs/2608.07532)

**<font color=#1a73e8>作者：</font>** Mojtaba Eslami  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern agentic AI systems combine multiple large language model agents with heterogeneous skills, yet most architectures either fix communication in advance or allow full broadcast. Both can be inefficient because token cost, latency, redundancy, and error propagation increase with the number of active agents and communication links. We model agent selection and communication as a cooperative game with task-conditioned net utility $U(C\mid x)=V(C\mid x)-\sum_{i\in C}c_i$, separating coalition-level costs from agent activation costs. We propose a marginal-value activation rule and greedy router, extend the model to optimize communication edges with per-edge costs, and use estimated Shapley values to predict which agents are worth contacting before and during execution. We connect the problem to submodular maximization and prove two limited guarantees: a curvature-refined bound for a monotone, cardinality-constrained special case, and a tight $1/2$-approximation, with a correction for signed objectives, for an unconstrained non-monotone case via double greedy. Neither guarantee applies directly to the main router, which remains a heuristic. We also prove a Shapley-submodularity sandwich bound linking the error of marginal-value routing to a per-agent diminishing-returns quantity. In synthetic experiments, greedy routing achieves $99.5%$ of brute-force-optimal utility while activating $1.96$ of $8$ agents on average, compared with $38.8%$ for full broadcast. Performance is robust to activation cost and redundancy weight but falls to $66%$ under strong violations of submodularity or noisy value estimates. We distinguish the framework from Shapley pricing, hedonic coalition formation, and communication-graph pruning, and propose evaluation on real multi-agent LLM benchmarks.

---


### 32. [MetaSpace: Metamorphic Testing for Spatial Cognition in Embodied Agents](https://arxiv.org/abs/2608.07533)

**<font color=#1a73e8>作者：</font>** Gengyang Xu, Dongwei Xiao, Yiteng Peng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An embodied agent is an intelligent entity that interacts with its environment through a physical body. Currently, the evaluation of embodied agents primarily relies on two paradigms: (1) manually annotated Visual Question Answering (VQA) pairs and (2) high-level task completion metrics, such as success in navigation or manipulation. The former is labor-intensive and subject to variability in annotation quality. The latter may obscure critical vulnerabilities, allowing agents to complete tasks through suboptimal means or safety violations, thereby concealing safety risks and inefficiencies. Given that spatial cognition is the cornerstone for executing embodied tasks, there is a pressing need to assess whether embodied agents possess robust spatial cognition during task execution.
Inspired by metamorphic testing principles in software engineering, we propose MetaSpace, a novel framework designed to evaluate the spatial cognition of agents. By leveraging spatiotemporal multimodal states derived from real execution trajectories, MetaSpace automatically generates test cases based on predefined metamorphic relations (MRs) grounded in logical rules and physical laws. Crucially, we encode these MRs as executable rules in a logic programming language (Prolog). Violations of these relations indicate failures in spatial cognition. Our empirical evaluation across three embodied scenarios demonstrates that MetaSpace successfully detects 90,422 spatial cognition errors in state-of-the-art (SOTA) MLLM-driven agents. We introduce the Spatial Cognition (SC) score to quantify performance. Results indicate that all SOTA agents achieve average scores between 0.44 and 0.52, significantly lower than the human benchmark of 0.96.

---


### 33. [When LLM Agents Negotiate: Private Information and Dynamic Bargaining in Supply Chains](https://arxiv.org/abs/2608.07538)

**<font color=#1a73e8>作者：</font>** Chen Liang, Fasheng Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLM agents move from decision support to autonomous procurement, firms need to know whether delegated negotiators create value, divide it predictably, and avoid money-losing contracts. We study this in a canonical supply chain bargaining problem: a buyer with private demand information negotiates a quantity-payment contract with an uninformed seller. We benchmark nine LLMs from OpenAI, Google, and Alibaba against a validated Perfect Bayesian Equilibrium across 9,840 LLM-to-LLM negotiations. First, capability governs value creation. Agents agree in 98.9% of negotiations and capture 95.4% of first-best surplus undiscounted, but average 2.98 rounds against the benchmark's 1.25, and this delay erodes 21-34% of surplus. Capability also governs reliability: baseline models accept individually irrational contracts in 19.2% of cases, versus 0.0-0.6% at mid-tier and flagship, making automated profit verification the binding guardrail below that threshold. Second, surplus capture is relational. Provider identity predicts who captures surplus better than capability rank: self-play buyer shares average 40% for OpenAI, 50% for Google, and 70% for Alibaba's Qwen, an ordering that survives restricted communication and no discounting. Reversing which provider sells moves the division by 7-18 percentage points, and the capable Qwen flagship is the weakest cross-family seller: vendor choice is a first-order distributional decision. Third, the prompt is a strategic lever. Delegation separates the principal's economic patience from the agent's prompted strategic patience, a free deployment choice that is the single strongest driver of surplus division (90% of explained variance). Together these establish an equilibrium-referenced audit of AI agents along three dimensions: discounted efficiency, distributional profile, and operational reliability.

---


### 34. [TREAT: Evaluating Access to Formal Knowledge across Equivalent Mathematical Representations](https://arxiv.org/abs/2608.07540)

**<font color=#1a73e8>作者：</font>** Fateme Mazdarani, Carlos Toxtli  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI systems increasingly operate between flexible input representations and formal objects used by downstream tools. A key challenge is recognizing when an unfamiliar formulation denotes a known formal object. We study this challenge through theorem recognition: given an equivalence-preserving transformation of a theorem condition, a model must recover the theorem identity associated with the standard statement. We introduce TREAT, a benchmark for evaluating whether large language models can recover known theorem identities from equivalence-preserving formula-level transformations. Rather than paraphrasing theorem text, TREAT changes the mathematical form of theorem conditions themselves, expressing known results through residual equations, witness statements, optimization identities, set relations, operator forms, and proof-intermediate characterizations. Starting from scraped theorem pages, we filter for entries with usable mathematical expression forms, extract canonical theorem conditions, and generate transformed variants with recorded assumptions and inverse mappings. The final corpus contains 737 theorem identities and 29,480 transformed rows. On a test panel, the best model retrieves the correct theorem identity in only 60.73% of cases. Other systems reveal different failure modes, including abstention, wrong detection, and malformed outputs. These suggest that theorem knowledge can be fragile under equivalent changes in representation. TREAT therefore provides a controlled testbed for evaluating representation-robust access to formal knowledge, with broader relevance to domains that require stable target objects, explicit equivalence relations, validation procedures, and auditable scoring.

---


### 35. [NeuroPilot: An Agent-Driven Smart Pipeline for Processing, Quality Control, and Managing Neuroimages](https://arxiv.org/abs/2608.07541)

**<font color=#1a73e8>作者：</font>** Yiyao Chen, Yucheng Li, Jungong Tong 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transforming raw neuroimage archives into analysis-ready derivatives relies on three brittle stages: data standardization, modality-specific preprocessing, and quality control (QC). While individual neuroimaging tools are well developed, their orchestration requires project-specific scripts, environment-adaptive tuning, and labor-intensive manual QC. To address this, we introduce NeuroPilot, a multi-agent system that digitalizes the expertise of neuroimage processing, QC, and data management into three LLM-invocable skills: dcm2bids-skill, neuroimage-pre-skill, and qc-agent-skill. The LLM-driven agent autonomously orchestrates workflows, generalizing various infrastructure settings into a single configuration to achieve the highest scalability. Demonstrating the system's generalizability, we deployed NeuroPilot across 17 cohorts (>123,000 subjects) spanning infant to aging populations and multiple MRI modalities (structural, diffusion, functional). In practice, after standardizing data via the dcm2bids-skill, the agent dynamically routes datasets to the optimal neuroimage-pre-skill based on available modalities and cohort traits (e.g., dispatching T1w and fMRI data to fMRIPrep, or selecting specialized pipelines for infant cohorts). The qc-agent-skill then drives an evidence-based, semi-automated QC via a 3-D browser dashboard, utilizing a multi-tiered verification system to optimize failed cases and escalate complex issues for supervisor inspection. Quantitatively, our QC agent screened 558 production subjects, validating its automated flags against FreeSurfer's topology-defect metrics. The infant processing pipeline achieved a 100% (201/201) completion rate on QC-validated inputs. Importantly, NeuroPilot compresses the traditional 2--3 month timeline for training staff and processing complete datasets into a single week. NeuroPilot is deployed in this https URL.

---


### 36. [An AI Scientist that Doesn't Drift: Taste, Structure, and Falsifiable Findings in a Quadruped Navigation Research Loop](https://arxiv.org/abs/2608.07542)

**<font color=#1a73e8>作者：</font>** Yiwen Zhang, Eloise Zeng, Jaeha Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous research loops driven by large language models can run machine-learning experiments at scale but tend to drift toward local refinements of whichever metric they optimise rather than testing the hypotheses that motivate the experiments. We address this structurally and present an AI Scientist for studying generalisation in quadruped robot navigation policies in simulation. Building on the autoresearch paradigm of Karpathy, our loop adds three components: an immutable experiment card that pairs each iteration's prediction with its outcome under a fixed schema, so a falsified hypothesis cannot be retconned; specialised subagents restricted to mechanical roles; and kkanbu, a preference oracle that holds the user's research taste as a typed knowledge graph and is the only component permitted to make subjective judgements. To isolate the oracle we run the identical loop twice across eleven research streams, with and without kkanbu. Neither arm drifts: both falsify roughly three quarters of their own hypotheses, and the best trained policy comes from the oracle-less arm. What the oracle changes is direction, not score: it alone explores test-time adaptation, it authored the winning designs where its arm led, and it carried lessons across streams that the other arm repeatedly re-derived. The scaffold keeps the loop honest; kkanbu decides where it looks.

---


### 37. [Performance of large language models in the optical diagnosis of colorectal polyps](https://arxiv.org/abs/2608.07543)

**<font color=#1a73e8>作者：</font>** Joshua C. Vences, William T. Tran, Nikko Gimpaya 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background and Study Aims: Accurate optical diagnosis of colorectal polyps guides resection strategy and surveillance, with multimodal large language models (MLLMs) showing potential for image-based diagnosis. We aimed to evaluate the diagnostic accuracy of MLLMs in classifying colorectal polyps and predicting histology. Methods: We conducted a retrospective diagnostic performance study using the PRIME dataset, a curated set of white light and narrow-band imaging (NBI) images. We evaluated Claude Opus 4, Google Gemini 2.5 Pro, GPT-o3, GPT-4o, and GPT-5. For Paris, Narrow-band Imaging Colorectal Endoscopic (NICE), and predicted histology, we calculated F1 scores, percent correct scores, and accuracy of each MLLM compared to expert responses for 132 cases. Cochran's Q and McNemar's Test were used to determine differences between predicted values of each MLLM. Results: The F1 scores among MLLMs were >0.9 for all models for neoplastic vs. non-neoplastic polyps. Gemini 2.5 Pro demonstrated the highest F1 scores for invasive vs. non-invasive polyps and low- vs. high-grade adenoma, at 0.560 and 0.492 respectively. Claude Opus 4 and GPT-5 had statistically significantly higher percent correct scores than other MLLMs at 41.7%, using Paris classification. Conclusions: Claude Opus 4 and Gemini 2.5 Pro showed the highest accuracy in differentiating polyp subtypes, performing closest to expert consensus. Sensitivity and specificity, however, did not meet ESGE standards, highlighting the need for prospective multicenter trials and the design of human-in-the-loop workflows before clinical deployment.

---


### 38. [Learning an Interior Layout Policy in a Domain Specific Language Action Space](https://arxiv.org/abs/2608.07547)

**<font color=#1a73e8>作者：</font>** Yuhao Lu, Weichen Zhang, Wenyi Xiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Indoor scene layout generation is a challenging task in interior design. Existing methods often oversimplify the task by reducing room conditions to coarse 3D bounding boxes and neglecting structural elements such as doors and windows. More fundamentally, many prior approaches formulate spatial reasoning as direct coordinate prediction, thereby casting interior layout design as continuous regression over raw geometric parameters, which hinders the model from learning the underlying reasoning logic of intelligent layout design. We propose \textbf{LayoutDSL}, a novel LLM-based framework for learning an interior layout policy in a domain-specific language (DSL) action space. The DSL provides an explicit symbolic representation of layout information and serves as a structured action space for layout reasoning, where each action corresponds to an interpretable design decision. Under this DSL-based policy learning paradigm, we construct 3D-FrontDSL, a dataset of room-structure annotations paired with synthetic DSL action sequences for supervised fine-tuning. To promote a more generalizable and scalable policy with verifiable feedback, we design rewards grounded in interior design principles and physical plausibility, and optimize the policy via reinforcement learning. Extensive experiments demonstrate that LayoutDSL substantially improves spatial plausibility and design logicality over strong baselines and existing methods.

---


### 39. [Auditing Medical Vision-Language Models on Chest Radiographs: Estimating Reference Agreement Across Institutions](https://arxiv.org/abs/2608.07550)

**<font color=#1a73e8>作者：</font>** Pengyang Yu, Yiou Wang, Zhongping Dong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models return structured chest-radiograph findings through interfaces exposing no confidence score, so a receiving institution cannot read off how far to trust an individual judgment. Whether agreement with an institution's reference standard transfers across sites, findings, prediction directions and question formats is largely unmeasured. We evaluated three generative vision-language models on three institutional chest-radiograph corpora and six findings under two elicitation protocols, comprising more than 345,000 finding-level predictions, and estimated finding-by-direction reference agreement at a receiving institution from a small budget of local labels. Estimation strategies were then stress-tested under repeated strict institution-held-out evaluation. Under evaluation excluding the receiving institution from development entirely, adaptive selection among the seven estimators that design admits did not improve on simple fixed alternatives: it achieved a mean Brier score of 0.1083, against 0.0853 for always using a Beta-Binomial empirical-Bayes estimator and 0.0855 for a target-only logistic model. Those two differ by 0.0003, less than this family's own sensitivity to a change of solver version, and each leads in about half the settings, so no default can be recommended. Their advantage over estimators pooling across institutions was concentrated at one site and not confirmatory once clustered by institution, and a plug-in empirical-Bayes posterior-predictive count interval at a nominal 95% level covered 87.0%, less at the hardest institution. Reference agreement therefore has to be re-evaluated per site and per interface; these results concern agreement with institutional labels, not clinical correctness.

---


### 40. [Mechanistic Interpretability-Guided Selective Fine-Tuning of Vision-Language Models for Centimeter-Level Flood Depth Estimation](https://arxiv.org/abs/2608.07562)

**<font color=#1a73e8>作者：</font>** Nafis Fuad, Xiaodong Qian, Dongxiao Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Urban flooding poses an escalating threat to transportation infrastructure, yet no operational system provides real-time, street-level flood-depth estimates at centimeter resolution. This paper presents three vision-language models fine-tuned for continuous flood-depth estimation from street-level imagery: FloodLlama-Dense, a fully fine-tuned QLoRA baseline, and FloodLlama-MI5 and FloodLlama-MI6, interpretability-guided sparse variants that fine-tune only the top five and six causally relevant cross-attention layers identified through mechanistic interpretability analysis, respectively. Training uses an approximately 610,000-image subset of a 2.81-million-image synthetic corpus generated in Unreal Engine 5. The dataset combines single-vehicle subsets with 5 cm depth increments and mixed-vehicle subsets with 1 cm depth increments, spanning seven vehicle types, four weather conditions, and flood depths from 0 to 40 cm. FloodLlama-Dense achieves an MAE of 0.40 cm, an RMSE of 1.97 cm, and an Acc@5cm of 97.59%. Mechanistic interpretability analysis combining linear probing, logit lens, centered kernel alignment (CKA), and cross-attention entropy reveals a two-stage adaptation pattern: layers L13-L22 restructure visual representations, while depth first becomes linearly decodable at layer L23. FloodLlama-MI5 and FloodLlama-MI6 leverage this insight by fine-tuning only five or six of the eight cross-attention layers, achieving an 86-88% reduction in trainable parameters (6.55-7.86 million versus 54.4 million) with minimal accuracy loss. On a real-world benchmark, FloodLlama-MI6 achieves 98.62% accuracy, compared with 86.61% for the published STURM-FloodDepth baseline.

---


### 41. [What to Edit Next: Visually Aligned Image-Editing Follow-Up Suggestions in Conversational Systems](https://arxiv.org/abs/2608.07565)

**<font color=#1a73e8>作者：</font>** Zhijing Zhang, Jinpeng Yu, Xin Song 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conversational assistants increasingly recommend follow-up edits to help users continue a task. Existing systems primarily target text-only interactions, leaving image-creation conversations underexplored. In image-creation tasks, useful follow-up edit suggestions must reflect user preferences, offer diverse directions, and remain executable on the current image. We collected 100,000 real multi-turn image-creation conversation samples from Qwen App and found that 80.1% are image-dependent, underscoring the need for multimodal recommendation. We address this setting with a three-stage framework. In Stage 1, we use real online data to build a human-reviewed table of appropriate follow-up editing intents, then create SFT targets and fine-tune a multimodal policy. In Stage 2, to align rule-guided SFT suggestions with actual user choices, we use user click feedback to optimize the policy through multi-objective reinforcement learning. In Stage 3, to reduce visual inconsistencies between suggested edits and the current image, we introduce a visual verifier as additional training supervision. Extensive experiments demonstrate that our framework significantly outperforms baselines on both automatic and human evaluations. In a live user-randomized A/B test with millions of users, our final framework reduces visual inconsistency from 3.7% to 0.9%. Furthermore, it significantly improves recommendation CTR by 32.70%, image take-away rate by 16.32%, and average conversation turns per user by 39.90% (all p<0.05).

---


### 42. [COMEX: A Composition-Grounded Benchmark and Learning Framework for Explainable Aesthetic Image Cropping](https://arxiv.org/abs/2608.07570)

**<font color=#1a73e8>作者：</font>** Rui Yang, Wei Zhou, Dingyong Gou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Explainable aesthetic image cropping requires not only localizing a visually pleasing crop but also explaining why it is preferred. Existing crop-and-explain methods largely treat explanation as post-hoc text generation and overlook composition, a key aesthetic factor that links crop decisions with interpretable reasoning. In this paper, we reformulate explainable aesthetic image cropping as a structured crop-composition-explanation problem. To support this setting, we introduce COMEX, a new benchmark built through image expansion and an IO-reversal pipeline. COMEX contains 33,161 quadruples, each consisting of an expanded image, a crop box, a composition category, and a composition-grounded explanation, enabling joint learning of crop localization, composition understanding, and explanation generation. We further propose a two-stage SFT+GRPO framework, where supervised fine-tuning establishes the structured output protocol and basic cropping ability, and GRPO further improves crop quality, composition prediction, and explanation faithfulness. We benchmark 15 large vision-language models and existing cropping methods on COMEX, establishing a comprehensive testbed for composition-grounded explainable aesthetic cropping. Experiments on both COMEX and prior benchmarks demonstrate the effectiveness and transferability of our framework, with strong performance across evaluation metrics.

---


### 43. [Multi-Branch Policy Optimization for Multimodal Large Language Models](https://arxiv.org/abs/2608.07581)

**<font color=#1a73e8>作者：</font>** Shuai Lyu, Yuning Gong, Ruiling Gao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Group-based reinforcement learning methods for multimodal large language models typically rely on trajectory-level credit assignment that applies a single advantage to all tokens in a response. However, multimodal reasoning involves substantially higher perceptual uncertainty than text-only settings, where the model must repeatedly re-examine visual information to verify intermediate interpretations, and different visual groundings can lead to divergent reasoning paths, making such uniform credit assignment particularly inadequate and causing relative advantages to progressively degenerate toward zero. To address these challenges, we propose Multi-Branch Policy Optimization (MBPO), a tree-based framework that constructs reasoning trees at vision-language decision boundaries, enabling sibling branches to explore diverse visual hypotheses and assigning segment-level credit through branch-relative advantages. We further introduce a temporal replay buffer to reuse informative segments while controlling policy staleness. Experiments on several multimodal reasoning benchmarks show that MBPO outperforms representative baselines, improving both learning signal quality and optimization efficiency. The code is publicly available at this https URL.

---


### 44. [ComplexityWorld: Benchmarking Vision-Language Models on Verifiable Visual Decision Making](https://arxiv.org/abs/2608.07584)

**<font color=#1a73e8>作者：</font>** Ningxin Pan, Hanyu Li, Yehui Tang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have made rapid progress in visual perception and increasingly support real-world tasks that depend on images. Many such tasks, however, require more than rec- ognizing what an image contains: a model must use visual evidence to make a complete decision whose parts jointly satisfy global constraints. We introduce COMPLEXITYWORLD, a benchmark of 390 tasks across 39 domain-inspired visual worlds and 29 decision categories. Each task is generated from a hidden structured specification, rendered as a visual scene, and scored by an exe- cutable verifier that accepts any feasible solution. Under direct inference, all evaluated models ex- cept GPT-5.6-Sol remain below 40% verifier ac- ceptance rate (VAR), while GPT-5.6-Sol reaches 75.6%. Performance improves substantially when the same decision information is made explicit in structured form, yet varies sharply across equiva- lent visual presentations. Agent scaffolds provide smaller, model-dependent gains. Together, these results reveal a persistent visual-to-decision bot- tleneck that additional inference alone does not remove.

---


### 45. [Weather- and Location-Aware Agentic Dining Recommendation: Leveraging LLM World Knowledge for Region-Sensitive Contextual Reasoning](https://arxiv.org/abs/2608.07593)

**<font color=#1a73e8>作者：</font>** Kadharmoideen Fadurudeen  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Context-aware recommender systems have long recognized that factors such as location, time, and weather shape where and what people choose to eat. Existing weather-aware food and point-of-interest recommenders, however, typically treat weather generically -- mapping conditions to preferences through hand-crafted rules or specially trained context models -- and do not capture that the culturally appropriate response to weather is itself region-specific: a rainy evening calls for hot tea and fried snacks in one culinary culture and for very different comfort food in another. Encoding such weather-by-region-by-cuisine interactions as explicit rules or training data is brittle and does not scale. We present a weather- and location-aware agentic dining-recommendation system that takes a different approach: a large language model (LLM) orchestrates tools for location and weather retrieval and then reasons in natural language over the combined context, drawing on the cultural and culinary world knowledge already latent in the model to produce region-sensitive, weather-appropriate recommendations without per-region rule tables or specialized training. We describe the agent architecture, the tool-orchestration flow (Google location services and a weather service feeding an OpenAI LLM), and the reasoning mechanism, and we report on a working prototype that was implemented and briefly deployed end-to-end. We discuss design trade-offs -- cost, latency, ambiguity handling, and fallbacks -- and we are explicit about limitations, including the absence of a formal user study and the risk of cultural stereotyping in locality-based inference. The contribution is architectural: a simple, extensible pattern for incorporating environmental and cultural context into agentic recommendation through LLM reasoning rather than engineered rules.

---


### 46. [Scaling Inherently Interpretable Language Models](https://arxiv.org/abs/2608.07594)

**<font color=#1a73e8>作者：</font>** Guide Labs Team, Andreas Madsen, Aya Abdelsalam Ismail 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Interpretability is often treated as a tax on capability: language models are trained as opaque systems, then explained after the fact, with methods whose reliability is difficult to establish. In this work, we challenge this premise. Rather than reverse-engineering a model, we make interpretability a constraint of the training pipeline, optimized alongside the language modeling objective. Across three orders of magnitude of compute, on both autoregressive and diffusion language models, interpretability scales with capability rather than against it. Surprisingly, model representations become more disentangled and aligned with human-understandable concepts with scale.
We instantiate the training-time recipe with Steerling-8B, a diffusion language model with a causal attention mask. For any group of generated tokens, Steerling-8B attributes the output to relevant input tokens, human-understandable concepts, and training data. This enables closed-loop intervention: diagnose an output through its concept or feature attribution, retrieve similar training data, and correct the behavior through concept steering without retraining. Steerling-8B remains competitive with open peer models trained on substantially 2-16x more compute, suggesting a different scaling paradigm: interpretability can be designed into training, and it improves with scale.

---


### 47. [TeXFix-Bench: An Empirically Grounded Multi-Format Benchmark for LLM-Based Document Source Repair](https://arxiv.org/abs/2608.07617)

**<font color=#1a73e8>作者：</font>** Prajwal S. Venkateshmurthy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific and technical writing depends on markup sources that must compile: LaTeX, Typst, and Markdown pipelines fail on missing delimiters, mismatched environments, broken imports, or package conflicts. Existing document-repair evaluations inject faults with ad-hoc edits that lack an empirical fault model. We present TeXFix-Bench, a multi-format benchmark for LLM-based full-source document repair grounded in a mined fault taxonomy. A Grounded-Theory study of localized hard-crash LaTeX faults from TeX Stack Exchange, GitHub commits, and package documentation (168 verified faults, dual open coding at $\kappa$=0.34) yields an 18-category taxonomy instantiated as DocMut: 48 AST-aware operators across three formats. A three-model cross-benchmark shows DocMut faults are 5.6-9.2 pp harder to repair than pattern-based mutations on the same seeds, and a real-error case study (88 mined human crashes, 67.0% repair success) brackets both synthetic sets from below. We construct 10,437 instances from 743 openly licensed seeds and evaluate seven LLMs under a fixed zero-shot protocol with provider-pinned routing, collecting 48,651 attempts at about USD 200 total inference cost. A complete 6,613-instance x 7-model balanced matrix confirms all rankings. A pinned engine gate yields a 27.5-point intention-to-treat compile spread (56.7-84.2%). Typst is markedly harder than LaTeX and Markdown. A restoration oracle over 28,129 compiling repairs shows that 13.6-18.5% of compiling repairs materially alter document text, and restoration rank diverges from compile rank: the model with the lowest compile rate restores content best among its successes. Compile success alone overstates repair quality. We release the taxonomy, DocMut, and all campaign artifacts.

---


### 48. [FlowErase-OPD: Multi-Concept Erasure via Anchored On-Policy Distillation in Flow Matching Models](https://arxiv.org/abs/2608.07620)

**<font color=#1a73e8>作者：</font>** Yi Sun, Yimin Zhou, Xinhao Zhong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in flow matching models have substantially improved the quality of text-to-image generation, but have also raised increasing safety concerns due to their potential to generate harmful or undesirable content. Existing concept erasure methods for flow matching models predominantly focus on removing individual concepts, while effectively erasing multiple concepts simultaneously remains challenging. We propose FlowErase-OPD, a framework for multi-concept erasure based on on-policy distillation (OPD). Our approach first distills multiple single-concept erased models into a unified LoRA module and introduces Anchored Multi-Teacher Distillation (AMTD), which incorporates a retention teacher to mitigate the trade-off between concept erasure and preservation of generative capabilities. To further improve the coordination of multiple erasure objectives, we develop Adaptive Retention Control (ARC), which dynamically adjusts the sampling frequency and loss weight of each erasure teacher, together with the relative contribution of erasure and retention teachers throughout training. Extensive experiments on nudity, object, and artistic-style erasure demonstrate that FlowErase-OPD consistently improves the trade-off between erasure effectiveness, image quality, and semantic alignment, achieving state-of-the-art performance across diverse multi-concept erasure settings. Furthermore, the resulting models exhibit strong robustness against adversarial attacks. These results highlight the potential of on-policy distillation as a principled framework for safe and controllable generation in flow matching models.

---


### 49. [CMU-Drive and V2V-VLA: Cooperative Multi-agent Unified Driving with Reasoning Benchmark and Vehicle-to-Vehicle Vision-Language-Action Models](https://arxiv.org/abs/2608.07621)

**<font color=#1a73e8>作者：</font>** Hsu-kuang Chiu, Stephen F. Smith  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models have recently achieved impressive performance for end-to-end autonomous driving, yet existing approaches are primarily designed for an individual single autonomous driving agent with limited support for cooperative perception, reasoning, and planning. We present Cooperative Multi-agent Unified Driving with Reasoning (CMU-Drive), a closed-loop end-to-end benchmark for evaluating cooperative autonomous driving with multiple connected autonomous vehicles (CAVs) operating in safety-critical driving scenarios with background traffic participants. We further propose Vehicle-to-Vehicle Vision-Language-Action (V2V-VLA), a cooperative VLA model that integrates cooperative driving into a single forward pass by jointly generating driving actions, future waypoints, language reasoning, and communication policies. Experiments on CMU-Drive establish the first benchmark and baseline for cooperative VLA driving and provide a foundation for future research on multi-agent, closed-loop, end-to-end cooperative autonomous driving. Our code, benchmark, and model checkpoint will be publicly released to facilitate open-source research.

---


### 50. [Controlled Memory Interference in Continual LLM Agents](https://arxiv.org/abs/2608.07622)

**<font color=#1a73e8>作者：</font>** Ao Ding, Hongzong LI, Shiqin Tang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term memory enables AI agents to maintain continuity across sessions, personalize behavior, and evolve through accumulated experience. Yet memory evolution is not simply a process of storing more information: new experiences may reinforce, revise, or interfere with existing memory states. Existing systems mainly emphasize memory construction and relevance-based retrieval, but several memories may remain simultaneously relevant while differing in state, temporal validity, or authority. We introduce Controlled Memory Interference (CMI), a controlled diagnostic and data-generation framework for studying how agent memory evolves under different memory relationships. Across controlled memory evolution, benign accumulation has limited effects, whereas relationship-specific interference sharply suppresses update plasticity with little stability gain, either by blocking target-memory exposure or by disrupting its downstream use. Lexical and Dense retrieval exhibit distinct interference pathways, while poisoning is more sensitive to update-authority cues than to recency alone. Beyond diagnosis, CMI provides targeted examples for interference-aware memory learning, improving the distinction between valid updates and interference-inducing memories while preserving performance on original memory tasks. These findings show that memory evolution is shaped not only by memory scale, but also by interactions among accumulated experiences. More broadly, memory interference emerges as an important factor for reliable continual agent memory systems.

---


> [!TIP]
> 当前位于：**1-50**（第 1/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-438](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
