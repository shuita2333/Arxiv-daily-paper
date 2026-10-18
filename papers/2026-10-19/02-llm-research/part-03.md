# 🧠 大模型相关研究 | 2026年10月19日

> 本类共 **321** 篇论文：已确认 **300** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-321](./part-07.md)

---

### 101. [FGSS-BO: Feedback-Guided Hypothesis Management for LLM-Based Bayesian Optimization](https://arxiv.org/abs/2610.21246)

**<font color=#1a73e8>作者：</font>** Hao Chen, Ziyang Ling, Ronald X. Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-guided Bayesian optimization (BO) uses past observations to guide search, but proposed directions and their revision can remain implicit. We propose Feedback-Guided Search State (FGSS), a structured hypothesis-management interface connecting language-based guidance to observed evidence, executable parameter interventions, and comparative support updates. An LLM reflector proposes and revises hypotheses; a deterministic curator validates them and maintains identities and test records. The evolving state guides candidate construction and priorities. Instantiated on LLAMBO, FGSS-BO retains its surrogate and default expected improvement selection, with a bounded testing policy. On two retrospective protocol/media tasks with nearest-neighbor response oracles, it attains higher sample mean final best and search AUC than the matched LLAMBO baseline and evaluated non-LLM baselines. Prose-reflection and EI-only controls show mixed component effects. Six direct-training hyperparameter-optimization tasks show task-dependent transfer, strongest on diabetes SVM; exact-grid and reaction controls examine other settings. FGSS exposes hypotheses, their execution, and cross-round revisions for inspection while supporting search gains in selected settings.

---


### 102. [FocusOPD: Structure-Guided On-Policy Distillation for Diffusion Models](https://arxiv.org/abs/2610.21250)

**<font color=#1a73e8>作者：</font>** Xinrui Lin, Shumin Wang, Suqi Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-teacher on-policy distillation enables rectified-flow models with diffusion-transformer architectures to combine task-specific capabilities within a single student. However, matching model outputs does not guarantee that their internal representations are aligned, and it remains unclear where and when additional feature supervision is most useful. We analyze the teacher-student feature mismatch across Transformer blocks and denoising timesteps, and find that the mismatch is concentrated in deeper Transformer blocks during early denoising and persists after OPD distillation, indicating ineffective distillation. Motivated by this observation, we introduce FocusOPD, which augments the base OPD objective with token-wise directional feature alignment restricted to deep layers and early denoising steps. Across two rectified-flow backbones and multiple OPD objectives, FocusOPD improves capability transfer in compositional generation, text rendering, and preference-based evaluation. On the primary benchmark, it improves over DiffusionOPD from 0.953 to 0.967 on GenEval, from 23.797 to 23.944 on PickScore, and from 6.052 to 6.199 on LAION-Aesthetic. Ablations show that selective deep and early supervision is more effective and efficient than alignment over the full network and trajectory.

---


### 103. [Do VLAs Really Follow Instructions? Diagnosing How-Level Instruction Following in Vision-Language-Action Models](https://arxiv.org/abs/2610.21251)

**<font color=#1a73e8>作者：</font>** Sangwu Park, Wonjoong Kim, Yeonjun In 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models are expected to follow instructions like their language backbones, yet prior work has focused on What-level instructions that specify the task rather than How-level instructions that specify how to carry it out. Through our diagnoses, we find that How-level instructions do not help current VLAs and lower task success. We hypothesize that pairing each training episode with a single instruction limits How-level instruction following, and show that training with segment-level enriched instructions makes actions respond to such instructions without consistently raising task success. To measure How-level instruction following beyond standard benchmarks, we introduce SIMPLER-IN, where success requires conditions given only in the instruction. It shows that the gained responsiveness does not extend to demanding or out-of-distribution How-level instructions. How-level instruction following thus remains an open challenge.

---


### 104. [LLM-Based Weak Annotation for Cybersecurity Tweet Classification: A Teacher-Student Framework](https://arxiv.org/abs/2610.21254)

**<font color=#1a73e8>作者：</font>** Ferry Afit Kurniawan, Kazushi Okamoto, Koki Karube 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cyber threat intelligence (CTI) relies on the timely identification of emerging threats, enabling organizations and security analysts to support situational awareness and decision-making. Social media platforms such as X (formerly Twitter) have become valuable CTI sources because vulnerabilities and attack activities are often discussed there before appearing in formal reports. However, the rapid growth of cybersecurity discussions on social media has created more content than domain experts can realistically review and annotate, making labeled data a major bottleneck for developing supervised learning approaches. While large language models (LLMs) have shown promise as weak annotators in other domains, their effectiveness for cybersecurity tweet classification and downstream training of domain-specific pre-trained language models (PLMs) remains underexplored. To address this challenge, we propose a Teacher-Student weak supervision framework in which a selected LLM serves as a Teacher to generate weak labels for unlabeled cybersecurity tweets, enabling the training of cybersecurity-specific PLMs without large-scale manual annotation. Experimental results show that PLMs trained solely on LLM-generated labels consistently achieve F1 scores above 0.92, remaining within 3 percentage points of fully human-supervised models across all evaluated architectures. These findings suggest that LLM-based weak annotation offers a practical alternative for constructing cybersecurity-specific training data when expert annotation resources are limited.

---


### 105. [Isolating a Language Model's Judgment with a Label-Free Subspace](https://arxiv.org/abs/2610.21256)

**<font color=#1a73e8>作者：</font>** Chaemin Jang, Donggyu Lee, Jeesoo Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models are often asked to make judgments: whether a proposed answer is correct, whether one statement follows logically from another, or whether a response is safe. Yet changing the instructions that specify how the judgment should be expressed can make the final answer less reliable, even for the same input. We ask whether this reflects a change in internal judgment or a failure to express it. Comparing hidden-state vectors for the same input under different instructions, we find that their differences concentrate in a low-dimensional expression subspace. We identify this subspace without benchmark labels and remove its contribution from a linear predictor to obtain an isolated judgment. Across correctness, entailment, and safety, the isolated judgment remains reliable under instructions not used to identify the subspace, even when the model's final answer and the original predictor degrade. When the judgment question is negated, isolation raises the predictor's AUROC from 0.504 to 0.825 for entailment and from 0.480 to 0.891 for safety. We also find that judgment is readable in earlier layers, before the expression subspace begins to disrupt the predictor. Together, these results provide a way to separate judgment from expression and recover internal judgments even when the model's final answers are unreliable.

---


### 106. [Fractional Power-of-Two Quantization for Efficient and Effective Multiplier-Free LLM Inference](https://arxiv.org/abs/2610.21257)

**<font color=#1a73e8>作者：</font>** Sunghyun Wee, Geunjae Choi, Hyeonjin Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) demand efficient inference, where the multiply-accumulate (MAC) operations in linear projections dominate compute and energy cost. Post-training quantization (PTQ) reduces this cost by mapping weights and activations to low-bit integers. Power-of-Two (PoT) weight quantization promises efficient multiplier-free LLM inference via shift-add logic, but suffers significant accuracy degradation at low bitwidths due to its coarse base-2 quantization grid. We introduce Fractional PoT (FPoT), a base-$\sqrt{2}$ (half-octave) fractional PoT grid that achieves practical 4-bit weight quantization while preserving a fully integer shift-add datapath. The method combines (i) the base-$\sqrt{2}$ weight grid with uniform integer activations, (ii) a calibration-time grid-alignment refinement absorbed into the static per-channel scale, and (iii) a lightweight 1-adder $\sqrt{2}$ approximation whose error is absorbed during weight calibration via approximate-grid quantization, yielding a processing element (PE) with significantly fewer gates than a 4-bit integer multiplier. On Llama-3-8B with 4-bit weight and activation quantization, FPoT improves zero-shot commonsense reasoning performance by 8.72% relative to the PoT baseline, while maintaining performance close to the uniform integer baseline, with only a negligible 0.4%p degradation. These results hold across various configurations spanning seven models and three bit-widths. Furthermore, FPoT can be integrated with state-of-the-art LLM PTQ methods, demonstrating framework-agnostic applicability.

---


### 107. [TRACER: A Multimodal Harness for Patient Care in Hospitals](https://arxiv.org/abs/2610.21266)

**<font color=#1a73e8>作者：</font>** Zane Durante, Paul Tang, Keshigeyan Chandrasegaran 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continuous video and clinical records provide complementary information for understanding how patient behavior evolves over a hospital stay. A central challenge is how to represent behavior across the entire stay while preserving access to fine-grained visual and clinical evidence. We introduce TRACER, a training-free multimodal harness that constructs minute-level action records from video and combines them with clinical records into hourly reports. The harness equips an LLM agent with tools to query this hierarchy, inspect relevant video, and retrieve clinical records. To evaluate TRACER, we construct two benchmarks. The first contains 397 annotated one-minute clips spanning 15 atomic actions; the second poses 144 clinician-informed multiple-choice questions, grounded in 264 hours of video and clinical records from two ICU patients. TRACER achieves up to 84.8% accuracy for action detection and 61.0% QA accuracy versus 49.3% for the strongest baseline using the same backbone. Across 280 patients spanning approximately 60,000 camera-hours, TRACER identifies significantly less purposeful activity in patients with a positive delirium assessment during their stay than in those without (p < 0.0001). Our results show that combining continuous video with clinical records can support understanding of patient behavior over time and across patient cohorts without training on protected health data.

---


### 108. [TRACER: Trajectory-Aware Tool Retrieval for LLM Agents](https://arxiv.org/abs/2610.21267)

**<font color=#1a73e8>作者：</font>** Tanish Kher, Sarvesh DK, Abedelkadir Asi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern agents select tools from registries, but exposing entire registries incurs high token costs and can impair selection as they grow. We present TRACER, a retrieval front-end that indexes observed tool-call sequences in a trie and ranks continuations using a learned blend of empirical and contextual priors. On a mixed retail-and-telecom $\tau^2$ environment, TRACER improves GPT-5.4's tool-selection accuracy by 4.7 points while reducing input tokens per step by 80%, exposing just 5 of 128 tools. In autonomous full-turn execution, it matches GPT-5.4's full-registry task success with 61% fewer input tokens per step. Across six environments and four models, TRACER improves tool-selection accuracy over full-registry selection in 21 of 24 model-environment pairs, with average gains of 6 to 10 points; the three exceptions trail by at most 2.2. We analyze failures in both regimes to identify directions for future work.

---


### 109. [Auditing Escalation Reliability in Healthcare LLM Agents: A Perturbation-Controlled Benchmark of Workflow-State Failures](https://arxiv.org/abs/2610.21270)

**<font color=#1a73e8>作者：</font>** Zihao Zheng, Junyi Yao, Baichuan Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Trustworthy biomedical AI requires reliable action selection when evidence is missing, stale, conflicting, or late, not only accurate answers on static inputs. We instantiate an episode-level evaluation protocol as 400 synthetic healthcare workflow episodes: 40 hand-authored semantic seeds across four task classes, two surface parameterizations, and five controlled variants, scored on ANSWER/ASK CLARIFICATION/ABSTAIN/ESCALATE under a pre-declared 5:1 missed-versus-unnecessary escalation cost. Reference actions are single-author study-policy labels, not clinician-adjudicated ground truth. Across five open-weight configurations (1.7B--9.7B), clean decision accuracy reaches 0.97, yet uncertainty-prompted models miss 32--97% of required escalations. The stronger 9.7B configuration narrows but does not remove the gap, falling from 0.97 clean accuracy to 0.78 under conflict. Verbalized confidence is inconsistent (ECE 0.10--0.54; failure AUROC 0.48--0.77), and a development-tuned confidence-only policy yields no utility gain. A transparent workflow-aware controller improves 5:1 utility for every model and reduces missed escalations to 0.12--0.24, at specificity 0.83--0.93. However, a 30-concept lexical stress test reduces each rule detector's recall from 1.00 on trigger phrases to 0.00 on unseen paraphrases, limiting the controller claim to this benchmark. Seed-clustered statistics, ablations, cross-task transfer, raw outputs, and manifests are packaged for audit. The results motivate explicit workflow-state evaluation while showing that apparently effective routing controls need their own generalization tests.

---


### 110. [TimeCap: A Scalable Open-Source Pipeline for Captioning Wearable Health Time-Series Data](https://arxiv.org/abs/2610.21274)

**<font color=#1a73e8>作者：</font>** Max Rosenblattl, Milana Gurbanova, Karl Aurel Deck 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series data generated continuously across industrial, environmental, and especially health domains produce multimodal signals whose scale and heterogeneity make their processing and interpretation particularly challenging. Time-Series Language Models (TSLMs) promise scalable interpretation of these signals, yet remain bottlenecked by a fundamental lack of text-annotated time series pairs that are signal-grounded, reproducible, and extensible across modalities and schemas. Existing paired corpora are either closed or limited in scale and modality coverage. Annotation with large language models could scale them up, but its outputs cannot be regenerated exactly, which prevents others from re-deriving, extending, or auditing the resulting corpus. To address this, we release TimeCap, an open deterministic captioning pipeline with three reusable extractor tiers and a cross-channel synthesis layer that operates directly on the signal with no language model in the loop, extensible to new schemas by writing channel definitions alone. This positions TimeCap as a reproducible mechanism for future dataset generation rather than a one-off release. Applying TimeCap to OpenMHC, the MyHeart Counts wearable dataset, yields MHCap, the largest open caption layer for multimodal wearable time-series data. MHCap spans 19 Apple HealthKit channels and 7,005,763 captions over 908,944 person-days. To showcase the impact of the corpus, we train OpenTSLM, a time-series language model, on MHCap and benchmark on health-outcome prediction. Caption-augmented training (OpenTSLM-Cap) outperforms a label-only baseline on 29 of 32 per-user binary evaluations across 8 tasks.

---


### 111. [Diviner: Agentic RCA with Human-Governed Adaptation for Large-Scale Infrastructure](https://arxiv.org/abs/2610.21281)

**<font color=#1a73e8>作者：</font>** Pradipta Ghosh, Gaurav Mitra, Shripad Nadgowda 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Root-cause analysis (RCA) in large-scale distributed systems is challenging because a single symptom can cross service, data, configuration, compute, and organizational boundaries. Responders must assemble incomplete evidence and coordinate experts who hold different parts of the causal path. Generic language-model agents do not solve this problem through tool access alone: they can use stale or mistimed context, interpret failed queries as absent symptoms, report unsupported system state, and overload observability services designed for human-paced use.
We present Diviner (Domain-Informed Verifiable Incident Navigation through Evidence and Review), an agentic RCA system operating at Meta and organized around a four-stage reliability lifecycle. Encode combines a large corpus of reviewed incidents with service-owner expertise to produce scoped, versioned skills, workflows, typed tools, and an incident knowledge graph. Execute uses an adaptive Lead and context-isolated workers to apply relevant knowledge to point-in-time evidence and maintain evidence-linked hypotheses. Evaluate compares saved investigation trajectories with responder-reviewed outcomes to measure exact cause, useful direction, and Groundedness. Adapt uses recurring gaps and on-call feedback to derive focused operational- knowledge updates, admitting them only after replay, quality checks, and owner approval.

---


### 112. [Mallea: Building, Steering, and Memorizing Worlds with Coding Agent](https://arxiv.org/abs/2610.21283)

**<font color=#1a73e8>作者：</font>** Xuanyi Liu, Ruiqi Li, Siwei Ma  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Code world models represent world dynamics through explicit state and executable rules. We investigate how to coordinate object representations, behavioral revisions, and visual memory within this formulation. We present Mallea, a system for building, steering, and memorizing worlds from text. A coding agent infers object interaction requirements from the prompt and jointly plans object structure, properties, and rules, favoring compact representations that support those requirements. The world evolves under the planned rules; optional user actions steer it, while text requests can edit properties or extend capabilities with unaffected state preserved. Object texture memory retains reusable appearance only for whitebox-defined objects and adapts it as those objects change. The program advances world state, while a generative renderer combines current structure with remembered appearance. By organizing construction, intervention, and memory around the same objects, Mallea conditions subsequent observations on the latest state and compatible appearance. Project page: this https URL.

---


### 113. [The Density of Thought: Predicting and Steering Reasoning in Large Language Models](https://arxiv.org/abs/2610.21286)

**<font color=#1a73e8>作者：</font>** Tanush Kalhan, Anupam Chattopadhyay, Sriram Ranga 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We investigate whether variation in information density across chain-of-thought (CoT) reasoning steps predicts answer correctness and can serve as a controllable inference-time target. We prompt frozen pretrained models to solve problems via CoT and measure the density of each reasoning step with two independent metrics: LP variance (how unevenly information is distributed across steps, computed as the variance in mean per-token negative log-likelihood) and the Caveman compression ratio. We then test whether density correlates with, and can be steered to improve, answer correctness. Experiments across six model scales, two training paradigms, and 60 GSM8K problems yield four main findings. First, lower LP variance predicts correctness in supervised fine-tuned (SFT) models, but this relationship weakens with scale and reverses in reinforcement-learning (RL) distilled models. Training paradigm therefore appears more influential than model size in determining density behaviour. Second, synthetic experiments reveal an intrinsic complexity preference: models trained on uniformly distributed data learn complexity-favouring distributions 2.0 to 2.6 times more accurately than simplicity-favouring ones. Third, direct inference-time density steering reduces accuracy from 60.0% to 8.3%, indicating that natural density patterns are functionally important to reasoning. Fourth, pre-generation nudging combining hint injection with contrastive KV-cache steering improves accuracy by 13.3 percentage points, consistent across both metrics. Finally, we introduce Entropy-Gated Density Routing (EGDR), a self-supervised method using token-level Shannon entropy to gate proportional KVcache adjustments during generation, improving accuracy by 10.0 percentage points without any external guidance.

---


### 114. [Bias Control and Injection for Multi-Agent Aggregation](https://arxiv.org/abs/2610.21290)

**<font color=#1a73e8>作者：</font>** Sungjae Lee, Soheil Abbasloo, Jabin Koo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent reasoning with large language models (LLMs) raises a central question for collective decision-making: when agents disagree, whose decision should be trusted? Resolving such disagreements is difficult because agents' decisions are susceptible to non-semantic biases such as majority pressure and response-style preferences, which can obscure the quality of the underlying reasoning. Our analysis shows how bias can be both mitigated and exploited: bias control improves initial answer selection, while bias injection elicits decision instability that serves as a reliability signal. Building on these findings, we introduce a test-time aggregation framework that requires neither validation data nor prior knowledge of relative model strength. The framework implements bias control by presenting one style-normalized reasoning trace per distinct answer, and bias injection by placing each aggregating agent's initially selected answer in the minority. Overall, our framework achieves higher average accuracy and better token efficiency than competing non-oracle aggregation methods across three mathematical reasoning benchmarks and four heterogeneous LLM combinations. It also improves final-answer accuracy when applied to multi-agent debate and Mixture-of-Agents, without modifying their interaction or synthesis processes.

---


### 115. [Can Capability Enhancement be Localized?](https://arxiv.org/abs/2610.21294)

**<font color=#1a73e8>作者：</font>** Anh Tuan Nguyen, Anna Bair, Zico Kolter  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer-based language models have shown strong capabilities across many tasks and domains. However, prior work shows that, for a given task, not all attention heads matter equally. Specifically, they suggest that many \textit{redundant} heads can be safely removed with little-to-no effect, while a small set of \textit{important} heads, when ablated, severely damages the model's performance on the given task. In this work, we investigate a complementary aspect, called \textit{Capability Enhancement Localization} (CEL): \textit{given a model and a task, does there exist a small set of heads whose removal improves the task performance?} We first investigate this question \textit{empirically} across models from different families. Using a simple two-stage routine that screens candidate heads and evaluates their joint ablations, we identify sparse head combinations whose removal improves task-specific performance without further fine-tuning. Motivated by these observations, we ask \textit{theoretically whether such a phenomenon can naturally arise from training dynamics, and under what conditions}. To this end, we construct a simplified multi-head softmax attention model and two tasks with conflicting features, and show that gradient descent from small random initialization provably concentrates the conflicting features into particular heads. We further show that ablating such heads improves performance on one task while harming the other, even though training converges to a global optimum of the joint objective. This establishes a possible training-induced theoretical explanation for CEL.

---


### 116. [Making every stage of medical device document assessment with large language models deterministic](https://arxiv.org/abs/2610.21300)

**<font color=#1a73e8>作者：</font>** Ryosuke Suzuki  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> To show that a medical device complies with regulation, experts judge whether documents and records meet each requirement and record the judgment for others to verify. For each assessment item that experts define, large language models could prepare a preliminary assessment: a label such as Satisfied or Not satisfied, a reason and quoted evidence. We sent fourteen commercial deployments of such models (seven models from three providers, through six routes) the same request repeatedly, with the deterministic sampling settings each accepted; every deployment returned differing assessments for at least one request, and in twelve the label changed. Reducing reasoning where the interface allows it did not reduce the variation, and prompts of retrieved passages removed it only for the smallest models. The same open-weight model was reproducible or not depending only on how it was served. A pipeline we built to be deterministic at every stage -- text extraction and optical character recognition (OCR), chunking, embedding, indexing, retrieval and inference -- returned byte-identical output at each stage across reruns, interruptions, edits, machines of one graphics processing unit (GPU) model and days, for blood glucose meter and infusion pump documents. OCR, embedding and approximate retrieval varied when their own serving was not made invariant, and outputs changed with the GPU model and with the inference engine's scheduling settings, which therefore belong in the recorded configuration. End-to-end determinism is achievable and gives a testable basis for audit and change control.

---


### 117. [VALCON: Benchmarking and Enhancing Value Consistency in Large Language Models via Dual-Role Variation](https://arxiv.org/abs/2610.21304)

**<font color=#1a73e8>作者：</font>** Junru Wu, Jingting Zheng, Yuqi Ren 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current value alignment evaluations for large language models (LLMs) heavily rely on output compliance, overlooking whether LLMs maintain value consistency when alternating between generator and evaluator roles. Such consistency is increasingly important because modern LLM agents and alignment pipelines often rely on the same LLM to both generate actions and evaluate their acceptability. To mitigate this limitation, we propose VALCON, a role-driven data construction framework that operationalizes value consistency into three benchmark suites (VAB-Consistency, VAB-Boundary, VAB-Challenge) via dual-role variation. By systematically pairing an LLM's generative behavior with its evaluative judgments under identical principles, VALCON synthesizes target evaluation data that exposes hidden value discrepancies. Experiments on 28 LLMs reveal pervasive cross-role inconsistency: models with highly compliant outputs frequently fail to align their judgments with their own generations. To understand and address this gap, we perform mechanistic probing that uncovers a role-dependent representational decoupling associated with this behavioral asymmetry. Guided by these insights, we propose a representation-directed intervention that effectively mitigates consistency failures. Our work establishes value consistency as a distinct alignment dimension and provides a complete evaluation-analysis-mitigation pipeline. Code and data are available at this https URL.

---


### 118. [VLA-$Δ$: Learning Physical State Transition for Vision-Language-Action Models](https://arxiv.org/abs/2610.21306)

**<font color=#1a73e8>作者：</font>** Qi Lu, Jiarun Li, Ce Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models transfer semantic knowledge acquired through vision-language pretraining to robot control, achieving strong performance across various benchmarks. However, most VLAs directly map observations to demonstrated actions without explicit supervision of intermediate physical state changes, making them prone to overfitting observation-action correspondences. Some methods introduce intermediate reasoning or future-state prediction in language, visual, or latent spaces to guide action generation, but do not explicitly supervise the physical state transition itself. We therefore propose VLA-$\Delta$, a general framework that uses physical changes between current and future states as explicit learning targets. To support this objective, we construct a large-scale pretraining dataset and derive physical state-transition annotations covering task-relevant semantics and visual motion changes, providing more direct supervision for continuous action generation. During inference, the model generates actions directly from current observations without additional inference overhead. VLA-$\Delta$ achieves performance competitive with the state of the art on LIBERO and RoboTwin, and outperforms $\pi_{0.5}$ in real-robot experiments. Our code is available at this https URL

---


### 119. [PocketTSLM: Deploying an On-Device Soft-Prompt Time-Series Language Model for Privacy-Preserving Smartphone Reasoning](https://arxiv.org/abs/2610.21308)

**<font color=#1a73e8>作者：</font>** Max Rosenblattl, Nikhil Krishnaswamy, Leon Nissen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Consumer phones and wearables increasingly collect physiological time-series data, yet most mobile systems treat these streams as summaries or text rather than as temporal evidence. This representation is poorly matched to personal health systems that need to retrieve, route, or summarize sensor evidence while preserving temporal structure. Cloud-hosted time-series language models avoid smartphone limits, but they repeatedly move sensitive physiology off the device and add latency and per-query compute cost. Mobile model alternatives that aggregate time-series data into statistical features or serialize raw samples as text either compress temporal structure or exhaust the context and memory budgets of small on-device models. We present PocketTSLM, a mobile-native deployment of OpenTSLM SoftPrompt, the soft-prompt variant of the OpenTSLM time-series language model. PocketTSLM runs fully on a consumer smartphone by injecting encoded time-series windows as embeddings instead of tokenizing time series as text. A numerical parity protocol verifies identical greedy-decoded token sequences between the Swift port and a Python reference using Apple's MLX machine-learning framework. Answers also match the PyTorch reference, although rationale wording can differ. An on-device context-economics benchmark compares the soft-prompt path with a text-serialized baseline on the same backbone. In our benchmark format, soft-prompting uses approximately 12 times fewer time-series tokens and reduces prompt-prefill cost. PocketTSLM processes 30-second Sleep-EDF electroencephalography clips for sleep staging and a 1,000-sample (10 s) 12-lead electrocardiogram clip from ECG-QA. In comparison, text-serialized baselines exceed the phone's context or memory budget at longer time-series windows. All inference runs entirely on the device, with no health data transmitted during inference.

---


### 120. [Combining LLM and Dynamic Analysis for Universal Testing of Static Application Security Testing Tools](https://arxiv.org/abs/2610.21309)

**<font color=#1a73e8>作者：</font>** Huaien Zhang, Yu Pei, Hao Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Static application security testing (SAST) tools help detect potential software vulnerabilities, but they themselves contain faults undermining reliability and usability. Automated testing can address these issues, yet current techniques suffer from limited program transformation diversity and lack mechanisms to verify generated variants, leading to reduced fault detection and high manual effort. We present LLM4SAST, the first universal framework detecting faults in SAST tools using large language models and dynamic feedback. Our key insight is leveraging LLMs to understand and transform code in diverse programming languages. We design novel metamorphic relations with transformations to guide variant generation, using an LLM to produce multi-language variants that satisfy these relations. To reduce erroneous variants and identify unique faults, we propose two heuristics: dynamic-feedback-driven selection and program-differencing-based clustering. For each metamorphic relation, a report-centric test oracle detects variants that fail tests and identifies underlying faults by differentially analyzing SAST reports of the seed program and its variants. LLM4SAST identified 66 unique faults across six SAST tools, with 32 confirmed or fixed after being reported to developers, demonstrating effectiveness. The proposed heuristics eliminate 47.8% of false positives, and LLM4SAST detects 3.4 times more faults while requiring only 39.8% of the variants compared to existing approaches.

---


### 121. [Loud and Clear: Making Visual Evidence Count in Multimodal Document RAG](https://arxiv.org/abs/2610.21318)

**<font color=#1a73e8>作者：</font>** Eunchan Jo, Seounghyun Jang, Sangwoo Mo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal document retrieval-augmented generation (RAG) has focused largely on retrieval, yet its answers depend on how well a vision-language model reads the retrieved pages. We find that evidence in retrieved pages remains underused even when the correct pages are retrieved. On SciEGQA oracle pages, five prior methods give the generator 0.7K to 2.7K visual tokens per query on average under a common image processor, yet raising the page-only budget from 1K to 32K improves accuracy by 15.22 points. At a fixed 16K budget, adding ground-truth crops improves accuracy by 3.75 points over page-only input. We study what the generator needs from retrieved pages through two requirements: Loud, making full use of visual token capacity, and Clear, refining the page so that its evidence becomes prominent. For Loud, increasing either the visual token budget or visual fidelity, the image resolution those tokens preserve, improves accuracy with the other held fixed, and full-page scaling outperforms repetition and tiling at matched budgets. For Clear, suppressing surrounding content improves accuracy without enlarging selected regions, and adding OCR of these regions to page images outperforms either input alone. We implement both as Loud and Clear (LoC), which combines higher-resolution pages with OCR from query-relevant regions without ground-truth annotations or additional training. LoC outperforms eight prior methods on SciEGQA, ViDoRe-v3, and MMLongBench-Doc, improving over the strongest, ColQwen3, by 8.88, 3.09, and 4.22 points with the same retriever and generator. It also outperforms its page-only variant under the same visual token budget. These results locate a bottleneck beyond retrieval: how the retrieved pages are given to the generator.

---


### 122. [ZoomCap: Evidence-Routed Visual Zooming for Recoverable Visual Information Transfer](https://arxiv.org/abs/2610.21320)

**<font color=#1a73e8>作者：</font>** Hao Shi, Jiafeng Wang, Yuzhuo Fu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detailed captions transfer visual information into vision-language model supervision, but quality is easily conflated with length: long single-pass outputs still miss small objects, text, and spatial relations or promote uncertain observations into confident claims. We formulate fine-grained captioning as recoverable visual information transfer, in which a teacher acquires missing evidence under a finite observation budget and converts it into reusable supervision. ZoomCap uses a draft caption to route conditional knowledge retrieval, OCR-sensitive reading, coverage-gap recovery, and adaptive visual zooming, allocating deeper crops only to the most complex eligible region, deriving spatial relations from grounded geometry, and fusing non-duplicate evidence. We also introduce FactCycle, which scores caption-derived atomic claims on two blind anchors--source image (truthfulness) and reconstruction (realizability)--separating fabrication from generator loss claim by claim; human and multi-judge comparisons complement this fact-level view. Against Qwen3.5-397B-A17B captions, ZoomCap achieves an 81.9% human tie-adjusted preference score with a teacher over 10x smaller, and FactCycle counts 52.4 transferred claims per image vs. 31.5 for ScaleCap. The evidence also transfers: in continual pre-training, ZoomCap-450K improves the 11-benchmark average by 1.31-2.38 points over the strongest competing corpus and Ling-Tiny-VL-v3 gains 1.4 points on a production document/OCR monitor suite (1.5 on perception) at 60B tokens; in medical pre-training, 2.64M ZoomCap-captioned images improve five VQA benchmarks by 3.04 points (vs. 1.76 for same-image Gemini-3.1-Pro captions).

---


### 123. [AdaLoop: Thinking with the Vision Encoder](https://arxiv.org/abs/2610.21323)

**<font color=#1a73e8>作者：</font>** Xinran Nicole Han, Yiyang Lu, Katelyn Gan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most vision-language models (VLMs) treat the vision encoder as a static feature extractor: it encodes an image once, independently of the question, and leaves subsequent reasoning to the language model. Yet different questions may require different visual operations and processing depths. We present AdaLoop, a framework for question-conditioned visual recurrence in VLMs. AdaLoop adapts visual computation to the question and reuses the encoder's transformations across multiple iterations, with the pretrained vision weights frozen. We also introduce VisRO, a procedural dataset and generation pipeline for training and evaluating vision-centric reasoning. On six VisRO tasks, AdaLoop outperforms standard fine-tuning and question-conditioned single-pass baselines with matched training data and optimizer updates. These gains hold across three VLM families on both in-distribution and out-of-distribution examples. Our findings suggest that pretrained vision encoders can contribute to reasoning through task-directed, iterative visual computation.

---


### 124. [CertEx: Exact Visual Retrieval at Scale by Certified Exclusion](https://arxiv.org/abs/2610.21325)

**<font color=#1a73e8>作者：</font>** Dongfang Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Exact $k$-nearest-neighbor (kNN) search over image descriptors and embeddings underlies visual retrieval, near-duplicate detection, the evaluation of learned representations, and increasingly the memory of LLM agents. However, exhaustive search computes every distance at full precision, whereas approximate indexes return recall below one. We observe that exact search only needs a proof that each excluded vector cannot be a neighbor. Because such a proof only has to be conservative, it can be checked in low precision, much as the retina examines the whole scene at low resolution. We call this principle certified exclusion and realize it in an exact kNN method for GPUs, which we call \certex. Specifically, \certex\ stores a lower-bounding projection of each vector in half precision and folds a rounding certificate into the same tensor-core dot product, so that only the few vectors that the test keeps need exact distances. We prove that \certex\ returns the exact kNN of every query. On sixteen datasets with up to 100M vectors, \certex\ is exact for every query at 7.1$\times$ to 18.0$\times$ the throughput of the fastest cuVS search on one H100 and outperforms quantized and graph indexes whenever every query must be exact.

---


### 125. [DocPilot: Interactive Agent Orchestration and Training for Long Visual Document Understanding](https://arxiv.org/abs/2610.21327)

**<font color=#1a73e8>作者：</font>** Zhuowen Liang, Xiaotian Lin, Yuyu Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal long-document question answering requires models to seek sparse evidence across pages and modalities, understand heterogeneous document content, and reason over the collected evidence. Even advanced vision-language models (VLMs) can overlook sparse evidence and struggle with cross-modal reasoning in a single pass. Existing document agents further introduce multi-step interaction, but some still rely on predefined workflows or coarse-grained actions, limiting the flexibility and granularity of document reasoning. We introduce DocPilot, an agentic document framework that supports expressive orchestration and makes complex document solving learnable by small language models (SLMs). DocPilot orchestrates evidence seeking through page-level navigation and fine-grained evidence localization, and integrates local visual inspection, code-based numerical reasoning, and cross-modal reasoning for multimodal understanding. To transfer these capabilities to small models, we propose curriculum-based agentic training that progresses from single-ability learning to adaptive orchestration through supervision from data-grounded reasoning traces and executable interaction trajectories. Across MMLongBench-Doc, DocBench, FinRAGBench-V, and MADQA, DocPilot achieves strong gains with frontier VLM backbones, while DocPilot-4B delivers competitive performance against substantially larger models, demonstrating strong effectiveness and generalization across diverse long-document reasoning settings. The code is available at this https URL.

---


### 126. [QuasiLeak-Bench: Evaluating LLM-Based Privacy Detectors on Policy-Conditioned Quasi-Evidence Group Recovery](https://arxiv.org/abs/2610.21333)

**<font color=#1a73e8>作者：</font>** Yufan Zhu, Yangfan Jiang, Yang Fei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural language messages often contain quasi-identifiers that are weak in isolation but can jointly reveal an individual's private attributes. We call such a jointly revealing set of cues a quasi-evidence group. Existing privacy benchmarks focus on explicit identifiers, attribute inference, or task-driven disclosures, leaving inference from quasi-evidence groups largely unmeasured. In practice, whether exposing such a quasi-evidence group violates privacy also depends on sender-specified disclosure policies. We introduce QuasiLeak-Bench, a benchmark for policy-conditioned quasi-evidence group recovery, which evaluates whether detectors recover complete quasi-evidence groups and flag the disclosures the given policy prohibits. To obtain reliable ground truth at scale, a reverse-construction pipeline first selects weak quasi-identifiers, composes them into quasi-evidence groups verified to jointly reveal a target attribute, and generates documents around this evidence, followed by automated quality control. Experiments show that existing privacy detectors transfer poorly to QuasiLeak-Bench, and locally deployable LLM-based detectors fall far behind proprietary models, mainly because they miss most quasi-evidence groups altogether. However, a 4B model fine-tuned on our training split surpasses the strongest prompted model on held-out documents, showing that the task is learnable.

---


### 127. [Ranking and Partitioning of Attention Heads for Sparse and Continual Reinforcement Learning Fine-tuning](https://arxiv.org/abs/2610.21336)

**<font color=#1a73e8>作者：</font>** Ruizhe Shi, Zaiwen Yang, Qiubo Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study sparse and continual reinforcement learning fine-tuning of language models through attention-head ranking and partitioning. For sparse learning, we rank attention heads by gradient norm to identify a small subset of heads that can be trained effectively. For continual learning, we partition heads across tasks to reduce cross-task interference and preserve previously learned capabilities. Theoretically, we relate gradient norm to training effectiveness, and further characterize why sparse, separated head updates can remain stable. Empirically, across math, instruction-following, and coding tasks, tuning higher-ranked heads consistently outperforms tuning lower-ranked ones while often matching denser baselines, and head partitioning improves retention while preserving adaptation to new tasks.

---


### 128. [Does On-Policy Distillation Need to Complete Every Rollout?](https://arxiv.org/abs/2610.21337)

**<font color=#1a73e8>作者：</font>** Zhengxin Zhang, Maosen Tang, Ning Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) effectively transfers capabilities from a teacher to a student through feedback on student-generated rollouts. However, generating complete student rollouts and computing teacher feedback for every token make OPD computationally expensive. We introduce Stochastic Truncated On-Policy Distillation (STOPD), which accelerates OPD by randomly truncating student rollouts and correcting the resulting sampling bias with blockwise inverse-probability weighting (IPW). At each training step, we sample a stopping position for each rollout before generation and let the student generate until that position or natural termination. We obtain teacher feedback on every generated token and use blockwise IPW to compensate for the lower probability of retaining later tokens while controlling the weights. We prove that this weighting preserves Vanilla OPD's gradient sum in expectation and derive one-step update-error bounds for SGD, Adam, and Muon. We evaluate STOPD across multiple teacher-student model pairs, task domains, and optimizers. STOPD reduces generated tokens by 25-48% while maintaining accuracy comparable to Vanilla OPD, achieving 1.3-2.2x training speedups.

---


### 129. [ARGUS: An Agenda-Driven Framework for Reliable User Simulation](https://arxiv.org/abs/2610.21346)

**<font color=#1a73e8>作者：</font>** Hang Zheng, Nan Jiang, Zichen Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> High-fidelity user simulators are essential for evaluating and training agents in interactive environments. However, current LLM-based simulators struggle with reliability issues, such as goal omission and policy non-compliance. We propose ARGUS (Agenda-dRiven Goal-oriented User Simulator), a neuro-symbolic framework that maintains the user's goal state using a dynamic agenda stack manipulated via symbolic operations. By rigorously decoupling state tracking from natural language generation, ARGUS facilitates strict goal progression and constraint-aligned interactions. For cost-efficient deployment, we distill ARGUS into compact models using a unified pipeline: evaluator-guided SFT followed by online RL with dense step-level rewards. To rigorously evaluate behavioral fidelity, we introduce a rubric-based metric Composite Behavioral Score (CBS). Evaluations on $\tau^3$-Bench and MultiWOZ demonstrate the significant superiority of the ARGUS architecture and the efficacy of our training pipeline. Code and data will be released soon.

---


### 130. [Emotion Is Not External Knowledge: Internal Attention Signals for Affective State Reasoning](https://arxiv.org/abs/2610.21347)

**<font color=#1a73e8>作者：</font>** Wenqiu Tang, Zhen Wan, Yihui Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) increasingly operate in multi-turn interactions that require maintaining latent conversational states, not only explicit facts. We study affective state as an implicit state inferred from sparse contextual cues that remain relevant after topic shifts, and ask whether LLMs expose internal attention signals for routing such evidence at inference time. Prior attention interventions rely on labeled in-domain head profiles and externally specified target spans, limiting transfer across affective-evidence distributions. We propose Self-targeted Internal Attention Boosting (SIAB), which localizes sparse affective heads via causal localization (in detail activation patching) on synthetic minimal pairs and boosts, at the answer position, the content tokens these heads already attend to; both edited heads and target tokens are derived from the model's own behavior, enabling the same head set to be reused across this http URL evaluate on ECC and GoEmotions across three LLMs and multiple prompting settings. Across settings, SIAB improves prompt-matched baselines by up to +10.3 macro-F1 on ECC and +5.5 on GoEmotions. Combined with PASTA-style external supervision, it achieves up to +13.84 accuracy points and +12.51 macro-F1 points, while mechanistic analyses trace the gains to sparse, emotion-enriched heads and show that layer proximity affects additivity.

---


### 131. [FedSkillGit: Federated Skill Evolution via Version Control](https://arxiv.org/abs/2610.21348)

**<font color=#1a73e8>作者：</font>** Boxun Lan, Jiamei Li, Weijian Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents can improve their capabilities by evolving reusable natural-language skills from execution experience. In real-world deployments, this experience is distributed across data owners who cannot pool their raw data, which motivates federated skill evolution. The natural first design lets each client evolve the whole skill document and upload the result for server-side aggregation. That design is poorly matched to skill evolution for three reasons. An evolved document can still carry client-specific content distilled from private traces, repeated transmission of a nearly unchanged document spends communication on knowledge that the population already holds and the contribution of a single client is buried in a document that the server cannot meaningfully attribute. We propose FedSkillGit, a federated skill evolution framework that replaces full-document updates with commits. Each participating client submits a bounded set of patches over named rules together with its local experience, which summarizes what the round taught it, and the pair passes a two-stage privacy filter before it leaves the client. The server deduplicates the submitted patches and the local experience of all participants, updates a global experience document that only the optimizers read, and merges the surviving patches into a candidate skill. The candidate is distributed to the clients, which score it on their own validation sets and report the results, and it is published only when the reported scores improve on the current version. Experiments on three datasets and three language model families show that FedSkillGit outperforms state-of-the-art baselines by up to 22% and approaches centralized evolution without sharing raw client data.

---


### 132. [RenoLayout: Unified Floorplan Renovation and Furniture Layout for Constraint-Aware Residential Design](https://arxiv.org/abs/2610.21366)

**<font color=#1a73e8>作者：</font>** Jingguo Liu, Yuanqing Liu, Chong Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Residential design aims to transform existing homes into functional living spaces while satisfying diverse design preferences and physical constraints. However, existing floorplan generation methods typically assume empty building boundaries as input, whereas renovation requires reasoning over existing floorplans. Furthermore, floorplan renovation and furniture layout are commonly addressed as separate tasks, overlooking their inherent spatial dependency. Consequently, practical residential design must preserve immutable structural components while transforming editable spatial elements. It must also optimize furniture placement under design objectives and physical constraints. To address these challenges, we formulate residential design as a design-point-guided conditional generation task and propose RenoLayout, a framework that translates a pre-design residential state together with a design-point set into an executable Geometry-as-Code program. To enable controllable supervision, we construct a Design Map comprising 123 fine-grained design points covering structural renovation and furniture layout. We further introduce Difference-Grounded Design-Point Annotation to derive design-point sets automatically from before--after design pairs with VLM-based consistency verification. RenoLayout is trained using a three-stage CPT--SFT--RL pipeline, progressively improving spatial reasoning, instruction following, and constraint compliance. We also introduce the RenoLayout Benchmark, a set of 200 real-world before--after renovation cases with complete furniture layouts. To the best of our knowledge, it is the first benchmark for unified residential design. These cases include design-critical structural and building-service constraints.

---


### 133. [ESG-Kor: A Korean Dataset for ESG-related Information Extraction and Practical Use Cases](https://arxiv.org/abs/2610.21368)

**<font color=#1a73e8>作者：</font>** Jaeyoung Lee, Geonyeong Son, Misuk Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the expansion of pre-trained language model usage in recent years, the importance of datasets for performing tasks in specialized domains has significantly increased. Therefore, we have built a Korean dataset called ESG-Kor to automatically extract Environmental, Social, and Governance (ESG) information, which has recently gained importance. ESG-Kor is a dataset consisting of a total of 118,946 sentences that extracted information on each ESG component from Korean companies' sustainability reports and manually labeled it according to objective rules provided by ESG evaluation agencies. To verify the effectiveness and applicability of the ESG-Kor dataset, classification performance was confirmed using several Korean pre-trained language models, and significant performance was obtained. Additionally, by extending the ESG classification model to documents of small and medium enterprises and extracting information based on ESG key issues and in-depth analysis, we demonstrated potential and practical use cases in the ESG field.

---


### 134. [Evaluating and Improving Static Application Security Testing Tools for Rust](https://arxiv.org/abs/2610.21373)

**<font color=#1a73e8>作者：</font>** Huaien Zhang, Zhengjie Zhao, Yu Pei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Rust has become a popular systems programming language in recent years because of its strong guarantees on memory and concurrency safety. Many types of system software have been re-implemented in Rust. However, Rust programs can still suffer from common memory and concurrency vulnerabilities due to unsafe code and misunderstandings of its complex mechanisms. To mitigate such vulnerabilities, developers often rely on static application security testing (SAST) tools. However, the effectiveness of existing Rust SAST tools on real-world vulnerabilities remains underexplored. In this paper, we first conduct an empirical evaluation of mainstream Rust SAST tools using security vulnerabilities identified in real-world Rust applications. We systematically assess their effectiveness, uncover common weaknesses, and analyze the root causes behind them. Motivated by the study, we propose TRUST, a large language model (LLM)-assisted automated testing framework. TRUST automatically analyzes the official Rust reference to derive and implement semantics-preserving transformations. It leverages these transformations to generate mutant programs for evaluating Rust SAST tools and uncovering potential faults within them. Overall, TRUST has revealed 46 faults across six popular SAST tools, 17 of which have been confirmed. In addition, our study yields ten empirical findings and four practical lessons that provide actionable guidance for developing more effective, robust, and maintainable Rust SAST tools.

---


### 135. [Memorilla: Latent Semantic Memory for LLMs](https://arxiv.org/abs/2610.21375)

**<font color=#1a73e8>作者：</font>** Adibvafa Fallahpour, Parsa Idehpour, Vignesh Kothapalli 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Memory enables large language models (LLMs) to use information beyond their parameters, such as past user conversations, long documents, or an agent's earlier actions. For a frozen LLM, access to this accumulated knowledge is limited to what a memory system places in its context window. However, gathering and combining relevant information needed for each query while keeping the model's context short remains challenging for existing systems. Here we introduce Memorilla, a memory system that gathers information from an entire document collection into a fixed number of query-dependent 'memory tokens' for a frozen LLM. Memorilla encodes documents (such as user chats, book chapters) once into reusable embeddings, then learns to retrieve and place query-specific information in the LLM's input embedding space. Using only 16 memory tokens, Memorilla achieves the best performance against baselines including Mem0 and MemoRAG on five of eight benchmarks spanning personalization, long-document and knowledge-intensive question answering. Notably, on FactKG, it reaches 84.33% accuracy versus 80.43% with full-context inference, while using 108x fewer tokens to represent the source documents. Furthermore, Memorilla can facilitate continual learning in agentic systems where the document count (the agent's past turns) increases throughout the trajectory. In a TextWorld environment, we show that Memorilla reduces the agent's tendency to wander between rooms it has already explored, and improves its average success rate from 18.6% with full-history in-context learning to 24.2%. Overall, Memorilla aids frozen LLMs in accumulating and using knowledge effectively across long-context interactions and takes a step towards building continually learning AI systems.

---


### 136. [DPA-MoE: A Runtime Precision Control Framework for MoE Inference](https://arxiv.org/abs/2610.21378)

**<font color=#1a73e8>作者：</font>** Jaeyun Kim, Hoonki Lee, Susie Shin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models reduce computation by routing each token to a small set of experts, but each selected expert is still used at a fixed precision. We present DPA-MoE, a runtime precision control framework that makes routed experts any-precision. DPA-MoE encodes expert feed-forward weights as prefix-decodable chunks using SharedScale AnyBCQ, profiles per-expert reconstruction residuals offline, and allocates chunks at inference time using live router gate scores. This post-routing allocation lets a single encoded MoE checkpoint operate at multiple effective weight budgets without retraining or re-encoding. Experiments on Qwen3-30B-A3B and DeepSeekMoE-16B show that DPA-MoE improves KL divergence and downstream accuracy over uniform chunk allocation at matched budgets, with modest steady-state throughput overhead in our prototype.

---


### 137. [Perception or Reasoning? Diagnosing and Tackling Reinforcement Learning Bottlenecks in VLMs](https://arxiv.org/abs/2610.21380)

**<font color=#1a73e8>作者：</font>** Zeyuan Yang, Zhuohao Chen, Jiaben Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has brought strong gains to language model reasoning, but its improvements on visual tasks remain less consistent. One difficulty is that visual task failures can arise from different sources: the same benchmark may be limited by perception for one model and by reasoning for another. We introduce Perception and Reasoning Attribution (PARA), which measures the remaining perceptual and reasoning headroom of each model--benchmark pair by comparing how many current errors are recovered with more accurate visual information versus a stronger reasoner. Across 4 vision-language models and 17 multimodal benchmarks, PARA broadly agrees with the expected characteristics of existing benchmarks while revealing substantial model-specific variation. More importantly, it shows that RL gains become smaller as perceptual headroom increases, but larger when reasoning explains more of the recoverable errors, suggesting that current RL exploits reasoning headroom more effectively than perceptual headroom. Motivated by this gap, we analyze how existing RL objectives affect visual perception and find that reward- and token-level signals influence visual attention only indirectly. We therefore propose GRAD, a group-relative attention distillation objective that uses the best rollout in each group to directly guide the visual attention of weaker rollouts. GRAD consistently improves performance across two model scales and seven benchmarks, and further complements existing RL methods.

---


### 138. [Calibration Language Shapes Block-Influence Pruning in Multilingual Language Models](https://arxiv.org/abs/2610.21383)

**<font color=#1a73e8>作者：</font>** Vedant Pandhare, Piyush Dhoka  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Block Influence (BI) ranks Transformer blocks for depth pruning from their input-output cosine change, but the ranking depends on the calibration distribution. We study whether English calibration transfers to Indian languages in Qwen2.5-1.5B-Instruct, Llama-3.2-1B, and Gemma-2-2B. English, Hindi, Marathi, and Tamil use disjoint Wikipedia articles for calibration and evaluation; every selector receives the same 150-chunk budget, and Tamil is excluded from multilingual aggregation to test cross-script transfer. Across all three models, late-block BI is 20.7-55.5% higher for the three Indian languages than for English, and every predeclared late-minus-middle contrast has a 95% bootstrap interval above zero. This mismatch changes the low-BI blocks selected for removal despite high global rank correlations. Averaging BI over equal English, Hindi, and Marathi budgets mitigates the resulting perplexity damage for Qwen at six removed blocks and for Gemma at all tested depths, including held-out Tamil. The mitigation is not universal: on Llama, balancing improves Hindi and Marathi at two removed blocks but severely harms Tamil, while larger pruning budgets select the same blocks and collapse perplexity regardless of calibration. Rank-mean and minimax-rank aggregators do not dominate the raw mean. These results support a diagnostic claim rather than a universal pruning rule: English-only BI systematically misses late-layer activity for Indian-language text, but multilingual calibration must still be validated per architecture and pruning budget.

---


### 139. [Learning to Reason with Selective Internal Feedback](https://arxiv.org/abs/2610.21392)

**<font color=#1a73e8>作者：</font>** Xun Lu, Shumeng Yang, Xinrui Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from internal feedback can improve language models without ground-truth answers or external verifiers. However, confidence and correctness can diverge during training, and continued optimization of average self-certainty can increase confidence while degrading reasoning accuracy. We introduce SIF, a reinforcement learning method that combines comparative reward construction with selective policy updates. SIF compares ranked token-level self-certainty profiles across multiple windows and peers, assigning positive rewards only when both levels of voting provide sufficient support. Sample and group level filtering determines which responses contribute to policy optimization. Experiments on three backbones across 12 mathematical and scientific reasoning benchmarks show that SIF's final checkpoints achieve higher average accuracy than the best-validation checkpoints of Intuitor and Vigor, with a gain of 4.71 percentage points over Intuitor on Qwen2.5-Math-1.5B. Further analyses show better retention of accuracy during continued optimization, while test-time training experiments demonstrate sustained improvements with as few as four rollouts per prompt.

---


### 140. [Self-Guided LLM Reasoning for Error Diagnosis in Vehicle Routing Problems](https://arxiv.org/abs/2610.21393)

**<font color=#1a73e8>作者：</font>** Ni Zhang, Jianan Zhou, Yue-Jiao Gong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vehicle Routing Problems (VRPs) are fundamental to many real-world applications. Recent advances in large language models (LLMs) have spurred progress in solving these NP-hard problems. However, most existing approaches assume that input instances are error-free, neglecting the presence of faults commonly encountered in real-world data. In this work, we systematically investigate the capability of LLMs to detect (and correct) errors in VRP instances, and identify key limitations, particularly in handling complex instances or errors that substantially increase the LLM's reasoning burden. To overcome these challenges, we propose a self-guided reasoning framework in which LLMs autonomously generate code that provides structured insights to aid in error diagnosis. Experiments across diverse problem settings and LLMs demonstrate that our framework significantly improves error detection performance, achieving near-perfect accuracy.

---


### 141. [Watts If? A Benchmark for Counterfactual Reasoning About the AI Data Center Buildout](https://arxiv.org/abs/2610.21397)

**<font color=#1a73e8>作者：</font>** Pankaj Chouhan, Rajarshi Das, Aditya Dubey 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An AI data center is committed years before it draws a watt: a few discrete choices (grid or on-site gas, evaporative or dry cooling, which county to file in) fix its capital, water draw, and carbon path, and LLMs are now asked to help screen them with no test of whether they track what each commitment rules out. We introduce DCBench-440, with two arms reported separately: 200 generative questions over STRIPS worlds for five US deal archetypes, with search-verified gold answers and no tested shortcut above 12% on any question type, and 240 multiple-choice questions grounded in quoted site records, emission equations, and stated scenarios. Across open-weight deployments, accuracy spans 12.5-71.5% (generative) and 58.3-92.5% (multiple choice). One skill fails everywhere: asked to list every action available at a decision gate, no model exceeds 4.0% exact match. The strongest list 72-85% of the actions that would change the project's state but omit most permitted actions that change nothing; with those excused, the best exact match is still 24%. Code, data, and other materials are available upon request.

---


### 142. [Multi-Reward Hacking: From Aggregation-Induced Drift to Trust-Anchored Defense](https://arxiv.org/abs/2610.21404)

**<font color=#1a73e8>作者：</font>** Yushu Li, Jiin Woo, Xiaoxiao Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To improve task performance while encouraging desirable response properties, LLM post-training often combines a primary reward (e.g., correctness) with auxiliary rewards (e.g., brevity or efficiency). However, how these rewards are aggregated can critically affect training outcomes. We show that symmetric aggregation, which treats reward channels equally, can induce a failure where aggregate reward improves while primary-task performance degrades, even when individual rewards are meaningful. We investigate this aggregation-induced failure through a one-step multi-reward decision formulation, characterizing when it constitutes multi-reward hacking. We prove that, under symmetric aggregation, deterministic conditional-mean GRPO converges to auxiliary-favoring behavior when auxiliary rewards are more reliably obtained, regardless of initialization. We propose Trust-Anchored Gating (TAG), which first elects an anchor channel based on the policy drift induced by optimizing each channel alone, then gates auxiliary credit on anchor satisfaction. Unlike calibration-sensitive static reweighting, TAG structurally eliminates credit for auxiliary-only outcomes while preserving additional credit for joint success. In the same analytical setting, TAG provably reverses this selection, converging to the primary-favoring action from any initialization when the primary channel is anchored. Experiments across Qwen and Llama models on mathematics and program synthesis reveal substantial degradation under symmetric, constrained, and normalized aggregation, whereas TAG mitigates this failure. On Qwen3-4B with a brevity reward, TAG achieves 0.581 pass@4 versus 0.220 for additive aggregation, while shortening responses by 44% relative to correctness-only training.

---


### 143. [MemCut: Every Secret Leaves a Trail in the Long-Term Memory of LLM Agents](https://arxiv.org/abs/2610.21405)

**<font color=#1a73e8>作者：</font>** Cheng Zhang, Xuanning Cao, Zhicheng Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term memory has become a crucial component of large language model (LLM) agents, with most research focusing on retrieving relevant information accurately and efficiently. However, a dependable memory system must also forget sensitive user data upon request. To evaluate this capability, we introduce MemCut, a systematic benchmark for user-requested forgetting. Its 456 hand-designed secrets in long-horizon conversations have fully annotated evidence trails to test recovery after deletion, including from messages that never state the secrets directly. We propose two recovery metrics. Native recovery measures reader success through the system's retrieval, whereas residual recovery measures the same reader's success when directly given surviving objects traced to annotated disclosures or evidence. We establish three reference deletion baselines to test how far existing retrievers and write models support forgetting across five memory designs and four LLMs. Disclosure removal reduces native recovery far more than residual recovery. LLM-guided deletion of ten additional turns from twenty retrieval candidates leaves 39-76% residual recovery. Subset sweeps (144 facts, three systems, two models) show that widening the pool at a fixed budget reduces residual recovery more than deleting all original candidates. These sweeps identify candidate coverage as a bottleneck in the reference baselines.

---


### 144. [Identifying Effective Strategies in Prompt Evolution for Stress and Emotion Prediction](https://arxiv.org/abs/2610.21407)

**<font color=#1a73e8>作者：</font>** SeungHyun Yi, Seungjun Yi, Sriram Sattiraju 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Early stress detection and risk prediction are crucial for timely mental health assessment and support. While large language models have recently shown promise for social media stress prediction, relying on accuracy can obscure false positives. Also, prompt revisions yield inconsistent gains across models and tasks, with unclear links to strategy combinations and instruction changes. By comparing six methods on social media stress and emotion data across two model sizes, we found that GEPA and its extension combining instructions from two prompts (GEPA+merge) improved prediction over initial prompts in several settings. We also identified five prompting strategies associated with development gains. These strategies included directing attention to emotional evidence, distinguishing current from past distress, illustrating indirect cues, requiring emotional context, and guiding label selection. Moreover, we documented four observations across tasks and evaluation settings. In a separate set of searches, binary stress prediction improved early, whereas multilabel emotion prediction initially declined and partly recovered. The other three concerned incorrect or conflicting instructions, gains on small comparison samples that did not hold on full development data, and changes in selected prompts' development and reported test rankings. These findings identify effective prompt evolution methods, strategy combinations associated with gains, and task and evaluation limits, providing guidance for applying prompt evolution methods to social media stress detection.

---


### 145. [Jev-LiteMAS: Separating Decisions from Generation in Multi-Agent Workflows](https://arxiv.org/abs/2610.21411)

**<font color=#1a73e8>作者：</font>** Kaixiang Wang, Zhaijiacheng Zhou, Jiong Lou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems rely on generative models for expert execution, workflow planning, and artifact review. Yet many coordination operations require only bounded decisions, such as selecting the next expert or judging artifact quality. Profiling three representative MAS frameworks, we find that routing and review account for 31.7-43.5% of generative-LLM tokens. However, replacing these operations with low-cost decision models introduces two interface gaps: generative planners produce execution plans and handoff instructions (planning gap), while reviewers provide actionable feedback for repairing flawed artifacts (review gap), which bounded decisions alone cannot provide. We introduce Jev-LiteMAS, a multi-agent framework that bridges both gaps by combining a lightweight decision model (Jev) with generative execution and feedback. To address the planning gap, Jev selects experts dynamically from the task and prior expert outputs, using accumulated context to ground subsequent execution without a pre-generated trajectory. To address the review gap, Jev screens intermediate artifacts against task criteria: passing artifacts proceed directly, whereas flagged ones undergo LLM re-review for acceptance or corrective feedback. Across four benchmarks and two backbones, Jev-LiteMAS reduces generative-LLM tokens by 12.7-54.6% over LAS, maintaining accuracy within 1.34 percentage points and lowering latency in seven of eight settings. Grounding routing in substantive expert outputs prevents up to 18.0 points in accuracy loss.

---


### 146. [JevAgentHarness: Benchmarking, Deploying and Training Decision Models That Share Control with LLMs](https://arxiv.org/abs/2610.21412)

**<font color=#1a73e8>作者：</font>** Kunlun Zhu, Tao Feng, Xu Han 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents now fix software, operate computers and serve customers, but their harnesses, the programs that run them, call a large LLM at every step, which makes long tasks slow and costly. Most of these calls end in a multiple-choice decision, such as which tool to call next. Decision models such as Jev answer these questions directly, at a fraction of an LLM call's time and price. We ask how a harness can delegate these decisions to a decision model with little loss of success. To evaluate decision models in agentic tasks, we build AgentDecisionBench, which tests them from isolated questions up to control of a running agent, on public benchmarks and our DecisionGym environment. The decision model most accurate on isolated questions solved only 69.5% of agent tasks, and without a fitted confidence threshold, delegating tool choices lowered success by 19.0 points. Building on these findings, we then design JevAgentHarness, which fits this threshold for each choice on the agent's own trajectories and lets the LLM decide below it. Because existing decision models never see the states an agent reaches after its own mistakes, we train AgentDecision-4B, an open 4B model, on such states with Jev's answers as labels. On tasks unlike its training data, the agent solved 91.5% of them with AgentDecision-4B and 82.0% with Jev. On tasks like their training data, 4B models trained this way made agents 81.1-89.0% cheaper and up to 2.5 times faster, without losing 3 or more points of task success. The models, data, and harness will be released at this https URL.

---


### 147. [What Does History Add? Calendar Controls and Information-Timing Audits for University Trajectory Forecasting](https://arxiv.org/abs/2610.21419)

**<font color=#1a73e8>作者：</font>** Zepei Cao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We audit the predictive value of historical summaries in a rule-based university trajectory simulator. Seventeen ridge specifications and persistence separate current plans, past-state and past-plan summaries, and calendar-only history-length indicators. Across training, validation and two family-held-out evaluations, we reconstruct 16,750 routes and 804,000 monthly records. On the original 40-family set, six-month history lowers six-step normalized RMSE from 0.159234 to 0.151522, but its difference from a length-only control is -0.000895 (descriptive paired 95% interval [-0.001957,0.000248]). Fixed weights on 30 families unused in identified prior tasks reproduce this pattern: 0.156480 to 0.150074 versus current-state prediction, but -0.000558 [-0.001783,0.000728] versus the length control. These uncertain comparisons do not generalize to all-history summaries, which improve on their own calendar control. Exploratory decomposition finds clearer preparation-index and funds benefits, whereas fatigue dominates the six-month model's loss and has an uncertain length-controlled benefit. Moreover, 28.20% of its six-step fatigue predictions violate the simulator's [5,90] support. We document family dependence, prior exposure, strict temporal indexing, matched recursive references and independent numerical replay. The task conditions on recorded future plans; it does not evaluate real-student forecasts, causal action effects, autonomous planning or language-model memory. This is an evaluation audit, not a new memory architecture.

---


### 148. [Learning from Interaction Experience via Localized Context Distillation](https://arxiv.org/abs/2610.21427)

**<font color=#1a73e8>作者：</font>** Zhezheng Hao, Yongkang Yang, Xilin Xia 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning from interaction experience is essential for enabling large language models to continually improve during deployment. Context distillation offers a promising path: privileged information extracted from experience is provided to a teacher, whose behavior is then distilled into a student model that has no access to it. However, both existing forms of context distillation have limitations. Off-policy context distillation trains the student on teacher-generated trajectories and thus suffers from exposure bias; whereas on-policy context distillation trains on the student's own rollouts, whose states are often uninformative and fail to convey behaviors the student cannot yet produce. To resolve this dilemma, we introduce Localized Context Distillation (LoCD). LoCD first localizes the critical spans of a student trajectory that require revision. The teacher then regenerates only these spans from the student's own prefix, and the student is trained on the regenerated segments. LoCD thereby concentrates learning on the most informative states while keeping exposure bias low. Extensive experiments across math reasoning, code generation, and agent tasks demonstrate that LoCD consistently outperforms strong baselines and achieves more stable training with smaller and sparser parameter updates.

---


### 149. [HyCo: Hybrid Drafting for Cost-Efficient Mobile-Cloud Speculative Decoding](https://arxiv.org/abs/2610.21436)

**<font color=#1a73e8>作者：</font>** Hanbin Bae, Heejin Choi, Joohyung Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Device-cloud speculative decoding reduces server computation, but growing a deep draft tree with a small language model (SLM) requires repeated passes on a mobile neural processing unit (NPU). We present HyCo, which assigns depth to the server model's native multi-token prediction (MTP) head, executed on the device, and alternative branches to one SLM pass. The server returns the hidden state, input embedding, and key-value entries needed by the head instead of executing its sequential steps. Quantization, a restricted vocabulary, and a 1K-token window fit both drafters to the NPU. An {\epsilon}-threshold rule additionally relaxes exact preservation of the verifier's sampling distribution. In single-client runs with a Galaxy S26 Ultra over LTE/5G, HyCo reduces server GPU time per output token relative to server-side MTP self-speculation by 38.6% on Spec-Bench and 29.2% on 32K-token summarization. With the same acceptance rule, three Spec-Bench runs per system show 9.0 percentage points more saving and 1.9x delivery speed than an SLM-only drafter. HyCo differs from Cloud+MTP by +0.2 judge-score points (paired 95% CI: -0.9 to +1.3); exploratory translation favors SpecEdge-{\epsilon}. Without relaxation, HyCo exact saves 27.7% and 11.9% on the two datasets.

---


### 150. [Each Reward to Its Relevant Tokens: Reward-Specific Token-Level Credit Assignment for Multi-Reward RL](https://arxiv.org/abs/2610.21439)

**<font color=#1a73e8>作者：</font>** Skylar Zhai, Haonan Wang, Zhining Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models are increasingly trained against several verifiable rewards at once, such as the correctness and the format of a tool call, or the individual constraints of a complex instruction. Reward-decoupled normalization (GDPO) normalizes each reward separately so that different reward combinations keep distinct advantages, but it still spreads every reward's advantage evenly over the whole response, although each verifier checks only a few positions. We propose MRTPO, which assigns the advantage of each reward to the tokens relevant to it, using the information its verifier checks, without auxiliary models or token-level annotations. For each reward, the policy replays its own response with and without that reward's verifier information, and the per-token Jensen-Shannon distance between the two next-token distributions measures each token's relevance and reassigns the advantage. On text-to-SQL, multi-constraint instruction following and tool calling, MRTPO converges faster and achieves better performance than the compared methods.

---


> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-321](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
