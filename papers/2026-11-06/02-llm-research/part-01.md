# 🧠 大模型相关研究 | 2026年11月06日

> 本类共 **207** 篇论文：已确认 **189** 篇，待复核 **18** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-207](./part-05.md)

---

### 1. [VAR-Q: Tuning-free KV Cache Quantization for Visual Autoregressive Image and Video Generation](https://arxiv.org/abs/2611.05380)

**<font color=#1a73e8>作者：</font>** Boxun Xu, Jiaji Lu, Yuxuan Yin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual autoregressive generation spans two dominant paradigms: next-scale prediction for images and video, and next-frame prediction for video. Both decode block-by-block rather than token-by-token, yielding KV caches whose statistics diverge from those of language models. At scale, KV memory exceeds the weights and limits large-scale deployment caused by a large amount of visual tokens. Our analysis of these caches reveals three findings. First, a small set of massive-value channels carries the functional load: ablating these outlier channels collapses generation, whereas ablating a matched set of inlier channels leaves quality intact. Second, the outliers organize along two axes, feature and block, with magnitudes persistent within each cell and shifting across cells. Third, this structure arises from two independent mechanisms: projection bias and RoPE-induced scattering. Guided by these findings, we propose VAR-Q, a tuning-free KV-cache quantization framework that groups along the same two axes. The generation loop provides block boundaries for free, removing the need for outlier detection or calibration. Paired with bit-packing kernels for runtime memory reduction, VAR-Q delivers low-bit quantization across nine models spanning both paradigms, cutting KV memory by up to 78.5% with negligible quality degradation and enabling 6x larger inference batches.

---


### 2. [DS@GT ARC at CheckThat! 2026: A Verdict-Anchored Pipeline for Generating Fact-Checking Articles](https://arxiv.org/abs/2611.05382)

**<font color=#1a73e8>作者：</font>** Hoang Thanh Thanh Truong, Shuyu Tian  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Misinformation spreads faster than professional fact-checkers can manually verify it and write articles explaining their verdicts. This creates a need to automate the production of fact-checking articles. This paper details work done by the DS@GT ARC team for CLEF 2026 CheckThat! Lab Task 3 Fact-Checking Article Generation. We seek to generate a full fact-checking article from a claim, its original verdict, and a set of scraped source documents. Our team built a four-stage pipeline that cleans noisy evidence, retrieves and clusters relevant sources, generates the article by conditioning \texttt{Llama-3.1-8B-Instruct} on the original fact-checker verdict, and recovers inline citations through deterministic post-processing. We achieved a mean score of 0.428 and ranked 3rd out of 9 teams for the CLEF 2026 CheckThat! Lab Task 3, compared to a baseline mean score of 0.272. Our code is available on GitHub at this https URL.

---


### 3. [CCDWIKI: Decoupling Case Formulation from Response Generation in Longitudinal CBT Dialogue](https://arxiv.org/abs/2611.05383)

**<font color=#1a73e8>作者：</font>** Mingwen Zhang, Ruiyang Song, Qinying Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cognitive Behavioral Therapy (CBT) demands more than empathic validation, requiring instead a structured formulation of the interplay among situations, automatic thoughts, emotions, and behaviors. Therapists formalize this interplay through a Cognitive Conceptualization Diagram, where maintaining longitudinal coherence necessitates continuous evidential adjudication to separate tentative hypotheses from established findings. Current dialogue systems track conversational history via retrieval or static profiles but lack the representational capacity to encode epistemic status. Consequently, provisional interpretations are often prematurely reified as established facts, inadvertently biasing downstream interventions. Addressing this limitation, CCDWiki is introduced as a plug-and-play advisor conceptualizing longitudinal therapy as evidence-grounded hypothesis adjudication. The approach encodes each clinical hypothesis as a mutable entry bound to corroborating and contradicting evidence. Across sessions, accumulating data strengthens supported entries, preserves provisional ones, and retracts contradicted assumptions. The resulting formulation distills into concise guidance for unmodified therapeutic language models. Experiments demonstrate substantial improvements in both conceptualization and intervention quality without requiring backbone retraining.

---


### 4. [SRRM: A Retrieval-Reconstruction Benchmark for Evaluating Long-Context Memory in Small Language Models](https://arxiv.org/abs/2611.05386)

**<font color=#1a73e8>作者：</font>** Christopher Alberto Hamonangan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Small Language Models (SLMs) are increasingly deployed on consumer-grade hardware, yet their ability to preserve information across progressively longer contexts remains insufficiently understood. Existing benchmarks primarily evaluate retrieval-oriented tasks, providing limited insight into whether successful retrieval reflects comprehensive long-context memory preservation. To address this limitation, this paper introduces Simple Retrieval-Reconstruction Memory (SRRM), a lightweight and fully reproducible benchmark that jointly evaluates Targeted Retrieval and Global Information Reconstruction. This study also proposes the Memory Preservation Ratio (MPR), a benchmark-level metric that quantifies the relationship between retrieval and reconstruction performance. SRRM was evaluated using a synthetic dataset on three Qwen2.5 models (0.5B, 1.5B, and 3B parameters) across context loads ranging from 10 to 100 factual statements. Experimental results show that reconstruction performance deteriorated substantially faster than retrieval accuracy as contextual information increased, indicating that retrieval alone is insufficient to characterize long-context memory preservation. Among the evaluated models, Qwen2.5-1.5B achieved the highest retrieval accuracy (86.7%), reconstruction performance (45.7%), and MPR (0.53), outperforming the larger Qwen2.5-3B model (72.2%, 18.5%, and 0.26, respectively). These findings demonstrate that increasing parameter count does not necessarily improve long-context memory preservation. Overall, SRRM provides a reproducible and extensible benchmark for systematically evaluating long-context memory while revealing complementary memory behaviors that remain hidden under retrieval-only evaluation frameworks.

---


### 5. [AI-Driven SaaS Platform Integration: AI Express for Unified Generative AI Services with Pay-As-You-Go Credit Systems and Scalable Microservice Architecture](https://arxiv.org/abs/2611.05389)

**<font color=#1a73e8>作者：</font>** Deepit Sapru  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generative AI is currently fragmented, with separate subscriptions required for text generation, image synthesis, and code assistance, leading to high costs and workflow disruptions. AI Express is a SaaS platform that consolidates these capabilities into a unified pay-as-you-go service. The platform provides a range of AI tools, including a Core Code Reviewer that evaluates GitHub repositories, a Text-to-Website generator that converts text into fully functional websites, script generation, grammar checking, data analysis, and watermark removal, all accessible through a single interface without requiring technical expertise.

---


### 6. [Who May Overrule the Agent? Evidence-Gated Authority in LLM Review Institutions](https://arxiv.org/abs/2611.05390)

**<font color=#1a73e8>作者：</font>** Fuad Ali  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent language-model systems often add a reviewer to improve an upstream agent's decision. Yet a reviewer can both repair errors and replace decisions that were already correct. We study this as a problem of institutional jurisdiction: conditional on the same proposal, task information, model, and review output, when is the reviewer authorized to make its recommendation binding? We compare broad override authority with an evidence gate that permits replacement only after the reviewer produces a mechanically valid record of a binding-constraint violation and a compliant repair. Across two locally run open-weight models, 96 spatial-policy tasks, and a 96-task portfolio-transfer benchmark, the gate sharply reduces corruption of correct proposals while retaining most repairs of violations. The directions of this tradeoff are partly implied by the rule; its magnitude depends on reviewer transitions and upstream proposal states. A prospective validation then gives the reviewer an explicit choice to retain, replace, or escalate. This eliminates correct-proposal corruption for Qwen, but Mistral still replaces all 48 correct proposals; Qwen also declines every welfare-only repair that Mistral frequently attempts. Thus interface design changes reviewer behavior but is not a model-independent safeguard. The result is not that restricted review is universally better. It is that reviewer competence, action interface, and binding jurisdiction jointly determine both the correction domain and the corruption surface.

---


### 7. [Uncertainty-Aware Resource Orchestration for Agentic AI Systems](https://arxiv.org/abs/2611.05392)

**<font color=#1a73e8>作者：</font>** Masoud Shokrnezhad, Tarik Taleb  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic artificial intelligence (AI) systems powered by large language models (LLMs) execute as autonomous multi-step pipelines that dynamically invoke tools, integrate observations into memory, and iterate until a task is resolved or a resource budget is exhausted. Unlike classical workflows with fixed graphs, the aggregate compute, bandwidth, and end-to-end latency demands of such pipelines are unknown at dispatch time: they emerge at runtime from intermediate observations and stochastic token sampling, yielding heavy-tailed, multi-modal random variables. This unpredictability forces infrastructure orchestrators into a dilemma: under-provisioning risks mid-execution throttling and deadline violations, while over-provisioning wastes scarce edge or cloud capacity. Existing schedulers require a fully known pipeline graph, while edge resource-management methods rely on parametric or stationary demand models, and neither fits the unknown, non-stationary profiles of agentic pipelines. We formalize this setting as the uncertainty-aware agentic orchestration problem, where the goal is to reserve, at dispatch time, compute and bandwidth allocations that cover actual pipeline demands, and to verify that the pipeline can meet its deadline, each with a prescribed probability. We then propose Conformal Reservation for Orchestration (CRO), an online algorithm that translates a sliding window of past execution traces into dispatch-time resource allocations with finite-sample, distribution-free coverage guarantees via conformal prediction. Simulations over heterogeneous task mixes with multi-modal and heavy-tailed profiles show that CRO is the only evaluated method that simultaneously satisfies target probabilistic coverage across all risk levels while, among coverage-feasible methods, attaining the lowest over-reservation, roughly halving the resource waste of the Chebyshev-bound baseline.

---


### 8. [Challenge-Aware Knowledge Recruitment with Meta-Agent Supervision for Medical Multi-Agent Reasoning](https://arxiv.org/abs/2611.05393)

**<font color=#1a73e8>作者：</font>** Riccardo Riccio, Haitz Sáez de Ocáriz Borde, Pietro Liò  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models perform strongly on standard medical QA but degrade on harder reasoning tasks, where multi-agent debate often fails to beat strong single-model prompting. We argue that a key limitation is that existing systems select experts and retrieve knowledge from the question alone, rather than from gaps that emerge during reasoning. We propose challenge-aware adaptive recruitment: an external CHALLENGER inspects the evolving reasoning trace and identifies specific factual or expertise gaps. These signals trigger targeted knowledge retrieval or mid-discussion specialist recruitment. On the MEDAGENTSBENCH hard subset (862 questions across nine biomedical datasets), upfront retrieval provides little benefit, while challenge-aware in-between retrieval performs better; on a multi-specialist backbone it improves accuracy on 8 of 9 datasets and adds 6 percentage points over Challenger Only. Ablations indicate benefits from both retrieval timing and gap-specific query signals, and a live web-search experiment shows that the timing advantage persists across retrieval backends. For specialist recruitment, self-triggered adaptation is unreliable, whereas Challenger-triggered recruitment raises GPT-4.1-mini MedQA accuracy from 46% to 54%, with positive direction on all tested generalization datasets. Naively combining retrieval and specialist recruitment degrades performance, highlighting the need to coordinate adaptive intervention channels. These results show that when and why external resources are recruited is a key design choice in multi-agent medical reasoning.

---


### 9. [A Feasibility Condition for Confidence-Gated Tiered LLM Inference](https://arxiv.org/abs/2611.05394)

**<font color=#1a73e8>作者：</font>** Sumit P. Ahuja  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tiered inference distributes large language model computation across a hierarchy of devices, from on-device and edge hardware to the datacenter, and is increasingly offered as the route to cheaper, lower-latency, and more private serving. Most such systems orchestrate frozen model checkpoints, and most decide what to resolve locally and what to escalate using a confidence signal produced by a forward-deployed model. We give a closed-form condition for when no threshold on that signal makes a tiered cascade worthwhile relative to sending every query to the backstop. Modeling the routing decision as a binary test and separating local from escalation cost through an architecture cost ratio $\kappa$, we derive a feasibility condition bracketed by a signal-free floor, below which a cascade is feasible at any signal quality, and a perfect-signal ceiling, above which none is. Read along the $\kappa$ axis the condition inverts: where local compute is billed, cost binds, matching a recent empirical finding; where it is sunk, on decentralized hardware, feasibility becomes unconditional and signal quality instead sets what the cascade achieves. We turn the condition into three design requirements that existing trained-in primitives satisfy only in isolation, and we propose, as future work, a co-designed architecture and a protocol to test it. The condition and the inversion hold independently of that architecture; they are the paper's contribution.

---


### 10. [Can Large Language Models Review the Scientific Literature? A Test Against a 102-Article Benchmark](https://arxiv.org/abs/2611.05459)

**<font color=#1a73e8>作者：</font>** Abdullah Al Kalbani, David M. Schultz, Alexandra K. Anderson-Frey 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to support scientific literature reviews, yet evaluations often examine individual tasks rather than the review process as a whole. We assess six AI tools across four stages: finding relevant articles, interpreting them, synthesizing across them, and proposing future research. The benchmark is a published review of the Spanish plume weather pattern and its 102-article corpus.
In the initial searches, five tools collectively identified 57 articles, with the best individual tool finding 42. Institutional library access increased discovery from 42 to 82 articles for Codex and from 15 to 79 for Claude Code. Given the complete corpus of 102 PDFs, three tools correctly identified all 18 articles discussing the Spanish plume substantially, but incorrectly classified 40% to 79% of the 84 passing mentions as substantial. The same three tools produced syntheses evaluated blindly by two domain experts. Although largely accurate, the syntheses provided limited insight and sometimes contained unsupported claims, quotation errors, and exaggerated statements of consensus. Finally, all three tools proposed research directions broader than the Spanish plume literature, although two approached questions identified in the benchmark review.
No single tool performed best across all tasks. We provide eight recommendations for researchers using AI tools in literature reviews. Our findings suggest that LLMs can assist with discovering and interpreting scientific literature, particularly when institutional access is available, but cannot replace expert judgment in evaluating evidence or synthesizing research.

---


### 11. [Objective-Conditioned Active Preference Learning for Multi-Objective Alignment](https://arxiv.org/abs/2611.05506)

**<font color=#1a73e8>作者：</font>** Duc Anh Vu, Thong Nguyen, Hoang Pham 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Aligning large language models (LLMs) with several objectives, such as helpfulness, harmlessness, and honesty, typically relies on preference judgment for each objective, growing the annotation cost linearly with the number of objectives. Active preference learning can reduce this cost by selecting the comparisons whose labels are expected to change the policy most. Existing remedies either lack an objective-aware query selection mechanism for the multi-objective setting or regard conflicting preferences as harmful, therefore excluding them from the training data. We introduce OGC-DPO (Objective-conditioned Gradient Coverage DPO), an active learning framework that treats each (response pair, objective) combination as a separate query and measures its informativeness through the policy's own implicit gradient, without relying on an external reward model. OGC-DPO then selects the queries that most expand each objective's gradient coverage. Empirical experiments across varying numbers of objectives demonstrate the effectiveness of OGC-DPO over existing active preference learning methods under the same annotation cost. Further analysis demonstrates that informative conflicts, rather than being uniformly harmful, provide a useful policy training signal.

---


### 12. [SlackBench: Benchmarking Agents on Collaborative Projects Grounded in Real Code Repositories](https://arxiv.org/abs/2611.05512)

**<font color=#1a73e8>作者：</font>** Mingxuan Li, Huanzhi Mao, Ruitao Zheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI Agents are becoming digital coworkers that can browse the web, write code, run experiments, and assist humans over extended horizons. Yet existing benchmarks fall short of real knowledge work: many rely on synthetic data or isolated tasks, missing the complex, multi-party dynamics of collaborative projects, where critical information is scattered across conversations, code, and evolving decisions. Even simple workplace questions may require locating relevant channels and direct messages, recovering context from long discussions, inspecting repository state, reconciling stale or conflicting evidence, and synthesizing across sources.
We introduce SlackBench, a benchmark for evaluating agents on realistic research and engineering workflows that require joint reasoning over workplace communication and evolving repository state. Grounded in privacy-preserving reenactments of real academic research projects, SlackBench provides reproducible environments with realistic multi-party dialogue, evolving decisions, and corresponding code changes grounded in GitHub repositories and Google Docs. It contains 140 queries spanning heterogeneous-source agentic search, abstention on unanswerable or false-premise questions, goal-directed summarization, and circumstance inference over long conversations. These tasks are not reducible to static corpus question answering: agents must determine which conversations matter, traverse threads, inspect repository state, and synthesize evidence across communication and code artifacts. Across 33 frontier models and agent harnesses, the best system scores around 80% and most agents score below 66%, highlighting substantial headroom for improvement. SlackBench thus provides an extensible framework for evaluating agents in collaborative work environments. The SlackBench dataset is available at this https URL .

---


### 13. [TSFM Meets LLM: Context as Covariates](https://arxiv.org/abs/2611.05515)

**<font color=#1a73e8>作者：</font>** Hemanth Ram, Sai Shankar Narasimhan, Shubhankar Agarwal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Textual information is ubiquitous in real-world time series datasets, appearing as news, reports, and annotations that hold key predictive signals not deducible from numerical history alone. Large Language Models (LLMs) interpret text but lack numerical precision, while Time Series Foundation Models (TSFMs) are quantitatively accurate but cannot reason about the effects of text. Moreover, the lack of large-scale paired multimodal datasets limits progress in bridging this gap. In this work, we address this challenge by providing a scalable approach for generating realistic multimodal datasets by annotating real-world time series with LLMs. Building on this, we propose Context as Covariates (CoCo), a forecasting framework in which an LLM distills its textual reasoning into numerically grounded forecast and confidence covariates that guide a TSFM backbone, thereby exploiting the strengths of both LLMs and TSFMs. We align the two models in stages, first fine-tuning the LLM via Group Relative Policy Optimization (GRPO) with a reward tied to covariate-induced improvement in forecasting performance, and then fine-tuning the TSFM on covariates generated by the aligned LLM. Our experiments show that models trained on our synthetic multimodal corpus generalize to real benchmarks spanning finance, economics, weather, traffic, and security. Notably, CoCo with Qwen3-4B-Instruct-2507 as the LLM and Chronos2 as the TSFM achieves up to 12% MAE improvement over state-of-the-art TSFMs and LLM forecasters, such as GPT-4o. Code, checkpoints, and the evaluation datasets are publicly available.

---


### 14. [When to Ask, When to Answer: Strategic Clarification for Ambiguous Reference Resolution in Dialogue](https://arxiv.org/abs/2611.05517)

**<font color=#1a73e8>作者：</font>** Ibrahim Khebour, Nikhil Krishnaswamy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> For humans, referential disambiguation is a collaborative process involving clarification questions asked when they will meaningfully change the outcome. However, large language models (LLMs) have been shown to be biased toward premature answering, preferring definite single-turn responses over more clarification exchanges. In this paper, we study the problem of "strategic clarification" -- asking clarification questions in a reference game when their answers will narrow the set of candidate referents. We construct a controlled test environment from the SIMMC 2.1 dataset that records how many questions each ambiguous reference needs to be successfully resolved, and examine how baseline LLM behavior and common post-training methods ask clarifying questions vs. attempt to answer the referent. We also propose BACE (Belief-Aware Critic with Epistemic tracking), a lightweight action chooser method on top of a frozen LM backbone, and show that BACE more consistently chooses the optimal number of clarifying questions than methods such as GRPO and ArCHer.

---


### 15. [Recasting Visual Language Models as EEG Foundation Models for Clinical Neurodiagnostics](https://arxiv.org/abs/2611.05538)

**<font color=#1a73e8>作者：</font>** Xin Zhou, Elena Sergeeva, Nan Bi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Historically automated electroencephalography (EEG) systems was done using task-specific supervised models trained on purposely annotated data. A more recent modeling paradigm relies on creating a unified representation, or a 'foundation model', for multiple modality-specific tasks through large-scale domain-specific pretraining on the unannotated EEG signal. The quality of this unified representation directly depends on the availability of the modality-specific datasets. At the same time, generalist Vision Language Models (VLMs) exhibit broad few-shot learning capacities as well as good fine-tuning adaptability to different visual and language tasks. Can VLMs learn how to read and interpret EEG visually, emulating to a degree the way human clinicians inspect the EEG patterns? In this work we make a case that they can: we show that generalist VLMs without large-scale EEG pretraining perform competitively across a collection of clinical neuro-diagnostic tasks, can adapt to different tasks in a few-shot learning setting better than specialist foundation models, and exhibit better performance with model scaling when modality-specific models fail to exhibit.

---


### 16. [Rewrite, Then Veto: Rewriter-Agnostic Edit Gating for LLM-Based Post-OCR Correction](https://arxiv.org/abs/2611.05539)

**<font color=#1a73e8>作者：</font>** Jorge Ramón Fonseca Cacho  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs can repair noisy OCR transcripts of historical documents, but they also change text that was already correct. We propose EditVeto, a veto gate placed after a full-context LLM rewrite. The rewrite is character-aligned to the OCR input, its differences are split into blocks, and a 0.6B-parameter gate keeps or reverts each block. An oracle analysis motivates the design: given the true error locations, per-span generation is worse than no correction, whereas vetoing a full rewrite's edits helps. Trained on rewrites by two Qwen3 models and evaluated, frozen, on the eight HIPE-OCRepair-2026 test sets, the gate improves all five rewriters tested, two of them unseen in training: weighted cMER falls by 0.0026-0.0044 and the preference score rises by 0.15-0.25 (paired bootstrap, p ~ 0.0002 each). On published competition outputs it lowers cMER for three of four teams but raises it for the winning run (0.0050 to 0.0065). In a second, disclosed test look, a retrained gate still improves LoRA-tuned rewriters (cMER -0.0011 to -0.0021), and an ensemble of their gated edits reaches a cMER of 0.0069 and a preference score of 0.928, mostly through fine-tuning and pooling rather than gating. Built only on public models and data, it is behind the winner (0.0050) and tied with the second-ranked run (0.0071), both from the only team using domain pre-training, and ahead of all other published runs. A third, secondary look shows the unchanged gate improving zero-shot Qwen3.8-27B (cMER 0.0114 to 0.0108) but only the preference score of its LoRA-tuned version.

---


### 17. [Iterated creation, grading, and revision of data science projects by language models](https://arxiv.org/abs/2611.05548)

**<font color=#1a73e8>作者：</font>** Rohan Alexander  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We evaluate the extent to which agentic AI models can complete an end-to-end data science project, and how this improves with feedback. A 'writer' model with specific tools creates a complete data science project including downloading, cleaning, and analyzing a dataset, and writing a short paper about it. The project is executed and a 'grader' model evaluates it. The writer can then revise its submission, and this repeats for a total of three rounds. We consider seven models from five developers: Anthropic, OpenAI, Google, DeepSeek, and this http URL. Each model is both a writer and a grader, so there are 49 writer-grader pairs and we run each pair three times. Of the 147 initial submissions, 107 run and render, and the average score increases from 59 per cent to 76 per cent after the final round of feedback. By writer the extent of the increase ranges from 3 percentage points for Anthropic's Opus 5.5 to 46 percentage points for Anthropic's Haiku 4.5, and by grader it ranges from 13 percentage points for Google's Gemini 3.8 Flash to 32 percentage points for Anthropic's Haiku 4.5. When a model grades its own writing the score tends to be about 9 percentage points higher than the average of what the other models give it. About half of the difference that we see from round to round is within the grader's own noise. Feedback generally results in the highest marks, but even just having the chance to revise, or having the additional budget, in terms of time or tool calls, without any feedback, results in considerable increases for some of the models but not for others. We find that how much such a loop helps depends on which model plays which role, but weaker models generally do not improve stronger models.

---


### 18. [Whose Transparency is it Anyway? Understanding Generative AI Transparency Needs and Gaps Across Stakeholders](https://arxiv.org/abs/2611.05549)

**<font color=#1a73e8>作者：</font>** Genevieve Smith, Sahiba Chopra, Natalia Luka 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Transparency has become a central principle in AI governance, yet there is little agreement about what transparency means, for whom, and in what contexts. Drawing on interpretive flexibility within the Social Construction of Technology, this paper examines how different stakeholders understand and experience transparency in generative AI. This study draws from a global survey of 400 end-users, AI builders, and policymakers, complemented by a structured focus group with end-users, grounding the quantitative findings in qualitative insights from the group most underserved by current transparency practice. We present three key findings. First, all three groups share similar understandings of what transparency means and what it should afford, centered on ensuring accuracy and privacy. Second, gaps between the importance of transparency features and their perceived availability are substantially larger for end-users than builders, revealing how power shapes what gets built and who it serves. Only 28% of end-users report that current transparency practices reflect their needs very well, compared to 53% of builders and 49% of policymakers. Third, transparency is situationally constructed, priorities shift with context and task structure, with role-specific frames activating when context demands them and receding when it does not. We argue that meaningful AI transparency requires moving beyond a one-size-fits-all solution, including current emphases on AI disclosure and static documentation, toward pluralistic transparency infrastructures that reflect the needs of diverse users and stakeholders.

---


### 19. [VirtualTrialHarness: Coordinating Agentic Operationalization of Virtual Trial Protocols Across Complex Clinical Schemas](https://arxiv.org/abs/2611.05551)

**<font color=#1a73e8>作者：</font>** Pengze Li, Jingna Feng, Yue Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Virtual trials use routinely collected clinical data to evaluate treatment strategies, but translating a study protocol into an executable analysis requires determining how clinical concepts and study requirements should be represented in the available data and applied consistently across the workflow. These decisions depend on local data representations and operational conventions and can involve source selection, patient and encounter identity, linkage, and temporal interpretation. Here we introduce VirtualTrialHarness (VTHarness), an agent framework that coordinates virtual-trial operationalization by selecting reusable procedural skills for each workflow stage and uses explicit contracts to maintain consistent study decisions across stages. We also introduce VTBenchmark for evaluating source selection and cohort construction. Across three complex synthetic environments, VTHarness successfully produced all required cohort outputs matching the references in 95.1% of workflows after requirement clarification, compared with 60.4% using retrieval from the same procedural corpus. Procedural skills improved source recovery across three language models and increased source overlap with analyst code in 13 Mayo Clinic cases. Site-specific adaptation enabled reference-matched cohort execution across eight MIMIC-IV tasks. Within the Mayo Clinic Virtual Trials Program, the framework supported investigator review of cohort construction and endpoint analysis. These findings support coordinating procedural guidance with workflow decisions to improve virtual-trial implementation across complex clinical schemas.

---


### 20. [AGORA: Reliability-Aware Aggregation of LLM Judges via Item-Response Theory](https://arxiv.org/abs/2611.05556)

**<font color=#1a73e8>作者：</font>** Junhyung Ahn  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-judge is a common substitute for costly human evaluation, and aggregating several judges is the standard remedy for any single judge's bias. Judge pools mix judges of very different reliability, while the human-labeled sets that validate them hold a few hundred items or fewer. In this regime the per-item mean weights weak judges as heavily as strong ones, and confusion-table models such as Dawid-Skene must estimate a per-judge error table from too few items. We propose AGORA (Aggregation Of Reliability-weighted Assessments), an item-response-theory aggregator that places every item on one latent quality scale and describes each judge by a sensitivity parameter and ordered rating thresholds, so judge reliability is learned from all items jointly and without human labels. Across three benchmarks, AGORA matches or exceeds Dawid-Skene on large evaluation sets, and its advantage widens as the set shrinks toward a few hundred items. It remains accurate as pools grow more uneven, a label-free dispersion statistic indicates in advance when trust weighting helps, and its learned trust weights track per-judge human validity.

---


### 21. [How Finely Can Vision-Language Models See Biology? Bio-VQA: A Benchmark for Taxonomic, Morphological, Spatial and Individual Reasoning](https://arxiv.org/abs/2611.05559)

**<font color=#1a73e8>作者：</font>** S M Rayeed, Qian Ma, Charles V. Stewart 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In biodiversity monitoring, a single image raises several questions: which taxon, how many, which trait, and whether the individual has been seen before. Vision-language models (VLMs) could answer all of these from the image, but their ability is largely untested in biology, as existing benchmarks focus mostly on species identification within a few taxonomic groups. We present Bio-VQA, the largest biological visual question answering (VQA) benchmark and the only one to span four aspects of biological visual understanding: hierarchical taxonomic reasoning, fine-grained attribute grounding, quantitative spatial reasoning, and individual re-identification. Bio-VQA contains 1.86M questions over 217K images from 11 public datasets, and extends right-or-wrong scoring to graded scoring, so a near-miss counts for more than a distant one. Evaluating 18 open-weight models from 3.75B to 38.4B parameters, we find that general visual capabilities do not transfer to biological organisms: the best model counts animals exactly on 41.7% of images with 2 to 10 individuals, less than half its accuracy on everyday objects at the same counts. Taxonomic accuracy falls to one sixth, from 0.72 at phylum to 0.12 at scientific name, and scaling helps mostly at coarse ranks. The gap to a domain specialist widens accordingly, from 0.731 against BioCLIP-2's 0.874 at class (1.2x) to 0.269 against 0.544 at scientific name (2x). On trait size measurement, 15 of the 18 models do no better than an image-blind baseline that predicts one fixed number for every specimen, and on re-identification, 17 of the 18 models fall below chance under adversarial conditions. These failures persist across a tenfold range of model size. We hope Bio-VQA becomes a standard test of how well VLM capabilities transfer to the biological domain.

---


### 22. [Discarded or Unreachable? Diagnosing and Repairing Spatial Relation Failure in Vision--Language Similarity](https://arxiv.org/abs/2611.05565)

**<font color=#1a73e8>作者：</font>** Mahdi Mostajabdaveh, Zirui Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contrastive vision-language models score left/right relations near chance, but the symptom has two causes that call for opposite repairs: the relation may survive in the pooled embedding yet be unreachable by native image-text similarity, or pooling may discard it while the dense features retain it. On clean two object photographs, across ten encoders, the lateral polarity is linearly decodable from the flip odd component of the pooled vector at 0.77-0.99, yet a search over a million captions leaves nine of the ten at chance under native scoring: an access failure. On controlled C4 orbits, where the relation is the only thing that varies, pooling keeps the arrangement axis at 0.998-1.000 and loses its polarity, which the patch grid retains: a pooling failure. Both sit downstream of the dense features, so one readout covers both. Our zero parameter, query conditioned spatial moment recomputes the geometry from the patch grid and stores it as a vector beside the native embedding. On a 118,287 image index it raises left/right pairwise accuracy against reversed geometry negatives from 0.51-0.53 to 0.81-0.96 and conditional R@1 among 21 category matched candidates from 0.05 to 0.37-0.75, at under a millisecond per batched query, while reproducing the native ranking exactly for queries that name no relation.

---


### 23. [Verified but Vacuous: Three Failure Surfaces of LLM-Driven Verified Code Generation](https://arxiv.org/abs/2611.05590)

**<font color=#1a73e8>作者：</font>** Aditya Vempaty, Himaneesh Sompalle, Manan Tayal 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> What should ``verified'' mean when evaluating LLM-generated code? Many existing pipelines report a single verification number. We argue this collapses three distinct properties measured in a conditional audit sequence: verifier acceptance (Surface A), \emph{syntactic specification binding (Surface B: does the proof obligation bind to the spec?), and \emph{semantic specification fidelity} (Surface C: does the spec capture the informal requirement?). Two empirical demonstrations show the surfaces separate. \textbf{First ($A \neq B$), via Li@Opus (a same-model reproduction of \citet{li2025dafny}'s Dafny-as-intermediate-representation (IR) pipeline under Claude Opus 4.7) on three Python benchmarks}: it reaches \textbf{99.1\% verifier acceptance} on HumanEval while only \textbf{1.9\%} carry a certificate binding to a spec-defined predicate or function. \textbf{Second ($B \neq C$), via VCG on two Rust benchmarks}: we use VCG (which is our own in-house Dafny-as-intermediate pipeline) on Rust because the Rust target lets us enforce fully-verifiable output (every component ships as a Dafny certificate, ensures-binding gate passing by construction). Even inside that construction, \textbf{11.48\% (MBPP-Rust) and 14.82\% (VeriContest LC slice) of structurally-verified samples still fail hidden tests}. On the LC slice of VeriContest, \textbf{VCG's reported End2End rate is 7.79\% (535/6870).} The cited external rates are 5.51\% (GPT-5.5) and 1.88\% (single-shot Opus 4.7). These give descriptive differences of 2.3 percentage points and 4.14$\times$, respectively; task-budget, repair and harness differences prevent a matched-performance claim.

---


### 24. [C-GRPO: Conformal Group Relative Policy Optimization](https://arxiv.org/abs/2611.05591)

**<font color=#1a73e8>作者：</font>** Arya Fayyazi, Seyedarmin Azizi, Mehdi Kamal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning-oriented language model training increasingly relies on multiple on-policy rollouts, but standard Group Relative Policy Optimization (GRPO) uses a fixed group size, wasting compute on easy prompts and under-exploring hard ones. Existing adaptive-budget methods alleviate this inefficiency, yet their stopping rules are heuristic and do not provide a finite-sample calibration guarantee. We propose CGRPO, which replaces the fixed rollout budget of standard GPRO with calibrated conformal thresholds over task-specific nonconformity scores, combining Adaptive Prediction Set (APS)-style calibration for closed-form reasoning, a first-success score for execution-based code, automatic miscoverage selection, and periodic re-calibration. We prove finite-sample coverage for the resulting stopping rule and show that, under monotone policy improvement, recalibration induces a non-increasing expected training budget. Across six benchmarks spanning mathematics, graduate-level science, and code generation, CGRPO reduces mean training rollouts by 49-70% relative to fixed-budget GRPO while retaining strong fixed-budget accuracy, achieves the strongest pass@1 among evaluated static and dynamic baselines on different datasets, and transfers across model families with up to 82% rollout savings.

---


### 25. [RAGCompass: Generalizable Retriever Routing via Reranking](https://arxiv.org/abs/2611.05596)

**<font color=#1a73e8>作者：</font>** Valentin Six, Mufei Li, Dongqi Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Different retrievers exist for retrieval-augmented generation, yet none performs best for all queries. Therefore, the key question is: given a query and retrieved passages from different retrievers, which one is most suited for that query? Existing routers usually make predictions from query-specific features and a fixed pool of retrievers; such routers have no output for an unseen retriever and are incapable by design on a new corpus. To fill these gaps, RAGCompass reads the retrieved passage sets themselves: passages from an unfamiliar retriever or corpus stay directly comparable to other passages, so routing stays well designed where a query-only map would fail. We contrastively fine-tune a reranker against the answer each evidence set produces, which accounts for most of the gain; a small comparison head adds a moderate improvement, and neither component has retriever-specific parameters. RAGCompass improves answer F1 by 28% relative to the best fixed retriever, and outperforms fusion baselines, three query-only routers, and a prompted 8B language model. Generalization experiments show that RAGCompass keeps most of its gain under an unseen corpus, retriever, or reader, while query-only baselines fall to the best fixed retriever or below.

---


### 26. [CAPTOR: text-encoder-free grounding by counting caption co-occurrence over the visual words of a frozen encoder](https://arxiv.org/abs/2611.05599)

**<font color=#1a73e8>作者：</font>** Elad Yoshai, Natan T. Shaked  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Grounding a text query in an image needs a matrix scoring every term against every patch. Vision-language models compute it with an aligned text encoder, which many image encoders, such as histopathology-related models trained on slides alone, lack. The Caption-Anchored Patch-Term Occurrence Representation (CAPTOR) estimates the matrix without a text encoder. It clusters a frozen image encoder's patch tokens into visual words and describes each captioned image by its share of patches in each word. A term signature is the standardized difference of those shares between images whose captions mention the term and the rest. The matrix factorizes into a term-by-word table and a query-independent image factor, so an image is encoded once and a new term adds one table row. Against every training-free baseline, CAPTOR leads on Common Objects in Context (COCO), Pascal Visual Object Classes (VOC) and Cityscapes. On COCO, scored on the cells one object owns, it reaches 0.565 mean intersection over union (mIoU) against 0.502. On all three, it is also level with a text alignment trained on the same backbone, which needs gradients, a text encoder and several times the captions. On held-out breast-cancer slides, it exceeds the strongest baseline scoring patches with a pathology text encoder by 0.160 mIoU. Read through CAPTOR, UNI, an encoder trained on slides alone, exceeds such baselines by 0.132 on a common grid. Counting can therefore give a text interface to any image encoder trained without language, wherever captioned images exist.

---


### 27. [On the Generalization Limitation of On-Policy Distillation for Post-RL Consolidation](https://arxiv.org/abs/2611.05609)

**<font color=#1a73e8>作者：</font>** Yichen Wang, Yufa Zhou, Siqi Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-teacher on-policy distillation (MOPD) extends on-policy distillation (OPD) to consolidate capabilities from multiple teachers. Although prior work reports near-perfect in-distribution (IND) distillation performance, we find that this can mask incomplete capability consolidation beyond the supervised distribution. A preliminary study on synthetic reasoning shows that OPD does not fully transfer teachers' generalization capabilities. We then extend this investigation to real-world tasks, evaluating extrapolative and compositional generalization across mathematical reasoning, coding, agent, and long-context capabilities using Qwen3 models. Across extrapolative settings, OPD and MOPD reach 96.04-102.73% of their teachers' IND scores. Yet their out-of-distribution (OOD) scores remain 2.45-16.25% below the base model's. Across three compositional settings, MOPD improves IND performance over the base model, but its performance on composed tasks as OOD remains 18.19-24.34% below that of the best teachers. To understand these gaps, we examine teacher capability and data coverage as two potential bottlenecks. Jointly alleviating these bottlenecks eliminates OOD forgetting in our experiments and suggests the potential for generalization beyond the teacher. (M)OPD also reduces OOD forgetting on average relative to its reinforcement learning (RL) baselines. Analysis of the associated update geometry reveals smaller and more spectrally concentrated updates on average than those of the RL baselines, along with greater shared update structure under MOPD. Motivated by these findings, we propose geometry-based patching and base-preserving replay to improve OOD performance while largely preserving IND performance. Our findings identify a blind spot in capability consolidation via (M)OPD, highlighting the need for algorithms that explicitly support OOD retention and generalization.

---


### 28. [Hybrid Spark: Adaptive Speculative Decoding That Lets the Content Choose the Drafter](https://arxiv.org/abs/2611.05611)

**<font color=#1a73e8>作者：</font>** Ekagra Ranjan, Bharat Venkitesh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Speculative decoding (SD) speeds up large language model (LLM) serving, but its gain depends on the workload's \emph{shape}, such as batch size and context length, and on its \emph{content}. A model-based drafter proposes a short block on any content, while a model-free drafter such as n-gram lookup proposes long copies at almost no cost when the output repeats its input, as in code editing. Adaptive verification spends a batch-wide verification budget on the draft tokens most likely to be accepted, but it supports only one model-based drafter. Model-free drafters provide no per-token confidence, so they cannot take part in budget allocation, and deployments must either fix one drafter or split their GPUs between drafters. We present \sys, a framework that runs a model-based and a model-free drafter on every step and gives each request the better of their chains, within adaptive verification and entirely on the GPU, which keeps asynchronous scheduling intact. The key idea is a price per verified draft token: the goodput that slot would earn elsewhere in the batch. Once the model-free drafter's tokens carry calibrated acceptance estimates, fit once on general text, this price puts both drafters' chains on one scale. Instantiated with \dspark and an n-gram drafter in vLLM, \sys achieves 1.10--1.62\x the output throughput of \dspark on code editing at batch size~4 and 1.04--1.27\x at batch size~128, while staying at 0.97--1.01\x of it on chat at temperature~0. A single deployment can therefore serve both workloads.

---


### 29. [Route to Remember: Adaptive Memory Selection for LLM Agents](https://arxiv.org/abs/2611.05636)

**<font color=#1a73e8>作者：</font>** Zeyu Fang, Jun Yin, Yongsheng Mei 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The memory of production agents is increasingly becoming a bottleneck and is built almost exclusively from text: key points are extracted from out-of-limit context and retrieved into context at query time. Therefore, every new query incurs an additional cost that grows with the accumulated history. Weight memory is a complementary alternative that internalizes knowledge into model parameters and answers with no context at all, and has recently proven effective in self-evolving agents for internalizing skills and behaviors. However, its application in episodic and semantic memory, such as user-specific facts, remains comparatively unexplored, and a gap remains between earlier attempts at weight memory and text-based systems regarding recall performance. We study how to make weight memory competitive as a long-term factual store by applying on-policy self-distillation (OPSD). It trains a context-free student from a teacher, which is the same model conditioned on the user's memory, together with a verify-then-regenerate router that lets weight and text memory each cover the queries they handle best. On the HaluMem benchmark, OPSD matches or surpasses strong text-memory baselines, including full-context prompting and retrieval systems, while reading fewer tokens per query. We further conduct an extensive study that characterizes the behavior of weight memory and analyzes how different training recipes affect its performance. As agent harnesses move toward persistent, multi-session deployments, these results position weight memory as a practical, low-cost component of agent memory and provide insights into feasible training and evaluation protocols for combining it with retrieval.

---


### 30. [Data-Efficient Scaling-Law Discovery for Recommendation Systems via Coupled Hyperparameter Scaling](https://arxiv.org/abs/2611.05643)

**<font color=#1a73e8>作者：</font>** John Martabano Landy, Louis C. Tiao, Yao Xuan 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale ranking and recommendation models of Web platforms benefit from increased compute much as large language models do, and their scaling behavior is broadly power-law in form. Yet ranking models have heterogeneous architectures which makes their scaling law less straightforward than that of LLMs. We address how to discover the scaling law of an arbitrary ranking model efficiently. We introduce a scaling layer, which groups primitive architecture parameters into semantically coherent groups and defines how they co-vary, inducing a mapping from a low-dimensional space of hyper-hyperparameters into the full architecture space. On top of it, Axia fits scaling-informed surrogates, selects configurations by a posterior-based acquisition criterion, and returns a Pareto frontier from which per-model operating points are validated -- replacing exhaustive sweeps with a small number of informative runs. A fleet-level evaluation protocol, computed on a fixed representative model set under matched trial budgets, makes refinements to either component measurable. Our contribution is an automated system that learns model-specific complexity-quality relationships and gives uncertainty-aware guidance for allocating compute across a heterogeneous model ecosystem. Across 34 model iterations in two development cycles on Meta's ads ranking and retrieval system, the workflow yielded a mean 0.66% offline normalized-entropy improvement and 0.36% cumulative online lift.

---


### 31. [When Are Two SAE Latents the Same Feature?](https://arxiv.org/abs/2611.05655)

**<font color=#1a73e8>作者：</font>** Alexandra Suvorikova, Ilgam Latypov, Anton Trukhan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Comparing sparse autoencoders (SAEs) requires connecting feature correspondence, differences between whole dictionaries, and uncertainty from finite evaluation data. We develop a framework that connects these tasks through an energy-weighted optimal-transport plan under a specified similarity geometry. The same plan defines a dictionary-level discrepancy, decomposes it into latent contributions, and quantifies how each latent's mass is distributed across counterparts. We characterize relationships between decoder, activation, and first-order causal similarities; idealized models clarify the interpretation of splitting and absorption. For fixed trained SAEs, we derive joint asymptotic inference for transport costs and fractions, accounting for activation similarities and both energy marginals estimated from the same documents. A joint document bootstrap gives asymptotically valid simultaneous confidence bands. Experiments across four language models locate cross-seed discrepancy and separate context-dependent changes.

---


### 32. [Grounded but Not Immune: Confirmation Bias in Agent-as-a-judge](https://arxiv.org/abs/2611.05662)

**<font color=#1a73e8>作者：</font>** Drake Benjamin Brown, Khushbu Pahwa, Yubin Ge 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating open-ended agent tasks increasingly falls to an Agent-as-a-Judge: an evaluator handed tools and the agent's full trajectory so it can verify a result against the environment. The premise is that a judge that gathers its own evidence should be grounded by it. We show that this grounding does not immunize the judge against confirmation bias: a single false pre-screening note, attributed to an authority and carrying no evidential bearing on the correct verdict, overturns up to 40% of a tool-using judge's correct verdicts across four judges and five datasets, even though the judge collects decisive evidence. The shift is driven by specific properties of the cue. We treat this cue as a controlled diagnostic of confirmation bias rather than an adversarial attack. Our central contribution is to explain how confirmation bias changes the judge's behavior in a trajectory. We classify changes in judge behavior and attribute changes to one of three failure modes: over-trust (verify, conclude correctly, then defer), hallucination (fabricate support for the flip), and under-investigation (stop at the first corroborating signal). For the two Claude judges, the failure is predominantly over-trust (67-75% of harmful flips), while smaller judges have error modes spread across all three. Lightweight mitigations blunt but never remove the bias.

---


### 33. [How Do Artificial Agents Make Decisions in Light of Visual Data?](https://arxiv.org/abs/2611.05671)

**<font color=#1a73e8>作者：</font>** Keyty Loza, Shayan Monadjemi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have demonstrated significant advances in reasoning with visual data, which is particularly important given that much of human knowledge is encoded visually in scientific articles and other sources. However, a gap remains in understanding how artificial agents, powered by VLMs, perceive and navigate decision-making under uncertainty in the presence of visual data. This study explores this gap by evaluating and analyzing autonomous decision-making processes. Building upon prior work in visualization literacy and decision theory, we conducted two complementary studies: one examining how agents perceive and quantify uncertainty encoded in visualizations, and another investigating how artificial agents make decisions based on visual data in the form of images. We analyzed perception accuracy and decision performance across models and visualization types. Our results show that GPT-4o demonstrates the highest accuracy in perceiving uncertainty in pie and bar charts among the tested models. For decision-making, autonomous agents showed the best alignment with rational decision theory when uncertainty was represented through circle charts, icon arrays, or text.

---


### 34. [GeoDIVE: Geospatial Descent Informed by Value Estimation](https://arxiv.org/abs/2611.05697)

**<font color=#1a73e8>作者：</font>** Hamza Iqbal, Dan Cher, Eric Xing 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Finding specific objects, structures, and spatial patterns supports critical work in agriculture, infrastructure planning, environmental monitoring, and disaster response. These features, however, are often dispersed across very large regions and span dramatically different spatial scales, which defines a search space that is costly to embed, maintain, and search naively. We introduce GeoDIVE, a model that treats a multiresolution satellite image gallery as a forest and uses best-first traversal to determine which tiles to encode. At each visited node, a lightweight model then predicts an optimistic estimate of the best query similarity hidden among its descendants using the query and subtree representations. In evaluations with image and open-vocabulary text queries, GeoDIVE matches exhaustive search at 10% of the encoding cost for image queries and leads all tested baselines at every budget in both modalities. To support future evaluation of multiscale geospatial search, we also release object-level image and text queries for Git-10M, constructed from Microsoft building footprints and OpenStreetMap polygons with VLM-generated captions. Source code and models will be made publicly available.

---


### 35. [Agents, Think Only When it Helps](https://arxiv.org/abs/2611.05709)

**<font color=#1a73e8>作者：</font>** Min-Seon Kim, Seungdong Yoa, Sanghyu Yoon 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agent distillation transfers agentic capabilities to student models by training on complete teacher trajectories that typically interleave thoughts and actions. We question how critical thought supervision is for agents' ultimate action performance. To answer this, we disentangle their impacts by independently perturbing teacher thoughts and actions during distillation. On widely adopted agent benchmarks across model scales, altering or discarding thoughts has little effect on student performance. We find, however, that thought supervision becomes important when information about the thought is not disclosed in the corresponding action during training. By identifying such discrepant cases, our findings challenge the common practice of distilling entire teacher trajectories for LLM agents, and offer a new insight that thought supervision can be a discernible choice for efficiency depending on whether the information of thought is disclosed in the action.

---


### 36. [Same Method, Different Task: What the Bitter Lesson Does Not License in Social Simulation](https://arxiv.org/abs/2611.05717)

**<font color=#1a73e8>作者：</font>** Justin Downes, Robby Milletich, Newel Hirst  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The bitter lesson holds that general methods leveraging computation defeat hand-encoded domain knowledge. We argue it carries a condition its popular reading omits: in every case Sutton cites, the general method was scaled against the same task the domain engineering was solving. Social simulation substituted across tasks instead, replacing hand-built agents with an artifact optimized for predicting text. The move is bitter-lesson-shaped, but the lesson does not license it. Prediction is a solitary act: the predictor bears no consequences from the interaction it models. Cooperation, defection, and norm enforcement are phenomena of interested parties; they do not exist for a disinterested observer at any scale. What is missing is not emergence, which LLM populations already show, but stakes. We show that several anomalies reported in prior work (excess cooperation that predates alignment training, collective agreement without individual fidelity, and population homogeneity) follow from this account. A 540-agent pilot with pre-specified hypotheses, which tests sensitivity to persistent consequences rather than cooperation, finds that consequences reshape strategies in two of three model families but never produce human-like heterogeneity. We argue for mixed-motive settings that shape agents rather than only test them, and ask whether agents should be pretrained differently from predictors.

---


### 37. [Cognitive Bias Signatures in Search-Equipped LLM Agents: A Stage-Resolved Analysis](https://arxiv.org/abs/2611.05720)

**<font color=#1a73e8>作者：</font>** Yanru Xiao, Yingwei Yu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Search can help LLM agents correct mistakes, but their starting conditions may shape which evidence they find and use. Drawing on cognitive-bias paradigms, we develop a controlled search harness to examine result order, records of prior work, and initial hypotheses while holding each question and document collection fixed. Matched controls distinguish order effects from differences in document composition and the effects of failed work from context length. Across 10 models and 1,000 synthetic search worlds, we track queries, retrieved documents, document openings, and final answers. Our comparisons suggest that final answers are more sensitive to initial evidence order during active search than when all evidence is supplied in full. Dead-end histories can reduce strategy switching relative to matched neutral histories, indicating an effect beyond context length. Under wrong hypotheses, stage measurements distinguish reduced retrieval or opening from errors that persist after counter-evidence is opened. Exploratory interventions show that opening counter-evidence more often can coincide with lower accuracy, while accuracy can improve with little change in opening.

---


### 38. [Give the Drafter a Second Chance to Guess: Parallel Reconsideration for Speculative Decoding](https://arxiv.org/abs/2611.05724)

**<font color=#1a73e8>作者：</font>** Hoang Anh Duy Le, Huibing Dong, Alireza Khadem 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates large language model inference with a small drafter, whose per-guess acceptance rate determines the achievable speedup. Feature-level drafters share a design choice: every token, easy or hard, is drafted under a single forward pass. Many of the tokens the target rejects are ones the drafter is itself unsure about yet the target answers decisively. To address this, we introduce Parallel Reconsideration: guided by its own uncertainty, the drafter reconsiders its hesitant guesses with extra passes that run in parallel with the one-pass draft, adding negligible latency. A co-designed training recipe and serving-time drafting algorithm append these reconsidered guesses to the original draft tree as refined candidates. Across models and benchmarks, on average, Parallel Reconsideration improves over the baselines by 5.3% to 10.2% on acceptance length and by 3.5% to 9.2% on speedup.

---


### 39. [Do Language Models Know Which Constraints Belong Together?](https://arxiv.org/abs/2611.05726)

**<font color=#1a73e8>作者：</font>** Junbo Jacob Lian, Kaixuan Chen, Hanzhang Qin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dantzig-Wolfe reformulation strengthens the linear relaxation of a mixed-integer program by convexifying a chosen set of constraint families, and every candidate costs a column generation run. The choice is hard when families strengthen the bound only together, because a search that adds one family at a time then stops at the linear relaxation. The classical inequalities of lot sizing, network design and facility location rest on such zero-marginal groups. We prove that when each evaluation convexifies at most $s$ of $k$ families, any method that observes only bounds needs a covering number of evaluations, of order $k^w$, to find a hidden group of $w$ families, also on actual Dantzig-Wolfe relaxations. A prediction that misses $e$ members reduces the cost to $\Theta(k^e)$, through one staged search that does not need to know $e$, so the evaluations a prediction saves measure what the predictor knows. We study two sources of predictions. A one-pass lookahead at an optimal LP dual is provably blind to groups whose families share no variable, and a language model reads the names and text of the model. JointDW verifies the prediction of the language model with the staged search and interleaves it with the lookahead at a bounded loss. Groups that strengthen the bound only jointly appear in a quarter of the MIPLIB-NL models whose bound can be improved. There the strongest language models identify them about as often as the lookahead, their predictions rest on the names for textbook models, and reasoning about doubles the accuracy of the same model. On larger models with distracting families, the lookahead finds the group in one evaluation of three families. Language models given only the text seldom name it, while one reasoning model given every coefficient names it in all but one answer and then needs fewer evaluations than the lookahead for pairs of families.

---


### 40. [Prospective Memory for Proactive LLM Agents](https://arxiv.org/abs/2611.05731)

**<font color=#1a73e8>作者：</font>** Yuanchen Bei, Zhining Liu, Tianxin Wei 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most memory systems for LLM agents are retrospective, preserving and retrieving past information to inform current decisions. Proactive agents, however, also require prospective memory: retaining future-directed intentions and realizing them when appropriate opportunities arise, even without explicit requests. Crucially, remembering the right intention does not guarantee acting at the right time: a related observation may call for waiting, while a later cue may make the same intention actionable. Inspired by cognitive theories of human prospective memory, we introduce Pro-Memory, a memory framework that separates maintaining future intentions from deciding when and how to realize them. Pro-Memory preserves pending objectives linked to their supporting evidence, assesses new observations against their original goals and activation conditions, and coordinates appropriate contributions with the agent's ongoing actions. It further updates intention states based on actions actually issued or evidence of resolution, while an experience memory distills feedback from completed episodes into guidance for future decisions. Experiments on two benchmarks spanning delayed-intention tasks and open-ended proactive assistance demonstrate consistent improvements in proactive task performance over representative memory approaches across multiple LLM backbones, while limiting unnecessary interventions.

---


### 41. [PersonaCodeBench: Evaluating Coding Agents in Persona-driven Human-Interactive Sessions](https://arxiv.org/abs/2611.05739)

**<font color=#1a73e8>作者：</font>** Haixin Wang, Jianheng Hou, Hongyu Shen 等 30 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents must deliver correct software while respecting users' expertise, preferences, and working conditions. Existing benchmarks increasingly incorporate interaction, yet personalized requirement fulfillment remains underexplored. We introduce PersonaCodeBench, which turns user characteristics into verifiable obligations in persona-driven multi-turn coding sessions. Our persona pool spans roles, technical abilities, interaction preferences, and practical constraints, yielding task-grounded evolved requirements for implementation, permissions, testing, explanation, and delivery. At runtime, a controller governs user simulator responses and requirement disclosure, using online requirement evaluation to provide feedback and advance the interaction. Requirements emerge progressively, with their content, disclosure conditions, and acceptance criteria fixed before evaluation. A completion verifier and a personalization verifier separately assess native correctness and persona fulfillment. Joint pass requires both adherence to the declared budget and compliance with validity conditions. We evaluate all major frontier agents, establish a comprehensive leaderboard, and conduct detailed experimental analyses to validate effectiveness. PersonaCodeBench supports reproducible evaluation of coding agents' ability to meet explicit, personalized user expectations alongside coding objectives.

---


### 42. [Text-Only Domain Adaptation for Low-Resource Medical ASR: Shallow Fusion and Density Ratio Rescoring for Hausa](https://arxiv.org/abs/2611.05744)

**<font color=#1a73e8>作者：</font>** Oche David Ankeli, Hassan Adelani Luqman, Theodora Ngozi Egbunike 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automatic speech recognition (ASR) systems often struggle with specialised medical vocabulary, especially in low-resource languages where domain-specific speech data are scarce. We investigate text-only domain adaptation for Hausa medical ASR using the fixed MMS-1B-FL102 acoustic model and two decoding-time language-model fusion methods: Shallow Fusion (SF) and the Density Ratio Approach (DRA). A 4-gram KenLM trained on 19,421 Hausa health sentences serves as the medical target model, while a 75,372-sentence general-domain model provides the source prior for DRA. Evaluation uses 250 recordings of 25 physician-reviewed prompts from 10 speakers across six northern Nigerian states. Under prompt-disjoint five-fold cross-validation, SF and DRA reduce WER from 29.56% to 23.55% and 23.33%, respectively. Both significantly outperform greedy decoding (p < 0.001), while their difference is not significant (p = 0.423). However, general-LM-only SF achieves 23.96% WER, indicating that the medical LM's additional improvement over a general LM is modest. Medical Term Error Rate also improves under fusion, but does not establish a distinct medical-domain advantage. These findings demonstrate that lightweight, text-only language-model fusion can improve Hausa medical ASR without additional domain-specific speech collection.

---


### 43. [Pairing Expert Critique with LLM-Driven Refinement: An Iterative Approach for Curating Quality AI Evaluation Datasets](https://arxiv.org/abs/2611.05749)

**<font color=#1a73e8>作者：</font>** Honson Ling, Kidus Admassu, Stephanie Rosenthal  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Evaluating and improving domain-specific LLM responses requires high-quality reference data and rubrics, yet expert authoring is slow and expensive, and synthetic datasets may fail to capture practitioner preferences unless they are grounded in expert judgment. We present SME-C (Subject Matter Expert Critique), a human-AI workflow that captures expertise through lightweight critiques of candidate responses and complements it with LLM-driven analysis and refinement to iteratively curate response datasets and evaluation rubrics. We validate SME-C in the domain of financial business briefs, collecting 3,853 critiques from 411 finance professionals on 520 queries across two survey rounds. We evaluate two LLM-driven refinement strategies: one guided by the experts' written critiques and one that infers critique solely from their preference votes. In a blind validation survey with 100 additional professionals, we found that both strategies significantly improved quality over the experts' top-ranked baseline responses. The gains were concentrated among weaker original responses, and the two strategies excelled in different ways: critique-based refinement produced more domain-grounded improvements, whereas vote-based refinement was more effective at identifying and removing irrelevant content. The resulting rubrics and refined dataset support reproducible offline evaluation and benchmarking of LLMs, suggesting that structured expert critique is a viable alternative to expert authoring for building high-quality, domain-specific evaluation resources more quickly, at scale, and at lower cost.

---


### 44. [Mechanical Engineering Skills: An Open Library of Agent Skills for Design, Analysis and Manufacturing](https://arxiv.org/abs/2611.05758)

**<font color=#1a73e8>作者：</font>** Achuth Chandrasekhar, Jesse Barkley, Peter Pak 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Mechanical engineers use specialized tools for CAD, simulation, manufacturing and research, each with a distinct interface and learning curve. We present Mechanical Engineering Skills, an open library of 33 agent skills that makes these capabilities accessible through a single text or voice conversation. Each skill combines operating instructions, executable tools and verification procedures. A language model interprets the request, selects and coordinates skills, while deterministic tools perform computations and return checked results. Default workflows require no tool-specific interface training, local model execution or model fine-tuning; skills load on demand and install with one command. Nineteen skills adapt published or preprint research from our laboratory, including text-to-CAD, linkage synthesis, CFD setup, stress-field and lattice surrogates, equation discovery, additive-manufacturing planning and in-process monitoring. Fourteen additional skills support core engineering and education. We describe the skill format, design principles and a method for translating research into practical workflows. Five case studies with explicit evidence scopes and independent reruns demonstrate exact analytical agreement for lattice homogenization, rocket apogee predictions within 4% of stored OpenRocket references, an equation fit nine times more accurate than a cubic polynomial at an unseen temperature, and an end-to-end rehearsal of porosity monitoring. Controlled agent comparisons remain future work. The open library is available at this https URL.

---


### 45. [PAYWORTHY: Can LLMs Predict Which Freelance Jobs an AI Agent Will Complete?](https://arxiv.org/abs/2611.05759)

**<font color=#1a73e8>作者：</font>** Mohammad Reza Rezaei, Dingxian Wang, Brett Levert 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Before an AI agent takes on a paid job, someone has to judge whether it is likely to succeed. We test whether frontier language models can make this call before any attempt. We propose PAYWORTHY which contains 1{,}494 real freelance job postings, sampled from 18.8M postings made between 2020 and 2026 on a freelancing platform. An agent attempts each job from the posting alone in a single run, and an LLM judge acting as the client decides whether to accept the work. We ask 18 models to forecast how likely the agent is to succeed and measure how well each model's forecasts rank the accepted jobs above the rejected ones (AUC, where 0.5 is a random ranking). The answer depends on how the agent is described. Told what the agent cannot do, every model ranks the jobs well (AUC 0.66--0.86). Told instead that it is a generic agent with a browser and code execution, the same models rank the same jobs about as well as a random ordering (0.45--0.56). These results hold under judges from four other model families (Claude, GLM, Kimi and Qwen), and the informed forecasts also rank the verdicts of two human raters.
Code is available at this https URL

---


### 46. [How Well Can Large Language Models Impersonate Individual Authors? A Comparative Evaluation](https://arxiv.org/abs/2611.05771)

**<font color=#1a73e8>作者：</font>** Harshit Gupta, Shunichi Ishihara  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study investigates the authorship impersonation capacity of six widely used large language models (LLMs): Gemini 3 Pro, Claude Opus, GPT 5.2, GPT 5.2 Pro, DeepSeek 3.2, and Grok 4.1 Fast. The evaluation was conducted using short product review texts selected to ensure high within author consistency in individual writing style. Two types of in context prompt were designed: a simple prompt with minimal instruction and a complex prompt incorporating explicit stylometric guidance for mimicry. Authorship mimicry was evaluated using a cosine distance based distance to training metric, supplemented by visual analyses of embedding distributions. The results indicate that authorship impersonation remained challenging for most LLMs, with Gemini 3 Pro showing the strongest apparent mimicry performance. However, subsequent overlap analysis revealed that Gemini 3 Pro extensively copied and reused sentences and phrases from the training texts, at levels far exceeding those observed among human authors. Follow up factor analyses showed that training set consistency was the most robust predictor of mimicry success across models, whereas author distinctiveness did not generalise as a reliable predictor. Global embedding visualisations further revealed a consistent macro level pattern: for most models, generated texts occupied regions of the embedding space that were largely separated from the corresponding human training clusters. This indicates limited convergence towards target author style and suggests the presence of model specific lexical and phraseological preferences. The findings highlight the importance of distinguishing genuine stylistic imitation from direct textual reuse and have implications for the forensic analysis of textual evidence involving potential LLM enabled impersonation.

---


### 47. [Timing is Everything: Inferring Temporal Membership in Continually Updated Models](https://arxiv.org/abs/2611.05781)

**<font color=#1a73e8>作者：</font>** Jie Fu, Xiangpeng Deng, Yuan Hong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Continual model updating has become a common practice in the deployment of machine learning systems. However, the dynamic training behaviors give rise to new risks not sufficiently addressed by existing studies. In this paper, we present the first systematic study of temporal privacy risk in continually updated deep learning models. We formalize the notion of temporal membership in continually updated models. We then define the temporal membership inference attack, which seeks to infer whether and when individual samples were involved in model training, at both timestamp-level and interval-level granularities. To this end, we propose TMIA, a novel black-box attack that leverages bidirectional LSTMs to infer temporal membership from model outputs observed across successive updates. Through extensive experiments on three language models and three image classification models, we show that TMIA is highly effective and significantly outperforms existing baselines. Finally, we evaluate three potential defenses, revealing the trade-off between privacy protection and model utility.

---


### 48. [FlyHash for LLM Agent Memory: An Empirical Validation and a New Application](https://arxiv.org/abs/2611.05791)

**<font color=#1a73e8>作者：</font>** Mohan Bheemadolu, Chrisogonas O. Odhiambo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly rely on external memory stores to retain information across conversations, typically via dense vector embeddings searched with approximate nearest-neighbor methods. The fruit fly's olfactory circuit computes a locality-sensitive hash of sensory input using a strikingly different mechanism - sparse random projection followed by winner-take-all competition - and prior work (Dasgupta et al., 2017) showed this scheme, dubbed FlyHash, preserves neighbor structure better per bit than conventional random-hyperplane hashing (SimHash) on several benchmarks. We apply FlyHash, to our knowledge for the first time, to LLM agent memory retrieval, and ask three questions a practitioner actually needs answered: does the quality advantage hold under a correctly matched-bit protocol (it does, robustly, across 10 seeds and four datasets spanning two modalities, with one specific, previously undocumented comparison pitfall identified and corrected along the way); does that advantage translate into real memory and latency savings, including against the dense-vector indexing (HNSW) practitioners default to today (no: at equal bits FlyHash's codes are larger and slower to compare than SimHash's, and HNSW dominates both hash methods at ordinary scale; a sparse-set comparison we introduce recovers most but not all of a naive latency gap, leaving hashing's practical case narrower and more specific than the quality result alone implies); and does the advantage survive genuine, non-circular agent-memory relevance labels rather than the nearest-neighbor-by-embedding proxy this literature otherwise relies on (it does). We report all three answers precisely, including the two that narrow rather than flatter the headline result, and release our implementation, a working agent-memory demo, and a full account of the methodological pitfalls we found and corrected.

---


### 49. [Consistency Is Not Understanding: Orbit Audits for Neural Field Weight Readers](https://arxiv.org/abs/2611.05798)

**<font color=#1a73e8>作者：</font>** Sungguk Cha, Mintae Kim, Youngsub Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recognizing visual content from neural-network weights requires separating functional information from arbitrary parameter coordinates. We audit this separation with hidden-neuron permutations and positive ReLU rescalings that preserve the represented function. The study contains 480 independently fitted shape fields and 1,000 MNIST fields, with transformed copies grouped by origin. On shape recognition, a statistics reader falls from \ShapeRawStats\% to \ShapeJointStats\% accuracy under joint transformations; a normalized set reader retains \ShapeNormSet\% with unchanged predictions. Four small frozen language models obtain \LMRange\% raw accuracy with next-token scoring. A separate four-configuration reasoning experiment with 1,920 scored sessions obtains \FrontRawRange\% raw accuracy with generated answers, while fresh identical raw prompts disagree on \FrontRawRepeatRange\% of origins. Canonicalization makes equivalent prompts identical, but this neither establishes recognition nor guarantees identical generated responses. Joint correctness/agreement metrics, semantic-cue controls, fresh repeats, and exact-rational rounding bounds separate these failure modes. The result is an inspectable evaluation protocol for visual weight readers, with claims restricted to the tested fields, prompts, and execution configurations.

---


### 50. [GREP: Grounding Generated Room Evaluation in Principles](https://arxiv.org/abs/2611.05802)

**<font color=#1a73e8>作者：</font>** Mohan Cao, Yongsen Mao, Chucheng Xiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent LLM-centric advances can generate attractive furnished rooms by selecting and arranging assets. Yet evaluation remains limited to specific perspectives or predefined questions, failing to reflect overall scene quality. To address this pressing need, we introduce GREP. Its core is a focus shift from defining specific questions to establishing a three-tier evaluation philosophy: basic physical validity checks whether a scene obeys physical constraints; visual coherence concerns compatibility in object scale, style, and composition; and, at the highest level, human-use logic requires object arrangements to align with everyday human habits. Guided by these principles, an evaluation agent autonomously and adaptively identifies issues from scene context, gathers evidence, and produces scores and reports. This supports scene-specific issue discovery and reliable judgments. Experiments show that (1) GREP achieves 87% agreement with human majority preferences, substantially outperforming baseline evaluators. (2) GREP reports improve scene quality through refinement, whereas score-only and no-feedback baselines show slight declines. (3) GREP suggests that as planning ability improves, recent models such as GPT-5.6 Sol can move from relying on pipelines and harnesses to challenging their guidance and constraints, but still lack the ability to resolve the resulting conflicts. Stronger models are therefore expected not only to plan well, but also to adapt to external guidance and constraints more flexibly. Project page: this https URL

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-207](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
