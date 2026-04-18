# 🧠 大模型相关研究 | 2026年04月18日

> 本类共 **143** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-143](./part-03.md)

---

### 51. [Evo-MedAgent: Beyond One-Shot Diagnosis with Agents That Remember, Reflect, and Improve](https://arxiv.org/abs/2604.14475)

**<font color=#1a73e8>作者：</font>** Weixiang Shen, Bailiang Jian, Jun Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-augmented large language model (LLM) agents can orchestrate specialist classifiers, segmentation models, and visual question-answering modules to interpret chest X-rays. However, these agents still solve each case in isolation: they fail to accumulate experience across cases, correct recurrent reasoning mistakes, or adapt their tool-use behavior without expensive reinforcement learning. While a radiologist naturally improves with every case, current agents remain static. In this work, we propose Evo-MedAgent, a self-evolving memory module that equips a medical agent with the capacity for inter-case learning at test time. Our memory comprises three complementary stores: (1)~\emph{Retrospective Clinical Episodes} that retrieve problem-solving experiences from similar past cases, (2)~an \emph{Adaptive Procedural Heuristics} bank curating priority-tagged diagnostic rules that evolves via reflection, much like a physician refining their internal criteria, and (3)~a \emph{Tool Reliability Controller} that tracks per-tool trustworthiness. On ChestAgentBench, Evo-MedAgent raises multiple-choice question (MCQ) accuracy from 0.68 to 0.79 on GPT-5-mini, and from 0.76 to 0.87 on Gemini-3 Flash. With a strong base model, evolving memory improves performance more effectively than orchestrating external tools on qualitative diagnostic tasks. Because Evo-MedAgent requires no training, its per-case overhead is bounded by one additional retrieval pass and a single reflection call, making it deployable on top of any frozen model.

---


### 52. [Pushing the Limits of On-Device Streaming ASR: A Compact, High-Accuracy English Model for Low-Latency Inference](https://arxiv.org/abs/2604.14493)

**<font color=#1a73e8>作者：</font>** Nenad Banfic, David Fan, Kunal Vaishnavi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deploying high-quality automatic speech recognition (ASR) on edge devices requires models that jointly optimize accuracy, latency, and memory footprint while operating entirely on CPU without GPU acceleration. We conduct a systematic empirical study of state-of-the-art ASR architectures, encompassing encoder-decoder, transducer, and LLM-based paradigms, evaluated across batch, chunked, and streaming inference modes. Through a comprehensive benchmark of over 50 configurations spanning OpenAI Whisper, NVIDIA Nemotron, Parakeet TDT, Canary, Conformer Transducer, and Qwen3-ASR, we identify NVIDIA's Nemotron Speech Streaming as the strongest candidate for real-time English streaming on resource-constrained hardware. We then re-implement the complete streaming inference pipeline in ONNX Runtime and conduct a controlled evaluation of multiple post-training quantization strategies, including importance-weighted k-quant, mixed-precision schemes, and round-to-nearest quantization, combined with graph-level operator fusion. These optimizations reduce the model from 2.47 GB to as little as 0.67 GB while maintaining word error rate (WER) within 1% absolute of the full-precision PyTorch baseline. Our recommended configuration, the int4 k-quant variant, achieves 8.20% average streaming WER across eight standard benchmarks, running comfortably faster than real-time on CPU with 0.56 s algorithmic latency, establishing a new quality-efficiency Pareto point for on-device streaming ASR.

---


### 53. [Geometric Metrics for MoE Specialization: From Fisher Information to Early Failure Detection](https://arxiv.org/abs/2604.14500)

**<font color=#1a73e8>作者：</font>** Dongxin Guo, Jikun Wu, Siu Ming Yiu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Expert specialization is fundamental to Mixture-of-Experts (MoE) model success, yet existing metrics (cosine similarity, routing entropy) lack theoretical grounding and yield inconsistent conclusions under reparameterization. We present an information-geometric framework providing the first rigorous characterization of MoE specialization dynamics. Our key insight is that expert routing distributions evolve on the probability simplex equipped with the Fisher information metric, enabling formal analysis via Riemannian geometry. We prove that standard heuristic metrics violate parameterization invariance (Theorem 1), establish that specialization corresponds to geodesic flow with quantified approximation bounds (Theorem 2), and derive a failure predictor with theoretical threshold justification (Theorem 3). The framework introduces two principled metrics: Fisher Specialization Index (FSI) achieving r=0.91+/-0.02 correlation with downstream performance, and Fisher Heterogeneity Score (FHS) predicting training failure at 10% completion with AUC=0.89+/-0.03 -- outperforming validation-loss-based early stopping by 23% while requiring 40x fewer compute cycles. We validate intervention protocols achieving 87% recovery rate when FHS>1 is detected. Comprehensive experiments across language modeling (WikiText-103, C4), vision MoE (ImageNet), and scaling studies (8-64 experts, 125M-2.7B parameters) validate our theoretical predictions.

---


### 54. [Chain of Modality: From Static Fusion to Dynamic Orchestration in Omni-MLLMs](https://arxiv.org/abs/2604.14520)

**<font color=#1a73e8>作者：</font>** Ziyang Luo, Nian Liu, Junwei Han  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omni-modal Large Language Models (Omni-MLLMs) promise a unified integration of diverse sensory streams. However, recent evaluations reveal a critical performance paradox: unimodal baselines frequently outperform joint multimodal inference. We trace this perceptual fragility to the static fusion topologies universally employed by current models, identifying two structural pathologies: positional bias in sequential inputs and alignment traps in interleaved formats, which systematically distort attention regardless of task semantics. To resolve this functional rigidity, we propose Chain of Modality (CoM), an agentic framework that transitions multimodal fusion from passive concatenation to dynamic orchestration. CoM adaptively orchestrates input topologies, switching among parallel, sequential, and interleaved pathways to neutralize structural biases. Furthermore, CoM bifurcates cognitive execution into two task-aligned pathways: a streamlined ``Direct-Decide'' path for direct perception and a structured ``Reason-Decide'' path for analytical auditing. Operating in either a training-free or a data-efficient SFT setting, CoM achieves robust and consistent generalization across diverse benchmarks.

---


### 55. [Quantifying Cross-Query Contradictions in Multi-Query LLM Reasoning](https://arxiv.org/abs/2604.14525)

**<font color=#1a73e8>作者：</font>** Rohit Kumar Salla, Ramya Manasa Amancherla, Manoj Saravanan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models frequently produce mutually inconsistent answers when reasoning over multiple related queries. We study case-file logical consistency: maintaining a globally satisfiable belief state across interdependent queries. We introduce a benchmark of 390 multi-query reasoning instances with entailment/contradiction/unknown labels and propose set-level metrics including Case Satisfiability Rate, Contradiction Density and Revision Cost. Our solver-augmented approach extracts commitments, verifies global satisfiability and performs counterexample-guided repair. Across four reasoning domains, our method substantially reduces cross-query contradictions (SetCons: 0.56 to 0.94) while preserving per-query accuracy, demonstrating that global coherence is critical for robust multi-query reasoning.

---


### 56. [Dissecting Failure Dynamics in Large Language Model Reasoning](https://arxiv.org/abs/2604.14528)

**<font color=#1a73e8>作者：</font>** Wei Zhu, Jian Zhang, Lixing Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) achieve strong performance through extended inference-time deliberation, yet how their reasoning failures arise remains poorly understood. By analyzing model-generated reasoning trajectories, we find that errors are not uniformly distributed but often originate from a small number of early transition points, after which reasoning remains locally coherent but globally incorrect. These transitions coincide with localized spikes in token-level entropy, and alternative continuations from the same intermediate state can still lead to correct solutions. Based on these observations, we introduce GUARD, a targeted inference-time framework that probes and redirects critical transitions using uncertainty signals. Empirical evaluations across multiple benchmarks confirm that interventions guided by these failure dynamics lead to more reliable reasoning outcomes. Our findings highlight the importance of understanding when and how reasoning first deviates, complementing existing approaches that focus on scaling inference-time computation.

---


### 57. [TRACER: Trace-Based Adaptive Cost-Efficient Routing for LLM Classification](https://arxiv.org/abs/2604.14531)

**<font color=#1a73e8>作者：</font>** Adam Rida  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Every call to an LLM classification endpoint produces a labeled input-output pair already retained in production logs. These pairs constitute a free, growing training set: a lightweight surrogate trained on them can absorb a significant portion of future traffic at near-zero marginal inference cost. The open questions are when the surrogate is reliable enough to deploy, what it handles versus defers, and how that boundary evolves as data accumulates.
We introduce TRACER (Trace-based Adaptive Cost-Efficient Routing), an open-source system that trains ML surrogates on an LLM's own production traces and governs deployment through a parity gate: the surrogate is activated only when its agreement with the LLM exceeds a user-specified threshold {\alpha}. To make the routing boundary transparent, TRACER generates interpretability artifacts describing which input regions the surrogate handles, where it plateaus, and why it defers.
On a 77-class intent benchmark with a Sonnet 4.6 teacher, TRACER achieves 83-100% surrogate coverage depending on the quality target {\alpha}; on a 150-class benchmark, the surrogate fully replaces the teacher. On a natural language inference task, the parity gate correctly refuses deployment because the embedding representation cannot support reliable separation. The system is available as open-source software.

---


### 58. [Predicting Post-Traumatic Epilepsy from Clinical Records using Large Language Model Embeddings](https://arxiv.org/abs/2604.14547)

**<font color=#1a73e8>作者：</font>** Wenhui Cui, Nicholas Swingle, Anand A. Joshi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Objective: Post-traumatic epilepsy (PTE) is a debilitating neurological disorder that develops after traumatic brain injury (TBI). Early prediction of PTE remains challenging due to heterogeneous clinical data, limited positive cases, and reliance on resource-intensive neuroimaging data. We investigate whether routinely collected acute clinical records alone can support early PTE prediction using language model-based approaches. Methods: Using a curated subset of the TRACK-TBI cohort, we developed an automated PTE prediction framework that implements pretrained large language models (LLMs) as fixed feature extractors to encode clinical records. Tabular features, LLM-generated embeddings, and hybrid feature representations were evaluated using gradient-boosted tree classifiers under stratified cross-validation. Results: LLM embeddings achieved performance improvements by capturing contextual clinical information compared to using tabular features alone. The best performance was achieved by a modality-aware feature fusion strategy combining tabular features and LLM embeddings, achieving an AUC-ROC of 0.892 and AUPRC of 0.798. Acute post-traumatic seizures, injury severity, neurosurgical intervention, and ICU stay are key contributors to the predictive performance. Significance: These findings demonstrate that routine acute clinical records contain information suitable for early PTE risk prediction using LLM embeddings in conjunction with gradient-boosted tree classifiers. This approach represents a promising complement to imaging-based prediction.

---


### 59. [Generative Augmented Inference](https://arxiv.org/abs/2604.14575)

**<font color=#1a73e8>作者：</font>** Cheng Lu, Mengxin Wang, Dennis J. Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data-driven operations management often relies on parameters estimated from costly human-generated labels. Recent advances in large language models (LLMs) and other AI systems offer inexpensive auxiliary data, but introduce a new challenge: AI outputs are not direct observations of the target outcomes, but could involve high-dimensional representations with complex and unknown relationships to human labels. Conventional methods leverage AI predictions as direct proxies for true labels, which can be inefficient or unreliable when this relationship is weak or misspecified. We propose Generative Augmented Inference (GAI), a general framework that incorporates AI-generated outputs as informative features for estimating models of human-labeled outcomes. GAI uses an orthogonal moment construction that enables consistent estimation and valid inference with flexible, nonparametric relationship between LLM-generated outputs and human labels. We establish asymptotic normality and show a "safe default" property: relative to human-data-only estimators, GAI weakly improves estimation efficiency under arbitrary auxiliary signals and yields strict gains whenever the auxiliary information is predictive. Empirically, GAI outperforms benchmarks across diverse settings. In conjoint analysis with weak auxiliary signals, GAI reduces estimation error by about 50% and lowers human labeling requirements by over 75%. In retail pricing, where all methods access the same auxiliary inputs, GAI consistently outperforms alternative estimators, highlighting the value of its construction rather than differences in information. In health insurance choice, it cuts labeling requirements by over 90% while maintaining decision accuracy. Across applications, GAI improves confidence interval coverage without inflating width. Overall, GAI provides a principled and scalable approach to integrating AI-generated information.

---


### 60. [Enhancing Mental Health Counseling Support in Bangladesh using Culturally-Grounded Knowledge](https://arxiv.org/abs/2604.14576)

**<font color=#1a73e8>作者：</font>** Md Arid Hasan, Azhagu Meena SP, Aditya Khan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) show promise in generating supportive responses for mental health and counseling applications. However, their responses often lack cultural sensitivity, contextual grounding, and clinically appropriate guidance. This work addresses the gap of how to systematically incorporate domain-specific, clinically validated knowledge into LLMs to improve counseling quality. We utilize and compare two approaches, retrieval-augmented generation (RAG) and a knowledge graph (KG)-based method, designed to support para-counselors. Our KG is constructed manually and clinically validated, capturing causal relationships between stressors, interventions, and outcomes, with contributions from multidisciplinary people. We evaluated multiple LLMs in both settings using BERTScore F1 and SBERT cosine similarity, as well as human evaluation across five metrics, which is designed to directly measure the effectiveness of counseling beyond similarity at the surface level. The results show that KG-based approaches consistently improve contextual relevance, clinical appropriateness, and practical usability compared to RAG alone, demonstrating that structured, expert-validated knowledge plays a critical role in addressing LLMs limitations in counseling tasks.

---


### 61. [MapSR: Prompt-Driven Land Cover Map Super-Resolution via Vision Foundation Models](https://arxiv.org/abs/2604.14582)

**<font color=#1a73e8>作者：</font>** Ruiqi Wang, Qi Yu, Jie Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution (HR) land-cover mapping is often constrained by the high cost of dense HR annotations. We revisit this problem from the perspective of map super-resolution, which enhances coarse low-resolution (LR) land-cover products into HR maps at the resolution of the input imagery. Existing weakly supervised methods can leverage LR labels, but they typically use them to retrain dense predictors with substantial computational cost. We propose MapSR, a prompt-driven framework that decouples supervision from model training. MapSR uses LR labels once to extract class prompts from frozen vision foundation model features through a lightweight linear probe, after which HR mapping proceeds via training-free metric inference and graph-based prediction refinement. Specifically, class prompts are estimated by aggregating high-confidence HR features identified by the linear probe, and HR predictions are obtained by cosine-similarity matching followed by graph-based propagation for spatial refinement. Experiments on the Chesapeake Bay dataset show that MapSR achieves 59.64% mIoU without any HR labels, remaining competitive with the strongest weakly supervised baseline and surpassing a fully supervised baseline. Notably, MapSR reduces trainable parameters by four orders of magnitude and shortens training time from hours to minutes, enabling scalable HR mapping under limited annotation and compute budgets. The code is available at this https URL.

---


### 62. [From Risk to Rescue: An Agentic Survival Analysis Framework for Liquidation Prevention](https://arxiv.org/abs/2604.14583)

**<font color=#1a73e8>作者：</font>** Fernando Spadea, Oshani Seneviratne  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decentralized Finance (DeFi) lending protocols like Aave v3 rely on over-collateralization to secure loans, yet users frequently face liquidation due to volatile market conditions. Existing risk management tools utilize static health-factor thresholds, which are reactive and fail to distinguish between administrative "dust" cleanup and genuine insolvency. In this work, we propose an autonomous agent that leverages time-to-event (survival) analysis and moves beyond prediction to execution. Unlike passive risk signals, this agent perceives risk, simulates counterfactual futures, and executes protocol-faithful interventions to proactively prevent liquidations. We introduce a return period metric derived from a numerically stable XGBoost Cox proportional hazards model to normalize risk across transaction types, coupled with a volatility-adjusted trend score to filter transient market noise. To select optimal interventions, we implement a counterfactual optimization loop that simulates potential user actions to find the minimum capital required to mitigate risk. We validate our approach using a high-fidelity, protocol-faithful Aave v3 simulator on a cohort of 4,882 high-risk user profiles. The results demonstrate the agent's ability to prevent liquidations in imminent-risk scenarios where static rules fail, effectively "saving the unsavable" while maintaining a zero worsening rate, providing a critical safety guarantee often missing in autonomous financial agents. Furthermore, the system successfully differentiates between actionable financial risks and negligible dust events, optimizing capital efficiency where static rules fail.

---


### 63. [Mechanistic Decoding of Cognitive Constructs in LLMs](https://arxiv.org/abs/2604.14593)

**<font color=#1a73e8>作者：</font>** Yitong Shou, Manhao Guan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) demonstrate increasingly sophisticated affective capabilities, the internal mechanisms by which they process complex emotions remain unclear. Existing interpretability approaches often treat models as black boxes or focus on coarse-grained basic emotions, leaving the cognitive structure of more complex affective states underexplored. To bridge this gap, we propose a Cognitive Reverse-Engineering framework based on Representation Engineering (RepE) to analyze social-comparison jealousy. By combining appraisal theory with subspace orthogonalization, regression-based weighting, and bidirectional causal steering, we isolate and quantify two psychological antecedents of jealousy, Superiority of Comparison Person and Domain Self-Definitional Relevance, and examine their causal effects on model judgments. Experiments on eight LLMs from the Llama, Qwen, and Gemma families suggest that models natively encode jealousy as a structured linear combination of these constituent factors. Their internal representations are broadly consistent with the human psychological construct, treating Superiority as the foundational trigger and Relevance as the ultimate intensity multiplier. Our framework also demonstrates that toxic emotional states can be mechanically detected and surgically suppressed, suggesting a possible route toward representational monitoring and intervention for AI safety in multi-agent environments.

---


### 64. [CausalDetox: Causal Head Selection and Intervention for Language Model Detoxification](https://arxiv.org/abs/2604.14602)

**<font color=#1a73e8>作者：</font>** Yian Wang, Yuen Chen, Agam Goyal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) frequently generate toxic content, posing significant risks for safe deployment. Current mitigation strategies often degrade generation quality or require costly human annotation. We propose CAUSALDETOX, a framework that identifies and intervenes on the specific attention heads causally responsible for toxic generation. Using the Probability of Necessity and Sufficiency (PNS), we isolate a minimal set of heads that are necessary and sufficient for toxicity. We utilize these components via two complementary strategies: (1) Local Inference-Time Intervention, which constructs dynamic, input-specific steering vectors for context-aware detoxification, and (2) PNS-Guided Fine-Tuning, which permanently unlearns toxic representations. We also introduce PARATOX, a novel benchmark of aligned toxic/non-toxic sentence pairs enabling controlled counterfactual evaluation. Experiments on ToxiGen, ImplicitHate, and ParaDetox show that CAUSALDETOX achieves up to 5.34% greater toxicity reduction compared to baselines while preserving linguistic fluency, and offers a 7x speedup in head selection.

---


### 65. [El Agente Forjador: Task-Driven Agent Generation for Quantum Simulation](https://arxiv.org/abs/2604.14609)

**<font color=#1a73e8>作者：</font>** Zijian Zhang, Aiwei Yin, Amaan Baweja 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI for science promises to accelerate the discovery process. The advent of large language models (LLMs) and agentic workflows enables the expediting of a growing range of scientific tasks. However, most of the current generation of agentic systems depend on static, hand-curated toolsets that hinder adaptation to new domains and evolving libraries. We present El Agente Forjador, a multi-agent framework in which universal coding agents autonomously forge, validate, and reuse computational tools through a four-stage workflow of tool analysis, tool generation, task execution, and iterative solution evaluation. Evaluated across 24 tasks spanning quantum chemistry and quantum dynamics on five coding agent setups, we compare three operating modes: zero-shot generation of tools per task, reuse of a curriculum-built toolset, and direct problem-solving with the coding agents as the baseline. We find that our tool generation and reuse framework consistently improves accuracy over the baseline. We also show that reusing a toolset built by a stronger coding agent can reduce API cost and substantially raises the solution quality for weaker coding agents. Case studies further demonstrate that tools forged for different domains can be combined to solve hybrid tasks. Taken together, these results show that LLM-based agents can use their scientific knowledge and coding capabilities to autonomously build reusable scientific tools, pointing toward a paradigm in which agent capabilities are defined by the tasks they are designed to solve rather than by explicitly engineered implementations.

---


### 66. [Retrieve, Then Classify: Corpus-Grounded Automation of Clinical Value Set Authoring](https://arxiv.org/abs/2604.14616)

**<font color=#1a73e8>作者：</font>** Sumit Mukherjee, Juan Shu, Nairwita Mazumder 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical value set authoring -- the task of identifying all codes in a standardized vocabulary that define a clinical concept -- is a recurring bottleneck in clinical quality measurement and phenotyping. A natural approach is to prompt a large language model (LLM) to generate the required codes directly, but structured clinical vocabularies are large, version-controlled, and not reliably memorized during pretraining. We propose Retrieval-Augmented Set Completion (RASC): retrieve the $K$ most similar existing value sets from a curated corpus to form a candidate pool, then apply a classifier to each candidate code. Theoretically, retrieve-and-select can reduce statistical complexity by shrinking the effective output space from the full vocabulary to a much smaller retrieved candidate pool. We demonstrate the utility of RASC on 11,803 publicly available VSAC value sets, constructing the first large-scale benchmark for this task. A cross-encoder fine-tuned on SAPBert achieves AUROC~0.852 and value-set-level F1~0.298, outperforming a simpler three-layer Multilayer Perceptron (AUROC~0.799, F1~0.250) and both reduce the number of irrelevant candidates per true positive from 12.3 (retrieval-only) to approximately 3.2 and 4.4 respectively. Zero-shot GPT-4o achieves value-set-level F1~0.105, with 48.6\% of returned codes absent from VSAC entirely. This performance gap widens with increasing value set size, consistent with RASC's theoretical advantage. We observe similar performance gains across two other classifier model types, namely a cross-encoder initialized from pre-trained SAPBert and a LightGBM model, demonstrating that RASC's benefits extend beyond a single model class. The code to download and create the benchmark dataset, as well as the model training code is available at: \href{this https URL}{this https URL}.

---


### 67. [ELMoE-3D: Leveraging Intrinsic Elasticity of MoE for Hybrid-Bonding-Enabled Self-Speculative Decoding in On-Premises Serving](https://arxiv.org/abs/2604.14626)

**<font color=#1a73e8>作者：</font>** Yuseon Choi, Jingu Lee, Jungjun Oh 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models have become the dominant architecture for large-scale language models, yet on-premises serving remains fundamentally memory-bound as batching turns sparse per-token compute into dense memory activation. Memory-centric architectures (PIM, NMP) improve bandwidth but leave compute underutilized under MoE's low arithmetic intensity at high batch sizes. Speculative decoding (SD) trades idle compute for fewer target invocations, yet verification must load experts even for rejected tokens, severely limiting its benefit in MoE especially at low batch sizes. We propose ELMoE-3D, a hybrid-bonding (HB)-based HW-SW co-designed framework that unifies cache-based acceleration and speculative decoding to offer overall speedup across batch sizes. We identify two intrinsic elasticity axes of MoE-expert and bit-and jointly scale them to construct Elastic Self-Speculative Decoding (Elastic-SD), which serves as both an expert cache and a strongly aligned self-draft model accelerated by high HB bandwidth. Our LSB-augmented bit-sliced architecture exploits inherent redundancy in bit-slice representations to natively support bit-nested execution. On our 3D-stacked hardware, ELMoE-3D achieves an average $6.6\times$ speedup and $4.4\times$ energy efficiency gain over naive MoE serving on xPU across batch sizes 1-16, and delivers $2.2\times$ speedup and $1.4\times$ energy efficiency gain over the best-performing prior accelerator baseline.

---


### 68. [Switch-KD: Visual-Switch Knowledge Distillation for Vision-Language Models](https://arxiv.org/abs/2604.14629)

**<font color=#1a73e8>作者：</font>** Haoyi Sun, Xiaoxiao Wang, Ning Mao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have shown remarkable capabilities in joint vision-language understanding, but their large scale poses significant challenges for deployment in resource-constrained scenarios. Knowledge Distillation (KD) offers a viable way to improve model capabilities without increasing model size or data requirements, making deployment more efficient. However, applying KD to VLMs is challenged by modality-specific supervision: although multimodal knowledge in VLMs is fused within the language space, current methods supervise each modality separately without explicitly addressing multimodal alignment, leading to inconsistent multimodal knowledge transfer. To address this, we propose Switch-KD, a visual-switch distillation framework that unifies vision-language knowledge transfer within a shared text-probability space. Switch-KD comprises two key components: (1) Visual-Switch Distillation, which switches the student's visual outputs into the teacher's language pathway to construct cross-modal probabilistic references for implicit visual knowledge transfer; and (2) Dynamic Bi-directional Logits Difference (DBiLD) loss, which adaptively aligns informative probability regions while preserving the distributional structures of teacher and student through bidirectional supervision. Guided by Switch-KD, a 0.5B TinyLLaVA effectively distills rich multimodal knowledge from its 3B teacher, yielding an average improvement of 3.6 points across 10 multimodal benchmarks without any architectural modification.

---


### 69. [StoryCoder: Narrative Reformulation for Structured Reasoning in LLM Code Generation](https://arxiv.org/abs/2604.14631)

**<font color=#1a73e8>作者：</font>** Geonhui Jang, Dongyoon Han, YoungJoon Yoo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Effective code generation requires both model capability and a problem representation that carefully structures how models reason and plan. Existing approaches augment reasoning steps or inject specific structure into how models think, but leave scattered problem conditions unchanged. Inspired by the way humans organize fragmented information into coherent explanations, we propose StoryCoder, a narrative reformulation framework that transforms code generation questions into coherent natural language narratives, providing richer contextual structure than simple rephrasings. Each narrative consists of three components: a task overview, constraints, and example test cases, guided by the selected algorithm and genre. Experiments across 11 models on HumanEval, LiveCodeBench, and CodeForces demonstrate consistent improvements, with an average gain of 18.7% in zero-shot pass@10. Beyond accuracy, our analyses reveal that narrative reformulation guides models toward correct algorithmic strategies, reduces implementation errors, and induces a more modular code structure. The analyses further show that these benefits depend on narrative coherence and genre alignment, suggesting that structured problem representation is important for code generation regardless of model scale or architecture. Our code is available at this https URL.

---


### 70. [Fact4ac at the Financial Misinformation Detection Challenge Task: Reference-Free Financial Misinformation Detection via Fine-Tuning and Few-Shot Prompting of Large Language Models](https://arxiv.org/abs/2604.14640)

**<font color=#1a73e8>作者：</font>** Cuong Hoang, Le-Minh Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The proliferation of financial misinformation poses a severe threat to market stability and investor trust, misleading market behavior and creating critical information asymmetry. Detecting such misleading narratives is inherently challenging, particularly in real-world scenarios where external evidence or supplementary references for cross-verification are strictly unavailable. This paper presents our winning methodology for the "Reference-Free Financial Misinformation Detection" shared task. Built upon the recently proposed RFC-BENCH framework (Jiang et al. 2026), this task challenges models to determine the veracity of financial claims by relying solely on internal semantic understanding and contextual consistency, rather than external fact-checking. To address this formidable evaluation setup, we propose a comprehensive framework that capitalizes on the reasoning capabilities of state-of-the-art Large Language Models (LLMs). Our approach systematically integrates in-context learning, specifically zero-shot and few-shot prompting strategies, with Parameter-Efficient Fine-Tuning (PEFT) via Low-Rank Adaptation (LoRA) to optimally align the models with the subtle linguistic cues of financial manipulation. Our proposed system demonstrated superior efficacy, successfully securing the first-place ranking on both official leaderboards. Specifically, we achieved an accuracy of 95.4% on the public test set and 96.3% on the private test set, highlighting the robustness of our method and contributing to the acceleration of context-aware misinformation detection in financial Natural Language Processing. Our models (14B and 32B) are available at this https URL.

---


### 71. [Learning to Draw ASCII Improves Spatial Reasoning in Language Models](https://arxiv.org/abs/2604.14641)

**<font color=#1a73e8>作者：</font>** Shiyuan Huang, Li Liu, Jincheng He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When faced with complex spatial problems, humans naturally sketch layouts to organize their thinking, and the act of drawing further sharpens their understanding. In this work, we ask whether a similar principle holds for Large Language Models (LLMs): can learning to construct explicit visual layouts from spatial descriptions instill genuine spatial understanding? We introduce Text2Space, a dataset that pairs natural language descriptions with ground-truth ASCII grid layouts and spatial QA pairs, enabling us to separate failures in constructing spatial representations from failures in reasoning over them. We adopt ASCII because it is human-readable, operates entirely within the token space of language models, and encodes spatial relations in a structurally verifiable form. Our evaluation reveals a pronounced "Read-Write Asymmetry": LLMs interpret ASCII representations effectively but struggle to produce them from text, and these construction errors propagate to incorrect answers downstream. To address this limitation, we train models on layout construction (Text$\rightarrow$ASCII) and find that it significantly improves spatial reasoning from text alone, even without producing any ASCII at inference time. Combining construction with comprehension training further amplifies these gains. Crucially, these improvements transfer to three external spatial reasoning benchmarks, demonstrating that, much as sketching sharpens human spatial thinking, learning to construct explicit layouts instills spatial understanding that generalizes beyond the training format.

---


### 72. [CURaTE: Continual Unlearning in Real Time with Ensured Preservation of LLM Knowledge](https://arxiv.org/abs/2604.14644)

**<font color=#1a73e8>作者：</font>** Seyun Bae, Seokhan Lee, Eunho Yang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The inability to filter out in advance all potentially problematic data from the pre-training of large language models has given rise to the need for methods for unlearning specific pieces of knowledge after training. Existing techniques overlook the need for continuous and immediate action, causing them to suffer from degraded utility as updates accumulate and protracted exposure of sensitive information. To address these issues, we propose Continual Unlearning in Real Time with Ensured Preservation of LLM Knowledge (CURaTE). Our method begins by training a sentence embedding model on a dataset designed to enable the formation of sharp decision boundaries for determining whether a given input prompt corresponds to any stored forget requests. The similarity of a given input to the forget requests is then used to determine whether to answer or return a refusal response. We show that even with such a simple approach, not only does CURaTE achieve more effective forgetting than existing methods, but by avoiding modification of the language model parameters, it also maintains near perfect knowledge preservation over any number of updates and is the only method capable of continual unlearning in real-time.

---


### 73. [Targeted Exploration via Unified Entropy Control for Reinforcement Learning](https://arxiv.org/abs/2604.14646)

**<font color=#1a73e8>作者：</font>** Chen Wang, Lai Wei, Yanzhi Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in reinforcement learning (RL) have improved the reasoning capabilities of large language models (LLMs) and vision-language models (VLMs). However, the widely used Group Relative Policy Optimization (GRPO) consistently suffers from entropy collapse, causing the policy to converge prematurely and lose diversity. Existing exploration methods introduce additional bias or variance during exploration, making it difficult to maintain optimization stability. We propose Unified Entropy Control for Reinforcement Learning (UEC-RL), a framework that provides targeted mechanisms for exploration and stabilization. UEC-RL activates more exploration on difficult prompts to search for potential and valuable reasoning trajectories. In parallel, a stabilizer prevents entropy from growing uncontrollably, thereby keeping training stable as the model consolidates reliable behaviors. Together, these components expand the search space when needed while maintaining robust optimization throughout training. Experiments on both LLM and VLM reasoning tasks show consistent gains over RL baselines on both Pass@1 and Pass@$k$. On Geometry3K, UEC-RL achieves a 37.9\% relative improvement over GRPO, indicating that it sustains effective exploration without compromising convergence and underscoring UEC-RL as a key for scaling RL-based reasoning in large models. Our code is available at this https URL.

---


### 74. [CURA: Clinical Uncertainty Risk Alignment for Language Model-Based Risk Prediction](https://arxiv.org/abs/2604.14651)

**<font color=#1a73e8>作者：</font>** Sizhe Wang, Ziqi Xu, Claire Najjuuko 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical language models (LMs) are increasingly applied to support clinical risk prediction from free-text notes, yet their uncertainty estimates often remain poorly calibrated and clinically unreliable. In this work, we propose Clinical Uncertainty Risk Alignment (CURA), a framework that aligns clinical LM-based risk estimates and uncertainty with both individual error likelihoods and cohort-level ambiguities. CURA first fine-tunes domain-specific clinical LMs to obtain task-adapted patient embeddings, and then performs uncertainty fine-tuning of a multi-head classifier using a bi-level uncertainty objective. Specifically, an individual-level calibration term aligns predictive uncertainty with each patient's likelihood of error, while a cohort-aware regularizer pulls risk estimates toward event rates in their local neighborhoods in the embedding space and places extra weight on ambiguous cohorts near the decision boundary. We further show that this cohort-aware term can be interpreted as a cross-entropy loss with neighborhood-informed soft labels, providing a label-smoothing view of our method. Extensive experiments on MIMIC-IV clinical risk prediction tasks across various clinical LMs show that CURA consistently improves calibration metrics without substantially compromising discrimination. Further analysis illustrates that CURA reduces overconfident false reassurance and yields more trustworthy uncertainty estimates for downstream clinical decision support.

---


### 75. [Rethinking Patient Education as Multi-turn Multi-modal Interaction](https://arxiv.org/abs/2604.14656)

**<font color=#1a73e8>作者：</font>** Zonghai Yao, Zhipeng Tang, Chengtao Lin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most medical multimodal benchmarks focus on static tasks such as image question answering, report generation, and plain-language rewriting. Patient education is more demanding: systems must identify relevant evidence across images, show patients where to look, explain findings in accessible language, and handle confusion or distress. Yet most patient education work remains text-only, even though combined image-and-text explanations may better support understanding. We introduce MedImageEdu, a benchmark for multi-turn, evidence-grounded radiology patient education. Each case provides a radiology report with report text and case images. A DoctorAgent interacts with a PatientAgent, conditioned on a hidden profile that captures factors such as education level, health literacy, and personality. When a patient question would benefit from visual support, the DoctorAgent can issue drawing instructions grounded in the report, case images, and the current question to a benchmark-provided drawing tool. The tool returns image(s), after which the DoctorAgent produces a final multimodal response consisting of the image(s) and a grounded plain-language explanation. MedImageEdu contains 150 cases from three sources and evaluates both the consultation process and the final multimodal response along five dimensions: Consultation, Safety and Scope, Language Quality, Drawing Quality, and Image-Text Response Quality. Across representative open- and closed-source vision-language model agents, we find three consistent gaps: fluent language often outpaces faithful visual grounding, safety is the weakest dimension across disease categories, and emotionally tense interactions are harder than low education or low health literacy. MedImageEdu provides a controlled testbed for assessing whether multimodal agents can teach from evidence rather than merely answer from text.

---


### 76. [SPAGBias: Uncovering and Tracing Structured Spatial Gender Bias in Large Language Models](https://arxiv.org/abs/2604.14672)

**<font color=#1a73e8>作者：</font>** Binxian Su, Haoye Lou, Shucheng Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are being increasingly used in urban planning, but since gendered space theory highlights how gender hierarchies are embedded in spatial organization, there is concern that LLMs may reproduce or amplify such biases. We introduce SPAGBias - the first systematic framework to evaluate spatial gender bias in LLMs. It combines a taxonomy of 62 urban micro-spaces, a prompt library, and three diagnostic layers: explicit (forced-choice resampling), probabilistic (token-level asymmetry), and constructional (semantic and narrative role analysis). Testing six representative models, we identify structured gender-space associations that go beyond the public-private divide, forming nuanced micro-level mappings. Story generation reveals how emotion, wording, and social roles jointly shape "spatial gender narratives". We also examine how prompt design, temperature, and model scale influence bias expression. Tracing experiments indicate that these patterns are embedded and reinforced across the model pipeline (pre-training, instruction tuning, and reward modeling), with model associations found to substantially exceed real-world distributions. Downstream experiments further reveal that such biases produce concrete failures in both normative and descriptive application settings. This work connects sociological theory with computational analysis, extending bias research into the spatial domain and uncovering how LLMs encode social gender cognition through language.

---


### 77. [Acceptance Dynamics Across Cognitive Domains in Speculative Decoding](https://arxiv.org/abs/2604.14682)

**<font color=#1a73e8>作者：</font>** Saif Mahmoud  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates large language model (LLM) inference. It uses a small draft model to propose a tree of future tokens. A larger target model then verifies these tokens in a single batched forward pass. Despite the growing body of work on speculative methods, the degree to which the cognitive characteristics of a task affect acceptance probability remains largely unexplored. We present an empirical study of tree-based speculative decoding acceptance dynamics. Our study spans four well-established NLP benchmark domains: code generation, mathematical reasoning, logical reasoning, and open-ended chat. For this, we use TinyLlama-1.1B as the draft model against Llama-2-7B-Chat-GPTQ as the target. Over 99,768 speculative nodes collected from 200 prompts, we derive per-domain acceptance rates, expected accepted lengths, depth-acceptance profiles, and entropy-acceptance correlations. We find that task type is a stronger predictor of acceptance than tree depth. Furthermore, only the chat domain consistently yields an expected accepted length exceeding 1.0 token per step. We also show that the entropy-acceptance correlation is consistently negative but weak across all domains (rho in [-0.20, -0.15]). Counterintuitively, chat produces the highest entropy yet the highest acceptance rate. We attribute this divergence to the lexical predictability of RLHF-aligned register. These findings have direct implications for domain-aware speculation budgets and draft-model selection strategies. Index Terms--speculative decoding, large language model inference, tree attention, draft model, acceptance probability, LLM efficiency

---


### 78. [DR$^{3}$-Eval: Towards Realistic and Reproducible Deep Research Evaluation](https://arxiv.org/abs/2604.14683)

**<font color=#1a73e8>作者：</font>** Qianqian Xie, Qingheng Xiong, He Zhu 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep Research Agents (DRAs) aim to solve complex, long-horizon research tasks involving planning, retrieval, multimodal understanding, and report generation, yet their evaluation remains challenging due to dynamic web environments and ambiguous task definitions. We propose DR$^{3}$-Eval, a realistic and reproducible benchmark for evaluating deep research agents on multimodal, multi-file report generation. DR$^{3}$-Eval is constructed from authentic user-provided materials and paired with a per-task static research sandbox corpus that simulates open-web complexity while remaining fully verifiable, containing supportive documents, distractors, and noise. Moreover, we introduce a multi-dimensional evaluation framework measuring Information Recall, Factual Accuracy, Citation Coverage, Instruction Following, and Depth Quality, and validate its alignment with human judgments. Experiments with our developed multi-agent system DR$^{3}$-Agent based on multiple state-of-the-art language models demonstrate that DR$^{3}$-Eval is highly challenging and reveals critical failure modes in retrieval robustness and hallucination control. Our code and data are publicly available.

---


### 79. [M2-PALE: A Framework for Explaining Multi-Agent MCTS--Minimax Hybrids via Process Mining and LLMs](https://arxiv.org/abs/2604.14687)

**<font color=#1a73e8>作者：</font>** Yiyu Qian, Liyuan Zhao, Tim Miller  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Monte-Carlo Tree Search (MCTS) is a fundamental sampling-based search algorithm widely used for online planning in sequential decision-making domains. Despite its success in driving recent advances in artificial intelligence, understanding the behavior of MCTS agents remains a challenge for both developers and users. This difficulty stems from the complex search trees produced through the simulation of numerous future states and their intricate relationships. A known weakness of standard MCTS is its reliance on highly selective tree construction, which may lead to the omission of crucial moves and a vulnerability to tactical traps. To resolve this, we incorporate shallow, full-width Minimax search into the rollout phase of multi-agent MCTS to enhance strategic depth. Furthermore, to demystify the resulting decision-making logic, we introduce \textsf{M2-PALE} (MCTS--Minimax Process-Aided Linguistic Explanations). This framework employs process mining techniques, specifically the Alpha Miner, iDHM, and Inductive Miner algorithms, to extract underlying behavioral workflows from agent execution traces. These process models are then synthesized by LLMs to generate human-readable causal and distal explanations. We demonstrate the efficacy of our approach in a small-scale checkers environment, establishing a scalable foundation for interpreting hybrid agents in increasingly complex strategic domains.

---


### 80. [CAMO: An Agentic Framework for Automated Causal Discovery from Micro Behaviors to Macro Emergence in LLM Agent Simulations](https://arxiv.org/abs/2604.14691)

**<font color=#1a73e8>作者：</font>** Xiangning Yu, Yuwei Guo, Yuqi Hou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-empowered agent simulations are increasingly used to study social emergence, yet the micro-to-macro causal mechanisms behind macro outcomes often remain unclear. This is challenging because emergence arises from intertwined agent interactions and meso-level feedback and nonlinearity, making generative mechanisms hard to disentangle. To this end, we introduce \textbf{\textsc{CAMO}}, an automated \textbf{Ca}usal discovery framework from \textbf{M}icr\textbf{o} behaviors to \textbf{M}acr\textbf{o} Emergence in LLM agent simulations. \textsc{CAMO} converts mechanistic hypotheses into computable factors grounded in simulation records and learns a compact causal representation centered on an emergent target $Y$. \textsc{CAMO} outputs a computable Markov boundary and a minimal upstream explanatory subgraph, yielding interpretable causal chains and actionable intervention levers. It also uses simulator-internal counterfactual probing to orient ambiguous edges and revise hypotheses when evidence contradicts the current view. Experiments across four emergent settings demonstrate the promise of \textsc{CAMO}.

---


### 81. [HWE-Bench: Benchmarking LLM Agents on Real-World Hardware Bug Repair Tasks](https://arxiv.org/abs/2604.14709)

**<font color=#1a73e8>作者：</font>** Fan Cui, Hongyuan Hou, Zizhang Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing benchmarks for hardware design primarily evaluate Large Language Models (LLMs) on isolated, component-level tasks such as generating HDL modules from specifications, leaving repository-scale evaluation unaddressed. We introduce HWE-Bench, the first large-scale, repository-level benchmark for evaluating LLM agents on real-world hardware bug repair tasks. HWE-Bench comprises 417 task instances derived from real historical bug-fix pull requests across six major open-source projects spanning both Verilog/SystemVerilog and Chisel, covering RISC-V cores, SoCs, and security roots-of-trust. Each task is grounded in a fully containerized environment where the agent must resolve a real bug report, with correctness validated through the project's native simulation and regression flows. The benchmark is built through a largely automated pipeline that enables efficient expansion to new repositories. We evaluate seven LLMs with four agent frameworks and find that the best agent resolves 70.7% of tasks overall, with performance exceeding 90% on smaller cores but dropping below 65% on complex SoC-level projects. We observe larger performance gaps across models than commonly reported on software benchmarks, and difficulty is driven by project scope and bug-type distribution rather than code size alone. Our failure analysis traces agent failures to three stages of the debugging process: fault localization, hardware-semantic reasoning, and cross-artifact coordination across RTL, configuration, and verification components, providing concrete directions for developing more capable hardware-aware agents.

---


### 82. [G-MIXER: Geodesic Mixup-based Implicit Semantic Expansion and Explicit Semantic Re-ranking for Zero-Shot Composed Image Retrieval](https://arxiv.org/abs/2604.14710)

**<font color=#1a73e8>作者：</font>** Jiyoung Lim, Heejae Yang, Jee-Hyong Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Composed Image Retrieval (CIR) aims to retrieve target images by integrating a reference image with a corresponding modification text. CIR requires jointly considering the explicit semantics specified in the query and the implicit semantics embedded within its bi-modal composition. Recent training-free Zero-Shot CIR (ZS-CIR) methods leverage Multimodal Large Language Models (MLLMs) to generate detailed target descriptions, converting the implicit information into explicit textual expressions. However, these methods rely heavily on the textual modality and fail to capture the fuzzy retrieval nature that requires considering diverse combinations of candidates. This leads to reduced diversity and accuracy in retrieval results. To address this limitation, we propose a novel training-free method, Geodesic Mixup-based Implicit semantic eXpansion and Explicit semantic Re-ranking for ZS-CIR (G-MIXER). G-MIXER constructs composed query features that reflect the implicit semantics of reference image-text pairs through geodesic mixup over a range of mixup ratios, and builds a diverse candidate set. The generated candidates are then re-ranked using explicit semantics derived from MLLMs, improving both retrieval diversity and accuracy. Our proposed G-MIXER achieves state-of-the-art performance across multiple ZS-CIR benchmarks, effectively handling both implicit and explicit semantics without additional training. Our code will be available at this https URL.

---


### 83. [SGA-MCTS: Decoupling Planning from Execution via Training-Free Atomic Experience Retrieval](https://arxiv.org/abs/2604.14712)

**<font color=#1a73e8>作者：</font>** Xin Xie, Dongyun Xue, Wuguannan Yao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-powered systems require complex multi-step decision-making abilities to solve real-world tasks, yet current planning approaches face a trade-off between the high latency of inference-time search and the limited generalization of supervised fine-tuning. To address this limitation, we introduce \textbf{SGA-MCTS}, a framework that casts LLM planning as non-parametric retrieval. Offline, we leverage Monte Carlo Tree Search (MCTS) to explore the solution space and distill high-fidelity trajectories into State-Goal-Action (SGA) atoms. These atoms are de-lexicalized primitives that abstract concrete entities into symbolic slots, preserving reusable causal logic while discarding domain-specific noise. Online, a retrieval-augmented agent employs a hybrid symbolic-semantic mechanism to fetch relevant SGAs and re-ground them into the current context as soft reasoning hints. Empirical results on complex benchmarks demonstrate that this paradigm enables frozen, open-weights models to match the performance of SOTA systems (e.g., GPT-5) without task-specific fine-tuning. By effectively amortizing the heavy computational cost of search, SGA-MCTS achieves System 2 reasoning depth at System 1 inference speeds, rendering autonomous planning both scalable and real-time feasible.

---


### 84. [A Mechanistic Account of Attention Sinks in GPT-2: One Circuit, Broader Implications for Mitigation](https://arxiv.org/abs/2604.14722)

**<font color=#1a73e8>作者：</font>** Yuval Ran-Milo, Hila Ofek, Shahar Mendel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers commonly exhibit an attention sink: disproportionately high attention to the first position. We study this behavior in GPT-2-style models with learned query biases and absolute positional embeddings. Combining structural analysis with causal interventions, validated across natural-language, mathematical, and code inputs, we find that the sink arises from the interaction among (i) a learned query bias, (ii) the first-layer MLP transformation of the positional encoding, and (iii) structure in the key projection. Crucially, each component we identify is individually dispensable: architectures omitting each of them robustly exhibit sinks. This indicates that attention sinks may arise through distinct circuits across architectures. These findings inform mitigation of sinks, and motivate broader investigation into why sinks emerge.

---


### 85. [Assessing the Performance-Efficiency Trade-off of Foundation Models in Probabilistic Electricity Price Forecasting](https://arxiv.org/abs/2604.14739)

**<font color=#1a73e8>作者：</font>** Jan Niklas Lettner, Hadeer El Ashhab, Veit Hagenmeyer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale renewable energy deployment introduces pronounced volatility into the electricity system, turning grid operation into a complex stochastic optimization problem. Accurate electricity price forecasting (EPF) is essential not only to support operational decisions, such as optimal bidding strategies and balancing power preparation, but also to reduce economic risk and improve market efficiency. Probabilistic forecasts are particularly valuable because they quantify uncertainty stemming from renewable intermittency, market coupling, and regulatory changes, enabling market participants to make informed decisions that minimize losses and optimize expected revenues. However, it remains an open question which models to employ to produce accurate forecasts. Should these be task-specific machine learning (ML) models or Time Series Foundation Models (TSFMs)? In this work, we compare four models for day-ahead probabilistic EPF (PEPF) in European bidding zones: a deterministic NHITS backbone with Quantile-Regression Averaging (NHITS+QRA) and a conditional Normalizing-Flow forecaster (NF) are compared with two TSFMs, namely Moirai and ChronosX. On the one hand, we find that TSFMs outperform task-specific deep learning models trained from scratch in terms of CRPS, Energy Score, and predictive interval calibration across market conditions. On the other hand, we find that well-configured task-specific models, particularly NHITS combined with QRA, achieve performance very close to TSFMs, and in some scenarios, such as when supplied with additional informative feature groups or adapted via few-shot learning from other European markets, they can even surpass TSFMs. Overall, our findings show that while TSFMs offer expressive modeling capabilities, conventional models remain highly competitive, emphasizing the need to weigh computational expense against marginal performance improvements in PEPF.

---


### 86. [Disentangle-then-Refine: LLM-Guided Decoupling and Structure-Aware Refinement for Graph Contrastive Learning](https://arxiv.org/abs/2604.14746)

**<font color=#1a73e8>作者：</font>** Zhaoxing Li, Hai-Feng Zhang, Xiaoming Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conventional Graph Contrastive Learning (GCL) on Text-Attributed Graphs (TAGs) relies on blind stochastic augmentations, inadvertently entangling task-relevant signals with noise. We propose SDM-SCR, a robust framework anchored in Approximate Orthogonal Decomposition. First, the Semantic Decoupling Module (SDM) leverages the instruction-following capability of Large Language Models (LLMs) to actively parse raw attributes into asymmetric, task-oriented signal and noise views. This shifts the paradigm from random perturbation to semantic-aware disentanglement. Subsequently, Semantic Consistency Regularization (SCR) exploits the spectral observation that semantic signals are topologically smooth while residual noise is high-frequency. SCR functions as a selective spectral filter, enforcing consistency only on the signal subspace to eliminate LLM hallucinations without over-smoothing. This ``Disentangle-then-Refine'' mechanism ensures rigorous signal purification. Extensive experiments demonstrate that SDM-SCR achieves SOTA performance in accuracy and efficiency.

---


### 87. [CoTEvol: Self-Evolving Chain-of-Thoughts for Data Synthesis in Mathematical Reasoning](https://arxiv.org/abs/2604.14768)

**<font color=#1a73e8>作者：</font>** Zhuo Wang, Zhuo Zhang, Yafu Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) exhibit strong mathematical reasoning when trained on high-quality Chain-of-Thought (CoT) that articulates intermediate steps, yet costly CoT curation hinders further progress. While existing remedies such as distillation from stronger LLMs and self-synthesis based on test-time search alleviate this issue, they often suffer from diminishing returns or high computing this http URL this work, we propose CoTEvol, a genetic evolutionary framework that casts CoT generation as a population-based search over reasoning this http URL trajectories are iteratively evolved through reflective global crossover at the trajectory level and local mutation guided by uncertainty at the step level, enabling holistic recombination and fine-grained refinement. Lightweight, task-aware fitness functions are designed to guide the evolutionary process toward accurate and diverse reasoning. Empirically, CoTEvol improves correct-CoT synthesis success by over 30% and enhances structural diversity, with markedly improved efficiency. LLMs trained on these evolutionary CoT data achieve an average gain of 6.6% across eight math benchmarks, outperforming previous distillation and self-synthesis approaches. These results underscore the promise of evolutionary CoT synthesis as a scalable and effective method for mathematical reasoning tasks.

---


### 88. [Constraint-based Pre-training: From Structured Constraints to Scalable Model Initialization](https://arxiv.org/abs/2604.14769)

**<font color=#1a73e8>作者：</font>** Fu Feng, Yucheng Xie, Ruixiao Shi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The pre-training and fine-tuning paradigm has become the dominant approach for model adaptation. However, conventional pre-training typically yields models at a fixed scale, whereas practical deployment often requires models of varying sizes, exposing its limitations when target model scales differ from those used during pre-training. To address this, we propose an innovative constraint-based pre-training paradigm that imposes structured constraints during pre-training to disentangle size-agnostic knowledge into reusable weight templates, while assigning size-specific adaptation to lightweight weight scalers, thereby reformulating variable-sized model initialization as a multi-task adaptation problem. Within this paradigm, we further introduce WeiT, which employs Kronecker-based constraints to regularize the pre-training process. Specifically, model parameters are represented as compositions of weight templates via concatenation and weighted aggregation, with adaptive connections governed by lightweight weight scalers whose parameters are learned from limited data. This design enables flexible and efficient construction of model weights across diverse downstream scales. Extensive experiments demonstrate the efficiency and effectiveness of WeiT, achieving state-of-the-art performance in initializing models with varying depths and widths across a broad range of perception and embodied learning tasks, including Image Classification, Image Generation, and Embodied Control. Moreover, its effectiveness generalizes to both Transformer-based and Convolution-based architectures, consistently enabling faster convergence and improved performance even under full training.

---


### 89. [MirrorBench: Evaluating Self-centric Intelligence in MLLMs by Introducing a Mirror](https://arxiv.org/abs/2604.14785)

**<font color=#1a73e8>作者：</font>** Shengyu Guo, Tongrui Ye, Jianbo Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent progress in Multimodal Large Language Models (MLLMs) has demonstrated remarkable advances in perception and reasoning, suggesting their potential for embodied intelligence. While recent studies have evaluated embodied MLLMs in interactive settings, current benchmarks mainly target capabilities to perceive, understand, and interact with external objects, lacking a systematic evaluation of self-centric intelligence. To address this, we introduce MirrorBench, a simulation-based benchmark inspired by the classical Mirror Self-Recognition (MSR) test in psychology. MirrorBench extends this paradigm to embodied MLLMs through a tiered framework of progressively challenging tasks, assessing agents from basic visual perception to high-level self-representation. Experiments on leading MLLMs show that even at the lowest level, their performance remains substantially inferior to human performance, revealing fundamental limitations in self-referential understanding. Our study bridges psychological paradigms and embodied intelligence, offering a principled framework for evaluating the emergence of general intelligence in large models. Project page: this https URL.

---


### 90. [Knowing When Not to Answer: Evaluating Abstention in Multimodal Reasoning Systems](https://arxiv.org/abs/2604.14799)

**<font color=#1a73e8>作者：</font>** Nishanth Madhusudhan, Vikas Yadav, Alexandre Lacoste  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Effective abstention (EA), recognizing evidence insufficiency and refraining from answering, is critical for reliable multimodal systems. Yet existing evaluation paradigms for vision-language models (VLMs) and multi-agent systems (MAS) assume answerability, pushing models to always respond. Abstention has been studied in text-only settings but remains underexplored multimodally; current benchmarks either ignore unanswerability or rely on coarse methods that miss realistic failure modes. We introduce MM-AQA, a benchmark that constructs unanswerable instances from answerable ones via transformations along two axes: visual modality dependency and evidence sufficiency. Evaluating three frontier VLMs spanning closed and open-source models and two MAS architectures across 2079 samples, we find: (1) under standard prompting, VLMs rarely abstain; even simple confidence baselines outperform this setup, (2) MAS improves abstention but introduces an accuracy-abstention trade-off, (3) sequential designs match or exceed iterative variants, suggesting the bottleneck is miscalibration rather than reasoning depth, and (4) models abstain when image or text evidence is absent, but attempt reconciliation with degraded or contradictory evidence. Effective multimodal abstention requires abstention-aware training rather than better prompting or more agents.

---


### 91. [The LLM Fallacy: Misattribution in AI-Assisted Cognitive Workflows](https://arxiv.org/abs/2604.14807)

**<font color=#1a73e8>作者：</font>** Hyunwoo Kim, Harin Yu, Hanau Yi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid integration of large language models (LLMs) into everyday workflows has transformed how individuals perform cognitive tasks such as writing, programming, analysis, and multilingual communication. While prior research has focused on model reliability, hallucination, and user trust calibration, less attention has been given to how LLM usage reshapes users' perceptions of their own capabilities. This paper introduces the LLM fallacy, a cognitive attribution error in which individuals misinterpret LLM-assisted outputs as evidence of their own independent competence, producing a systematic divergence between perceived and actual capability. We argue that the opacity, fluency, and low-friction interaction patterns of LLMs obscure the boundary between human and machine contribution, leading users to infer competence from outputs rather than from the processes that generate them. We situate the LLM fallacy within existing literature on automation bias, cognitive offloading, and human--AI collaboration, while distinguishing it as a form of attributional distortion specific to AI-mediated workflows. We propose a conceptual framework of its underlying mechanisms and a typology of manifestations across computational, linguistic, analytical, and creative domains. Finally, we examine implications for education, hiring, and AI literacy, and outline directions for empirical validation. We also provide a transparent account of human--AI collaborative methodology. This work establishes a foundation for understanding how generative AI systems not only augment cognitive performance but also reshape self-perception and perceived expertise.

---


### 92. [Modeling LLM Unlearning as an Asymmetric Two-Task Learning Problem](https://arxiv.org/abs/2604.14808)

**<font color=#1a73e8>作者：</font>** Zeguan Xiao, Siqing Li, Yong Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine unlearning for large language models (LLMs) aims to remove targeted knowledge while preserving general capability. In this paper, we recast LLM unlearning as an asymmetric two-task problem: retention is the primary objective and forgetting is an auxiliary. From this perspective, we propose a retention-prioritized gradient synthesis framework that decouples task-specific gradient extraction from conflict-aware combination. Instantiating the framework, we adapt established PCGrad to resolve gradient conflicts, and introduce SAGO, a novel retention-prioritized gradient synthesis method. Theoretically, both variants ensure non-negative cosine similarity with the retain gradient, while SAGO achieves strictly tighter alignment through constructive sign-constrained synthesis. Empirically, on WMDP Bio/Cyber and RWKU benchmarks, SAGO consistently pushes the Pareto frontier: e.g., on WMDP Bio (SimNPO+GD), recovery of target model MMLU performance progresses from 44.6% (naive) to 94.0% (+PCGrad) and further to 96.0% (+SAGO), while maintaining comparable forgetting strength. Our results show that re-shaping gradient geometry, rather than re-balancing losses, is the key to mitigating unlearning-retention trade-offs.

---


### 93. [Learning Ad Hoc Network Dynamics via Graph-Structured World Models](https://arxiv.org/abs/2604.14811)

**<font color=#1a73e8>作者：</font>** Can Karacelebi, Yusuf Talha Sahin, Elif Surer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ad hoc wireless networks exhibit complex, innate and coupled dynamics: node mobility, energy depletion and topology change that are difficult to model analytically. Model-free deep reinforcement learning requires sustained online interaction whereas existing model based approaches use flat state representations that lose per node structure. Therefore we propose G-RSSM, a graph structured recurrent state space model that maintains per node latent states with cross node multi head attention to learn the dynamics jointly from offline trajectories. We apply the proposed method to the downstream task clustering where a cluster head selection policy trains entirely through imagined rollouts in the learned world model. Across 27 evaluation scenarios spanning MANET, VANET, FANET, WSN and tactical networks with N=30 to 1000 nodes, the learned policy maintains high connectivity with only trained for N=50. Herein, we propose the first multi physics graph structured world model applied to combinatorial per node decision making in size agnostic wireless ad hoc networks.

---


### 94. [Domain Fine-Tuning FinBERT on Finnish Histopathological Reports: Train-Time Signals and Downstream Correlations](https://arxiv.org/abs/2604.14815)

**<font color=#1a73e8>作者：</font>** Rami Luisto, Liisa Petäinen, Tommi Grönholm 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In NLP classification tasks where little labeled data exists, domain fine-tuning of transformer models on unlabeled data is an established approach. In this paper we have two aims.
(1) We describe our observations from fine-tuning the Finnish BERT model on Finnish medical text data.
(2) We report on our attempts to predict the benefit of domain-specific pre-training of Finnish BERT from observing the geometry of embedding changes due to domain fine-tuning.
Our driving motivation is the common\situation in healthcare AI where we might experience long delays in acquiring datasets, especially with respect to labels.

---


### 95. [Intermediate Layers Encode Optimal Biological Representations in Single-Cell Foundation Models](https://arxiv.org/abs/2604.14838)

**<font color=#1a73e8>作者：</font>** Vincenzo Yuto Civale, Roberto Semeraro, Andrew David Bagdanov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current single-cell foundation model benchmarks universally extract final layer embeddings, assuming these represent optimal feature spaces. We systematically evaluate layer-wise representations from scFoundation (100M parameters) and Tahoe-X1 (1.3B parameters) across trajectory inference and perturbation response prediction. Our analysis reveals that optimal layers are task-dependent (trajectory peaks at 60% depth, 31% above final layers) and context-dependent (perturbation optima shift 0-96% across T cell activation states). Notably, first-layer embeddings outperform all deeper layers in quiescent cells, challenging assumptions about hierarchical feature abstraction. These findings demonstrate that "where" to extract features matters as much as "what" the model learns, necessitating systematic layer evaluation tailored to biological task and cellular context rather than defaulting to final-layer embeddings.

---


### 96. [Exploring and Testing Skill-Based Behavioral Profile Annotation: Human Operability and LLM Feasibility under Schema-Guided Execution](https://arxiv.org/abs/2604.14843)

**<font color=#1a73e8>作者：</font>** Yufeng Wu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Behavioral Profile (BP) annotation is difficult to automate because it requires simultaneous coding across multiple linguistic dimensions. We treat BP annotation as a bundle of annotation skills rather than a single task and evaluate LLM-assisted BP annotation from this perspective. Using 3,134 concordance lines of 30 Chinese metaphorical color-term derivatives and a 14-feature BP schema, we implement a skill-file-driven pipeline in which each feature is externally defined through schema files, decision rules, and examples. Two human annotators completed a two-round schema-only protocol on a 300-instance validation subset, enabling BP skills to be classified as directly operable, recoverable under focused re-annotation, or structurally underspecified. GPT-5.4 and three locally deployable open-source models were then evaluated under the same setup. Results show that BP annotation is highly heterogeneous at the skill level: 5 skills are directly operable, 4 are recoverable after focused re-annotation, and 5 remain structurally underspecified. GPT-5.4 executes the retained skills with substantial reliability (accuracy = 0.678, \k{appa} = 0.665, weighted F1 = 0.695), but this feasibility is selective rather than global. Human and GPT difficulty profiles are strongly aligned at the skill level (r = 0.881), but not at the instance level (r = 0.016) or lexical-item level (r = -0.142), a pattern we describe as shared taxonomy, independent execution. Pairwise agreement further suggests that GPT is better understood as an independent third skill voice than as a direct human substitute. Open-source failures are concentrated in schema-to-skill execution problems. These findings suggest that automatic annotation should be evaluated in terms of skill feasibility rather than task-level automation.

---


### 97. [Zero-Shot Retail Theft Detection via Orchestrated Vision Models: A Model-Agnostic, Cost-Effective Alternative to Trained Single-Model Systems](https://arxiv.org/abs/2604.14846)

**<font color=#1a73e8>作者：</font>** Haileab Yagersew  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retail theft costs the global economy over \$100 billion annually, yet existing AI-based detection systems require expensive custom model training on proprietary datasets and charge \$200-500/month per store. We present Paza, a zero-shot retail theft detection framework that achieves practical concealment detection without training any model. Our approach orchestrates multiple existing models in a layered pipeline - cheap object detection and pose estimation running continuously, with an expensive vision-language model (VLM) invoked only when behavioral pre-filters trigger. A multi-signal suspicion pre-filter (requiring dwell time plus at least one behavioral signal) reduces VLM invocations by 240x compared to per-frame analysis, bounding calls to <=10/minute and enabling a single GPU to serve 10-20 stores. The architecture is model-agnostic: the VLM component accepts any OpenAI-compatible endpoint, enabling operators to swap between models such as Gemma 4, Qwen3.5-Omni, GPT-4o, or future releases without code changes - ensuring the system improves as the VLM landscape evolves. We evaluate the VLM component on the DCSASS synthesized shoplifting dataset (169 clips, controlled environment), achieving 89.5% precision and 92.8% specificity at 59.3% recall zero-shot - where the recall gap is attributable to sparse frame sampling in offline evaluation rather than VLM reasoning failures, as precision and specificity are the operationally critical metrics determining false alarm rates. We present a detailed cost model showing viability at \$50-100/month per store (3-10x cheaper than commercial alternatives), and introduce a privacy-preserving design that obfuscates faces in the detection pipeline. The source code is available at this https URL.

---


### 98. [TrigReason: Trigger-Based Collaboration between Small and Large Reasoning Models](https://arxiv.org/abs/2604.14847)

**<font color=#1a73e8>作者：</font>** Yi Zhao, Yajuan Peng, Cam-Tu Nguyen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) achieve strong performance on complex tasks through extended chains of thought but suffer from high inference latency due to autoregressive reasoning. Recent work explores using Small Reasoning Models (SRMs) to accelerate LRM inference. In this paper, we systematically characterize the capability boundaries of SRMs and identify three common types of reasoning risks: (1) path divergence, where SRMs lack the strategic ability to construct an initial plan, causing reasoning to deviate from the most probable path; (2) cognitive overload, where SRMs fail to solve particularly difficult steps; and (3) recovery inability, where SRMs lack robust self-reflection and error correction mechanisms. To address these challenges, we propose TrigReason, a trigger-based collaborative reasoning framework that replaces continuous polling with selective intervention. TrigReason delegates most reasoning to the SRM and activates LRM intervention only when necessary-during initial strategic planning (strategic priming trigger), upon detecting extraordinary overconfidence (cognitive offload trigger), or when reasoning falls into unproductive loops (intervention request trigger). The evaluation results on AIME24, AIME25, and GPQA-D indicate that TrigReason matches the accuracy of full LRMs and SpecReason, while offloading 1.70x - 4.79x more reasoning steps to SRMs. Under edge-cloud conditions, TrigReason reduces latency by 43.9\% and API cost by 73.3\%. Our code is available at \href{this https URL}{this https URL}

---


### 99. [Adaptive Test-Time Compute Allocation for Reasoning LLMs via Constrained Policy Optimization](https://arxiv.org/abs/2604.14853)

**<font color=#1a73e8>作者：</font>** Zhiyuan Zhai, Bingcong Li, Bingnan Xiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time compute scaling, the practice of spending extra computation during inference via repeated sampling, search, or extended reasoning, has become a powerful lever for improving large language model performance. Yet deploying these techniques under finite inference budgets requires a decision that current systems largely ignore: which inputs deserve more compute, and which can be answered cheaply? We formalize this as a constrained optimization problem (maximize expected accuracy subject to an average compute budget) and solve it with a two-stage Solve-then-Learn pipeline. In the solve stage, Lagrangian relaxation decomposes the global constraint into per-instance sub-problems, each admitting a closed-form oracle action that optimally prices accuracy against cost. We prove that the induced cost is monotone in the dual variable, enabling exact budget targeting via binary search. In the learn stage, a lightweight classifier is trained to predict oracle actions from cheap input features, amortizing the allocation rule for real-time deployment. We establish that the task-level regret of the learned policy is bounded by its imitation error times the worst-case per-instance gap, yielding a clean reduction from constrained inference to supervised classification. Experiments on MATH and GSM8K with three LLMs (DeepSeek-V3, GPT-4o-mini, Qwen2.5-7B) show that our method consistently outperforms uniform and heuristic allocation baselines, achieving up to 12.8% relative accuracy improvement on MATH under matched budget constraints, while closely tracking the Lagrangian oracle upper bound with over 91% imitation accuracy.

---


### 100. [Schema Key Wording as an Instruction Channel in Structured Generation under Constrained Decoding](https://arxiv.org/abs/2604.14862)

**<font color=#1a73e8>作者：</font>** Yifan Le  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Constrained decoding has been widely adopted for structured generation with large language models (LLMs), ensuring that outputs satisfy predefined formats such as JSON and XML. However, existing approaches largely treat schemas as purely structural constraints and overlook the possibility that their linguistic formulation may affect model behavior. In this work, we study how instruction placement influences model performance in structured generation and show that merely changing the wording of schema keys, without modifying the prompt or model parameters, can significantly alter model performance under constrained decoding. Based on this observation, we propose to reinterpret structured generation as a multi-channel instruction problem, where instructions can be conveyed explicitly through prompts and implicitly through schema keys during decoding. To the best of our knowledge, this is the first work to systematically study how schema key formulation acts as an implicit instruction channel and affects model performance under constrained decoding. Experiments on multiple mathematical reasoning benchmarks show that different model families exhibit distinct sensitivities to these instruction channels: Qwen models consistently benefit from schema-level instructions, while LLaMA models rely more heavily on prompt-level guidance. We further observe non-additive interaction effects between instruction channels, showing that combining multiple channels does not always lead to further improvement. These findings suggest that schema design not only determines output structure, but also carries instruction signals, offering a new perspective on structured generation in LLMs.

---


> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-143](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
