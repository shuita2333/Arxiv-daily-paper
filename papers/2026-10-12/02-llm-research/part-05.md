# 🧠 大模型相关研究 | 2026年10月12日

> 本类共 **288** 篇论文：已确认 **273** 篇，待复核 **15** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-288](./part-06.md)

---

### 201. ["Hot-Blooded" vs "Cold-Blooded": Simulating the Behavioral Phenotypes of Childhood Aggression via Generative Agents](https://arxiv.org/abs/2610.11951)

**<font color=#1a73e8>作者：</font>** Liping Fu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This study examines the construct validity of LLM-based generative agents in simulating reactive, proactive, and co-occurring aggression in children. Four distinct agents were instantiated using a theory-driven parameterization grounded in the social information processing model. A total of 1,920 simulation runs were conducted across eight social scenarios, employing a hybrid blind-coding pipeline to extract 32 quantitative behavioral indicators. Results demonstrate robust discriminant validity relative to a non-aggressive baseline, with large effect sizes. High cross-seed reliability confirms that behavioral differentiation is driven by underlying psychological parameters rather than model stochasticity. Qualitative narrative analyses further converged with established empirical literature. Overall, these findings indicate that theory-parameterized LLM agents can accurately reproduce distinct aggression subtypes, offering a scalable, highly controllable framework for hypothesis generation, intervention piloting, and the refinement of psychological measurement tools.

---


### 202. [Look Where You Can: Active View Selection for CAD Reconstruction under Occlusion](https://arxiv.org/abs/2610.11954)

**<font color=#1a73e8>作者：</font>** Kartik Bali, Mahish Guru, Yiderigun Borjigin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> CAD reconstruction methods assume a luxury reality rarely grants: unrestricted visual access to the object, photographed from any desired angle. Real objects, however, are scene-embedded, bolted against walls, wedged into corners, resting on floors, where the scene renders much of the view sphere unreachable and the remaining views unequally informative. We introduce \textbf{SightCAD}, a framework for parametric CAD reconstruction that treats view feasibility as a first-class constraint. In this work we consider objects from standard CAD benchmarks embedded in realistic indoor scenes with physically derived visibility constraints over a discrete view sphere. A learned view selector must choose $K$ feasible views for a vision--language model (VLM) that generates executable CadQuery code, scored by geometric fidelity of the executed solid. Because reward arrives only after discrete view selection, autoregressive generation, and CAD-kernel execution, we propose a joint training paradigm in which the view selector and the CAD-generation VLM are trained together against this reward. The learned selection policy departs sharply from random, uniform, and coverage-greedy alternatives, outperforming surface-area maximization (SA-max) by up to $6.4$ Intersection-over-Union (IoU) points across budgets $K\in\{1,\dots,5\}$. The full system surpasses strong external baselines on scene-embedded, occluded multi-view renders of DeepCAD and Fusion360 objects ($+21$ and $+17$ effective-mIoU points over the best baseline, respectively), as well as on test-time domain-canonicalized real images from the industrial T-LESS benchmark and on both synthetic and real images from the MP6D industrial metal-parts benchmark, while producing the highest rate of executable programs of any method compared (invalid-code rate ${\leq}1.5\%$).

---


### 203. [MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement](https://arxiv.org/abs/2610.11959)

**<font color=#1a73e8>作者：</font>** Xiaomi LLM-Core Team, Zongming Qiao, Ziyue Hua 等 100 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) is the central training paradigm for advancing large foundation models towards self-improvement. This report introduces the MiMo-V2.6 series, an omni-modal family that pushes the frontier of model intelligence by scaling RL compute. Prior to RL, we conduct mid-training on a broad multimodal corpus to provide ample exploration space, and build a solid infrastructure on the pretrained hybrid-SWA architecture to support subsequent scale-up. We scale RL compute along three dimensions: (1) larger batches and higher throughput, with an asynchronous training that consumes 1,568 samples and 2.7-3.7B tokens per step at context lengths of up to 1M; (2) more diverse and complex environments, spanning code, general, visual, and cyber domains under a mixture of agent harnesses; and (3) more grader compute, via groupwise agentic grading that yields more accurate reward signals for long-horizon tasks and steers the model towards shorter, more token-efficient solutions. To keep training stable at scale, we freeze the MoE router and establish a multi-layer defense against reward hacking. We further build infrastructure for mixed-task agentic RL, including a unified trajectory representation, high-concurrency multi-framework rollout, decoupled control and data planes, and training-inference consistency. We open-source the training dynamics, RL environments, and RL framework to facilitate reproduction and further research on scaled RL and model self-improvement.

---


### 204. [MindFlow: Mind Supernet Powered Thinking Flows for Research Idea Innovation](https://arxiv.org/abs/2610.11966)

**<font color=#1a73e8>作者：</font>** Mengdi Liu, Wenjue Chen, Wenyue Chen 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Research idea innovation is a fundamental engine of scientific progress, yet it remains difficult to generate and evaluate in a scalable and controllable way. This challenge lies in its inherently open-ended and multi-objective nature, where ideas should balance novelty, plausibility and feasibility. While recent LLM-based approaches have made progress through carefully designed prompts or agent pipelines, they are constrained by predefined, static ideation workflows. To address this limitation, we propose MindFlow, a framework that explicitly formulates ideation as a graph-structured Flow in Mind, which is composed of modular thinking operators and modeled by a probabilistic mind supernet. Given a research topic, a controller dynamically samples thinking flows to generate candidate ideas. This open-ended problem is optimized using a tournament-based relative ranking, enabling the controller to progressively favor higher-quality thinking flows. We further introduce an evaluation protocol that jointly assesses problem finding and problem solving, going beyond title- or abstractonly judgments. Across diverse topics, MindFlow shows its superiority as an explicit, controllable and optimizable research idea innovator.

---


### 205. [Specialized Decision Models vs. General-Purpose LLMs: Benchmarking Jev Across Knowledge, Reasoning, and Multilingual Tasks](https://arxiv.org/abs/2610.11978)

**<font color=#1a73e8>作者：</font>** Xing Li, Qingcheng Chang, Jinzhong Ning 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Jev is a "System One" model that returns a choice among given options instead of generating text. We study how such a specialized decision model compares with general-purpose large language models (LLMs). We evaluate Jev on 13 multiple-choice benchmarks covering knowledge, reasoning, and multilingual understanding, and compare it with 19 LLMs in three tiers: frontier, representative, and small. Jev is competitive with frontier LLMs on knowledge and commonsense benchmarks and obtains the best score on MMLU-Redux and ARC-Challenge. Outside mathematics, it also outperforms most representative LLMs and all small LLMs. However, it falls behind on mathematical word problems: on MathQA, it is 17.7 points below the frontier median and scores lower than all 19 LLMs. These results indicate that a specialized decision model can match general-purpose LLMs on decisions that rely mainly on knowledge, but not on decisions that require multi-step calculation.

---


### 206. [FearCaut-Qwen: Affective Steering in a Vision-Language Model Shifts the Decision Criterion for Hazard Assessment](https://arxiv.org/abs/2610.11986)

**<font color=#1a73e8>作者：</font>** Xiaoshan Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) show great potential for damage assessment after a disaster, but a recurring deficiency is that they are reluctant to declare a hazard; that is, recall is low even when overall accuracy appears adequate. This study examines that deficiency by using signal detection theory to decompose the decision behavior into perceptual capability and decision-criterion placement. We then propose a novel method for correcting the over-conservative decision policy, inspired by the finding that fear makes humans risk-averse, and ask whether an affective representation associated with fear can be causally manipulated to similarly alter a VLM's decision tendency. Using mechanistic interpretability, we localize a causally implicated affective circuit in the model and use activation steering to manipulate it while observing the effect on downstream prediction. The method is tested on a two-stage SeisMLLM pipeline built on Qwen2.5-VL-7B-Instruct, which flags only 27.0% of genuinely unsafe buildings on the SeisMLLM-1K test split and never issues a false Red, an SDT criterion of c = +1.354, despite adequate evidence quality (d' = 1.521). An affective direction is localized on emotion-rich natural scenes, causally validated by sparse-neuron knockout and distributed steering on held-out emotion data, and then injected into the building task. Fear-direction injection raises Red recall to 75.7% (p<0.001), and subtracting the same direction suppresses Red predictions entirely, whereas norm-matched random and matched happiness directions show no significant effect. The mechanism is a shift in criterion (c=-1.515) while discrimination is not improved (d'=-0.493). These results show that VLM decisions can be adjusted at inference time without retraining and demonstrate how mechanistic interpretability can be used to diagnose and control VLM decision behaviors in engineering applications.

---


### 207. [MetaOPD: Meta-Learned Token Weighting for On-Policy Distillation](https://arxiv.org/abs/2610.11989)

**<font color=#1a73e8>作者：</font>** Zipeng Wang, Xinpeng Dong, Yuefan Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student on its own generated responses using token-level teacher supervision. However, uniform weighting overlooks differences in token learning value, while existing weighting methods rely on predefined mappings from prediction signals to token weights. These mappings are not learned from the effectiveness of the resulting student updates, limiting their ability to adapt to evolving learning needs. In this paper, we propose MetaOPD, a bilevel optimization framework that jointly learns the student model and a lightweight token-weighting network. The inner objective updates the student through weighted OPD, while the outer objective optimizes the weighting network using validation loss on reference solutions after a virtual student update. Differentiating through this update connects weighting decisions to their effects on post-update performance, allowing the mapping from prediction signals to token weights to evolve alongside the student. Experiments on six mathematical reasoning and three out-of-domain datasets, covering two student scales and seven baselines, demonstrate the effectiveness of MetaOPD, with Avg@8/Pass@8 gains over OPD of 1.99/5.97 percentage points for the 0.6B student and 2.25/6.41 points for the 1.7B student.

---


### 208. [DataVista: Diagnosing Multimodal LLMs on Data Video Understanding](https://arxiv.org/abs/2610.11993)

**<font color=#1a73e8>作者：</font>** Yupeng Xie, Zhenyang Wang, Jiayi Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Data video is a media form that integrates data visualization with video narrative, widely adopted in news reporting and business analysis. Compared with general video understanding, data video understanding places greater emphasis on accurately reading data from animated charts, integrating evidence across charts and time, and understanding how narrative organization and visual design communicate information. Yet existing benchmarks target either general videos or static charts, and data video understanding has not been systematically evaluated. We present DataVista, the first benchmark for data video understanding, containing 961 real-world data videos and 6,775 evaluation questions organized under a three-level progressive capability framework (data perception, temporal reasoning, narrative understanding) with 10 fine-grained question types across five topic domains. Systematic evaluation of 19 mainstream MLLMs shows that the best-performing model, Gemini-3.1-Pro, achieves 70.0% overall accuracy, still far below human expert performance, with models performing worst on Causal Reasoning and Narrative Structure. Increasing frame counts and adding subtitles mainly benefit data perception and temporal reasoning, with limited gains in narrative understanding. Further analysis of model responses identifies typical failure modes in chart reading, evidence judgment, and instruction understanding. The benchmark is available at this https URL.

---


### 209. [Agentic-TTT: Training test-time policy for test-time training](https://arxiv.org/abs/2610.12002)

**<font color=#1a73e8>作者：</font>** Jiahao Lu, Mohan Kankanhalli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time training (TTT) adapts an LLM's parameters using signals derived from test inputs, and can make striking improvements in pre-specified settings such as IMO competitions or designated open problems. By turning deployment experience into parameter updates, TTT provides a direct mechanism for model-level self-improvement. Yet TTT is not universally beneficial: each TTT algorithm works in different settings, and applying an ill-suited method could waste test-time compute or even damage model performance. Therefore, such parameter-level self-improvement requires agency: the model must decide when TTT is warranted, which algorithm to invoke, and whether an existing skill can be reused. To fill this gap, we introduce Agentic-TTT, which learns a test-time policy to govern those decisions. Agentic-TTT turns TTT procedures into callable tools, treats accumulated skills as an evolving deployment environment, and trains its policy using the observed utility gains from its decisions. On our benchmark, Agentic-TTT nearly doubles the utility over the backbone model, learns to trade off utility against compute, and generalizes to domains unseen during training. Together, these results point toward autonomous self-improvement: models that can decide how to learn from their own deployment experience.

---


### 210. [Examining Social Attribution in LLM Reasoning: A Theory-Guided Probing Methodology](https://arxiv.org/abs/2610.12022)

**<font color=#1a73e8>作者：</font>** Zhaoxin Yu, Qingchao Kong, Dajun Zeng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in sociotechnical systems where social attribution, the reasoning process attributing external events to the causes and reasons of agents' social behaviors, plays a critical role. These processes involve judgments of social cause, responsibility, and blame/credit to agents. Although attributional models are well-studied in social psychology and cognition through Attribution Theory, social attribution remains underexplored in AI, particularly LLM social reasoning. This paper provides the first systematic exploration of LLM social attribution. Our work focuses on responsibility and blame attributions, examining current LLMs' judgments and their underlying internal mechanisms. Guided by attribution theory, we construct a social attribution benchmark consisting of a Vignette subset based on classic scenarios from attribution theory research and a Reality subset based on real-world social narratives, yielding 7,639 responsibility/blame judgment questions. On this basis, we evaluate 32 representative LLMs and 5 basic non-LLM baselines. To further explore the internal mechanisms underlying the LLM judgment process, we develop a probing-based methodology to investigate the latent-space representations of 5 key attribution dimensions and the consistency of their influences on LLM judgments compared to those in human social attribution. Our research findings reveal that current LLMs exhibit measurable but incomplete agreement with human responsibility and blame judgments, and meanwhile, this agreement is positively correlated with model size. Some attribution dimensions are systematically decodable from specific positions in LLM hidden states, and their influences on the final judgment are consistent with those indicated by human Attribution Theory. The dataset and associated code are available at this https URL.

---


### 211. [Natural Language to First-Order Logic LLM-based Autoformalization](https://arxiv.org/abs/2610.12030)

**<font color=#1a73e8>作者：</font>** Andrea Brunello, Cristian Curaba, Luca Geatti 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have renewed interest in autoformalization. Yet, when First-Order Logic (FOL) is considered as the target formalism, the field still lacks a unified task formulation and a systematic survey. This paper addresses this gap: we first provide a principled definition for the FOL-autoformalization task by distinguishing Ontology Extraction from Logical Translation, showing how their conflation obscures (cross-study) evaluation; we review existing datasets, evaluation metrics, and LLM-based methods, including fine-tuning, prompting, and verification-based refinement; we identify open challenges in benchmarking, semantic evaluation, ontology-aware methods, and end-to-end applications.

---


### 212. [Do Not Train Away Uncertainty: Early Uncertainty Anchored Calibration](https://arxiv.org/abs/2610.12048)

**<font color=#1a73e8>作者：</font>** Yutong Xie, Jiawei Tang, Zhenglin Hua 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep neural networks, including large language models, have achieved remarkable performance across various tasks. However, they are prone to overconfidence during training or fine-tuning. In this work, we observe a consistent phenomenon across different models that the early model is better calibrated, while later training or fine-tuning yields marginal accuracy gains but substantially increases calibration errors. Our analysis suggests that the early model retains uncertainty awareness in both its predictions and features, which is gradually lost with continued training. To avoid training away this uncertainty awareness, we propose \textbf{EUA-Cal}, a novel method that exploits the \textbf{E}arly model as an \textbf{U}ncertainty \textbf{A}nchor for \textbf{Cal}ibration. EUA-Cal introduces early prediction regularization to preserve early predictive uncertainty and prototype structure regularization to exploit uncertainty reflected in the early feature space, jointly mitigating overconfidence. Extensive experiments on image classification and multiple-choice question answering across eight diverse models demonstrate that EUA-Cal outperforms state-of-the-art calibration methods.

---


### 213. [Structure Tax: How Structured Output affects LLMs Performance](https://arxiv.org/abs/2610.12056)

**<font color=#1a73e8>作者：</font>** Vineet Kumar, Kanishka, Bhuvanesh Mandora  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deploying large language models in production often requires constraining outputs to structured formats such as JSON or XML, and prior work treats the resulting accuracy loss as an inherent `structure tax'. We re-examine this claim by evaluating a battery of models, datasets and schemas, measuring task accuracy, confidence calibration, and hidden-state geometry. The tax turns out to depend on schema design rather than on structure per se: reasoning-first field ordering matches or exceeds free-form accuracy, while answer-first ordering causes steep drops, particularly in smaller models. Format sensitivity scales inversely with a task's own structural constraints, and schemas that preserve reasoning order also improve calibration with CKA showing greater separability between correct and incorrect representations in middle transformer layers. Our findings indicate that properly designed structured formats can match or exceed free-form performance, reframing the critical question from `whether to structure' to `how to structure' for optimal reasoning preservation.

---


### 214. [Look Back, Think Ahead: Visual Memory on Demand for Efficient Multimodal Reasoning](https://arxiv.org/abs/2610.12060)

**<font color=#1a73e8>作者：</font>** Yicheng Xue, Han Wu, Jufeng Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Processing long visual token sequences from high-resolution images makes multi-step reasoning computationally expensive for multimodal Large Language Models (MLLMs). Existing one-shot pruning and aggregation methods compress visual tokens into a fixed context before decoding. However, visual evidence needs can shift as reasoning unfolds, making it difficult for a fixed compressed context to retain all the details needed across stages. To address this challenge, we propose ViMoD, a lightweight framework that maintains a compact visual context while preserving access to original fine-grained evidence as reasoning needs evolve. Deformable Aggregation of Region-wise Tokens (DART) learns content-adaptive groups and aggregation capacities, constructing compact Coarse representations linked to recoverable original Fine tokens. Temporal Routing for Adaptive Contextual Evidence (TRACE) integrates decoding history to anticipate upcoming evidence needs and select, retain, or replace active Fine-token groups. Selected Fine tokens augment the persistent Coarse context in the frozen backbone, enabling stage-specific evidence access without continuously attending to all visual tokens. On Qwen3-VL-4B, ViMoD outperforms all evaluated baselines on all eight reasoning benchmarks at a 20% target visual token budget, improving the mean normalized score by 39.0% over the strongest evaluated one-shot baseline. These gains are achieved with only 0.0546% additional trainable parameters relative to the frozen backbone.

---


### 215. [When Should Agents Think? Adaptive Reasoning via Cross-Turn Estimation](https://arxiv.org/abs/2610.12061)

**<font color=#1a73e8>作者：</font>** Yiruo Cheng, Shen Huang, Xiaoshuai Song 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based agents have demonstrated strong capabilities on complex tasks. They typically perform reasoning before each action throughout an interaction trajectory. However, reasoning may not be necessary at every turn, as reasoning produced earlier can continue to support subsequent actions. A key challenge is therefore to determine when existing reasoning remains sufficient and when a new reasoning step is needed, without relying on costly generation-based verification. We find that decreases in the likelihood of subsequent reference actions after removing additional reasoning closely track whether those actions remain recoverable given earlier reasoning, providing an effective and lightweight signal for estimating cross-turn action support. Based on this observation, we propose Reasoning Adaptation through Cross-Turn Estimation (RACE), a training approach for adaptive agent reasoning. RACE introduces a Likelihood-Guided Progressive Reasoning Cover Detection (LoGiC) procedure that progressively identifies reasoning turns whose removal has limited impact on the current and subsequent reference actions. The resulting removal signals are incorporated into both supervised fine-tuning and agentic reinforcement learning, enabling the policy to learn when to reason and when to act directly. Extensive experiments on four representative agent benchmarks show that RACE substantially reduces reasoning cost while maintaining or improving task performance.

---


### 216. [ILM: An AI-Powered Storytelling Educational Tool](https://arxiv.org/abs/2610.12064)

**<font color=#1a73e8>作者：</font>** Suhaila Mohammed, Abdelaziz Serour, Allison Lahnala  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Digital technologies have made Islamic narratives more accessible, but existing platforms provide limited support for structured learning and comprehension of these stories, particularly in Arabic and multilingual settings. We present ILM, an interactive educational platform for Stories of the Prophets that combines Arabic natural language processing, structured knowledge representation, and retrieval-based question generation. Admin-approved Arabic narratives are processed by a Knowledge Graph (KG) Constructor Engine that identifies entities and narrative relationships and stores them as structured knowledge, enabling learners to explore stories through a visual story map and answer entity- and relation-based questions generated from the KG. Separately, a multilingual retrieval pipeline retrieves relevant passages from the original narratives to generate multiple-choice and open-ended comprehension questions. For open-ended questions, an LLM-as-a-Judge evaluates learners' answers against the retrieved passages and reference answers to determine correctness. The platform also incorporates Quranic content as a separate enrichment layer, allowing selected narratives to be supplemented with source-supported information. By combining structured knowledge with passage-based retrieval, ILM supports narrative exploration, comprehension, and assessment across Arabic and multilingual content. The system demonstrates the feasibility of combining structured knowledge representation and retrieval-based generation to support interactive learning of Islamic narratives. A demo is available at this http URL.

---


### 217. [All Verdicts are Not Equal: Rethinking LLM Judge Reliability](https://arxiv.org/abs/2610.12083)

**<font color=#1a73e8>作者：</font>** Vineet Kumar, Darshita Rathore, Anindya Moitra  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-Judge is the standard paradigm for NLP evaluation, yet its systemic reliability remains poorly understood despite being widely treated as a deterministic ground truth. We present a comprehensive reliability audit, stresstesting six frontier models across four benchmarks, five prompt formats, two presentation orders, three sampling temperatures, and ten repetitions per condition. Our empirical analysis reveals severe vulnerabilities: verdicts change across identical replications at temperature zero, position-order swaps flip the majority of verdicts on challenging tasks, and the most deterministic judge achieves perfect consistency by trivially repeating incorrect verdicts, agreeing with ground truth only 51% of the time. To formalize these multi-faceted failure modes, we introduce the trustworthy verdict rate (T ), a unified metric capturing the joint probability that an evaluation is reproducible, order-invariant, and accurate. UsingT , we derive a theoretical upper bound on accuracy imposed by position bias and show that reliability is item-specific rather than modellevel. Finally, we demonstrate that shifting from pairwise win-rate to holistic rubric scoring improves trustworthiness more than any single-format prompting intervention, offering an actionable framework for robust NLP evaluation.

---


### 218. [Is Memorization Context-Sensitive? Prefix-Based Extraction Beyond Isolated Prefixes](https://arxiv.org/abs/2610.12085)

**<font color=#1a73e8>作者：</font>** Ali Satvaty, Narjes Sharafi, Jirui Qi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can expose memorized training sequences under prefix-based extraction: given a prefix from a training example, the model may assign high probability to the original continuation. In deployed systems, however, prefixes are rarely evaluated in isolation. They often appear together with instructions, retrieved documents, or other task-specific context, as in retrieval-augmented generation (RAG). This motivates examining whether contextual conditioning mitigates memorization or merely changes the set of memorized samples that become extractable. We investigate this issue through paired item-level measurements of probabilistic suffix extraction. For each prefix-suffix pair, we score the target suffix under an empty prompt and under retrieved contexts of varying relevance, across three open-weight instruction-tuned models. We find that context does not simply erase memorization. Instead, extractable memorization consists of a context-robust core and a context-sensitive boundary. Many samples that are extractable without context remain extractable under the retrieved context, especially as the prefix length increases. At the same time, context mainly affects marginal samples near the extraction threshold: it suppresses some exposures, but also enables new ones that are missed by prefix-only evaluation. These findings qualify the view that RAG reduces memorization risk. Context can lower aggregate extraction by suppressing boundary cases, yet robustly extractable samples persist, and context-enabled extractability remains security-relevant.

---


### 219. [EvoAlloc: A Self-Evolving Resource Allocation Agent for Efficient Program Evolution](https://arxiv.org/abs/2610.12086)

**<font color=#1a73e8>作者：</font>** Yanning Dai, Yuhui Wang, Nanbo Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based program evolution relies on evaluation feedback to guide the iterative search for high-performing programs. However, evaluation is often computationally expensive, making it essential to allocate limited resources to candidates that can most effectively advance the search. Existing LLM-based methods typically rely on fixed allocation strategies throughout the search, potentially wasting resources on low-value candidates while overlooking promising ones. We propose EvoAlloc, a self-evolving resource-allocation agent that learns from search experience to revise its strategy for allocating computational resources across candidates. EvoAlloc periodically consolidates prior search and allocation outcomes into reusable experience, which informs subsequent strategy revisions. It further uses a counterfactual exploration mechanism to occasionally evaluate candidates denied resources by the allocator, revealing their outcomes to enrich its experience for future strategy updates. Across coding and agent-harness optimization benchmarks, EvoAlloc requires 59-82% fewer full evaluations and 61-89% fewer total LLM tokens to reach baseline-level performance. Moreover, under the same full-evaluation budget, EvoAlloc achieves 8.7-12.0% higher final performance.

---


### 220. [Recompose and Refine Latent Reasoning Flows for Vision-Language-Action Models](https://arxiv.org/abs/2610.12090)

**<font color=#1a73e8>作者：</font>** Hongyu Shi, Sen Zhao, Zuyu Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Latent reasoning enables vision-language-action (VLA) models to transform multimodal observations into task-relevant internal states before generating continuous robot actions. While existing methods learn to generate or refine such states for each policy query, they discard successful reasoning after execution and therefore reconstruct similar computation from scratch. We present Reasoning and Flow Memory (FLOWMEM), a unified VLA model that turns successful latent computation into reusable reasoning experience. Rather than appending a fixed retrieved context, FLOWMEM dynamically retrieves and recomposes compatible latent fragments as the embodied context evolves, forming a reasoning route that follows the temporal structure and progress of successful computation. The route is then refined using current visual and proprioceptive evidence before it conditions action generation. Experiments on RoboMME and LIBERO-Plus show that FLOWMEM attains 48.0% and 77.3% success, outperforming memory-free policies by 1.7 and 4.1 percentage points, respectively. These results demonstrate the value of reusing successful latent computation for closed-loop VLA control.

---


### 221. [Could LLM Watermark Detection be Public?](https://arxiv.org/abs/2610.12106)

**<font color=#1a73e8>作者：</font>** Georgios Milis, Tom Sander, Tomáš Souček 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Watermarking large language models is popular for tracing chatbot and agentic outputs, yet detectors remain unreleased since exposing them could let attackers do targeted edits with the detector's feedback. However, watermarks are already vulnerable to uninformed tampering attacks. We thus first quantify whether a public detector would be an additional liability in a deployment setting at varying levels of access, from token-level scores to a binary verdict. Second, we introduce a split-key public-private watermarking method that exposes one key through a public detector while keeping the other for full verification and forensics. An informed attacker can only move the public signal, creating an imbalance between public and private scores. We introduce a statistical test for this imbalance, and combine it with the full key verdict in a two-stage mechanism. Third, we evaluate the split-key method on a wide range of removal and forgery attacks, comparing the uninformed to detector-informed settings. Public detection improves removal only at small edit budgets, since plain rephrasing already strips the watermark at a lower quality cost, but it does enable forgery, which the private pipeline can identify. Overall, releasing half of the watermark enables transparency and interoperability, and tampering with the released half stays detectable. This bounds the provider's liability and questions the need to keep detectors fully private.

---


### 222. [Universal Textual Teaching for LLMs](https://arxiv.org/abs/2610.12114)

**<font color=#1a73e8>作者：</font>** Zhanyi Lu, Huan Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation (KD) transfers knowledge from stronger Teacher models to weaker Student models, but most methods require training the Student parameters, thereby binding the distilled knowledge to a specific architecture and checkpoint. This implicit representation is difficult to interpret or reuse across models and limits KD for API-only or costly-to-train models. This paper studies knowledge transfer for large language models (LLMs). We introduce Universal Textual Teaching (UTT), a parameter-update-free framework that distills observed Teacher-Student knowledge gaps into a textual, interpretable, and reusable natural-language artifact called Primer. Specifically, UTT first identifies representative gap cases through paired evaluations, and iteratively updates the Primer via multi-role interactions: the Student attempts each task, the Prompter turns evaluation feedback into a teaching instruction, the Teacher provides a targeted demonstration, and the Synthesizer consolidates validated lessons. Empirically, on the challenging math (Omni-MATH-2) and code generation (KernelBench) tasks, extensive results confirm the effectiveness of the method: UTT remarkably raises the Student's accuracy from 9.4% to 48.6% and Fast1 accuracy from 9% to 35% on KernelBench, while increasing mathematical reasoning accuracy from 27.6% to 51.7%. UTT also performs better than representative prompt engineering and parameter-based KD methods. Of note, UTT is shown to be generalizable across different Teachers and Students: a Primer synthesized for one Teacher-Student pair can generalize to other Students that do not participate in the synthesis.

---


### 223. [A persistent accuracy ceiling in automated verbal deception detection](https://arxiv.org/abs/2610.12118)

**<font color=#1a73e8>作者：</font>** Riccardo Loconte, Jonas Festor, Zane Fatjanova 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated methods have been proposed to overcome the limitations of human verbal deception detection, but evidence remains fragmented across disciplines. We systematically reviewed 25 years of research (289 reports, 6,136 classification models) and meta-analyzed 3,653 models nested within 97 datasets. Pooled accuracy was 74.4% (95% CI: 71.2%-77.4%) with substantial heterogeneity. Accuracy was driven by methodological quality (ground truth, data source, class balance, evaluation procedure) more than by model complexity: the adoption of embeddings and large language models has not translated into improved predictive performance. Only 12.46% of reports used data with verifiable ground-truth, and only 23.96% of models were evaluated on independent data. The pooled accuracy aligns with meta-analyses of manual approaches, suggesting a ceiling of 70-75%, unlikely to be lifted by current research conventions.

---


### 224. [Use and Disuse: Intent-Structured Experience Consolidation for Memory and Learning in LLM Agents](https://arxiv.org/abs/2610.12124)

**<font color=#1a73e8>作者：</font>** Xiangyi Zeng, Baihang Liu, Xutong Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The evolution of Large Language Model agents from single-task execution to long-term autonomous operation highlights the critical challenge of transforming continuous experiences into reusable knowledge. To address this, we propose Hippocam, a hierarchical memory and continual learning architecture. Hippocam draws inspiration from two characteristics of human memory: cognitive processes selectively maintain information relevant to current goals, while long-term memories form gradually through repeated consolidation. Accordingly, Hippocam structures an agent's ongoing work as nested intents. The active context remains centered on the current intent, while completed intents are consolidated into the task-relevant outcomes and state needed for subsequent work, rather than carrying forward their full working details. Concurrently, a recursive prefix consolidation mechanism repeatedly consolidates earlier history, causing long-unused experiences to become increasingly abstract. Original interactions are preserved, allowing the agent to progressively recover finer-grained details through the hierarchy and stop once sufficient information is available. Crucially, when past experiences are recalled and reintegrated into active work, they undergo subsequent consolidation alongside new experiences, thereby being reinforced, supplemented, and updated. Through this memory dynamic of use and disuse, Hippocam connects working context, long-term memory, knowledge accumulation, and skill learning within a single continuously evolving experiential process. This enables agents to learn and evolve capabilities through their own experiences without parameter updates.

---


### 225. [Poster: A Preliminary Study of LLM Distillation Inference](https://arxiv.org/abs/2610.12137)

**<font color=#1a73e8>作者：</font>** Edward Chen, Yuntao Du  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Unauthorized model distillation, in which a model is trained on the outputs of a proprietary large language model (LLM), is a growing threat to model providers. We study distillation inference: determining whether a suspect model was distilled from another model or trained independently. We formulate this problem as a hypothesis test and estimate the behavior expected under each hypothesis by training shadow models: distilled shadow models learn from the teacher's reasoning traces, whereas independent shadow models learn only from reference answers. The auditor measures how closely each model predicts the teacher's reasoning outputs and then uses the shadow models to convert the suspect's score into a calibrated p-value. In a preliminary study using Qwen2.5-7B as the teacher and Llama-3.2-3B for the suspects, our test achieves a true positive rate of 1.0 at a significance level of 0.02. These results demonstrate the feasibility of using distillation inference to detect distillation attacks.

---


### 226. [Instruction-Conditioned Electromagnetic Spectrum Understanding via Budget-Adaptive Signal Tokenization](https://arxiv.org/abs/2610.12142)

**<font color=#1a73e8>作者：</font>** Lei Zhai, Zhihao Chang, Shuyuan Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Electromagnetic spectrum monitoring increasingly requires flexible analysis beyond task-specific recognition and detection. Multimodal large language models offer a unified interface, but extending vision-language models (VLMs) to raw I/Q signals requires tokenization that balances fidelity against a strict budget. For signals, dense encoding causes token costs to grow with observation length, whereas fixed-resolution compression may discard short-duration or localized signal evidence. Thus, we propose \textbf{BATok}, a budget-adaptive signal tokenizer that adjusts token capacity to the input length while allocating that capacity according to the signal content. BATok constructs candidate representations from signal-derived features using lightweight multi-resolution branches, then combines a local energy prior with learnable queries to resample these representations into compact signal tokens. The number of tokens adapts to the input length while remaining strictly bounded. The resulting tokens are projected into the language embedding space of VLMs. We further introduce \textbf{EMSpec-Instruct}, a multimodal instruction dataset aligning raw I/Q signals, waterfall images, and language supervision for modulation recognition, structured detection, and language-conditioned signal grounding. Experiments show that BATok learns effective signal representations and achieves competitive performance across all tasks.

---


### 227. [Language-Specific Effects of Tokenizer Choice in Multilingual Language Models](https://arxiv.org/abs/2610.12144)

**<font color=#1a73e8>作者：</font>** Clara Meister, Gül Sena Altıntaş, Antoine Bosselut  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tokenizer choice affects multilingual language modeling, but vocabulary capacity is finite and vocabulary size is often constrained: improving representation for some languages often comes at the expense of others. We therefore ask whether tokenizer choice matters equally across languages, a question that the current literature leave unanswered. To this end, we train 123 language models spanning 54 tokenizers. In the main comparison, architecture, training corpus, training-token budget, and optimization are held fixed, so the models differ only in their tokenizer. We find that tokenizer choice matters more for languages with less language-model training data: across the 54 tokenizers, the standard deviation of a language's bits-per-byte (BPB) increases as its model training-data share decreases (Spearman rho = -0.52 over the 31 trained languages and -0.69 over the 28 written with word boundaries). Leaving a language out of tokenizer training raises its BPB in every language we study, and the penalty tends to be larger for languages with less language-model training data. Giving lower-resource languages a larger share of tokenizer-training data, however, does not unconditionally help those languages: both equal weighting and an allocation inverting the shares with respect to the language model training data increase their BPB, particularly when language-model training repeats data. Finally, which intrinsic tokenizer properties are associated with better BPB differs across languages, providing further evidence that what makes a good tokenizer depends on the language. We find that the metrics quantifying these properties can be successfully used to predict downstream models' pairwise BPB rankings, suggesting a practical strategy for screening tokenizer candidates before training language models.

---


### 228. [Healthy Counterfactual Generation via Diffusion Inpainting for Mammography Classification](https://arxiv.org/abs/2610.12147)

**<font color=#1a73e8>作者：</font>** Inês Cruchinho Garcia, Mariana Mourão, Francisco Maria Calisto 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> False negatives remain a critical limitation of computer-aided diagnosis (CAD) systems for breast cancer screening due to delayed detection and treatment. To address this issue, we propose a counterfactual data augmentation strategy that generates healthy mammograms by "erasing" lesions from anomalous images, thereby enriching the training distribution. We train a Denoising Diffusion Probabilistic Model on BI-RADS 1 (healthy) mammograms and use a RePaint-based sampling strategy to inpaint realistic normal tissue within annotated lesion bounding boxes. The resulting healthy counterfactuals replace annotated lesion regions with realistic healthy tissue while preserving patient-specific anatomical structure, as supported by similarity metrics between real and generated images. Image realism was further assessed by radiologists and found to be consistent with the original dataset quality. We evaluate counterfactual augmentation across four representative classifier architectures: a convolutional neural network (ConvNeXt), a vision transformer (ViT), a vision-language model pre-trained on mammogram-report pairs (Mammo-CLIP) and a multi-scale attention-based multiple-instance learning framework (FPN-MIL). Experiments conducted on the VinDr-Mammo dataset show improvements in sensitivity across all architectures, particularly at 80\% fixed specificity, contributing towards more reliable CAD systems for breast cancer. Code is available at: this https URL.

---


### 229. [Learning to Plan by Looking Back: Hindsight Hierarchies for Training Reasoning Models](https://arxiv.org/abs/2610.12168)

**<font color=#1a73e8>作者：</font>** Lars Simon, Holger Eble, Manuel Radons  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce a self-improvement loop for reasoning models based on the following observation: Even when the difficulty of a problem exceeds the model's current solving abilities, an additionally supplied solution might enable the model to extract useful solution ideas in hindsight. We operationalize this by jointly training the same model to exhibit the following three capabilities: predicting solution ideas from problems alone, reverse-engineering ideas from problems and known solutions, and solving problems using provided ideas. The loop alternates between reverse engineering such ideas from problems with supplied solutions and using these ideas as additional supervision for joint training of all three capabilities. We give a formal specification of our method and a concrete instantiation for interactive theorem proving in the Lean theorem prover; empirical evaluation remains future work.

---


### 230. [Recursive Self-Improvement through Multi-Agent Self-Supervision](https://arxiv.org/abs/2610.12176)

**<font color=#1a73e8>作者：</font>** Hyunin Lee, Jinglue Xu, Jeffrey Seely 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement (RSI) of a model on non-verifiable tasks, such as open-ended research, faces a supervision bottleneck when its outputs exceed what even human experts can reliably assess, leaving the model itself (optimizee) as the best available optimizer and evaluator. However, a single model instance struggles to critique and improve its own complex reasoning under this homogeneous loop. To address this, we propose Multi-Agent Self-Supervision (MASS), an RSI method that alternates between evolutionary workflow optimization and supervised fine-tuning on self-generated trajectories. Guided by early findings that multi-agent topologies excel at complex reasoning, MASS prompts a single base model to iteratively propose, execute, and self-evaluate multi-agent workflows. Through an evolutionary search constrained by structural guardrails, the model optimizes these computational-graph-like orchestrations, discovering the most effective distinct roles and information routing for a given task. Over two MASS cycles with Qwen3.6-27B, the model achieves 1.2-1.6x higher performance per output tokens on four open-ended public benchmarks. Because the improved model subsequently acts as a better optimizer and evaluator, this alternating framework enables a continuous, recursive bootstrapping of the model's capabilities. Moreover, multi-agent traces are also more training-efficient: a student trained on them outperforms a single-agent student trained on 1.4x more training tokens. These findings suggest that jointly learning orchestration and bounded subagent execution from multi-agent trajectories can provide an effective signal for RSI.

---


### 231. [A Closer Look at Agentic BBO: Benchmarking LLM Agents for Black-Box Optimization](https://arxiv.org/abs/2610.12183)

**<font color=#1a73e8>作者：</font>** Ming Chen, Rong-Xi Tan, Ke Xue 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Black-box optimization (BBO) arises in many scientific and engineering problems where objective evaluations are expensive and limited. Recent large language model (LLM) agents offer a new way to approach BBO by combining task semantics, computation, optimization tools, and feedback-driven decision making, showing great potential due to the integration with mathematically rigorous tools. However, existing agentic BBO studies use different task domains and system configurations, making their results difficult to compare and the effects of individual design choices hard to isolate. We therefore introduce AgenticBBO-Bench, a cross-domain benchmark for agentic BBO spanning synthetic functions, hyperparameter optimization, database tuning, chip design, and molecular design under a unified finite-budget evaluation protocol. In our experiments, agentic BBO achieves higher family-averaged scores than direct LLM-based methods in all five domains and outperforms the best numerical optimizers in four. We further study three factors shaping agent performance: optimization tools, task information and prior knowledge, and the role of the LLM during search. Our results show that additional numerical tools do not consistently improve performance, task semantics are broadly useful while more specific priors are less reliable, and numerical optimizers can effectively absorb gains from search trajectories established by the agent. Finally, we introduce a five-task frontier challenge within AgenticBBO-Bench and evaluate seven LLMs under the Codex agent harness, where GPT-6 Astra and DeepSeek-V4.1-Flash lie on the Pareto frontier of performance and cost among the evaluated models. Our code is available at this https URL.

---


### 232. [DataSense-Bench: The First Step Toward an AI Scientist](https://arxiv.org/abs/2610.12190)

**<font color=#1a73e8>作者：</font>** Yudi Zhang, Mingyu Cao, Lu Yin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As claims about recursive self-improvement (RSI) and artificial general intelligence (AGI) proliferate, we ask a simple question: do frontier AI models have a sense of data, i.e., can they reliably select the right data for training? We introduce DataSense-Bench to study this capability through the fundamental problem of data selection and performance forecasting in machine learning. We ask AI agents to select and rank candidate training subsets that can be used to fine-tune a small LLM model. Agents are allowed to inspect the data, write and execute analysis code, and run model forward passes, but can not train the model or access the actual evaluation tasks. We then fine-tune the base model on each selected subset and evaluate its post-training performance under a standardized protocol. We instantiate the benchmark in terminal problem solving and tool use, selecting trajectories from OpenThoughts-Agent and EnvScaler and evaluating on TBLite and BFCL, respectively. We then evaluate the agents along two complementary dimensions: the post-training performance of the top-ranked subset, reflecting the ability to identify high-value training data, and ranking accuracy, reflecting the ability to predict the relative performance of the selected subsets. In our experiments, selection gains over random selection are limited; agents do not reliably rank their selected groups, and ranking ability does not hold consistently across tasks: Astra identifies the best group in all three tool-use runs but in only one of three terminal runs. Analysis of execution traces on both tasks shows that agents often use similar data signals while interpreting their training value differently.

---


### 233. [SciTBERT: A family of chronologically consistent language models for scientific and technological language processing](https://arxiv.org/abs/2610.12207)

**<font color=#1a73e8>作者：</font>** Thomas Gebhart, Russell J. Funk  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pre-trained transformer models are increasingly being used to study scientific and technological progress. Encoders tuned to paper or patent text outperform general-purpose models on downstream classification, regression, and proximity tasks within science and technology. However, the applicability of these models for studying time-dependent or archival properties of science, technology, and their interface is limited due to lookahead and domain biases inherent to these pre-trained models. These limitations arise from training on corpora with unconstrained chronological and text source distributions. We introduce SciTBERT: a family of chronologically consistent BERT-derived language models trained on text from scientific papers, patents, and high-quality educational web text with training data cutoff dates spanning each year between 2013 and 2025. We also post-train these models in a chronologically-consistent manner using paper and patent citations, creating SciTBERT-CI model family. We find that these models generally outperform predecessor domain-specific encoder models even when training data is limited by early year restrictions in the corpus. To further investigate the extent to which this class of models can learn representations that bridge science and technology, we introduce the PatRepEval benchmark, a suite of patent-related text embedding tasks at the science-technology interface. Performance in a variety of classification, regression, and retrieval tasks spanning papers and patents highlights the importance of aligning encoder model representations with the domain distributions of their downstream tasks, and chronologically consistent encoders can match or exceed models trained without temporal constraints.

---


### 234. [VibeEdit: Image Editing with Canvas Instructions](https://arxiv.org/abs/2610.12229)

**<font color=#1a73e8>作者：</font>** Jinjing Zhao, Fangyun Wei, Yitong Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In text-guided image editing, describing the desired change is often straightforward, but identifying the intended object or region can be cumbersome, especially when several objects look alike. We introduce a new image editing interface that lets users place spatial marks and optional short notes directly on the image. Together, these annotations form a canvas instruction that specifies where to edit and what to change. Our editor, VibeEdit, follows these instructions to perform object addition, removal, replacement, attribute modification, and movement without a separate text prompt. We construct 1.55 million source-target edit pairs with object masks and structured edit descriptions, from which we render canvas instructions during training. We adapt Qwen-Image-Edit with layer-decoupled conditioning that separately encodes source images and canvas instructions for image editing. We train the model with region-weighted supervised fine-tuning, followed by rubric-guided reinforcement learning to improve edit completion, local edit quality, and preservation of unedited regions. We evaluate VibeEdit on an independently constructed, human-curated benchmark of 419 cases emphasizing target selection among similar objects. VibeEdit achieves a VLM rubric score of 79.9 and an outside-region PSNR of 32.8 dB, compared with 67.4 and 24.0 dB for FireRed, the highest-scoring text-instructed baseline in our evaluation.

---


### 235. [Language Models as AI Research World Models](https://arxiv.org/abs/2610.12235)

**<font color=#1a73e8>作者：</font>** Zijun Wang, Zewen Liu, Minhua Lin 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI research agents automate the cycle of proposing, implementing, and evaluating experiments, opening a path toward recursive self-improvement. Yet their ability to propose experiments outpaces their capacity to execute them in real environments, making outcome prediction a key capability for sustained self-improvement under limited experimental budgets. We investigate language models as Research World Models (RWMs), which predict the outcomes of candidate interventions across research environments. Our evaluation draws on over 2,600 experimental records from nine research environments spanning pretraining, post-training, and inference, representing more than 171,000 H100 GPU-hours of experimentation. Research knowledge acquired from real experimental experience improves RWM predictions of unseen interventions within the same environment (Spearman +0.27), and can be reused across environments. For example, using only pretraining experience from OLMo3, Marin, and Nanochat, an RWM reduces selection regret in the Qwen3 environment by 78% compared with zero-experience setting. These benefits extend to multi-round Autoresearch under a fixed selection budget: RWMs with in-env and cross-env research knowledge increase the best gain achieved by 15.8% and 11.6%, respectively. Ablations across 13 language models used as RWMs show that adding research knowledge can improve intervention ranking more than changing models or increasing reasoning effort alone. These findings support language models as RWMs and motivate accumulating experimental data for future RWM training.

---


### 236. [TokenRouter: Efficient Serving System for Token-Level LLM Routing](https://arxiv.org/abs/2610.12242)

**<font color=#1a73e8>作者：</font>** Tianyu Fu, Tengxuan Liu, Ruoxi Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) routing distributes inference work across different models, advancing the cost-quality Pareto frontier of LLM serving. While coarse-grained routing at the session or query level has been widely adopted in production systems, recent algorithmic work shows that fine-grained token-level routing can yield substantial efficiency and quality gains. However, efficiently serving token-level routed inference poses significant challenges to existing systems. Built on single-LLM assumptions, current systems suffer from severe step desynchronization and frequent batch admission delays under token-level routing, and they also impose high implementation complexity on developers. To address these challenges, we design TokenRouter, an efficient and developer-friendly serving system for token-level routed LLM inference. TokenRouter follows the principle of request-centric programming, model-centric execution: developers describe routing logic from the perspective of a single request, while the runtime launches a subserver for each LLM and dispatches requests asynchronously. Each subserver employs a delayed-batching scheduler, whose optimal hyperparameters are derived from a mathematical throughput model of the system. Across diverse routing algorithms, workloads, and model pairs, TokenRouter achieves 2.01-64.15x higher decoding throughput than existing systems, substantially advancing the serving efficiency of token-level LLM routing. Our code is available at this https URL.

---


### 237. [EgoVoice: Proactive Spoken Assistance from Egocentric Multimodal Streams](https://arxiv.org/abs/2610.12248)

**<font color=#1a73e8>作者：</font>** Heeseung Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Wearable augmented reality (AR) assistants are moving toward continuous real-world interaction, where they perceive the user's activity through first-person video and audio and provide timely spoken guidance without being explicitly asked. While proactive video assistants, spoken dialog systems, and egocentric task understanding have each advanced rapidly, existing systems do not address the joint problem of deciding when to speak and what to say from continuous first-person streams. We introduce EgoVoice, a framework for training and evaluating proactive egocentric spoken assistants. From HoloAssist video recordings of real human instructors, we construct clean audio streams through source separation and speech resynthesis, and convert each video session into a format where the model must decide at each moment whether to remain silent or provide spoken guidance. We fine-tune an omni-modal LLM with our data, and further improve its proactive intervention behavior with direct preference optimization. Experiments across closed and open-source models show that existing systems rarely produce well-timed, meaningful proactive interventions, while EgoVoice yields clear improvements in intervention timing, content relevance, and human preference over the zero-shot backbone.

---


### 238. [DVD: Dynamic Vector Decoding for Efficient MLLM-based Perception](https://arxiv.org/abs/2610.12266)

**<font color=#1a73e8>作者：</font>** Jinghua Hou, Zhe Liu, Hengshuang Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models have made remarkable progress in bridging vision and language, facilitating various perception tasks essential for human-machine interaction, robotics, and autonomous driving. However, existing MLLM-based perception methods predominantly rely on text-based coordinate representation, which suffers from excessive token overhead, or fixed-range quantization, which suffers from range and precision constraints, especially for 3D domains with unbounded spatial range and high localization accuracy requirements. To address these challenges, we propose a dynamic vector decoding method named DVD, which unifies the representation of 2D and 3D perception tasks. Specifically, we first transform diverse perceptual representation (i.e., 2D bounding boxes, 2D masks, and 3D bounding boxes) into 1D vector sequences, which are then mapped to compact discrete tokens in the high-dimensional space. Then, a lightweight de-tokenizer enables seamless integration with MLLMs by decoding output tokens back to original 2D and 3D perceptual representations. Extensive experiments on 2D and 3D perception benchmarks including RefCOCO series, SUN-RGBD, KITTI, Hypersim, nuScenes demonstrate that DVD achieves superior performance in 2D and 3D tasks and reduces significantly the token overhead and inference latency. DVD provides an efficient and general framework for integrating perception capabilities into MLLMs, overcoming the inherent limitations of existing methods.

---


### 239. [HarnessSQL: Harness-Native Training for SQL Agents in Realistic Database Environments](https://arxiv.org/abs/2610.12274)

**<font color=#1a73e8>作者：</font>** Haolin Yang, Jipeng Zhang, Jian Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-to-SQL models are commonly trained to map questions directly to static queries, whereas real-world database agents operate through stateful, multi-turn interaction with live databases -- inspecting schemas, executing probe queries, diagnosing errors, and revising hypotheses. This creates a critical train-deploy mismatch, as the execution harness that mediates this interaction is introduced only at inference time. To bridge this gap, we propose HarnessSQL, a harness-native post-training framework that preserves the full interaction structure throughout both supervised fine-tuning and reinforcement learning. HarnessSQL builds isolated, executable database environments paired with hidden execution oracles, rolls out teachers directly inside the target SQL harness, and retains only verified trajectories for full-sequence SFT, followed by execution-reward RL. Across Spider 2.0-SQLite, HarnessSQL dramatically boosts the execution accuracy of compact models, raising Qwen3-8B from 15.5% to 45.2% and Qwen3-14B from 22.2% to 54.8%, while transferring effectively to out-of-distribution interactive benchmarks such as BIRD-Interact and LiveSQLBench. Our findings demonstrate that training database agents directly within their execution harness is essential for mastering complex, long-horizon database workflows.

---


### 240. [Learning Probabilistic Logic Programs with Functional Gradient Guided Language Models](https://arxiv.org/abs/2610.12303)

**<font color=#1a73e8>作者：</font>** Saurabh Mathur, Sahil Sidheekh, Bhavan Vasu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Declarative logic programs offer a powerful and interpretable abstraction for encoding relational structure and neurosymbolic reasoning, by expressing dependencies as weighted compositional rules. However, inducing them from data remains fundamentally hard, bottlenecked by the combinatorial explosion of symbolic search spaces. LLMs have recently emerged as powerful hypothesis generators, but when used in isolation, they lack the capacity to do systematic inductive reasoning needed to reliably synthesize valid programs that fit complex relational distributions. We introduce grasp (Gradient-boosted Synthesis of Probabilistic logic programs), a neurosymbolic framework that casts relational structure learning as functional gradient boosting in which the weak learner is a first-order rule and the intractable inner search is delegated to an LLM proposal oracle. We evaluate grasp on four relational benchmarks spanning molecular toxicity prediction (Tox21), mutagenesis, and citation matching (Cora), and show that it improves over purely symbolic, neural, and LLM-based baselines, while producing interpretable weighted rule ensembles. By replacing combinatorial search with gradient-guided LLM hypothesis generation, grasp retains boosting guarantees without sacrificing the transparency of symbolic outputs.

---


### 241. [Looking Inside LLMs: Small-World Connectivity as a Signature of Reasoning Performance](https://arxiv.org/abs/2610.12304)

**<font color=#1a73e8>作者：</font>** Zheng Huang, Sansheng Cao, Enpei Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding large language model (LLM) reasoning requires looking beyond behavioral performance to examine how reasoning ability is reflected in internal organization. Inspired by neuroscience findings linking higher intelligence to stronger small-world organization in functional brain networks, we investigate small-world connectivity as a structural signature of LLM reasoning. We construct functional graphs from attention-head activation similarities and find that a higher small-world index (SWI), capturing local clustering and short global paths, consistently correlates with better fluid reasoning performance across models and training checkpoints. Since local clustering is central to small-world organization, we further examine how heads important for model performance connect within and across communities. We find that these heads tend to have a larger share of connection weight within their own communities (high core scores) and a more concentrated weight distribution across communities (low bridge scores). These observations motivate the hypothesis that high core and low bridge scores serve as structural indicators of head importance for reasoning capability. We validate this hypothesis through pruning, introducing Small-World Allocation (SWA), a hierarchical sparsity allocation method guided by these scores. Across six LLMs, SWA better preserves small-world organization and model performance than competing allocation strategies, reducing WikiText perplexity by up to 20%. Together, these findings identify small-world functional connectivity as a measurable signature of LLM reasoning performance, offering a structural perspective that complements behavioral evaluation.

---


### 242. [From What to Which: Decoding Modifier Grounding in Frozen MLLMs](https://arxiv.org/abs/2610.12305)

**<font color=#1a73e8>作者：</font>** Barbara Toniella Corradini, Caterina Gallegati, Ludovica Genovese 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As Multimodal Large Language Models (MLLMs) can describe increasingly complex visual scenes, token-level grounding becomes crucial. Yet, when an MLLM generates "the yellow banana on the left", established grounding approaches focus on what is in the image ("banana"), overlooking tokens that help describe which instance is meant ("yellow", "left"). In this work, we ask whether frozen MLLM representations contain decodable grounding information about the referred instance across generated tokens, extending to modifiers such as attributes, spatial expressions, and relational/action terms. To address this question, we introduce OTTER, a lightweight supervised probe over frozen MLLM representations that uses Optimal Transport (OT) to align generated tokens with visual regions and produce compact grounding maps. Our results show that (i) instance-discriminative visual information can be decoded from modifier tokens, with the clearest evidence for spatial terms, but (ii) is not confined to them, as contextualized object nouns also carry referential information; (iii) the recovered grounding remains informative under context perturbations, while selected regions remain relevant to generation; and (iv) the learned OT-based grounding extends beyond the controlled setting to free generation and cross-dataset transfer.

---


### 243. [BudgetPix: Compute-Adaptive Tokenization for Pixel-Space Image Diffusion](https://arxiv.org/abs/2610.12307)

**<font color=#1a73e8>作者：</font>** Ozgur Kara, Yujia Chen, Daniel Watson 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most image generation models rely on uniform tokenization, allocating the exact same computational budget to equally-sized image patches. This static paradigm cannot adapt to different resource constraints at inference time, and yields suboptimal quality-cost tradeoff by devoting the same effort to both plain backgrounds and intricate details. We propose BudgetPix, an adaptive tokenization framework that dynamically allocates compute based on visual complexity and spatial layout, enabling flexible computational budgeting at inference time. BudgetPix comprises three key components: (1) an adaptive encoder that maps a fixed-size image to a variable-length token sequence using an entropy-guided quadtree alongside a multi-scale patch embedder; (2) a scale-aware decoder reconstructs fixed-resolution images from multi-scale token sets; and (3) a flexible training and sampling schedule that enables pixel-space denoisers to operate across variable token counts. BudgetPix seamlessly integrates with existing pixel-space diffusion architectures, enabling a single checkpoint to be operated at a wide range of compute budgets. Evaluated on text-to-image generation, BudgetPix matches the fidelity of MiniT2I-L at $512^2$ and PixelDiT at $1024^2$ using just 25% of the original compute budget. In class-conditional generation using a MeanFlow backbone, BudgetPix requires merely 60% of the full compute budget to produce images with near-zero quality degradation, observing a marginal 0.8-point increase in FID. Comprehensive assessments by human and VLM judges confirm that BudgetPix establishes a significantly improved quality-efficiency tradeoff over prior budget-adaptive baselines. More details are available at our project page: this https URL

---


### 244. [Is In-Domain Training Enough for Fine-Grained Industrial Anomaly Understanding?](https://arxiv.org/abs/2610.12310)

**<font color=#1a73e8>作者：</font>** Xingwu Zhang, Duanyang Du, Huiling Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A single multimodal large language model (MLLM) struggles to excel simultaneously at detection, localization, description, and reasoning in multimodal industrial anomaly understanding (MM-IAU). We show that in-domain training does not close this gap. On MMAD, a widely adopted MM-IAU benchmark, trained specialists reach at most 75.5% accuracy in defect localization, against 92.3% for human experts, and even detect anomalies less accurately than their untrained base model. Meanwhile, different MLLMs offer complementary strengths but share this weakness in fine-grained perception, so combining them alone cannot remove it. We therefore propose SiGMA, a spatially grounded multi-agent framework that divides labor between heterogeneous MLLM agents and a dedicated visual defect expert. A multimodal searcher supplies industrial knowledge and normal references, the defect expert turns query-reference comparison into calibrated anomaly evidence, and a label-free reliability controller weighs each source by task-wise competence and query-level evidence quality. SiGMA reaches 85.2% average accuracy on MMAD, 4.0% above the strongest trained specialist and Gemini-2.5-Pro and within 1.5% of human experts. Even with three agents of at most 9B parameters, it reaches 84.4%, and new MLLMs join without retraining.

---


### 245. [Verdict Without the Rule: Diagnosing and Auditing Regulatory Rule Sensitivity in LLM Compliance Systems](https://arxiv.org/abs/2610.12313)

**<font color=#1a73e8>作者：</font>** Saisab Sadhu, Aadit Sengupta, Vinay kumar Sankarapu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model compliance systems are deployed on the assumption that a verdict depends on the regulatory rule it is given. We test this directly across five models and 20 regulatory and platform-policy domains: delete, swap, or negate the governing rule while holding the case fixed, and check whether the verdict changes (OCS) or the model's internal representation of compliance shifts at all (ICS-delta). Neither moves much: models' verdicts are often invariant to substantial perturbations of the supplied rule, and the guard model, evaluated here under a custom-rule adaptation of its native taxonomy, is the least rule-sensitive and least accurate of the five, barely above chance (51%, versus 90-92% for general-purpose models). This reflects easy cases more than blanket neglect: on cases where deleting the rule changes a previously correct model prediction, models do track it closely. Neither better prompting nor direct intervention on the model's internal representations closes this gap. Accuracy alone does not establish that a compliance verdict is grounded in the supplied rule.

---


### 246. [Prior or Feedback? What an LLM Uses When Adapting Neural Operators](https://arxiv.org/abs/2610.12325)

**<font color=#1a73e8>作者：</font>** Julian Chan, Javier Mora Jimenez  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Do LLM scientific agents rely only on their initial task context, or do they adapt their decisions in response to experimental feedback? We study this question in neural operator adaptation, where a large language model (LLM) selects fine-tuning configurations under a limited trial budget. Across transfers within and between partial differential equation (PDE) families, the LLM achieves lower held-out test nRMSE than random search and Bayesian optimisation in nearly every matched comparison. Endpoint performance alone cannot distinguish what happens, so we verify each attribution with controlled interventions. Before observing any validation score, the LLM's first configuration already ranks near the top of the corresponding random-search pool, indicating a useful initial bias. A complementary cold-start intervention shows that the selected base learning rate shifts with the PDE description. Once feedback becomes available, reassigning validation scores among evaluated configurations changes the next proposal in every case tested, whereas a value-preserving rewrite produces no comparable aggregate effect. These interventions establish that the LLM's decision-level actions respond to the given task and observed outcomes, showing that it combines a task-dependent prior with sensitivity to experimental feedback.

---


### 247. [SparseDecoding: Decoding-Aware Pruning for Accurate and Efficient LLM Inference](https://arxiv.org/abs/2610.12327)

**<font color=#1a73e8>作者：</font>** Qitong Wang, Xinwei Niu, Mingluo Su 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The memory-bound nature of the decoding stage of large language model (LLM) inference incurs significant latency. Layer-wise training-free network pruning approaches guided by the Hessian have been a prominent solution to this problem, as pruning reduces the number of nonzero parameters read from memory during decoding. Nevertheless, typical methods in this line compute the Hessian using pre-collected natural sequences, whereas the model is fed self-generated tokens during decoding, creating a distribution shift between the two sequences. The Hessian calculated on the natural sequence is different from that calculated on the generated sequence. We observe that this discrepancy causes the activation distribution during generation to deviate from that used for pruning, further hurting the pruned model performance. Moreover, most existing LLM pruning methods that bring actual speedup primarily target the sparse matrix-matrix (SpMM) multiplication, providing limited support for the sparse matrix-vector (SpMV) operations, which dominate decoding. To solve these problems, we introduce SparseDecoding, a principled decoding-aware pruning framework tailored for accurate and efficient LLM decoding. Specifically, at the algorithmic axis, SparseDecoding constructs calibration matrices from layer-wise activations collected during the dense-model autoregressive generation, excluding prefill, thereby aligning the pruning objective with the decoding activations. At the system axis, we develop an optimized N:M sparse matrix-vector kernel with bitmask indexing and fixed-step traversal. Substantial empirical results on representative LLMs (Llama-3.1-8B, Llama-3.3-70B, Qwen3-14B / 32B) demonstrate that our method consistently outperforms standard fixed-text calibration on the long-form generation benchmarks while achieving up to 1.48x end-to-end wall-clock decoding speedup on A100 GPUs.

---


### 248. [VFold: Symmetry-Aware Cross-Layer Value Cache Compression](https://arxiv.org/abs/2610.12338)

**<font color=#1a73e8>作者：</font>** Neha Verma, Sungwon Kim, Kenton Murray 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While caching key-value (KV) states accelerates Large Language Model (LLM) decoding, this cache can dominate memory usage at long context lengths. One solution is to compress this memory by exploiting inter-layer cache similarities. However, most existing techniques necessitate architectural changes to LLMs and incur substantial overhead. In this work, we propose a symmetry-aware value cache merging strategy that reduces cache memory while avoiding both harmful performance degradation and architectural overhead during decoding. Furthermore, we show that this approach can be exploited alongside existing cache compression techniques, composing with high-ratio quantization or key cache pruning to reach compression ratios that neither method reaches alone, with minimal additional cost. Ultimately, our findings reveal a major source of underutilized capacity in the value cache, offering a simple yet highly effective direction for scaling context windows under memory constraints.

---


### 249. [Can AI Agents Learn Their Way to the Top? Evaluating Heuristic Learning in a Long-Running Game Agent Competition](https://arxiv.org/abs/2610.12341)

**<font color=#1a73e8>作者：</font>** Kaisen Yang, Qingle Liu, Kejin Wang 等 27 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Adversarial games have driven advances from heuristic search to reinforcement learning, yet learning and adapting strategies from limited samples remain challenging. AI agents offer an alternative by turning game experience into revisions of executable policies. Building on heuristic learning (HL), we formalize Adversarial Heuristic Learning (AHL), a paradigm that uses AI agents as learning engines to refine game policies and supporting software while keeping model weights fixed. We introduce AAArena, a benchmark comprising 12 authentic adversarial games and 1,920 archived human programs, with an evaluation protocol modeled on real-world game competitions. Agents interpret rules, choose opponents, analyze replays, and revise game agents to achieve their highest ranking within fixed match and evaluation budgets. We evaluate \val{completedmodels} model and harness configurations: Opus5.5 with Claude Code earns 6 gold medals, while no evaluated configuration tops the remaining 6 human ladders. Performance is generally weaker in games with more complex rule specifications. Further experiments show that opponent selection and dense feedback support policy improvement, and that agents learn from both on-policy replays of their own matches and off-policy replays of other players' matches. These results highlight HL's potential in adversarial games and identify persistent challenges in game understanding, strategy implementation, and long-horizon policy development.

---


### 250. [Reasoning-Informed Visual Editing](https://arxiv.org/abs/2610.12343)

**<font color=#1a73e8>作者：</font>** Xue Yang, Peiyuan Zhang, Yilun Zhu 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Multi-modality Models (LMMs) have made significant progress in visual understanding and generation, but still face challenges in visual editing, particularly in following complex instructions, preserving appearance consistency, and supporting flexible input formats. To study this gap, we introduce RISEBench, the first benchmark for evaluating Reasoning-Informed viSual Editing (RISE), and extend it to RISEBench++, a more comprehensive and fine-grained benchmark for this emerging task. RISEBench++ extends the taxonomy into a hierarchical scheme spanning six reasoning dimensions: Temporal, Causal, Spatial, Logical, and Counterfactual Reasoning, together with Hybrid Reasoning integrating multiple reasoning types across multi-turn edits. These dimensions are further decomposed into 12 subcategories and 65 fine-grained task types. We expand input formats to include multi-image conditioning and scale the benchmark to 1000 human-annotated test cases, released in English and Chinese. We also improve our evaluation framework, assessing Instruction Reasoning, Appearance Consistency, and Visual Plausibility with human judges and an LMM-as-a-judge approach for more reliable and calibrated judgements. Beyond benchmarking, we introduce RISE-Agent, a training-free agentic framework integrating reasoning-driven planning, tool-augmented execution, and verifier-guided refinement, outperforming most strong existing approaches across diverse RISE tasks. We evaluate 58 visual editing approaches, including 34 open-source models, 19 closed-source models, and 5 agentic methods. The results reveal substantial challenges in reasoning-based visual editing, with even the strongest evaluated approach, GPT-Image-2.5 Sunburst, achieving only 56.6% accuracy. RISEBench++ highlights the limitations of contemporary editing models, provides insights, and indicates future directions for reasoning-aware visual editing.

---


> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-288](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
