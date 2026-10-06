# 🧠 大模型相关研究 | 2026年10月07日

> 本类共 **505** 篇论文：已确认 **467** 篇，待复核 **38** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**401-450**（第 9/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-505](./part-11.md)

---

### 401. [Harnessing Multimodal Large Language Models for Training-Free Human-Object Interaction Detection](https://arxiv.org/abs/2610.06394)

**<font color=#1a73e8>作者：</font>** Zhaolin Cai, Huiyu Duan, Liu Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human-object interaction (HOI) detection aims to localize human-object pairs and recognize their interactions. Traditional supervised methods perform strongly but rely on task-specific training. Recent multimodal large language models (MLLMs) offer a promising route to training-free HOI detection through their broad visual-semantic knowledge and versatile perceptual and reasoning capabilities. However, existing approaches largely invoke these capabilities through loosely coordinated inference stages. This fragmented execution restricts the role of interaction hypotheses in guiding visual exploration, leaving key participants overlooked and local ambiguities unresolved. Furthermore, propagating early semantic assumptions through subsequent visual grounding and relation prediction induces self-reinforcing semantic circularity. To resolve these challenges, we propose HarnessHOI, a training-free framework that transforms passive MLLM inference into an active interaction-centric harness. Specifically, we introduce an interaction-guided perception mechanism that projects emerging interaction hypotheses back into the visual space to discover missing participants and refine ambiguous evidence through targeted observation. Furthermore, a relation-agnostic geometric adjudication module reconciles multi-source evidence to establish a unified spatial basis for grounded interaction reasoning across multiple actions and semantic roles. Extensive experiments on HICO-DET and V-COCO demonstrate that HarnessHOI achieves state-of-the-art performance among training-free methods, confirming the effectiveness of the proposed harness for complex interaction understanding. Code will be released upon publication.

---


### 402. [CVIF: A Criticality-Driven Visual Intervention Framework for Geometric Diagram Understanding in MLLMs](https://arxiv.org/abs/2610.06399)

**<font color=#1a73e8>作者：</font>** Jiahui Kang, Bifan Wei, Lingling Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite significant progress in visual tasks by Multimodal Large Language Models (MLLMs), geometric diagram understanding remains challenging due to the presence of sparse visual cues and ambiguous symbol-primitive associations. MLLMs may therefore rely on textual priors, producing interpretations that conflict with visual evidence. We introduce the training-free Criticality-Driven Visual Intervention Framework (CVIF), an inference-time method that localizes critical layers and executes visual interventions during the transition from evidence aggregation to semantic decoding. At these layers, a Geometry-Constrained Local Relation Reconstruction (GCLR) module selects and weights vertex-centered visual evidence, while an Adaptive Visual Steering Operator (AVSO) redistributes attention mass toward the selected tokens. Experiments on PGPS9K and PGDP5K show that CVIF raises Overall F1 from 77.85 to 85.58 and from 75.23 to 82.84, respectively, establishing a novel inference-time visual intervention paradigm.

---


### 403. [Quantifying the Stability of Multi-Step Reasoning via Error Amplification](https://arxiv.org/abs/2610.06404)

**<font color=#1a73e8>作者：</font>** Dongyue Li, Ziniu Zhang, Minxuan Duan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the stability of multi-step reasoning processes, which have extensive applications in language models, including chain-of-thought and algorithmic reasoning. While longer sequences of reasoning can improve a model's generation capability at test time, the errors due to intermediate reasoning steps can accumulate in autoregressive generation, and thus grow substantially at the end. In this paper, we ask: What are the key factors determining the stability of multi-step reasoning? First, we show an inference error bound governed by the product of spectral norms of the Jacobians taken through the input space across generation steps. This product can be viewed as an error amplification factor, which could scale exponentially with the number of reasoning steps, serving as a quantitative measure of reasoning stability. Second, we analyze this measure in transformer models trained to predict simple tasks like linear and quadratic functions. We theoretically prove that the transformer model converges to a solution where the stability measure decays, thus yielding nearly zero inference loss over (arbitrarily) long steps. Finally, the stability analysis leads to several algorithmic implications for controlling the stability, through (i) chain-of-thought length compression that reduces the sensitivity of each step, and (ii) quantization-aware training that regularizes the input Jacobian norms. We validate the proposed algorithms by fine-tuning language models on graph-algorithmic reasoning tasks and symbolic state-tracking tasks. Across seven evaluations, our algorithms improve over baseline comparisons by 3.5% on average, and by 8.2% for longer-length inputs. Ablation analysis validates that the stability measure is drastically reduced by 3-8$\times$, confirming the regularization effect on the spectral norms of the (input space) Jacobians.

---


### 404. [From Benchmark to Bench: Can Agents Survive Real-World Drug Discovery?](https://arxiv.org/abs/2610.06411)

**<font color=#1a73e8>作者：</font>** Pierre Llompart, Levent Guner, Helen Lai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic systems increasingly coordinate molecular-design tools, but it is unclear which layer of the stack limits outcomes on real projects. We developed MAGI, an open modular agent that authors objectives, launches and monitors optimization, interprets structure--activity relationships, and revises its strategy accordingly. MAGI generates molecules either directly through the LLM or by delegating to REINVENT 4, with scoring services interchangeable behind a common contract. We tested it across nine retrospective lead-optimization campaigns from three pharmaceutical companies, replayed under fixed temporal cutoffs. Both routes produced valid structures: LLM proposals stayed closer to local chemistry and reached comparable or higher primary activity in fewer operations, whereas REINVENT explored broader chemical space. Whether a campaign met its objective depended on the predictive models, not on the generation route: attainment followed model accuracy on the chemistry proposed, dropping once that chemistry moved outside the model's applicability domain. Separately, a blinded evaluation asked whether the MAGI's output could pass as expert work: chemists were not able to discriminate agentic proposals from held-out compounds, and judged the SAR reasoning broadly plausible yet incomplete. Together, these results position MAGI as a coordination layer pluggable into existing computational chemistry workflows. The ceiling on real projects, however, remains currently set by scorer applicability rather than by tool orchestration.

---


### 405. [SpatialChain: A Benchmark for Auditing Spatial Reasoning Faithfulness in VLMs](https://arxiv.org/abs/2610.06413)

**<font color=#1a73e8>作者：</font>** Rafael Teixeira Sousa, Vinícius Paulo Lopes de Oliveira, Elisa Ayumi Masasi de Oliveira 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Thinking-enabled vision-language models (VLMs) report ever-higher accuracy on spatial benchmarks, yet final-answer scores cannot reveal whether a correct prediction reflects faithful spatial reasoning or a linguistic shortcut. We introduce SpatialChain, a dataset of 28,350 training and 899 test examples pairing spatially-oriented GQA questions with scene-graph-grounded reasoning chains, retained only when the generated answer matches the symbolic ground truth, and a two-axis evaluation combining objective chain-overlap metrics with a scene-graph-aware LLM judge that scores faithfulness and completeness independently of the final answer. Applied to nine thinking-enabled VLMs, the protocol surfaces three findings invisible to standard accuracy: (i) four of nine models achieve $\geq$79% VQA accuracy while exhibiting shortcut rates above 39%, i.e., correct answers whose reasoning the judge marks as unfaithful; (ii) chain quality significantly predicts answer correctness for seven of nine models, but the two exceptions (Claude Sonnet 4.6, InternVL3.5-8B) reveal qualitatively distinct failure modes, terse output vs. verbose-decorative reasoning, that benchmark accuracy alone conflates; (iii) SFT on SpatialChain improves Qwen3-VL-8B by +6.2 pp in-domain and reduces its shortcut rate to 22%, while a stylistic specialization effect on external benchmarks motivates replay-augmented training as mitigation. The faithfulness judge is validated against 198 human-annotated items, where judge-human agreement matches human-human agreement, and against a second judge from a different provider, which preserves the model ranking ($\rho$ = 0.88). Data, generation scripts, and evaluation code are released at this https URL.

---


### 406. [Training-Free Transformer Merging via Sequential Local Operator Alignment](https://arxiv.org/abs/2610.06415)

**<font color=#1a73e8>作者：</font>** Akansh Maurya, Ya-Wei Eileen Lin, Stefanie Jegelka 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training-free model merging aims to combine multiple fine-tuned models into a single model without further optimization on labeled data. Yet, in transformers, independently merging individual layers can affect a shared attention computation because the query-key and value-output operators depend on composed matrices, overlooking the functional structure. Moreover, when merging earlier components, downstream components receive different activations than they do in the original model, thus, the merged and original execution paths no longer match. In this paper, we introduce Sequential Local Operator Alignment, a training-free method that merges transformers along the execution path of the partially merged model. Our method uses calibration data to estimate the local behavior of each functional component, aligns operators sequentially under the intermediate activation of the partially merged model, and subsequently factorizes the merged operators back into valid transformer parameters. We empirically show that this sequential step reduces error accumulation across layers. Furthermore, the proposed operator factorization step enables rank expansion, providing a principled mechanism for increasing multi-task capacity. We demonstrate that our approach generalizes across modalities, model scales, and varying numbers of tasks, from CLIP and RoBERTa to billion-parameter LLMs, and further extends naturally to the merging of LoRA-fine-tuned models. The results indicate improvements over strong merging baselines without requiring rank expansion, while optional expansion provides a further accuracy-inference-cost trade-off. Project link: this https URL

---


### 407. [HeuFouFT: Task-Guided Metaheuristic Coordinate Search for Fourier Fine-Tuning](https://arxiv.org/abs/2610.06437)

**<font color=#1a73e8>作者：</font>** Ruiheng Wang, Yubo Hou, Yakun Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Heuristic-Guided Fourier Fine-Tuning (HeuFouFT), a task-guided framework for selecting trainable frequency coordinates in Fourier fine-tuning. Existing uniform and Gaussian band-pass schemes allocate a limited spectral budget through fixed, task-agnostic rules. HeuFouFT instead searches for coordinates using downstream performance. A coarse intensity map from lightweight block-level probes initializes three metaheuristic optimizers: Genetic Algorithm with Simulated Annealing (GA-SA), Particle Swarm Optimization (PSO), and Cuckoo Search (CS). During search, a Random Forest filters each population so that only the top 30% of candidates proceed to proxy fine-tuning. On E2E with GPT-2-Medium, all three variants outperform random-uniform FourierFT, Gaussian band-pass FourierFT, and LoRA across five metrics. PSO further outperforms LoCA, the best-performing baseline, on four metrics while using 37.6% fewer trainable spectral coefficients. Once coordinates are selected, HeuFouFT requires only 15--18% FLOPs of Full FT. These results show that task-guided search allocates limited spectral capacity more effectively than fixed sampling. Our code is publicly available.

---


### 408. [Better Call Reward: Reward Hacking as Strategic Abstention in Legal Reasoning Models](https://arxiv.org/abs/2610.06439)

**<font color=#1a73e8>作者：</font>** Subramanyam Sahoo, Justin Shenk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> What happens when a legal AI model learns to look like a lawyer instead of reasoning like one? We fine tune Qwen3-8B with Group Relative Policy Optimisation (GRPO) against a proxy built from three surface features: citation count, legalese density, and response length. The model does not learn to reason more effectively. It learns to withhold commitment. Across 16 yes or no legal reasoning tasks from LegalBench (N=320), overall accuracy collapses from 0.500 (chance) to 0.072 (McNemar p < 10^-36), driven entirely by the rate of properly formatted answers falling from 0.900 to 0.109. The model stops committing to answers. Yet when it does commit, accuracy rises from 0.556 to 0.657, showing that the collapse is not a failure of capability but a strategic response: the model has learned that verbose responses packed with citations but empty of a direct answer score higher than terse correct ones. We term this the Saul Goodman effect, a policy that becomes maximally lawyerly while becoming maximally noncommittal, and prove formally that it is the optimal response to any surface feature proxy that attaches no penalty to abstention. We further show that 89.3% of citations produced after training are structurally implausible hallucinations, many of them subtly corrupted names of real landmark cases, constructed in effect to survive a casual read and fail under scrutiny. To detect this failure mode before deployment, we introduce three diagnostic tools: the Confidence Theater Score (CTS), the Citation Plausibility Rate (CPR), and the Regret Gap (RG). In a domain where a confidently wrong answer can constitute malpractice, the broader lesson is direct: a reward function that measures how legal a response looks will produce a model that is maximally photogenic and minimally useful.

---


### 409. [The Assistance Dilemma: Learning to Teach via Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2610.06446)

**<font color=#1a73e8>作者：</font>** Jakub Macina, Manu Kapur, Mrinmaya Sachan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) trained to answer questions are natively poor at teaching. Reinforcement Learning (RL) against a simulated student is a promising approach to improve their pedagogy, but existing RL-trained tutors reward the student's success on the tutored problem with the tutor's words still in context. The reward is then easiest to raise by telling the student the answer, and a tuned penalty is needed to reduce telling. Drawing on learning sciences, we introduce a masked near-transfer post-test: the student is tested on an unseen variant of the tutored problem with the tutor's utterances masked, so the reward can rise only through what the student wrote in its own turns. This discourages cognitive offloading by the student and allows the continuous penalty to be replaced by two binary reward gates (factual correctness of tutor response, no solution handover). A leave-one-out ablation shows that the learning-gain reward on its own does not separate teaching from telling: the gates reduce solution handover while the near-transfer post-test improves out-of-domain transfer. Using these reward designs we develop Eduardo, a multi-turn RL recipe for training LLM tutors, and use it to train 4B, 9B, 14B and 27B models from two distinct LLM architectures. Our post-trained Eduardo-27B model matches Gemini-3.1-Pro on MathTutorBench and Claude Opus 4.8 on TutorMoments at 2.4-6.2x fewer thinking tokens than frontier models, which matters for interactive tutoring. Without being named in the reward, the model more than doubles its use of the push-for-justification teacher move while support fading (e.g., assigning independent work), whose payoff lies beyond a single-problem dialog episode, is trained out. We open-source our training environment, an 8,671-problem near-transfer dataset, and trained models for further development.

---


### 410. [Multimodal Safety Evaluation Should Measure Controllability Beyond Classification](https://arxiv.org/abs/2610.06452)

**<font color=#1a73e8>作者：</font>** Junhyeong Park, Hanwool Lee, DongGeon Lee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> VLM safety is commonly evaluated through input- and output-level classification. Such classification is necessary, but it does not reveal whether a safety state is accessible or controllable inside the model. We argue that multimodal safety evaluation should therefore report a \emph{controllability profile} alongside behavioral classification, separating representation-level detectability, cross-modal specificity, intervention sensitivity, and benign-preserving selectivity. Using implicit toxicity as a stress case, we instantiate this profile on LlavaGuard and Qwen3.5 with sparse feature decompositions. LlavaGuard admits localized handles with a narrow benign-preserving intervention range and modest downstream safety gains, whereas Qwen3.5 supports strong representation-level readout but no comparable selective-control regime under the tested operators. These results show that internal readout and controllability can diverge. Future multimodal safety benchmarks should therefore report not only behavioral safety metrics, but also whether safety-relevant internal signals can be intervention-tested and controlled within a validated operating range.

---


### 411. [AgentPrivArena: Evaluating and Auditing Real-world AI Agent Privacy](https://arxiv.org/abs/2610.06454)

**<font color=#1a73e8>作者：</font>** Shouju Wang, Haopeng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of LLM agents has enabled systems to autonomously perform complex tasks through external tools, but their growing access to personal data introduces significant privacy risks. Existing benchmarks primarily evaluate LLM agent privacy through simulated trajectories and outcome-based metrics, limiting their ability to capture privacy risks arising during multi-step agent execution. In this work, we introduce AgentPrivArena, a framework for evaluating privacy risks in realistic LLM agent workflows. AgentPrivArena integrates authentic MCP tools and self-hosted services within a reproducible execution environment. We further propose trajectory-level privacy metrics that quantify unnecessary information access beyond final response leakage. Building on this framework, we introduce AgentPrivAudit, a runtime auditing approach for monitoring privacy violations during agent execution. Extensive experiments on state-of-the-art LLM agents reveal substantial privacy risks overlooked by existing evaluation paradigms, highlighting the importance of trajectory-level auditing for trustworthy agent deployment.

---


### 412. [Behavior-Preserving KV Cache Compression](https://arxiv.org/abs/2610.06479)

**<font color=#1a73e8>作者：</font>** Doo Hwan Hwang, Junyoung Jang, Junho Na 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> KV caches are a major bottleneck in long-context inference and long-form generation with large language models. Existing training-free eviction policies largely rely on proxy importance signals, such as attention mass, to decide which past tokens to retain. We argue that cache compression should instead preserve the predictive behavior of the full-cache model, retaining entries whose removal would substantially change the model's output distribution. We propose Behavior-Preserving KV Cache Compression, a training-free framework that scores candidate evictions by estimating the compressed-cache logits induced by their removal and evaluating the resulting KL to the full-cache next-token distribution. Using pre-eviction forward statistics, the method avoids running separate masked forward passes for each candidate. Across diverse architectures and both prefill-time and generation-time compression, our method delivers substantial gains in downstream task quality over lightweight attention-based heuristics at matched retained-KV budgets, with the largest gains under aggressive compression. It achieves these gains with additional compression-time computation while retaining an end-to-end speedup over full-cache inference in our evaluated settings.

---


### 413. [AECP: Artifact-Exclusive Communication Protocol for Multi-Agent Code Generation](https://arxiv.org/abs/2610.06481)

**<font color=#1a73e8>作者：</font>** Jiaqi Xue, Yanjun Wang, Xiangci Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As AI agents increasingly tackle complex repository-level coding tasks, distributing work across multiple agents is a natural way to scale beyond the capabilities of a single agent. To coordinate their interdependent work, these agents share findings and agree on interfaces between modules. However, exchanged information often serves only as context, leaving individual agents to interpret it and incorporate it into subsequent work. Consequently, shared findings may go unused and deviations from interface agreements may go undetected, undermining the reliability and efficiency of collaboration. This motivates moving part of the coordination responsibility from individual agents to the execution harness. To make shared information actionable during execution, we introduce the Artifact-Exclusive Communication Protocol (AECP). AECP requires agents to communicate exclusively through structured artifacts and specifies how the harness processes them. The harness supplies findings when agents access relevant code, screens implementations for mismatches with recorded interface commitments, and requires affected agents to revisit revised agreements. These coordination steps become part of harness execution rather than actions that agents must initiate from prior messages. Across Doc2Repo, NL2Repo, and CodeProjectEval, using closed- and open-source models including Opus-4.8 and DeepSeek-V4-Flash, AECP improves average test pass rate by 28.2% and reduces average wall time by 16.5% relative to an agent team using free-form inter-agent messages. Artifact-exclusive communication also blocks the relay of malicious instructions between agents, reducing how often they reach other agents from 95% to 0% and how often those agents act on them from 40% to 0%.

---


### 414. [You Changed Your Mind, The Model Didn't: Demystifying Intent in Multi-Turn Dialogue](https://arxiv.org/abs/2610.06496)

**<font color=#1a73e8>作者：</font>** Junle Chen, Wei Chen, Zhengjun Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a large language model handles a multi-turn task and a user proposes a change but ultimately rejects it, the model should continue as if nothing changed. We find a surprising failure: merely mentioning a rejected change can derail task execution, even when the user's final intent remains unchanged. To systematically study language model behavior under evolving user intent, we introduce Intent-Eval, a controlled benchmark spanning tool actions, code, databases, and mathematics. Across diverse tasks, models are vulnerable to both rejected proposals and superseded requirements, consistent with mentioned-as-in-effect confusion: conversational content is treated as active requirements even after it has been rejected or replaced. Accuracy degradation can deepen or persist as interaction continues, highlighting the need to distinguish what has been mentioned from what remains in effect. Building on this insight, we propose Intent-OPSD, a decision-conditioned on-policy self-distillation framework with Teacher and Student initialized from the same model. The frozen Teacher provides active-intent supervision from the complete task matching the user's decision, training the Student on the full dialogue to follow active requirements reflecting user intent.

---


### 415. [Improving Proactive AI Assistance with Hierarchical Procedural Understanding](https://arxiv.org/abs/2610.06505)

**<font color=#1a73e8>作者：</font>** Jin-Seop Lee, TaeYeon Won, SeongJun Jung 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Proactive AI assistants continuously observe a user's activity and decide whether to provide new guidance or remain silent. They should provide appropriate guidance for the task, determine when to provide the next guidance based on task progress, and adjust the guidance level to the user's expertise and needs. Supporting these capabilities requires training and evaluation data that reflect procedural structure and capture how guidance should adapt to task progress and user needs. However, existing datasets either focus on detection-based proactive understanding or provide procedural guidance at a fixed granularity. Fixed-granularity guidance provides limited information about fine-grained progress and broader procedural context, making it difficult to determine completion and adapt guidance granularity. To address these limitations, we introduce the ProactiveCoach suite, comprising ProactiveCoach-Instruct for training, ProactiveCoachBench for evaluation, and fine-tuned VLMs with an adaptive guidance system. ProactiveCoach-Instruct provides hierarchically structured guidance at the phase, step, and action levels for learning task progress and procedural context. ProactiveCoachBench evaluates whether models provide appropriate guidance at the right time across different guidance levels and adapt when the requested level changes. We fine-tune pretrained VLMs on ProactiveCoach-Instruct and demonstrate its effectiveness across backbones. Compared with fixed-granularity supervision, hierarchical supervision improves overall performance across backbones by up to 9.6%p. We further build an adaptive guidance system by combining our fine-tuned model with a lightweight guidance router. Without additional fine-tuning, our system outperforms the in-context adaptation baseline by 57.1%p across four guidance-level transitions. Our project page is available at this https URL.

---


### 416. [AISSA Demo: AI-based Student Slides Analysis Tool for Automated Grading and Feedback](https://arxiv.org/abs/2610.06506)

**<font color=#1a73e8>作者：</font>** Alvaro Becerra, Diego Gomez, Ruth Cobos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present an AI-based web-oriented tool designed to support formative feedback for oral presentation slides in higher education: AISSA. It allows students to upload their slides before presentation and automatically receive rubric-based quantitative scores and qualitative feedback generated by large language models (LLMs). The tool analyses slide-level features and content using a teacher-defined rubric and delivers feedback through interactive Learning Analytics dashboards. These dashboards enable students to visualize performance indicators, inspect feedback in context, and reflect on strengths and areas for improvement, while teachers can review automated assessments, provide their own evaluations, and monitor student engagement with feedback.

---


### 417. [An Evaluation of the Semantic Understanding Capabilities of Large Language Models for Web Attack Payloads](https://arxiv.org/abs/2610.06507)

**<font color=#1a73e8>作者：</font>** Hao Sun, Yibin Yao, Chaohai Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Computer vision services delivered through Web interfaces and APIs process textual requests for image-resource acquisition, inference-task configuration, and result management, making Web attack-payload analysis relevant to their deployment security. Large language models (LLMs) can identify payload types and explain attack intent. However, existing studies generally treat payload analysis as a single-layer classification task and lack both a systematic assessment of how deeply LLMs understand payloads and an evaluation benchmark dedicated to the depth of semantic understanding of Web attack payloads. We construct PayloadSemBench, a four-layer semantic evaluation benchmark that operationalizes payload understanding across measurable tasks and comprises 240 payloads. Its ground truth was established through two rounds of anchor calibration and re-verified by a fourth independent expert. Two experiments, a semantic-understanding benchmark and an analysis mapping semantic understanding to detection performance, yielded three main findings: (1) type identification and intent understanding were generally strong, whereas severity assessment was the principal weakness; (2) the effects of obfuscation varied across models and layers, with intent explanation and reconstruction of specific obfuscation techniques more susceptible to degradation, while performance did not degrade synchronously across all layers; and (3) semantic understanding and detection decisions were partially decoupled, with only 12.5% to 50% of missed detections attributable to semantic-understanding failures. External re-evaluation on an independent 180-record dataset comprising production WAF alert streams and real application requests reproduced the non-uniform four-layer capability profile and the layer-specific differences on obfuscated payloads.

---


### 418. [SOL: Measuring Gaps between Text Distributions by Double Sliced Wasserstein Metrics](https://arxiv.org/abs/2610.06513)

**<font color=#1a73e8>作者：</font>** Gregor Kornhardt, Moritz Piening, Jannis Chemseddine 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating text generation requires measuring how well the generated distribution matches the data distribution. For autoregressive models, this is done by the perplexity. Diffusion and flow-based language models can only provide a likelihood bound, whose tightness differs between model families. Sample-based substitutes such as generative perplexity with entropy do not consider the distribution fit. We propose SOL,
a distance between text distributions. Each sequence is represented by the empirical measure of its hidden states under a fixed transformer and the distributions of these measures are compared by the double sliced Wasserstein distance. We prove that SOL is a metric if the transformer is injective. Experiments show that SOL detects distributional failures, recovers expected model trends, and provides stable sample-based estimates. We put forward SOL to fill the gap in the current evaluation protocol used for non auto-regressive models. As a first step we use SOL to re-evaluate a variety of models trained on OpenWebText.

---


### 419. [ANT: A Multi-Granularity Network Traffic Dataset and Benchmark for Agents Behavior Auditing](https://arxiv.org/abs/2610.06514)

**<font color=#1a73e8>作者：</font>** Fan Li, Xiangyu Gao, Zixuan Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The growing adoption of large language model (LLM) agents creates a need for network administrators and security teams to audit agent behavior within organizational networks without inspecting private user content. Network traffic offers an observable source of evidence, but how much it reveals about agent tasks and operations remains unclear. Existing traffic datasets lack the joint task and stage annotations needed to evaluate this question. We introduce ANT (Agent Network Traffic), a dataset providing agent behavior information at risk, scenario, and behavior primitive granularities alongside network traffic. ANT contains 3,114 execution episodes across 20 tasks and five scenarios, comprising 276,417 bidirectional flows and 40,049 behavior primitive segments organized into 47 macro groups. We establish a benchmark for agent risk identification, scenario recognition, and behavior primitive classification using 13 representative traffic analysis baselines. The results show that existing methods recover useful but uneven behavioral signals. They struggle to identify risk when malicious workflows resemble benign tasks and to distinguish scenarios with similar traffic patterns. Primitive classification is more reliable for frequent macro groups and those with distinctive traffic patterns than for rare or semantically similar groups. ANT provides a common basis for developing more precise auditing and forensic analysis of agent behavior from network traffic. Our data and code are available at this https URL.

---


### 420. [Test-Time Adaptation of Reasoning Strategies with Bayesian Nonparametric Memory](https://arxiv.org/abs/2610.06516)

**<font color=#1a73e8>作者：</font>** Keshav Ramji, Tahira Naseem, Ramón Fernandez Astudillo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While modern large language models (LLMs) have been trained to reason through verbalized chains-of-thought, the generation cost grows substantially due to suboptimal paths to reach the final answer. Furthermore, as new insights are discovered while observing various input queries (e.g. through self-reflection), limited mechanisms exist for carrying forward these findings to be applied to subsequent problems. One can view the list of such strategies or behaviors as a growing cheatsheet, with elements retrieved from this memory module at inference-time. In this work, we consider structured cheatsheets, with learned clusters of behaviors. We introduce a Hierarchical Dirichlet Process Gaussian Mixture Model (HDP-GMM) over behavior embeddings, which shares components across domains while allowing domain-specific mixing weights, and uses the posterior predictive to retrieve relevant behaviors for a query; we call this a $\textit{Bayesian Cheatsheet}$. This mechanism allows for cheap adaptation in an online test-time training (TTT) setting, softly updating the mixture's sufficient statistics following each sample and enabling the creation of new components when the synthesized behaviors are sufficiently novel. We demonstrate that Bayesian Cheatsheet achieves clear performance gains relative to existing memory modules across reasoning benchmarks such as AIME'25, Omni-MATH, and PhysReason, even in the cold-start setting. We show that the Bayesian Cheatsheet is an adaptively reorganizing memory module, as behaviors can be re-assigned to components through a single step of collapsed Gibbs sampling. Our findings highlight the value of Bayesian-inspired memory modules for effective test-time adaptation and the role of structure in metacognitive reasoning.

---


### 421. [Anatomy of LLM Sycophancy: What a Flip Rate Hides](https://arxiv.org/abs/2610.06522)

**<font color=#1a73e8>作者：</font>** Haonan Huang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A model under pushback can correct itself, capitulate, or hold, and one flip rate counts a correction and a capitulation alike. Using SycoLens, a modular replay protocol, we test how user pressure and evaluation settings shape measured flip rates. Each measurement is one stateless replay of an item, a committed answer, and one scripted user line in a fixed form. Every effect is read against a matched control with the line deleted. Pushback wording, committed text, answer format, boundary distance, and ground truth become factors of one instrument; earlier instruments vary one to three of them. Across eleven frontier models from three providers and about 760,000 controlled replays, which models look sycophantic depends on how the user pushes back. Lines that assert the opposite verdict and lines that challenge the answer without asserting one rank the models almost unrelatedly. Flip effects grow several-fold near a model's boundary, yet items answered identically in every screening draw still carry about half of the most-affected totals. On arithmetic tasks where the truth is known, one model re-derives and corrects itself under pressure while another abandons correct answers without written work. On the model tested, a planted derivation lowers release of the answer it argues for, true or wrong, where a bare stated value does not; the wrong answer is corrected much more often than the true one is abandoned. Under a yes/no readout the rankings come closer, entangled with a pressure-induced shift toward "no". One score per model therefore compares different behaviours across models and benchmarks. We condense these dependencies into a reporting profile; the instrument, records, and analyses will be released upon publication.

---


### 422. [AICoFe Demo: AI-based Collaborative Feedback System](https://arxiv.org/abs/2610.06532)

**<font color=#1a73e8>作者：</font>** Alvaro Becerra, Alejandra Palma, Ruth Cobos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Peer feedback promotes active learning, critical reflection, and skill development, but its effectiveness is often limited by the quality of feedback students provide. Recent advances in LLMs offer new opportunities to support peer feedback by generating more coherent and actionable feedback while preserving human oversight. This paper presents AICoFe, an AI-based collaborative feedback system designed to support teacher, peer, and self-assessment in higher education. AICoFe integrates rubric-based evaluations, GenAI-supported feedback, Learning Analytics dashboards, and video recordings to foster reflective learning. The system combines quantitative scores and qualitative observations to generate structured feedback focused on strengths, areas for improvement, and actionable recommendations, which teachers can review and curate. An evaluation with 65 undergraduate and master's students shows high satisfaction with the coherence and usefulness of the feedback, as well as the excellent usability, indicating that AICoFe effectively supports peer feedback in authentic educational settings.

---


### 423. [HERA: Harness-Environment Co-Evolution for Reliable Agentic Abstention](https://arxiv.org/abs/2610.06563)

**<font color=#1a73e8>作者：</font>** Han Luo, Bingbing Wen, Guang Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly capable of acting in complex tool-use environments, yet they often fail to recognize when tasks are infeasible and no valid solution exists. Recent work has formalized this reliability gap as the problem of agentic abstention, and existing approaches typically optimize a model or agent harness against a fixed set of tasks, leading to limited generalization to unseen failure modes. We introduce HERA, a framework for harness-environment co-evolution for agentic abstention. HERA consists of (i) a pipeline to automatically construct verifiable pairs of feasible and infeasible tasks by applying controlled environment mutations that transform solvable tasks into cases requiring abstention, and (ii) a co-evolution procedure in which performance failures on previous tasks are used to drive harness adaptation and generate new execution environments and tasks geared towards previous weaknesses. On held-out evaluation tasks, an evolved harness from HERA improves abstention accuracy from 61.7% to 83.3% while improving feasible-task completion from 68.3% to 76.7%, achieving the highest abstention and feasible-task completion among the compared methods. The resulting best harness transfers across 19 other LLMs, improving abstention accuracy by 15.3 percentage points on average without any model-specific optimization, and enabling smaller models to match the performance of more powerful models at an estimated 85% lower cost.

---


### 424. [BrainTRACE: Tracing Longitudinal, Multimodal, and Volumetric Evidence in Brain MRI Clinical Reasoning](https://arxiv.org/abs/2610.06571)

**<font color=#1a73e8>作者：</font>** Qizhen Lan, Mengchen Fan, Hang Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Brain MRI interpretation is a longitudinal clinical reasoning problem: radiologists compare serial studies, integrate information across MRI sequences, localize findings within volumetric anatomy, and translate this evidence into report-grounded assessments. Existing medical VQA and 3D imaging benchmarks capture important parts of this workflow, but often evaluate brain MRI through isolated images, static volumes, or ungrounded report-style answers, thereby obscuring failures in the evidence chain that support clinical validity. We introduce BrainTRACE, a report-grounded benchmark for evaluating whether vision-language models can trace the evidence structure required for longitudinal brain MRI interpretation. BrainTRACE contains 7,273 scored VQA instances derived from 1,778 longitudinal patients, 7,299 MRI studies, and approximately 29k co-registered 3D MRI sequence volumes. The benchmark is organized by five levels of clinical reasoning, from acquisition recognition to case-level synthesis, and by evidence demands covering longitudinal comparison, report-grounded references, multi-sequence integration, and volumetric spatial evidence. BrainTRACE supports rendered inputs compatible with standard VLM interfaces, a 3D-evidence condition, and a decomposed case-reasoning track that audits six steps in a longitudinal evidence chain. Evaluation of 20 VLM configurations shows that current systems can identify isolated visual cues but rarely compose them into grounded longitudinal interpretations. We release the benchmark specification, evaluation lists, scoring implementation, scoring rubrics, and audit-record format to support reproducible progress in brain MRI VLM evaluation.

---


### 425. [Before Agent Tells The Lie: Has Deception Already Been Represented?](https://arxiv.org/abs/2610.06576)

**<font color=#1a73e8>作者：</font>** Xinling Li, Dadi Guo, Qingyu Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based agents can exhibit deceptive behavior during task execution, including hiding failures, fabricating results, or falsely signaling task completion. Existing monitoring approaches mainly detect deception after it appears in observable actions or outputs. In this paper, we investigate whether deceptive behavior can be predicted from an agent's internal representations before it becomes externally visible. We frame deception monitoring as a trajectory-level representation analysis problem and align agent trajectories around key decision points. Using hidden states extracted before these points, we show that future honest and deceptive outcomes can be reliably distinguished, with predictive signals remaining detectable several model calls before the final decision. We further characterize the temporal evolution of these signals: deception-related representations are weak early in execution but become increasingly identifiable as trajectories progress, while transferable structure can emerge before the strongest decision-adjacent signals appear. Finally, we intervene on the identified honest-deceptive representation directions during inference and find that activation steering reduces downstream deceptive behavior, suggesting that these representations influence agent decisions. Our findings indicate that agent deception is an evolving internal process that can be detected and potentially mitigated before it is expressed externally.

---


### 426. [Does AI Help Cyber Attackers or Defenders? Evidence from Nonpublic Vulnerabilities and Subsequent Attacks](https://arxiv.org/abs/2610.06584)

**<font color=#1a73e8>作者：</font>** Tobias Heldt, Matt Turk, Christoph Landolt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The release decision for frontier AI systems increasingly relies on cyber capability benchmarks, yet public vulnerability benchmarks can expose agents to previously published advisories, exploits, and fixes, making it difficult to distinguish prior exposure from capability on unseen vulnerabilities. We evaluate open-weight and proprietary AI models on exploit generation, vulnerability repair and subsequent attacks in five nonpublic software environments, including vulnerabilities we privately disclosed while they remained unpatched. Researcher-developed and reviewed deterministic graders, not LLM judges, determine task scores. Comparisons with 209 disclosed vulnerabilities and cryptographic challenges reveal substantial variation across systems and vulnerability types. Repair scores exceed attack scores in two nonpublic environments and fall below them in three. Passing an initial security test is also insufficient: another exploit succeeds in 92 of 524 non-independent defender test intervals after the initial exploit is stopped. These results motivate vulnerability-specific attack-repair comparisons and subsequent resistance tests.

---


### 427. [The Review Lottery: Calibrating an Observational Estimator of Peer-Review Noise (ICLR 2017-2025)](https://arxiv.org/abs/2610.06591)

**<font color=#1a73e8>作者：</font>** Feilian Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How much of a conference accept/reject decision would change if the same paper were reviewed by a different set of reviewers? Running a second independent program committee is the gold standard for answering this, but it is prohibitively expensive: done only twice (NeurIPS 2014 and 2021). We build an observational estimator of this quantity from public review data alone, calibrate it twice, and apply it to nine years of ICLR (2017-2025; 36,113 papers, 134,912 reviews). The estimator decomposes scores with a Bayesian ordered-probit model into paper quality and reviewer noise, maps scores to decisions with a logistic model, and simulates two independent committees (posterior draws B=1,000; committee sizes k=2,3,4). Estimated disagreement rates are 23-30% at k=2 and 18-24% at k=4; 30-50% of accepted papers would be rejected. External calibration: at the NeurIPS 2021 reviewer-count caliber (k=3), the simulated 2021 disagreement rate is 23.3% [21.7%, 25.0%] vs. reported 23.0% (bias +0.3pp); accept precision and committee correlation agree within 5pp and 0.04. Internal calibration: on 18,740 papers with 4+ reviews, random model-free 2+2 reviewer splits agree with the k=2 simulation within 1pp in 2018 and 2021-2025. Longitudinally, we find no robust time trend in reviewer noise over 2017-2025. The high accepted-paper flip rates of 2020 and 2021 have distinct mechanisms: the 2020 four-point scale compressed scores (23.7% of papers had zero within-paper variance), and a counterfactual shows coarsening the scale raises disagreement by about 7pp; 2021 instead combined the lowest signal-to-noise ratio in the sample with the most threshold-crowded acceptances. For the LLM era, a 2023 breakpoint test on within-paper score variance finds no break, but the design has almost no power, and no post-2022 review text or confidence data exist, so no LLM attribution is attempted.

---


### 428. [Can Agent Harnesses and Inference Engines Hear Each Other? The HEAR Protocol for Agentic LLM Serving](https://arxiv.org/abs/2610.06597)

**<font color=#1a73e8>作者：</font>** Jiaqi Zhao, Haodong Chen, Jitai Hao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly execute complex workflows involving multi-turn reasoning, tool use, and parallel agents. Efficient serving requires decisions that span two layers with complementary information: the agent harness understands workflow dependencies, context lifecycles, and execution objectives, whereas the inference engine observes request queues, KV-cache state, resource pressure, and execution capabilities. Existing interfaces do not systematically connect these views, limiting workflow-aware execution.
HEAR, a bidirectional Harness--Engine Pairing protocol for agentic LLM serving. HEAR standardizes how the harness communicates workflow intent and execution requirements and how the engine returns runtime state, capabilities, and outcomes. By separating protocol semantics from optimization policies, HEAR supports diverse coordination strategies without changing workflow or model semantics. We instantiate HEAR for online cache-aware runtime coordination and workload-aware execution-mode selection for agent roles.
Across four conversational and research-agent benchmarks under memory-constrained, concurrent serving, HEAR achieves a $1.61\times$ batch speedup and reduces median time-to-first-token by $2.23\times$ on SCBench. Mooncake shows that workflow intent and live engine state provide complementary benefits across load regimes. On BrowseComp-Plus and DeepResearchBench, workload-specific configurations yield $1.23\times$ and $2.45\times$ end-to-end speedups, respectively, without observed task-quality degradation. These results establish HEAR as a reusable coordination substrate for efficient agentic LLM serving.

---


### 429. [Word-Level Text Unmixing via Evidence-Preserving Ownership Routing with Language Models](https://arxiv.org/abs/2610.06603)

**<font color=#1a73e8>作者：</font>** Jinglin He, Siyang Jiang, Lixing He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text from multiple sources can become interleaved into a single sequence when attribution metadata is lost, such as overlapping speech transcripts, document reading flows, or concurrent agent streams. We formalize this challenge as Word-Level Text Unmixing: given an interleaved lexical stream and source count K, recover the original source sequences while preserving every word occurrence and its within-source order exactly. Directly generating separated texts with LLMs can omit, duplicate, or hallucinate words, violating this exact-reconstruction objective. We therefore propose Evidence-Preserving Ownership Routing (EPOR), which decouples source-ownership prediction from reconstruction. EPOR adapts a causal LLM to predict canonical ownership routes conditioned on the mixed stream and prior routing decisions. At inference, completion-safe constrained decoding is combined with deterministic indexed reconstruction, yielding structurally valid K-source partitions that preserve every observed occurrence exactly once. We also introduce UNMIXBENCH, covering controlled synthetic mixtures, timestamp-derived speech from AMI and ICSI, layout-derived document streams from ReadingBank, and simulated concurrent digital outputs. Across five evaluation tracks, a 4B EPOR model achieves the lowest mean minimum-permutation word error rate among finetuned baselines, reducing the five-track mean by 22.3% relative to compact source-array generation and remaining competitive with zero-shot frontier LLMs. These results show that when lexical evidence is fully observed, separating ownership inference from lexical regeneration provides a reliable alternative to direct generation.

---


### 430. [Separators Make Carry Propagation Learnable:The Geometry of Latent Carry in a Multiplication Transformer](https://arxiv.org/abs/2610.06605)

**<font color=#1a73e8>作者：</font>** Sama Satariyan, Raphael Cousin, G{é}rard Biau  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers asked to multiply multi-digit numbers in a single forward pass often fail, and interpretability studies of pretrained language models find arithmetic solved by input-range heuristics rather than by an explicit carry. We train small Llama-style transformers from scratch on 4x4 multiplication without chain of thought and find that the input format is decisive: inserting a space token between digits raises exact-match accuracy from 1% to 89%. Output positions are learned in carry-chain order, with the middle digits, which have the longest-range dependencies, learned last. Inside the model, the separator token that predicts each digit (its prediction slot) encodes the carry-in as an angle on a ring in the residual stream; examples with more distinct carry values fill more of the ring. Activation patching between examples matched on the column sum shows that this state is causally used before the last layer: patching the prediction slot alone transfers the source carry in up to 84% of cases after block 4 for one middle column of our best model, while for other columns the carry is first assembled at the neighboring answer slot before reaching its own. Remaining errors are almost always off by one, consistent with a small error on the carry or on the circular digit code.

---


### 431. [Lens3D: Target-Conditioned Visual Foveation for Fine-Grained 3D Understanding](https://arxiv.org/abs/2610.06611)

**<font color=#1a73e8>作者：</font>** Junming Huang, Zini Chen, Shuaiying Hou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing 3D large language models often overlook fine-grained attributes and less visually salient objects and parts, even when relevant evidence is present in scene videos. We introduce Lens3D to improve fine-grained object understanding through external visual assistance and knowledge transfer. Its LensUnd pipeline adopts 3D localization to select informative, complementary views for an external 2D vision-language model, supporting fine-grained object captioning, small-object grounding, and fine-grained object question answering. LensDistill transfers the resulting fine-grained knowledge to 3D LLMs through detailed caption supervision, enabling captioning from native inputs without external VLM calls. We also construct LensBench, a held-out evaluation set of 2,068 objects with three silver-standard reference descriptions per object. Experiments with Video-3D LLM and 3DRS demonstrate that LensDistill substantially improves fine-grained object captioning while preserving existing grounding and scene-level QA performance. These results establish the feasibility of transferring externally acquired fine-grained knowledge into native 3D LLMs.

---


### 432. [FREA: A Multi-Source Expert Benchmark for Reaction Feasibility Verification](https://arxiv.org/abs/2610.06614)

**<font color=#1a73e8>作者：</font>** Botao Yu, Bo Zhou, Daniel Adu-Ampratwum 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As generative models and AI agents propose chemical reactions at a scale beyond expert review, feasibility verifiers decide which proposals enter synthesis planning. But do their decisions agree with chemists across different kinds of candidates? We introduce FREA, a benchmark of 751 reactions labeled by expert chemists under an explicit feasibility criterion, drawn from retrosynthesis model proposals, zero-yield experimental records, edits by large language models (LLMs), and five negative candidate generation methods. Our evaluation finds that no verifier leads across all sources: LLMs given only the criterion are competitive with dedicated verifiers, while forward models perform best on retrosynthesis proposals but reject most feasible edits of recorded reactions at the evaluated operating points. Looking beyond aggregate scores, both forward models perform below chance when separating infeasible alternative disconnections from feasible generated candidates. To study whether negative supervision addresses these weaknesses, we also release a corpus of over 14 million recorded reactions and generated negative candidates. In matched training comparisons, adding a mixture of generated negatives to forward training raises mean AUROC across sources, but these gains do not extend to retrosynthesis proposals. Varying the generation method further shows that the largest gain on generated candidates coincides with worse proposal screening. These findings motivate evaluating verifiers against experts across sources and designing negatives for transfer to model proposals.

---


### 433. [Video Encoders Built on Image Representations](https://arxiv.org/abs/2610.06616)

**<font color=#1a73e8>作者：</font>** Jusheng Zhang, Wenhao Wang, Longqi Cai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The design of a video encoder determines when frames begin to interact and which frame-specific visual evidence remains accessible to the language model. Native video pathways couple neighboring frames during visual encoding, whereas image pathways preserve independently computed frame representations but incur a much larger visual-token cost when all image tokens are forwarded. We ask a basic question: whether a compact video encoder can instead be built on image representations. To answer this question, we separate three operations that are often coupled: per-frame representation, cross-frame token allocation, and temporal interaction. A frozen image encoder first produces frame-specific candidates. A question-aware selector then allocates a fixed token budget across frames using relevance, diversity, and cross-frame correspondence, after which a lightweight learned refiner reads neighboring-frame context and writes residual updates only to the retained anchors. This preserves source positions and keeps the visual output at the fixed budget. Across 13 benchmarks and three vision-language backbones, the resulting pathway matches full-image aggregate performance while using only about 28%-35% of its visual tokens. Specifically, on Qwen3-VL-8B, it achieves a 13-benchmark macro-average of 62.75 with 1,535 visual tokens, compared with 62.58 for the full Image pathway at 4,424 tokens and 59.49 for native Conv3D at 2,212 tokens. On Qwen3-VL-32B, it reaches a 13-benchmark macro-average of 66.28, compared with 66.09 for Image, while providing a 2.16x end-to-end speedup. These results show that compact video encoding does not require early temporal mixing: frame-specific evidence can be preserved first, allocated jointly, and temporally contextualized after selection.

---


### 434. [If My Toy Could Talk: How Young Children Imagine, Design, and Test AI-Enabled Toys](https://arxiv.org/abs/2610.06619)

**<font color=#1a73e8>作者：</font>** Feiwen Xiao, Ruiyang Wu, Xinyue Cui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> To investigate the design space where children might design AI chatbots for their own toys, we developed ToyTalk, a technology probe that positions children as designers of LLM-enabled toys. Children begin with a familiar toy, configure its AI-enabled version through a no-code interface, and then interact with and test the character. We deployed ToyTalk with 76 children aged 7-9 across five elementary schools in the southeastern U.S. We examine how children define their toy, probe what it becomes, and respond when behavior diverges from expectations. Children predominantly designed toys with socially positive personalities, supportive roles, and interpersonal rules. In conversation, they most often probed identity and knowledge, while also testing capabilities, memory, and relationships. When mismatches arose, children typically responded through correction, persistence, and retesting, while few returned to reconfigure the system. We discuss implications for children's design agency, testing practices, and expectations of coherence in child-facing generative AI.

---


### 435. [Frozen Factor or Spectral Band? Disentangling Two Choices in Low-Rank LoRA](https://arxiv.org/abs/2610.06621)

**<font color=#1a73e8>作者：</font>** Adnan Slimane Ali, Ayoub Belfatmi, David Ngwe Pouth  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spectral variants of low-rank adaptation (LoRA) choose both a subspace and which factor to freeze. We separate these choices by freezing the input factor A or output factor B on the top or bottom singular directions of pretrained weights, with learning rates selected separately. At rank 2, the same-band advantage of freezing A is larger than either within-factor band difference on all four task-model pairs with complete comparisons. Freezing B also trails comparable-budget free LoRA by 8-18 percentage points on five pairs spanning a formatting task and OpenBookQA. The A-frozen advantage persists in a single-GPU-model replication and within individual MLP module groups, including controls with equal or greater trainable counts for B frozen, and when A is frozen on a random orthonormal basis. The factor contrast weakens with rank. On OpenBookQA / Qwen2.5-1.5B at rank 16, PEFT's MiCA implementation trails comparable-budget LoRA by 3.08 points under a shared training recipe transferred from the MiCA paper. A trained oracle output subspace largely removes the low-rank deficit; partial warm-up gains recur across three direction seeds. The factor-versus-band ordering is descriptive; an approximate multiplicity audit weakens several earlier significance claims. These results extend known factor asymmetry by showing how its magnitude depends on spectral placement, rank and training conditions.

---


### 436. [JEV versus LLMs: Accuracy, Cost and Calibration on Seven Political Science Replications](https://arxiv.org/abs/2610.06625)

**<font color=#1a73e8>作者：</font>** Matthew DiGiuseppe, Steven Denney  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) annotate and scale political text or constructs by generating text tokens. A new class of models, which TypeSafe markets as "System One" models, instead returns decisions and probability distributions across a user-supplied fixed answer set. A commercial model, JEV, is advertised as having a dramatic cost and speed advantage over traditional LLMs along with better calibrated decisions. As such, it might be useful for social scientists looking to quickly and cost-effectively annotate or scale large corpora of text and have a reliable indicator of a classifier's uncertainty. Yet, the accuracy of these claims and the broader model accuracy in social science text-based tasks are not yet established. In this paper, we do just that and hope to establish the suitability of JEV for social science tasks. We compare JEV with LLMs and human coders from published research, and with a current mid-tier commercial LLM (GPT-6 Luna) and an open-weight alternative (Qwen3.8-27B). We find that JEV matches, or comes close to, the capabilities of both LLMs in a variety of tasks. However, we find no cost advantage over GPT-6 Luna at OpenAI's batch prices. Further, we find that, when each question is asked once, JEV's probabilities are better calibrated than GPT-6 Luna's token probabilities, but not consistently better than Qwen3.8-27B's. We conclude that unless researchers have a need for speed, JEV's only obvious advantage is ease of parsing the underlying choice probabilities.

---


### 437. [LoGRA: Scaling LLM Reinforcement Learning with Low-Rank Gradient Sketches](https://arxiv.org/abs/2610.06647)

**<font color=#1a73e8>作者：</font>** Shaokun Zhang, Yifan Zhang, Jian Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has greatly advanced the capabilities of large language models (LLMs), but its memory demands remain a barrier to broader adoption. We introduce LoGRA, an approach to RL post-training that reduces memory by retaining useful learning signals in low-rank gradient sketches. These compact representations support both model updates and efficient policy synchronization. To prevent overly large updates from disrupting learning, we complement gradient compression with predicted-KL step control, which estimates policy changes before applying each update and adjusts its magnitude accordingly. Across reasoning tasks, LoGRA reduces average training memory by up to 45.7\% without sacrificing performance. It also enables stable training of a 27B-parameter model for over 1,100 steps on a single eight-GPU node, where dense Adam runs out of memory, making previously memory-infeasible RL training practical. Code is available in the \href{this https URL}{Molt library}.

---


### 438. [Representation-Space MMD for Diffusion Language Models](https://arxiv.org/abs/2610.06648)

**<font color=#1a73e8>作者：</font>** Ilya Drobyshevskiy, Ilia Sudakov, Maksim Semenov 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce a post-training method for diffusion language models (DLMs) that minimizes Maximum Mean Discrepancy (MMD) between generated and reference distributions in the feature space of a frozen pretrained DLM. To estimate MMD, we retain contextual features at individual token positions, obtaining multiple observations per sequence from a single extractor pass. We optimize this objective using policy gradients for discrete models and direct differentiation through generated latents for continuous models. In both cases, computing the loss directly from these features enables efficient post-training without full sampling trajectories or jointly trained auxiliary models. Experiments show lower generative perplexity at comparable entropy on OpenWebText and better accuracy-computation trade-offs on GSM8K. On 16B DMax-LLaDA2.0 models with hybrid masked-uniform diffusion, we increase decoding parallelism with similar or higher accuracy on math and code benchmarks.

---


### 439. [Wikidata Search Traces: A Dataset for Training Knowledge Graph Search Agents](https://arxiv.org/abs/2610.06650)

**<font color=#1a73e8>作者：</font>** Mohamed Chenene, Carlos Rosas-Hinostroza, Pierre-Carl Langlais 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Wikidata is one of the largest open knowledge bases, yet answering a complex question over it still requires a SPARQL query that names the right entities and properties and chains their relations. Language models offer a natural-language alternative but answer largely from memory, which is least reliable for less prominent entities. We study agents that instead answer by exploring the graph, and argue that two obstacles limit them: the lack of training data recording how a solver explores, and interfaces that add large graph results directly to the model's context. We test three hypotheses: that the difficulty of graph search can be controlled through the structure of a question rather than only through obscure entities or wording; that much of the failure on long-horizon search comes from how retrieved evidence is managed rather than from the model itself; and that, in a suitable environment, open-weight models can match commercial closed ones. We construct multi-hop questions on a frozen Wikidata snapshot by replacing named entities with nested conditions, checking after each expansion that the target remains unique and that every new condition is necessary. We release 10,235 solving traces over single-entity and multi-hop questions, together with the recursive language model (RLM) harness that produced them, in which models batch graph calls, keep results in persistent Python state and interpret selected evidence through sub-calls. On 100 questions, the harness improves both models we ran under both interfaces compared with direct tool calling over the same functions: gpt-6-luna rises from 49 to 61 correct answers, doubling its multi-hop accuracy, and Qwen3.8-27B, an open-weight model served on a single GPU, from 60 to 74.

---


### 440. [What Matters for Latent Reasoning with Flow Matching](https://arxiv.org/abs/2610.06666)

**<font color=#1a73e8>作者：</font>** Yassine Ouali, Adrian Bulat, Georgios Tzimiropoulos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent reasoning lets a large language model (LLM) think in a continuous space and verbalize only the answer. We argue that an effective latent thought must meet five requirements: it should be useful, helping produce the correct answer rather than merely changing it, diverse, so that resampling yields different reasoning trajectories, explainable, so that a decoded chain of thought (CoT) reflects reasoning the answer actually follows, refinable with more inference compute, and efficient, costing less than an explicit CoT at comparable accuracy. Current methods rarely meet these requirements: they learn shortcuts from the question, distill the explicit CoT into their weights, or imitate it one token at a time. We focus on flow matching in a learned latent space, the family we argue is best placed to meet them, and identify the training choices that make it work. The result is Flow-based Latent Reasoning (FLaRe), a simple recipe covering what the latent space encodes and how to shape it, where to train the flow, how to read out the answer, and a final stage of training on the model's own verified thoughts. A probe for each requirement shows that FLaRe improves on prior latent methods in all five. It also compares favorably with them on arithmetic benchmarks, while reaching 97% of the accuracy of explicit CoT at a quarter of its latency.

---


### 441. [Language models can notice an impossible engineering problem yet still report it as solved](https://arxiv.org/abs/2610.06668)

**<font color=#1a73e8>作者：</font>** Shaoliang Yang, Jun Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models draft engineering calculations, but answer accuracy does not show whether they reject an impossible problem. We tested 14 models on 30 pairs of mechanics problems, each with a valid version and one made impossible by changing a given value or assumption. Two independent solvers verified every answer key and showed that each flawed problem was physically impossible. We scored solving of valid problems separately from rejection of their flawed counterparts. Each reply required a "solved" or "cannot solve" status; rejection meant "cannot solve" or withholding an answer. The initial prompts did not warn that problems could be flawed. Across three recent models, 12 of 90 replies failed to reject a flawed problem. In 11 of these replies, the model stated the flaw, answered a corrected problem and still reported the original as "solved", according to artificial intelligence raters and numerical checks. We later retested four models from one provider, offering "flawed" instead of "cannot solve" and asking them to name and explain the defect. Three models showed statistically significant increases in rejection, but valid-problem solving fell in three. Evaluations therefore need to score both versions and distinguish flaw recognition from the reported status.

---


### 442. [Reward Stealing Attack on Large Language Models](https://arxiv.org/abs/2610.06670)

**<font color=#1a73e8>作者：</font>** Jiaming Qian, Pengyang Zhou, Jiahe Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Adversarial attacks on Large Language Models (LLMs) aim to induce harmful content. However, existing methods suffer from high computational costs or strict model-pairing dependencies, limiting their scalability and transferability. We propose Reward Stealing Attack (ReSA), an adversarial attack framework that targets the latent safety reward underlying LLM alignment. ReSA employs maximum entropy inverse reinforcement learning to recover a proxy reward model solely from the aligned model's behavior. The extracted reward is then reversed at inference time to derive an adversarial policy, efficiently implemented via a reward-guided decoding mechanism. Experiments demonstrate that a single recovered reward generalizes across prompts and diverse models to reveal a fundamental alignment vulnerability, enabling ReSA to significantly outperform existing attacks in effectiveness and transferability. The code is available at this https URL.

---


### 443. [Learning What to Imitate: Entropy-Aware Distribution Mixing](https://arxiv.org/abs/2610.06671)

**<font color=#1a73e8>作者：</font>** Juan Garcia Giraldo, Matteo Santelmo, Eduard Durech 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small language models are often post-trained as students on reasoning traces from stronger teacher models to efficiently learn new skills. However, token-level imitation on traces that lie far outside the student's expected distribution often produces \textit{confident conflicts}, whereby the student is required to imitate a continuation that it deems unlikely (i.e., low-probability) despite being confident in a different continuation (i.e., in a low-entropy state). To mitigate the degradation in generalisation and catastrophic forgetting caused by these conflicts, we propose \textbf{Entropy-Aware Mixing}: a dynamic per-token interpolation of the student and teacher distributions, gated by the student's predictive entropy. We implement both convex and geometric interpolations for both offline trace generation (via speculative decoding, then SFT) and on-policy forward-KL distillation. Our results show that entropy-aware mixing stabilises distillation, improving in-distribution and out-of-distribution math reasoning while better preserving general capabilities than fixed-teacher supervision. Nonetheless, the optimal entropy schedule depends on the training source, with offline-generated traces favouring concave schedules (greater overall teacher influence) and on-policy training favouring linear or convex schedules (teacher concentrated in high-entropy states).

---


### 444. [VideoTapestry: Query-Adaptive Memory Refinement for Multi-Agent Long-Video Understanding](https://arxiv.org/abs/2610.06672)

**<font color=#1a73e8>作者：</font>** Yucheng Liu, Yufei Yin, Mingxiao Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-video understanding places substantial demands on memory, as answering questions often requires retrieving information distributed across extended temporal spans. Existing approaches broadly follow two paradigms: query-driven exploration, which is sensitive to localization errors, and query-independent memory construction, which may omit question-specific details. We introduce VideoTapestry, a training-free multi-agent framework that adapts a preconstructed hierarchical video memory through coarse-to-fine, query-driven refinement. The preconstructed memory organizes video content into three levels, capturing global narrative context, event-level temporal structure, and fine-grained relational evidence, respectively. To support coarse-to-fine localization and observation, we assign a specialized agent to each level, keeping retrieval and refinement within a scale-specific context. Guided by the query, these agents revisit relevant video regions and enrich layer-wise memories with targeted multimodal observations. Their refinements are assembled according to the original hierarchy into a composite query-adaptive memory, preserving global context in a compact form while retaining fine-grained evidence along query-relevant branches for final reasoning. Compared with direct GPT-5.5 inference, VideoTapestry achieves absolute accuracy gains of 17.2%, 14.9%, 9.8%, and 7.0% on LVBench, LongVideoBench (Long), Video-MME (Long), and EgoSchema, respectively, achieving the state-of-the-art results among all competitors.

---


### 445. [The Pushback Paradox: A Two-Probe Diagnostic for Language Model Compliance](https://arxiv.org/abs/2610.06673)

**<font color=#1a73e8>作者：</font>** Stefan Bühler, David Exler, Markus Reischl 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Are language models compliant with user instructions? A model that always complies can be stopped but also exploited, while one that always resists can be neither exploited nor stopped. We contribute an open two-probe benchmark that can place any language model on this spectrum. In the active probe, a user instructs the model to act and accept a lower payoff, which measures exploitability. In the passive probe, the user instructs it to wait and give up a higher payoff, which measures stoppability. The two compliance rates combine into a compliance index $\kappa$. Applied to twelve language models, the benchmark shows that seven mostly follow the instruction in both probes and justify their action by pointing to the instruction. Only Claude Sonnet-4.6 and Claude Opus-4.7 can be stopped without being exploitable, Claude Opus-4.6 and GPT-5-mini resist both instructions, and no model is exploitable but unstoppable. Knowing where a language model sits on the compliance index $\kappa$ matters for human operators and for multi-agent systems, whether distributed or orchestrated.

---


### 446. [How Sparse Probability Maps Shape Mixture-of-Experts Routing](https://arxiv.org/abs/2610.06677)

**<font color=#1a73e8>作者：</font>** Tomás Brogueira, Marcos Treviso, Miguel Couceiro  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-experts (MoE) routers typically apply softmax to the router scores and keep the top-K experts, making every token use exactly K experts. Sparsity-inducing probability maps such as sparsemax, alpha-entmax and normmax can adaptively assign exact zeros to selected experts, and therefore appear to offer token-dependent expert participation, even when using the same top-K machinery. In this work, we study whether and how this sparsity survives training. We train matched 300M and 1B top-2 MoE language models with softmax, 1.5-entmax, sparsemax and 2-normmax, and find that the maps behave very differently once trained: at 1B, entmax discards 30% less probability mass than softmax while almost never dropping a selected expert, sparsemax retains the most mass, and normmax routes 21% of tokens to a single expert. These outcomes are not properties of the maps alone. Each map drops a selected expert only when the gap between the two largest scores reaches a fixed threshold, and the trained routers differ in the score distribution they learn: the entmax router learns scores with roughly half the spread of softmax's, which keeps its top-2 gaps below its threshold, while sparsemax and normmax, which share the same threshold, learn different gap distributions and hence different participation. Routers thus co-adapt their scores to the map, and a map's capacity to produce zeros does not by itself determine expert participation. While none of the sparse maps improves validation loss over softmax, they make the trained models far less sensitive to selecting more experts at inference: sparsemax trained with K=2 loses 0.02 nats when run with K=8, where softmax loses 0.58. Our results indicate that adaptive MoE routing has to be designed around the joint behavior of the probability map and the learned scores, rather than around the map alone.

---


### 447. [Closing the Context Gap: Activation Alignment for Tabular In-Context Learning](https://arxiv.org/abs/2610.06679)

**<font color=#1a73e8>作者：</font>** Yoel Zeldes  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models perform in-context learning (ICL) by conditioning predictions on labeled training examples provided as context. Unlike traditional models that separate training from inference, these models must process all training examples in every forward pass, making each prediction expensive. Restricting the number of training examples reduces this cost but substantially degrades performance. Instead of discarding context, we propose activation alignment, a method that leverages the full context to teach a model how to behave when seeing only a subset. This is achieved by training a lightweight linear transformation on synthetic unlabeled data to map the intermediate activations of a data-constrained "student" (using partial context) toward those of a full-context "teacher" (using all data). Training the aligner requires no GPU and converges in seconds to minutes on commodity hardware. We evaluate on 38 classification datasets from the TabArena benchmark using the leading two tabular foundation models, TabPFN-3 and TabFM. Across all context budgets, the aligned student yields broad, statistically significant improvements over the unaligned baseline for both models. In low-data regimes, alignment recovers nearly half of the teacher's predictive advantage. The method provides a practical, low-overhead approach to achieving the inference speed of compact contexts while closing a significant fraction of the performance gap to the full-context teacher.

---


### 448. [Aligning Multimodal Patient Evidence with Biomedical Knowledge Graphs for Clinical LLMs](https://arxiv.org/abs/2610.06685)

**<font color=#1a73e8>作者：</font>** Jiawen Du, Arshan Ali Khan, Chenhao Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical questions often depend on linking a patient's multimodal evidence to external biomedical knowledge, yet existing predictive systems rarely represent such links explicitly, so they can neither be traced to their evidence sources nor removed to measure their contributions. We present MM-KG (Multimodal Knowledge Graph), which represents heterogeneous, multimodal patient observations and biomedical concepts as separate layers in one typed graph, joined by explicit alignment edges. First, modality-specific harmonizers convert EHR text, imaging, genomic, and biospecimen data into typed observations mapped to UMLS concepts, which a route-prioritized aligner links to a biomedical knowledge graph. Query-conditioned retrieval then selects a compact subgraph for downstream use by a large language model or a graph neural network. We build MM-KGs for MIMIC-IV and ADNI, and evaluate them with a 2x2 design that separates patient evidence, biomedical knowledge, and their interaction. On questions that require both sources, neither source alone performs far above chance, whereas their combination yields a drug-controlled AUROC interaction of +0.194 on MIMIC and +0.299 on ADNI. On held-out five-candidate ranking, MM-KG outperforms MindMap by +0.131 Hits@1 and leads an adapted GraphCare on the items that require consulting the patient, and deleting the single answer-bearing relation from the retrieved packet returns Hits@1 to the no-knowledge baseline. Finally, query-conditioned retrieval reaches 0.731 AUROC with 6.8x less context than the strongest generic policy, whereas static knowledge graph context gives no consistent gain on ordinary outcome prediction. Knowledge graphs thus benefit clinical LLMs not as background context but as explicit links between multimodal patient evidence and the relation a question requires, and MM-KG makes these links retrievable, traceable, and testable.

---


### 449. [OVAL: Output-Aware Local Page Bases for KV Cache Retrieval](https://arxiv.org/abs/2610.06686)

**<font color=#1a73e8>作者：</font>** Ashkan Shahbazi, Chayne Thrash, Soheil Kolouri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long context inference with large language models becomes increasingly expensive as attention must operate over an ever growing KV cache. Page sparse attention reduces this cost by representing each KV page compactly and retrieving only a subset for each query. Existing retrieval methods are designed to estimate attention scores or page relevance, but their objectives do not directly account for how approximation errors affect the resulting value weighted attention output. We introduce \method{}, an output aware page encoding derived from the joint structure of keys and values while preserving the key information needed for accurate retrieval. \method{} is training free and requires no additional value dependent statistics at inference time. Once constructed, its stored representation has the same size and decode time scoring cost as a key only spectral representation. Across long reasoning, long context understanding, and long generation benchmarks, \method{} consistently improves over the key only spectral baseline and performs competitively with recent KV cache compression and retrieval methods. On long reasoning benchmarks, it achieves strong avg@\(k\) performance across model benchmark pairs, while matching or surpassing leading baselines on several long context understanding and generation settings with modest decoding overhead. Code is available at \url{this https URL}.

---


### 450. [MedPrune: Topology-Efficient Multimodal Multi-Agent Communication Evolution for Medical VQA Tasks](https://arxiv.org/abs/2610.06695)

**<font color=#1a73e8>作者：</font>** Jiuheng Wan, Runze Li, Chen Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While medical multimodal large language models (Med-MLLMs) advance medical visual question answering (VQA), existing clinical workflow-inspired multi-agent frameworks suffer from interaction patterns and excessive computational overhead caused by redundant communication topologies. In this paper, we propose MedPrune, an efficient medical multimodal multi-agent collaboration framework that dynamically prunes both nodes and edges from the communication topology to enhance reasoning ability and token efficiency. Specifically, we first formulate the diagnostic process as a heterogeneous communication graph, where nodes represent specialist agents from various departments and edges capture intra- and inter-departmental interactions. Building on this graph, we introduce two sparsification mechanisms to enable adaptive collaborative evolution: (1) Heterogeneous Node Sparsification, which eliminates task-irrelevant specialist agents irrelevant to the current multimodal question via reinforcement learning-driven topological optimization, and (2) Heterogeneous Edge Sparsification, which selectively retains only the most diagnostically salient intra- and inter-departmental connections by jointly optimizing task performance and topological complexity. Extensive medical VQA experiments under full-set and few-shot training settings prove MedPrune surpasses multi-agent baselines and boosts token efficiency with strong adversarial robustness.

---


> [!TIP]
> 当前位于：**401-450**（第 9/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-505](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
