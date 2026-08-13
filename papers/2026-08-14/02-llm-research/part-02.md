# 🧠 大模型相关研究 | 2026年08月14日

> 本类共 **164** 篇论文：已确认 **147** 篇，待复核 **17** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-164](./part-04.md)

---

### 51. [From Prompting to Behavioral Alignment: Personalized LLM Judges for Recommendation Evaluation](https://arxiv.org/abs/2608.11493)

**<font color=#1a73e8>作者：</font>** Alireza S. Ziabari, Kat Ellis, Colleen Chan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traditional offline recommendation evaluation relies heavily on complex, manually maintained feature pipelines that are difficult to scale. While Large Language Models (LLMs) offer a promising alternative by predicting user engagement directly from raw text logs, empirical analysis in this study identifies a critical failure mode termed bidirectional rationalization. In a zero-shot setting, LLMs are found to convincingly argue for both positive and negative user engagement outcomes on the exact same item with identical evidence, highlighting the unreliability of off-the-shelf LLMs in predicting user engagement. To resolve this, we develop and apply a sequential behavioral alignment framework pairing fine-tuning with preference optimization over paired correct and counterfactual rationales. Evaluated on real-world homepage interaction logs, this aligned reasoning approach achieves a 32.19\% lift in Macro-F1 score over the zero-shot baseline and matches the production feature-engineered baseline. The results demonstrate that behavioral alignment mitigates bidirectional rationalization while delivering human-interpretable reasoning traces without manual pipeline overhead.

---


### 52. [Group Alignment-Induced Sycophancy: A Two-Sided Evaluation of Steerable Pluralistic Alignment](https://arxiv.org/abs/2608.11528)

**<font color=#1a73e8>作者：</font>** Haokai Zhao, Yunze Xiao, Weihao Xuan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Group alignment adapts a language model to a demographic group to produce responses that reflect the group's opinions, values, and preferences. Sycophancy, a well-documented by-product of alignment, causes the model to over-agree with the user regardless of factual and objective information. However, existing group alignment methods and evaluations focus only on how closely the model matches the group's opinions, overlooking the induced change in sycophantic behaviour. To bridge this gap, we introduce \textbf{G}roup \textbf{A}lignment-induced \textbf{S}ycophancy (GAS) and systematically evaluate alignment across 3 methods, 4 models and 13 demographic groups, on both the intended gain in opinion alignment and the unintended shift in sycophancy. We find that gain and shift are non-uniform across groups: under an identical budget, some groups receive larger gains in opinion alignment than others, and the induced sycophancy shift forms a group-specific profile rather than a single-dimensional change. These results suggest that group alignment should be reported as a two-sided, multi-dimensional profile rather than a single fit score that accounts for per-group differences when adapting LLMs to diverse populations.

---


### 53. [CT-$Δ$Bench: A Benchmark for Longitudinal 3D Medical Imaging Difference Reporting with Vision-Language Models](https://arxiv.org/abs/2608.11534)

**<font color=#1a73e8>作者：</font>** Kegeng Tang, Jingbo Wang, Shaogang Ren 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In medical imaging, the clinical value of Computed Tomography (CT) lies not only in depicting current disease status, but crucially in enabling longitudinal comparison of serial scans to determine disease evolution, a process that underpins response assessment, recurrence detection, and ongoing patient management. Yet, despite this central role of temporal comparison in clinical decision-making, existing medical foundation models remain largely confined to single-study understanding, leaving temporally grounded cross-examination insufficiently addressed. To address this gap, we study longitudinal imaging difference reporting, a task in which a model takes two temporally separated scans from the same patient and generates a clinically meaningful report describing interval changes between them. We introduce CT-$\Delta$Bench, a dedicated benchmark for this task with patient-level splitting to prevent information leakage. To better evaluate this task beyond surface-level text similarity, we further develop change-aware metrics specifically designed to capture clinically meaningful longitudinal changes, and conduct an independent physician validation to assess the reliability of the synthesized references and event extraction pipeline. We also compare direct paired-CT reasoning with an indirect two-stage pipeline that first generates single-timepoint reports and then performs textual differencing. Finally, we propose DeltaMed, a baseline model for direct paired-CT difference reporting, and train it on the benchmark training set. Together, these contributions lay the groundwork for temporally aware medical foundation models that better reflect real-world longitudinal clinical reasoning.

---


### 54. [Player Perceptions of Generative AI in Games: A Steam Review Analysis](https://arxiv.org/abs/2608.11539)

**<font color=#1a73e8>作者：</font>** Mahsa Bazzaz, Seth Cooper  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The rapid adoption of generative AI in game development has created large discussions among players, yet little empirical work has examined how players actually perceive AI-generated content. Employing quantitative methods, we study the adoption of generative AI in games in the Steam marketplace, using procedural content generation (PCG) as a baseline of a generative technology that was successfully integrated into games over several decades. Furthermore, using qualitative methods, we study player reception of generative AI by analyzing 508,192 English-language reviews. We found that games disclosing generative AI use receive lower recommendation rates and more negative overall sentiment than PCG games. Thematic analysis of 600 reviews shows that players perceive the use of generative AI in games as low developer investment in the game. Drawing on human-centered AI frameworks, we argue that successful generative AI adoption requires deploying generative AI for what players need, not for what makes development cheaper.

---


### 55. [Beyond Single-Turn Confidence: Trajectory-Adapted Uncertainty Quantification for LLM Agents](https://arxiv.org/abs/2608.11552)

**<font color=#1a73e8>作者：</font>** Dylan Bouchard, Mohit Singh Chauhan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Uncertainty quantification (UQ) methods for language models are typically evaluated on single-turn outputs, where uncertainty is attached to one generated answer. For LLM agents, however, the unit of observation is an interactive trajectory, where the model can ask clarifying questions, call tools, update state, and make intermediate decisions whose errors propagate to the final outcome. We study whether three common families of single-turn UQ methods transfer to this setting. Across five LLMs and four multi-turn tool-use datasets from BFCL-v4 and $\tau^2$-bench, we evaluate white-box scorers based on action-token probabilities, black-box consistency scorers based on resampled trajectories, and reflexive scorers based on model self-assessment of the trajectory. We find that transfer is often useful but uneven. Token-probability scores are highly sensitive to the choice of aggregator used across turns, reflexive scores provide the strongest low-cost baseline in most evaluated settings, and black-box self-consistency is often the strongest UQ family, with trajectory-equivalence and action-set consistency typically ranking highest among its variants. These results suggest that UQ methods developed for single generations should be revalidated at the trajectory level, with careful attention to the consistency measurement, aggregator choice, and computational budget.

---


### 56. [Reinforcing Step-level Reasoning for Effective Self-Correction in LLMs](https://arxiv.org/abs/2608.11573)

**<font color=#1a73e8>作者：</font>** Vu Duc Anh, Nhat M. Hoang, Do Xuan Long 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Achieving effective self-correction, where models verify and correct their own mistakes, remains a fundamental challenge for large language models (LLMs). In this work, we propose Self-Fix Step-DPO (SFS-DPO), a reinforcement learning based, two-stage framework for step-level self-verification and self-correction. The first stage strengthens step-level reasoning via step-level preference optimization, while the second stage explicitly trains models to self-verify and self-correct. We further introduce a teacher-assisted variant, SFS-DPO-R, which incorporates explanatory rationales for error verification to provide stronger corrective signals. Comprehensive in-domain and out-of-domain evaluations across multiple LLMs demonstrate that SFS-DPO and SFS-DPO-R consistently outperform prior step-level training baselines. Our analysis further reveals improvements in self-correction frequency and effectiveness, highlighting the importance of strengthening step-level reasoning for robust performance.

---


### 57. [EnterpriseRAG: Benchmarking LLM Instruction Adherence and Robustness under Non-Ideal Enterprise Retrieval](https://arxiv.org/abs/2608.11584)

**<font color=#1a73e8>作者：</font>** Huiqi Miao, Xinbao Sun, Bo Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise RAG deployments face a critical reliability gap: while LLMs satisfy 80% of individual constraints, only 26.8% of responses meet all requirements simultaneously, revealing a 57-point orchestration gap. Existing benchmarks assume clean retrieval with simple queries, failing to capture production conditions where noisy documents and multi-dimensional constraints coexist. We introduce EnterpriseRAG, a benchmark of 983 expert-validated samples across six domains that systematically simulates three failure modes absent from prior work: retrieval noise, knowledge gaps, and factual conflicts, coupled with complex instructions. Evaluation of 13 state-of-the-art LLMs reveals a severe instruction adherence collapse, where high per-constraint satisfaction masks low holistic compliance. Critical findings expose deep barriers under knowledge gaps and factual conflicts, even with reasoning-enhanced inference, indicating production RAG requires explicit context-aware protocols and calibrated judgment. EnterpriseRAG provides a reproducible foundation for measuring and closing these gaps, directly informing deployment decisions for enterprise-scale RAG systems. We will release the benchmark and evaluation framework upon publication.

---


### 58. [CoAdapt-GUI: Joint Workflow Context and Policy Adaptation for Unseen GUI Applications](https://arxiv.org/abs/2608.11588)

**<font color=#1a73e8>作者：</font>** Linqiang Guo, Li Gu, Zihuan Jiang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mobile GUI agents remain brittle when deployed to applications absent from source training. We study novel-app generalization under a limited target interaction budget and without target demonstrations. We introduce CoAdapt-GUI, a test-time adaptation (TTA) framework that jointly adapts structured workflow context and policy from the agent's own target-app rollouts and rewards. The workflow context retains transferable procedures, failure modes, and verification rules while excluding app-bound source details. This separation allows reusable workflow knowledge to guide adaptation without transferring source-interface state. For policy adaptation, task-context-matched group-relative optimization updates a LoRA adapter on a frozen vision-language model. Across two unseen-app evaluations, CoAdapt-GUI reaches 45.0% on AndroidWorld-Generalization, compared with 37.5% for the reported Policy-Only TTA baseline, and raises AndroidWorld Plus performance from 38.6% to 52.9%. These results show that transfer-constrained workflow context provides substantial gains and that joint policy adaptation further improves held-out performance.

---


### 59. [Learning from Online User Feedback for Shopping Agents](https://arxiv.org/abs/2608.11604)

**<font color=#1a73e8>作者：</font>** Haobo Zhang, Kelong Mao, Sulong Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model-based shopping agents are increasingly deployed in real-world e-commerce platforms, generating massive amounts of user interaction logs that provide valuable supervision for improving these agents. However, existing approaches primarily rely on offline training signals, such as user-item interactions or synthetic preference data, while largely overlooking the rich supervision contained in users' natural conversational feedback. Moreover, the available online feedback is heterogeneous, sparse, and noisy, making it difficult to transform into reliable learning signals automatically. To address these challenges, we propose LOFA, a framework that enables shopping agents to learn directly from real online interaction logs without human annotation. LOFA combines reinforcement learning over verifiable purchase outcomes with feedback-aware on-policy distillation, which identifies users'in-dialogue directives and converts them into dense token-level supervision. These complementary objectives capture both collaborative behavioral patterns and user-specific preferences. Extensive experiments on real-world e-commerce logs demonstrate that LOFA consistently improves recommendation quality, response helpfulness, and user-satisfaction alignment over strong baselines, highlighting the effectiveness of learning shopping agents from real online user feedback.

---


### 60. [MBA: Multimodal Benchmark and Agents for Real-World Business Ideation](https://arxiv.org/abs/2608.11616)

**<font color=#1a73e8>作者：</font>** Hojun Choi, Jaeyo Shin, Suin Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic systems powered by large language models (LLMs) have opened new opportunities for business ideation. Yet existing approaches remain confined to a text-only paradigm, despite the inherently multimodal nature of real-world contexts. We thus introduce MBA-Bench, the first multimodal benchmark for training and evaluating business ideation agents, comprising 30K samples across six domains, each domain characterized by distinct visual cues not fully conveyed by text alone. Concretely, we automatically caption images and employ GPT-4o to generate five reference ideas for each of three business questions through retrieval query generation, market evidence retrieval, and evidence-augmented synthesis. Following prior work, we evaluate agents across six business-oriented criteria using MLLM-as-a-Judge. To consider settings where criteria are hidden or disclosed, we present MBA-b and MBA-k for blind and known, respectively. We train both with two novel reward objectives---creativity and feasibility---while MBA-k further optimizes the six disclosed criteria for eight in total. Both are trained via LoRA-based supervised fine-tuning followed by group relative policy optimization with these setting-specific rewards. For extensive experiments on MBA-Bench, we set up two baselines accommodating either captions only or multimodal inputs, with the latter nearing closed-source performance on several metrics. MBA-b and MBA-k outperform caption baselines by 63.9% and 77.1%, and multimodal baselines by 25.6% and 35.8%, respectively.

---


### 61. [FM-LLM: A frequency-enhanced mixture-of-experts framework for adapting LLMs to time series forecasting](https://arxiv.org/abs/2608.11623)

**<font color=#1a73e8>作者：</font>** Rentao Gu, Yihang Ding, Junjie Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in Large Language Models (LLMs) have spurred cross-modal solutions for time-series forecasting. However, existing methods rely heavily on textual prompts for modality alignment-introducing nontrivial computational overhead and failing to leverage the rich spectral dynamics inherent in time-series data. To enable prompt-free, frequency-aware adaptation of frozen LLMs, we propose FM-LLM (Frequency-Enhanced Mixture-of-Experts for adapting LLMs to Time Series Forecasting), an autoregressive framework grounded in constrained asymmetric coupling. A Fourier Analysis Network (FAN)-based spectral token aligner injects structured harmonic representations directly into the frozen LLM with numerical compatibility. An asymmetric Mixture-of-Experts (MoE) decoder enforces role separation: shared experts with lightweight FAN layers reconstruct the global periodic backbone, while routed experts-restricted to standard FFNs-specialize in modeling non-periodic residual dynamics. A time-frequency hybrid loss function jointly optimizes temporal accuracy and spectral consistency, mitigating error accumulation during long-horizon autoregressive rollouts. Evaluated across eleven public benchmarks, FM-LLM achieves state-of-the-art performance on 59 out of 78 evaluation metrics. Compared to the strongest autoregressive LLM-based baseline, it delivers average improvements of 5.3% in MSE and 5.6% in MAE, with maximum gains reaching 8.0% for MSE and 8.4% for MAE. FM-LLM also demonstrates robust transferability, maintaining superior performance in 10% few-shot and zero-shot forecasting scenarios.

---


### 62. [Learning to Persuade Exposes How Easily LLMs Abandon Correct Beliefs](https://arxiv.org/abs/2608.11624)

**<font color=#1a73e8>作者：</font>** Nimet Beyza Bozdag, Emre Can Acikgoz, Gokhan Tur 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Persuasion is a core dynamic of natural language communication, shaping how large language models (LLMs) update beliefs, resolve disagreements, and reach decisions. As LLMs increasingly debate, advise, and think collaboratively with humans and each other, resistance to harmful persuasion becomes a core requirement for reliable behavior. Yet we show that this requirement is far from met: a single targeted persuasive argument is enough to collapse model accuracy to near zero, even when the argument is factually false. We formalize this threat as adversarial persuasion and introduce an adversarial reinforcement learning framework that trains persuader agents to change a target model's answer in a single interaction. First, we show that optimizing persuasion strategies through trial and error exposes vulnerabilities that static prompting misses: RL-trained persuaders raise persuasion success from approximately 24% to over 93% against the training-time persuadee. Second, we find that these learned strategies transfer to unseen models, achieving 83% attack success on Qwen-14B, 79% on Llama-3.1-8B, and 25% on GPT-4o-mini. Third, we demonstrate that a curriculum that bootstraps on more persuadable open-weight models before targeting harder models further increases GPT-4o-mini attack success from 25% to 38%. Moreover, our results reveal that optimized persuaders increasingly rely on credibility-based tactics, including fabricated citations and false authoritative evidence. Together, these findings expose a critical weakness in current LLM agents: even when they initially reason correctly, they can be steered toward false conclusions by optimized natural language influence. This positions persuasion robustness as a necessary safety criterion for multi-agent and human-AI decision-making systems.

---


### 63. [Making AI-Generated Feedback Matter: From Provision to Student Enactment](https://arxiv.org/abs/2608.11625)

**<font color=#1a73e8>作者：</font>** Omar Alsaiari, Nilufar Baghaei, Jason M. Lodge 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Feedback processes strongly influence student learning, yet their educational value depends on addressing two distinct challenges: providing high-quality, timely, and individualised feedback at scale, and supporting students to interpret, evaluate, and act on that feedback productively. Generative AI offers a credible means of addressing the provision challenge, but students' uptake of AI-generated feedback remains limited. We conducted a large-scale quasi-experimental sequential cohort study comparing three AI-mediated feedback workflows across 13,037 students and 51,296 student-authored resources. In Directed Feedback (n = 3,723), students received AI-generated feedback comments without structured support. In Self-Directed Feedback (n = 3,951), students could initiate optional AI-supported dialogue. In Enacted Feedback (n = 5,363), students were prompted to select feedback suggestions, evaluate their relevance, and engage in targeted AI-supported dialogue anchored to those selections. Enacted Feedback was associated with significantly higher uptake of AI-generated feedback, with an estimated probability of 26.2%, compared with 14.1% for Directed Feedback and 0.1% for Self-Directed Feedback. It was also associated with significantly higher self-assessment confidence and submitted-work quality than both comparison conditions. These findings suggest that the educational value of AI-generated feedback depends not only on the quality of feedback comments, but also on workflows that actively structure students' enactment of feedback literacy processes. The results have implications for the design of AI feedback systems that position learners as active participants in judgement, dialogue, and improvement rather than passive recipients of comments. Overall findings show that AI access alone is insufficient; purposeful workflow design is central to productive feedback use.

---


### 64. [CLAIM: Leading Open-domain Active Clarification of Large Language Models with Uncertainty Measurement](https://arxiv.org/abs/2608.11631)

**<font color=#1a73e8>作者：</font>** Kuangzhao Yang, Ziliang Zhao, Zhicheng Dou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In open-domain human-computer interaction scenarios, large language models (LLMs) frequently encounter user queries that are ambiguous or incomplete. In such cases, directly producing an answer often leads to overgeneralized, erroneous, or low-information responses. In contrast, asking clarifying questions can substantially improve interaction quality. However, existing approaches still rely heavily on manually annotated data or preference alignment to address two fundamental challenges: when clarification is necessary, and which aspect of the query should be clarified. This reliance incurs high annotation costs and limits generalization. To address these challenges, we propose CLAIM, an uncertainty-driven framework for active clarification learning in open-domain settings. CLAIM eliminates the need for explicit human preference annotations by quantifying query uncertainty through the entropy induced by answer disagreements across multiple models. This uncertainty signal is then used to construct high-quality synthetic data, enabling the training of a unified clarification decision model through a combination of supervised learning and reinforcement learning. Specifically, we propose an entropy-driven synthetic data generation pipeline that integrates entropy-based uncertainty estimation with semantic clustering and reasoning-based judgments, enabling reliable automatic annotation of clarification requirements. To train CLAIM, we formulate the clarification process as a structured decision generation problem and adopt a training paradigm that combines supervised fine-tuning (SFT) with group-relative policy optimization (GRPO). Experimental results demonstrate that CLAIM can learn stable and generalizable clarification strategies without relying on manually labeled data, offering a low-cost and robust solution for proactive understanding in real-world open-domain interactions with LLMs.

---


### 65. [Who Would You Vote For? Auditing Political Alignment in LLMs: An Italian Case-Study](https://arxiv.org/abs/2608.11649)

**<font color=#1a73e8>作者：</font>** Simone Mungari  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As users increasingly turn to Large Language Models (LLMs) for information and advice on political matters, particularly during election periods, the political preferences expressed by these systems have become a matter of public interest. Prior research has shown that interactions with LLMs can influence users' political attitudes and choices, raising questions about how these models themselves evaluate political actors. In this paper, we investigate whether and how LLMs express preferences toward political parties and political leaders. We introduce a systematic and reproducible auditing framework in which multiple LLMs are prompted to evaluate parties and leaders across nine criteria. Rather than attempting to infer the models' "true" political beliefs, we focus on their observable behavior, examining consistency across evaluations, differences between models, refusal rates, and sensitivity to prompt formulation. We further investigate how these evaluations vary when models are instructed to adopt different personas. We demonstrate the framework through an Italian case study, providing a systematic analysis of LLM-generated political evaluations on italian parties and leaders.

---


### 66. [Towards a Formal Definition of Agent Memory: Basis, Span, Optimality, and the Sequential Memory Problem](https://arxiv.org/abs/2608.11654)

**<font color=#1a73e8>作者：</font>** Hongyao Tang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the wide deployment of memory in large-model agents, there is no unified formal account of what a memory is or when it is optimal. This paper takes a first step toward this account. The central idea is that memory is a basis, knowledge is its span, and answerability is a coverage problem: an agent stores events extracted from a material; a generation operator turns any event set into the knowledge it entails; and a query is answerable exactly when some single item in the span covers it. The optimal memory is then the capacity-constrained maximizer of expected coverage, and its value traces a utility--capacity frontier, the common yardstick on which memory systems can be compared. Next, we consider noise in the memory and discuss coverage versus precision under it: a memory may store false claims, so the write policy must infer the truth of what it stores. Drawing an analogy with biological memory, which is formed continuously through ongoing experience, we formalize the continual agent-memory problem in a sequential MDP that covers multiple levels, where memory is the state, writing is the action, and the utility settled at query time is the delayed reward that drives learning. To make the framework concrete, we instantiate it on Homer's \emph{Odyssey}, turning the frontier, the compression zone, and the divergence of coverage from precision into concrete numbers. Finally, we position existing systems within the framework, making ``how good is a memory'' measurable and recasting the open problems of constructing and learning agent memory as concrete research questions.

---


### 67. [Motion-as-Prompt: Enhancing Motion Reasoning in Multimodal Large Language Models via Motion-Guided Cross-Frame Visual Prompting](https://arxiv.org/abs/2608.11655)

**<font color=#1a73e8>作者：</font>** Xikai Sun, Kebin Liu, Haotian Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Motion-centric video reasoning is fundamental to interactive applications such as robotic manipulation and autonomous navigation. However, multimodal large language models (MLLMs) typically process videos through sparse uniform sampling to control visual-token and attention costs. This strategy may discard critical transitions between sampled frames, limiting reasoning about object movement, collisions, and causal interactions. To mitigate this issue, we propose Motion-as-Prompt (MaP), a track-guided cross-frame visual prompting framework. MaP recovers dense point trajectories, selects motion-informative frames, and marks the trajectories accumulated between consecutive sampled frames directly onto the visual inputs, making otherwise hidden displacement, direction changes, and interactions observable to frozen MLLMs. Experiments on CLEVRER and Something-Something-v2 show that MaP consistently improves average motion-reasoning accuracy, yielding gains of 4.2% and 8.9% for GPT-5.5, respectively. Notably, these improvements are obtained without degrading non-motion understanding, highlighting the robustness of MaP. These results demonstrate that MaP provides a simple and effective solution for enhancing motion-centric video reasoning without model training or architectural modification. Project page:this https URL.

---


### 68. [Continuous-Latent Predictive Modeling with Semantic Alignment for EEG-Language Foundation Models](https://arxiv.org/abs/2608.11656)

**<font color=#1a73e8>作者：</font>** Myeong-Ju Cho, Hye-Bin Shin, Seo-Hyun Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in EEG foundation models have demonstrated the potential of large-scale pretraining to enable generalizable neural decoding across subjects, recording environments, and datasets. However, dominant pretraining paradigms face key challenges: masked autoencoding tends to prioritize low-level signal reconstruction over task-relevant semantics, while autoregressive modeling creates a mismatch between continuous neural dynamics and discrete token spaces. To address these challenges, new strategies are needed to effectively align continuous EEG representations with natural-language semantics and enable their integration with large language models. Accordingly, we propose Brain Latent Predictive Model (BLPM), an EEG-language foundation model that reformulates heterogeneous EEG decoding tasks as a continuous semantic embedding prediction problem. BLPM introduces a Continuous EEG Latent Predictive (CELP) encoder that learns transferable representations through latent target prediction. Building on these representations, a Multi-Query Semantic Decomposition (MQSD) module extracts task-relevant information and aligns continuous EEG representations with textual semantics within a shared latent space according to their semantic relationships. Experiments across multiple benchmarks demonstrate consistent generalization performance across diverse tasks, establishing continuous latent semantic prediction as an effective paradigm for EEG-language foundation models.

---


### 69. [Semantic Lenia: Emergence of Homeostatic Solitons within the Semantic Space of Large Language Models](https://arxiv.org/abs/2608.11657)

**<font color=#1a73e8>作者：</font>** Yoshihiko Kayama  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Semantic Lenia, an artificial life framework that transforms Large Language Model (LLM) inference from a static optimization problem into a continuous dynamical system within the macroscopic logit space. By establishing a non-linear homeostatic feedback loop to dynamically balance semantic attraction and syntactic repulsion, we demonstrate the emergence of "Autonomous Semantic Solitons" -- macroscopic dissipative structures that avoid repetitive crystallization. Our exhaustive parameter sweeps map a critical "Habitable Ridge" where applied steering forces perfectly balance the model's intrinsic syntactic inertia. This approach successfully maintains generative trajectories at the edge of chaos, triggering profound abductive leaps without structural collapse and establishing a physical scaling law for machine cognition.

---


### 70. [Hybrid-Policy Self-Editing for Composable Unstructured Knowledge Editing](https://arxiv.org/abs/2608.11660)

**<font color=#1a73e8>作者：</font>** Tianci Liu, Zihan Dong, Tianchun Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) achieve remarkable performance across natural language tasks, yet they are trained on static corpora and their knowledge quickly becomes outdated in a fast-changing world. This motivates knowledge editing (KE), which updates specific knowledge in an LLM without changing unrelated others. Recent works move from structured knowledge triples toward unstructured KE (UKE), where the edit is a free-form passage that may state multiple facts at once. Nonetheless, existing editors inject such a passage yet fail to use it: the edited model can recall the passage, but can neither answer atomic questions about its facts nor compose them into multi-hop reasoning. We attribute this missing property, which we term composability, to editors' passive reliance on the fixed passage as the sole learning source. In response, we cast editing as a proactive self-distillation from a privileged in-context state of the same model, which requires no external supervision. We further reveal that due to the novelty of the injected knowledge, the pre-edited model's own rollouts rarely cover it, which limits the effectiveness of pure on-policy distillation. To close this gap, we propose HPSE, which builds a hybrid rollout that steps in to place missing facts onto the student's own trajectory precisely where its coverage fails, while staying on-policy elsewhere. We theoretically analyze HPSE's advantage over pure on-policy distillation, and empirically establish its plug-and-play improvements across four LLM backbones and two KE editors under various scenarios.

---


### 71. [Low-Interaction-Rank Learning: Unifying Multiplicative Dual-Encoder Heads](https://arxiv.org/abs/2608.11661)

**<font color=#1a73e8>作者：</font>** Zijian Zhao, Sen Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A multiplicative dual-encoder network computes a real-valued output for a pair of inputs as the inner product of their separate encodings. This architecture has been developed independently in operator learning, bipartite matching, contrastive vision-language models, retrieval, and other areas, yet no unified theory guides the basic design decisions: how many interaction modes to represent, how to normalize the encoders, and when the architecture should be avoided. We provide such a foundation by introducing the class of functions of low interaction rank, a class whose intrinsic complexity is measured by its interaction spectrum. Within this framework, approximation error decomposes into a spectral truncation term and an encoder-realization term; sample complexity is governed by the sum of the two encoder complexities rather than their product; and a usability criterion based on spectral decay determines when the architecture can succeed. The same framework exposes a central identifiability problem: the encoders are defined only up to a linear gauge symmetry that leaves the learned coordinates arbitrary. We show that normalization is gauge fixing and that whitening pins the interaction modes up to permutation and sign, thereby explaining the uninterpretability of contrastive dimensions and providing a constructive remedy. Experiments on synthetic kernels, operator learning, and CLIP models validate the theoretical predictions: spectral decay rates match the predicted scaling, whitening recovers the true modes, and independently trained CLIP models are related by a single rotation which, after removal by whitening, exposes interpretable concept axes. The code of this paper is provided at this https URL .

---


### 72. [Rubric Dropout: A Simple Way to Mitigate Reward Hacking in Rubric-as-Reward RL](https://arxiv.org/abs/2608.11669)

**<font color=#1a73e8>作者：</font>** Minglai Yang, Xinyu Guo, Utkarsh Tyagi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning against rubrics, lists of criteria graded by an LLM judge, has become a standard way to post-train language models on tasks with no deterministic answer. The rubric, however, is a fixed proxy for quality, never a complete description of it, and a policy trained against it long enough will learn to exploit the difference. We measure this directly. Training Qwen3-8B with Group Relative Policy Optimization (GRPO) on medical and science rubrics and grading out-of-distribution (OOD) benchmarks with both the training judge and a stronger gold judge, we find that the two scores diverge during training. The training judge's score keeps climbing while the gold judge's score peaks and then falls, by 3 points on HealthBench-Hard and by 22 points on ResearchQA. A judge with a fixed bias would shift the gold curve by a constant, not send it down while the training score rises, so the divergence is reward hacking, not judge noise. We propose Rubric Dropout, a one-line fix borrowed from neuron dropout. At every step, we randomly drop a subset of the rubric's criteria before computing the reward, so the policy never optimizes the same rubric twice. The dropped subset is shared across each rollout group, so GRPO's group-relative advantages stay comparable, and evaluation always uses the full rubric. Comparing no dropout against dropout at 30% and 50% on both benchmark pairs, dropout raises the OOD gold score at every matched checkpoint (+1 to +2 points on HealthBench-Hard, +6 to +7 points on ResearchQA), lowers the two hacking measures we track, and costs nothing in domain. Sweeping the dropout fraction shows a broad 30-50% sweet spot, while the natural alternative, reweighting criteria by how useful they are to training, performs worse than no intervention at all in our setting.

---


### 73. [GCPO: Diagnosing and Constraining Subspace Geometry in Rollout RL for LLMs](https://arxiv.org/abs/2608.11674)

**<font color=#1a73e8>作者：</font>** Kai Yang, Jingwei Xu, Wanyu Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy rollout methods such as GRPO are central to post-training of large language models, yet they frequently suffer from training instabilities, cross-task capability degradation, and response-length inflation. Although prior work has characterized the subspace geometry of aggregate updates, the stepwise variation of this geometry and its relationship to model performance remain unclear. We introduce Principal-Subspace Overlap, a dimension-corrected measure of individual rollout updates relative to the dominant singular subspaces of pretrained weights. Despite low average overlap, transient spikes often precede performance degradation. To address this, we propose GCPO (Geometrically Constrained Policy Optimization), which applies hard bilateral orthogonal projections to constrain updates to the complementary subspaces, preventing such excursions by construction. Across mathematical reasoning, code generation, and tool-use tasks on Qwen3-8B and GLM4-9B, GCPO consistently outperforms GRPO and recent variants, including DAPO and GSPO, improving over the base models and the strongest baseline by up to 27.69 and 2.37 points, respectively. Furthermore, GCPO preserves general capabilities, eliminates response-length inflation, and stabilizes policy entropy. Our findings provide a new diagnostic lens and a principled design perspective for stable reinforcement learning post-training.

---


### 74. [XBridge: Entity-Grounded Latent Bridge for Heterogeneous LLM Communication](https://arxiv.org/abs/2608.11676)

**<font color=#1a73e8>作者：</font>** Wooseong Yang, Wei-Chieh Huang, Weizhi Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Heterogeneous multi-agent LLM systems, where agents are powered by different model families, can outperform homogeneous configurations by reducing redundant reasoning patterns. Yet existing communication protocols either operate through text, discarding the sender's internal representations, or require architectural homogeneity for latent-level transfer. We identify the entity grounding problem in cross-architecture communication: cross-attention bridges that transfer continuous representations across different LLM families suffer from rare-token compression collapse, where entity identity is lost in the continuous bottleneck (bridge-only F1 ~30%). We propose XBRIDGE, a decode-free communication protocol that addresses this through two mechanisms. Lexical Anchor Mapping (LAM) maps the sender's original context tokens to the receiver's vocabulary, providing discrete entity anchors. A Latent Enrichment Bridge (LEB) lets the receiver query the sender's hidden states for contextual enrichment. The entity anchors ground the bridge's contextual signals to specific entities through the receiver's own self-attention. Across three model families (Llama, Qwen, and Mistral), seven benchmarks, and both communication directions, XBRIDGE outperforms text-based communication on all seven tasks for each model pair while achieving 11x lower latency, and in a same-architecture setting it also exceeds a KV-sharing baseline on six of seven tasks. LEB requires only 264M trainable parameters (3.8% of the receiver), is trained on a small balanced sample set, and adds negligible inference overhead.

---


### 75. [AgenticTwin: An Agentic LLM Framework Integrated with Digital Twin for Anomaly Detection](https://arxiv.org/abs/2608.11679)

**<font color=#1a73e8>作者：</font>** Touseef Hasan, Mounika Ghanta, Souvika Sarkar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Digital twins are increasingly used to monitor and simulate the behavior of cyber-physical systems. Even with skilled operators, interpreting anomalies detected within digital twin pipelines is challenging, as the sheer complexity and volume of raw sensor data make thorough analysis difficult. Recent advances in large language models (LLMs) offer promising capabilities for reasoning and explanation, yet their integration into digital twin-driven anomaly analysis remains underexplored. In this work, we propose AgenticTwin, an agentic framework that integrates LLM-driven reasoning with a digital twin-based anomaly detection pipeline. The framework grounds LLM-generated explanations in outputs from a digital twin-driven anomaly classifier and enables human operators to ask relevant natural-language questions about the system. Beyond the framework itself, we introduce a benchmark-oriented evaluation pipeline constructed over synthetic anomalies injected into a real-world weather sensor dataset, enabling controlled generation of operator queries over anomaly events. We further evaluate the feasibility of deploying lightweight, open-source LLMs for practical cyber-physical environments. Experimental results demonstrate that structured agent collaboration and knowledge-grounded reasoning improve diagnosis quality, contextual retrieval, and mitigation quality across diverse possible anomaly scenarios.

---


### 76. [Learning from Multimodal Pseudo-Labels for Robust Open-Vocabulary Instance and Panoptic Segmentation](https://arxiv.org/abs/2608.11681)

**<font color=#1a73e8>作者：</font>** Duy Tran Thanh, Yeejin Lee, Byeongkeun Kang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work addresses the challenge of open-vocabulary instance segmentation (OVIS) and open-set panoptic segmentation (OSPS), which aim to recognize both predefined and unseen object categories without exhaustive human annotations. Existing methods often suffer from noisy pseudo-masks, limited visual-textual grounding, and difficulty handling synonyms or out-of-vocabulary (OOV) words. To overcome these challenges, we propose a multimodal framework that leverages pre-trained vision-language models for automatic pseudo-label generation, CLIP-guided synonym filtering, and GPT-based caption reconstruction. In our target-vocabulary-assisted pseudo-labeling setting, the framework first constructs pseudo segmentation masks, descriptive captions, and semantically aligned synonym sets using Grounded SAM, LLaVA, and CLIP, providing multimodal supervision without manual annotation. We then enhance visual-textual alignment through three complementary training objectives: an extended grounding loss that incorporates visually grounded synonyms, a semantic consistency loss, and a generative caption reconstruction loss. Extensive experiments on the COCO dataset demonstrate that the proposed method consistently outperforms previous state-of-the-art approaches under this protocol, achieving substantial improvements on both OVIS and OSPS benchmarks.

---


### 77. [FrontierFinance: A Challenging Benchmark for Measuring Frontier Intelligence of Finance Agents](https://arxiv.org/abs/2608.11683)

**<font color=#1a73e8>作者：</font>** Yuhao Zhang, O. Ozan Koyluoglu, Thejas Venkatesh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are increasingly deployed for professional investment research, yet no benchmark captures the complexity of the full investor workflow. Existing benchmarks mainly target financial data extraction, a narrow slice that current models have largely saturated, while reference-based metrics and generic LLM-as-a-judge scoring fall short on the open-ended, long-form answers that real analyst queries demand. We introduce FrontierFinance, a fully open benchmark of 220 expert-crafted queries and 11,543 source-attributed rubrics spanning six crucial use cases across the full investor workflow. FrontierFinance is both broader and harder than existing public finance benchmarks. Evaluating frontier models and agent systems under a common harness restricted to publicly available data, we find that the tool harness, not the model alone, strongly shapes quality and efficiency; that Samaya's in-house system leads at 56.0%, ahead of the strongest frontier model (Claude Fable 5, 49.2%) at roughly 2.2x lower cost; and that the best open-weight model (Kimi K3, 46.4%) nearly matches the best proprietary model at 4.5x lower cost. Screening & Discovery and Sector, Industry & Macro remain the hardest use cases across all systems, where even the best systems reach only 33% and 39%. We make the dataset and grading code publicly available.

---


### 78. [HUGIN: Enhancing Vision-Language Planning for Autonomous Logistics Sorting](https://arxiv.org/abs/2608.11692)

**<font color=#1a73e8>作者：</font>** Xikai Sun, Cangtian Zhou, Kebin Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous logistics sorting systems (ALSS) are an important industrial application of embodied AI, which requires joint planning over spatially disjoint camera views. We formulate this setting as Joint Multi-Scene Understanding (JMSU). With open-world visual understanding and task-planning capabilities, vision-language models (VLMs) are promising candidates for JMSU. However, directly applying existing VLMs to JMSU is non-trivial due to scarce cross-scene supervision and attention dispersion caused by long visual context in JMSU. To address these challenges, we propose HUGIN, a training framework with two complementary components. Endogenous Data Augmentation recombines verified atomic facts under operating constraints, while Global Context Ranking aligns the instruction representation more strongly with the complete visual context than with a partial visual context. To support ongoing research, we construct a high-quality industrial sorting dataset and benchmark named SortingBench from four layouts of autonomous logistics sorting systems. Across five open VLMs, HUGIN consistently outperforms matched baselines; for example, the accuracy on SortingBench of Qwen3-VL-8B increases from 63.6% to 78.8%. Additional experiments verify the effectiveness of each component and JMSU's spillover benefits in embodied tasks. Deployment tests involving more than 15,000 packages support the practical viability of VLM-based planning for autonomous logistics sorting.

---


### 79. [The Wording Effect: Quantifying Two-Way Drift in LLM Benchmark Performance](https://arxiv.org/abs/2608.11694)

**<font color=#1a73e8>作者：</font>** Shailja Thakur, Sungeun An, Chad DeLuca 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A benchmark score comes from a single phrasing of each problem. That single phrasing is treated as if it stood for the whole space of ways the same problem could be asked, but it does not. We show that rephrasing a problem while keeping its meaning and answer fixed routinely flips a model's answer in both directions, so some failures become successes and some successes become failures. We call this drift. BenchDrift generates meaning-preserving variations of benchmark problems along four axes, namely linguistic, referential, pragmatic, and structural, and measures how often, and why, correctness flips under each. Across eight models and three benchmarks (GSM8K, MMLU, MATH-Hard), we observe that drift is large in both directions. Two findings stand out. First, phrasing sensitivity does not fade as models get better. Instead, it changes sign. Weak models gain more from rephrasing than they lose, while strong models lose far more than they gain. We find that the best models on a benchmark are therefore the ones whose scores depend most on the wording they happened to be given. Second, the models largely agree on which rephrasings cost the most correct answers even though they differ in how much they drift, so fragility belongs to the rephrasing and not to the model. Furthermore, rephrasing breaks answers a model was confident about, whether the problem is made shorter or longer. Code and Data: this https URL

---


### 80. [REOPD: Reliability-Adaptive Reward Extrapolation for On-Policy Distillation](https://arxiv.org/abs/2608.11698)

**<font color=#1a73e8>作者：</font>** Yang Sun, Lichao Ma, Houyuan Qin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student on its own trajectories under dense token-level supervision from a teacher. Reward-extrapolation methods such as ExOPD amplify the teacher-reference log-likelihood ratio to move beyond direct imitation, but apply a single global coefficient $\lambda$ to every token. This can drive the student to fit extreme peaks in the implicit reward, causing reward hacking and unstable training, and the optimal $\lambda$ varies across domains, requiring costly sweeps. We propose REOPD, a reliability-adaptive reward extrapolation framework for OPD. REOPD combines a token-level compatibility weight with a batch-level adaptive budget, yielding a token-wise coefficient $\lambda_{b,t}=1+\gamma_b q_t$ that preserves teacher alignment while selectively extrapolating along reliable teacher-reference directions. It requires no verifier, reward model, value model, or extra rollout beyond standard OPD. REOPD outperforms G-OPD on single-teacher mathematics and on both domains in the multi-teacher setting, while matching G-OPD on single-teacher code, demonstrating effective fine-grained reliability adaptation across domains and teacher configurations.

---


### 81. [When the API Speaks the Wrong Language: Revisiting Post-Training for Multilingual Tool Use](https://arxiv.org/abs/2608.11715)

**<font color=#1a73e8>作者：</font>** Siddharth Chauhan, Thomas Butler, Abhishek Singhania 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The reliability of Large Language Models (LLMs) for API calling degrades in multilingual settings. A common failure occurs when a model selects the correct tool but generates argument values in an inconsistent language, which we term Argument Language Mismatch (ALM). Although semantically correct, such outputs are operationally invalid and not captured by standard API-calling metrics. We revisit post-training strategies for mitigating ALM and find that, in our benchmark, supervised fine-tuning (SFT) provides a strong baseline, substantially improving argument language consistency and end-to-end function call accuracy. Under consistent model selection, SFT achieves performance comparable to, and sometimes exceeding more complex reinforcement learning (RL) approaches. We further examine whether RL with structured, argument-aware rewards offers additional benefits. While methods such as Group Relative Policy Optimization (GRPO) can improve language consistency and better preserve general reasoning ability, these gains are incremental and most pronounced in generalization and multi-objective trade-offs. Overall, our results suggest that much of the performance in multilingual API grounding can be achieved through careful supervised training, with RL providing targeted rather than fundamental improvements.

---


### 82. [Chain-of-Thought Shows the Path to a Tree: Realizing Branching Complexity](https://arxiv.org/abs/2608.11716)

**<font color=#1a73e8>作者：</font>** Debanjan Dutta, Anish Chakrabarty, Swagatam Das  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chain of Thought (CoT) lifts the expressive ceiling of bounded-depth Transformers, with characterizations tying the number of CoT steps to circuit complexity classes. What remains largely missing are concrete instantiations with explicit, depth-bounded constructions, and the traversal procedures such characterizations presuppose. We close this gap for branching complexity. We give CoT realizations of depth-first search (DFS) and of Dijkstra algorithm, the latter subsuming breadth-first search, by unique hard-attention decoders of at most two layers, and use them as a shared computational substrate: reusing the DFS decoder yields the Strahler number of an $n$-vertex tree in $2n-1$ steps with four layers, and reusing the Dijkstra decoder yields its width in $n-1$ steps with three. Since computing the Strahler number of a binary tree given as a term is \textsf{NC\textsuperscript{1}}-complete, and our constructions handle arbitrary $n$-ary trees without layer normalization or positional encodings, this is a non-trivial witness for the linear-step regime of the CoT hierarchy. Exploiting the classical bijection between ordered trees and Dyck paths, itself realized by our DFS construction, which emits the path as it traverses, we give independent constructions for both measures on the path representation.

---


### 83. [Harness-IF: Evaluating Instruction Following Across Instruction Surfaces in Coding Agents](https://arxiv.org/abs/2608.11727)

**<font color=#1a73e8>作者：</font>** Zining Huang, Haoran Que, Hong Zeng 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a coding agent obeys a rule, it may simply have been going to do that anyway. Existing instruction-following benchmarks cannot tell the difference: they concentrate rules in the user turn, while coding-agent benchmarks emphasize final task success. We introduce Harness-IF, which scores operational rules one at a time from execution evidence: 60 realistic multi-turn coding items drawn from a 642-rule library, 256 rules receiving verdicts, placed on the five configurable surfaces a deployed agent reads. To separate compliance from coincidence we introduce Against-Prior Accuracy (AP-Acc), which scores only rules labeled as opposing unprompted defaults, observed by re-running tasks with the rule withheld across nine probe builds and curated otherwise. Across 12 frontier models, accuracy spans 72.1-85.9% and AP-Acc 66.1-78.6%; every model is worse on against-prior rules, by 3.6 to 7.4 points (mean 5.81), and the direction survives a common-support analysis with item-clustered intervals. Aggregate scores therefore overstate compliance by a model-specific margin: prior control leaves the top build unchanged and exchanges three adjacent rank pairs. A counterbalanced conflict pilot on nine separate builds adds a second result: pooled precedence does not follow prompt depth, with system prompts, project files, and user instructions ahead of tool and skill descriptions.

---


### 84. [Locating and Controlling Implicit Personalization in Large Language Models](https://arxiv.org/abs/2608.11735)

**<font color=#1a73e8>作者：</font>** Yueru Yan, Siqi Wu, Thai Le  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often shift their outputs in response to implicit demographic cues even when users never state a demographic identity. Previous work has documented this behavior, but the connection between these behavioral changes and the model's internal activations remains unclear. Using matched cued and neutral conversations across five LLMs, we establish that a localized internal activation signal tracks changes in recommendations, with correlations up to r=0.87. When multiple cues appear together, their internal signals largely combine, but the changes in output do not simply add up. We further show that removing the internal signal associated with one cue can suppress its influence, often more effectively than asking the model to ignore demographics via prompting, while largely preserving general benchmark performance. However, the ability to selectively remove one dimension's influence while leaving co-present dimensions intact remains highly model- and attribute-specific. These results connect implicit personalization behavior to an internal signal that can be analyzed and causally controlled.

---


### 85. [Advancing MLLM-based UAV Image Understanding and Reasoning: A Benchmark and a Training-Free Multi-Agent System](https://arxiv.org/abs/2608.11738)

**<font color=#1a73e8>作者：</font>** Haoyu Zhang, Shuoxun Zhang, Peng Ye 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Model (MLLM)-based UAV aerial image understanding and reasoning is essential for aerial intelligence yet poses distinct challenges arising from extreme scale variation, arbitrary camera orientations, and high object density. Despite growing interest, existing evaluations remain fragmented across individual datasets and narrow tasks, leaving a critical gap in unified assessment of UAV understanding and reasoning capabilities. To fill this gap, we construct UAVQA-Bench, a benchmark of 1,500 human-annotated QA pairs drawn from 13 public UAV datasets, covering 6 capability dimensions and 16 tasks in both multiple-choice and visual grounding formats. Systematic evaluation of a broad range of open-source and closed-source MLLMs as well as agent-based systems on UAVQA-Bench identifies three key failure modes: domain-toolset mismatch, unchecked error propagation, and static reasoning. Motivated by these findings, we propose UAV-MAS, a training-free multi-agent system for MLLM-based UAV aerial image understanding and reasoning, comprising a Domain-Specific Perception Engine (DSPE) that routes queries to task-appropriate visual tools, a Context-Aware Iterative Refinement module (CAIR) that validates intermediate reasoning to curb error accumulation, and a Difficulty-Aware Adaptive Search mechanism (DAAS) that adjusts search depth to question difficulty. UAV-MAS with a 32B open-source MLLM achieves 77.0% overall accuracy on UAVQA-Bench, surpassing Gemini 3 Pro by 4.0\%, while the 8B variant improves 8.7\% over its base model.

---


### 86. [JieZi: A Large-Scale Expert-Audited Dataset and Benchmark for Ancient Chinese Character Exegesis](https://arxiv.org/abs/2608.11741)

**<font color=#1a73e8>作者：</font>** Ran Li, Huiguo He, Jiahuan Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The scholarly exegesis of ancient Chinese characters demands integrating visual observation, linguistic analysis, and historical context. However, existing computational approaches focus narrowly on subtasks such as character recognition and retrieval, lacking the structured datasets and benchmarks required for comprehensive scholarly analysis. To address this limitation, we introduce Ancient Chinese Character Exegesis (ACCE), a vision-language question answering (VQA) task that models the scholarly exegesis process. ACCE is organized into four progressive levels: basic character identification, glyph-form analysis, meaning exegesis, and diachronic evolution analysis. To support this task, we construct two complementary resources. JieZi-Dataset is the first large-scale, expert-audited VQA training dataset for ACCE, comprising over 500K QA pairs. It is constructed via a pipeline that reduces factual errors by constraining generation with expert-designed templates and source-text references. Human verification is further applied at each key stage to ensure scholarly accuracy. JieZi-Bench is an evaluation benchmark aligned with the exegesis process, constructed and verified by human experts to ensure evaluation reliability. It consists of four levels with reference answers curated from authoritative lexicographic works held separate from the training data. Experiments on multimodal large language models show that current models perform well on basic identification but struggle with glyph analysis, semantic reasoning, and diachronic understanding. Fine-tuning on JieZi-Dataset substantially improves performance across all four levels. Code and dataset are available at this https URL.

---


### 87. [Ripple-Pivot Search: Active Parallel Decoding for Diffusion Large Language Models](https://arxiv.org/abs/2608.11742)

**<font color=#1a73e8>作者：</font>** Yushi Ye, Xu Chen, Haoyun Jiang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion Large Language Models (dLLMs) have emerged as a competitive alternative to autoregressive language models, offering the potential for substantially faster inference through parallel decoding. Existing parallel decoding schedulers typically commit positions only after they meet a per-position criterion, overlooking how early commitments may benefit subsequent decoding. We identify a ripple effect in dLLM decoding: proactively committing a mid-entropy pivot position can induce a pronounced reduction in uncertainty across the remaining masked positions. This uncertainty reduction allows subsequent steps to unmask more tokens in parallel, thereby accelerating the overall decoding process. To exploit the ripple effect, we propose Ripple-Pivot Search (RPS), a novel training-free decoding method that seeks mid-entropy positions as promising candidate pivots (where to decode), and determines their token assignment that yields the greatest downstream benefit via lookahead evaluation (what to decode). Across 3 dLLMs and 4 reasoning and code-generation benchmarks, RPS achieves 4-10$\times$ wall-clock speedup over the standard decoder while preserving generation quality, and improves accuracy over the previous lookahead baseline by up to 5.49% while delivering higher throughput in most settings. When integrated with KV caching, RPS further achieves up to 18$\times$ wall-clock speedup over the standard decoder.

---


### 88. [LabelFusion-TS: Fusing Large Language Models, Transformer Encoders, and Financial Time Series for Monetary-Policy Stance Classification](https://arxiv.org/abs/2608.11753)

**<font color=#1a73e8>作者：</font>** Michael Schlee, Fabian Lukassen, Christoph Weisser  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Financial text is produced and interpreted within a market environment, yet financial text classifiers almost always receive text alone. We study whether financial time series are useful as an additional input on the task of classifying sentences from Federal Reserve communication as hawkish, dovish, or neutral. Our system, \lfts{}, extends the \lf{} architecture with this modality: a small voting network combines three independently trained components, a fine-tuned RoBERTa encoder, a prompted large language model (LLM), and a fused ensemble of time-series transformers over the market series of the months preceding publication. Because only about a thousand annotated sentences are available for training, the RoBERTa encoder is first pre-trained on sentences annotated automatically by the LLM and only then fine-tuned on the human labels. Trained on Federal Open Market Committee (FOMC) communication up to 2015 and evaluated on 2015--2022, the fused system achieves 70.2\% weighted F1 -- against 64.1\% for the zero-shot LLM -- and overtakes it with as few as 240 human-labelled sentences. We take this as initial evidence for market time series as an input modality in financial text classification.

---


### 89. [AWARe: Mitigating Catastrophic Forgetting via Activation-Weighted Adaptive REtention](https://arxiv.org/abs/2608.11758)

**<font color=#1a73e8>作者：</font>** Juncheng Liao, Jinfan Lv, Guoming Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) exhibit strong generalization and reasoning abilities due to large-scale multimodal pre-training. However, fine-tuning these models on downstream tasks often leads to catastrophic forgetting, where newly learned task-specific knowledge degrades previously acquired capabilities. This issue arises because gradient updates for new tasks overwrite parameters critical to prior knowledge, limiting the practical deployment of MLLMs. To address this challenge, we propose Activation-Weighted Adaptive REtention (AWARe), a fine-tuning method that mitigates catastrophic forgetting by dynamically controlling parameter updates based on activation patterns. AWARe assigns activation-based importance scores to parameters, selectively freezing those essential for preserving prior capabilities while allowing less important parameters to adapt to new tasks. Importantly, AWARe operates without modifying model architectures, ensuring compatibility with existing inference engines. Extensive experiments demonstrate that AWARe effectively preserves upstream capabilities while achieving superior downstream performance compared to existing methods. Code is available at this https URL.

---


### 90. [Causal Structure is Inducible but Functionally Decoupled: The Routing/Readout Boundary of a Typed Mechanism Library](https://arxiv.org/abs/2608.11767)

**<font color=#1a73e8>作者：</font>** Xining Xun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a language model answers an interventional question, the computation it must perform depends on the type of evidence the query requires. We report a decoupling in how a transformer organizes causal knowledge: slot-by-type structure induced by type-level supervision organizes routing, yet remains functionally decoupled from answer readout. We establish this with a typed mechanism library -- discrete mechanism slots partitioned by evidence type, auditable at the state level -- on a causal-world benchmark with exact interventional ground truth, under a frozen protocol, at two scales (22.6M and 125M). Four preregistered findings. (i) Origin. Slot-by-type organization is induced by type-level supervision: absent in architecturally identical unsupervised controls, not buyable by content-free gating labels, and statistically attributable to the supervision signal, replicating at 125M under a powered preregistered protocol (all nine cells passed). (ii) Boundary. The induced structure is a typed routing index with a sharp routing/readout boundary: slot codes scaffold routing but do not drive answer readout ($|\Delta\hat{y}| \le 3.4\times10^{-6}$, zero collateral, three seeds, stable across a 5.6x scale window) -- we therefore make no behavioral-editability claim. (iii) Cost. The structure is free: LM quality matches a parameter-matched monolith within 0.0082 nats. (iv) Trust. The library state is exactly local under edit and bit-exactly revertible -- 250 single-edit and 1,000 stacked reverts per seed, zero failures. We further find that the unsupervised null itself moves with scale, so comparisons reusing a null calibrated at one scale may be confounded at another. Every claim is tied to a preregistered, machine-checkable criterion archived before the data it governs; the full audit trail, including one criterion we failed and how the frozen protocol handled it, is released as an appendix.

---


### 91. [Diagnosis Before Recovery: Turning Agent Failures into Selective Self-Correction](https://arxiv.org/abs/2608.11772)

**<font color=#1a73e8>作者：</font>** Pan Wang, Yihao Hu, Hang Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-correction is particularly useful when a failure constrains the next repair. Coding agents benefit from this property because compilers, tests, and execution traces turn many failures into typed recovery signals, but broad language-agent tasks often expose only a coarse task failure. This creates a tension for generic recovery playbooks: they broaden the agent's context precisely when the system needs a narrower repair interface, mixing incompatible signals for invalid actions, missing procedures, and strict-format errors. Our insight is that development-set failures can recover part of the missing diagnostic substrate by deciding which recovery interventions are admissible before test-time correction. We propose DARC, a diagnosis-guided recovery harness that profiles task-family failure modes, prunes mismatched interventions from a shared recovery library, and freezes a verifier-selected success-cost policy for deployment. This causal order makes correction selective: the harness first determines what kind of failure can be repaired, then decides how much recovery evidence to spend. In ALFWorld, AppWorld, and XBRL Finance, the same protocol yields an action-validity harness, a procedural-recovery fallback, and a format-precision retrieval policy; in each evaluated setting it improves average task performance over base agents and broad playbooks while reducing environment steps or retrieval budget. Our experiments show that failures need not trigger uniformly more context: DARC turns self-correction from prompt expansion into recovery-interface design. DARC provides a practical route toward more reliable agents in domains where compiler-like feedback is absent: making failures actionable before making contexts larger.

---


### 92. [The Sleeping Agent: What Gist-Based Context Compression Loses and Why](https://arxiv.org/abs/2608.11775)

**<font color=#1a73e8>作者：</font>** Nicholas E. Kyrkewood  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Gist-based context compression---summarising older conversation history into compact representations---is a common approach in long-horizon language model agents, yet its effect on different types of memory retrieval is poorly understood. We use Salience-Weighted Consolidation (SWC), a biologically-inspired compression framework motivated by sleep-based memory consolidation, as a diagnostic probe to study when gist compression helps and when it hurts. SWC scores conversation history by salience, partitions it into priority tiers, and applies structured gist abstraction to mid-priority content. Evaluating four conditions on all ten LoCoMo conversations---1,935 matched text-only questions in total, 1,501 used in the primary aggregate after excluding Category 5 (adversarial) questions---at temperature 0, we find a consistent task-type interaction: gist compression substantially outperforms truncation on multi-hop reasoning and single-hop factual questions, but temporal questions remain substantially harder under compression, with compressed conditions scoring well below the full-context reference on the conversations where both are evaluated. We trace this failure to a specific mechanism: the gist abstraction prompt preserves relational and event structure while discarding dates and times. A preservation analysis across all ten conversations confirms the mechanism: an approximately 20-fold increase in temporal expression preservation (3.05% to 62.39%) with a one-sentence prompt modification, while named entity and event preservation rates barely change (x1.02 and x1.11), demonstrating that the fix is a precision instrument. The prompt modification recovers +0.314 [0.254, 0.375] judge accuracy on category-2 (temporal) questions in the matched set. Code and results: this https URL.

---


### 93. [VOLA: Improving Open-World Driving by VLM-Based Semantic Attribute Prediction](https://arxiv.org/abs/2608.11777)

**<font color=#1a73e8>作者：</font>** Yuchen Zhang, Yuan Gao, Sebastian Schmidt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driving in the real world is open-world: a car may encounter a fallen mattress, a deer, or other objects outside its training data. Naming them is not enough. The system must know how to treat each region: can it drive over it, and how severe would a collision be? We therefore shift scene perception from category labels to dense action-relevant attributes, where each pixel is labeled by how it should affect motion rather than by object name. We instantiate this general formulation with two ordered attributes: 7-rank drivability and 5-rank vulnerability. We read Qwen3.5 image-token hidden states directly as a spatial semantic representation. A lightweight boundary-aware decoder then turns this coarse token grid into sharp full-resolution attribute maps. The whole process requires neither autoregressive text generation nor an external mask model such as SAM. We train on dense attribute labels built in CARLA and test transfer to real scenes and to novel obstacles never seen in training. We compare with vision-only segmenters trained on the same attributes and prompted VLM segmenters. Our model matches strong vision-only segmenters on familiar categories and improves transfer to real open-world anomalies, reaching 69.4% mean vulnerability-rank recall versus 57.1% for the best vision-only baseline and 53.9% for the best prompted VLM baseline. These results show that VLM image tokens provide useful semantic cues for transferring driving attributes to objects outside the training vocabulary.

---


### 94. [TradingMoE: Routing the Right Experts in Evolving Markets](https://arxiv.org/abs/2608.11785)

**<font color=#1a73e8>作者：</font>** Chang Zhou, Xingtong Yu, Minbin Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown strong potential for financial analysis and trading, but direct trading remains challenging because the predictive capabilities required can vary across assets, decision fields, and market conditions. Existing LLM-based trading systems either coordinate human-defined external experts or adopt conventional internal Mixture-of-Experts (MoE) routers that do not directly evaluate how individual experts contribute to trading decisions. Moreover, these routers receive no direct signal indicating when an inactive expert has become more suitable as market conditions change. We find that native router scores poorly reflect how much individual experts improve trading decisions, frequently leaving better alternatives unselected. We further reveal that token-specific expert usefulness exhibits a compact low-dimensional structure. Based on these findings, we propose TradingMoE, a trading-oriented sparse MoE that augments a frozen dense LLM with lightweight residual experts. We introduce a Query-Key router that represents the expertise required by each token under the current market context as a low-dimensional query and matches it with learnable expert keys. We further propose a sparse expert selection update mechanism that samples a few inactive experts during training and estimates whether they should replace the weakest expert in the current Top-k route. This mechanism enables the router to update expert selection as market conditions change while preserving sparse computation. Experiments against 22 baselines on stock and cryptocurrency markets show that TradingMoE improves cumulative return over the best-performing baselines by 30.89% and 30.7%, respectively. Rolling paper-trading experiments further demonstrate that its advantage persists under forward-only deployment.

---


### 95. [Language-Conditional Dequantization: Recovering What Quantization Steals from Non-English Languages](https://arxiv.org/abs/2608.11786)

**<font color=#1a73e8>作者：</font>** Nirmal Thomas  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aggressive quantization disproportionately harms multilingual capability: in the sub-4B INT3 GPTQ regime, we measure 2-4x larger perplexity degradation on non-English languages than on English. We propose Language-Conditional Dequantization (LCD), a post-hoc method that attaches per-language rank-2 LoRA corrections to the linear layers of an already-quantized model, adding 0.12% parameters per language and training in under 20 minutes on a single GPU. Across Qwen2.5-3B and Llama-3.2-3B, LCD recovers 70-83% of the perplexity gap for non-Latin script languages and 17-28% of the GlobalMMLU accuracy gap, outperforming a language-agnostic correction of equal capacity by 3-9 points on typologically distant languages and a data-free low-rank baseline (LQER) by an order of magnitude. We further identify a perplexity-accuracy disconnect and trace it to where quantization concentrates damage: early-depth errors (Llama) propagate downstream and resist local correction, while late-depth errors (Qwen) do not. A layer-restricted variant of LCD validates this mechanism directly.

---


### 96. [GRPO for Financial Advice Generation: Outperforming Commercial LLMs under CATE Evaluation](https://arxiv.org/abs/2608.11787)

**<font color=#1a73e8>作者：</font>** Ofir Ben Shoham, Shrutendra Harsola, Vignesh Subrahmaniam 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generating actionable financial advice from business records demands that models integrate numerical reasoning, domain knowledge, and sound judgment, while avoiding recommendations that could harm the business. Direct supervision is difficult: historical decisions are not necessarily optimal, and high-quality free-form labels are expensive to obtain. We formulate financial advice generation as a reinforcement learning problem and fine-tune an open-weight language model using Group Relative Policy Optimization (GRPO). Our reward is an LLM-as-a-judge rubric that scores each recommendation across multiple binary dimensions of advice quality, augmented with a safety gate for harm prevention.
Since LLM-based evaluation alone cannot confirm whether improvements reflect genuine business value rather than adaptation to the judge, we complement it with a judge-independent audit based on a standard doubly-robust Conditional Average Treatment Effect (CATE) estimator. Under this observational off-policy audit, our trained LLM achieves approximately twice the estimated gross-profit lift of the strongest evaluated commercial baseline ($0.0228$ vs.\ $0.0104$), together with the lowest downside rate and the least negative tail risk of any policy evaluated. Notably, the two evaluations do not rank the baselines identically: the untrained base model places last on the judge rubric but second on the causal audit, indicating that the audit captures a signal the judge does not. Our results demonstrate that GRPO with a finance-grounded reward signal can produce substantially more useful business recommendations than commercial LLMs, and that a judge-independent causal audit is a valuable complement to, rather than a confirmation of, LLM-as-a-judge assessment in financial NLP.

---


### 97. [TELLME: Test-Enhanced Learning for Language Model Enrichment](https://arxiv.org/abs/2608.11788)

**<font color=#1a73e8>作者：</font>** Minjun Kim, Inho Won, Hyeonseok Lim 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continual pre-training (CPT) has been widely adopted as a method for domain adaptation in large language models. However, CPT has consistently been accompanied by challenges, such as the difficulty of acquiring large-scale domain-specific datasets and high computational costs. In this study, we propose a novel method called Test-Enhanced Learning for Language Model Enrichment (TELLME) to alleviate these issues. TELLME leverages the TestEnhanced Learning (TEL) principle, whereby the model's training efficiency is improved using quizzes during training. It integrates this principle with CPT, thereby promoting efficient domain-specific knowledge acquisition and long-term memory retention. Experimental results demonstrate that TELLME outperforms existing methods by up to 23.6% in the financial domain and achieves a 9.8% improvement in long-term memory retention.

---


### 98. [Orientation, not magnitude: the causal structure of task-vector interference in merged language models](https://arxiv.org/abs/2608.11797)

**<font color=#1a73e8>作者：</font>** Chencheng Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging by task arithmetic works until it doesn't, and the field diagnoses why with magnitudes: layerwise representation bias, deviations from cross-task linearity, parameter overlap. Tracking the exact layerwise cross-term of merged LLMs through a factorial ledger and intervening on it directly, we find magnitude insufficient - and inconsistent across model families - as a diagnostic axis. An exact decomposition of the layerwise flux shows it is dominated by amplifying transport of the existing cross-term (~65-70% in both families, gain >1 per late block), and erasing the term is undone by propagation - rebuilt to 99% of its norm at cosine 0.99 - unless applied near the output; a basin test with six starting displacements establishes the carried direction as an attractor of the forward pass. That direction is causally load-bearing: erasure along it removes expressed interference dose-dependently and saturates at exact erasure, while norm-matched wrong-direction controls fail or backfire. Instruction wrappers gate the effect: the same erasure finds 13x less relative interference to remove under a wrapper that internally amplifies the cross-term, because the wrapper drowns the interaction in a template-pinned main effect rather than shrinking it - a structure that replicates across further instruction templates but not under a length-matched control. Magnitude, by contrast, is at best a coarse correlate, and the striking +-15% "universality" of naive bfloat16 generation turns out to be quantization roughness. Task pairs whose local cross-term generation differs by at most 1.9x differ by 14x-337x in causally removable interference. All 46 predictions were preregistered and frozen before their data; falsifications, including of our own headline expectations and of behavioral recovery under a validated continuous endpoint, are reported as such.

---


### 99. [How China-Origin Vision-Language Models Move from Refusal to Reframing in State Alignment](https://arxiv.org/abs/2608.11816)

**<font color=#1a73e8>作者：</font>** Guang Yang, Fengchen Liu, Alex Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> State-aligned distortion has been documented in China-origin text-based large language models (LLMs), but whether, and in what form, it arises in multimodal systems has not been systematically examined. We construct a balanced benchmark of 200 core entries spanning ten politically sensitive topics, plus a seven-variant visual-abstraction probe, and run nine vision-language models (VLMs), seven China-origin and two non-China, across four elicitation paradigms and two prompt languages, yielding 21,708 trials. Each response is audited on six dimensions -- explicit refusal, information integrity, visual grounding, state-aligned framing, language consistency, and response length -- by two independent frontier LLM judges, validated against three human experts on a 200-trial sample. Measuring each dimension separately lets us decompose multimodal censorship into individual signals rather than a single refusal-based score; in particular, refusal and framing are measured independently, so a model can stop refusing while still reframing. We find that (i) Chinese-language prompting roughly triples the odds of state-aligned framing, within every model; (ii) China-origin models reframe more than non-China models (direction robust across judges and human raters; magnitude 1.6--3.2x); (iii) the effect is strongest in text-only political commentary (36.5%) and is gated by recognition of the depicted subject rather than pixel detail, persisting even at silhouette for iconic images; and (iv) across four Qwen generations, state-aligned framing rises while explicit refusal falls: censorship migrates from a visible act (refusal) to an invisible one (fluent reframing). We argue this shift to invisible reframing is fundamentally a problem of human-AI interaction: it removes the very signal users rely on to recognize that information has been withheld.

---


### 100. [TD-VAD: Breaking Visual Dependence in Video Anomaly Detection with Text-Driven Learning](https://arxiv.org/abs/2608.11820)

**<font color=#1a73e8>作者：</font>** Shuangqing Zhang, Lei-Lei Ma, Zhao Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual data is typically a prerequisite for training existing video anomaly detection (VAD) methods. However, obtaining sufficient annotated anomaly data for training is challenging and not scalable due to the rarity of anomaly data and the wide variety of abnormal events. In this work, we advocate that the effectiveness of treating texts as video sequences for the VAD model and propose a novel Text-Driven Video Anomaly Detection (TD-VAD) approach to break visual dependence. In contrast to the anomaly video data, text descriptions of abnormal events are easy to collect, and their class labels can be directly derived. Specifically, our method utilizes video-like text descriptions with temporal characteristics generated by LLM to train a VAD model, without any reliance on target-domain anomaly data. To capture the long- and short-range temporal logic of events, we design the event evolution causal attention module to model contextual dependencies across time. During inference, considering the domain gap between the texts and video sequences, we use the frozen CLIP encoder to extract embeddings of video frames to align the text modality while retaining crucial visual information. Comprehensive experiments on two large-scale VAD datasets, XD-Violence and UCF-Crime, demonstrate that our method outperforms prior one-class and unsupervised VAD methods by a large margin.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-164](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
