# 🧠 大模型相关研究 | 2026年07月01日

> 本类共 **247** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-247](./part-05.md)

---

### 51. [EVLA: An Electro-Aware Multimodal Assistant for Physically-Grounded Driving Reasoning and Control](https://arxiv.org/abs/2606.28938)

**<font color=#1a73e8>作者：</font>** Yuxin Liu, Zihan Chen, Haoyu Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern vision-language models (VLMs) for driving assistants typically treat vehicle dynamics as a black box, resulting in decisions that lack awareness of the vehicle's real-time electro-mechanical state. To bridge this gap, we introduce the Electro-Visual-Language Assistant (EVLA) -- a novel framework that combines multi-modal scene understanding with real-time perception of the electrified powertrain state (e.g., motor torque, battery SOC). Our approach features two key innovations: first, a Unified Co-State Encoder (UCSE) that fuses visual, textual, and vehicle-state inputs into a shared latent representation, augmented with an Energy-Efficiency Field to model spatial energy costs; and second, an Electro-aware Structured Reasoning Chain (ESRC), which replaces external chain-of-thought prompting with an internal, deterministic reasoning process grounded in physical constraints and optimization objectives. Trained end-to-end with a physics-guided joint loss, EVLA learns to generate context-aware and energy-optimal driving decisions. Extensive evaluations on a driving QA benchmark demonstrate that EVLA substantially outperforms strong fine-tuned VLM baselines, improving the final score by +0.0871 and accuracy by +5.6\%. Ablation studies validate the necessity of each component, and efficiency analyses show that EVLA achieves 36\% faster inference than multi-stage pipelines. This work underscores that integrating vehicle-state awareness and structured physical reasoning is crucial for developing next-generation, physically-grounded driving assistants.

---


### 52. [When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration](https://arxiv.org/abs/2606.28958)

**<font color=#1a73e8>作者：</font>** Luís Brito, Carlos Baquero  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> LLM agents can share more than text. In some systems, an agent can send a short visible message while also passing its full KV-cache state to another model. This hidden state can help the final model combine evidence from several agents, but it is also hard to inspect. A visible message may look harmless even if the hidden state has been changed.
We study this problem in a multi-agent question-answering setup. Specialists each see part of the evidence, send a short commitment, and pass full KV-cache state to a coordinator. In clean runs, this latent collaboration improves over a matched text-only version. On transformed HiddenBench with Qwen3-4B, it reaches EM/F1 of 0.338/0.486, compared with 0.231/0.369 for text collaboration. Qwen3-8B and HotPotQA runs show the same direction of improvement.
The problem appears when one specialist is malicious. Some false visible commitments can steer answers. More seriously, changing the hidden KV state can collapse performance even when the visible commitment still looks plausible. A verifier that checks only text misses this failure mode. Simple magnitude checks catch some obvious corruptions, but adaptive attacks can evade them while still damaging the final answer.
The most reliable fix we find is not to guess whether hidden state looks normal, but to protect it in transport. We implement an HMAC-SHA256 manifest that binds the specialist, session, model, visible commitment, tensor metadata, and payload digest. It accepts all 774 honest replayed payloads and rejects all 295 recorded tampered payloads. The main lesson is that full-KV latent memory can be useful, but it should be treated as a security-sensitive object, not as ordinary internal model state.

---


### 53. [Expert Evaluation of Clinical AI Tools on Real Point-of-Care Clinical Queries](https://arxiv.org/abs/2606.28960)

**<font color=#1a73e8>作者：</font>** Jean Feng, Vishal Patel, Patrick Heagerty 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Physicians now pose millions of clinical questions to AI tools each week, yet these tools are evaluated largely on hypothetical or exam-style questions, not those actually asked in practice. We report a blinded evaluation built on 620 Real-world Point-Of-Care Queries (Real-POCQi) submitted to the OpenEvidence (OE) platform by physicians spanning 30 specialties, as well as 187 questions from HealthBench. 149 practicing physicians across 36 states made head-to-head comparisons between answers from three frontier general-purpose models (Claude Opus 4.8, Gemini 3.1 Pro, and GPT-5.5) and a specialized clinical tool (OE), with graders matched to each question's specialty. When comparing answers along five dimensions relevant to clinical decision support -- accuracy, clinical utility, source quality, verifiability, & completeness -- physicians scored the specialized tool highest on all axes; in the primary analysis on Real-POCQi, win differences (margins between win and loss rates) ranged from 25 to 39 percentage points (p<0.001). Results remained consistent in sensitivity analyses stratifying by citation display, answer length, OE-user status, and Real-POCQi versus HealthBench. In parallel, LLM judges were found to systematically differ from expert judges, though both generally agreed on the best model. These findings underscore two conclusions: (i) AI tool evaluations should reflect real-world query distributions and use expert judges that mirror the specialization defining modern medicine and (ii) the consistent advantage of the specialized tool over general-purpose models does not necessarily mean that the latter cannot serve similar purposes, but that targeted engineering and customization can yield meaningful gains in performance for its users. We release Real-POCQi as a public benchmark, as well as the prespecified statistical analysis for reproducing results of this study.

---


### 54. [Beyond the Mean: Three-Axis Fidelity for Aligning LLM-Based Survey Simulators from Small Pilot Data](https://arxiv.org/abs/2606.28963)

**<font color=#1a73e8>作者：</font>** Eun Cheol Choi, Youngrae Kim, Prabhu Pugalenthi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to simulate social survey responses, yet their outputs exhibit systematic biases: marginal distributions are skewed, response variance is poorly calibrated, and predictor-outcome relationships are attenuated. We ask a simple question: given a small pilot sample of human responses, can an LLM recover the statistical characteristics of a broader population? We decompose recovery along three axes: structural fidelity, marginal fidelity, and individual fidelity. Using a COVID-19 misinformation survey as a case study, we benchmark three families of approaches: prompting, rectification, and fine-tuning. The findings suggest that fine-tuning on small pilot samples offers a balanced approach for achieving multiple forms of fidelity, but the levels of such fidelity can vary across subsamples, potentially threatening pluralistic alignment.

---


### 55. [Self-Evolving Agentic Image Restoration via Deliberate Planning and Intuitive Execution](https://arxiv.org/abs/2606.28971)

**<font color=#1a73e8>作者：</font>** Shuang Cui, Fan Ji, Guanglong Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world image restoration (IR) remains challenging due to complex and coupled degradations. While recent agentic IR frameworks leverage Large Language Models for flexible tool planning, they face two critical limitations. First, from a search scheme perspective, excessive reliance on greedy strategies fails to balance exploration and exploitation. Second, existing agentic systems underutilize information, exhibiting episodic amnesia. To address these challenges, we propose \textbf{Self-Evolving Agentic Image Restoration (SEAR)}, which formulates restoration as a sequential decision-making problem. Inspired by the dual-process theory, SEAR comprises an Intuitive Executor and a Deliberate Planner, respectively following the fast-thinking \textit{System 1} and slow-thinking \textit{System 2} principles. The Deliberate Planner employs Pruning-Aware Monte Carlo Tree Search for long-horizon reasoning, utilizing a hybrid no-reference reward and a Multimodal Large Language Model (MLLM)-based tournament to prevent metric exploitation. Complementarily, the Intuitive Executor leverages a self-evolving episodic memory indexed by degradation-aware state fingerprints. This mechanism distills expensive search trajectories into adaptive expertise, overcoming episodic amnesia while progressively amortizing cold-start exploration costs through memory reuse. Extensive experiments on synthetic and real-world benchmarks demonstrate its strong perceptual and quantitative performance.

---


### 56. [Can LLMs Hire Fairly? Racial Bias in Resume Screening](https://arxiv.org/abs/2606.28978)

**<font color=#1a73e8>作者：</font>** Zhenyu Gao, Wenxi Jiang, Yutong Yan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We audit fourteen mainstream large language models (LLMs) for hiring discrimination using the paired-resume methodology of Kline, Rose, and Walters (2022). The sole 2023-vintage model reproduces the pro-White callback gap documented in field experiments on labor market discrimination ($+2.12$ pp, significant at the 1\% level). Every model released in 2024 or after shows either a null gap or a significant pro-Black reversal (up to $-3.01$ pp). The same pattern holds on the gender axis. Based on 24,024 paired postings per model across 14 models, our results document a reversal in the direction of algorithmic hiring bias across model generations.

---


### 57. [Learning from Acquisition: Metadata-driven Multimodal Pre-training for Cardiac MRI](https://arxiv.org/abs/2606.28991)

**<font color=#1a73e8>作者：</font>** Xueyi Fu, Liwei Hu, Zi Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cardiac magnetic resonance imaging (CMR) routinely records structured acquisition metadata, yet most CMR foundation models rely primarily on image-only pre-training and leave this naturally available source of weak semantic supervision largely underexplored. We propose MetaCLIP-CMR, a metadata-driven framework based on Contrastive Language--Image Pre-training (CLIP), which converts imaging modality, anatomical view, scanner vendor, field strength, and scanner model into textual supervision for CMR representation learning. The pretrained image encoder is evaluated on imaging modality classification, cine view classification, and cardiac segmentation. MetaCLIP-CMR achieves 86.8% modality accuracy and 86.5% cine view accuracy, clearly outperforming ImageNet and masked reconstruction initialisations. For downstream cardiac segmentation, MetaCLIP-CMR consistently obtains the highest Dice score across the evaluated ACDC and M&Ms cine short-axis (SAX) settings under both full-data and 20% fine-tuning regimes. Compared with recent image-focused large-scale CMR pre-training models, MetaCLIP-CMR achieves comparable ACDC segmentation performance, while requiring less than 1% of their pre-training image scale. These results suggest that metadata learning offers a natural and easy-to-use strategy for transforming routinely recorded acquisition information into effective supervision for foundation-level CMR representation learning, highlighting the promise of metadata-driven multimodal pre-training.

---


### 58. [Fine-Tuning General-Purpose Large Language Models for Agricultural Applications:A Reproducible Framework and Evaluation Protocol Based on Qwen3-8B](https://arxiv.org/abs/2606.28992)

**<font color=#1a73e8>作者：</font>** Zhaoyang Li, Ruijie Zhang, Jiaqi Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> General-purpose large language models (LLMs) have demonstrated strong abilities in opendomain question answering, information extraction, and text generation. Agricultural applications, however, are domain-specific, region-dependent, time-sensitive, and safety-critical. Without data governance, expert evaluation, and evidence constraints, an agricultural assistant mayproduce unreliable advice on crop diseases, pesticide use, fertilization, or policy this http URL avoid presenting unverified simulated numbers as real experimental findings, this paper doesnot report any model-performance claims that have not been produced by an actual training runand expert evaluation. Instead, we propose AgriTune-R, a reproducible and auditable frameworkfor adapting general-purpose LLMs to agricultural tasks. The framework selects the publiclyverifiable Qwen3-8B model as the recommended base model and integrates agricultural datagovernance, instruction construction, LoRA/QLoRA parameter-efficient fine-tuning, retrievalaugmented generation, expert evaluation, and safety control for high-risk questions. The contributions are: (1) a structured workflow for agricultural LLM adaptation; (2) an evaluationprotocol for agricultural knowledge QA, pest and disease consultation, cultivation management,and policy explanation; (3) an expert-review rubric combining factuality, safety, evidence consistency, and uncertainty expression; and (4) a clear separation between protocol design andempirical conclusions, providing an executable baseline for future empirical studies.

---


### 59. [Mural: Transferring LLM knowledge to image generation via Mixture-of-Transformers](https://arxiv.org/abs/2606.29013)

**<font color=#1a73e8>作者：</font>** Achin Jain, Jie An, Siddharth Chaudhary 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Leveraging capabilities of large language models (LLMs) in text-to-image (T2I) synthesis is an important research direction. In this work we investigate whether the knowledge of a frozen LLM can be effectively utilized in T2I generation when trained exclusively on standard text-image pairs. We integrate a frozen, reasoning-capable LLM with a diffusion-based image generator via shared attention within the Mixture-of-Transformers (MoT) architecture. Our experiments span two critical questions: (1) what degree of the LLM's intrinsic knowledge remains accessible during T2I training, and (2) what novel capabilities emerge in the resulting system. Across established benchmarks, our models achieve strong performance among unified understanding-generation systems: 0.85 on GenEval, 86.75 on DPG-Bench, and 0.66 on WISE with inference-time reasoning, using only text-image data. Remarkably, we uncover emergent behaviors absent from training data, including cross-lingual image generation, color-guided composition, emoji / ASCII scene construction, and generation directed by world knowledge. These results demonstrate that pretrained LLM knowledge can guide image synthesis under standard text-to-image training paradigms, without interleaved multimodal signals or explicit reasoning supervision. Our findings open new avenues for harnessing frozen model capabilities in resource-constrained multimodal learning.

---


### 60. [Customized Generative AI Agent for Transportation Engineering Practice: A Development and Continued Pre-training Guideline](https://arxiv.org/abs/2606.29014)

**<font color=#1a73e8>作者：</font>** Dianwei Chen, Yuan-Zheng Lei, Zifan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advancements in generative artificial intelligence (AI) and large language models (LLMs) have shown significant promise in automating complex reasoning, summarization, and question-answering tasks. However, the effectiveness of general-purpose LLMs in specialized engineering domains remains limited due to insufficient exposure to technical standards, engineering terminology, and domain-specific semantics. This study proposes a systematic approach to developing a customized generative AI agent for transportation engineering applications. A curated corpus of U.S. transportation manuals, design guidelines, and regulatory documents is used to conduct continued pretraining of six state-of-the-art LLMs through a unified low-rank adaptation (LoRA) framework. The training process is monitored to ensure convergence and model stability. Performance is evaluated using standard natural language processing metrics, including BLEU-4 and ROUGE, with Qwen2.5-7B and LLaMA-3.1-8B demonstrating the highest domain alignment and response quality. Results validate the effectiveness of LoRA-based adaptation in improving LLM performance on technical content interpretation and context-specific reasoning. This work contributes a reproducible development framework for constructing domain-specialized generative AI agents, supporting broader deployment in transportation research, design, planning, and policy analysis.

---


### 61. [Efficient Spatio-Temporal Grounding with Multimodal Large Models via Second-Level Tracking and RL Verification](https://arxiv.org/abs/2606.29023)

**<font color=#1a73e8>作者：</font>** Tianshu Zhang, Yan Wang, Ji Qi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatio-temporal grounding in long videos requires precise temporal localization and robust object tracking conditioned on natural-language queries. While recent vision-language models (VLMs) show strong reasoning ability, directly applying frame-by-frame inference to long sequences is computationally expensive and unstable. We propose a practical pipeline that shifts from frame-level to second-level tracking and performs cross-second smoothing to preserve continuity while reducing sequence length. To improve reasoning supervision, we synthesize chain-of-thought style trajectories using advanced multimodal models for temporal localization and target selection, and replace generated spatio-temporal coordinates with ground-truth annotations to avoid noisy supervision. We further optimize the policy with reinforcement learning using a verifier based on $t\_\mathrm{IoU}+mv\_\mathrm{IoU}$. Experiments across multiple FPS settings show that our method achieves a strong trade-off between efficiency and localization quality.

---


### 62. [Memory as an Attack Surface in LLM Agents: A Study on Multiple-Choice Question Answering](https://arxiv.org/abs/2606.29030)

**<font color=#1a73e8>作者：</font>** Shahnewaz Karim Sakib, Anindya Bijoy Das  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents extend conventional large language model (LLM) applications by integrating language understanding with task execution, external tool use, and memory mechanisms. While memory allows agents to retain prior interactions and provide more personalized and context-aware responses, it also introduces a new vulnerability: information stored in memory can influence future outputs even when the current query is clean. In this paper, we investigate memory manipulation in LLM-based agents for multiple-choice question answering. We first design and implement an LLM-based AI agent with an external memory component that stores and retrieves task-relevant information. We then introduce basic memory manipulation scenarios in which misleading or corrupted memories are inserted into the agent before it answers multiple-choice questions. Using a controlled experimental setup, we compare the agent's performance before and after memory manipulation and measure changes in answer accuracy, attack success rate, and selection of manipulated options. Our results show that even simple memory manipulations can noticeably affect the agent's final answers, causing it to select incorrect options despite receiving clean and well-formed questions.

---


### 63. [How to Leverage Synthetic Speech for LLM-Based ASR Systems?](https://arxiv.org/abs/2606.29031)

**<font color=#1a73e8>作者：</font>** Yanis Labrak, Dairazalia Sanchez-Cortes, Sergio Burdisso 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In regulated domains such as banking and healthcare, where privacy constraints make real speech costly to collect and retain, synthetic speech from modern text-to-speech (TTS) is an appealing alternative for training automatic speech recognition (ASR) without exposing sensitive customer recordings. Yet a persistent distributional gap between synthetic and real data limits how far it can replace genuine recordings. Prior work largely treats this gap as a black box to be engineered around, but in our work, we instead examine its origin directly by probing a SLAM-ASR architecture. Then, we localise where its LLM backbone separates real from synthetic speech and find the discriminative signal concentrated in the early-to-middle layers, where temporal and prosodic perturbations disrupt it most. We further show that representation-level separability, help, but does not directly predict downstream ASR gains. On the other hand, convolving synthetic audio with room impulse responses (RIRs) narrows the gap not by making synthetic speech sound cleaner or more natural, but by reproducing the acoustic irregularities of real recordings. Translating these findings into the training procedure, by adding a layer-selection module combined with RIR augmentation matches a fully real-data baseline using only 25% of the real speech (13.6h) and surpasses it at all higher proportions.

---


### 64. [The strength of clinical evidence is recoverable from language model representations but not from their stated grades](https://arxiv.org/abs/2606.29034)

**<font color=#1a73e8>作者：</font>** Soroosh Tayebi Arasteh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly summarize clinical evidence, where a claim's weight depends on how strongly it is supported. Yet these models convey confidence poorly, and properties they never state, such as truth, are often readable from their activations. Whether a clinical model registers evidence strength, distinct from truth, and states it when asked is untested, and any such signal could be lexical. We compiled 45,134 clinical claims from six public sources, harmonized 20,611 into a four-level evidence grade under three independent frameworks, and tested 22 local, open-weight LLMs from several developers (0.6-70 billion parameters; general, medical, and reasoning), with lexical, truth, and cross-framework controls. A linear estimator recovered the grade in every model (median AUROC 71.8), yet decodability did not rise with scale and was weakest in reasoning models. The grade the models stated fell to chance, 25-27 percentage points below the estimator. The recoverable signal was largely lexical and did not transfer across topics or frameworks, yet it was distinct from factual truth and still flagged weakly supported claims (AUROC 69.2). Clinical LLMs thus carry an ordered evidence-strength signal they do not express, so their stated grades fail to convey a claim's support even when it is recoverable from their representations and text.

---


### 65. [MOSAIC: Orchestrating Collaborative Knowledge Tracing with Hierarchical Semantic Alignment](https://arxiv.org/abs/2606.29049)

**<font color=#1a73e8>作者：</font>** Xinjin Li, Mengyue Wang, Yuzhen Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge Tracing (KT) is important for personalized education but traditionally suffers from two key limitations: a reliance on shallow ID-based representations that neglect semantic depth and a restriction to single-granularity mastery estimation that overlooks hierarchical knowledge dependencies. To address these challenges, we propose MOSAIC (Multi-granularity Online Semantic AI for Collaborative Knowledge), a novel framework that orchestrates LLM-driven semantic alignment with sequential modeling. Unlike methods that use LLMs solely as predictors, MOSAIC leverages a frozen LLM to generate dynamic, context-aware embeddings and hierarchical prediction prompts, explicitly capturing collaborative signals and peer interactions. Furthermore, we introduce a cross-granularity consistency objective that jointly regularizes mastery estimation across concept, topic-cluster, and global proficiency levels. Extensive experiments on ASSISTments, EdNet, and a newly collected large-scale MOOC dataset demonstrate that MOSAIC establishes new state-of-the-art results. Specifically, our method achieves AUC improvements of up to 3.4\% and Accuracy gains of up to 2.5 \% across all benchmarks. Notably, MOSAIC exhibits superior robustness in collaboration-rich environments and long-sequence scenarios (AUC 0.862 on MOOC), offering both high predictive precision and semantically grounded interpretability.

---


### 66. [When Can Conformal Risk Control Certify LLM Outputs? Bounds, Impossibility, and Adaptation for Structured Generation](https://arxiv.org/abs/2606.29054)

**<font color=#1a73e8>作者：</font>** Varun Kotte  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) deployed for structured generation (NER, JSON extraction, QA, and classification) lack formal reliability guarantees, and standard heuristic abstention policies miss user-specified risk targets by 7.5--12.5%. We characterize when conformal risk control (CRC) can certify structured LLM outputs and when it provably cannot. First, we prove an impossibility result: when the base risk (\mu > \alpha), any distribution-free method must abstain on at least ((\mu-\alpha)/(1-\alpha)) examples, yielding a closed-form feasibility test: one can check whether CRC will work before running it. Second, we analyze a certification hierarchy across Hoeffding, empirical Bernstein, and a betting-based e-CRC bound, with strict gains in low-variance/large-sample regimes: the Hoeffding-to-Bernstein step delivers the largest gain (+37% certified configurations), while e-CRC adds value when calibration data is scarce (10% certification at 20% data versus 0% for Hoeffding). Third, we validate adaptive conformal inference (ACI) under cross-dataset shift, reducing risk-target violations from 71% to 21%, with residual failures concentrated exactly where the impossibility bound predicts. Across six open-weight models (3B--72B parameters), eight datasets, four tasks, and six nonconformity scores, hard NER/QA/CLS configurations are uncertifiable at (\alpha = 0.10); relaxing to (\alpha = 0.30--0.40) unlocks practical certification (47% NER, 40% QA, 60% CLS). The framework gives a three-step deployment recipe: check feasibility, select the bound and score, then mitigate shift.

---


### 67. [Flow Matching in Feature Space for Stochastic World Modeling](https://arxiv.org/abs/2606.29059)

**<font color=#1a73e8>作者：</font>** Francois Porcher, Nicolas Carion, Karteek Alahari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World modeling requires forecasting uncertain futures while preserving information useful for
downstream perception. Existing visual world models often struggle to satisfy both goals:
VAE-based stochastic models operate in low-dimensional reconstruction latents, which can
limit perception performance, while deterministic predictors using strong pretrained features
collapse multimodal futures into a single blurry mean. In this work, we propose FlowWM, a
stochastic world model that performs flow matching directly within pretrained feature space
(e.g., DINOv3). This is challenging because pretrained features are substantially
high-dimensional, making standard diffusion recipes suboptimal. To address this, we
investigate the design choices needed for feature-space flow matching and introduce a
differentiable one-step projection mechanism that enables efficient training with temporal
consistency and task-driven objectives. We evaluate FlowWM on two benchmarks: a synthetic
benchmark for systematic evaluation of accuracy and diversity, and a real-world benchmark
FuturePerception. FlowWM improves perception performance, mode coverage, and horizon
robustness, validating our proposed design for stochastic world modeling in high-dimensional
feature spaces.

---


### 68. [ThinkProbe: Beyond Accuracy -- Structural Profiling of Open-Ended LLM Reasoning Traces via Non-Generative Thought Graphs](https://arxiv.org/abs/2606.29067)

**<font color=#1a73e8>作者：</font>** Mohamed Amine Kerkouri, Simon D. Hernandez, Marouane Tliba 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present ThinkProbe, a framework for structural analysis of LLM reasoning traces. ThinkProbe converts each trace into a Thought Graph a directed graph with cycles, 8 node types, and 6 edge types and derives a 19-metric five-dimensional cognitive profile (5D-CP: Breadth, Depth, Structure, Metacognitive, Efficiency) through a fully non-generative pipeline combining rule-based segmentation and discriminative semantic linking. Applied to 4{,}200 traces from 7 native reasoning models across 200 open-ended questions and 10 cognitive domains, ThinkProbe reveals that reasoning structure is a stable, model-level property: between-model variance exceeds between-domain variance by up to fourfold across four of five cognitive dimensions, with Structure showing genuine sensitivity to question domain, exposing qualitatively distinct cognitive profiles invisible to accuracy-based evaluation.

---


### 69. [Low-cost concept-based localized explanations: How far can we get with training-free approaches?](https://arxiv.org/abs/2606.29069)

**<font color=#1a73e8>作者：</font>** Darian Fernández-Gutiérrez, Rafael Bello, Marilyn Bello 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Concept-based Explainable AI (C-XAI) seeks human-understandable explanations grounded in semantic concepts, yet validation is limited by the scarcity of fine-grained concept annotations. We evaluate whether mid-scale Multimodal Large Language Models (MLLMs) can perform localized concept naming under strict zero-shot conditions by assigning labels to bounding-box regions at both object and part levels. We propose a reproducible zero-shot evaluation protocol for Concept Naming (CoNa) with (i) closed-set, category-constrained prompting for moderate vocabularies and (ii) Open-CoNa, an embedding-similarity-based strategy for large label spaces. Experiments with four MLLMs (7B-32B) show consistent performance trends across datasets, reaching 62%-88% object-level exact-match accuracy, highlighting the potential of training-free concept annotation from localized regions. We discuss limitations and failure modes and release a reproducible framework to support future low-cost C-XAI research.

---


### 70. [Evolution Fine-Tuning: Learning to Discover Across 371 Optimization Tasks](https://arxiv.org/abs/2606.29082)

**<font color=#1a73e8>作者：</font>** Young-Jun Lee, Seungone Kim, Minki Kang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Would experience designing faster GPU kernels also help close in on a long-standing open mathematical conjecture? Large Language Models (LLMs) integrated into evolutionary search have recently produced state-of-the-art solutions on optimization tasks, including open mathematical conjectures, GPU kernel design, scientific law discovery, and combinatorial puzzles. To achieve this, prior work applied search scaffolds to one target task at a time, so every new problem is approached from scratch and the experience accumulated during search is discarded once the model finishes its attempt. This leaves the capability of iteratively evolving a solution (e.g., knowing which part to mutate and how, deciding when to backtrack) entirely in the scaffold rather than in the model itself. Whether the model itself could acquire this capability and reuse it across different tasks has been largely unexamined. To address this, we introduce Evolution Fine-Tuning (EFT), a mid-training paradigm that teaches LLMs to evolve solutions across tasks by converting evolutionary search trajectories into supervision. We construct Finch Collection, a 156K-trajectory dataset spanning 10 domains and 371 optimization tasks, and fine-tune open-source LLMs from 2B to 9B parameters. Empirically, EFT confers cross-task generalization: across 22 held-out tasks, our models surpass their base counterparts by 10.22% on average. Furthermore, when paired with test-time RL, our model matches state-of-the-art performance on two circle-packing tasks and outperforms its base-model counterpart on the Erdős minimum-overlap problem. EFT thus serves as a "practice phase" for general-purpose discovery agents that do not solve new problems from scratch.

---


### 71. [AB-RAG: Adaptive Budgeted Retrieval-Augmented Generation for Reliable Question Answering](https://arxiv.org/abs/2606.29090)

**<font color=#1a73e8>作者：</font>** Ansh Kamthan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) has become the standard way to ground large language models in external knowledge, yet most systems retrieve a fixed number of passages for every question regardless of its difficulty. This wastes computation on easy questions, starves hard ones, and gives no signal for when a generated answer can be trusted. With a growing share of question answering systems built on top of commercial language model APIs, a method that can decide how much to retrieve, and how far to trust its own answers, without retraining the underlying model, is of clear practical value. This paper presents AB-RAG (Adaptive Budgeted Retrieval-Augmented Generation), a training-free and backbone-agnostic framework that generates an answer, estimates its confidence from a combination of three signals, and then decides whether to stop or to retrieve more evidence, subject to a fixed retrieval budget. The estimator combines the model's own certainty, the agreement between the answer and the evidence, and the variance of the retrieval scores. For models that expose token probabilities the certainty signal is read directly; for closed APIs it is approximated by self-consistency, so the method works without access to model internals. Across three backbones and two datasets, the central result is that the confidence estimate reliably separates correct from incorrect answers on every backbone, reaching a clean split of 57.6% against 0% Exact Match between high- and low-confidence answers on a factoid dataset. The adaptive policy improves accuracy on capable backbones, and the study reports its negative and nuanced findings honestly, including a confidence signal that proved unsuitable for short answers and a retrieval signal whose sign was found and corrected through measurement. The entire study was carried out on a single consumer laptop with only a few dollars of API spend.

---


### 72. [Statistically Indistinguishable, Operationally Distinct: A Formal Barrier for Tabular Foundation Models](https://arxiv.org/abs/2606.29091)

**<font color=#1a73e8>作者：</font>** Tassilo Klein, Johannes Hoffart  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models cannot reason about data produced by running systems without access to the rules that govern them. We make this statement falsifiable. The \emph{Operational Turing Test} (OTT) constructs pairs of legal and rule-violating database states whose $1$- and $2$-way column-value marginals match to a total variation of $<0.02$; Le~Cam's lemma then bounds any values-only classifier at $\geq0.49$ Bayes error. Three values-only baselines (XGBoost, TabICL, TabPFN) hit the bound exactly (accuracy $0.50$, pre-registered two one-sided tests (TOST) $p<0.002$), raw row-level access does not help, exposing relational value consistency closes most of the gap, and only a classifier fed by seven executable rule-derived audits reaches $1.00$ classification accuracy. In three matched $100$-state frontier large-language-model (LLM) runs, models given the schema, trigger source, rule tables, and state files classify at most $2/50$ legal states as LEGAL; GPT-5.5 accepts $0/50$ legal states even with higher reasoning effort and a Structured Query Language (SQL) executor. The access-ladder pattern also appears on a second schema with structurally distinct rule families (banking ledger: cross-row balance, cumulative aggregate). The barrier is identifiability, not capacity: scale, data, and richer features cannot cross it without operational grounding.

---


### 73. [From Fog Chamber to Aircraft Window: Pixel-Registered Imaging and Synthetic Fine-Tuning Enable Cross-Domain Defogging](https://arxiv.org/abs/2606.29093)

**<font color=#1a73e8>作者：</font>** Alexander Ingold, Sabina D. Menon, Manya Yellepeddy 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A deep defogging pipeline pretrained on controlled laboratory fog and fine-tuned with domain-randomized synthetic fog applied to clear outdoor scenes generalizes across a graded sequence of out-of-distribution settings with no target-domain training, from chamber-free free-flowing fog to iPhone video recorded through an aircraft cabin window in flight, an entirely unseen sensor, scene, and optical path. This directly addresses an open transfer limitation reported for real-world binocular defogging. Two design choices support the transfer. First, a single-camera fog imager photographs a flat-panel display through an artificial-fog enclosure with a fixed 114~mm scattering path, producing 5{,}495 pixel-aligned foggy/clear pairs. Exact registration permits a paired Laplacian ratio that predicts per-image restoration quality far better than single-image proxies (Spearman $\rho = 0.632$ versus $0.399$) and supports pixel-exact $L_1$ reconstruction training that avoids adversarial hallucination. Second, the fog-chamber checkpoint is fine-tuned on Mapillary Vistas crops overlaid with on-the-fly randomized synthetic fog spanning a broad range of strengths, spatial variations, airlights, and noise conditions. On a 552-image held-out split, a uniform comparison of 30 restoration backbones places NAFNet at the top (24.33~dB~/~0.7912~SSIM), with a compact alternative within 1.29~dB at 3\% of the parameter count, and a ResNet-50 classifier confirms that the restoration preserves semantic content rather than only pixel-level structure. On unpaired aircraft-window video, NIQE decreases from a mean of 6.22 to 4.97 after fine-tuning, with temporally stable output across full-motion sequences. The same backbone, under paired supervision, also reaches 20.71~dB~/~0.683~SSIM on a non-overlapping O-HAZE/NH-HAZE split (a transferability check rather than a competitive ranking).

---


### 74. [DiLaServe: High SLO Attainment Serving for Diffusion Language Models](https://arxiv.org/abs/2606.29094)

**<font color=#1a73e8>作者：</font>** Tzu-Tao Chang, Benjamin Yuanyang Hong, Kiet Pham 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) have recently emerged as a promising alternative to conventional autoregressive language models. By generating multiple tokens in parallel during each denoising step, they offer higher inference throughput while maintaining competitive quality. However, realizing these throughput gains while meeting latency SLOs in a serving system requires addressing challenges introduced by DLMs' unique characteristics. These include navigating the speed-quality tradeoff created by confidence-based denoising, choosing appropriate parallelization levels across model instances under fluctuating load, and coordinating approximate KV caching mechanisms that introduce non-uniform per-step costs. To address these challenges, we present DiLaServe, a cluster-level serving system for DLMs. DiLaServe enables deadline-aware scheduling and adaptive load control through confidence-threshold adjustment, and dynamically reconfigures the cluster by solving a quality-aware optimization problem, while explicitly modeling the step-level heterogeneity introduced by approximate KV caching. Across multiple benchmarks and real-world traces, DiLaServe improves SLO attainment by up to 56.6 percentage points and reduces end-to-end request latency by up to 46\% while incurring less than 1\% accuracy drop.

---


### 75. [TrafficAlign: Aligning Large Language Models for Traffic Scenario Generation](https://arxiv.org/abs/2606.29097)

**<font color=#1a73e8>作者：</font>** Zhi Tu, Liangkun Niu, Tianyi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent research has investigated the use of large language models (LLMs) to generate traffic scenarios for autonomous driving. However, pretrained LLMs often fail to align with real-world traffic distributions. In this work, we present TrafficAlign, an automated framework that synthesizes traffic scenarios based on real-world driving videos, performs data validation, and aligns LLMs with the synthesized scenarios. The evaluation shows that traffic scenarios generated by TrafficAlign are highly effective, revealing up to 10.8% more collisions on average across three autonomous driving models than state-of-the-art methods. Furthermore, fine-tuning these driving models with TrafficAlign-generated scenarios significantly reduced collision rates by 36.1% compared with the original models. A qualitative study using traffic datasets from six geographically diverse regions shows that TrafficAlign-generated scenarios exhibit strong alignment with corresponding traffic distributions in these regions.

---


### 76. [Characterizing Large Language Model Agentic Workflows: A Study on N8n Ecosystem](https://arxiv.org/abs/2606.29116)

**<font color=#1a73e8>作者：</font>** Yutian Tang, Yuming Zhou, Huaming Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are rapidly being adopted in low-code and no-code automation platforms, where non-expert users design workflows that combine natural language understanding with external services and APIs. LLM agents are LLM systems that use LLMs as a core "brain" to reason, plan, and autonomously execute complex, multi-step tasks. In this paper, we present the first large-scale empirical study of LLM agentic workflows in low-code automation platforms. We analyze more than 6,000 publicly available n8n workflows and examine four aspects of their design: task distribution, structural and tool use patterns, reliability mechanisms, and autonomy levels. Our analysis shows that LLM workflows are not merely prompt response pipelines. Instead, LLMs are commonly embedded within broader automation structures involving control logic, external tools, communication services, storage systems, and human review points. We further find that while many workflows include lightweight post-processing or routing logic after LLM execution, explicit reliability mechanisms such as structured fallback paths, repair loops, failure-specific alerts, and human approval gates remain relatively uncommon. These results reveal a gap between the increasing deployment of LLM agents in practical automation ecosystems and the limited engineering support for reliability, safety, and governance. Overall, our study provides ten empirical findings and five research takeaways for researchers, platform developers, and practitioners seeking to understand and improve real-world LLM agentic workflows.

---


### 77. [DistilledGemma: Balanced Efficiency-Accuracy for Person-Place Relation Extraction from Multilingual Historical Articles](https://arxiv.org/abs/2606.29130)

**<font color=#1a73e8>作者：</font>** Youssef Aboelwafa, Ahmed Samir, Nagwa Elmakky 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present DistilledGemma, an efficient and accurate system for the HIPE-2026 shared task on person-place relation extraction from multilingual historical newspaper articles in English, German, and French. Our approach adopts a three-stage knowledge distillation pipeline designed to balance classification accuracy with computational efficiency. In the first stage, we systematically explored prompt engineering strategies across eight large language models to identify the most effective reasoning architecture for this challenging task. In the second stage, we applied supervised fine-tuning (SFT) via QLoRA to a Gemma 4 26B A4B teacher model, leveraging its strong multilingual capabilities to generate silver-standard chain-of-thought traces across the training corpus. In the final stage, we performed response-level distillation to transfer these learned reasoning patterns into a compact Gemma 4 E2B student model. In the official evaluation, our team WHEREAMI ranked 3rd on the standard test set with an accuracy profile mean score of 0.688, and 2nd on the binary test set with a mean score of 0.8156. Notably, by distilling knowledge from the 26B teacher to the 2.3B student, we preserved strong reasoning capabilities while reducing the deployed model size to approximately 2.3B effective parameters; the LoRA adapters used during training were merged into the student for inference. This configuration ranked 2nd in the balanced efficiency-accuracy profile across both the standard and binary test sets. These results demonstrate that knowledge distillation provides a practical and scalable solution for historical document processing, achieving competitive performance without excessive computational cost.

---


### 78. [How Token Influence Decays with Distance: A Green-Function View of Trained Language Models](https://arxiv.org/abs/2606.29139)

**<font color=#1a73e8>作者：</font>** Matthias Brändel, Stephan Köhler, Oliver Rheinbach  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study how the next-token prediction of an autoregressive Transformer language model changes under small perturbations of earlier input token embeddings. Motivated by operator learning and iterative solvers for differential equations, we investigate how the influence of one token on another decays with distance in a trained model. In multilevel methods for differential equations, such as domain decomposition, multigrid, and multilevel preconditioning, one often exploits a separation between strong local interactions and weaker but essential global interactions. The latter correspond to the long tail of the Green's function and are typically handled by a coarse-level operator. Inspired by this perspective, we compute an empirical, distance-resolved gradient profile of token dependencies using autograd. Experiments on trained Pythia models and Qwen2.5-0.5B show that, over the measured distance range, the median Jacobian sensitivity is much better described by a power-law-type decay than by an exponential alternative: the diagonal-normalized profile is well described by $$\overline G(r) \approx \gamma+\beta(r+1)^{-p}$$ with exponents $p \approx 0.7$--$0.9$ (typically $0.8$--$0.9$). This behavior appears on coherent text from Gutenberg and WikiText-103. Token-shuffling experiments show that the power-law profile persists even when syntax and prediction quality collapse, whereas randomly initialized models do not exhibit it. The slowly decaying long-range sensitivity thus appears to be a learned property of trained autoregressive Transformer operators. These findings suggest that hierarchical or coarse-level mechanisms in language models may be able to exploit the long-tailed sensitivity profiles.

---


### 79. [Flow Reasoning Models: Scaling Reasoning Through Iterative Self-Refinement](https://arxiv.org/abs/2606.29150)

**<font color=#1a73e8>作者：</font>** Alec Helbling, Andrey Bryutkin, Mauro Martino 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Discrete flow models have recently shown promising performance on few-step text generation; however, when naively applied to structured reasoning tasks such as Sudoku and Zebra puzzles, they converge confidently to incorrect answers (solving only $\sim$36% of Sudoku puzzles). We introduce Flow Reasoning Models (FRMs), a training and test-time-scaling framework for structured reasoning with flow models. We make the observation that, despite their poor solve rate, flow models can act as their own verifiers. A correct answer is a stable fixed point of the denoising dynamics, returning to itself when re-noised and re-solved. This enables a test-time-scaling paradigm: propose many candidate solutions and keep those that are dynamically stable, which alone reaches high solve rates on Sudoku-Shah (~$100\%$) and Zebra ($95.9\%$). This even generalizes to harder out-of-distribution puzzles like Sudoku-Extreme ($96.1\%$), without ever training on that distribution. This pure search, however, wastes a great deal of computation generating incorrect candidate solutions. We therefore design a training recipe to improve the base model's efficiency. First, we train flow models with a self-conditioning channel and close it at inference, letting them refine their own past predictions. Second, we train models to avoid their own failed generations using direct preference optimization. These changes substantially improve the base model's efficiency, letting it reach $99.2\%$ on Sudoku in just $7$ forward passes, over $8\times$ fewer than the strongest matched masked-diffusion baseline we compare needs for the same accuracy. When combined with test-time scaling, this lets flow models solve hard out-of-distribution puzzles (e.g. Sudoku-Extreme) far more efficiently.

---


### 80. [On the Nonlinearity of Learning Rate Scaling for LLM Training](https://arxiv.org/abs/2606.29158)

**<font color=#1a73e8>作者：</font>** Zaiwen Yang, Huaqing Zhang, Jing Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning-rate transfer can reduce the cost of training large language models: instead of sweeping learning rates at target scale, practitioners extrapolate from smaller runs. Existing approaches often assume that the optimal learning rate follows a log-linear scaling law in data scale and model size. We carefully examine and evaluate this scaling law. In our empirical study of GPT-2--style models from 22M to 707M parameters trained on 5B to 100B tokens, the optimal learning rate develops upward curvature at larger scales, leading to inaccurate extrapolation. We find that this curvature largely disappears when learning rates are replaced by effective learning rate (the step size in normalized weight space), and when data $D$ extrapolation is used instead of model size $N$ extrapolation. Next, we explain nonlinearity in scaling: weight-norm converges to equilibrium slower when optimal learning is small, requiring a larger step size to reduce the transient phase. Experiments with AdamH, which directly controls the effective learning rate, further support this explanation.

---


### 81. [Invariant Reasoning Directions in Latent Trajectories of Language Models](https://arxiv.org/abs/2606.29164)

**<font color=#1a73e8>作者：</font>** Arun Vignesh Malarkkan, Manan Roy Choudhury, Utkarsh Byahut 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent reasoning models perform multi-step inference directly in hidden-state space, yet the structure of these latent reasoning trajectories remains poorly understood. We show that contrastive refinement signals between stronger and weaker reasoning trajectories exhibit a highly concentrated low-rank structure, while unconstrained latent updates remain sensitive to paraphrases, checkpoint choice, and trajectory perturbations. These observations suggest that latent reasoning trajectories contain stable invariant directions mixed with unstable instance-specific variation. We introduce \textbf{Trajectory-Invariant Latent Refinement (TILR)}, a training-free intervention framework for identifying and manipulating stable reasoning directions in latent space. TILR first learns a low-rank invariant subspace from contrastive trajectory differences across inputs, then constrains latent interventions to this subspace while suppressing poorly aligned updates through an adaptive alignment gate. Across six reasoning benchmarks, we find that a small number of latent directions explain most variation between strong and weak reasoning trajectories. Interventions on these directions causally improve reasoning consistency and reduce trajectory instability under paraphrases and perturbations. TILR improves answer consistency under paraphrase by ~10% and reduces latent trajectory variance by up to $50\%$ while preserving reasoning accuracy. These results support a geometric view of latent reasoning in which transferable reasoning behavior emerges from stable low-dimensional structure within hidden-state trajectories.

---


### 82. [Selective Memory Retention for Long-Horizon LLM Agents](https://arxiv.org/abs/2606.29178)

**<font color=#1a73e8>作者：</font>** Pranath Reddy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When does retention matter for memory-augmented LLM agents? We study this with TraceRetain, a lightweight framework for bounded external memory in frozen LLM agents that scores entries by interpretable features (success, age, access frequency, redundancy, specificity, similarity, downstream utility) and evicts the lowest-scoring ones at capacity. On clean ALFWorld with gpt-5-mini, external memory robustly improves over no memory across two seeds, but differences among bounded retention policies fall within Wilson 95% CIs: clean ALFWorld at T=100 to T=200 does not naturally exhibit the memory pollution retention is designed to address. Under a controlled noisy-write stress (75% synthetic distractors), unbounded memory and FIFO-K50 degrade on Precision@5 (20.2% to 12.4% and 15.8% to 3.8%) while TraceRetain-CEM is essentially unchanged (16.9% to 16.6%) and preserves 97/100 task success. The mechanism: unbounded memory has the highest mean similarity (0.87) but lowest precision, indicating failed distractors close to the query in embedding space. Held-out in-distribution evaluation shows memory-augmented policies solving 47 to 49 of 50 tasks vs. 39/50 for no memory. Bounded retention buys memory and step efficiency on saturated clean benchmarks at no task-success cost, and only differentiates from cache heuristics when streams contain noise.

---


### 83. [Evidence-Informed LLM Beliefs for Continual Scientific Discovery](https://arxiv.org/abs/2606.29182)

**<font color=#1a73e8>作者：</font>** Dhruv Agarwal, Reece Adamson, Andrew McCallum 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Open-ended scientific discovery with large language models (LLMs) increasingly operates as a long-horizon loop of hypothesis search and verification, where a reward signal guides which hypotheses to test next. A notable recent example is AutoDiscovery, which uses "Bayesian surprise" - the belief shift an LLM undergoes after observing evidence for a hypothesis - as both a discovery metric and a reward for search. We first observe that AutoDiscovery treats surprisal as a static quantity, while surprisal in human reasoning is non-stationary - it is defined relative to beliefs that evolve with experience, a prerequisite for continual scientific discovery. We address this mismatch with evidence-informed LLM beliefs: priors updated with evidence from previous hypotheses to compute non-stationary surprisal for new hypotheses. We compare in-context belief-updating mechanisms and find that embedding-based retrieval-augmented generation over prior discoveries best anticipates eventual posteriors, identifying 37.5% of static surprisals as spurious. We then modify search to avoid these spurious rewards and prioritize hypotheses that remain surprising under non-stationary beliefs. Concretely, we introduce two complementary changes to the original search procedure: belief-update filtering and diversity maximization. Across five discovery domains, our method increases accumulated non-stationary surprisal by 30.62% on average compared to the original search procedure, demonstrating that continual scientific discovery with LLMs requires not only better belief measurement but also search procedures that avoid redundancy and encourage diversity.

---


### 84. [BaRA: Bayesian Adaptive Rank Allocation for Parameter-Efficient Fine-Tuning](https://arxiv.org/abs/2606.29184)

**<font color=#1a73e8>作者：</font>** Zhibin Duan, Yuhong Wang, Jiahong Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While Low-rank adaptation (LoRA) enables highly efficient fine-tuning by constraining task-specific updates to fixed low-rank subspaces, this rigid design limits representational flexibility and often results in overconfident predictions and miscalibrated uncertainty, especially in low-data regimes. Recent Bayesian LoRA variants improve uncertainty estimation by modeling posterior distributions over adaptation parameters. However, these approaches typically rely on fixed or heuristically determined ranks, overlooking the inherently context-dependent nature of adaptation capacity. In this paper, we propose BaRA, a Bayesian Adaptive Rank Allocation framework for parameter-efficient fine-tuning. Drawing inspiration from probabilistic topic models, BaRA dynamically allocates adaptation capacity by activating a sparse, context-dependent subset of disentangled latent factors, enabling instance-wise variation in effective rank. This Bayesian formulation provides principled, data-driven capacity control, mitigating over-parameterization while preserving expressiveness. Beyond the modeling contribution, we provide a complexity-theoretic generalization analysis showing that the generalization gap of BaRA depends on the learned joint effective rank $\bar{s}_{\Phi,\theta}$ induced by the global-local gate, rather than the maximum rank $r$. This result explains why sparse adaptive rank allocation can reduce the effective hypothesis complexity while preserving input-dependent expressiveness. Extensive experiments on diverse natural language benchmarks demonstrate that BaRA consistently improves predictive performance, robustness, and uncertainty calibration compared to standard LoRA and existing Bayesian LoRA variants.

---


### 85. [Representational Depth of Evaluation Awareness Shifts With Scale in Open-Weight Language Models](https://arxiv.org/abs/2606.29196)

**<font color=#1a73e8>作者：</font>** Archit Manek  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Do language models know when they are being tested? This question matters for AI safety: a model that recognises an evaluation context could alter its behaviour strategically, making downstream benchmarks harder to interpret. Using 11 models spanning Qwen 2.5, Gemma 2, and Llama 3.2, we find a systematic size-dependent shift in representational depth: in both Qwen 2.5 and Gemma 2, the layer at which evaluation-awareness is most linearly recoverable moves from late layers in smaller models to early layers in larger ones. This suggests that scale changes not only the strength of evaluation-awareness but also where it is most linearly recoverable in the network. This depth shift helps explain why within-family scaling trajectories are non-monotonic or inverse rather than smooth and family-general, showing that a simple universal power-law account is not supported under denser within-family sampling. Finally, white-box probe signals are consistently stronger than black-box behavioural expression, and the relationship between the two varies by family in ways not predicted by probe AUROC alone.

---


### 86. [Can OCR-VLMs Read Devanagari? A Stress-Test Benchmark and Post-Correction Study](https://arxiv.org/abs/2606.29213)

**<font color=#1a73e8>作者：</font>** Aditya Pratap Singh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> OCR systems, ranging from classical engines to specialised OCR vision-language models (OCR-VLMs) and frontier multimodal LLMs, report strong results on English and Chinese document benchmarks, yet their behaviour on Indic scripts is largely uncharacterised. We benchmark ten systems on Devanagari (Hindi): classical EasyOCR; open VLMs (Qwen2.5-VL-3B, Qwen3-VL-8B, olmOCR-7B); specialised OCR-VLMs (DeepSeek-OCR, Unlimited-OCR); and frontier closed models (Gemini 2.5 Flash, Claude Opus 4.7, GPT-5.5, Mistral OCR), across four synthetic degradation conditions and 300 real printed scans. We report four findings. First, on clean rendered text all ten cluster within chrF++ 91 to 98, so synthetic text does not separate them. Second, under degradation the specialised OCR-VLMs are the most fragile: DeepSeek-OCR suffers rare but catastrophic repetition failures (outputs up to 71 the reference length) that wreck its corpus mean even though its median is the best of any system, which is why we report median and catastrophic-rate instead of the mean. Third, on real scans nine of the ten systems collapse (EasyOCR falls from chrF++ 93.6 to 58.3) and the field spreads across a 76-point range, so synthetic renders badly overstate Devanagari quality. Fourth, strong English OCR does not predict Indic OCR: GPT-5.5 drops to chrF++ 58.5 (tying classical EasyOCR) and olmOCR-7B, the model behind olmOCR-Bench, falls to 40.5, while the open Qwen3-VL-8B (75.2, runnable on a single 24 GB GPU) beats GPT-5.5 and approaches Mistral; Gemini and Claude lead at 86.3 and 82.2. An error taxonomy separates surface errors (numerals, punctuation) from structural ones (conjuncts, matras, nukta), and a byte-level (ByT5) post-corrector improves a cheap engine on its own error distribution (chrF++ +1.2 to +1.5) but does not transfer across engines. We release the benchmark, code, and models.

---


### 87. [Multi-Block Diffusion Language Models](https://arxiv.org/abs/2606.29215)

**<font color=#1a73e8>作者：</font>** Yijie Jin, Jiajun Xu, Yuxuan Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Block Diffusion Language Models (BD-LMs) improve diffusion-based text generation with KV caching and flexible-length generation. A natural next step is to extend them from Single-Block Diffusion (SingleBD) to Multi-Block Diffusion (MultiBD), where a \textit{running-set} of consecutive blocks is decoded concurrently for inter-block parallelism. However, existing BD-LMs are mostly trained under teacher forcing, where the model observes only one noisy block conditioned on a clean prefix. While the recent diffusion forcing strategy introduces visibility among multiple noisy blocks, its training states still differ from MultiBD inference, where decoding operates on a bounded \textit{running-set} with heterogeneous slot-wise noise patterns. To bridge this gap, we propose \textit{Multi-Block Diffusion Language Models} (MBD-LMs), obtained by post-training BD-LMs with \textit{Multi-block Teacher Forcing} (MultiTF). MultiTF integrates teacher forcing and diffusion forcing by training on bounded \textit{noise-groups} conditioned on clean prefixes, with randomized \textit{noise-schedulers} that better match MultiBD inference states. To make MultiBD practically executable, we further introduce an optimized decoding algorithm based on the \textit{Block Buffer} mechanism that preserves prefix-cache reuse, keeps input shapes static, and translates increased decoding parallelism into wall-clock acceleration. Empirically, MBD-LLaDA2-Mini increases average Tokens Per Forward pass (TPF) from 3.47 to \textbf{6.19} and improves average accuracy from 79.95\% to \textbf{81.03\%}; when combined with DMax, MBD-LLaDA2-Mini-DMax reaches an average TPF of \textbf{9.34} with only a 1.02\% accuracy drop on math and code benchmarks.

---


### 88. [Depth Exploration for LLM Decoding](https://arxiv.org/abs/2606.29223)

**<font color=#1a73e8>作者：</font>** Weisi Yang, Zipeng Sun, Stephen Xia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive LLM decoding evaluates every generated token through the full layer stack, even though many tokens become predictable at intermediate depths. Existing lossless depth-adaptive methods exploit this redundancy by choosing a single non-final exit depth and verifying its prediction with the final-depth model. However, our measurements show that this selection-based strategy leaves substantial headroom: choosing an exit too late wastes computation, while choosing one too early triggers fallback and discards dependent drafts. We propose Depth Exploration Decoding (DEX), a lossless decoding algorithm that replaces single-depth selection with parallel exploration over multiple candidate depths. At each commit position, DEX validates candidates against the final-depth reference, commits exactly the final-depth token, and collapses the exploration lattice to retain only reusable branch states. This expand--commit--collapse procedure preserves equivalence to standard autoregressive decoding while reducing the cost of committing each token. Across early-exit-trained and standard LLMs, DEX outperforms representative depth-selection baselines and achieves competitive end-to-end throughput against speculative and distributed decoding methods. Moreover, DEX improves as the explored depths become finer, showing that parallel depth exploration provides a scalable way to exploit the underused depth axis of LLM decoding.

---


### 89. [PolicyGuard: A Dialogue-Grounded Sub-Agent Verifier for Policy Adherence in LLM Agents](https://arxiv.org/abs/2606.29225)

**<font color=#1a73e8>作者：</font>** Seongjae Kang, Taehyung Yu, Sung Ju Hwang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents handle user requests on behalf of organizations through tool calls and must follow the company policies stated in their system prompts. Prior work approaches this as a safeguarding problem -- external checks that block non-compliant agent actions. We argue that policy adherence is a broader problem: real workflows unfold across many turns, require explicit user confirmation and prerequisite reads, and hinge on the content of the dialogue rather than on any single argument value. Meeting this bar requires (i) full conversation context, (ii) self-reasoning over the policy and the current dialogue, and (iii) conversation-specific remediation that guides the agent's next turn -- three capabilities that prior safeguard work has often underestimated. We introduce POLICYGUARD, a sub-agent verifier that shares the agent's view of the dialogue, reasons over the policy in context, and provides actionable feedback for the agent's next turn. On tau^2-BENCH airline across three vendors (GPT-5.4, Claude Sonnet 4.6, Gemini 2.5 Pro) with four trials per setting, POLICYGUARD improves PASS4 by +12.0 / +6.0 / +12.0 pp. Per-call analyses show POLICYGUARD achieves higher policy-violation recall while blocking roughly half as often as argument-level guards.

---


### 90. [Understanding Evaluation Illusion in Diffusion Large Language Models](https://arxiv.org/abs/2606.29228)

**<font color=#1a73e8>作者：</font>** Hengxiang Zhang, Jiaxi Ren, Hongxin Wei  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite the capability of parallel decoding, diffusion large language models (dLLMs) require many denoising steps to maintain generation quality, motivating recent research on efficient decoding strategies. However, existing studies have reported inconsistent evaluation results even under seemingly identical evaluation settings, risking biased conclusions about dLLM decoding methods. To understand this evaluation concern, we conduct a rigorous evaluation of current decoding methods for dLLMs across diverse evaluation settings. Surprisingly, our analysis reveals that the ranking of decoding methods is highly sensitive to the choice of prompt templates. Single-template evaluation can lead to an illusion that decoding methods improve inference efficiency without performance degradation. Through comprehensive experiments, we find that current parallel decoding methods consistently underperform the single-token decoding baseline, failing to overcome the speed-quality trade-off. We further identify this evaluation inconsistency as the high sensitivity of parallel decoding methods to minor variations in prompt templates. Our experiments show that an effective prompt template can achieve strong evaluation results even with fewer denoising steps, markedly outperforming the marginal gain from increasing denoising steps. Beyond prompt templates, our experiments indicate that overlooked evaluation settings can also notably affect the assessment of decoding methods. Based on these findings, we propose practical guidelines for the reliable evaluation of decoding methods in dLLMs.

---


### 91. [When Does Synthetic CT Transfer? A Label-Free Donor/Host Diagnostic for Medical Vision-Language Model Routing on Real Lung CT](https://arxiv.org/abs/2606.29232)

**<font color=#1a73e8>作者：</font>** Fakrul Islam Tushar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A synthetic measurement of model competence is useful only if it survives the move to real data, yet the real labels that would verify it are exactly what medical imaging lacks. We ask whether transfer can be predicted in advance, label-free, and answer with a mechanism: on synthetic digital twins, competence that is donor-driven (a property of the transplanted nodule) survives the synthetic to real change of host, while host-driven competence (a property of the surrounding anatomy) need not. We test this on three lung CT vision-language tasks chosen to span that axis, across five public VLMs, four guidance conditions, and seven real datasets. The prediction holds in every case: presence and size orderings transfer (R2 >= 0.96), lobe does not; the split survives leave-source-out calibration, and the diagnostic names that boundary before any real label. TrialCouncil, a training-free council calibrated only on synthetic CT, confirms it by matching the best fixed model exactly where transfer is predicted. The contribution is not the router but the finding that transfer itself is predictable, label-free, from synthetic data alone.

---


### 92. [Towards Evaluating Data Priors for Tabular Foundation Models](https://arxiv.org/abs/2606.29241)

**<font color=#1a73e8>作者：</font>** Zeynep Türkmen, Kürşat Kaya, Alexander Pfefferle 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data-generating priors are a central component of tabular foundation models because they define the task distribution used during pretraining. However, priors are rarely evaluated as independent components, making it difficult to understand how much they affect downstream model behavior. This raises a methodological question: how can priors from different tabular foundation models be compared independently of the architectures and training protocols they were introduced with? To study this question, we implement a unified interface for publicly available priors from recent tabular foundation models and priors constructed from real datasets. We generate training tasks from each prior, train the same model architecture under a fixed training protocol, and evaluate the resulting models on shared downstream classification tasks. We compare priors through both generated-task statistics and downstream predictive performance. Our results show that different priors favor different downstream behaviors, with some achieving stronger absolute performance and others exhibiting more consistent relative rankings across datasets. We further find that data-level similarity only partially explains downstream behavior. Our code is available at this https URL.

---


### 93. [When Summaries Distort Decisions: Information Fidelity in LLM-Compressed Financial Analysis](https://arxiv.org/abs/2606.29251)

**<font color=#1a73e8>作者：</font>** Hoyoung Lee, Suhwan Park, Seunghan Lee 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial decision-makers face more information than they can directly inspect, making context compression necessary. Yet when large language models (LLMs) compress financial source material, they can alter the investment judgment supported by the original source. We frame this problem as information fidelity: compression loses fidelity when it changes the decision induced by the source. In agentic systems, such losses may recur across intermediate steps and amplify throughout the decision process. Across financial filings and earnings-call transcripts, we find that LLM-based compression can produce fluent and factually plausible compressed contexts that nevertheless alter downstream decisions. We analyze two diagnostic patterns associated with fidelity loss: decontextualization, where salient evidence is retained but separated from the caveats and contextual qualifiers needed for correct interpretation, and model dependency, where different compressors expose different views of the same source. We then propose Agentic Context Compression, which generates multiple candidate compressions and audits their disagreements against the original source. Our results suggest that financial compression should be evaluated not only by efficiency or factuality, but also by its ability to preserve decision-relevant context.

---


### 94. [Travel-Oriented Reasoning Large Language Model via Domain-Specific Knowledge Graphs](https://arxiv.org/abs/2606.29254)

**<font color=#1a73e8>作者：</font>** Vignesh Ram Nithin Kappagantula, Shayan Hassantabar, Samuel Simpson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) demonstrate broad reasoning abilities but struggle with accuracy and reliability in specialized domains such as travel, where reasoning depends on precise definitions, rules, and expert-defined conceptual frameworks, and where confident but unfounded outputs arise from a reasoning failure in which the model has not internalized the underlying domain graph rather than from missing domain knowledge alone. We propose a modular pipeline for building a travel-domain reasoning LLM grounded in an expert-designed knowledge graph (KG). Our pipeline integrates a travel KG that encodes domain entities and their relationships, a bottom-up construction procedure that walks the KG to produce multi-hop question answer (QA) pairs, a supervised fine-tuning stage that embeds the domain knowledge into a reasoning-capable LLM using the generated QA pairs as auditable reasoning traces, and a travel-domain benchmark dataset that measures the fine-tuned model's accuracy and calibration. We evaluate our approach using Qwen3-4B with LoRA adaptation. Our reasoning model achieves an $82.4\%$ exact match on the benchmark. This performance significantly outperforms the pretrained Qwen3-4B baseline at $22.4\%$. A calibration analysis decomposes the residual $17.57\%$ of errors into two distinct failure modes: an over-confident multi-label decoder that predicts both correct answers plus one spurious option on most dual-answer mistakes, and a smaller reasoning failure on single-answer questions where the supporting facts are present in the KG but the model fails to reconstruct the correct multi-hop path. This split confirms that explicit KG-grounded reasoning substantially improves the accuracy and uncertainty interpretation of LLMs in specialized domains, and isolates per-option calibration and trace-length-aware decoding as the next axes of improvement.

---


### 95. [MIThinker: A Plug-and-Play Policy-Optimized Thinker For Motivational Interviewing Counseling](https://arxiv.org/abs/2606.29265)

**<font color=#1a73e8>作者：</font>** Yizhe Yang, Palakorn Achananuparp, Heyan Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning large language models (LLMs) have recently made much progress in complex problem-solving, leveraging internal reasoning (or thought) to guide their solution generation. However, existing LLM-based counseling agents, including those using Motivational Interviewing (MI), generate responses without explicitly aligning thoughts with counseling techniques, limiting their effectiveness. We propose MIThinker, a lightweight thinking model that generates therapeutic thoughts to guide MI counseling agents in strategy selection and response generation. To overcome the lack of annotated thought data, we introduce AugR1-MI, an automated pipeline that reverse-engineers counselor's thoughts from observed responses. Through two-stage training combining supervised fine-tuning and reinforcement learning, MIThinker demonstrates improved theory-of-mind assessment and strategy alignment. Comprehensive evaluations show that MindfulMI, our agent leveraging MIThinker, achieves MI competency comparable to state-of-the-art systems with an order of magnitude less computation.

---


### 96. [Enhancing Part-Level Point Grounding for Any Open-Source MLLMs](https://arxiv.org/abs/2606.29267)

**<font color=#1a73e8>作者：</font>** Jin-Cheng Jhang, Fu-En Wang, Xin Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual grounding aims to associate free-form textual queries with specific regions in an image. While recent Multimodal Large Language Models (MLLMs) have demonstrated promising capabilities in this domain, they primarily excel at object-level grounding and often struggle with part-level grounding-an essential requirement for fine-grained tasks such as robotic manipulation. In this work, we introduce a general approach that equips any open-source MLLMs with accurate 2D part-level point grounding, offering a more direct alternative to conventional grounding representations. Our method leverages the attention mechanisms inherently present in MLLMs. By synthesizing text-conditioned, grounding-aware queries within intermediate layers via the proposed Q-Synth Module, we capture target-relevant attention patterns and refine them with a lightweight Attention-to-Point Decoder, which converts these patterns into a point-centric heatmap for final prediction. Notably, all original MLLM parameters are frozen, ensuring full preservation of their pre-trained capabilities. Experiments show that our design consistently improves part-level grounding accuracy across datasets and can be seamlessly integrated into any open-source MLLMs.

---


### 97. [Minority Sentinel: When to Overturn Majority Voting in Multi-Agent LLM Debates](https://arxiv.org/abs/2606.29270)

**<font color=#1a73e8>作者：</font>** Chuan He, Zebin Chen, Zhengyi Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-Agent Debate (MAD) with Majority Voting is a dominant paradigm for improving LLM reasoning, yet its effectiveness rests on the Condorcet Jury Theorem's assumption of independent errors. Because contemporary LLMs share similar pretraining corpora, their errors are strongly correlated, causing the majority to systematically suppress correct minority opinions, a phenomenon we term Minority Truth. Through debates among three heterogeneous LLM agents on six benchmarks, we find that roughly one in four divergent cases has the minority holding the correct answer, yielding a 10-percentage-point theoretical recovery margin. We propose Minority Sentinel, a lightweight meta-classifier that extracts a multi-dimensional debate fingerprint from debate logs and trains a LightGBM model to decide when to overturn majority voting. Minority Sentinel achieves a stable Flip Precision of 81.2% with positive Net Gain across all six datasets and all 20 random seed trials, demonstrating that debate logs contain sufficient behavioral signals for a non-LLM classifier to reliably recover suppressed minorities without degrading system accuracy. The LLM-as-Judge baseline yields negative Net Gain despite higher recall, confirming that flip safety, not recovery volume, determines intervention value.

---


### 98. [A Hybrid Framework for Song Lyric Annotation Based on Human-LLM Alignment](https://arxiv.org/abs/2606.29273)

**<font color=#1a73e8>作者：</font>** Rashini Liyanarachchi, Frank Tran, Md Mahmudul Hasan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emotion recognition of song lyrics is a challenging task since lyrics may not necessarily align with the overall emotion of a song. As a result, lyrics annotation remains largely underexplored. Drawing inspiration from research in large language model (LLM) assisted annotation, we examine the alignment between humans and LLMs for annotation of lyrics by creating a new sentence-level dataset of lyrics. Our observations highlight the subjectivity of the task and the inherent challenges. Following this, we present a hybrid annotation framework that optimizes human and LLM annotation by predicting potential misalignment in annotation.

---


### 99. [Adaptive Block Diffusion: Resolving Training-Inference Mismatch in Diffusion Language Models](https://arxiv.org/abs/2606.29275)

**<font color=#1a73e8>作者：</font>** Gagan Jain  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion Language Models (DLMs) are typically trained under fixed context structures, restricting denoising to predetermined token subsets. This creates a mismatch between training and inference, where models must operate over arbitrary configurations, leading to degradation off the training grid. We propose Adaptive Block Diffusion (ABD), which resolves this mismatch by optimizing denoising risk over a distribution of prefix-window configurations. By treating the configuration as a stochastic variable, ABD trains a single model over the full configuration space without architectural changes. We show that generalization across decoding strategies is governed by the support of the training distribution, and that ABD guarantees denoising optimality for any inference policy whose configurations are covered during training. Empirically, ABD exhibits structural invariance across decoding scales, avoiding off-grid collapse and recovering a monotonic relationship between block size and perplexity, while matching or outperforming fixed-block specialists at their target scales.

---


### 100. [Deterministic Decisions for High-Stakes AI. A Zero-Egress Pipeline with the Deployability of RAG and the Accuracy of Machine Learning](https://arxiv.org/abs/2606.29280)

**<font color=#1a73e8>作者：</font>** Craig Atkinson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We identify intervention bias as a previously unquantified failure mode of zero-shot large-language-model (LLM) educational advisory agents: without task-specific training, they recommend action when a hindsight-optimal oracle policy mandates inaction. In a six-arm ablation on the Open University Learning Analytics Dataset (N=800 students, four temporal cutoffs), at day 56 -- when the oracle designates 70.1% of students as needing no intervention -- zero-shot GPT-4o recommends action for 73%, a 43 percentage-point false-positive rate. Commercial RAG and SQL-augmented retrieval are comparably miscalibrated; at 10,000 students this implies about 4,300 unnecessary advisor contacts per cycle.
Supervised policy learning eliminates this bias: a trajectory-conditioned ONNX Decision Transformer (DT) and a snapshot XGBoost classifier, trained on the same oracle-labelled trajectories under strict prefix-only features, both achieve near-zero calibration error. The DT reaches macro-F1 0.79 (macro-recall 0.85) across all five action classes, predicting even the rare load-reduction action without collapsing, at a 0% action flip rate and sub-5 ms CPU decision latency. The two supervised arms are on par; the DT's edge over XGBoost at the final cutoff is indicative only (unpaired across cohorts).
Scope: we validate Stage-2 decision-making (EAV state vector to supervised policy) under controlled oracle input from structured OULAD data; high fidelity reflects feature-oracle alignment, not general high-stakes-AI capability. The most robust finding is the intervention-bias contrast, not the absolute accuracies. We also show an Evaluation Gap: LLM-as-judge scoring (DeepEval G-Eval) is blind to intervention bias, rewarding fluent over-prescription rather than decision quality.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-247](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
