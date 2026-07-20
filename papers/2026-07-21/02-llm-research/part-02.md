# 🧠 大模型相关研究 | 2026年07月21日

> 本类共 **75** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-75**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-75**

---

### 51. [Induction in Both Directions: A Mechanistic Analysis of In-Context Learning in Masked Diffusion Language Models](https://arxiv.org/abs/2607.15893)

**<font color=#1a73e8>作者：</font>** Andy Catruna, Emilian Radoi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While the internal mechanisms of autoregressive (AR) transformers have been studied extensively, much less is known about diffusion language models (DLMs), an emerging alternative that generates text by iterative denoising. In this work, we study how DLMs implement induction, a mechanism behind in-context learning in which the model finds a repeated context and copies the token that followed it. Our analysis compares attention-only AR models and absorbing-mask DLMs with matched architectures. We find that DLMs learn a bidirectional induction circuit, where previous-token and next-token heads write local context into the residual stream and later induction heads use it to find and copy the answer from the matching source position. The circuit is direction-symmetric, working whether the source appears in the past or in the future. When only left context is visible, matching what an AR model sees, the DLM does not outperform its AR counterpart in induction capabilities. However, we observe it has stronger induction when both sides of the masked token are visible, pointing to bidirectional context access rather than a stronger one-sided mechanism. Beyond induction, we provide causal evidence that DLMs compute the global fraction of masked tokens and use it as an implicit timestep, even though they are given no explicit timestep embedding.

---


### 52. [Orbis 2: A Hierarchical World Model for Driving](https://arxiv.org/abs/2607.15898)

**<font color=#1a73e8>作者：</font>** Sudhanshu Mittal, Arian Mousakhan, Silvio Galesso 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current world models operate at a single level of abstraction, with most prioritizing perceptual fidelity while lacking the spatial reasoning and semantic understanding required for real-world downstream tasks. We present a hierarchical driving world model that factorizes future prediction across two levels operating at distinct temporal and abstraction scales: a high-level predictor that forecasts coarse scene structure over extended temporal horizons, and a low-level generator that produces detailed predictions conditioned on the high-level output. This decomposition yields high perceptual fidelity while also capturing strong spatial and semantic representations. We further show that pretraining with a diffusion forcing objective yields substantially richer internal representations than the standard teacher forcing objective, while teacher forcing -- predicting only the next frame from clean context -- produces more stable autoregressive rollouts. We therefore introduce a generic two-stage training paradigm that pretrains the model with diffusion forcing and fine-tunes with teacher forcing, combining the representational benefits of the former with the rollout stability of the latter. Our approach achieves state-of-the-art results across the standard suite of driving world model evaluations on established benchmarks, including long-horizon generation fidelity, steering responsiveness evaluated on counterfactual scenarios, and internal representation quality. Project page with code, demo, checkpoints and qualitative results: this https URL

---


### 53. [ContinuityBench: A Benchmark and Systems Study of Stateful Failover in Multi-Provider LLM Routing](https://arxiv.org/abs/2607.15899)

**<font color=#1a73e8>作者：</font>** Vishal Pandey, Gopal Singh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In production large language model (LLM) deployments, high API availability guarantees do not equate to conversational continuity. When a primary provider experiences an outage or strict rate-limiting, naive stateless failover mechanisms successfully maintain uptime but silently discard conversation history, severely disrupting the user experience. To rigorously quantify and resolve this failure mode, we introduce two novel metrics: Continuity Preservation Rate (CPR) and Continuity Latency Overhead (CLO). We propose a stateful, multi-provider proxy architecture utilizing a History-Forwarding strategy to seamlessly reconstruct conversational state across heterogeneous LLM endpoints during failover events. Furthermore, we release continuity-bench, this https URL, an open evaluation harness designed to stress-test context preservation under high-concurrency provider failure conditions. Our empirical evaluation ($N=750$ failover events) demonstrates that our stateful proxy achieves a 99.20\% CPR [95\% CI: 98.27\%, 99.63\%], cleanly transferring deep conversational context to fallback providers, compared to a near-0\% preservation rate for standard stateless architectures. Finally, we characterize failover latency distributions, identifying the critical necessity of asynchronous exponential backoff with jitter to prevent cascading retry storms against strict-limit fallback APIs. Our results provide a principled foundation for building robust, state-preserving multi-model inference systems.

---


### 54. [DSWorld: A Data Science World Model for Efficient Autonomous Agents](https://arxiv.org/abs/2607.15901)

**<font color=#1a73e8>作者：</font>** Zherui Yang, Fan Liu, Hao Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite strong capabilities in data understanding and decision-making, autonomous data science agents still heavily rely on trial-and-error workflows that involve expensive computation. This bottleneck motivates models that can anticipate the effects of data science operations before real execution. In this paper, we introduce the concept of Data Science World Model, which model the data science execution environment by predicting environment state transitions conditioned on current workflow states and candidate operations. We further propose DSWorld, a practical framework that combines structured state construction, cost-aware routing, lightweight real execution, and an LLM-based simulator for expensive operations. To support training, we construct an 8K-scale transition trajectory dataset and introduce Reflective World Model Optimization, an error-aware reinforcement learning strategy for improving transition prediction. Experiments show that DSWorld accelerates RL-based agent training by approximately $14\times$ and search-based inference by approximately $3$-$6\times$ while maintaining competitive performance, and outperforms the strongest LLM baseline by 35.6% on transition prediction tasks. The code is available at this https URL.

---


### 55. [HETA++: Global Structure-from-Motion with Hybrid Explicit Translation Averaging](https://arxiv.org/abs/2607.15912)

**<font color=#1a73e8>作者：</font>** Peilin Tao, Hainan Cui, Mengqi Rong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Global Structure-from-Motion (SfM) offers advantages over incremental methods in terms of efficiency and error distribution. However, the task of translation averaging remains challenging. Many existing methods rely solely on relative translations or feature tracks, which either degrade under collinear camera motion or are susceptible to outliers. In this paper, we propose a novel hybrid explicit translation averaging framework that incorporates both relative translations and feature tracks. Specifically, we first refine the relative translations using global camera rotations and remove globally inconsistent relative translations. Next, we employ convex distance-based objective functions to estimate the initial camera positions and 3D points, followed by refinement using a non-bilinear angle-based objective function. Furthermore, since camera rotations are fixed during translation averaging, inaccurate camera rotations can severely limit the accuracy of camera positions. To address this issue, we then robustly refine both camera rotations and camera positions with selected feature tracks through bounded angle-based refinement and subsequent reprojection-based bundle adjustment. In this step, feature tracks are selected to maintain a balanced spatial distribution and improve optimization efficiency. Finally, we perform a complete bundle adjustment using all reliable feature tracks to refine the camera parameters and 3D points. Extensive experiments on various sequential and unordered real-world datasets demonstrate the superior accuracy, robustness, and scalability of our approach, outperforming state-of-the-art methods in both accuracy and computational efficiency.

---


### 56. [Knowledge-Guided Cross-Modal Fusion for Adult-to-Pediatric ECG Transfer via Label-Conditioned Contrastive Alignment](https://arxiv.org/abs/2607.15928)

**<font color=#1a73e8>作者：</font>** Xinran Liu, Yuwen Li, Hongxiang Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adult and pediatric electrocardiogram (ECG) interpretation relies on age-sensitive criteria, and models pretrained mainly on adult ECGs often transfer poorly to pediatric populations when pediatric labels are scarce. Existing multimodal ECG--text methods typically align waveforms and text at the global sample level, entangling evidence from co-occurring diagnoses and limiting transfer under this gap. We propose Pediatric-Adult ECG Alignment via Cross-modal Enhancement (PEACE), a knowledge-guided framework pretrained on the largely adult MIMIC-IV ECG corpus. PEACE describes each diagnosis along rhythm, morphology, and ST--T axes and, per recording, composes only positive-label descriptors into three axis tokens and a fused embedding. A label query network (LQN) uses diagnostic labels as queries to cross-attend over ECG tokens and axis tokens, while label set aware bidirectional contrastive learning (LSBC) aligns pooled ECG features with the fused embedding when recordings share diagnoses. Curriculum adaptive fusion (CAF) gates alignment strength according to smoothed classification loss and training progress, limiting disruption during early optimization. The knowledge branch is used only for training supervision; inference uses ECG signals alone. On ZZU-pECG, PEACE reaches macro average AUCs of 59.39%, 81.74%, and 91.56% under zero-shot, 50-shot, and full fine-tuning, with the clearest gains over foundation and knowledge-pretraining baselines under limited supervision; versus domain adaptation initializations, zero-shot improves substantially while 50-shot AUC is comparable to DANN. After fine-tuning on PTB-XL, PEACE reaches 96.90% macro average AUC over nine harmonized labels. Ablations confirm that label-conditioned knowledge alignment, rather than global text fusion, is the key driver of pediatric transfer gains.

---


### 57. [From Plausible to Actionable: A Position on LLM Self-Explanations](https://arxiv.org/abs/2607.15957)

**<font color=#1a73e8>作者：</font>** Elize Herrewijnen, Benedetta Muscato, Gizem Gezici 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) can generate natural language explanations that rationalize their own decisions, a phenomenon commonly referred to as this http URL explanations have emerged as a promising direction for explainable artificial intelligence (XAI), particularly for interpreting LLM this http URL, while self-explanations often appear plausible, whether they faithfully reflect a model's underlying reasoning process remains an open question. In this opinion paper, we argue that self-explanations can be highly plausible, questionably faithful, and yet highly actionable. From a traditional XAI perspective, we identify the limitations of standard evaluation protocols for LLM-generated self-explanations and propose practical guidelines for assessing their plausibility and faithfulness. Moreover, we argue that evaluation should extend beyond these criteria to actionability, highlighting applications of LLM rationalization capabilities that support informed decision-making and appropriate action across diverse stakeholders.

---


### 58. [A Human-Centric Evaluation of a Retrieval-Augmented Generation System for Explaining Quebec Insurance Contracts](https://arxiv.org/abs/2607.15963)

**<font color=#1a73e8>作者：</font>** David Beauchemin, Richard Khoury  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> With the rise of online insurance sales, consumers face a significant \enquote{advice gap}, requiring them to navigate complex legal contracts without expert guidance. This paper presents a human-centric, extrinsic evaluation of a state-of-the-art Retrieval-Augmented Generation system, designed to make Quebec automobile insurance contracts more understandable. Through a user study with 154 participants from Laval University, we assess the agent's real-world utility by measuring system satisfaction, cognitive effort, perceived autonomy, and risk. Our results show the system is perceived as a \enquote{cognitive equalizer}, receiving high ratings for satisfaction, trust, and clarity. Crucially, users value the sense of autonomy the system provides even more than the knowledge itself, with this effect being most pronounced among participants with lower financial literacy, demonstrating how such an agent can directly empower individuals. However, our study also highlights some limitations: participants expressed a strong preference for human agents in high-stakes or emotionally charged scenarios. This work highlights the importance of human-in-the-loop frameworks in ensuring the responsible implementation of AI in high-stakes consumer finance.

---


### 59. [BayesPO: Bayesian Prompt Optimization via Parallel-Tempered Gradient-Guided Discrete MCMC](https://arxiv.org/abs/2607.16001)

**<font color=#1a73e8>作者：</font>** Junjie Zhou, Zhijian Ou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prompt optimization adapts large language models (LLMs) without updating model parameters, but many automatic prompt optimizers remain heuristic search procedures over candidate instructions. This paper studies prompt optimization as Bayesian posterior sampling over discrete prompt tokens. We define a posterior distribution by combining a task likelihood term, which rewards prompts that explain input-output examples, with a language-model prior, which favors fluent instructions. This converts prompt optimization into an energy-based posterior sampling problem, for which gradients can be used to guide discrete Markov chain Monte Carlo (MCMC) proposals over vocabulary tokens. We refer to our framework as BayesPO, short for Bayesian Prompt Optimization. In this paper, BayesPO is instantiated with Markov chain Monte Carlo: it uses a Metropolis-Hastings corrected Gibbs-with-Langevin (GwL) proposal and integrates parallel tempering for global exploration of rugged LLM-induced energy landscapes. The concrete sampler further adapts the GwL sampler to the practical constraints of non-weight-tied LLM embeddings. Experiments with Qwen2.5 models show that the sampler discovers semantically meaningful prompts on diagnostic tasks, that parallel tempering helps escape a local optimum in a poetry completion task, and that post-optimizing APE prompts on 24 instruction-induction subtasks improves average accuracy from 60.04% to 63.23%. The study also reveals two main limitations: energy minimization may overfit small optimization sets, and the current sampler remains computationally expensive. These findings position Bayesian prompt sampling as a principled post-optimization tool and point to a promising direction for probabilistic prompt optimization.

---


### 60. [Revisiting data-driven dynamic security assessment with a tabular foundation model](https://arxiv.org/abs/2607.16031)

**<font color=#1a73e8>作者：</font>** Olayiwola Arowolo, Maosheng Yang, Jochen Cremer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data-driven pre-fault dynamic security assessment (DSA) rapidly evaluates the dynamic risk of credible contingencies on a power system using machine learning. Existing approaches face two limitations. First, they require a large labelled database for training, with a separate model trained, tuned, and maintained for each contingency in a potentially long list of credible contingencies. Second, the trained models generalize poorly to unseen contingencies. This work addresses the limitations by using a tabular foundation model (TFM) that assesses stability through in-context learning, requiring no retraining or hyperparameter optimization. A single TFM can assess many contingencies at once, removing the need for one model per classifier. We also characterize when the use of electrical distance coordinates (EDC) as continuous features enables generalization of TFM to unseen contingencies and when they do not, demonstrating how a few labelled samples can reliably improve generalization. Through comprehensive case studies on the IEEE 68-bus system, we show that a single TFM attains an average Macro F1 score of about 90% with only 120 labelled samples per contingency, roughly two orders of magnitude fewer than conventionally assumed, without any model retraining or hyperparameter tuning. For new/unseen contingencies, we show that using just 10 labelled samples of the new contingency with EDC encoding matches the best achievable transfer learning oracle model, which requires fully labelled data and is not deployable in practice. Overall, this initial study paves the way towards developing and deploying foundation models for power system operations, with possible applications across multiple operational tasks.

---


### 61. [SciForge: An AI-Native, Multimodal Workbench for Scientific Discovery](https://arxiv.org/abs/2607.16038)

**<font color=#1a73e8>作者：</font>** SciForge Team, Zhangyang Gao, Minghao Fang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific work increasingly spans heterogeneous artifacts -- papers, code, datasets, scientific file formats, model outputs, figures, manuscripts, and team decisions -- yet general-purpose AI assistants rarely preserve these objects as a coherent, auditable research state. We present SciForge, a multimodal research-native AI workbench that reserves the graphical interface for human judgment while search, parsing, model routing, workflow execution, plotting, writing, and presentation generation run as modular agent-accessible services. SciForge is built around five pillars: (i) \emph{goal-scoped scientific decision governance} for \textbf{goal-oriented} research, with review gates and shared review surfaces; (ii) \emph{translate-then-reason} for \textbf{multimodal} input, routing scientific objects through domain translators before the agent reasons; (iii) \emph{evidence governance} for \textbf{auditable} traceability, linking claims to provenance chains and audit findings; (iv) \emph{collaborative team science} for \textbf{collaborative} research, enabling multi-role decision governance, with shared team workspaces planned for future releases; and (v) \emph{real-world application scenarios} for \textbf{practical} impact, demonstrated through eight end-to-end user cases, with flagship demonstrations including multi-day agentic research sprints for gene discovery, AI-guided de novo protein design, molecular optimization, and genome-to-BGC discovery. The system combines a thin interaction layer, contextual research capability patterns, an Agent Runtime and Workflow Engine, an Evidence-DAG audit sidecar and a Scientific Model Router. SciForge currently runs as a desktop application, with mobile supervision support; future releases will deepen team collaboration. The system is open-source and available at this https URL

---


### 62. [DELUGE: Towards Continental-Scale Daily Pluvial Flood Damage Prediction via Interpretable Conditioning on Foundation Model Embeddings](https://arxiv.org/abs/2607.16050)

**<font color=#1a73e8>作者：</font>** Yuya Kawakami, Daniel Cayan, Dongyu Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pluvial (rainfall-driven) flooding accounts for 45% of National Flood Insurance Program (NFIP) claims in the United States and is harder to predict than its riverine and coastal counterparts, with existing approaches limited to coarse resolution, regional domains, or computationally intensive process-based models unsuitable for daily continental-scale use. We present DELUGE, a multimodal deep learning framework for daily pluvial flood damage prediction at ~1 km resolution and national scale, trained on spatially and temporally corrected NFIP claims (2017-2022) and structured around the hazard, exposure, and vulnerability components of disaster risk. Rather than blanket coverage of the Conterminous United States (CONUS), we model the top 100 highest-claim 75 km cells, distributed nationwide and accounting for ~81% of total pluvial flood claims. Our architectural novelty is a pair of parametric modules in the hydrometeorology branch, a Value Modulator and a Temporal Modulator, conditioned on terrain descriptors and AlphaEarth foundation-model embeddings, that expose directly inspectable hydrological response parameters and provide architecture-level interpretability-by-design. Under a spatial block holdout, DELUGE outperforms tuned Random Forest, XGBoost, and LightGBM baselines by 9% to 30% on a dollar-weighted area under the precision-recall curve (PR-AUC), a metric that emphasizes the rare, high-cost claims of greatest operational interest. Beyond DELUGE, we argue this interpretable conditioning scheme is a transferable pattern for integrating foundation-model embeddings into other geospatial prediction tasks.

---


### 63. [Frontier AI performance across the business disciplines: a case-grounded benchmark of knowledge work and analytical reasoning](https://arxiv.org/abs/2607.16057)

**<font color=#1a73e8>作者：</font>** Ajay Patel, Kartik Hosanagar, Ramayya Krishnan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are improving rapidly as reflected in benchmark scores, yet these AI benchmarks largely test capabilities such as factual recall, narrow question answering, mathematical problem-solving, and coding and agentic tool-use. What remains poorly measured is AI progress on the analytical knowledge work white-collar professionals perform daily, including synthesizing complex information, exercising judgment under uncertainty and incomplete information, applying strategic and adversarial thinking in multi-stakeholder settings, weighing trade-offs, and producing defensible, structured analyses. This gap is even more pronounced for subjective components of such work, where success can be challenging to define. The "case method" form of education practiced by top business schools provides a natural foundation for addressing this measurement gap, and we construct BusinessCaseBench, a benchmark spanning hundreds of questions drawn from business cases across eighteen disciplines, each paired with a grading rubric derived from the expert-written instructor case solution. On BusinessCaseBench, frontier AI models already score highly against instructor rubrics, and capability within one model family improves substantially over two years. These results provide strong evidence that AI performance on this class of work is already high and rapidly improving, with implications for business schools, where case pedagogy trains undergraduates and MBAs in this kind of analytical reasoning, and for entry-level professional roles, where such skills have historically anchored early-career work.

---


### 64. [Frontier Language Models Struggle to Copy: Text Can Be Better Viewed in 2D](https://arxiv.org/abs/2607.16072)

**<font color=#1a73e8>作者：</font>** Haodong Wen, Yiran Zhang, Yingfa Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While large language models (LLMs) can solve advanced reasoning problems in seconds, we show that even frontier models fail to perform a much simpler operation: exactly copying an input string that lies well within their context windows. We attribute this failure to positional encodings in Transformer architectures, whose inductive bias favors copying through a shortcut based on matching local contexts rather than carefully locating the corresponding input positions. To address this issue, we introduce 2D-RoPE, which organizes text into a 2D grid rather than a 1D sequence and assigns each token a row ID and a column ID. Under this view, copying becomes simply retrieving input tokens at a fixed column offset, which makes the task easy to learn. In synthetic copy experiments, shallow Transformers with 2D-RoPE achieve perfect copying at input lengths hundreds of times longer than those seen during training, whereas standard positional encodings fall far behind. We further show that the advantage of 2D-RoPE language models on copy tasks consistently holds in large-scale pretraining on DCLM with model sizes up to 1.4B parameters. Overall, our results suggest that viewing text in 2D can benefit language modeling, and we hope this encourages future work to further explore the potential of 2D positional encodings.

---


### 65. [HCIG: A Hierarchical Cross-Modal Incongruity Graph Network for Multimodal Sarcasm and Cyberbullying Detection](https://arxiv.org/abs/2607.16076)

**<font color=#1a73e8>作者：</font>** Bhavana Verma, Priyanka Meel, Dinesh Kumar Vishwakarma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal sarcasm and cyberbullying detection remain challenging because the intended meaning often emerges from incongruity between textual and visual information rather than from either modality alone. Existing multimodal approaches primarily rely on feature fusion or cross-modal attention, which may not effectively capture hierarchical semantic inconsistencies across different levels of representation. To address this limitation, this paper proposes HCIG (Hierarchical Cross-modal Incongruity Graph Network), a novel framework that models cross-modal incongruity at token, phrase, and global levels using graph attention networks and adaptively integrates these representations through a learned hierarchical attention mechanism. As a complementary architecture, we also introduce GCCN (Graph-based Cross-modal Contradiction Network), which performs graph-based reasoning using contradiction-aware pooling for efficient multimodal interaction learning. The proposed models are evaluated on the MMSD sarcasm benchmark and the MultiBully cyberbullying dataset, together with comprehensive ablation studies and cross-task transfer experiments. Experimental results demonstrate that HCIG achieves the best performance on MMSD with 85.74% accuracy and 85.29% macro-F1, while GCCN attains the highest macro-F1 (68.66%) on MultiBully and HCIG achieves the highest accuracy (69.62%) and bullying-class F1 (74.90%). The findings demonstrate that hierarchical multi-granularity incongruity modeling provides more effective multimodal reasoning than conventional fusion strategies, offering a robust framework for sarcasm and cyberbullying detection in social media.

---


### 66. [How Do VLMs Fail? Vision-Operation Misalignment in Compositional VQA](https://arxiv.org/abs/2607.16094)

**<font color=#1a73e8>作者：</font>** Navya Gupta, Bingjie Xu, Avinash Anand 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Compositional visual question answering requires Vision-Language Models (VLMs) to execute multiple reasoning operations like object selection, spatial relation resolution, and attribute verification. Despite strong aggregate performance, the mechanistic basis of VLM failures on this task remains underexplored. To address this gap, we analyze vision-operation misalignment in VLMs by examining how failures relate to specific reasoning operations and the internal computational pathways through which they arise and propagate. We introduce an Operation-centric mechanistic framework that decomposes VLM failures by both the reasoning operation where they originate and the internal computational pathway through which they propagate. Our analysis reveals four mechanistically distinct failure modes: grounding failure, reasoning failure, attribute extraction failure, and language prior dominance failure. Each characterized by a unique relationship between visual grounding strength and answer correctness. Through three complementary causal interventions applied across all transformer layers, we further demonstrate a pathway dissociation: grounding failures route exclusively through the feedforward network, reasoning failures route through late-layer attention, and attribute extraction failures localize to the answer-position feedforward computation. This dissociation demonstrates that different failure types require fundamentally different corrective strategies, providing a principled foundation for targeted improvements to VLM reliability in multimedia reasoning.

---


### 67. [Understanding Reasoning from Pretraining to Post-Training](https://arxiv.org/abs/2607.16097)

**<font color=#1a73e8>作者：</font>** Jingyan Shen, Ang Li, Salman Rahman 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become central to improving large language models (LLMs) on complex reasoning tasks, yet RL post-training is largely studied in isolation from the pretraining that precedes it. As a result, two basic questions remain open: (1) how do pretraining choices (model size, data) shape the returns to RL compute, and (2) what does RL actually do to the model? These questions are difficult to study in the standard LLM setting: pretraining corpora are vast and uncontrolled, making it hard to attribute behaviors to pretraining versus RL, and systematic compute sweeps across both stages are prohibitively expensive. To address these challenges, we use chess as a controlled testbed for studying reasoning across the full pretraining-to-post-training pipeline. We follow the standard LLM training pipeline by pretraining language models from 5M to 1B parameters on human chess games, supervised fine-tuning on synthetic reasoning traces, and running RL on chess puzzles with verifiable rewards. Using this framework, we find that the post-RL performance at given RL compute level is well-predicted from the pretraining loss, and slope of the RL reward curves improves approximately linearly with the pretraining tokens. Beyond scaling, we find that RL does not simply sharpen the SFT policy: on easy puzzles it amplifies correct moves the SFT policy already preferred, while on hard puzzles it surfaces correct moves that were nearly absent under SFT. We further test whether our findings transfer beyond chess by training a 1B language model on math-domain text, where the same predictive pattern emerges: longer-pretrained checkpoints reach higher post-RL performance and improve faster under RL. In sum, we provide a quantitative account of the pretraining-to-RL interface and a controlled testbed for studying the science of reasoning across the full pretraining-to-post-training pipeline.

---


### 68. [The Honest Quorum Problem: Epistemic Byzantine Fault Tolerance for Agentic Infrastructure](https://arxiv.org/abs/2607.16109)

**<font color=#1a73e8>作者：</font>** Jun He, Deying Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State machine replication (SMR) and Byzantine fault-tolerant (BFT) consensus guarantee agreement despite a bounded number of arbitrary, colluding faulty participants. However, these guarantees rely on participants outside this set correctly executing the protocol's transition semantics. Agentic validators expose a weaker boundary: an authenticated, responsive, non-equivocating, and protocol-compliant reasoning participant may still endorse a semantically invalid transition due to reasoning errors.
We call this failure mode an epistemic fault, and the collective phenomenon the Honest Quorum Problem (where "honest" means protocol-compliant, not semantically correct). Such a quorum can satisfy ordinary checks while forming a certificate for an invalid transition. Thus, agreement alone does not guarantee semantic validity or execution safety. Furthermore, because agentic validators often share model weights, training distributions, prompts, or toolchains, they are highly susceptible to correlated epistemic faults.
We define Epistemic Byzantine Fault Tolerance (EBFT), a fault-tolerance model for agentic infrastructure and post-deterministic distributed systems. EBFT augments the conventional Byzantine fault bound with two separate, confidence-indexed quantities: $e_\delta$ bounds coherent invalid endorsements outside the Byzantine set, and $u_\epsilon$ bounds unusable validator support that degrades liveness. These quantities characterize semantic safety risk and liveness degradation independently. We derive quorum-threshold conditions for semantic validity, consensus agreement, liveness, and feasible threshold selection, and outline a calibration methodology for estimating these budgets. We show that adding nominally distinct agents improves fault tolerance only when it measurably reduces the upper-tail concentration of invalid endorsements or unusable support.

---


### 69. [CRAFT: Clustering Rubrics to Diagnose Weak LLM Capabilities and Generate Targeted Fine-Tuning Data](https://arxiv.org/abs/2607.16122)

**<font color=#1a73e8>作者：</font>** Vipul Gupta, Zihao Wang, Razvan-Gabriel Dumitru 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluations should do more than measure a models current performance. They should tell us what to fix for the next model iteration and provide a way to generate targeted post training data. Most evaluation pipelines identify weak examples, topics, or categories, but they leave the underlying capability failure implicit: they say where a model fails, not why. We introduce CRAFT, a method that converts any rubric based evaluation dataset into a model specific diagnosis of weak capabilities. CRAFT treats each grading criterion as a capability probe: it extracts a capability description from every prompt rubric pair, clusters these descriptions into a hierarchical capability tree, scores the target model at every node, and selects low performing nodes dynamically across tree levels, at the granularity where each failure is clearest. The selected weak capabilities then direct the generation of targeted supervised finetuning data. Holding the data generation, finetuning, and evaluation setup fixed, we compare CRAFT against prompt level EvalTree clustering and untargeted random generation on four open source models, two professional domains (finance and legal), and 13 held out benchmarks disjoint from the diagnostic data. CRAFT achieves the strongest finance domain average for all four models under repeated temperature decoding; on legal domain, it is strongest for three of four models and remains within the decoding variance bands of the best baseline on the fourth. Diagnosing weaknesses at the level of rubric criteria, rather than prompts or categories, thus yields both a sharper picture of what a model cannot do and measurably better models after finetuning on that diagnosis.

---


### 70. [ToolSciVer: Multimodal Scientific Claim Verification with Visual Tool Augmented Reinforcement Learning](https://arxiv.org/abs/2607.16131)

**<font color=#1a73e8>作者：</font>** Binglin Zhou, Peng Shi, Ryo Kamoi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Scientific Claim Verification (MSCV) requires models to verify scientific claims using visually grounded evidence from papers, including figures, tables, charts, and textual context. However, existing methods often fail because they struggle to locate decisive visual evidence, accurately read structured scientific visuals, and integrate multimodal observations into reliable reasoning. We introduce ToolSciVer, the first tool-augmented framework for MSCV to our knowledge. ToolSciVer equips a VLM with three type-aware visual tools, table row/column focus, chart-to-structure parsing, and high-resolution region zoom, which convert dense scientific visuals into explicit, claim-facing evidence, and trains the policy with Group Relative Policy Optimization (GRPO) under a composite reward of answer correctness, format validity, length control, tool-use efficiency, and tool-validity penalties. Experiments on SciVer and MuSciClaims datasets on five VLMs from three model families (Qwen, InternVL, Gemma) demonstrate that our method achieves superior performance compared to four competitive baselines including prompting-based and RL-based tool-use methods, highlighting the effectiveness of learned, type-aware tool use for scientific claim verification.

---


### 71. [An Exam for Active Observers](https://arxiv.org/abs/2607.16165)

**<font color=#1a73e8>作者：</font>** Jiarui Zhang, Muzi Tao, Shangshang Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human vision is a closed loop: gaze is continuously redirected by intermediate hypotheses rather than a single snapshot. Decades of psychophysics and cognitive science have argued that this active observation is essential for a wide range of tasks. Whether today's multimodal large language models (MLLMs) exercise active observation is an empirical question that current vision-language benchmarks do not answer. We introduce ActiveVision, a benchmark that makes active observation measurable for MLLMs, comprising 17 tasks across 3 categories. Tasks are designed to force repeated visual perception rather than a single static description. Frontier MLLMs collapse on ActiveVision: the highest-scoring model we evaluate, GPT-5.5 at the highest exposed reasoning-effort tier, solves only 10.6% of items and scores zero on 11 of the 17 tasks, and even Claude Fable 5, despite topping most reasoning and coding leaderboards, solves just 3.5%, far behind three human participants who average 96.1%. Furthermore, much of the gap persists even when models write and run their own vision code: such code is unreliable on realistic imagery, and catching its failures itself requires the active perception the models lack. Together, these results indicate that current MLLMs lack robust active visual observation, motivating architectures and training objectives that close the perception-reasoning loop.

---


### 72. [When Does Muon Help Agentic Reinforcement Learning?](https://arxiv.org/abs/2607.16169)

**<font color=#1a73e8>作者：</font>** Kai Ruan, Jinghao Lin, Zihe Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon is competitive with AdamW in large-scale pre-training, but its value for reinforcement-learning (RL) post-training remains unclear. We study vanilla Muon in sparse-reward agentic RL through matched single-seed comparisons with AdamW on ALFWorld using Qwen2.5-0.5B-Instruct. Under Group-in-Group Policy Optimization (GiGPO), applying Muon only to hidden weight matrices raises final-window validation success from 0.290 to 0.546 (+88%); high-rate AdamW controls retain no post-update success. The effect depends on the advantage estimator and learning rate. At 3e-5, Muon improves GRPO from 0.161 to 0.268, whereas GraphGPO's late-window gap narrows near saturation. At 1e-5, GraphGPO Muon reaches 0.901, raises normalized validation AUC from 0.399 to 0.556, and reaches 0.5 and 0.75 success 30 and 60 updates earlier, respectively. These exploratory results show that Muon can benefit agentic RL and motivate studying the policy optimizer, advantage estimator, and learning rate jointly. Multi-seed and cross-task validation remain open.

---


### 73. [Vision-Language Assistant for Emotional Reactions to Risky Driving](https://arxiv.org/abs/2607.16181)

**<font color=#1a73e8>作者：</font>** Harine Choi, Eun Hak Lee, Zhengzhong Tu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This study introduces a vision-language pipeline that detects risky driving behaviors and generates emotionally expressive responses to support driver awareness and comfort. Although vision-language models have advanced perception and reasoning in autonomous driving, existing systems rarely consider the emotional dimension or real-world user experience. Keep Yelling Assistant (KYA) detects high-risk driving maneuvers in real time, such as sudden cut-ins. It then produces emotional responses through a large language model tailored to driver preferences. The framework comprises two core modules. The vision module uses YOLOv8 variants to detect nearby vehicles and identify risky behaviors such as sudden cut-ins. Key driving metrics, including relative distance, speed, and projected reach time, are extracted and normalized to produce a structured behavior log. The language module processes this log with user-defined emotional tone settings, such as neutral, humorous, and analytical, and generates verbal reactions using state-of-the-art large language models, including ChatGPT-4o, Claude 3, Gemini 2.5, and Copilot. We evaluated the proposed system using dashcam videos containing risky driving behaviors and a user study involving 108 participants. Participants selected preferred response styles, and the large language models were evaluated based on emotional alignment. All models received favorable ratings, although preferences varied across personas. Notably, the combination of YOLOv8s and ChatGPT-4o achieved the highest score of 4.29 out of 5.00. By integrating real-world perception with emotionally adaptive dialogue, KYA introduces a new paradigm for emotionally intelligent in-vehicle artificial intelligence. It offers promising directions for improving safety, trust, and emotional well-being in both conventional and autonomous vehicles.

---


### 74. [PagedWeight: Efficient MoE LLM Serving with Dynamic Quality-Aware Weight Quantization](https://arxiv.org/abs/2607.16184)

**<font color=#1a73e8>作者：</font>** Yuchen Yang, Yifan Zhao, Anisha Dasgupta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) is a popular class of large language models (LLMs), offering high efficiency and accuracy. However, in KV-cache-intensive serving scenarios, MoEs often exhibit a tension between the GPU memory requirements of the model weights and the growing KV cache. We propose PagedWeight, a novel management method for MoE LLM serving that dynamically quantizes MoE model's weights at runtime and balances expert-weight precision with the KV cache sizes. PagedWeight exposes and effectively navigates the complex tradeoff between the model's task accuracy, memory consumption, and throughput/latency. Across several memory-sensitive MoE serving scenarios, PagedWeight improves the quality-memory tradeoff over several existing quantization baselines. PagedWeight achieves FP16-equivalent accuracy with up to 72.0% GPU memory savings and 1.94$\times$ throughput improvement, and improves quality over quantization methods by up to 39.3% at a similar memory budget with at most 4.1% throughput loss.

---


### 75. [Knowing the Self, Understanding the World: A Dual-Cognition Benchmark for UAV Spatio-temporal Reasoning with MLLMs](https://arxiv.org/abs/2607.16193)

**<font color=#1a73e8>作者：</font>** Like Liu, Zhengzheng Xu, Haitao He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models have achieved strong performance across diverse vision-language tasks, yet their capabilities in UAV scenarios remain insufficiently explored. Recent UAV-oriented benchmarks have begun to evaluate MLLMs in aerial scenarios, but they typically focus on scene understanding, event recognition, or navigation completion, rather than jointly assessing the dual-cognition capability required for UAV agents: reasoning about both the UAV's own state and the external environment in multiview spatio-temporal contexts. To address this gap, we present UAV-DualCog, a benchmark for aerial multiview spatio-temporal reasoning built on this dual-cognition perspective. UAV-DualCog includes both image and video tasks to jointly evaluate self-state and environment-state reasoning, while requiring spatial or temporal grounding beyond discrete answer prediction. We also develop an automated pipeline that constructs data from scene-level semantic point clouds, yielding a scalable benchmark with diverse scenes, hundreds of landmarks, and thousands of QA samples. Extensive evaluations show that current MLLMs remain far from reliable in UAV dual cognition. Self-state reasoning, viewpoint transformation, precise spatial grounding, and temporal interval localization are persistent bottlenecks, and additional validation with thinking/frontier models and a human baseline confirms that the benchmark is understandable to humans but challenging for existing models. We further construct UAV-DualCog-Train from disjoint scenes and show through a lightweight optimization probe that it provides useful structured supervision, suggesting its value not only as an evaluation benchmark but also as a data resource for advancing MLLM-based UAV agents. Project website and supplementary materials: this https URL

---


> [!TIP]
> 当前位于：**51-75**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-75**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
