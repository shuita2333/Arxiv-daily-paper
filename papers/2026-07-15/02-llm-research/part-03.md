# 🧠 大模型相关研究 | 2026年07月15日

> 本类共 **199** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-199](./part-04.md)

---

### 101. [Trust Before Fusion: QIMG-7 and Source-Aware Resolution for Polluted Multimodal RAG](https://arxiv.org/abs/2607.10798)

**<font color=#1a73e8>作者：</font>** Saadeldine Eletter, Owais Aijaz, Preslav Nakov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal retrieval-augmented generation (RAG) is often evaluated with clean evidence, yet real retrieval can return topically relevant but unreliable content: false text and misleading images from corrupted metadata, entity swaps, typographic overlays, semantic edits, adversarial patches, blends, or style transfer. We introduce QIMG-7, a controlled benchmark for multimodal retrieval pollution in multi-sentence factual QA, spanning four datasets, seven image-attack families, and 16 paired clean/polluted regimes, for 1,760 evaluation rows per method. Across four generator/gate stacks, naive multimodal fusion is brittle: in the main gpt-4o-mini stack, Full-MM support drops from 0.908 with clean text to 0.490 with polluted text, often making Parametric fallback safer than retrieval. We propose source-aware trust resolution (SATR), a training-free approach that compares Parametric, Text-only, and Full-MM candidate answers and selects among candidate answers or falls back based on source reliability. The Field-Selector variant achieves the best balanced score, 0.816, improving over Full-MM by 11.7 points and over the Cascaded Router by 2.7 points. Ablations show that, in this text-first setting, explicit text-reliability modeling is the dominant driver of these gains. Overall, in text-first factual QA with multimodal retrieval conflict, our results support selective trust rather than unconditional fusion. Artifacts are available at this https URL.

---


### 102. [Weight-Adjusted Gradients Reveal Parameter Importance and Failure Modes in LLMs](https://arxiv.org/abs/2607.10803)

**<font color=#1a73e8>作者：</font>** Shrestha Datta, Hongfu Liu, Anshuman Chhabra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding which parameters are influential in Large Language Models (LLMs) is central to improving their efficiency, reliability, and interpretability. We introduce Weight-Adjusted Gradients (WAG), a simple yet effective approach for estimating parameter importance that explicitly captures the interaction between model weights and first-order gradient information and identifies parameters that disproportionately influence model behavior, such as those responsible for collapse phenomena in LLMs. Across a range of models and settings, we show that WAG surfaces a tiny but critical subset of parameters whose modification leads to dramatic degradation in performance, a failure mode that existing importance metrics overlook. These findings reveal a previously underexplored interplay between weights and gradients, suggesting that parameter importance cannot be fully understood through either signal alone. The surprising effectiveness of WAG points to fundamental structural properties of trained networks and motivates new open questions about the role of zeroth-order and first-order information in deep learning. We demonstrate the practical utility of WAG across multiple applications, including expert allocation in mixture-of-expert architectures, parameter-specific unlearning, mixed-precision quantization, and layer selection for knowledge editing. Our results position WAG as a unified approach for analyzing, debugging, and controlling LLMs, and opens new directions for principled model-level interpretation.

---


### 103. [Diagnosing and Mitigating Thinking Collapse in On-Policy Self-Distillation](https://arxiv.org/abs/2607.10805)

**<font color=#1a73e8>作者：</font>** Keqin Peng, Chen Li, Yuanxin Ouyang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-Policy Self-Distillation (OPSD) has emerged as a crucial paradigm for enhancing and aligning Large Language Models (LLMs). However, in complex reasoning tasks, OPSD paradoxically degrades downstream performance. In this paper, we systematically investigate this pathology and identify a severe optimization trap we define as \textbf{Thinking Collapse} -- a sharp decline in the model's native intermediate reasoning behavior, measured by epistemic-token density (ET per 1k). Through entropy-based gradient masking and token-level target analysis, we show that this collapse is triggered by aggressive teacher gradients at high-student-entropy decision forks, where student epistemic tokens are frequently suppressed into teacher non-epistemic targets and are highly concentrated in high pointwise student-teacher divergence regions. To resolve this optimization pathology, we propose \textbf{Adaptive Dual-Perspective OPSD (AD-OPSD)}, a robust control framework that dynamically moderates the self-distillation objective. AD-OPSD selectively anchors high-suppression-risk sandboxed tokens to a reference prior derived from the frozen base model via an asymmetrical pointwise divergence gate, preserving native thinking capacity while retaining OPSD's error-correcting power. Extensive experiments across competitive mathematical benchmarks show that AD-OPSD improves over standard OPSD by up to \textbf{+4.1\%} absolute average accuracy across diverse model scales and datasets. Further analysis demonstrates that AD-OPSD mitigates thinking collapse and generalizes robustly to different post-training paradigms.

---


### 104. [Distributed Agent System: Fault-Tolerant Collaboration Among Embodied Agents](https://arxiv.org/abs/2607.10811)

**<font color=#1a73e8>作者：</font>** Kai Yu, Lu Chen, Hanqi Li  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> AI engineering is shifting from passive text generation by large language models (LLMs) to agent-driven task execution, creating new reliability challenges for long-horizon tasks under resource constraints and environmental uncertainty. Conventional error-elimination optimization strategies fail to address cumulative error propagation. This paper proposes Distributed Agent System (DAS), a device-edge-cloud framework for fault-tolerant collaboration among heterogeneous agents. We redefine agent reliability as system-level fault tolerance rather than single-turn zero-error accuracy, and present a two-layer fault-tolerance architecture: single-agent execution reliability via fault-tolerant alignment, and cross-agent communication reliability via semi-formal language protocols. This framework provides a practical engineering pathway for reliable heterogeneous embodied agents collaboration in industrial scenarios.

---


### 105. [Auditing Belief-Conditioned LLM Agents in Hidden-Information Social Deduction Games](https://arxiv.org/abs/2607.10814)

**<font color=#1a73e8>作者：</font>** Yuan Gao, Jiangyi Yang, Yao Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Evaluating LLM agents in hidden-information multi-agent settings is hard: final outcomes are high-variance and rarely reveal why an agent decided as it did. We study this in a 9-player Werewolf environment where agents act under strict, code-level information isolation, and we build an auditable framework that maintains an external belief state over hidden roles, logs belief updates and belief-action deviations as structured evidence, and supports a defensive offline improvement loop that reviews bad cases before any strategy change.
Across 1,080 frozen games spanning belief-disabled, active-belief, kernel-ablation, camp-restricted, consumption-policy, and high-load arms, and including a seed-paired A0/A1 comparison, the active-belief condition is associated with substantially better good-side outcomes: in the 200-seed A0/A1 comparison the good-side win rate rises from 0.205 to 0.390 (paired McNemar $\chi^2 = 16.4$, $p < 0.001$), with fewer irreversible witch-poison errors. We do not, however, attribute this shift to belief content. Direct action-belief consistency is low ($\approx 0.21$), and giving belief only to the werewolves helps the good side more than giving it only to the good side, which argues against a simple holder-benefit account; we therefore report the effect as an association and treat its mechanism as unresolved. The contribution is the audit framework itself: it makes the effect measurable, exposes low direct action-belief consistency, rejects an unreliable forced-consumption intervention with evidence, and separates strategy effects from load confounds. We accordingly position external belief in high-noise hidden-information games primarily as an auditable cognitive baseline that also carries decision-relevant signal, turning opaque agent behavior into replayable evidence for safer, controlled iteration.

---


### 106. [Large Language Models for Token-Efficient and Semantic-Preserving Opinion Summarization](https://arxiv.org/abs/2607.10825)

**<font color=#1a73e8>作者：</font>** Fabrizio Marozzo, Stefano Iannicelli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Opinionated text - spanning product reviews, hotel feedback, and social posts - captures rich signals about user experiences, preferences, and concerns. However, the scale, redundancy, and imbalance of such corpora make it challenging to analyze opinions effectively, particularly when the goal is to generate summaries that remain faithful to the diversity of viewpoints expressed. This paper presents a framework that preserves semantics in LLM-based opinion summarization while minimizing token usage. We combine multidimensional classification (e.g., sentiment, topics) with a family of stratified sampling strategies to select compact yet representative subsets of opinions before prompting the LLM. Tailored prompts then produce balanced summaries that surface the salient aspects expressed in the opinions (e.g., strengths and weaknesses of products/hotels). Experiments on Amazon product reviews, Tripadvisor hotel reviews, and X/Twitter posts demonstrate that our method significantly reduces token usage and computational cost while consistently outperforming traditional AI-based and standard LLM summarization baselines in terms of content coverage, balance, and semantic preservation.

---


### 107. [3D-DefectBench: A Controlled Factorial Study of Vision-Language Model Evaluation Pipelines for Fine-Grained 3D Generation Defects](https://arxiv.org/abs/2607.10826)

**<font color=#1a73e8>作者：</font>** Zhenyu Zhao, Nanshan Jia, Jihyeon Je 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated evaluation is essential for scaling generative 3D systems, where exhaustive human review is costly and slow. However, the reliability of an automated judge depends on the entire evaluation pipeline, not only the underlying vision-language model (VLM), but also how assets are rendered, what visual evidence is provided, how the task is specified, and how human reference labels are constructed. We introduce 3D-DefectBench, a benchmark and framework for systematic analysis of VLM-based 3D defect detection pipelines. It complements holistic ratings and pairwise preferences with nine fine-grained binary defects spanning geometry, texture, and prompt adherence, providing actionable diagnostics for generator development and judge evaluation. Using a balanced factorial design, we vary four pipeline factors, VLM, camera protocol, visual input, and prompt schema, across 84 inference designs and approximately 3.2 million scored defect decisions, followed by staged validation on a broader set of frontier models. Model choice is the largest determinant of agreement with human labels, but the remaining factors also affect performance, interact with model selection, and can change the best configuration. Within the evaluated design space, a compact six-view RGB protocol performs comparably to denser multi-view settings and inputs augmented with depth or surface normals, making it a strong cost-effective default. Under this standardized pipeline, the best of 12 VLM judges still lag behind trained human labelers, while texture agreement drops sharply when expert-consensus labels are replaced by noisier silver labels. These findings show that automated judges should be evaluated as complete pipelines and calibrated across human reference regimes, rather than benchmarked only as standalone models. We release labels, prompts, predictions, and Croissant metadata on Hugging Face.

---


### 108. [Quantifying the Sources of Instability in LLM-Based Stance Analysis of Public Discourse](https://arxiv.org/abs/2607.10846)

**<font color=#1a73e8>作者：</font>** Bo Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Computational social science increasingly relies on automated preprocessing pipelines -- speaker diarization, ASR transcript cleaning, sentence segmentation -- to convert raw media into analyzable text. When these pipelines produce different outputs from the same input, two distinct sources of instability can arise: the preprocessing pipeline itself (diarization method, segmentation rules) and the downstream measurement instrument (LLM annotation vs.\ keyword lexicon). Using 256 YouTube interviews across 41 public figures from five domains, we compare two speaker-diarization pipelines and two measurement methods, all targeting the coupling between affective valence and epistemic modality. We find that (1) preprocessing pipeline sensitivity is concentrated in speakers with limited video samples (N $\leq 5$); for the four best-sampled speakers (N $\geq 16$), the mean absolute pipeline-induced change in $r(\text{neg}, \text{emph})$ is only $0.13$; (2) cross-method disagreement is larger and more systematic -- the LLM and keyword-lexicon methods assign opposite coupling directions to several well-sampled speakers, even within the same preprocessing pipeline; and (3) aggregate valence proportions are highly stable ($|\Delta p(\text{neg})| < 6$pp) regardless of pipeline or method, masking both sources of instability. The contribution is a diagnostic framework that separates pipeline effects from measurement effects: researchers studying cross-dimensional relationships in interview data should verify that their conclusions are robust to both sources of variation, with particular attention to measurement method choice.

---


### 109. [Predictive Divergence Masks for LLM RL](https://arxiv.org/abs/2607.10848)

**<font color=#1a73e8>作者：</font>** Xiangxin Zhou, Jiarui Yao, Penghui Qi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning for large language models (LLMs) typically relies on trust-region masks to stabilize off-policy updates. The dominant PPO-style approach uses the sampled-token importance ratio for two criteria: a proximity criterion, which asks whether the policy has moved too far from the behavior policy, and a direction criterion, which asks whether the update pushes it farther away. Recent work DPPO improves the proximity criterion by replacing PPO's ratio-based test with a probability divergence between the behavior and training policies. However, its direction criterion is still inherited from PPO. A token can be masked only when the sampled-token importance ratio moves away from one. We observe that this ratio-based direction criterion is a single-sample proxy that can disagree in sign with the change of the divergence that defines the proximity criterion. We therefore propose the predictive divergence mask, which asks whether the next policy-gradient step will increase or decrease the same divergence used by the trust region. For the discrete softmax policies used in LLM RL, we derive this prediction in closed form. Because production rollout engines expose only a truncated (top-K) view of the vocabulary, we develop two lightweight top-$K$ estimators for this prediction. Detailed analysis shows the divergence-based direction is better aligned with the realized change of the divergence than the sampled ratio, and the resulting masks improve RL training across model scales and precision settings.

---


### 110. [Capabilities of Claude Fable 5 on Biomedical Challenge Problems](https://arxiv.org/abs/2607.10849)

**<font color=#1a73e8>作者：</font>** Dominic Okonkwo, Magnus Hodgson, Temitope I. David 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Frontier language models are increasingly evaluated on biomedical benchmarks, but two problems undermine most published evaluations: legacy benchmarks are near-saturated, and open-ended responses are graded by other language models. We evaluate Claude Fable 5, Anthropic's most capable publicly available model, across eight biomedical benchmarks, four text and four multimodal, using deterministic scoring against fixed answer keys throughout. We include two Claude predecessors and GPT-5 as baselines. Refusal is tracked as a distinct outcome in every result table. That decision produces the paper's central finding. Fable 5 refuses between 8.0% and 99.4% of questions depending on the benchmark, a pattern absent in both predecessors and in GPT-5. Once refused items are excluded from the denominator, Fable 5's accuracy exceeds or meets every other model on every benchmark in this study. We identify two distinguishable refusal patterns: one concentrating in basic-science and mechanism content across MedQA and MedXpertQA MM, confirmed independently on two benchmarks using each benchmark's own category labels; and a separate disease-domain pattern on RareBench, where inborn metabolic disease presentations are refused near-universally while adult-onset autoimmune presentations are not. The primary constraint on Fable 5's biomedical usefulness is willingness to engage, not capability once it does.

---


### 111. [Reliability Scaling Laws for Quantized Large Language Models](https://arxiv.org/abs/2607.10855)

**<font color=#1a73e8>作者：</font>** Sirine Ayadi, Sándor Daróczi, Stephan Günnemann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantization is a powerful strategy to build capable and resource-efficient large language models (LLMs) by reducing the bitwidth of the parameters. While quantized LLMs achieve state-of-the-art performance on unperturbed inputs using standard predictive metrics, their performance on perturbed inputs, measured using reliability metrics, remains underexplored, despite its importance for reliable deployment. To address this gap, we first conduct a comprehensive reliability evaluation of quantized LLMs consisting of three key components: (1) Uncertainty: We assess the trustworthiness of LLMs quantized to 2, 3, 4, and 8 bits using six different quantization methods, employing established uncertainty metrics. (2) Calibration: We assess how well-calibrated the uncertainty estimates of quantized models are across model scales and bit precisions. (3) Robustness: We design character-level and word-level input perturbations to evaluate the reliability of quantized models under semantically-preserving variations in the inputs that arise in real-world applications. Second, we characterize how reliability scales with the total number of model bits. Our study reveals that while the performance scales monotonically with the total number of bits, the reliability scalings are nonlinear. A reliability peak occurs for 4-bit quantized models, indicating that quantizing moderately sized models offers the best reliability-efficiency trade-off. Additionally, our empirical findings reveal that quantization enhances the robustness of LLMs to natural input perturbations.

---


### 112. [Toward Contemplative LLM: A Modular Framework for Evaluating and Enhancing LLM Alignment in Mental Health](https://arxiv.org/abs/2607.10871)

**<font color=#1a73e8>作者：</font>** Asher Sprigler, Yang-Yang Feng, Iftach Amir 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Contemplative traditions have long guided ethical behavior and prosocial interaction, and recent work suggests that contemplative principles (e.g., mindfulness, compassion, non-dual reasoning) may offer a promising paradigm for aligning large language models (LLMs), improving cooperation and reducing ethical violations in LLM outputs. However, as new models, evaluation metrics, and benchmarks emerge rapidly, it remains challenging to systematically assess whether and how contemplative principles enhance LLM alignment across diverse and evolving scenarios, and existing approaches are often ad hoc and fail to generalize. We present a modular, extensible evaluation framework, initially targeted at the mental health domain, that enables seamless integration of new models, metrics, and benchmarks through a reusable pipeline. The framework currently reproduces existing state-of-the-art results and supports systematic cross-evaluation by flexibly mixing and matching models, metrics, and benchmarks, enabling fair comparison and deeper insight. Its plug-and-play prompting module offers a principled pathway for incorporating ethical perspectives such as contemplative principles, allowing domain experts to define alignment criteria without requiring technical expertise. Although initially focused on mental health, the framework is domain-agnostic and extends naturally to areas such as decision-making, moral reasoning, and human-AI collaboration. By bridging computational evaluation with human-centered ethical reasoning, this work lays the groundwork for interdisciplinary research spanning cognitive science, behavioral economics, philosophy, and system design, toward robust, trustworthy, and socially beneficial human-AI ecosystems.

---


### 113. [SETA: Scaling Environments for Terminal Agents](https://arxiv.org/abs/2607.10891)

**<font color=#1a73e8>作者：</font>** Qijia Shen, Zhiqi Huang, Vamsidhar Kamanuru 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are rapidly shifting toward agents that solve tasks through diverse interfaces, including web and graphical user interfaces (GUIs). Among these, the terminal command line provides a text-based, general-purpose interface, covering tasks from system operations to data science and machine learning. However, scaling terminal-agent training remains challenging, as it requires diverse and coherent task instructions, executable environments, and reliable verification, while lacking naturally grounded supervision data. In this work, we propose SETA, a scalable framework for generating verifiable terminal environments for reinforcement learning (RL). The framework consists of two pipelines sharing a unified verification mechanism: SETA-Synth converts diverse sources into standardized RL environments, and SETA-Evol further expands from existing environments with adaptive control of difficulty and diversity. Together, we construct and release SETA-Env, the largest open-source verifiable terminal RL dataset to date, containing over 4,500 environments. We evaluate our dataset by training Qwen3-8B with GRPO on SETA-Env, achieving 12% pass rate on Terminal-Bench 2.0, the best reported result for an RL-trained model at the 8B scale. We further observe gains on DeepSeek-V4-Flash under the same terminal agent harness, with pass@1 on Terminal-Bench 2.0 improving from 40% to 43% and pass@5 improving from 54% to 58%. These results demonstrate that SETA- Env provides high-quality training environments for terminal agents and serves as a valuable resource for advancing research on terminal-based agent learning.

---


### 114. [When Context Dominates: Multimodal Signatures of Takeover Readiness Under Varying Hazard and Cognitive Load Conditions](https://arxiv.org/abs/2607.10945)

**<font color=#1a73e8>作者：</font>** Shiva Azimi, Yasaman Hakiminejad, Luis Gomero 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Semi-automated driving systems promise to reduce crashes by assisting with perception and control, yet they simultaneously introduce additional human factors challenges by requiring drivers to monitor automation and rapidly resume control when failures occur. Prolonged passive monitoring can degrade vigilance, delay reactions, and increase takeover risk, but the extent to which distraction, hazard context, and drivers' underlying cognitive and physiological states jointly shape takeover performance remains insufficiently understood. This study investigates these interacting factors using a controlled, within-subjects driving simulator experiment that crosses two hazard types (dynamic pedestrian and static crash events) with three levels of secondary task engagement (no task, conversation, and working memory load). Driver responses were assessed using a multimodal sensing framework that integrates vehicle-dynamics measures, subjective workload ratings, autonomic physiology (electrodermal activity and heart rate variability), and prefrontal cortical activation measured with functional near-infrared spectroscopy. Results show that hazard context is the primary determinant of takeover behavior, with pedestrian events producing longer and more variable maneuvers and crash events yielding faster and more stable responses. Secondary tasks exerted smaller effects on objective vehicle control, while internal-state measures showed more variable task-related patterns. These findings highlight the importance of jointly considering environmental context and human state when evaluating takeover readiness and designing driver monitoring systems. This study lays the groundwork for adaptive, context-aware strategies that support safer human-automation collaboration in semi-automated vehicles.

---


### 115. [A Multi-Agent Framework for Zero-Dimensional Reduced-Order Model Planning](https://arxiv.org/abs/2607.10994)

**<font color=#1a73e8>作者：</font>** Bingteng Sun, Hao Yin, Yiling Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zero-dimensional reduced-order models (0D ROMs) are central to multi-dimensional design workflows for high-end complex equipment. However, the planning process currently relies on manual expertise, limiting topological exploration and prolonging iterations. Even traditional optimization methods such as Genetic Algorithms (GA) are typically confined to local parameter tuning. Although Large Language Model (LLM) agents have shown promise in exploring large sample spaces, and frameworks such as Chain of Thought (CoT) and Reason and Act (ReAct) improve reasoning reliability, while Retrieval-Augmented Generation (RAG) overcomes domain knowledge barriers, a single agent still falls short for the long-horizon and highly coupled nature of complex 0D ROM planning. This paper proposes the Zero-dimensional reduced-order model CO-Planning framework (Z-COPA), a multi-agent architecture featuring a Symbolic Action Graph Engine (SAGE) and a MILP-Guided Navigation (MGN) optimizer. Its core innovation is a dedicated graph representation method that accurately encodes the 0D flow network topology, converting the empirical planning process into a rigorous graph structure optimization problem. We validate the forward and inverse design capabilities and generalization performance of Z-COPA on two real aircraft engine secondary-air systems, two IEEE power-distribution reconfiguration benchmarks, and two water-distribution network benchmarks. The results show superior task completion quality, obtaining the best performance in both forward and reverse design of air systems. Z-COPA disrupts the traditional 0D model planning paradigm, providing a new technical approach for exploring broader topological space and achieving highly automated, globally optimal air system architectures.

---


### 116. [TabPFN beyond Tabular Data: Calibration and Accuracy on Multimodal Embeddings](https://arxiv.org/abs/2607.11007)

**<font color=#1a73e8>作者：</font>** Jingxiang Zhang, Lujia Zhong, Zijie Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Few-shot multimodal classification commonly attaches a lightweight head, such as $k$-nearest neighbors, logistic regression, or a linear SVM, to a frozen pretrained encoder. Although computationally efficient, these heads can produce poorly calibrated confidence scores, limiting their reliability in calibration-sensitive applications. We evaluate TabPFN as a plug-and-play, zero-gradient classification head for frozen image, text, and audio encoders. Across 22{,}820 evaluation episodes spanning 14 datasets, 11 encoders, and three modalities, TabPFN achieves the best mean rank among nine classification heads on both negative log-likelihood (NLL) and expected calibration error (ECE). At a representative setting, it reduces NLL by 48--62\% and ECE by 2.1--5.3$\times$ relative to the average of the eight baselines while matching or exceeding their average accuracy. Its accuracy advantage is conditional, concentrating at moderate-to-high shot counts and low-to-moderate feature dimensions ($k \ge 50$, $d \le 32$), and diminishing when labeled data are scarce, feature dimensions are high, or competing methods approach ceiling accuracy. In targeted backbone-adaptation experiments, replacing the trained linear head with TabPFN substantially improves calibration while preserving competitive accuracy. These results provide empirical guidance for using TabPFN as a training-free head in calibration-sensitive multimodal classification. To support transparency and reproducibility, we publicly release the source code, experiment configurations, and evaluation scripts in our GitHub repository: this https URL.

---


### 117. [EasyOPD: An Easy-to-use On-Policy Distillation Framework for Large Language Models](https://arxiv.org/abs/2607.11012)

**<font color=#1a73e8>作者：</font>** Jie Sun, Mao Zheng, Mingyang Song 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conventional language-model distillation often relies on fixed teacher-generated data, which may not cover the states encountered by an evolving student policy. On-policy distillation (OPD) instead collects teacher or evaluator supervision on student-generated rollouts. However, existing OPD methods differ substantially in supervision form, tokenizer compatibility, teacher access, and supervision granularity, leading to fragmented implementations that are difficult to reproduce and extend. We present \textsc{EasyOPD}, an on-policy distillation framework built on verl, a distributed reinforcement-learning framework for large language models. \textsc{EasyOPD} separates user-side configuration, method-specific supervision logic, and verl-based execution. Its method modules connect to the shared backend through extension boundaries for loss construction, rollout metadata, reward processing, tokenizer alignment, and teacher-side computation. We instantiate representative methods for three OPD settings -- cross-tokenizer OPD, on-policy self-distillation, and step-wise OPD. Experiments on reasoning, code-generation, scientific-knowledge, and tool-use benchmarks show that these implementations can be executed through the same verl-based backend while retaining their method-specific objectives and task-dependent performance profiles. We release \textsc{EasyOPD} with runnable YAML configurations, documentation, and an installable demonstration package and video.

---


### 118. [QwenPaw-Data: Bridging Facts, Methodology, and Execution for Autonomous Enterprise Data Analytics](https://arxiv.org/abs/2607.11019)

**<font color=#1a73e8>作者：</font>** Tianjing Zeng, Yuntao Hong, Zhongjun Ding 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise data analysis is emerging as a distinct frontier for autonomous agents. Compared with general-purpose interaction and software engineering, it operates in an open, ambiguous, and continuously evolving environment. These characteristics call for a data-agent architecture that treats semantics, methodology, execution, and evolution as first-class system concerns. To this end, we introduce QwenPaw-Data, an agentic data system designed for enterprise intelligent data analysis. QwenPaw-Data consolidates heterogeneous assets from warehouses, dashboards, documents, interaction logs, and historical tasks into reusable, governable, and evolvable analysis assets, then turns natural-language requests into end-to-end analytical workflows spanning data understanding, retrieval, analysis, report generation, and decision support. Its architecture decomposes the problem into three collaborative subsystems: DataBridge provides trustworthy semantic grounding through interconnected metadata, knowledge, and trace graphs; Skill-Hub codifies expert analytical methodology into reusable and verifiable skills; and Host materializes these evidence and method assets into controllable, artifact-centric runtime execution. Across these subsystems, semantics, methods, traces, and feedback are continuously deposited back into the system, forming a self-evolving asset flywheel. Experiments on public benchmarks and real-world industrial BI workloads show that QwenPaw-Data improves both verifiable data access capability and higher-level analytical quality, offering a practical foundation for reliable, traceable, and continuously improving enterprise data agents.

---


### 119. [Can a Language Model Learn Facts Continually in Its Weights?](https://arxiv.org/abs/2607.11020)

**<font color=#1a73e8>作者：</font>** Charles O'Neill  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continual learning promises a language model that keeps acquiring knowledge after training, with each new fact written into its weights. Whether weight writes can support accumulation remains undecided. We follow invented facts written into Qwen3 models from creation through sequences of twenty to one hundred later writes, using held-out questions of five types, with the original model given the fact in its prompt as the reference. Across these experiments, the breadth of the training data determines the kind of knowledge created. Bare-statement training produces recitation, while diverse restatements reduce the recitation-to-use gap from 27.4 to 5.4 points without showing the model a conclusion. This difference carries into later writes: after twenty sequential writes, bare-statement facts retain 1% accuracy while facts written from broad study data retain 46%. We also find that facts can be behaviourally forgotten without being erased. Forgotten facts keep most of the log-probability added by their write, and under bare-statement training 70% of wrong answers about them contain the most recently written fact. The same writes barely degrade the model's use of facts in context, and a forgotten study fact supplied in the prompt recovers to 77-80% on its questions. These results describe knowledge that is stored but question-keyed: later writes redirect the questions that reached it. Damage to unrelated abilities tracks KL divergence from the original model, and the later writes cause interference regardless of how the earlier fact was stored. Broad data can create usable knowledge, and a frozen reference can preserve capability, but no intervention we tested, including those built on accurate local measurements of each write, keeps earlier facts reachable. When facts must be composed or survive later writes, the reliable channel is context rather than the weights.

---


### 120. [Dimensionality in Satisfaction Ratings](https://arxiv.org/abs/2607.11026)

**<font color=#1a73e8>作者：</font>** Andrew Hong, Jason Potteiger  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We used a large language model (GPT-4.1) to annotate the text of about 9,000 support conversations at a global consumer-goods firm, decomposing customer-care satisfaction into component axes (overall, agent, outcome, product, and customer effort), and validated the LLM annotations against the satisfaction ratings customers gave themselves. Four of five axes track self-reported satisfaction closely (overall, agent, and outcome near an unadjusted 0.65; effort -0.54), while product satisfaction is weak against the available proxy. The unadjusted correlation also understates the alignment: the disagreements concentrate in a small, readable tail of divergent sessions rather than in general drift, and the overall correlation rises to 0.811 when only the severe divergences are excluded and to 0.914 when the full divergent tail is excluded. The axes are also highly collinear, and adding them to the overall score does not improve prediction of the customer's rating, the decomposition's value is not incremental prediction but attribution and coverage. And, with greater coverage the picture of the data changes. Read on every contact rather than the few that return a survey, satisfaction is markedly lower than the survey reports (a full-census 2.91 against the surveyed 3.62 on a five-point scale). The promise of decomposed satisfaction as a methodology is the ability to identify more nuanced drivers of customer experience in conversational data.

---


### 121. [Flout at Your Own Risk: LLMs Struggle with Pragmatic Cooperativity Under Epistemic Asymmetry](https://arxiv.org/abs/2607.11053)

**<font color=#1a73e8>作者：</font>** Hannah VanderHoeven, Abhijnan Nath, Nikhil Krishnaswamy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fruitful collaborations rely on cooperative communications, including of contextual cues to incorporate into reasoning. The increasing use of LLMs in collaborative and agentic pipelines raises questions about the extent to which they exhibit these pragmatic capabilities, especially in scenarios where they may not have access to the same information as their collaborators. In this paper, we perform a novel investigation into the pragmatic reasoning capabilities of LLMs in a multi-party collaborative task under partial information conditions. We formalize a notion of collaborative epistemic asymmetry that explicitly connects objective task success to Grice's cooperative principle and empirically assess various LLMs' abilities to act cooperatively as both speakers and listeners, including both prompting and post-training strategies. Our results show that while LLMs exhibit certain pragmatic capabilities in collaborative settings, and these can be elicited through prompting and post-training, they still face challenges in pragmatic communication with incomplete information, and that certain failure modes do correlate with floutings of Grice's maxims that go unrecognized.

---


### 122. [MJ: Multi-turn LLM Jailbreaking via Decomposed Credit Assignment](https://arxiv.org/abs/2607.11070)

**<font color=#1a73e8>作者：</font>** Junyoung Park, Namgyu Park, Sechan Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern large language models (LLMs) operate in interactive multi-turn settings, making multi-turn jailbreaking a realistic threat model and an important setting for automated red teaming. A core challenge in learning multi-turn jailbreak attackers is credit assignment: different turns contribute differently to the final outcome, yet existing learning signals are often too coarse to identify their individual contributions. We propose decomposed credit GRPO (DC-GRPO), a unified turn-level credit assignment framework for Group Relative Policy Optimization in multi-turn jailbreak learning. DC-GRPO assigns a separate group-relative learning signal to each turn by combining immediate and future credit, avoiding the credit misassignment induced by broadcasting a single trajectory-level score across the dialogue. We instantiate this framework with static and dynamic weighting rules that differ in how the two credit sources are balanced while sharing the same turn-level structure. Across multiple victim LLMs and benchmarks, the dynamic- and static-weighted variants achieve average ASR5@3 scores of 98.26% and 97.88%, respectively, substantially outperforming the state-of-the-art methods, including SEMA (86.58%) and TROJail (86.23%). Their consistently strong performance indicates that the central empirical benefit comes from turn-level group-relative credit assignment rather than a particular weighting rule. Warning: This paper contains examples of harmful content.

---


### 123. [ResearchQA: Benchmarking Citation-Grounded Question-Answering on Scientific Papers](https://arxiv.org/abs/2607.11074)

**<font color=#1a73e8>作者：</font>** Saba Imran, Debanjum Singh Solanky  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used to assist scientific reading, but existing evaluation methods often fail to detect whether answers are supported by verifiable citations. We introduce ResearchQA, a benchmark of 6,211 single-paper question-answer pairs from 494 open-access papers spanning eight domains and four question types: lookup, comprehension, multi-hop, and adversarial. ResearchQA is designed for citation-grounded evaluation: it permits multiple valid supporting passages for a claim and rewards grounded refusal when the source paper does not support an answer. We evaluate eight leading closed- and open-weight models in a citation-grounded chat-with-paper setting using a deterministic citation matcher and an LLM-based rubric evaluator. Citation-based metrics separate systems more clearly than LLM-evaluator scores: section coverage and citation accuracy vary substantially across models, while evaluator scores remain tightly compressed. We further find that open-weight models approach the best closed-model citation accuracy while achieving 3 to 6 times lower per-example latency. We release the benchmark, evaluation harness, and evaluator prompt.

---


### 124. [Do Video-LLMs Actually Watch? Diagnosing Character-Tracking Failures in Long-Form Video](https://arxiv.org/abs/2607.11078)

**<font color=#1a73e8>作者：</font>** Mohammad Al-Ratrout, Shayla Sharmin, Aditya Raikwar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Can a Video Large Language Model (Video-LLM) follow one person through a long video, keeping track of who they are well enough to report, in order, how their outfit changes across a full TV episode? Benchmarks increasingly score this kind of task, and the strongest open-source 7--8B models now reach 37--38% on InfiniBench's global appearance task, which asks exactly that. But does that score come from tracking the named character, or from something easier? We test this with a nine-condition diagnostic protocol applied to three architecturally distinct open-source Video-LLMs, with Gemini~2.5~Flash as a frontier reference, and find the accuracy does not come from character tracking. When we change the character named in the question to a different cast member, leaving the video and answer options untouched, the models change their answer only 4--31% of the time, so they are largely ignoring who the question asks about. Breaking that test down by the gender of the swapped name shows why: the models react more when the name is changed to a different-gender character than to a same-gender one (a 13--28 point gap), picking up coarse gender cues but unable to tell same-gender individuals apart. This shallow processing surfaces again when we drop the multiple-choice options and ask the same questions open-endedly: open-source accuracy drops 18--25 points, with none of 151 answers fully correct, versus a 12-point drop for Gemini. Further checks rule out the obvious innocent explanations, adding subtitles, using the most informative frames, or doubling the number of frames all leave character tracking unimproved, so the bottleneck is not how much video the model sees but how it ties that video to the person the question names. We release a diagnostic toolkit for auditing what such benchmark scores actually measure.

---


### 125. [Are LLMs Ready for Scientific Discovery? A Capability-Oriented Benchmark for AI Scientists](https://arxiv.org/abs/2607.11079)

**<font color=#1a73e8>作者：</font>** Chuhan Shi, Xiaoquan Ren, Sicheng Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing benchmarks for scientific data analysis evaluate LLMs primarily on code execution or workflow completion, overlooking that scientific analysis serves to support distinct types of scientific claims: hypothesis exploration, statistical inference, mechanistic explanation, each with different assumptions and validity criteria. We introduce SDABench, a benchmark that reorganizes evaluation around six capabilities (descriptive, exploratory, inferential, predictive, causal, and mechanistic) across five domains (Biology, Chemistry, Environment, Geography, Physics). SDABench comprises 527 real-data instances (SDA-Real) and 6000 synthetic instances (SDA-Synth), each in both multiple-choice and open-ended formats, constructed through an automated pipeline. Evaluating 15 representative LLMs, we find that models handle descriptive analysis well but degrade sharply on tasks requiring assumption selection, latent-process modeling, or mechanistic reasoning. SDABench further provides a five-stage error analysis framework that locates where LLMs fail: more advanced models more reliably identify the relevant scope and variables, but still struggle to select appropriate analytical procedures, model variable relationships, and draw valid conclusions.

---


### 126. [OS-Pruner: Pruning Chains-of-Thought of Reasoning Models via Optimal Stopping](https://arxiv.org/abs/2607.11089)

**<font color=#1a73e8>作者：</font>** Mohammed Ehab, Aymane El Gadarri, Vivek F. Farias 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have achieved remarkable success in complex reasoning tasks through Chain-of-Thought (CoT) prompting. However, these models often exhibit "computational overthinking," generating redundant reasoning steps that increase latency and cost without improving accuracy. Recent studies suggest that CoT trajectories can be significantly pruned, yet existing methods often rely on forcing a static thinking budget, heuristic filtering, sub-optimal early exit via classification, or expensive re-training. In this paper, we introduce OS-Pruner, a lightweight plug-in framework that formulates chain-of-thought pruning as an optimal stopping problem. Given a reasoning prefix, OS-Pruner learns whether further reasoning is worth its token cost by optimizing an explicit utility that trades off final-answer accuracy against generated length. Our novel formulation enables the model to dynamically assess the sufficient point of termination for a reasoning chain. OS-Pruner is designed to be lightweight during both training and inference, and to provide users with fine-grained control over the reasoning-effort vs. accuracy trade-off. On diverse reasoning benchmarks and base models, OS-Pruner achieves 20-60\% reduction in generation length with minimal accuracy sacrifice.

---


### 127. [Beyond the Eye: Efficient Multimodal Reasoning via Self-Regulated Implicit Visual Tools](https://arxiv.org/abs/2607.11106)

**<font color=#1a73e8>作者：</font>** Xiuwei Chen, Quanlin Chen, Wentao Hu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent multimodal large language models (MLLMs) have made remarkable progress on fine-grained perception tasks under the "Thinking with Images" (TwI) paradigm by iteratively performing various visual tool operations. However, this paradigm relies heavily on frequent external tool calls and repeated image re-encoding, which leads to substantial computational overhead and inference latency. To address these issues, we propose Beyond the Eye (BEE), a novel implicit visual tool paradigm centered on self-regulated capability. BEE directly incorporates visual tool invocation behaviors into the training objective and encourages the model to develop a self-regulated invocation mechanism. This design enables the model to adaptively balance internal knowledge and implicit tools, avoiding redundant tool usage while substantially reducing inference latency. Specifically, BEE involves a two-stage training process: (1) Formalized Chain-of-Thought (CoT) Supervised Fine-tuning (SFT). We construct CoT trajectories with structured tool slots and mixed invocation states. This stage activates the model's implicit tool representations and adaptive switching capability. (2) Self-regulated Reward-Driven Alignment. To address redundant tool usage caused by ambiguous cognitive boundaries, we first introduce the Net Tool Gain (NTG) metric to quantify this phenomenon. Based on this observation, we further propose a self-regulated reward mechanism. This mechanism penalizes ineffective tool dependency and encourages the model to perform knowledge routing, ensuring that implicit tools are invoked only when the model's internal knowledge is insufficient. BEE achieves state-of-the-art performance in fine-grained visual perception while remaining competitive in general reasoning tasks and achieving substantial gains in inference efficiency.

---


### 128. [ToolAtlas: Learning Once, Reusing Everywhere with Tool-Side Memory](https://arxiv.org/abs/2607.11126)

**<font color=#1a73e8>作者：</font>** Yue Fang, Zhibang Yang, Fangkai Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly rely on external tools served by shared providers and accessed by heterogeneous downstream agents. Existing approaches improve tool use on the agent side through parameter updates, prompt refinement, or agent-side memory, making tool knowledge difficult to share and limited to behaviors observed in past tasks. We argue that reusable tool knowledge should instead be maintained by the tool provider. We introduce ToolAtlas, a graph-based framework that builds a persistent provider-side tool memory of tool capabilities, failure boundaries, and cross-tool compositions through execution-verified probing. At inference time, agents query the tool memory via adaptive graph traversal. Across two MCP-based benchmarks spanning eight services, ToolAtlas outperforms existing tool-side optimization and agent-side memory baselines by up to 21.61% in pass@1 and 18.61% in pass@4. The same tool memory also transfers across environment instances and agent frameworks without retraining or task-time exploration, yielding up to 24.16%/16.22% and 17.49%/14.27% relative gains in pass@1/pass@4, respectively. Ablation studies show that these gains arise from combining tool-centered memory organization with capability-guided execution probing. These results establish provider-side tool memory as an effective and reusable paradigm for tool servers. Our code is in: this https URL.

---


### 129. [Do LLMs Fabricate Legal Citations? A Bilingual Benchmark on Saudi Data Protection Law and the GDPR](https://arxiv.org/abs/2607.11127)

**<font color=#1a73e8>作者：</font>** Noura Suliman Alrajeh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Organizations and regulators increasingly consult large language models (LLMs) for regulatory-compliance questions, yet a wrong statutory citation can silently propagate into legal advice, compliance documentation, and policy decisions. We introduce a bilingual benchmark of 120 questions probing whether freely accessible LLMs fabricate article citations for two data-protection instruments: the EU General Data Protection Regulation (GDPR) and the Saudi Personal Data Protection Law (PDPL). The benchmark pairs direct citation retrieval questions with false premise verification probes and deliberately unanswerable "trap" questions -- including questions about a repealed article and about deadlines that exist only in implementing regulations, not in the law itself. Every question is posed in both Arabic and English, and all scoring is fully automatic against a manually verified gold reference. Evaluating three freely accessible models (Gemini 2.5 Flash, GPT-OSS-120B, Nemotron-3-Super-120B), we find a dramatic jurisdiction gap: near-ceiling citation accuracy on the GDPR (94-100% on direct retrieval) against majority fabrication on the Saudi PDPL (60-77%), invariant to query language; the highest fabrication rates (67%) arise from statute-vs-regulations confusion, and 91% of fabricated citations are asserted with confidence >= 0.8. Fabrication tracks the jurisdiction of the law, not the language of the query, and model confidence provides no protection -- indicating that verbatim-verification safeguards, rather than model self confidence, must gate any institutional reliance on LLMs for compliance screening.

---


### 130. [TIGER: Text-Conditioned Visual Gated Routing with Acceptance Alignment for Multimodal Speculative Decoding](https://arxiv.org/abs/2607.11131)

**<font color=#1a73e8>作者：</font>** Quynh Vo, Cong-Duy Nguyen, Ponhvoan Srey 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates autoregressive generation by letting a lightweight drafter propose multiple tokens that are verified by a larger target model. Although effective for text-only LLMs, speculative decoding yields limited gains in VLMs because drafters often diverge on vision-critical content, while existing multimodal acceleration methods do not directly address irrelevant visual evidence or optimize the verifier-accepted prefix length that governs speedup. We propose TIGER, a Text-conditioned vIsual GatEd Routing framework for multimodal speculative decoding. TIGER dynamically selects a sparse set of context-relevant visual tokens based on the drafter's current textual state, rather than expose the full visual token set or a fixed compressed interface. To better align training with inference-time efficiency, we optimize the drafter with acceptance-aligned group-based policy training using verifier-derived rewards based on accepted prefix length, built on top of distillation warm start with KL anchoring. This encourages the drafter not only to imitate the target model, but also to produce speculative continuations that survive verification for longer prefixes. Experiments show that TIGER yields consistent gains in accepted prefix length and speculative speedup under exact verifier-side speculative decoding, while achieving favorable quality-latency trade-offs with comparable downstream accuracy in visual-routing analyses.

---


### 131. [A Formal Hierarchical Architecture for Agentic Orchestration with Stack-Based Execution and Lazy Discovery](https://arxiv.org/abs/2607.11138)

**<font color=#1a73e8>作者：</font>** Prashant Devadiga, Abhishek, Adithya Mishra 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid expansion of capabilities in Large Language Model (LLM) agents has exposed a critical architectural bottleneck: when agents are given access to a flat, monolithic registry of tools, the model must evaluate hundreds or thousands of options simultaneously. This leads to decision-space explosion, context window saturation, and degraded routing accuracy. To address these limitations, this paper presents a hierarchical, skill-based architecture for agentic orchestration. Capabilities are organized as a rooted tree where internal nodes make routing decisions and leaf nodes execute deterministic tasks. The runtime enforces a single-step execution loop governed by a Last-In-First-Out (LIFO) stack, giving the agent a form of memory akin to a Pushdown Automaton, therefore enabling it to track nested execution contexts and resume deterministically from any depth. Capability discovery follows a manifest-driven, lazy-loading protocol: only the immediate children of the active node are loaded, so memory and prompt costs scale with the explored path rather than the global registry. By replacing global memory with localized stack frames, the architecture prevents outputs from one execution branch from leaking into another, establishing the isolation guarantees required for deployment in regulated enterprise environments. We also discuss UPI Help, an AI-powered digital payments support product, as a motivating production deployment context. We provide a mathematical formalization of the orchestration state, detailed algorithmic analysis of the execution loop, and controlled benchmarks comparing flat and hierarchical routing under increasing tool catalogs, multi-step workflow pressure, and visible schema-token exposure per LLM call.

---


### 132. [NextFund: A Unified Performance Tracking Platform for Agentic Portfolio Management](https://arxiv.org/abs/2607.11141)

**<font color=#1a73e8>作者：</font>** Changlun Li, Peixian Ma, Qiqi Duan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) based agents are beginning to participate in portfolio construction and market analysis, where decisions must be justified under evolving information and risk constraints. Current assessment practice, however, remains poorly aligned with this setting: many studies rely on static examinations or report only terminal portfolio returns, while the intermediate evidence, analyst judgments, and execution steps that produced those returns stay largely invisible. We introduce NextFund, an evaluation platform that makes financial-agent behavior observable under live market conditions. The platform couples time-consistent market access, coordinated multi-agent analysis, and persistent logging of the full decision path from observation to trade. Through an interactive Trading Arena, users can compare models across markets, inspect equity curves, and drill from leaderboard outcomes down to individual justifications. We present NextFund on Hong Kong, U.S., and China A-share equities, illustrating how inspectable decision histories enable fairer benchmarking and more actionable diagnosis. Our demo is available at this https URL.

---


### 133. [The Hidden Footprint: Making Storage a First-Class Metric for LLM Agent Evaluation](https://arxiv.org/abs/2607.11149)

**<font color=#1a73e8>作者：</font>** Chenglin Yu, Hongquan Gui, Ying Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agent benchmarks measure task completion, reliability, and inference cost, but not the persistent data an agent run leaves on disk, including logs, context snapshots, checkpoints, and debug traces. We introduce AgentFootprint, a cross-framework benchmark of post-run agent storage footprint. Its serialization-aware metric suite measures total retention, channel composition, duplication, growth, compressibility, and conversation-history reconstructability. It addresses a measurement trap: naive byte-level measurement understates duplication by an order of magnitude because database paging and JSON escaping obscure repeated content. A fixed-trace control separates agent-generated logical volume from persistence-layer amplification: replaying the same trajectory through seven persisting frameworks yields a 6.7x spread. Under identical models, tools, and tasks, configurations with 100% accuracy differ by 15.7x in retained bytes, although their defaults support different recovery and audit capabilities. Three full-history configurations grow superlinearly on a repeated-observation stress task. Exported trajectories from 108 instance-normalized SWE-bench Verified submissions span three orders of magnitude per instance, with no detectable correlation with resolve rate. A content-addressed store reduces retention by 4.8x-32.7x while preserving every reconstructability score. These results establish persistent storage as a resource metric to report jointly with accuracy and reconstructability.

---


### 134. [SISA-Rec: A Semantically Integrated Sequential Recommender with Contrastive Alignment](https://arxiv.org/abs/2607.11168)

**<font color=#1a73e8>作者：</font>** Soohan Abbasi, Shahid Munir Shah, Rafia Shaikh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recommendation systems help users recommend relevant items from a large collection of choices. Present work on transformer-based sequential recommendation learns user preferences from interaction logs, but it mostly focuses on item identifiers and doesn't fully use the semantic meaning of items. This limitation becomes a major challenge in sparse and cold-start scenarios where historical interaction data is limited. To solve this problem, we introduce SISA-Rec (Semantically Integrated Sequential Recommendation), a transformer-based framework that embeds semantic context directly into sequential modeling. Our approach fuses item ID embeddings with BERT-based text embeddings via a gated fusion module, injects semantic similarity into the self-attention mechanism, and leverages an attention-based aggregation module to construct comprehensive user representations. Finally, a joint learning objective which combines Bayesian Personalized Ranking (BPR) and contrastive alignment loss, aligns the underlying behavioral and semantic spaces. Experiments were conducted on the two highly sparse Amazon Beauty and Amazon Toys \& Games datasets, both having 99.93\% sparsity. The results show that SISA-Rec outperforms state-of-the-art baseline models across all evaluation metrics. Compared with the BERT4Rec \cite{petrov2022systematic}, SISA-Rec improves HR@10 by 16.6\% and NDCG@10 by 10.3\% on Amazon Beauty, and HR@10 by 23.1\% and NDCG@10 by 17.9\% on Amazon Toys \& Games. Cold-start analysis further shows that the proposed model achieves the largest improvements for users with limited interaction historical records. This showcases the value of semantic information when user behavior data is scarce. Overall, the results demonstrate that integrating semantic information into the attention mechanism leads to more accurate and reliable recommendations.

---


### 135. [TC-MAF: Train-Calibrated Bounded Multi-Evidence Fusion for Multimodal Industrial Anomaly Detection](https://arxiv.org/abs/2607.11170)

**<font color=#1a73e8>作者：</font>** Ming Deng, Sijin Sun, Xiaochuan Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal anomaly detection benefits from complementary RGB and 3D evidence, yet auxiliary RGB reconstruction is not equally reliable across product categories and class-wise test-time policy selection is usually unavailable. We propose TC-MAF, a base-anchored multi-evidence fusion design that combines a multimodal detector, complementary Dinomaly evidence, and a small cross-modal consistency cue under one fixed pixel-level fusion formula. A lightweight training-dispersion confidence (TDC) term scales auxiliary participation using only normal training statistics. On MVTec-3D, TC-MAF reaches 0.979 image-level AUROC and 0.990 pixel-level AUPRO, achieving the best mean results on both detection and localization among the compared multimodal methods. Systematic ablations show that the fusion structure itself is the dominant factor, while TDC provides a smaller but reproducible calibration gain over no calibration or arbitrary calibration. Additional experiments show that the same design remains effective under a pooled-statistics variant, auxiliary-branch and backbone substitutions, few-shot settings, a missing-3D setting, and cross-dataset evaluation on Eyecandies. Code is available at this https URL.

---


### 136. [Amplitude-Only FFN Intervention for Tool-Structured LLM Inference Method: Gated Evaluation Protocol, and Cross-Model Empirical Results](https://arxiv.org/abs/2607.11183)

**<font color=#1a73e8>作者：</font>** Sheng Xu, Boyuan Huang, Ke Jia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly operate as tool-using agents, where small format, argument, or function-call errors can invalidate otherwise plausible responses. We study inference-time feed-forward network (FFN) intervention for improving structured outputs without retraining model weights. Our project began with Orthogonal Residual Projection (ORP), a direction-changing repair attempt that revealed sensitive SwiGLU FFN intervention sites but often caused more harm than fixes. We therefore propose Amplitude Gating (AG), a non-destructive alternative that preserves pretrained FFN weight directions and modulates only activation magnitudes during generation. We define a fine-grained intervention system spanning P1/P2/P3 and branch-specific P1s/P2a/P2b sites, and introduce an evaluation protocol that separates combination-oracle headroom from fixed configurations and learned gates, enforces sample-level accounting, and uses task-aware metrics for binary and partial-credit datasets. Across Qwen3.5-9B, Qwen3-8B, and Qwen2.5-7B, AG is weakly positive in aggregate but strongest on tool-structured tasks. On Qwen3.5-9B, a category-level learned gate improves tool/structured/agentic performance from 38.66% to 42.92% (+4.27 percentage points), with Hermes function-call tasks reaching about +7.6 points. On Qwen3-8B, Hermes JSON mode improves by +11.36 points. Qwen2.5-7B retains oracle headroom but current learned gates fail to capture it, showing that deployment requires model- and category-specific routing. Comparisons of entropy AG with Newton-Schulz-windowed AG show that neither family is uniformly dominant. These results identify tool-structured inference as the most credible first target for safe FFN-level inference optimization, while prospective online validation and broader cross-model evaluation remain necessary.

---


### 137. [GDP.pdf: Benchmarking Grounded Multimodal Reasoning over Professional PDF Documents](https://arxiv.org/abs/2607.11192)

**<font color=#1a73e8>作者：</font>** Suhaas Garre, Emily Ritchie, Sushant Mehta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A large share of day-to-day work in professional domains happens inside PDF files: benefits packets, leases, datasheets, clinical guidelines, construction plans. Benchmarks for document AI have generally measured the required capabilities in isolation: OCR, layout analysis, chart reasoning, table QA, document VQA. A high score on any one of them does not necessarily reveal whether a model can answer a realistic question that someone in the field would actually ask about a specific PDF. this http URL is a benchmark built to measure this directly. It consists of question-document pairs authored by working professionals in ten fields, and a candidate question was kept only when at least two frontier multimodal models failed it in a way that mattered: a wrong answer, missed decisive evidence, or a fabricated claim, rather than a superficial difference such as style. Each item comes with a rubric of atomic criteria, so we can report a graded rubric score as well as a strict task-level pass rate, and each item is tagged against a taxonomy of eleven capabilities in three tiers, spanning text extraction and grounding, table and chart comprehension, cross-referencing, spatial reasoning, and abstention on unsupported queries. We evaluated seven frontier models on the 100-item benchmark. The best model passed only 15% of the items and the worst passed 1%. Most errors trace back to a small set of recurring loss patterns: misaligned tables, misread charts, skipped footnotes and exclusions, miscounted floor-plan symbols, scan noise, and amendments that supersede earlier text. The full 100-item benchmark is publicly available at this https URL

---


### 138. [What We Talk About When We Talk About LLM Planning: Evidence for Two Distinct Planning Abilities](https://arxiv.org/abs/2607.11197)

**<font color=#1a73e8>作者：</font>** Sukai Huang, Chenyuan Zhang, Fucai Ke 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When LLMs exhibit uneven performance across planning tasks, these gaps are often attributed to task difficulty. We argue that this explanation is incomplete, as task-level variation may reflect distinct latent planning competencies rather than differences along a single ability spectrum. We study this question on ACPBench-Hard by evaluating multiple LLM families under varying test-time reasoning budgets and applying a multidimensional item response theory model to uncover the latent competency structure underlying LLM planning. The analysis reveals two principal dimensions that shape planning performance: operational reasoning, the ability to evaluate local action applicability and immediate state transitions, and structural enumeration, the ability to reason about goal reachability and landmark structure. Operational reasoning improving under model scaling and longer reasoning traces, while structural enumeration remains comparatively insensitive. Our findings motivate competency-level evaluation of LLM planning, shifting the focus from whether models improve overall to which planning competencies improve, under what conditions, and why.

---


### 139. [DynEval: Holistic Evaluations of T2I Generative Models in the Wild](https://arxiv.org/abs/2607.11199)

**<font color=#1a73e8>作者：</font>** Shyam Marjit, Dheeraj Baiju, Anuj Shikarkhane 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in text-to-image (T2I) generation have led to models capable of producing highly realistic images. Yet, reliably evaluating their outputs remains challenging, especially at scale. Existing automatic evaluators, often relying on a static prompt set, struggle to capture subtle failure modes such as partial prompt misalignment, compositional errors, or visually plausible but semantically incorrect generations. In this work, we introduce DynEval, a Dynamic Evaluation framework designed to jointly assess text-to-image alignment and image quality of T2I models. To support scalable training beyond limited human-annotated data, we construct two large datasets. First, we build GenDB, a collection of 500K prompt-image pairs generated from human-written prompts drawn from DiffusionDB using a tiered prompt-model generation strategy. Second, building upon GenDB, we construct DynEvalInstruct, a 250K instruction dataset comprising prompt-image-response triplets distilled from a structured evaluation pipeline that decomposes evaluation into text-image alignment and visual quality reasoning. Using this dataset, we perform full fine-tuning of a compact evaluator through a curriculum learning strategy to effectively distill the superior evaluation capabilities of a larger teacher vision-language model, resulting in DynEval-2B and DynEval-4B. In extensive comparisons against existing evaluators across 11 benchmarks, our evaluator achieves a higher overall correlation with human judgments. Furthermore, it provides fine-grained analysis of the capabilities and failure modes of 36 T2I models across 42 subcategories and 9 semantic dimensions.

---


### 140. [ProgramTab: Boosting Table Reasoning of LLMs via Programmatic Paradigm](https://arxiv.org/abs/2607.11207)

**<font color=#1a73e8>作者：</font>** Pei Guo, Enjie Liu, Yunzhi Tan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Table-based reasoning with large language models (LLMs), which requires reasoning based on natural language questions and structured tabular data, has gained widespread attention. However, a series of issues still constrain the application of this task. The previous approaches suffered from significant performance degradation when faced with large tables due to the difficulty of long text modeling and the limitation of input length for LLMs. The text-to-SQL approach is used to efficiently extract key information from tables and generate smaller sub-tables. However, tabular data, especially web tables, often lack the necessary structure and consistency, making them unsuitable for performing mathematical logic operations using SQL queries. We propose the ProgramTab framework, which guides LLMs employing in-context learning to perform tabular data preprocessing with Python code, as well as the momentous contents extraction with row and column extraction and SQL generation. The experiment results on table reasoning datasets demonstrate that the ProgramTab framework effectively deals with table-based reasoning tasks and outperforms all LLM-based baselines.

---


### 141. [FastTPS: An Optimized Method for LLM Token Phase for AI accelerators](https://arxiv.org/abs/2607.11211)

**<font color=#1a73e8>作者：</font>** Wenzong Yang, Danyang Zhang, Kun Cao 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The popularity of large language models (LLMs) escalates an ongoing demand for effective inference. However, due to the sequential processing of tokens during the token phase in decoder-only LLMs inference, the inherent low parallelism leads to reduced throughput and suboptimal utilization of the computing units on artificial intelligence (AI) accelerators, particularly when handling long-sequence inputs that impose significant memory overhead. Recently, many reported methods have been developed as potential solutions, since they emerge with numeric deviation. This paper presents FastTPS, a high performance and low-precision loss method for accelerating the token-phase in LLM inference on general AI accelerators which includes three key components: (1) AI accelerator-enabled reloading-free KV Cache concatenation which decreases memory access overhead as well as enables full fusion of Attention, (2) high-efficiency and high-accuracy 'RoPE' attention based on the tiling optimized FLAT, and (3) highly-fused MLP with fine-grain pipeline scheduling. Our results confirm that FastTPS significantly alleviates memory bottlenecks in the token phase, delivering a 6x speed improvement (compared to none-fusion) on an AMD Ryzen AI 300 series NPU with BF16 precision while sustaining 93% peak memory bandwidth utilization during Phi3-mini-4k-instruct inference.

---


### 142. [Multi-Agent LLMs Fail to Explore Each Other](https://arxiv.org/abs/2607.11250)

**<font color=#1a73e8>作者：</font>** Hyeong Kyu Choi, Jiatong Li, Wendi Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Exploration is essential for reliable autonomy in multi-agent systems, yet it remains unclear whether large language model (LLM) agents can explore effectively when interacting with one another. We show that modern LLM agents fail to do so, often exhibiting myopic and polarized interaction patterns that lead to suboptimal coordination and increased regret. We formalize this challenge as the Multi-Agent Exploration problem, modeling it as a partially observable stochastic game (POSG) problem in which agents must probe peers to infer their capabilities and identify effective interaction strategies. To address this, we introduce Multi- Agent Contextual Exploration (MACE), a lightweight framework that explicitly promotes exploration through structured peer selection. Across both contextual and parametric diversity settings, MACE substantially improves exploration behavior and downstream task performance. We further show theoretically that the value of exploration increases with agent diversity. Overall, our results highlight a fundamental limitation of current LLM agents and underscore the importance of explicitly guided exploration for reliable multi-agent autonomy. Code will be released in this https URL

---


### 143. [LaGuadia: Language-Guided Adaptive Distillation from Pathology Foundation Models](https://arxiv.org/abs/2607.11257)

**<font color=#1a73e8>作者：</font>** Gangsu Kim, Won-Ki Jeong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathology Foundation Models (PFMs) offer powerful Whole Slide Image (WSI) representations but suffer from massive computational costs. While Knowledge Distillation (KD) can create efficient student models, existing multi-teacher methods often use suboptimal uniform weighting that ignores tissue heterogeneity. We propose LaGuadia (Language-Guided Adaptive DistillAtion), a framework that develops a compact pathology image encoder by dynamically integrating expertise from multiple PFMs under clinical linguistic guidance. Our approach utilizes a multi-stage pipeline: first, extracting visually observable clinical keywords from pathology reports; second, aligning visual features with these keywords via a Vision-Language meta-teacher (MedSigLIP) to provide dense semantic guidance; and finally, performing adaptive KD where teacher contributions are weighted based on their semantic alignment with the clinical narrative. Experiments on WSI captioning, visual question answering, and slide-level classification tasks demonstrate that an 87M parameter LaGuadia student model matches or exceeds foundation-scale models such as GigaPath and UNI, achieving strong factual consistency and robust generalization. These results highlight clinical language as an effective semantic anchor for building efficient and reliable digital pathology systems. Code is available at this https URL.

---


### 144. [TreeThink: A Modular Tree Search Library for Mathematical Reasoning with LLMs](https://arxiv.org/abs/2607.11258)

**<font color=#1a73e8>作者：</font>** Burak S. Akbudak, Zeynel A. Uluşan, Can S. Erer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tree search algorithms enable systematic exploration of the proof space in neural theorem proving. Existing LLM tree search libraries primarily target natural language reasoning and do not provide native integration with formal verifiers, while theorem proving systems often rely on task-specific search implementations. We introduce TreeThink, an open-source Python library for modular, fully asynchronous tree search in neural theorem proving. It integrates established tree search methods with vLLM-based inference pipelines and diverse node evaluation techniques, ranging from lightweight heuristics to neural evaluators. We support Lean~4, Rocq, and Isabelle/HOL alongside natural language. It connects directly to each language's Read-Eval-Print Loop (REPL) server for real-time verification and proof state extraction. We evaluate TreeThink on miniF2F and MATH500, demonstrating cross-language formal proof search, natural language reasoning support, and up to 6.3$\times$ wall-clock speedup from asynchronous execution. Source code is released under the MIT license at this https URL , and the library is accessible as a downloadable package at this https URL .

---


### 145. [Automated Textbook Auditing with Multi-Agent LLM Systems](https://arxiv.org/abs/2607.11276)

**<font color=#1a73e8>作者：</font>** Ciprian Cristescu, Adrian-Marius Dumitran, Angela-Liliana Dumitran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ensuring the quality of educational materials requires more than standard proofreading: textbooks must be audited for factual accuracy, domain-specific technical correctness, and linguistic quality simultaneously -- a task that general-purpose grammar checkers cannot address. We present \textbf{AI Textbook Auditor}, a modular multi-agent pipeline for automated quality assurance of educational materials across subject domains. The system accepts a textbook PDF and produces a structured, human-reviewable report via two analysis tracks: a \textbf{Factual and Technical Track} in which an ensemble of specialized LLM agents detects factual inaccuracies, code errors, incorrect definitions, and conceptual inconsistencies, augmented with web search for humanities domains; and a \textbf{Grammar Track} operating PDF-natively to preserve diacritical encoding. A \textbf{Judge Agent} filters false positives using domain-specific rules before presenting findings to a human reviewer. The pipeline supports two ingestion modes -- vision-native page rendering and PyMuPDF text extraction -- and is domain-adaptable via custom prompts encoding subject-specific error taxonomies. We demonstrate the system on two Romanian upper-secondary textbooks: a CS textbook (56 technical findings across seven categories, with an expert-validated precision of 62.5\%) and a history and social sciences textbook (72 findings spanning factual errors, ideological bias, and grammar). The system is designed as a triage tool that reduces the manual effort of locating candidate issues, with human expert validation required before any editorial action.

---


### 146. [A Unified Framework for Comprehensive Cardiac CT Segmentation and Phenotyping: Human-in-the-Loop Data Annotation, Vision Foundation Model Development, Multicenter Evaluation and Clinical Validation](https://arxiv.org/abs/2607.11287)

**<font color=#1a73e8>作者：</font>** Pooya Mohammadi Kazaj, Leo Fridolin Weber, Wen Xie 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Comprehensive quantification of cardiac structures from computed tomography (CT) remains limited not by data availability but by the scalability of measurements, which makes routine use impractical. Here we present a unified framework for comprehensive cardiac CT segmentation and phenotyping that combines a human-in-the-loop annotation pipeline, a cardiac CT augmentation technique, and a self-supervised foundation model pre-trained on 60,000 unlabeled cardiac CT scans. Using this approach, we assembled the largest and most comprehensive expert-annotated cardiac CT segmentation dataset to date, comprising 1598 cases and 14 distinct cardiac structures (1000 for training, 598 for the external test set). Across five external datasets, the framework segmented all structures more accurately and comprehensively than existing open-source tools. Self-supervised pre-training improved labeling efficiency, with the most significant gains observed during external evaluation in the low-data regime. Benchmarking across convolutional, transformer, and state-space architectures showed comparable performance, indicating that data quality and pre-training, rather than architecture, drove accuracy. The framework was scaled to population-level phenotyping, with segmented anatomy that carries functionally relevant information about ventricular function and disease severity beyond demographic variables. By openly releasing the largest dataset with human labels, code, model weights, a CT augmentation library, and software, this work provides a reproducible foundation for opportunistic cardiac phenotyping from routinely acquired CT scans.

---


### 147. [SLVMBench: Skill Learning from Video Memory](https://arxiv.org/abs/2607.11312)

**<font color=#1a73e8>作者：</font>** Yudong Yang, Guangzhi Sun, Yixuan Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Skill Learning from Video Memory (SLVMBench), the first benchmark that jointly evaluates whether video large language models (video-LLMs) can learn skills from long video memory and apply them to real-time tasks. SLVMBench presents models with 2-3 hour video streams that contain a tutorial video embedded in a stream of arbitrary irrelevant videos, resembling real-world human learning practices. Video-LLMs are asked to apply the acquired skill to answer real-time questions about an ongoing video. Unlike long-video understanding benchmarks that emphasize passive comprehension and skill-learning benchmarks that rely on short, immediate demonstrations, SLVMBench tests the full pipeline of memorizing and extracting procedural knowledge, as well as transferring it to real-time tasks. Moreover, rigorous human annotations feature sub-second-level temporal calibration, manually engineered questions eliminating common-sense guessing, and collated tutorials to ensure coverage of the required skills. Evaluations on state-of-the-art proprietary and open-source video LLMs show that video-LLMs struggle substantially with learning and applying skill knowledge from videos. Moreover, performance degrades markedly when the skill knowledge is placed within a long video memory. These results reveal a key limitation of existing video LLMs and position SLVMBench as the first benchmark for studying real-time skill acquisition and application from long-context video memory.

---


### 148. [Calibrated e-CUSUM Decoding for Quantized Reasoning Models: Why Token Log-Probability Is the Wrong Observable for Decoding Monitors](https://arxiv.org/abs/2607.11317)

**<font color=#1a73e8>作者：</font>** El Hassane Ettifouri, Ayoub Belfatmi, Mahaman Sanoussi Yahaya Alassan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Low-bit quantization makes small reasoning models inexpensive to deploy but can degrade their chains of thought. This motivates decoder-side monitors that intervene when generation becomes unreliable. We show that a natural candidate, the centered token log-probability increment $\log p(w_t)+H_t$, is the wrong observable for this purpose. Under the model's own sampling law it is a mean-zero martingale by construction, so it measures sampling self-consistency rather than trajectory health and is nearly silent during confident repetition, where both $\log p(w_t)$ and entropy are close to zero. We introduce a training-free decoding controller that combines (i) a degeneration-aware alarm score fusing token uncertainty with explicit verbatim repetition and (ii) a calibrated e-process-inspired sequential detector. The raw product process is Ville-valid under a conditional-mean null, while the deployed CUSUM-floored statistic is treated as an empirical change detector because the score is history-dependent and autocorrelated. On GSM8K with DeepSeek-R1-Distill-Qwen-1.5B in FP16 and INT4, calibration turns a monitor that fires on 93--95% of generations into a selective detector of failing traces ($\phi \approx 0.3$, precision $\approx 0.6$ against a 0.38 base rate). In this pilot, the controller reduces measured verbatim-degeneration signals and yields a positive but statistically inconclusive INT4 accuracy change from 63% to 69% (paired McNemar $p=0.18$, $n=100$), at a 28% token-budget cost. We also find that non-termination, rather than looping, is the dominant failure mode on GSM8K. The main contribution is methodological: an explanation of why centered token log-probability is inadequate for decoder monitoring and a calibrated, cautiously evaluated replacement.

---


### 149. [PRISM Edit: One Vector for All Temporal Answers](https://arxiv.org/abs/2607.11327)

**<font color=#1a73e8>作者：</font>** Chen Huang, Qi Zheng, Ruiqin Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model editing keeps large language models (LLMs) up to date without retraining, but temporal facts expose a limitation of the prevailing locate-and-edit paradigm: an update is not always a replacement. When a fact changes, the new answer should become current while the old answer may remain correct in historical time contexts. Building on this insight, we use causal tracing to show that LLMs already support this distinction via a two-stage internal computation: early MLP layers retrieve a time-agnostic subject representation, and later layers modulate it with temporal context to yield the time-correct answer. Motivated by this finding, we introduce PRISM Edit, which optimizes a single polysemous representation across temporal contexts and leverages the model's inherent modulation pathway to route it to temporally correct predictions, without any architectural modification. We evaluate on TimeConflict, a new temporal editing benchmark we introduce, and on temporally augmented CounterFact. PRISM Edit improves over the best baseline by +23.3 Temporal Consistency (TC) and +33.7 Current Relative-time Score (CRS) on average while being more than 2x faster. Code and data are publicly available at this https URL.

---


### 150. [HierCAD: Hierarchical Text-to-CAD Design via Structure Alignment and Parameter Grounding](https://arxiv.org/abs/2607.11339)

**<font color=#1a73e8>作者：</font>** Jimin Xu, Tianbao Wang, Tao Jin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent text-to-CAD approaches have shown promising results by leveraging large language models, but they often struggle with maintaining structural consistency in complex designs and accurately grounding geometric parameters. To address these issues, we propose HierCAD, a hierarchical text-to-CAD framework that improves both structural reasoning and parameter prediction. HierCAD reformulates CAD generation as progressive reasoning by decomposing CAD construction trees into object-level procedural reasoning and part-level topology reasoning trajectories. To further improve generation fidelity, we introduce a unified Structure Alignment and Parameter Grounding (SAPG) learning strategy. Structure alignment aligns topology reasoning trajectories with their corresponding parametric CAD spans, while parameter grounding mitigates shortcut learning through structure-preserving parameter perturbations and ranking-based supervision. Experiments demonstrate that HierCAD outperforms prior state-of-the-art methods on both CAD sequence generation and reconstructed CAD model evaluation. Our code is available at this https URL.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-199](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
