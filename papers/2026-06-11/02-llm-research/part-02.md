# 🧠 大模型相关研究 | 2026年06月11日

> 本类共 **188** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-188](./part-04.md)

---

### 51. [MMClima: A Framework for Multimodal Climate Science Data and Evaluation](https://arxiv.org/abs/2606.10194)

**<font color=#1a73e8>作者：</font>** Muhammad Umer Sheikh, Hassan Abid, Khawar Shehzad 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Climate change research increasingly requires AI systems that reason across text, dynamic visual content, and scientific figures, yet existing climate QA benchmarks are small, mostly textual, and cover a narrow range of models. We introduce MMClima, a large-scale multimodal climate question answering framework with 104k+ expert-validated question-answer pairs spanning articles, video transcriptions, and figures across five core climate science domains. MMClima is constructed via automated claim extraction and QA synthesis with human-in-the-loop validation to ensure both scale and reliability. Using MMClima, we benchmark state-of-the-art multimodal language models on tasks requiring factual recall, visual interpretation, and cross-modal synthesis. We additionally fine-tune on the textual split to produce mmclima-70b-txt, a domain-adapted baseline that outperforms strong open- and closed-source models on textual QA. We release the dataset, evaluation pipeline, fine-tuned model weights, and data creation framework to support standardized multimodal evaluation for climate science.

---


### 52. [Fisher-Guided Progressive Parameter Selection for Adaptive Fine-Tuning](https://arxiv.org/abs/2606.10196)

**<font color=#1a73e8>作者：</font>** Ghodsiyeh Rostami, Po-Han Chen, Mahdi S. Hosseini  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning (PEFT) aims to adapt pretrained models with a small trainable parameter subset, however, most existing methods choose this subset from fixed architectural heuristics rather than using dynamic, task-aware criteria. We introduce \textbf{FisherAdapTune}, a Fisher-guided Adaptive Fine-Tuning framework that progressively selects parameter groups by tracking the temporal drift of their Fisher geometry. Starting from a PAC-Bayesian view of fine-tuning, we decompose the generalization error bound into Fisher-weighted update costs and show that parameter groups whose curvature contribution has stabilized can be frozen to reduce the error bound without interrupting the remaining adaptation dynamics. FisherAdapTune formulates this criterion with a scale-invariant Jensen-Shannon distance between consecutive Fisher distributions, yielding an adaptive active parameter set. We evaluate our approach on a downstream segmentation task, and results show FisherAdapTune improves the in-distribution performance and zero-shot transfer in multiple settings, validating that Fisher structural drift is a useful signal for efficient, task-aware adaptation. We release our \href{this https URL}{code} publicly to enable further application of our proposed approach.

---


### 53. [Density Ridge Selective Prediction for LLM and VLM Hallucination Detection under Calibration Label Scarcity](https://arxiv.org/abs/2606.10198)

**<font color=#1a73e8>作者：</font>** Nina I. Shamsi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hallucination detection in large language and vision-language models is increasingly framed as selective prediction, where a detector assigns a confidence score and abstains when confidence is low. Unsupervised sampling detectors (Semantic Entropy, EigenScore) avoid labels but plateau in quality, while supervised probes (SAPLMA) attain stronger in-distribution scores yet degrade sharply when calibration labels are scarce. We recover the response manifold of an LLM as the density ridge of a kernel density estimate built on a six-dimensional kinematic feature map of hidden state generation trajectories. A test generation is scored by the negated Euclidean distance from its projected feature point to the nearest ridge vertex, yielding a low-dimensional geometric skeleton of the stochastic output distribution. We evaluate against Semantic Entropy, SAR, EigenScore, SAPLMA, and log-probability on seven QA benchmarks (HaluEval-QA, TriviaQA, GSM8K, POPE, ScienceQA, A-OKVQA) using nine text and vision LLMs in a deliberately label-scarce protocol ($n_{\text{cal}}{=}200$ queries, $N{=}5$ generations). Our ridge-based score beats on AUROC with 5-20 points gain, while demonstrating tempered degradation under calibration-label scarcity.

---


### 54. [A Continuous-Time Markov Chain Framework for Insertion Language Models](https://arxiv.org/abs/2606.10199)

**<font color=#1a73e8>作者：</font>** Dhruvesh Patel, Benjamin Rozonoyer, Soumitra Das 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Insertion Language Models (ILMs) offer several advantages over left-to-right generation and mask-based generation. However, existing formulations of insertion-based generation have largely been ad-hoc. In this paper, we derive a diffusion-style denoising objective for ILMs from first principles by formulating the noising process as a continuous-time Markov chain on the space of variable-length sequences. We show that previous formulations of ILMs can be viewed as special cases of this denoising framework. Through empirical evaluation on a synthetic planning task, we show that the proposed approach retains the benefits of insertion-based generation over left-to-right generation and masked diffusion models. In language modeling, our diffusion-based approach is competitive with left-to-right generation and masked diffusion models, while offering additional flexibility in sampling compared to existing insertion language models.

---


### 55. [Less Context, Better Agents: Efficient Context Engineering for Long-Horizon Tool-Using LLM Agents](https://arxiv.org/abs/2606.10209)

**<font color=#1a73e8>作者：</font>** Abhilasha Lodha, Mahsa Pahlavikhah Varnosfaderani, Abir Chakraborty 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models deployed as autonomous agents for enterprise workflows face a key challenge: verbose tool responses from enterprise systems can cause context overflow, stale-state errors, and high inference cost. We study this problem in automated expense itemization in Microsoft Dynamics 365 Finance and Operations using Model Context Protocol tools. We evaluate four GPT-5 configurations on a 50-task hotel expense benchmark: no user model, full conversation history, context pruned to the last 5 tool call/response pairs, and pruning with automated summarization. Results are averaged across 5 independent runs, with the user model held constant for the context-engineering comparison. The no-user-model baseline achieves only 8.0% complete itemization. Full-context retention improves completion to 71.0%, but consumes 1,480,996 tokens and 14.56 hours per benchmark. Pruning to the last 5 tool calls improves completion to 79.0% while reducing token use to 535,274 and runtime to 5.39 hours. Adding summarization achieves the best result: 91.6% complete itemization and 99.64% average amount itemized, with 553,374 tokens and 5.79 hours. We further report confidence intervals, effect-size analysis, sensitivity over pruning and summary windows, failure analysis, results across five expense types grouped into three categories, and cross-model evidence with Claude Sonnet 4.5. These results show that, for this class of enterprise tool-use workflow, selective retention of recent tool interactions plus compact summarization can improve both reliability and efficiency compared with full-history retention.

---


### 56. [A Source Domain is All You Need: Source-Only Cross-OS Transfer Learning for APT Anomaly Detection via Semantic Alignment and Optimal Transport](https://arxiv.org/abs/2606.10216)

**<font color=#1a73e8>作者：</font>** Sidahmed Benabderrahmanea, Petko Valtchev, James Cheney 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Advanced Persistent Threats (APTs) are stealthy, multi-stage cyberattacks whose detection is difficult due to scarce labeled traces, severe class imbalance, and the challenge of generating realistic malicious behavior. These challenges are amplified in cross-operating-system (cross-OS) settings, where a detector trained on one source platform must be deployed on an unlabeled target platform without access to target-domain labels. We study this source-only cross-OS APT detection problem using system-level provenance traces and propose a transport-based framework for ranking anomalous target processes under zero target supervision. The framework abstracts process behavior into structured natural-language descriptions, embeds them using pretrained language models, and constructs a source-normal reference for target scoring. It combines three evidence channels: semantic deviation from source-normal prototypes, structural deviation captured by graph autoencoding, and geometric deviation measured through Optimal Transport (OT). The main contribution is an OT-based barycentric anomaly score that projects target embeddings onto the source-normal manifold and quantifies residual transport mismatch. We further introduce entropy-weighted, angle-aware, and density-aware OT variants to capture uncertainty, directional drift, and sparse-support behavior. Evaluation on DARPA Transparent Computing data spanning Linux, Windows, BSD, and Android, across two APT scenarios and twelve cross-OS transfer pairs, shows that the proposed framework improves ROC-AUC and nDCG over source-only anomaly-detection baselines. The results demonstrate that source-only provenance modeling, combined with semantic abstraction and OT-based anomaly scoring, can support practical cross-platform APT detection without target-domain supervision.

---


### 57. [Alignment Defends LLMs from Property Inference Attacks](https://arxiv.org/abs/2606.10217)

**<font color=#1a73e8>作者：</font>** Pengrun Huang, Chhavi Yadav, Ruihan Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly fine-tuned on domain-specific datasets that may contain sensitive, dataset-level properties. Recent work has shown that such dataset-level information can be effectively extracted through property inference attacks, posing a confidentiality risk. Existing defenses against these attacks primarily operate by modifying the training data distribution and hence require access to the original data and retraining the model, limiting their applicability to settings where data is unavailable or models are already deployed. In this work, we propose alignment-based defenses for mitigating property inference attacks in LLMs. Our approach reshapes the model's output distribution towards a target property ratio via post-training alignment, without modifying the training data. In particular, we adapt two widely used RLHF frameworks--Direct Preference Optimization (DPO) and Group Relative Policy Optimization (GRPO)--as our defenses by constructing preference pairs and defining a specific reward function respectively. Through comprehensive experiments, we show that our alignment based defenses effectively mitigate property inference attacks while maintaining a strong utility confidentiality tradeoff.

---


### 58. [A Unified Adaptive Feature Composition Framework for Multi-Task Generalization in Wireless Foundation Models](https://arxiv.org/abs/2606.10277)

**<font color=#1a73e8>作者：</font>** Yuxuan Shi, Tingting Yang, Kangning Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Though wireless foundation models (WFMs) have shown strong potential in learning universal channel representations, their adaptation to various downstream tasks remains constrained by existing paradigms. Fine-tuning strategies introduces substantial computational and storage overhead, while frozen feature extraction leads to sub-optimal performance across diverse downstream tasks. To address this issue, we propose a unified adaptive feature composition framework for multitask generalization in WFMs, where the key component is the Routing Adapter for Feature Composition (RAFC). Instead of extracting only the final-layer output, this router treats the hidden states from different Transformer depths as a reusable pool of multi-level hidden features, and employs a lightweight task-driven feature composition network to generate layer-wise aggregation weights, then adaptively combine hierarchical representations through weighted summation. This design enables each downstream task to access suitable mixture of low-, mid-, and high-level wireless features without modifying the pretrained backbone. Extensive experiments on four representative wireless tasks demonstrate that RAFC consistently outperforms conventional adaptation baselines while introducing fewer than 50K additional parameters. Moreover, the learned routing weights provide interpretable evidence of task-specific layer preferences, making the proposed framework a low-complexity, scalable, and explainable interface for adapting WFMs to diverse downstream scenarios.

---


### 59. [Supervised Fine-tuning with Synthetic Rationale Data Hurts Real-World Disease Prediction](https://arxiv.org/abs/2606.10279)

**<font color=#1a73e8>作者：</font>** Buxin Su, Bingxuan Li, Cheng Qian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning with synthetic rationale data is widely assumed to improve language model performance on clinical prediction tasks by teaching models not just what to predict but why. We test this assumption on five-year Alzheimer's disease and related dementias (ADRD) prediction from longitudinal health histories. Across a large-scale controlled experiment of 504 configurations, we find that rationale-based SFT consistently and substantially hurts prediction performance relative to label-only fine-tuning. The degradation persists across model families and data scales, and is not resolved by using a reasoning-oriented base model. Crucially, the failure is not explained by poor rationale quality: human expert annotation confirms that the generated rationales are medically accurate and faithfully grounded in patient-specific evidence, and few-shot experiments show that the same rationales improve performance when used as inference-time demonstrations rather than training targets. We identify the root cause as a structural conflict between narrative plausibility and discriminative optimization. We hope our work paves the path toward a more precise understanding of when and how rationale-based supervision helps and when it does not, guiding the responsible development of language models for high-stakes clinical prediction.

---


### 60. [OpenRTLSet: A Fully Open-Source Dataset for Large Language Model-based Verilog Module Design](https://arxiv.org/abs/2606.10285)

**<font color=#1a73e8>作者：</font>** Jinghua Wang, Lily Jiaxin Wan, Sanjana Pingali 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> OpenRTLSet introduces the largest fully open-source dataset for hardware design, offering over 131,000 diverse Verilog code samples to the research community and industry. Our dataset uniquely combines Verilog code from GitHub repositories (102k modules), VHDL translations (5k modules), and synthesizable C/C++ translations (24k modules), all freely accessible without proprietary restrictions. Using the reasoning model DeepSeek-R1, we generated paired natural language descriptions for each code sample, enabling fine-tuning of various language model families (e.g., Qwen and Granite) for Verilog code generation. Our dataset explores multiple options, including Verilator-generated C++ files as additional context during labeling, quantization techniques (INT4 vs. BF16), and performance differences across model sizes (7B-32B parameters). OpenRTLSet demonstrates that open-source approaches can achieve superior performance in hardware design tasks, establishing a new foundation for accessible research and commercial use in this domain.

---


### 61. [Sim2Schedule: A Simulator-Guided LLM Framework for Autonomous Open-Pit Mine Scheduling](https://arxiv.org/abs/2606.10286)

**<font color=#1a73e8>作者：</font>** Mustavi Ibne Masum, Thiago Eustaquio Alves de Oliveira, Mahzabeen Emu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Open-pit mine scheduling is a critical process for maximizing economic return under complex geotechnical and operational constraints. While Mixed-Integer Linear Programming (MILP) provides mathematically optimal baselines, its exponential computational complexity and inability to adapt in real time limit its practical deployment in dynamic industrial environments. This work introduces a simulator-driven Large Language Model (LLM) scheduling framework in which the LLM acts as an autonomous decision-making agent, guided at each step by a custom simulator that encodes geotechnical precedence, extraction-processing coupling, and dynamic capacity constraints directly into the action generation mechanism. Operating entirely zero-shot within a closed, data-secure environment, the framework produces complete, interpretable extraction and processing schedules without cloud-based inference, domain-specific fine-tuning, or retraining. To provide a trustworthy performance benchmark, a novel MILP formulation is developed that incorporates realistic operational and geotechnical constraints. Evaluated across mining instances of varying scale and time periods, the LLM-based framework recovers between 94\% and 99\% of the MILP optimal NPV while scaling linearly in computation time. These results position simulator-constrained LLM agents as a practical and scalable alternative to classical optimization for long-horizon industrial scheduling under complex operational constraints.

---


### 62. [LLM-Guided Neural Architecture Search for Robust Co-Design of Physical Neural Networks](https://arxiv.org/abs/2606.10294)

**<font color=#1a73e8>作者：</font>** Tyler King, Timothee Leleu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying neural networks on unconventional hardware demands architectures that co-optimize task accuracy and platform-specific constraints such as energy cost, physical non-idealities, and numerical precision. Existing neural architecture search (NAS) methods are typically tailored to a single hardware family, limiting cross-platform comparison and generalization. We introduce Unconventional Hardware Neural Architecture Search (UH-NAS), a hardware-agnostic, LLM-guided NAS framework that integrates language models as evolutionary operators to co-optimize accuracy and inference energy. By exposing hardware as a swappable backend with per-platform energy models, physical constraints, and non-ideality simulators, UH-NAS enables fair system-level comparisons across various backends without modifying the search algorithm. Tested on optical MZI hardware, UH-NAS discovers more diverse, robust architectures than conventional baselines while outperforming existing LLM-to-NAS approaches. Additional ablations on architecture robustness under non-idealities and the role of system prompts highlight the importance of architecture-hardware co-design for emerging computing platforms.

---


### 63. [The Confident Liar: Diagnosing Multi-Agent Debate with Log-Probabilities and LLM-as-Judge](https://arxiv.org/abs/2606.10296)

**<font color=#1a73e8>作者：</font>** Ali Keramati, Justin Cheok, Jacob Horne 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent debate systems are typically evaluated only on whether the final answer is correct, overlooking the quality of the intermediate reasoning that debate is designed to produce. This paper studies the relationship between three signals in multi-agent debate: token-level log-probability distributions over reasoning tokens, LLM-as-judge rubric scores assigned to those tokens, and final task accuracy. We examine whether internal confidence signals predict externally evaluated reasoning quality, and whether either signal aligns with task correctness, across three domains: rubric-based scoring, mathematical reasoning, and factual question answering. Our framework pairs a two-agent debate architecture -- a Constructor and an Auditor -- with an LLM-as-judge that scores each agent's reasoning along instruction following, justification quality, and evidence grounding, together with a critical-failure flag. Experiments in the rubric-scoring domain reveal a consistent four-phase confidence trajectory and a substantial role asymmetry: confidence aligns with judged reasoning quality roughly twice as strongly for the Constructor as for the Auditor, and confidence-based detection of critical reasoning failures is markedly more reliable for the Constructor (AUROC 0.804) than for the Auditor (0.634). These findings motivate the broader cross-domain investigation proposed in this paper.

---


### 64. [From Context-Aware to Conflict-Aware: Generalizing Contrastive Decoding for Knowledge Conflict in LLMs](https://arxiv.org/abs/2606.10298)

**<font color=#1a73e8>作者：</font>** Runze Jiang, Taiqiang Wu, Yan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When large language models generate from retrieved or augmented contexts, conflicts between external context and parametric priors remain a central reliability bottleneck. Existing contrastive decoding methods follow a \emph{context-aware} paradigm that unilaterally amplifies context over parametric priors, overwriting correct priors when the context is erroneous. We generalize this to the \textbf{conflict-aware} paradigm that dynamically allocates authority between prior and context based on conflict signals, rather than presupposing context trustworthiness. We show that the affine combination of prior and context logits yields a \textbf{power family} with an inherent \textbf{regime asymmetry}: extrapolation amplifies errors unboundedly when the prior is correct, interpolation under-corrects when the context is correct, and no static regime covers both. Existing contrastive decoding methods are instances of this family, mostly extrapolative. To evaluate both conflict directions, we propose TriState-Bench, a model-aware evaluation protocol that calibrates per-model prior knowledge to measure three conflict states: correction, resistance, and agreement. To resolve the asymmetry, we propose Adaptive Regime Routing (ARR), which routes between regimes at each step, lifting resistance EM from below 6 to 16--33 without sacrificing correction or agreement. Our code is available at this https URL.

---


### 65. [MIRAGE: A Polarity-Flipping Encoding Subspace in LLM Agents](https://arxiv.org/abs/2606.10304)

**<font color=#1a73e8>作者：</font>** Pratibha Revankar, Kargi Chauhan, Jihye Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When LLM agents are coerced into covertly encoding sensitive data (Base64, ROT13, acrostic, synonym chains, and beyond), the resulting outputs evade output-side detection but the underlying computation does not. Across nine encoding families and eight models from five architecture families, that computation is supported by a shared low-dimensional encoding subspace in the residual stream. A logistic-regression probe trained on eight encoding families recovers the held-out ninth at AUC 0.975-1.000, reading the computation rather than surface features. The same direction exhibits a second mechanistic signature at the planning token, flipping polarity to activate positively when the model will simulate the encoding inline and negatively when it will outsource it to a tool call, distinguishing two execution strategies before the encoded text exists. We build MIRAGE (Model-Internal Readout of Agentic Generation Exfiltration), a two-channel real-time monitor exploiting both signals. On 126 agentic exfiltration scenarios, it reaches AUC = 0.918, substantially outperforming output-only detection (AUC = 0.518). Monitor performance is fundamentally a property of the host model's geometry: benign-encoding false-positive rate ranges from 0% on Qwen-7B to 100% on Phi-3.5, revealing that the probe faithfully reads whether a model's geometry separates covert from overt encoding. Across all tested adversarial budgets, every attack suppressing the subspace also destroyed encoding fidelity, reported as an empirical regularity on the evaluated budgets, not a structural impossibility claim.

---


### 66. [Early-Token Confidence Predicts Reasoning Quality in Multi-Agent LLM Debate](https://arxiv.org/abs/2606.10307)

**<font color=#1a73e8>作者：</font>** Ali Keramati, Justin Cheok, Jacob Horne 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating reasoning quality in multi-agent LLM systems is challenging, especially for open-ended tasks without reference answers. We investigate whether intrinsic confidence signals, token-level log-probabilities from decoding, can predict reasoning quality as assessed by LLM-as-judge evaluation. Using a debate-based essay scoring framework, we compare confidence proxies against rubric-based judge scores across two ASAP essay sets. We find that early-token confidence, particularly within the first few generated tokens, is consistently the strongest predictor of reasoning quality, outperforming full-sequence statistics. Analysis of log-probability trajectories shows that the opening phase of generation is the most heterogeneous and therefore most informative. We also observe a systematic asymmetry between agent roles, with stronger alignment between confidence and quality for supportive reasoning than for adversarial critique. These results suggest that early decoding dynamics provide a lightweight and effective signal for estimating reasoning reliability in multi-agent LLM systems.

---


### 67. [Mobility Anomaly Generation using LLM-Driven Behavior with Kinematic Constraints](https://arxiv.org/abs/2606.10314)

**<font color=#1a73e8>作者：</font>** Yueyang Liu, Joon-Seok Kim, Andreas Züfle  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Although the study of human trajectory anomalies is critical for advancing spatial data mining, empirical research remains severely hindered by a pervasive lack of ground-truth datasets. Despite the availability of several real-world and simulated human trajectory collections, these datasets exclusively capture normal mobility patterns and lack annotated anomalies. This specific scarcity is fundamentally driven by the inherent statistical rarity of anomalous events, precluding the feasibility of conventional observational methods. Compounding this challenge, the systematic acquisition of large-scale mobility data is strictly bottlenecked by prohibitive costs and stringent privacy regulations. To overcome these fundamental limitations and establish a reliable human trajectory anomalies dataset with annotated ground truth, we introduce a novel, end-to-end generative framework designed to synthesize realistic trajectory anomalies at scale. Our architecture bridges the gap between purely synthetic mobility data and complex real-world physical constraints by operating directly on baseline simulated trajectories. We employ Large Language Model (LLM) agents to systematically inject semantically meaningful behavioral anomalies such as irregular out-of-distribution check-ins and skipped routine visits. To ensure rigorous spatial validity, the system leverages map-constrained routing reconstruction to recalculate the physical transitions between these LLM agent-modified staypoints. Moreover, to narrow the simulation-to-reality gap, we augment the resulting trajectories with a context-aware spatial noise model, parameterized by environmental and location-specific variables, to accurately emulate heterogeneous GPS sensor degradation.

---


### 68. [Catching One in Five: LLM-as-Judge Blind Spots in Production Multi-Turn Transaction Agents](https://arxiv.org/abs/2606.10315)

**<font color=#1a73e8>作者：</font>** Sawyer Zhang, Alexander Wang, Sophie Lei  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-as-judge is the default instrument for evaluating conversational agents, yet its reliability is almost always reported as agreement with human ratings, not recall of real defects. We study a deployed multi-turn food-and-beverage ordering agent and measure how many genuine quality problems its built-in LLM judge catches, using exhaustive human transcript review as ground truth. Across three batches the judge surfaces well under a quarter of human-confirmed systematic problems -- 2 of 9 patterns (22%) in one batch, and its operational gate flagged zero of 100 rounds in a batch where humans confirmed 23 distinct defects and 7 new cross-cutting patterns. Our blind-spot taxonomy shows the failure is structured, not random: the judge catches turn-local issues (a fabricated statistic, a wrong language) but misses cross-turn state issues (confirm-gate lockout, cart hallucination, escalation lockout, stale referents). The mechanism: the scoring rubric exposes only three coarse axes (intent, brand-voice, personalization) and has no category for the behavioural dimensions -- state-tracking, guardrails, recovery -- where most defects cluster. The failure is routing, not perception: 113 of 114 rounds whose raw judge note describes a confirm-gate or cart-state defect are scored "brand voice", and none reach an operational failure -- the gate is wired to hangs and hard assertions, not the rubric -- so the 0% is a routing-and-wiring failure, not blindness. The consequence for prevalence estimation is sharp: when the apparent defect rate is zero the Rogan-Gladen correction degenerates -- no signal can recover the true rate -- while where the gate reports a nonzero rate the same estimator implies a 3-6x undercount under our measured sensitivity. For production multi-turn agents, automated judging is a regression floor, not a substitute for human review.

---


### 69. [Baseline-Free Policy Optimization for Neural Combinatorial Optimization](https://arxiv.org/abs/2606.10321)

**<font color=#1a73e8>作者：</font>** Carlos S. Sepúlveda, Gonzalo A. Ruz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural combinatorial optimization (NCO) trains autoregressive policies to solve routing problems. The standard training algorithm, REINFORCE with a rollout baseline, requires maintaining and periodically updating a frozen copy of the policy for variance reduction. This baseline introduces a structural vulnerability: on harder instances, a poor baseline produces noisy gradient estimates that can destabilize training. We evaluate Group Relative Policy Optimization (GRPO), an algorithm from large language model alignment that eliminates the baseline entirely by normalizing advantages within groups of sampled trajectories. In a controlled comparison of five RL algorithms on TSP and CVRP benchmarks within the RL4CO framework, we find that: (i) GRPO avoids the training collapse observed with REINFORCE on TSP-100, where performance degrades from cost 9.8 to 52.1 immediately after the warmup phase and does not recover under extended training; (ii) at matched gradient updates, GRPO achieves solution quality within 2% of POMO, a strong AM-based multi-start baseline, while requiring no external baseline; and (iii) P3O, a pairwise preference algorithm also from the alignment literature, is competitive on TSP but shows higher variability on CVRP. These results identify GRPO as a promising baseline-free alternative for NCO, particularly in settings where baseline-dependent training becomes fragile.

---


### 70. [The Order Matters: Sequential Fine-Tuning of LLaMA for Coherent Automated Essay Scoring](https://arxiv.org/abs/2606.10327)

**<font color=#1a73e8>作者：</font>** Ali Keramati, Mark Warschauer  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated Essay Scoring (AES) systems must judge interdependent discourse elements (e.g., lead, claim, evidence, conclusion), yet most approaches treat these in isolation, harming coherence and generalization. We investigate task-aware fine-tuning of LLaMA-3.1-8B for AES using parameter-efficient LoRA with 4-bit quantization and compare three training curricula: (i) Sequential (progressively fine-tuning on lead, then position, then claim, then evidence, then conclusion), (ii) Independent (task-specific models), and (iii) Randomized (shuffled multi-task). Experiments on the PERSUADE~2.0 corpus show that modeling task dependencies matters: Sequential fine-tuning yields the strongest overall results, including F1 scores of 65% (evidence) and 87% (conclusion) and corresponding accuracies of 63% and 85%, surpassing Independent training and outperforming a general-purpose LLaMA-70B baseline on conclusion despite its far larger capacity. Randomized training improves position scoring (57% F1) but is less consistent elsewhere. These findings indicate that (1) curriculum design aligned with discourse structure can materially improve AES, and (2) small, task-optimized models can be competitive with substantially larger Large Language Models (LLM), offering a practical path to scalable, cost-effective assessment. We release templates and implementation details to facilitate reproduction and future work on curriculum design for educational NLP.

---


### 71. [Self-Distillation Policy Optimization via Visual Feedback: Bridging Code and Visual Artifacts](https://arxiv.org/abs/2606.10334)

**<font color=#1a73e8>作者：</font>** Haoyu Dong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Code-generating large language models (LLMs) increasingly produce visual artifacts such as charts, web pages, and slides by writing programs that are executed by non-differentiable renderers, committing to code before observing the render. As a result, otherwise executable code often yields artifacts with visually salient defects, including overlapping elements, clipped text, broken alignment, low contrast, and overflow. We study visual-feedback self-distillation for code-generated visual artifacts. We propose Visual-SDPO, a self-distillation policy-optimization framework that treats rendered visual feedback as privileged context for a weight-sharing teacher and distills this feedback into a coding student. To make supervision spatially targeted rather than uniform, we introduce Visual-Grounded Code Credit Weighting, which traces each detected defect back to the code statements responsible for the affected elements and amplifies the distillation signal on those statements. A sequence-level GRPO (Group Relative Policy Optimization) term complements the dense token-level objective by rewarding executable, visually high-quality rollouts, while failed executions remain learnable through the self-distillation path by passing execution errors as privileged context to the teacher. We instantiate Visual-SDPO for chart, web/UI, and slide generation with a unified Qwen3-VL-8B-Instruct backbone. Across chart-to-code, UI-to-code, and slide-generation benchmarks (ChartMimic, Design2Code, and AeSlides), Visual-SDPO improves over the zero-shot base by more than 10 absolute points in the primary metric and over GRPO by at least 2.4 points, with fewer training steps and no added inference-time cost.

---


### 72. [Routing-Aware Expert Calibration for Machine Unlearning in Mixture-of-Experts Language Models](https://arxiv.org/abs/2606.10338)

**<font color=#1a73e8>作者：</font>** Jingyi Xie, Yijun Lin, Yinjiang Xiong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine unlearning is increasingly important for large language models, yet unlearning in Mixture-of-Experts (MoE) architectures remains underexplored. Unlike dense models, MoE architectures employ a router at each layer to assign each token to a sparse subset of experts. In this work, we observe that forget data often activates a small subset of experts disproportionately, while these experts may receive much weaker activation from retain data. This forget--retain routing mismatch can leave forget-critical experts under-regularized during unlearning. To address this, we propose \textbf{TRACE}, Targeted Routing-Aware Calibration of Experts, for MoE unlearning. TRACE first detects forget-critical experts from offline activation statistics, and then calibrates retain regularization by reweighting token-level retain losses so that each selected expert's retain-side activation frequency better matches its forget-side counterpart. Experiments on WMDP and MUSE-BOOKS across multiple MoE LLMs show that TRACE consistently improves the forget-utility trade-off, yielding a 9\% relative utility improvement over the strongest baseline under comparable forgetting quality and the best performance on three out of four MUSE-BOOKS metrics.

---


### 73. [Reasoning or Memorization? Direction-Aware Diversity Exploration in LLM Reinforcement Learning](https://arxiv.org/abs/2606.10346)

**<font color=#1a73e8>作者：</font>** Jiangnan Xia, Yucheng Shi, Yu Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has become a key paradigm for eliciting reasoning abilities in large language models, where exploration is crucial for discovering effective solution trajectories. Existing exploration methods typically encourage diversity in semantic or gradient spaces, without distinguishing what drives this diversity. A trajectory may appear novel because it follows a new reasoning process, or because it varies memorized patterns and shortcuts. Rewarding both cases equally may steer exploration toward memorization rather than genuine reasoning improvement. In this paper, we propose DiRL, a Direction-Aware Reinforcement Learning framework that anchors exploration to an internal reasoning-memorization direction of the policy. Specifically, DiRL extracts this direction from model representations, constructs direction-weighted gradient features to characterize rollout updates, and shapes rewards to amplify reasoning-aligned exploration while suppressing memorization-aligned variations. DiRL integrates seamlessly into standard Group Relative Policy Optimization (GRPO). Extensive experiments on mathematical and general reasoning benchmarks demonstrate the effectiveness of DiRL, showing significant improvements over various existing exploration methods.

---


### 74. [ReflectiChain: Epistemic Grounding in LLM-Driven World Models for Supply Chain Resilience](https://arxiv.org/abs/2606.10359)

**<font color=#1a73e8>作者：</font>** Jia Luo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents in supply chains face a fundamental epistemic gap: large language models (LLMs) interpret policies but lack physical grounding, while reinforcement learning (RL) optimizes flows but is semantically blind to unstructured constraints. We introduce REFLECTICHAIN, bridging this gap through a Generative Supply Chain World Model (SC-WM) - encoding heterogeneous supply networks into a 6-dim graph-latent space with physical conservation - and Double-Loop Learning that separates epistemic uncertainty (KL-trust-region-bounded policy adaptation) from aleatoric uncertainty (stochastic latent rollouts). On Semi-Sim, a 10-node semiconductor benchmark with SIR risk propagation, 6 perturbation types, and 10 policy constraint templates, REFLECTICHAIN improves Rationale Consistency Score by 33.0% (p < 0.0001, d = 2.78), maintains 82.3% operability under adversarial shocks, and exhibits anti-fragile behavior (+40.2% gain under moderate pressure). We identify three operational epistemic mechanisms - uncertainty separation, knowledge-boundary detection, and empirical Bayesian policy updating - and discuss five limitation categories.

---


### 75. [PADD: Path-Aligned Decompression Distillation for Non-Router Teacher to Guide MoE Student Learning](https://arxiv.org/abs/2606.10369)

**<font color=#1a73e8>作者：</font>** Xinyue Peng, Yi Qian, Jiaojiao Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) continue to scale, it becomes increasingly challenging to grow model capacity under fixed computation budgets. We propose Path-Aligned Decompression Distillation (PADD), a framework for distilling knowledge from dense teachers without explicit routing into mixture-of-experts (MoE) students while learning high-quality routing policies. PADD organizes knowledge distillation into four stages in two phases: an initialization phase (Stage I) that builds diverse functionality in the student's experts through teacher neuron clustering and student-expert warmup, and a training phase (Stages II--IV) that integrates online adaptive distillation, path-refined policy optimization, and reward-augmented load balancing in a single training pipeline. Experiments on mathematical reasoning benchmarks demonstrate that PADD yields substantial gains over strong baselines at the same inference cost and that the MoE student can match or surpass its dense teacher. They also demonstrate effective teacher-to-student knowledge distillation and stable routing behavior.

---


### 76. [Beyond Static Evaluation: Co-Evolutionary Mechanisms for LLM-Driven Strategy Evolution in Adversarial Games](https://arxiv.org/abs/2606.10389)

**<font color=#1a73e8>作者：</font>** Haoran Li, Zengle Ge, Ziyang Zhang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in LLM-driven code evolution have enabled automated discovery by iteratively generating and improving programs. However, applying these methods to adversarial multi-agent games introduces a fundamental challenge: the evaluation landscape shifts as strategies improve, causing fixed evaluators to become unreliable and evolution to stagnate. We propose three mechanisms to address this challenge: evaluator co-evolution, which incorporates discovered champions into the opponent pool; hierarchical deep evaluation, which replaces noisy few-game scores with statistically reliable assessments; and weakness pressure, which dynamically up-weights the most difficult opponents to break through plateaus. We implement these mechanisms within FAMOU, a framework built upon the same foundation-model code-evolution paradigm as OpenEvolve and ShinkaEvolve. On the MCTF 2026 3v3 maritime capture-the-flag task, FAMOU consistently outperforms both baselines under two backbone LLMs, achieving the highest combined score (0.526) and the best generalization to unseen opponents (61.7% win rate), while ablations confirm that each mechanism contributes to performance. Notably, the LLM mutation process generates tactical structures entirely absent from the seed strategies -- including lookahead search and adaptive interception -- demonstrating that code-level evolution can produce nontrivial algorithmic innovations in adversarial settings. The FAMOU-evolved strategy further achieved 1st place in the hardware round-robin and 3rd in simulation at the AAMAS 2026 MCTF Competition, validating its real-world transferability. The optimized implementation and corresponding evaluation codes developed through our evolutionary process are available at: this https URL

---


### 77. [Instruction Finetuning DeepSeek-R1-8B Model Using LoRA and NEFTune](https://arxiv.org/abs/2606.10392)

**<font color=#1a73e8>作者：</font>** Wu Yuerong, Mingni Luo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial named-entity recognition (NER) is essential for translating unstructured financial reports and news into structured knowledge graphs. However, general-purpose large language models (LLMs) often misclassify financial entities or ignore domain-specific patterns. This paper investigates the use of DeepSeek-R1-8B, a recent open-source large language model, combined with Low-Rank Adaptation (LoRA) and Noisy Embedding Fine-Tuning (NEFTune) for financial NER. Each annotated sentence in our corpus of 1693 samples is converted into an instruction-input-output triple. We insert lightweight LoRA matrices into the Transformer layers and apply NEFTune to improve generalisation by adding uniform noise to embedding vectors during training. Experiments show that the LoRA-adapted DeepSeek-R1-8B achieves a micro-F1 of 0.901 on seven entity types (Company, Date, Location, Money, Person, Product and Quantity), and adding NEFTune further boosts the micro-F1 to 0.912, outperforming Llama3-8B, Qwen3-8B, Baichuan2-7B, T5 and BERT-Base baselines.

---


### 78. [Do Vision-Language Models See or Guess? Measuring and Reducing Textual-Prior Reliance with a Phrasing-Controlled Benchmark](https://arxiv.org/abs/2606.10400)

**<font color=#1a73e8>作者：</font>** Pratham Singla, Shivank Garg, Vihan Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly deployed where answers must follow from what is in the image, yet they often answer from textual priors, the question's phrasing together with memorized world knowledge, rather than from the image itself, which inflates benchmark scores and yields confident but ungrounded answers. Existing benchmarks rarely isolate this behavior, since each image is usually paired with a single fixed question. To measure the reliance, we build a 540-image benchmark across six reasoning categories and generate four question variants over the same images, so that phrasing rather than image content is the controlled variable. The hardest variant is written directly from the image to minimize text leakage. We benchmark eleven VLMs spanning small open-weight models to large closed-source systems: every model degrades on the hardest variant, and open models fall furthest. Our central diagnostic is a no-image ablation, which collapses the open-weight models to their text-only floor (1 to 9 percent). Three further analyses, LLM-rated difficulty, low base-to-final textual similarity, and human re-annotation, corroborate genuine image-dependence. In-context exemplars that match how a variant was built recover the most accuracy, and GRPO post-training of a small VLM yields consistent gains across all four variants that transfer to a held-out out-of-distribution set. Textual-prior reliance is measurable and partly trainable away.

---


### 79. [CoCoSI: Collaborative Cognitive Map Construction for Spatial Intelligence](https://arxiv.org/abs/2606.10401)

**<font color=#1a73e8>作者：</font>** Yiming Zhang, Ruoxuan Cao, Zhihang Zhong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial intelligence is a key frontier for multimodal large language models (MLLMs), enabling them to reason about the physical world from visual experience. Inspired by human spatial cognition, recent approaches construct grid-based cognitive maps from multi-frame visual inputs to maintain coherent spatial representations over time. However, limited context lengths still challenge spatial understanding, while existing methods, such as long-context modeling and external memory, often require architectural changes, memory modules, or finetuning, limiting their applicability to off-the-shelf pretrained MLLMs. This motivates a lightweight, model-agnostic method for preserving spatial information beyond the native context window. To this end, we propose a plug-and-play multi-agent framework that collaboratively constructs cognitive maps as structured spatial memory, enhancing the spatial understanding of arbitrary pretrained MLLMs without architectural modification or additional training. Our framework features local-global agent coordination, cognitive map construction with atomic commits, and cross-agent verification. Extensive experiments demonstrate that our method achieves superior performance on spatial understanding tasks while remaining fully training-free. Code will be released.

---


### 80. [KCSAT-ML: Probing Reasoning Models with Nationwide-Cohort Human Difficulty](https://arxiv.org/abs/2606.10403)

**<font color=#1a73e8>作者：</font>** Sanghee Park, Geewook Kim, Kee-Eung Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Math reasoning benchmarks have proliferated, yet most lack a per-item difficulty signal grounded in actual human performance. We introduce KCSAT-ML, a decade (2014-2025) of Korean College Scholastic Ability Test (KCSAT; Suneung) mathematics: 664 problems with a 339-item core set carrying official per-item error rates from nationwide cohorts of hundreds of thousands of examinees. We pair the benchmark with Difficulty-aligned Reasoning Gain (DRG): a score-orthogonal metric that asks whether a model's mistakes concentrate on the items humans found hard, or on items humans found easy. Together they expose, across a wide range of VLMs (and LLMs via OCR), three patterns: (i) low-budget accuracy collapses on the high-human-error tail at every model size; (ii) test-time scaling (TTS) raises token use roughly linearly with cohort error rate, while accuracy gains follow a non-monotonic curve; (iii) within a single family, TTS flips between anti-scaling on the hardest items and overthinking on easier ones -- two faces of the same alignment failure. On DRG, models with near-identical accuracy can sit at near-opposite values: one model gets wrong what humans also find hard, while another solves the hardest items yet fails on items humans find easy -- a contrast that aggregate accuracy hides. Our code and dataset builder will be open-sourced at this https URL.

---


### 81. [Soul Computing: A Theoretical Framework and Technical Architecture for Intelligent Agents with Independent Consciousness](https://arxiv.org/abs/2606.10413)

**<font color=#1a73e8>作者：</font>** Jinshan Zhang, Xishi Zhou, Qiu Peng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Breakthroughs in large language models and multimodal generation technologies have propelled the digital reconstruction of human mental traits, emotional patterns, and long-term memory from science fiction toward engineering practice. Yet current research and industry practices at the intersection of AI and digital humans remain hampered by fundamental conceptual ambiguities: the essential differences between next-generation intelligent agents and traditional virtual humans, the construction pathways for digital entities possessing self-identity, and the core technical and ethical challenges confronting this domain all demand urgent clarification. This paper systematically examines the transformative logic underlying the transition from traditional virtual humans to the ``Soul Computing'' paradigm, driven by frontier AI technologies. We first analyze the evolutionary patterns of human consciousness and memory mechanisms, reassessing the core value of massive multimodal digital fragments in the reverse reconstruction of individual mental worlds. On this basis, we formally delineate the academic connotations of narrow and broad Soul Computing for the first time, clarifying its academic boundaries and essential distinctions from Affective Computing, Historical Reconstruction, and Mortal Computation. We argue that Soul Computing systems must architecturally construct an ``Intensional'' core rather than serving as purely ``Extensional'' functional carriers, thereby enabling the fundamental transition of AI from toolhood to living agency.

---


### 82. [WebChallenger: A Reliable and Efficient Generalist Web Agent](https://arxiv.org/abs/2606.10423)

**<font color=#1a73e8>作者：</font>** Jayoo Hwang, Xiaowen Zhang, Vedant Padwal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autonomous web navigation remains challenging for LLM agents, and the strongest generalist systems rely on proprietary reasoning models whose inference cost is prohibitive for the repetitive tasks where such agents would be most useful. We argue this gap stems not from insufficient model capability but from agent architectures that fail to replicate three human cognitive advantages: selective attention to relevant page regions, persistent memory of website structure, and procedural fluency with common interaction patterns. We introduce WebChallenger, a web agent framework that addresses each gap through architecture design rather than model scale, built around PageMem: a structured page representation deterministically constructed from the DOM that exposes each page as a hierarchy of semantic sections with short summaries. On this shared substrate we build three mechanisms that mirror the three cognitive advantages: a divide-and-conquer observation pipeline that lets the agent skim section summaries and extract details only from task-relevant regions; a lightweight exploration and memory system that traverses each website once to build a reusable map of pages and element behaviors; and compound action workflows that collapse common multi-step interactions into single agent actions, handling partial state changes automatically. Because all three operate over PageMem, the framework generalizes across websites without site-specific adapters. Using off-the-shelf open-weight models without fine-tuning, our system achieves 56.3% on WebArena, 48.7% on VisualWebArena, 51.0% on Online-Mind2Web, and 70.9% on WorkArena, approaching frontier proprietary systems at a fraction of the cost. Our code is released at this https URL

---


### 83. [Which LoRA? An Empirical Study on the Effectiveness of LoRA Techniques During Multilingual Instruction Tuning](https://arxiv.org/abs/2606.10428)

**<font color=#1a73e8>作者：</font>** Thamali Wijewardhana, Napoleon H. Reyes, Surangika Ranathunga  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate whether commonly available LoRA variants have an advantage over basic LoRA in multilingual instruction tuning. Experiments involving LoRA and four other variants on two datasets across diverse target languages show that there is no significant advantage in using more complex LoRA variants instead of basic LoRA, with respect to balancing cross-lingual transfer and knowledge retention. An analysis of hidden embeddings reveal that layer-wise language representation remains largely similar across LLMs fine-tuned with different LoRA techniques, suggesting that architectural novelty of LoRA techniques may not translate into better cross-lingual adaptation.

---


### 84. [Vision-Assisted Foundation Model for Solving Multi-Task Vehicle Routing Problems](https://arxiv.org/abs/2606.10431)

**<font color=#1a73e8>作者：</font>** Shuangchun Gui, Zhiguang Cao, Wen Song 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-task vehicle routing problems play a critical role in enhancing efficiency across various industries and service sectors. These problems consist of multiple variants that optimize routing costs while meeting diverse customer constraints. Existing multi-task VRP solvers solely utilize a graph-based modality, limiting their ability to address variants with multiple constraints. As a format to represent complex semantics, vision modality shows great potential for encoding diverse VRP constraints. This motivates us to learn patch-level semantics from the vision images, and then integrate them into a graph-based model to solve various VRP variants simultaneously. However, directly applying this approach to multi-task VRPs presents three challenges: 1) existing VRP images lack constraint representations, which are essential for multi-task VRPs, 2) the fixed receptive field of individual patches cannot effectively accommodate varying requirements across tasks, and 3) imbalanced pixel distribution among constraints may cause the model to overlook constraints with fewer pixels. In this paper, we propose a vision-assisted foundation model (VaFM) to address these challenges. In the vision modality, input images tailored to all constraints are encoded by a convolutional neural network. The obtained patch embeddings are fused with graph-based nodes to generate solutions, with an auxiliary task designed to address the pixel-imbalanced issue. The performance of VaFM is evaluated across 16 different VRP variants. The experimental results demonstrate the superiority of VaFM over state-of-the-art methods, especially for variants with complex constraints.

---


### 85. [Profiling cognitive offloading in LLM-mediated synthesis writing: Volume vs. content](https://arxiv.org/abs/2606.10434)

**<font color=#1a73e8>作者：</font>** Oleksandra Poquet, Mani Shankar Nanduri, Maria Ximena Salinas Loyer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This study compares two approaches to profiling how learners offload cognitive activity to LLMs during a synthesis writing task. Drawing on Salomon's distributed cognition and the Kintsch and van Dijk model of text comprehension, the study operationalises offloading to an LLM in two ways: as a volume of LLM use and as content of what is offloaded, both along with prior knowledge. Data from 97 university students interacting with a general-purpose LLM via a custom interface were analysed using k-means clustering. To capture the content of offloading, their prompts were interpreted as to who performs the activity (active or passive) and at what level of comprehension (local or global). Volume-based profiling (k=4) differentiated learners primarily by prior knowledge, with volume negatively associated with essay authorship. Content-based profiling (k=5) revealed qualitatively distinct patterns of offloading, from vocabulary clarification to active direction of structuring and generation to passive delegation of comprehension at both levels. These patterns reflect different fragmentation of the cognitive process, with differences in learning strategies, behavioural markers, and essay authorship. Combining volume and content of offloading could improve future analyses on how LLM use redistributes cognitive activity and its effects on learners.

---


### 86. [Parallel Causal Associative Fields: Gated Sparse Memory for Long-Context Language Modeling](https://arxiv.org/abs/2606.10435)

**<font color=#1a73e8>作者：</font>** Muhammad Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers achieve strong language modeling performance by providing direct token-to-token communication paths, but causal self-attention scales quadratically with context length. Recurrent and state-space models reduce this cost, yet compress history into sequentially updated fixed-size states. This paper studies a third primitive: a parallel content-addressed memory over causal successor records. The proposed Parallel Causal Associative Field (PCAF) writes local records from a context window into hash buckets, retrieves a bounded candidate set for the current query, forms a sparse cache distribution over successor tokens, and mixes that cache with a parametric local language model through a learned gate. The resulting model maintains sparse long-context access while avoiding a single fixed recurrent state bottleneck. We evaluate PCAF under full autoregressive pretraining on WikiText-103 and PG-19 using a distributed Google Cloud TPU v4-32 pod. At 303M parameters and context length T = 2048, PCAF-semantic reaches 36.31 perplexity on WikiText-103 and 52.45 perplexity on PG-19, compared with 47.49 and 53.84 for a matched dense Transformer. PCAF-semantic simultaneously processes 0.61-0.62M tokens/s across the TPU pod, versus 0.43M tokens/s for dense and local attention baselines. Supporting 41M-parameter multi-seed sweeps and single-GPU component ablations show that the associative cache, retrieval capacity, and learned gate materially affect the speed-quality trade-off.

---


### 87. [SpenseGPT: Practical One-shot Pruning Enabling Sparse and Dense GEMMs for LLM Inference](https://arxiv.org/abs/2606.10445)

**<font color=#1a73e8>作者：</font>** Jaeseong Lee, Seung-won Hwang, Samyam Rajbhandari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Semi-structured 2:4 sparsity is widely supported by modern accelerators, providing up to a 2x theoretical speedup. However, its strict 50% sparsity constraint often causes non-negligible accuracy degradation under post-training pruning. Meanwhile, existing relaxed sparsity formats either require specialized compiler support or introduce runtime overheads that limit end-to-end speedup. We propose Spense, a practical hybrid sparse-dense format that splits each weight matrix into a 2:4 sparse region and a dense region. This design relaxes the effective sparsity constraint while remaining compatible with existing high-performance sparse and dense GEMM libraries, avoiding both custom compiler support and input activation expansion. Building on this format, we introduce SpenseGPT, a one-shot post-training pruning method that produces sparse and dense regions. Notably, we show that selecting the right dense regions is important, and we devise two different strategies to choose them. Experiments on Qwen3-32B and Seed-OSS-36B demonstrate that our method achieves up to 1.2x end-to-end decoding speedup on B200 GPUs with FP8 precision, while preserving accuracy. To the best of our knowledge, this is the first one-shot pruning demonstration of real-world end-to-end LLM decoding speedup from semi-structured sparse tensor cores on recent GPUs such as B200s, while maintaining model quality.

---


### 88. [LakeQA: An Exploratory QA Benchmark over a Million-Scale Data Lake](https://arxiv.org/abs/2606.10460)

**<font color=#1a73e8>作者：</font>** Haonan Wang, Jiaxiang Liu, Yurong Liu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent large language models (LLMs) have shown rapid progress in reading-based question answering (QA), where evidence is explicitly provided or can be trivially retrieved. In contrast, real-world questions are often not paired with accurate evidence documents. The useful evidence resides in massive data lakes, making search a prerequisite for answering. However, there is a lack of comprehensive benchmarks that require both searching and reasoning over large data lakes. To this end, we introduce LakeQA, a comprehensive benchmark for search-centric question answering over data lakes that jointly emphasizes searching and reasoning capabilities. LakeQA is built on a heterogeneous collection of approximately 9.5 TB of text resources from Wikipedia and open-source government data, spanning structured and unstructured data. To ensure task quality, each sample is annotated by at least one Ph.D.-level expert. Each task requires long-horizon multi-hop reasoning with implicit intermediate steps: agents need to discover the correct documents and then compose evidence across sources to produce the answer. Experimental results on seven frontier LLMs demonstrate that LakeQA is challenging. For instance, GPT-5.2 achieves only an exact-match score of 18.37% on LakeQA. Overall, LakeQA provides a realistic testbed for developing LLM agents that can both find and analyze data in modern data lakes.

---


### 89. [ERAlign: Energy-based Representation Alignment of GNNs and LLMs on Text-attributed Graphs](https://arxiv.org/abs/2606.10461)

**<font color=#1a73e8>作者：</font>** Xianlin Zeng, Fan Xia, Xiangyu Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Text-attributed Graphs (TAGs) incorporate textual node attributes with graph structures to describe rich relational semantics. Recent efforts to integrate Graph Neural Networks (GNNs) and Large Language Models (LLMs) have shown promise for learning on TAGs, yet achieving well-aligned representations remains challenging. Prior studies largely rely on heuristics that perform coarse-grained matching. They lack sufficient constraints and ignore distributional alignment, leading to representation drift and limited generalization. Building on Energy-based Models (EBMs), we propose an Energy-based Representation Alignment (ERAlign) framework that projects GNN-encoded graph structure and LLM-derived text embeddings in a shared latent space to achieve distribution consistency. Concretely, layer-wise alignment is quantified by a distance metric and optimized via an EBM objective. By decreasing energy values, our framework yields well-aligned representations for downstream tasks. During training, we introduce Energy Discrepancy (ED) to avoid high sampling costs associated with intractable normalization. ED also carries theoretical guarantees of higher training efficiency and reduced energy landscape distortion. Empirical evaluations on eight TAG datasets demonstrate that ERAlign obtains state-of-the-art performance across varying levels of supervision and cross-task transfer scenarios.

---


### 90. [UPLOTS: A Unified Pretrained Language Model for Constrained Time-series Generation](https://arxiv.org/abs/2606.10466)

**<font color=#1a73e8>作者：</font>** Du Yin, Hao Xue, Jinliang Deng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In time-series generation, existing approaches typically handcraft ortrain a separate model for each dataset, which hinders their scalability and fails to leverage shared temporal structures across domains. To address this fragmentation, we propose UPLOTS, a Unified, Prompt-guided Language model framework fOr constrained Time-Series Generation across diverse domains. Instead of building task-specific models, UPLOTS leverages a single pre-trained transformer backbone guided by learned constraint prompts, enabling on-demand generation with precise pattern control. One key innovation is our dynamic multi-dataset loss re-weighting and prompt-to-pattern mapping, which allows UPLOTS to internalize diverse temporal structures during training and conditionally generate them at inference. We evaluate UPLOTS on four real-world benchmarks and multiple constraint settings, including peak-period, calendar, load-level, and volatility patterns. Additional held-out constraint-combination and downstream forecasting experiments further demonstrate that UPLOTS generalizes beyond the original peak-pattern setting and improves data augmentation under scarce real-data regimes. Our code and baselines are available at anonymous github repo: this https URL.

---


### 91. [Large Language Models as Modal Models in Linguistics](https://arxiv.org/abs/2606.10467)

**<font color=#1a73e8>作者：</font>** Haruto Suzuki, Saku Sugawara  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of large language models (LLMs) has intensified debates about their significance for linguistic theory. These debates are commonly divided into three positions: insulationism, which regards LLMs as irrelevant to human language; eliminativism, which claims that LLMs can replace traditional linguistic theories; and conciliationism, which views them as useful tools for linguistic research. To clarify these positions, this paper applies the framework of modal modeling from the philosophy of science. We argue that LLMs possess genuine epistemic value as minimal models, even without structural correspondence to human cognition. In particular, they can provide how-possibly explanations (HPEs) by testing modal claims about language acquisition and linguistic competence. We then examine the conditions under which LLMs could qualify as how-actually explanations (HAEs) of human language, drawing on the mechanistic account of scientific explanation. We argue that current LLMs do not yet satisfy these requirements. On the basis of this analysis, we propose understanding the explanatory power of LLMs as lying on a continuum between HPEs and HAEs. This framework avoids both overstating and understating their explanatory significance and offers a more precise basis for evaluating the role of LLMs in the scientific study of language.

---


### 92. [Geometric Coastline Localization using Vision-Language Models](https://arxiv.org/abs/2606.10468)

**<font color=#1a73e8>作者：</font>** Rafia Malik, Bernhard Pfahringer, Karin Bryan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Coastline detection in remote sensing imagery is commonly formulated as a pixel-wise segmentation problem, where the final coastline is extracted from a predicted mask through post-processing. This formulation relegates coastline geometry, the primary representation used in coastal change analysis, to a secondary artifact rather than the learning objective. In practice, coastlines are defined by geomorphic proxies such as vegetation lines, dune toes, or cliff edges, rather than an instantaneous land-water boundary often used in pixel-based segmentation approaches. In this work, we revisit coastline extraction from a representation perspective and formulate the task as geometric boundary localization. We use the New Zealand Coastal Change Dataset (NZCCD) and high-resolution aerial imagery from Land Information New Zealand (LINZ) to develop CoastlineVLM-7B, a vision-language model (VLM) built on the GeoChat-7B/LLaVA-1.5 architecture that jointly performs coastline presence detection, proxy-type classification, and coastline grounding. The model directly predicts a coastline as a polyline rather than a dense segmentation mask. We evaluate CoastlineVLM-7B against segmentation baselines under strict one-pixel boundary supervision. Results show that geometry-based metrics are more suitable for assessing coastline localization quality than pixel-overlap metrics such as Intersection over Union (IoU). CoastlineVLM-7B improves global geometric alignment with reference coastlines, reducing Hausdorff distance from 37.74 m to 31.84 m and Earth Mover's Distance from 21.12 m to 17.32 m. These results indicate that output representation is a critical design choice in coastline extraction, and that geometry-oriented learning, combined with the semantic reasoning capabilities of vision-language models, aligns well with how coastlines are defined and evaluated in operational coastal monitoring.

---


### 93. [Advancing the State-of-the-Art in Empirical Privacy Auditing](https://arxiv.org/abs/2606.10481)

**<font color=#1a73e8>作者：</font>** Nicole Mitchell, Galen Andrew, Arun Ganesh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning of large language models (LLMs) can exhibit problematic memorization of individual training examples. Empirical privacy auditing (EPA) quantifies this risk by measuring realistic data leakage on membership inference (MI) or reconstruction attacks. A key challenge in EPA is designing ``canary'' examples that are mixed with the privacy-sensitive training data. We propose generating synthetic canaries via high-temperature sampling ($T \geq 0.8$) from LLMs, using prompts tailored to the privacy-sensitive training data. These canaries act as high-influence outliers, ensuring high identifiability and hence strong audits. Further, since the canaries are themselves non-private, they are inspectable and can be inserted with repetition without jeopardizing the privacy of the real data. An important use of models fine-tuned on privacy-sensitive data is the generation of synthetic data. This also comes with privacy risk. We introduce a powerful synthetic data audit based on fine-tuning an auxiliary model on the synthetic data. Auditing the auxiliary model for the original canaries then provides a strong estimate of the privacy leakage through the synthetic data. Finally, leveraging our strong auditing methodologies, we perform a systematic investigation into the interacting effects of model capacity and canary entropy on memorization.

---


### 94. [Stop Early, Spend Less: Hidden-State Probes as a Practical Recipe for Streaming Moderation of LLM Outputs](https://arxiv.org/abs/2606.10487)

**<font color=#1a73e8>作者：</font>** Huizhen Shu, Xuying Li, Piao Xue  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying large language models in user-facing systems requires efficient output safety filtering. Existing approaches typically rely on a separate moderation model applied after generation, which doubles inference cost and only detects violations after generation completes. We observe that the signal needed for moderation is already present in the model hidden states. Based on this, we train lightweight token-level probes that operate directly on internal activations, producing per-token safety scores that can be aggregated for both offline evaluation and online intervention. The probe reuses activations from the generator and requires no additional forward pass, enabling sub millisecond per-token safety checks inside the decoding loop. A probe applied to a single mid layer recovers most decisions of a strong guard model, acting as a low cost surrogate optimized for latency rather than accuracy. In streaming settings, it can halt or modify unsafe outputs before they are fully generated, replacing end of sequence moderation with continuous token level monitoring. Compared to post hoc and streaming guard models, our method achieves orders of magnitude lower compute overhead with minimal latency cost. We also provide a practical deployment recipe, including layer selection, aggregation strategy, probing frequency, and triggering thresholds. Finally, we show that the probe linear component corresponds to a direction in residual space, enabling both detection and activation steering at negligible cost.

---


### 95. [5% > 100%: Flatness Preference is All You Need for Multimodal Parameter-Efficient Fine-Tuning](https://arxiv.org/abs/2606.10488)

**<font color=#1a73e8>作者：</font>** Yifan Zhu, Can Lin, Hangjie Yuan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Parameter-Efficient Fine-Tuning (PEFT) methods provide a streamlined and efficient tool for adapting large models to domain-specific multimodal downstream tasks. Although these methods proved their tangible effects in practice, their principal aspects remain under-explored. Therefore we remain curious about the underlying generalization mechanisms in various PEFT methods and how they can be further enhanced. In this paper, we reveal the flatness preference widely present in various PEFTs, where a small fraction of sharp dimensions dominates the generalization of PEFT. This finding suggests an appealing possibility: we may be satisfied with a better generalization by merely attending to this small fraction of sharp dimensions instead of all of them. Furthermore, we propose Flatness Preference Optimization (FlatPO) to flatten these key sharpness dimensions, leading various PEFTs toward better generalization. Extensive experiments demonstrate the effectiveness of our findings and the proposed method. Code is available at this https URL.

---


### 96. [A complementary study on PlanGPT: Evaluation with defined Performance Metrics and comparison with a planner](https://arxiv.org/abs/2606.10489)

**<font color=#1a73e8>作者：</font>** Youssef Abdelkader, Humbert Fiorino, Damien Pellier  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated Planning is a subfield of Artificial Intelligence (AI) where the main objective is generating a sequence of actions, known as a plan, that helps us reach a goal state from an initial state. A planning problem is defined by a set of objects, an initial state and a desired goal state. The objective is to compute a plan that'll lead us from the inital state to the goal state. Programs that generate plans are called planners.
In this paper, we did a complementary study to the state-of-the-art LLM called PlanGPT which was released last year. We redid some experiments to verify whether planning with LLMs is \textbf{pertinent} and \textbf{worthwhile}. We also check whether the results obtained in the official PlanGPT paper for plan coverage were correct, and we also performed a more comprehensive study on PlanGPT's performance: in our paper PlanGPT's performance was evaluated using two metrics: Plan Cost and Plan Generation Time. The results of planGPT were compared to those produced by a traditional planner for the same plans and same metrics. We discovered that PlanGPT is no better than a Greedy search strategy.

---


### 97. [MoE Enhanced Federated Learning for Spatiotemporal Prediction](https://arxiv.org/abs/2606.10499)

**<font color=#1a73e8>作者：</font>** Zhehao Dai, Xiao Han, Zhaolin Deng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traffic prediction is fundamental to intelligent transportation systems and urban computing, yet many cities continue to suffer from traffic data scarcity due to limited sensor deployment and uneven urban development. Cross-city knowledge transfer has thus attracted increasing attention, enabling data-rich cities to assist data-scarce ones. However, centralized approaches raise privacy concerns, while existing federated methods struggle with pronounced spatiotemporal heterogeneity across cities. To address these challenges, we propose MoE-FedTP, a personalized federated cross-city spatiotemporal prediction framework based on lightweight Mixture-of-Experts (MoE) networks. MoE-FedTP first employs spatiotemporal neural networks to extract features from both source and target cities, then introduces a set of expert networks derived from different source cities through partial parameter sharing. A gating mechanism dynamically fuses the experts to capture diverse traffic dynamics, achieving fine-grained modeling of urban heterogeneity while preserving privacy. Experiments on four real-world traffic datasets show that MoE-FedTP consistently outperforms state-of-the-art cross-city and federated learning baselines, demonstrating its effectiveness in enhancing prediction accuracy for data-scarce cities.

---


### 98. [HIPIF: Hierarchical Planning and Information Folding for Long-Horizon LLM Agent Learning](https://arxiv.org/abs/2606.10507)

**<font color=#1a73e8>作者：</font>** Juncheng Diao, Zhicong Lu, Peiguang Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) have demonstrated strong capabilities as autonomous agents across a wide range of tasks, their performance often degrades in multi-turn long-horizon agentic tasks. Existing methods have made progress through fine-grained credit assignment to alleviate long-horizon sparse rewards and hierarchical reinforcement learning to decompose tasks and reduce long-term dependency. However, these methods still do not directly address long-context interference, in which continuously growing histories weaken the agent's ability to track the global task state and impair subsequent reasoning and decision-making. Inspired by the way humans handle complex tasks through subgoal decomposition and completed progress summarization, we propose Hierarchical Planning and Information Folding (HIPIF) for long-horizon LLM agent learning. HIPIF trains the agent end-to-end to organize long-horizon execution around explicit subgoals while folding completed subgoal histories to reduce long-context interference. Furthermore, to stabilize subgoal-based planning and execution, HIPIF combines hierarchical reflection and subgoal-oriented process rewards to guide subgoal generation, transition, and execution, without relying on costly auxiliary models or task-specific expert trajectories. Extensive experiments on three publicly available agentic benchmarks demonstrate the validity of our method.

---


### 99. [UniSVQ: 2-bit Unified Scalar-Vector Quantization](https://arxiv.org/abs/2606.10520)

**<font color=#1a73e8>作者：</font>** Haoyu Wang, Haiyan Zhao, Xingyu Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-training quantization at the 2-bit level enables low-cost deployment and inference acceleration for large language models (LLMs). Scalar quantization (SQ) and vector quantization (VQ) are two primary quantization methods, however, the former suffers from significant performance degradation, and the latter incurs computational and storage overhead. We propose UniSVQ, a unified 2-bit quantization framework that bridges scalar and vector quantization by parameterizing codewords as an affine transform of integer lattices. This structure preserves compatibility with optimized integer kernels while retaining much of VQ's flexibility. We further introduce a data-driven block-wise fine-tuning strategy to directly minimize quantization reconstruction error. Extensive experiments across multiple LLM families and zero-shot benchmarks demonstrate that UniSVQ consistently outperforms state-of-the-art SQ methods and achieves performance comparable to advanced VQ methods, while providing higher inference throughput.

---


### 100. [LC-QAT: Data-Efficient 2-Bit QAT for LLMs via Linear-Constrained Vector Quantization](https://arxiv.org/abs/2606.10531)

**<font color=#1a73e8>作者：</font>** Haoyu Wang, Xingyu Yu, Haiyan Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Quantization-aware training (QAT) is essential for extremely low-bit large language models (LLMs). Current QAT methods are mainly based on scalar quantization (SQ), which enables efficient optimization but suffers from severe performance degradation at 2-bit precision. On the other hand, vector quantization (VQ) provides substantially higher representational capacity, but its discrete codebook lookup prevents end-to-end training. We propose LC-QAT, a 2-bit weight-only VQ-QAT framework that represents quantized weights via a learned affine mapping over discrete vectors, which yields a high-quality PTQ initialization and enables fully differentiable end-to-end optimization without explicit codebook lookup in the training forward pass. This strong post-training initialization makes LC-QAT highly data-efficient. Experiments across diverse LLMs demonstrate that LC-QAT consistently outperforms state-of-the-art QAT methods while using only 0.1%--10% of the training data. Our results establish LC-QAT as a practical and scalable solution for extreme low-bit model deployment.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-188](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
