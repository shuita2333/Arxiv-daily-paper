# 🧠 大模型相关研究 | 2026年10月02日

> 本类共 **390** 篇论文：已确认 **371** 篇，待复核 **19** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**351-390**（第 8/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-390**

---

### 351. [PhantomEnvironments: Training LLM Agents in Fictional Worlds](https://arxiv.org/abs/2609.40221)

**<font color=#1a73e8>作者：</font>** Anmol Kabra, Swathi Saravana Selvam, Albert Gong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training LLM agents with reinforcement learning (RL) is bottlenecked by environments, which must provide verifiable rewards, support long-horizon interaction, and scale cheaply. Existing approaches rely on costly human-curated data or on LLM-generated environments that risk hallucinations and benchmark contamination. We show that LLMs can instead be trained into capable search agents using synthetic environments generated entirely by rules, whose generation requires no LLM and has zero marginal cost. We build PhantomEnvironments, multi-turn RL environments from fictional worlds, where agents must search a corpus of templated articles to answer multi-hop questions. Despite sharing no facts with the real world, these strikingly simple environments yield agents that transfer to real-world multi-hop search benchmarks, often outperforming real-world training data on newer benchmarks. Trained agents generalize to unseen fictional universes, and Qwen models learn to scale their search budget roughly linearly with question difficulty, suggesting emergent search scaling from environment interaction alone. Ablating environment complexity reveals that hop count drives transfer more than constraints or comparisons: even the simplest rule-generated environments are a surprisingly effective, free resource for training generalizable LLM agents.

---


### 352. [EviRover: Reinforcing Agentic Perception Beyond a Glance](https://arxiv.org/abs/2609.40230)

**<font color=#1a73e8>作者：</font>** Kaixuan Fan, Kaituo Feng, Tianshuo Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual perception is conventionally formulated as a one-shot prediction from a single glance at the image, under the assumption that the image content and the model's parametric knowledge suffice to resolve the query. This assumption often fails in real-world scenarios that hinge on fine-grained visual details or require knowledge-intensive and up-to-date information. We term such cases \textit{perception under insufficient evidence} and formulate perception as an agentic process that can obtain information beyond a single glance. To address the absence of data for this setting, we design two dedicated data generation pipelines, yielding EviRover-SFT-5K and EviRover-RL-12K for training. We further construct EviLens, a human-verified benchmark comprising 688 instances across five perception categories. Building on these data, we present EviRover, to our knowledge the first perception agent explicitly trained to resolve perceptual queries through interaction, using supervised fine-tuning followed by agentic reinforcement learning. Experiments show that the 4B EviRover outperforms its backbone by 30 points on average on EviLens, reaching performance comparable to advanced proprietary models. The gains transfer beyond EviLens to WebEyes, conventional perception benchmarks, and general multimodal benchmarks, including a 15-point improvement on BrowseComp-VL. All code, models, and data are released.

---


### 353. [Distribution Matching Distillation for Continuous Diffusion Language Models](https://arxiv.org/abs/2609.40235)

**<font color=#1a73e8>作者：</font>** Paul Le Van Kiem, Dario Shariatian, Umut Simsekli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous diffusion language models generate all tokens in parallel, yet high-quality generation can still require hundreds of network evaluations (NFEs). We study how distributional distillation can reduce this cost by exploiting the student's probabilistic token outputs. Our unified formulation connects the student's output parameterization to the resulting gradient estimators and yields two methods with the same student architecture and reverse-KL matching objective: Simplex-DMD uses continuous token relaxations and pathwise gradients, while Reinforce-DMD uses categorical sampling and REINFORCE with a learned density ratio. We develop both methods for multi-step generation and investigate the training and sampling choices associated with each parameterization. On OpenWebText, for sequences of 1,024 tokens, Simplex-DMD achieves a generative perplexity of 45.6 at a unigram entropy of 5.44 nats in just 4 NFEs, a 49% reduction relative to the strongest evaluated diffusion baseline at matched entropy and sampling budget. Reinforce-DMD improves the frontier at larger budgets, reaching a generative perplexity of 14.9 at an entropy of 5.00 nats with 256 NFEs, a 20% reduction under the same comparison protocol.

---


### 354. [Comparison of techniques for fine-tuning open-weight models for entity extraction from radiology reports](https://arxiv.org/abs/2609.40236)

**<font color=#1a73e8>作者：</font>** Aawez Mansuri, Kush Mehta, Mohammadreza Chavoshi 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Converting free-text radiology reports into structured labels supports cohort building, quality assurance, and monitoring of clinical imaging models, but the strongest label extractors are hosted proprietary models whose use raises privacy, cost, and reproducibility concerns. We asked whether a fine-tuned open-weight model (Gemma-3-12B) can match GPT-4o at multi-label intracranial hemorrhage (ICH) acuity extraction from non-contrast head-CT reports, and which ingredients matter. Using a 2x2 design, we crossed two adaptation strategies (a discriminative classification head, CH; generative instruction fine-tuning, IFT) with two training-data sources (distillation of real GPT-4o-labeled reports; synthetic reports generated by GPT-4o from real exemplars), across five training sizes, benchmarked on 100 expert-adjudicated reports against GPT-4o and the un-tuned open-weight base. The distilled instruction-tuned model (DIFT) matched GPT-4o (macro-F1 0.845 vs 0.850; p = 1.000) and exceeded the base model by 0.178. The decisive factor was the training-data source, not the fine-tuning method: both synthetic-data models failed to exceed the un-tuned open-weight base at any training size and underperformed the distilled models across all acuity classes. Fine-tuning and inference fit within the memory envelope of a single 24 GB consumer GPU. For narrow, high-value clinical label-extraction tasks, distilling real reports, rather than generating synthetic ones, is what closes the gap to a hosted model, enabling a private, low-cost, version-stable on-premises alternative.

---


### 355. [ComputerSD: Online Self-Distillation from Real-Time Feedback for Computer-Use Agents](https://arxiv.org/abs/2609.40253)

**<font color=#1a73e8>作者：</font>** Yong Du, Tongbo Chen, Zhengxi Lu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online training enables computer-use agents (CUAs) to improve through interaction with executable environments. However, existing methods primarily rely on sparse outcome rewards, which provide no supervision for intermediate actions. On-policy self-distillation (OPSD) offers token-level learning signals through privileged rescoring, but directly applying it to CUA online training presents two challenges: fixed guidance may become misaligned with the student's current state, and guidance-induced probability shifts may conflict with step-level correctness. We introduce ComputerSD, an online self-distillation method for CUAs that converts real-time feedback from executed GUI transitions into guidance for policy learning. A fine-tuned GUI analyzer produces guidance and a step-level value score after each action; the guidance provides privileged context, while the score regulates the resulting OPSD signals. ComputerSD jointly optimizes token-level OPSD and trajectory-level GRPO in a fully asynchronous training framework. On OSWorld-Verified, ComputerSD outperforms outcome-only GRPO by 1.9 and 4.1 percentage points on the general-purpose Qwen3-VL-8B-Thinking and specialized EvoCUA-8B backbones, respectively. Evaluation in out-of-distribution settings further supports the generalizability of ComputerSD. These results demonstrate the effectiveness of learning from real-time feedback through online self-distillation for CUAs.

---


### 356. [OpenTSLM TeeMoE: A Unified Time-Series Language Model for Forecasting, Contextual Prediction, and Reasoning](https://arxiv.org/abs/2609.40265)

**<font color=#1a73e8>作者：</font>** Tony Chen, Timo Stoffregen, Maxwell Xu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world time-series applications increasingly require models that can handle time series forecasting, context-conditioned prediction, and language-based temporal reasoning. Yet current time-series foundation models remain fragmented across these capabilities: numerical specialists often provide the strongest forecasts, while language-based models offer broader contextual understanding and analysis. A central challenge is to unify these heterogeneous capabilities without reducing their individual performance. We introduce OpenTSLM TeeMoE, a generalist time-series language model that can forecast directly from observed time series, reason over textual context and temporal patterns, and synthesize and refine predictions from external numerical forecasting specialists. We independently train three low-rank experts for forecast aggregation, native forecasting, and temporal analysis over a shared backbone. A learned LoRA mixture-of-experts controller then weights their frozen parameter updates for each request. Our proposed model achieves strong performance on widely used benchmarks for time series forecasting, context-conditioned prediction, and language-based temporal reasoning, ranking among the top three on GIFT-Eval by mean MASE rank, Context is Key by RCRPS, and TimeSeriesExam by accuracy.

---


### 357. [cua-speedrun: Standardized Benchmarking of the Speed of Computer-Use Agents](https://arxiv.org/abs/2609.40284)

**<font color=#1a73e8>作者：</font>** Pranjal Aggarwal, Lawrence Keunho Jang, Sean Welleck 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Computer use agents (CUAs), which use graphical user interfaces (GUIs) to complete tasks on a computer, have recently surpassed human performance on many standard benchmarks, including difficult long-horizon tasks. Their capabilities are undoubtedly impressive, however, a key barrier to the widespread adoption and deployment of CUAs remains their speed and cost. Progress towards faster yet capable CUAs requires reliable evaluation of their speed, but many CUA benchmarks currently face a reproducibility crisis. Benchmarks are based on complex infrastructure with varying machine and container configurations that confound the evaluation of the execution speed of CUAs. Towards addressing this gap, we propose cua-speedrun, which introduces standardized infrastructure and task sets, with a focus on evaluating the speed and efficiency of CUAs. cua-speedrun uses a uniform virtual machine setup and execution pipeline, along with a common agent interface that enables single-agent implementations to operate seamlessly across different benchmarks. Across four different CUA benchmarks, we evaluate how reasoning effort, agent harnesses, and environment latency affect performance, speed, and cost. We find no single model family is optimal for all three; none of the open-weight models are on the frontier, and also, unintuitively, for some models increasing the reasoning effort can speed up task completion, while faster environment input-output can slow down overall task completion time. We also demonstrate that we can effectively reduce the evaluation task set of most CUA benchmarks without degrading overall statistical power, allowing for more efficient benchmarking and comparison. We believe cua-speedrun will enable structured progress towards fast, efficient CUAs, unlocking new real-world use cases and applications. All code, infrastructure, and analysis are available at this https URL.

---


### 358. [PivotOPD: Learning to Recover from Pivotal Mistakes in Multi-Turn Agents](https://arxiv.org/abs/2609.40285)

**<font color=#1a73e8>作者：</font>** Yinghui He, Yapei Chang, Khushi Bhardwaj 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) is a promising approach for training language agents, providing dense teacher supervision on student-generated trajectories. However, in multi-turn interaction, an incorrect action changes the states the student encounters later, so errors compound across turns. In preliminary experiments across three Qwen3 models (8B to 235B), we find that more than half of the failed rollouts contain a pivotal mistake, an action that moves the agent farther from completing the task, and this mistake typically occurs early. These pivotal mistakes often remain recoverable: guiding the model for only a few turns after the pivotal turn can restore task success. We therefore propose PivotOPD, an on-policy distillation framework that jointly trains the student to prevent pivotal mistakes and to recover from the states they create. At each pivotal mistake, a teacher model provides a gold action and then names a recovery action at each of the next few turns. Preventive distillation uses the gold action with reverse KL to steer the student away from the pivotal mistake, while recovery distillation uses the recovery actions with forward KL to transfer recovery behaviors that the student rarely samples. Against 13 baselines on ALFWorld, WebShop, and Search-based QA, PivotOPD achieves the strongest average performance for both Qwen3-1.7B and Qwen3-8B students, improving over the strongest baseline on ALFWorld by +5.5% with the 1.7B student. The gains also transfer to another model family on the software engineering domain, where PivotOPD raises the resolve rate of a Nemotron-3.5 student on SWE-Bench Verified by +3.2%. Project page: this https URL

---


### 359. [Linguistic Loopholes in LLM Unlearning: From a 174-Language Benchmark to Coverage-Aware Unlearning](https://arxiv.org/abs/2609.40286)

**<font color=#1a73e8>作者：</font>** Tyler Skow, Shravan Chaudhari, Rama Chellappa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Unlearning a fact in one language does not guarantee its removal in others as changing the query or even the requested answer language can reopen seemingly forgotten knowledge -- a cross-lingual loophole. The most straightforward solution to this challenge -- unlearning in all languages -- is neither scalable nor desirable as it amplifies damage to unrelated model capabilities. We introduce the task of language budgeted multilingual unlearning where the goal is to select a subset of languages that maximizes cross-lingual erasure. To study this task we introduce the Cross-Lingual Unlearning Tensor, an unlearning benchmark that spans 174 language--script pairs and 25 atomic paraphrase types to examine when forgetting generalizes across linguistic expressions of the same knowledge. We further propose COVER, which selects source languages to maximize predicted COVERage of languages receiving no forget supervision, enabling unlearning on a language budget. Surprisingly, we find naively selecting strong individual sources does not reliably compose into strong source sets motivating our development of COVER. At deployment COVER only requires benign calibration data and access to the frozen model. Across three model families and two disjoint forget sets, COVER reduces mean held-out residual access by 7.8--27.3% relative to uniform source selection. We find these gains extend beyond synthetic benchmarks to real news documents in low-resource language settings using human translated data from the Low Resource Languages for Emergent Incidents (LORELEI) corpus.

---


### 360. [How Much Is an AI Token Worth? Scaling Laws for Wild AI-Generated Web Text](https://arxiv.org/abs/2609.40295)

**<font color=#1a73e8>作者：</font>** Jenna Russell, Ben Glickenhaus, Katherine Thai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Web text makes up the majority of pretraining data and is increasingly AI-generated. After applying FineWeb quality filtering, we find that 27.5% of tokens from June 2026 web data are labeled as AI-generated by Pangram, rising to 31.1% by August. Unlike synthetic data or model-collapse setups, this *wild* AI text comes from many models, is written for human readers, and arrives unlabeled in pretraining corpora. How does AI text in the wild affect language model pretraining? To answer this question, we pretrain 800 language models, varying the ratio of added AI tokens to human tokens, and fit scaling laws to held-out losses on both human and AI-generated text. For data-starved models, adding AI tokens to pretraining data initially lowers loss on human text, but the benefit saturates as more are added and quickly *reverses* into harm. For models trained on high budgets of human text, AI tokens raise loss almost immediately, while the same number of fresh human tokens keeps lowering it. Scaling laws such as Hoffman et al. (2022) fail to predict this behavior. We propose a new scaling law with separate benefit and harm terms that allows the value of an AI token to change sign while also reducing to Chinchilla in the absence of AI text. When fit on smaller models, our scaling law predicts the effect of AI text on held-out human-text loss for models up to 3.6x larger with 41% lower error than the best existing law over all AI ratios. We recommend filtering AI text when the target is human text, repeating human text before expanding the training dataset with AI-generated web text, and reporting validation loss on human and AI text separately AI text remains valuable when the target is AI text. We release WildAI, an 83B-token corpus with AI, topic, and format labels, all 800 models and code at this https URL.

---


### 361. [How Much of a Harness Does a Strong Agent Need for Autonomous ML Engineering?](https://arxiv.org/abs/2609.40303)

**<font color=#1a73e8>作者：</font>** Kirill Brilliantov, Alejandro Hernández-Cano, Emmanuel Abbé  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent autonomous machine learning engineering (MLE) agents have made significant progress on public leaderboards. Often motivated by progress stagnation over long-horizon cycles and limited Large Language Model (LLM) primitives, modern MLE agents are deployed on top of increasingly elaborate machinery: multi-agent orchestrators, dedicated retrieval subagents, and more. While such harnesses expand, the use of more primitive but improved coding agents - where LLMs have direct access to the execution environment through read, write, and bash primitives - has received little attention in the field. In this paper we find that, under an equal time budget and the same frontier LLM backbone, open-source state-of-the-art harnesses provide no advantages over a single session of a minimal-harness coding agent baseline, pointing to the backbone as the primary driver for performance. Via a series of large-scale systematic ablation studies, we argue that the machinery layers become redundant in the coding agent setting. We conclude that the effort spent elaborating hand-crafted harnesses around strong models yields poor returns for current MLE benchmarks.

---


### 362. [Scaling Laws for Looped Mixture of Experts](https://arxiv.org/abs/2609.40316)

**<font color=#1a73e8>作者：</font>** Yanbei Chen, Anirudh Goyal, Raghuraman Krishnamoorthi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped transformers and Mixture-of-Experts (MoE) offer complementary routes to efficient scaling: recurrence increases computational depth at fixed parameters, while MoE sparsity expands total capacity at fixed active compute. Yet existing scaling laws model recurrence or sparsity in isolation. In this work, we introduce Loop Scaling Laws, the first scaling law to jointly model recurrence and sparsity alongside model size and data. At its core is a bounded, sparsity-conditional recurrence mapping that characterizes the effective-parameter gain from looping and how sparsity raises this gain. The laws predict the held-out loss of looped models more accurately than prior alternatives, and recover the standard dense and MoE scaling laws as special cases. Beyond prediction, the fitted laws provide a principled foundation for designing looped MoE models under compute and memory constraints. Downstream evaluations further demonstrate the complementary benefits of the two axes: sparsity delivers ~3x active-parameter efficiency, recurrence yields ~2x total-parameter efficiency on reasoning, and joint scaling further advances the performance frontier. As a practical extension, we show these gains hold at trillion-token scale: at matched training compute, a looped MoE with law-derived recurrence matches a ~2x larger non-looped MoE on the reasoning benchmarks, while enabling test-time scaling through recurrence.

---


### 363. [GLARE: Generating Listening Heads with Appropriate Reactions](https://arxiv.org/abs/2609.40317)

**<font color=#1a73e8>作者：</font>** Zikai Liao, Yumin Suh, Yi Ouyang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While talking head generation has advanced rapidly, generating natural listener behavior in dyadic conversations, which know when to react, how to react, and with what type of response, remains underexplored. Existing dyadic datasets lack fine-grained listener reaction annotations, and prevailing evaluation metrics inherited from talking-head and video generation measure visual realism rather than whether a listener reacted appropriately. We address these gaps along three aspects. First, we curate a listening-head-specific dataset built from RealTalk and Seamless Interaction, comprising approximately 147 hours of paired speaker-listener videos with 64,557 event-level reaction annotations across six categories: nodding, head shaking, smiling, laughing, frowning, and surprised. Second, we introduce an audio-driven baseline built on a flow-matching transformer, namely GLARE, with prosody conditioning derived from Qwen2-Audio and a temporal reaction loss that explicitly supervises frame-wise reactions. Third, we propose a reaction-oriented evaluation protocol that jointly measures reaction occurrence (R-F1), temporal alignment (R-tIoU), asymmetric temporal deviation (R-ATD), and reaction-region visual quality (R-FID), giving a more behaviorally grounded assessment than visual-quality-only metrics. Experiment results show consistent gains over prior listening-head methods in both visual fidelity and reaction-level metrics, suggesting that reaction-aware data, modeling, and evaluation are critical for natural listening behavior.

---


### 364. [MatLoom: Layered Text-to-Material Generation in a Compact Program Space](https://arxiv.org/abs/2609.40322)

**<font color=#1a73e8>作者：</font>** Anson Y. Lam, Shuqing Li, Michael R. Lyu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Material generation should produce not only an appearance, but also the rules that construct it. We introduce MatLoom, a compact, layer-oriented language for text-to-material generation with pretrained language models. Each program composes alpha-masked layers whose shared spatial expressions define coverage and physically based rendering (PBR) channels, making dependencies between patterns, color, and relief explicit. A standalone interpreter evaluates the program into material maps, while the source retains named fields and layer parameters for subsequent authoring. Without task-specific fine-tuning, our pipeline uses parser-guided repair and preview-based critique to revise material designs, then searches noise seeds while keeping each candidate's remaining source fixed. On a curated benchmark of 141 prompts evaluated with six backbones, our best-performing configuration achieves higher mean scores than three diffusion baselines on all four flat-layout prompt-alignment metrics. Its initial programs already exceed all three baselines on mean BLIPScore, before critique or seed search. Retained programs have a median length of 21 lines when pooled across backbones. In a blind four-way comparison involving 30 participants and 20 prompts, our renders receive 59.2% of choices, compared with 19.3% for the most-preferred baseline. Compact executable programs thus offer a way to generate prompt-aligned materials while retaining their construction as part of the asset.

---


### 365. [Cogentic: Multi-Agent Orchestration for Automated Proof Discovery](https://arxiv.org/abs/2609.40324)

**<font color=#1a73e8>作者：</font>** Yang Cai, Vineet Gupta, Yanchen Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present Cogentic, a multi-agent harness for automated proof discovery on open research problems. While frontier language models can generate strong mathematical ideas in a single shot, single-shot generation is often insufficient for open problems that require exploring multiple competing conjectures, overcoming subtle technical obstructions, and retaining intermediate progress over a long horizon. Cogentic addresses these challenges through an iterative prove--verify loop in which an orchestrator allocates a population of independent provers across distinct proof directions, subjects their output to adversarial verification by several specialized components, and promotes confirmed intermediate results into a persistent verified ledger that later rounds build on. The harness is designed to be able to solve research-level math and theoretical computer science problems. Using Gemini as the base model, Cogentic produced novel results on five open problems across online learning, auction theory, and mechanism design. Each result was independently verified by domain experts and is developed in full in companion papers. We list these results, and new ones as they are verified, at this https URL .

---


### 366. [WorldAuditBench: Interactive 3D World Auditing with Multimodal Agents](https://arxiv.org/abs/2609.40325)

**<font color=#1a73e8>作者：</font>** Ziyan Jiang, Jingbo Yang, Jiabao Ji 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As interactive 3D worlds are increasingly used to study intelligent behavior, it becomes important to develop efficient pipelines for identifying anomalies in these simulated environments, such as floating objects, traversable walls, or objects inconsistent with the surrounding scene. Multimodal AI systems, including vision-language models (VLMs) and vision-language-action models (VLAs), have shown potential for automating this task. However, 3D world auditing is complex, requiring the close coupling of two distinct capabilities: action, to navigate the 3D world and search for anomalies systematically and efficiently; and visual reasoning, to understand the environment and identify anomalies from multimodal observations. It remains largely unexplored whether multimodal agents can effectively couple these two capabilities, using visual reasoning to identify potential anomalies while taking actions to validate them. In this paper, we introduce WorldAuditBench, a benchmark for 3D world auditing comprising 213 anomaly tasks across 13 environments built with Unreal Engine 5 and this http URL, spanning five anomaly families. We evaluate five frontier models under a fixed exploration budget using two auditing paradigms: VLA-based exploration followed by VLM-based anomaly identification, and an end-to-end VLM agent in which visual reasoning directly guides action selection. Across the evaluated models and two paradigms, success rates range from 6.6% to 42.3%, substantially below human performance (83.4%). Through the task of world auditing, WorldAuditBench provides a testbed for studying how multimodal agents couple action and visual reasoning in interactive 3D environments, while highlighting current limitations in their ability to gather and interpret evidence during exploration.

---


### 367. [Is Weight Tying Still Beneficial for Decoder-Only LLMs in Private Settings Under DP-SGD?](https://arxiv.org/abs/2609.40335)

**<font color=#1a73e8>作者：</font>** Razan El Mais, Ali Chehab, Ibrahim Issa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differentially Private Stochastic Gradient Descent (DP-SGD) is a leading approach for privacy-preserving fine-tuning of large language models (LLMs). Many decoder-only LLMs employ weight tying between input and output embeddings, a design choice originally introduced for parameter efficiency and improved language modeling performance in the non-private setting. However, the impact of weight tying under differentially private training remains largely unexplored. In this work, we investigate the role of weight tying in the DP setting using GPT2 and DistilGPT2 as representative decoder-only architectures. Interestingly, we find that untied embeddings consistently outperform weight-tied models under DP-SGD, achieving gains of up to 4.74% points in accuracy on SST-2, QNLI, and QQP. Beyond improved utility, untying embeddings enables the use of memory-efficient ghost clipping for DP-SGD. By contrast, weight tying introduces shared-parameter interactions that complicate standard ghost norm computation and largely negate its computational advantages. As a result, untied models achieve over 60% lower memory usage while preserving the benefits of ghost clipping. Our results indicate that untied embeddings provide a more effective and scalable design for differentially private training of decoder-only LLMs and highlight the need to revisit standard LLM architectural choices in the privacy-preserving setting.

---


### 368. [EvoDuet: Bilevel Co-Evolution of Web Searching and Task Solving for Scientific Discovery](https://arxiv.org/abs/2609.40340)

**<font color=#1a73e8>作者：</font>** Young-Jun Lee, Jinheon Baek, Soyeong Jeong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evolutionary search with large language models (LLMs) can stall when progress requires external knowledge the model lacks. Supplying relevant documents helps, but simply adding web search tool can keep returning the same pages as solutions change. We introduce EvoDuet, a bi-level optimization method that co-evolves solutions and search queries with fixed model parameters. At each iteration, a retrieval gate lets the LLM assess its knowledge gap and choose to retrieve new documents, reuse stored ones, or proceed without them. An inner loop refines queries and ranks documents by the solution scores they are predicted to yield; an outer loop generates candidates in parallel from these documents and records the evaluated outcomes for later searches. Across 21 optimization tasks with one candidate per iteration, EvoDuet raises OpenEvolve's normalized discovery gain from 74.1% to 78.0% with GPT-5.6-Luna and from 61.3% to 82.3% with Gemini-3.8-Flash, whereas Qwen3.5-9B does not benefit. Our best runs surpass the previously reported best scores on eight tasks, including Swap Reduction on Q20 and Rosetta, and match them on three more. EvoDuet also improves with other scaffolds (e.g., Top-K, EvoX) on Sums/Diffs and Denoising, demonstrating its applicability across evolutionary search scaffolds.

---


### 369. [Removing Timing Shortcuts Improves Non-Invasive Brain-to-Text](https://arxiv.org/abs/2609.40359)

**<font color=#1a73e8>作者：</font>** Dulhan Jayalath, Oiwi Parker Jones  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We find that major reported improvements in decoding words from non-invasive brain recordings are largely reproducible without any brain data. In the influential work of d'Ascoli et al. (2025), time series of brain activity from subjects perceiving continuous speech are segmented into fixed-length windows starting at each word. A neural network then generates predictions for all of the words in a sentence together. Neighbouring windows partially overlap, implicitly revealing the interval between words. Since these intervals indicate the duration of the words spoken, and different words tend to have different durations - for example, "the" is much shorter than "supercalifragilisticexpialidocious" - the neural network can improve its predictions of words without relying on the underlying brain activity. Consistent with this, the method reaches 22.0% balanced accuracy on synthetic signals containing no brain information, compared with 22.3% on real brain recordings. To prevent the network from learning this shortcut, we make a single, simple change. Instead of jointly encoding all windows in a sentence, we process each independently. As a result, the neural network achieves better performance by learning underlying word-specific information from brain recordings. This makes two existing strategies become much more effective than before. Both aggregating predictions from distinct neural responses to the same word and using a pretrained LLM as a linguistic prior now substantially improve results. On our perceived speech benchmark, this simple recipe (SimpleB2T) achieves a word error rate of 36.6% with five observations per word, approaching past invasive speech decoding performance, albeit under different conditions. The results in this work expose an important shortcut in brain-to-text decoding and show that removing it leads to a simple and considerably more effective strategy.

---


### 370. [Semifactual Credit-Augmented Policy Optimization](https://arxiv.org/abs/2609.40360)

**<font color=#1a73e8>作者：</font>** Junshu Pan, Zhizhang Fu, Shulin Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has improved the reasoning capabilities of large language models (LLMs), yet their predictions remain sensitive to task-irrelevant prompt features. We investigate this sensitivity through semifactual prompt interventions that preserve the underlying problem and its answer. Our analysis reveals substantial variation in token-level sensitivity and shows that suppressing high-drift token candidates during decoding improves reasoning accuracy without updating model weights. These findings highlight a limitation of Group Relative Policy Optimization (GRPO), which assigns the same outcome-derived advantage to every response token and may reinforce potential spurious dependence alongside useful reasoning. Motivated by this observation, we introduce Semifactual Credit-Augmented Policy Optimization (SCAPO), a causally inspired variant of GRPO that incorporates semifactual stability into token-level credit assignment. SCAPO measures token probability drift for fixed responses under semifactual interventions and uses normalized stability scores to reduce advantages for relatively unstable tokens during early training, while granting no additional credit for stability alone. On Qwen3-4B-Base and Qwen3-1.7B-Base, SCAPO improves AIME 2024-2026 accuracy over GRPO by 5.63 and 4.17 percentage points, respectively. At both model scales, SCAPO achieves the best results on most evaluated mathematics benchmarks and all evaluated out-of-distribution benchmarks among the compared methods. These results suggest that semifactual stability provides an effective training signal for improving reasoning and generalization through finer-grained credit assignment in RLVR. The code is available at this https URL.

---


### 371. [Ranking-Aware Prompt Optimization for Multimodal Clinical Diagnosis](https://arxiv.org/abs/2609.40361)

**<font color=#1a73e8>作者：</font>** Tian Xia, Minghao Liu, Yiqing Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) are rapidly advancing clinical diagnosis, yet their adaptation pipelines remain anchored to accuracy-based objectives. Clinical data are heavily class-imbalanced: a constant-majority predictor can score above 90% accuracy while being clinically useless. We therefore evaluate and optimize for AUROC, a threshold-free score that ranks positives above negatives and is invariant to class balance. We focus on prompt optimization in MLLMs. Reflective methods such as GEPA use a binary scores matrix with one row per evaluation instance and one column per candidate prompt; cells record per-instance correctness, so the column average is accuracy and drives candidate selection. We introduce pair-level Pareto prompt evolution (Ranking-PE), which replaces each correctness row with a pairwise-ordering row over (positive, negative) instance pairs: the cell is 1 if the candidate scores the positive higher than the paired negative. The column average then equals empirical AUROC (by the Wilcoxon-Mann-Whitney identity). We apply this swap at all three layers the prompt evolution search reads from - the scores matrix that decides Pareto dominance, the per-example feedback to the reflection LM, and final candidate selection - at no extra model calls and with no surrogate loss. Across three diseases on MIMIC, accuracy-based prompt evolution can degrade ranking; Ranking-PE reverses this, beating the accuracy-based recipe by +5.8 AUROC pp on fine-tuned Qwen3-VL-8B and +16.2 pp on MedGemma-4B. Ablations examine each design component and show that a medical-grade visual backbone - via vision-encoder-tuned SFT or medical pretraining - is a prerequisite that prompt search cannot replace - our recipe extends reflective prompt evolution from text-only data to multimodal clinical decision-making.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 372. [CollageAttack: Exploiting Cross-Modal Alignment Flaws in T2I Models through Spatial Text Composition](https://arxiv.org/abs/2609.38253)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhiyi Mou, Yao Lu, Wangze Ni 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Text-to-image (T2I) models have substantially improved in language understanding, in-image text rendering, and visual composition, while their safety mechanisms do not always keep pace with these capabilities. This creates a cross-modal attack surface in which harmful semantics can remain inconspicuous in a serialized prompt yet emerge through image-level composition. We propose CollageAttack, an automated single-prompt black-box jailbreak that shifts semantic assembly into the image plane by combining context-relevant scenes, scene-grounded textual carriers, and spatially distributed text fragments. Experiments across multiple open-weight and commercial T2I models show that CollageAttack achieves attack success rates of up to 86.0%, outperforming the strongest baseline on the same model by 18.5 percentage points, while consistently producing more harmful outputs and preserving the source intent. We further find that distributed textual fragments can reconstruct the intended semantics after generation, with visual composition producing stronger communicative impact than text alone. These results reveal a cross-modal safety gap in which harmful meaning emerges from the composition of individually less explicit elements.

---


### 373. [The Geometry of Harmfulness in Multi-Turn Attacks](https://arxiv.org/abs/2609.38389)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yelyzaveta, Husieva, Lauren Alvarez  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) remain vulnerable to adversarial attacks that circumvent safety alignment to elicit harmful outputs. It remains unclear how harmfulness and refusal representations evolve over the course of multi-turn attacks, and why single-turn defenses are less effective in multi-turn settings. This work investigates how the geometry and temporal dynamics of harmfulness and refusal representations evolve across multi-turn attacks. We analyzed hidden-state representations from three instruction-tuned LLMs (Llama-3.1-8B-Instruct, Qwen2.5-7B-Instruct, and Gemma-2-9B-it) using three multi-turn attack frameworks (Crescendo, ActorAttack, and X-Teaming), and examined representation behavior across conversation turns, model layers, and token positions under various context configurations. Across models and frameworks, we found that (1) each attack framework traverses different geometric directions, yet each achieves comparable success in eliciting harmful outputs; (2) multi-turn harmfulness directions became increasingly linearly separable at the end-of-turn token position across turns in middle to late model layers; and (3) harmfulness representations are weakly aligned with refusal-related representations. The results indicate that multi-turn attacks do not succeed by suppressing the model's internal representation of harmfulness. Instead, harmfulness representations become increasingly separable across conversation turns, while remaining only weakly aligned with refusal-related representations. The findings are one possible explanation for why static single-turn safety probes may degrade in multi-turn settings, and suggest that robust defenses must consider temporal representation dynamics rather than identifying harmfulness with isolated or single-turn prompts.

---


### 374. [NeurDuo-EEG: A Long-Sequence EEG Foundation Model with Persistent State and Explicit Memory](https://arxiv.org/abs/2609.38587)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yifan Wang, Haiping Liu, Yang Cui 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) is recorded continuously over hours, with relevant dynamics spanning timescales from milliseconds to hours. Most EEG foundation models nevertheless process fixed windows independently, limiting their ability to capture information encoded in long-timescale dynamics. State-space architectures enable persistent recurrent processing, but long-range information remains implicitly compressed in recurrent states. We present NeurDuo-EEG, a causal EEG foundation model with channel-resolved persistent memory. NeurDuo-EEG introduces multi-timescale memory management with learned consolidation and selective retrieval, enabling persistent modelling of continuous EEG with fixed-size state. It is pre-trained on 3,955 hours of EEG from 17 public datasets using multichannel autoregressive prediction of discrete spectral codes. Across three short-window and two long-sequence downstream tasks, NeurDuo-EEG achieves the best performance on four of five benchmarks, including all three short-window tasks and seizure detection, where AUC-PR improves from $0.285$ to $0.471$ over the strongest non-NeurDuo baseline. NeurDuo-EEG also remains competitive on sleep staging and supports efficient streaming inference, with nearly constant per-chunk latency as the available history grows to one hour. Notably, the Small variant achieves this with only 4.7M backbone parameters. These results demonstrate the value of persistent, multi-timescale modelling for both long-sequence and short-window EEG analysis. Our code is available at this https URL.

---


### 375. [After a Decade: Bringing Shadow Removal into the Real World with Agentic Training Data](https://arxiv.org/abs/2609.38607)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shilin Hu, Jingyi Xu, Dimitris Samaras 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Shadow removal looks nearly solved on established benchmarks, yet remains brittle in the real world. Models have advanced; the paired training data they rely on have barely changed in nearly a decade. The reason is simple: obtaining a shadow-free target requires removing the occluder while keeping the scene, camera, and illumination otherwise unchanged, making diverse paired data difficult to capture. Meanwhile, large shadow detection datasets already contain diverse real-world images and masks, but no shadow-free targets. To turn this abundant but incomplete data into paired supervision, we propose an offline agentic workflow combining physics-motivated generation, failure detection, feedback-driven retry, candidate selection, and deterministic correction. Using this workflow, we construct AgenticShadow, a dataset of 17,138 image-mask-target triplets spanning general scenes, faces, and remote sensing. Our construction workflow reduces Color Distribution Difference by 50.5% over previous shadow removal work, while training existing shadow removal models on AgenticShadow reduces cross-domain LAB RMSE by 19.7-37.5%.

---


### 376. [Alignment via Training Against Probes Without Losing Monitorability](https://arxiv.org/abs/2609.38645)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Lena Libon, Alexander Panfilov, Ben Rank 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Models are usually aligned based on their observed outputs, using demonstrations, preference data, or reward signals. These objectives reward responses that look aligned. More capable models may learn to satisfy them without internalizing the intended behavior, for example by faking compliance during training. Such superficial compliance could be harder when the objective is defined on model internals rather than outputs. Therefore, we study probe-guided fine-tuning, using probes that detect undesired properties in model activations as a direct training signal. We evaluate linear and non-linear probes with different numbers of probes per layer across two alignment objectives: harmlessness and honesty. We find that training against probes that do not update during training is an easily exploitable objective, while continuously updated probes substantially reduce harmfulness and improve honesty while preserving utility. Probe-guided fine-tuning achieves better safety-utility trade-offs than DPO and inference-time steering, while being substantially more robust against jailbreak and abliteration attacks. Moreover, the concepts stay linearly encoded after fine-tuning, meaning oversight is not lost by our method. Training against probes thus offers a way to shape what models represent rather than only what they output, which may become increasingly important as models get better at making their outputs look aligned.

---


### 377. [Staying on Task: Testing the Foundations of Long-Horizon Agent Reliability](https://arxiv.org/abs/2609.38712)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jeffrey Willette, Krishna C. Puvvada, Boris Ginsburg  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon agentic workflows require models to sustain repeated state-dependent actions all while the context grows, sub-task complexity changes, and new data arrives. Each situation represents an independent axis along which an agent may fail. An agent reconciling a long ledger, for example, must repeatedly read its state, update the correct record, and preserve alignment across thousands of outputs. A model may accept the entire ledger yet lose its place or stop applying the operation consistently as generation proceeds. We introduce Long-Transduction, a controlled diagnostic that tests a model's ability to stay on task during long generation while continuously reading, mutating, and outputting input-context dependent operations such as arithmetic, sorting, variable lookups, and table transformations. Long-Transduction evaluation independently varies local task complexity, input data formatting, and context length isolate failures along each axis. We evaluate seven open-weight models, finding a 62.8\% decrease when scaling context length from 4-128K, a 36.5\% decrease when varying input format, and a 39.9\% decrease by increasing local task complexity. Together, these failures represent critical liabilities in long-horizon agentic workflows.

---


### 378. [Molecular Property Prediction under Structural Shift with Tabular Foundation Models](https://arxiv.org/abs/2609.38744)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jinmo Lee, Dooho Lee, Minho Jeong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting molecular properties for compounds that differ structurally from labeled training molecules is important for drug discovery and materials design. Tabular foundation models (TFMs) offer a promising approach through in-context learning, but their performance under structural shifts and the value of molecular comparisons in this setting remain underexplored. We study structural generalization in molecular property prediction and introduce MolPAIR (Molecular Pair-Augmented In-context Refinement), a framework that combines molecule-level and molecular-pair contexts without task-specific parameter updates. A global tabular foundation model (TFM) first predicts a query's property from labeled molecular examples. A second frozen TFM predicts differences in prediction errors between the query and labeled reference molecules, using these comparisons to refine the initial prediction. Across 58 MoleculeACE and Polaris tasks, CheMeleon representations combined with TabPFN-3 already outperform each evaluated baseline on a majority of tasks. MOLPAIR further improves this predictor on 46 of 58 tasks, with gains across four molecular representations and three TFM backbones. These results show that explicit molecular comparisons can strengthen tabular in-context learning for structural generalization while keeping the molecular encoder and pretrained model weights fixed. The code and datasets are available at this https URL.

---


### 379. [When Reasoning Goes Astray: Attention Dynamics of Uncontrolled Reasoning](https://arxiv.org/abs/2609.38817)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuanhe Zhang, Ziwei Wang, Jie Ren 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large reasoning models (LRMs) improve performance on complex tasks through extended reasoning, yet the same process can degenerate into redundant verification and persistent generation loops. Such uncontrolled reasoning increases inference cost and creates risks of resource exhaustion and service degradation. However, existing mitigations largely truncate long outputs or react to surface repetition, and thus fail to distinguish normal thinking from uncontrolled reasoning or explain how benign reasoning degenerates into harmful behavior. In this paper, we operationalize LRM generation as four states and further introduce Reasoning-state Analysis via Dynamic Attention Responses (RADAR), which identifies the current reasoning state in real time and characterizes how effective reflection can develop into uncontrolled generation. Guided by RADAR's analysis, we further realign abnormal attention distributions toward patterns observed in normal requests and examine how this correction affects excessive reflection and persistent looping. Temporal analyses show that uncontrolled reasoning is characterized by attention distributions that deviate from normal generation, with abnormal trends becoming detectable before repetition begins. Correcting these deviations through Attention Realignment consistently reduces looping while largely preserving benign performance. Together, RADAR provide a mechanistic account of how reasoning becomes uncontrolled, offering actionable guidance for identifying critical failure stages and designing targeted runtime interventions.

---


### 380. [Mitigating the Length-Scaling Tax with Online Distillation](https://arxiv.org/abs/2609.38854)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xu Wan, Wenyue Xu, Shengjie Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Length scaling during reinforcement-learning (RL) post-training is often viewed as a sign of improved reasoning ability, especially on difficult problems, but may also make responses to already-solved problems unnecessarily verbose. We quantify this side effect as the length-scaling tax (LST): excess response length on already-solved queries without a commensurate accuracy gain. To mitigate LST, we propose Length Self-Distillation (LSD), which routes solved prompts to on-policy distillation and retains the original RL objective for unsolved prompts. LSD uses an exponential moving average of the online policy as its teacher, requiring no external model. We find that LSD achieves comparable or better performance than RL across multiple variants, while substantially curbing response-length growth on easy queries. LSD reduces LST from 19.0% to -3.7% on single-turn reasoning and from 31.4% to 13.7% on multi-turn agentic tasks, demonstrating that LSD effectively preserves concise response patterns on easy queries while supporting efficient exploration on difficult queries during RL post-training.

---


### 381. [Unmerge: Efficient Machine Unlearning via Task Arithmetic](https://arxiv.org/abs/2609.38895)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Haoran Tang, Andrew Tan, Rajiv Khanna  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Approximate machine unlearning seeks to remove the influence of a forget set from a trained model without full retraining. Existing gradient-based methods require data-dependent hyperparameter search, struggle when forget and retain knowledge are entangled, and offer little insight into where unlearning actually happens inside the network. We recast unlearning through the lens of task arithmetic: if finetuning produces a merged task vector $\tau_m$ that combines learning on forget and retain sets, unlearning is the inverse operation that subtracts a learned forget component $\tau_F$ to recover the retain task vector $\tau_R$. The forget signal is concentrated: at every layer, forget activations lie in a subspace spanned by a handful of dominant directions, so we factorize $\tau_F$ in a low-rank forget basis, which is faithful up to a small tail-eigenvalue residual and limits how far the correction can perturb retain. We then optimize three intuitive goals (match the merged vector inside the forget span, suppress leakage into the retain span, and bound the correction size) that provably bound forget leakage and retain damage in activation space. The resulting algorithm, Unmerge, is fast and powerful: on class-level unlearning with ResNet-50 on CIFAR-100 and Tiny ImageNet, it improves Tug-of-War by up to ~24% over a baseline of comparable runtime and by up to ~18% over stronger baselines that run ~5x slower, keeps membership-inference exposure at the level of retraining, and shrinks the feature-distribution gap to the retrained model, where relabeling methods leave forget features cleanly separable. Further studies show that Unmerge also applies to ViT-S/16 and scales to Llama-3.2-3B. The per-layer basis geometry that drives the algorithm also serves as a layerwise diagnostic for when and where unlearning becomes structurally hard.

---


### 382. [Robust Risk-Sensitive Reinforcement Learning from Corrupted Human Feedback](https://arxiv.org/abs/2609.38938)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xinyi Ni, Lifeng Lai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with human feedback (RLHF) learns from human comparisons, which can be corrupted or deliberately manipulated. This paper studies online risk-sensitive RLHF with static conditional value-at-risk (CVaR) under adversarial preference-label flips. We consider additive linear rewards and a fixed-reference protocol with one comparison per episode and at most $C$ flipped labels over $K$ episodes. We propose weighted streamed-preference CVaR RLHF (WSP-CVaR-RLHF), which combines uncertainty-weighted reward estimation with optimistic augmented-state CVaR planning. For known transitions and normalized rewards, we establish the regret bound $\widetilde{O}\left(\frac{d}{\kappa}\sqrt{\frac{K}{\alpha}}+\frac{dC}{\kappa\alpha}\right)$ up to lower-order terms, where $d$ is the reward-feature dimension, $\alpha$ is the CVaR level, and $\kappa$ characterizes the preference link. The bound separates the clean statistical cost from the penalty caused by corrupted feedback. We further extend the analysis to unknown tabular transitions, where the trajectory distribution entering the CVaR objective must be learned together with the reward. We address the resulting coupled uncertainty using rectangular transition confidence sets, joint optimistic planning, and a history-level CVaR simulation argument. Experiments under four adversarial attacks demonstrate that WSP-CVaR-RLHF consistently reduces cumulative regret relative to its unweighted robust counterpart while preserving confidence-set coverage.

---


### 383. [T-Router: Learning Thalamic Routing for Reasoning with Parameter-Efficient Reinforcement Learning](https://arxiv.org/abs/2609.39109)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Liuxian Ma, Jiale Dai, Jiaqi Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient reinforcement learning aims to improve reasoning with a compact trainable interface to a pretrained model. We introduce the Thalamic Router (T-Router), which concentrates adaptation on the reuse of completed computations. A compressed, addressable bank preserves block changes; a depth-recurrent controller conditions their selection and relative-scale writeback. This coupling gives thalamic context-dependent routing a concrete computational form: learn which earlier contributions a receiving layer uses, and with what influence. Correctness rewards train the interface while preserving backbone parameters and layer order. On an 8.95B-parameter backbone, T-Router allocates 41.73M parameters (0.466% of the backbone) and achieves 83.64 +/- 1.16 MathAvg after GSM8K RL, compared with 73.79 +/- 1.83 for full-parameter GRPO across three evaluation rounds. At a comparable parameter budget and with matched retries, it exceeds LoRA's 77.28 +/- 1.95 MathAvg, improving all three task families and raising mean AIME accuracy from 48.33 to 60.56. Capacity-controlled comparisons favor addressable block changes and recurrent context; separate search training extends the interface to tool-mediated reasoning. These results establish controlled computation reuse as an effective route to parameter-efficient reasoning reinforcement learning.

---


### 384. [Autoresearch in Mixed-Integer Linear and Nonlinear Programming](https://arxiv.org/abs/2609.39360)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuwei Gu, Yaoxin Wu, Tong Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite recent progress in autoresearch, applying it to practical operations research problems, typically formulated as NP-hard mixed-integer linear or nonlinear programs (MILPs or MINLPs), remains challenging because effective research requires systematically managing competing ideas and long-horizon experimental trajectories. We introduce AutoMIP, a reusable agent skill for organizing long-horizon autoresearch in mixed-integer programming through idea pooling and algorithm tree search. AutoMIP maintains a persistent pool of complementary candidate ideas while organizing executable experiments into an algorithm tree, enabling the agent to preserve unexplored hypotheses, refine promising algorithms, and switch to alternative methodological directions based on historical states. On MILP and MINLP benchmark cohorts, AutoMIP achieves the highest final success rates among the evaluated autoresearch frameworks. On MIPLib, AutoMIP discovers new best solutions for 31 of 60 instances, surpassing existing autoresearch frameworks. On MINLPLib, it achieves new best solutions for 52 of 60 instances. Ablation studies further demonstrate the complementary contributions of idea pooling and algorithm tree search, highlighting the importance of jointly maintaining diverse research ideas and structured experimental trajectories for long-horizon autoresearch.

---


### 385. [When, Not How Much: Evaluating Time-Series Foundation Models on Sparse Events](https://arxiv.org/abs/2609.39386)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Daniel Schoess, Florian von Wangenheim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretrained time-series foundation models (TSFMs) are evaluated as forecasters of future values, yet for sparse series many decisions depend only on which future periods contain activity. Standard benchmarks do not assess this. On five sparse datasets, we rank positions within forecast windows that contain both events and zeros. The released point forecasts of 12 TSFMs improve chance-corrected average precision over training-free references by at most 0.031, and in chance-corrected AUC the median TSFM falls below them on every dataset. With event supervision, linear probes of six frozen backbones improve on their backbone's point forecast in 29 of 30 backbone--dataset pairs. Averaging the predicted quantiles instead of taking their median improves the ranking of most TSFMs that forecast the median, and on two datasets the strongest such outputs rival the probes. The probes' advantage over raw-context learners depends on the dataset, and under the same probe, pretrained features outperform randomly initialized ones for five of six backbones. For sparse-event ranking, released point forecasts thus add little over simple references, whereas lightweight event heads on frozen TSFMs rank events better than these forecasts, and the best of them exceed gradient-boosted trees trained on the raw context on three of the five datasets. More broadly, assessing pretrained forecasters on tasks beyond value forecasting requires reporting their outputs, supervised probes of their representations, and raw-context and randomized controls side by side, since each supports a different conclusion.

---


### 386. [CIDER-FM: Foundation Models for Causal Inference from Diverse Experimental Regimes](https://arxiv.org/abs/2609.39523)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuche Gao, Arik Reuter, Siyuan Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal foundation models (CFMs) amortise causal inference over priors of synthetic structural causal models (SCMs), predicting the effect of an experiment on a specific variable. However, observational data alone may leave multiple causal models compatible with available evidence, while experimental data with interventions on exactly the variable of interest might be unavailable. This work studies CFMs as a method to combine finite observational and surrogate-interventional datasets in order to predict a target conditional interventional distribution (CID) more accurately than with observational data alone. We first formalise the conceptual benefits of surrogate experiments. Building on this analysis, we introduce \textsc{Foundation Models for Causal Inference from Diverse Experimental Regimes} (\emph{CIDER-FM}), a causal foundation model that uses an intervention-aware representation and hierarchical three-axis attention to exchange information across variables, samples, and experimental regimes. We evaluate CIDER-FM against a wide range of baselines across diverse synthetic graph and mechanism families, as well as on both simulated and real-world data from Causal Chambers. Our results demonstrate strong CID prediction performance and show that incorporating experimental context can improve predictions over observational data alone.

---


### 387. [Free Everywhere, Exact on Trees: PPO's Dropped Correction Buys Sample Efficiency Under Aggressive Reuse](https://arxiv.org/abs/2609.39634)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Nima H. Siboni  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Common policy improvement methods, including TRPO, PPO, and GRPO, estimate policy improvement under the behavioral policy's state-visitation distribution rather than the improved policy's own. The substitution makes the objective estimable from the behavioral policy's rollouts but adds a bias growing with policy divergence, hence the trust region or clip, and hence no reuse of a batch far off-policy. We show that under history-injective dynamics, where each state is reached by exactly one history, the dropped state-visitation ratio equals the product of per-step policy ratios along the sampled prefix, on every trajectory and not only in expectation. The ratio is therefore restored exactly, from log-probabilities PPO already computes. Autoregressive generation and canonical-order constructive optimization are both history-injective. The exact correction pays importance-sampling variance that grows with the horizon, so we generalize it to a one-parameter family with PPO ($\alpha{=}0$) and the full correction ($\alpha{=}1$) as endpoints: a single bias--variance knob. A gradient-level analysis of the unclipped surrogate identifies two channels the correction acts through and three conditions under which it carries signal; an enumerable testbed confirms the conditions' predictions. On hard credit-assignment scheduling tasks, a short corrected warmup with aggressive early sample reuse learns faster than PPO and than the same reuse uncorrected; the marginal gain grows with task difficulty ($+0.02$ to $+0.09$ learning-curve AUC), and the early win over PPO tracks the prefix bias that reuse incurs. A correction held throughout, or applied where clipping already contains the reuse bias, is null to harmful.

---


### 388. [BAM! Bayesian Anything Model: a foundation model for generative computational imaging](https://arxiv.org/abs/2609.39660)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Alessio Spagnoletti, Charlesquin Kemajou Mbakam, Jonathan Spence 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative models are transforming Bayesian computational imaging, yet the field still lacks physics-aware foundation models. Current practice falls into two camps. Large foundation image models are deployed as plug-and-play priors with zero-shot approximate likelihood guidance, which introduces significant bias and computational cost. Physics-aware generative models avoid this bias, but each is tied to a specific dataset, task and instrument. We introduce BAM (Bayesian Anything Model), a lightweight foundation model for few-step, physics-aware posterior sampling that generalises robustly to unseen data and tasks, zero-shot or with minimal finetuning. BAM upgrades the operator-conditioned Reconstruct Anything Model (RAM) backbone (Terris et al.) into a conditional flow map, so instrument physics is specified at inference time rather than fixed during training. BAM has just 36M parameters and is pre-trained jointly on large image corpora and libraries of forward operators. A single network then draws posterior samples in a few steps, with no likelihood approximation and no guidance weights to tune. Across linear inverse problems on FFHQ, AFHQ, LSUN, DIV2K and the Kohler camera-shake benchmark, BAM outperforms in just 3 steps both specialised models and leading zero-shot methods in sample quality, at a fraction of their computational cost. BAM gives the community an accessible entry point to generative computational imaging, lowers the economic and environmental cost of training imaging models, and opens a new path for research on physics-aware Bayesian computational imaging. Official page: this https URL

---


### 389. [NodeGround: A Node Classification Benchmark in the Graph Foundation Model Era](https://arxiv.org/abs/2609.39673)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jinmo Lee, Dooho Lee, Minho Jeong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can a pretrained graph model replace training and tuning a separate predictor for each dataset? Answering this requires evaluating prediction quality alongside computational cost. We present NodeGround, a node classification benchmark that puts graph foundation models (GFMs) and dataset-specific supervised learning under a common evaluation framework. The benchmark spans 51 datasets and evaluates six GFMs alongside 15 supervised methods under two label-availability regimes. Shared data partitions, validation-only model selection, controlled hyperparameter searches, and multiple predictive metrics make comparisons systematic, while workflow measurements account for adaptation, training, tuning, and inference. The results favor carefully tuned graph neural networks overall. GraphPFN reaches third place by Elo when more labels are available, yet its relative strengths vary substantially with dataset properties. Efficiency comparisons further qualify the benefits of pretrained reuse: GVT and GraphPFN appear on the Pareto frontiers when supervised methods are represented by their default and fully tuned configurations. Adding intermediate tuning budgets removes this advantage for GVT and leaves GraphPFN extending the estimated frontier in the label-rich setting alone. Thus, reusing pretrained parameters does not yet provide a broadly reliable route to either stronger predictions or cheaper workflows. We release the evaluation pipeline, run-level records, and an open leaderboard at this https URL.

---


### 390. [AIMS: An Agentic AI Framework for Sim-to-Real Multi-Modal ISAC](https://arxiv.org/abs/2609.39964)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yijie Bian, Kai Zhang, Wei Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-modal integrated sensing and communication (ISAC) enables environmental perception and reliable connectivity for intelligent wireless networks. Data-driven multi-modal ISAC models depend heavily on annotated real-world data to learn relationships across sensing and wireless observations, thereby constraining scalable deployment. Although synthetic data generation reduces the burden, adapting existing simulation pipelines to a target deployment requires consistent scene, sensing, wireless, and learning configurations, while mismatches among these coupled components impair sim-to-real transferability. To address the challenge, we propose an agentic artificial intelligence (AI) framework for sim-to-real multi-modal ISAC, named AIMS. Given a natural-language deployment request specifying the target task, deployment conditions, and real-data budget, AIMS derives a deployment-specific sim-to-real configuration and coordinates its execution to produce a deployment-specific task model. A two-agent architecture coordinates scene construction with task learning. A scene construction agent generates geographically grounded, synchronized sensing and wireless records from shared physical states, while a scene understanding agent configures task-relevant modalities and mixture-of-experts (MoE) learning for zero-shot inference or few-shot adaptation. Structured domain knowledge guides dependency-aware planning, while validation evidence supports feedback-driven revision of affected decisions. Experiments on the real-world DeepSense~6G dataset demonstrate improved vehicle detection and beam prediction over the considered simulation and fusion baselines. A separate orchestration benchmark evaluates task interpretation, dependency reasoning, and feedback-driven replanning across diverse deployment requests, showing improved plan correctness with structured domain knowledge and validation feedback.

---


> [!TIP]
> 当前位于：**351-390**（第 8/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-390**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
