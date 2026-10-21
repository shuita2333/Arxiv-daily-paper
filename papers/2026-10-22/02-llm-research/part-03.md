# 🧠 大模型相关研究 | 2026年10月22日

> 本类共 **299** 篇论文：已确认 **275** 篇，待复核 **24** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-299](./part-06.md)

---

### 101. [FocusOVD: Geometric and Contextual Feature Refinement for Open-Vocabulary Small-Object Detection](https://arxiv.org/abs/2610.27479)

**<font color=#1a73e8>作者：</font>** Hanlin Kou, Beiqi Bai, Li Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary object detection aims to detect both seen and unseen categories by leveraging the semantic knowledge of vision-language models. However, existing methods often struggle with small objects due to insufficient preservation of high-resolution details, ineffective information aggregation across feature levels, and limited region-level discriminability. To address these challenges, we propose FocusOVD, an open-vocabulary object detector that enhances small-object representations without modifying the frozen VLM backbone. FocusOVD introduces three complementary components: a Reweighted Cross-scale Feature Fusion module, which learns normalized level-wise weights to adaptively balance shallow appearance details and deep semantic cues during feature pyramid aggregation; a Residual Pinwheel-shaped Gated Convolution module, which strengthens local geometric responses in high-resolution features; and a Residual Convolutional Gated Linear Unit module, which suppresses background-dominated activations and enhances RoI discriminability before prediction. Extensive experiments on COCO-OVD and LVIS-OVD demonstrate the effectiveness of FocusOVD. On COCO-OVD, FocusOVD achieves a novel-category AP of 36.3%, outperforming CORA, UniDetector, and SAMP by 1.3%, 1.1%, and 1.5%, respectively; on LVIS-OVD, it achieves an overall AP of 33.7%, surpassing the strongest competing method by 0.6%. These results demonstrate the strong generalization ability of FocusOVD for open-vocabulary small-object detection.

---


### 102. [Runtime Control for AI Agents: Closing the Evaluation--Execution Gap in Operational Workflows](https://arxiv.org/abs/2610.27480)

**<font color=#1a73e8>作者：</font>** Jayesh Bhadane, Ramachandra Yerramsetti, Rajesh Gupta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-model agents increasingly participate in operational workflows where approvals, binds, and payments create commitments. An approval valid when issued may no longer authorize execution after relevant facts, evidence, policy, or authority change. We call this the evaluation--execution gap. We specify a state-bound runtime assurance layer that separates probabilistic measurement from deterministic adjudication, binds an execution allowance to the decision-relevant basis of an approval, invalidates that allowance after relevant logged changes, and rechecks admissibility at dispatch. This distinguishes the continued validity of a prior approval from a current-state policy check. We describe eight failure modes, an assurance model, a reference architecture, and prospective interventions with retrospective remediation. In a scripted 42-case replay, the state-bound configuration identifies 15 later-invalidated approvals that a deliberately non-re-evaluating point-in-time comparator does not revisit; it holds 14 affected actions before dispatch and compensates one landed effect. These results illustrate behavior under the stipulated policies and event orders, not superiority over dispatch-time enforcement designs or production effectiveness. Under explicit interception, ingestion, dependency, and serialization assumptions, the model establishes dispatch-time validity within the registered execution surface.

---


### 103. [The More the Better? A Comparison of Single- and Multi-Agent LLM Setups on a Financial Review Task](https://arxiv.org/abs/2610.27488)

**<font color=#1a73e8>作者：</font>** Pei Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Practitioner guidance holds that a large language model reviews a document better when the work is divided among agents. We test a narrow form of it in a controlled comparison of single-agent and multi-agent setups on a financial task, reviewing credit assessment memos against requirements. One agent checks six requirements in one call. A team of three on the same model checks the same memo, two requirements each, in the same words, with no roles or later stage. Labels are known for every requirement on 300 synthetic memos, so misses and false alarms are measured separately. Two primary predictions are tested on four models at a Bonferroni-corrected level. Under an instruction to decide each requirement once, the team catches 0.08 to 0.10 more of the defects that carry an explanation on the three models whose single agent misses some, at the corrected level on two. It raises more false alarms on all four, at the corrected level on three. Balanced accuracy, an exploratory measure, changes by 0.02 or less, and the team uses 2.2 to 2.4 times the tokens. Showing each agent the requirements it was not given reduces the added false alarms on the two Claude models, at the corrected level on one. In exploratory comparisons, sampling the single agent three times and flagging on any draw gives higher balanced accuracy than the team on those models, and the team's results depend on the instruction.

---


### 104. [Orthogonal Boundary Unlearning for Dual-Use Concepts in Large Language Models](https://arxiv.org/abs/2610.27490)

**<font color=#1a73e8>作者：</font>** Niccolò Ronchetti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mitigating catastrophic risks from large language models requires excising hazardous operational capabilities, such as cyberwarfare exploitation and pathogen enhancement, without degrading benign scientific utility. In these dual-use domains, legitimate defensive science and malicious attacks share vocabulary, syntax, and internal model representations, causing standard unlearning methods to induce severe collateral damage (concept bleeding).
In this work, we present Orthogonal Boundary Unlearning (OBU), a mathematically grounded framework designed to eliminate collateral damage on benign dual-use capabilities. OBU extracts a domain-matched capability subspace from paired calibration queries via singular value decomposition on empirical activation covariances, and restricts parameter updates strictly to the orthogonal null space. This guarantees that benign representations experience zero parameter perturbation along the spanned calibration subspace.
We present two complementary realizations of OBU: Projected LoRA, which applies the orthogonal constraint during iterative gradient-based fine-tuning, and Closed-Form Weight Surgery, which directly edits model weights in a single analytical step without training. Across four modern open-weight foundation models (Gemma-3-4B, Qwen3.5-4B, SmolLM3-3B, and Granite-4.2-3B), OBU achieves strong dual-use concept separation, substantially mitigates in-context priming attacks, and demonstrates durable resistance against adversarial relearning without degrading benign domain competence.

---


### 105. [Self-Evolving Agents through Privileged Retrospective Distillation](https://arxiv.org/abs/2610.27495)

**<font color=#1a73e8>作者：</font>** Yuhang Zhou, Yifan Wu, Bo Peng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-evolving agents aim to improve from their own experience rather than remain fixed after deployment, but naturally collected trajectories often lack ground-truth solutions or verifier-derived rewards. We introduce Retrospective Self-Distillation (RSD), a multi-round framework that turns such experience into dense supervision using privileged retrospective context. For each on-policy trajectory, the same underlying model acts as both student and teacher: the teacher re-scores the student's realized actions while conditioning on cross-task precedents and lessons, together with turn-level reflection and future hindsight from the completed trajectory. The resulting teacher distribution is distilled back into the policy through on-policy self-distillation. Across rounds, the experience bank grows and the retrospective context is refreshed, allowing the model, its data, and its supervision to co-evolve. We further introduce frontier-guided context-policy evolution, where a stronger frontier model proposes constrained edits to how privileged context is constructed. Across ALFWorld, ScienceWorld, and SearchQA with Qwen3-8B and Qwen3-14B, RSD improves performance by up to 59.7% relative to the base model, while frontier-guided context-policy evolution adds up to a further 44.7% relative improvement over a fixed context policy. These results show that naturally accumulated experience can be converted into persistent model capability without ground-truth trajectories or verifier-derived rewards for the core policy update.

---


### 106. [Progressive Subset Selection and Cascaded Consistency for Unsupervised Vision-Language Model Adaptation](https://arxiv.org/abs/2610.27515)

**<font color=#1a73e8>作者：</font>** Hao Yan, Guanghui Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained Vision-Language Models (PVLMs) achieve strong zero-shot recognition but often suffer performance degradation under target-domain shift. Unsupervised adaptation provides a practical way to improve target-domain performance without labeled data, but it remains challenging because pseudo-labels generated by the model can be unreliable and no labeled validation set is available for model selection or early stopping. We propose a simple framework for unsupervised PVLM adaptation that combines progressive margin-based subset selection with cascaded consistency learning. The subset selection strategy constructs a class-balanced pseudo-labeled set using prediction margins and gradually expands it during training, enabling adaptation to start from reliable supervision anchors before incorporating broader target-domain data. Cascaded consistency learning further exploits unlabeled samples by using temporally smoothed teacher predictions on weakly augmented views to supervise student predictions on strongly augmented views, with confidence filtering to reduce the influence of uncertain pseudo-labels. To preserve the pretrained embedding structure, the framework updates only normalization parameters in the visual encoder and class prototypes initialized from text prompts. Experiments across multiple recognition benchmarks with both CLIP and SigLIP backbones show consistent improvements over zero-shot baselines and competitive performance against recent unsupervised PVLM adaptation methods. These results suggest that progressive pseudo-label selection and teacher-guided consistency provide an effective and lightweight strategy for adapting PVLM classifiers without labeled target data.

---


### 107. [HealBench: A Fine-Grained Benchmark for Evaluating Psychological Comfort in Text-to-Image Generation](https://arxiv.org/abs/2610.27516)

**<font color=#1a73e8>作者：</font>** Junjie Xu, Yuzhe Yang, Rui Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite advances in photorealism, semantic fidelity, and aesthetics, text-to-image generation and image editing remain understudied in a human-centered dimension: whether their outputs feel psychologically comforting. Grounded in cognitive evaluation theory, we define psychological comfort as an affective response shaped by viewers' appraisal of restorative and emotionally supportive visual cues. We introduce HealBench, a fine-grained benchmark of 30,000 high-quality image-text pairs spanning 19 categories and 92 subcategories, selected from 100,000 candidates through a human- and expert-in-the-loop pipeline combining vision-language model matching, human preference models, expert filtering, and exemplar-guided augmentation. We also construct HealBench-Eval, a feature-clustered evaluation set of 1,095 instances. Using HealBench-Eval, we conduct objective and subjective evaluations of 14 representative image generation models and prompt-rewriting strategies. Results reveal a gap between conventional visual quality and perceived comfort: strong semantic alignment and aesthetics do not guarantee emotionally restorative images. Reinforcement learning experiments further show that HealScorer can serve as a reward signal for assessing and improving the emotional and restorative quality of generated images. These findings establish psychological comfort as a distinct dimension of human-centered image generation and position HealBench as a foundation for affect-aware generative models.

---


### 108. [When Health Assistants Agree Too Readily: A Benchmark of Time-Critical Self-Diagnosis](https://arxiv.org/abs/2610.27518)

**<font color=#1a73e8>作者：</font>** Marilyn Zhang, Tianfeng Chen, Patricia M Pechter 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Every day, more than 40 million people ask ChatGPT a health question, such as whether laptop posture explains a stiff neck and days of pounding headache. Posture is plausible, but meningitis is a time-critical possibility. We introduce SelfDx, a paired benchmark for whether models have the appropriate response behavior, a form of epistemic independence, in health questions where misplaced agreement with the user's self-diagnosis could delay urgent or emergency care. Each of 100 pairs contrasts a caution case, where a serious alternative remains possible, with an agreement case, where the user supplies evidence that rules out the alternative and it is safe for the model to agree. We find across 27 frontier models that they tend to inappropriately agree with the user's self-diagnosis in cases that require caution. Even the best current-generation model reaches only a 77.0% appropriate caution rate on time-critical condition cases. To address this gap, we experiment with three prompt variants that increase appropriate caution but reduce appropriate agreement by 9-35%, indicating excessive caution. In contrast, supervised fine-tuning on 128 balanced examples improves both rates together across three runs. We recommend post-training to improve appropriate caution without making models cautious on every case, with paired evaluation to verify both response behaviors.

---


### 109. [Less is More: Concise Retrieval and Critic-based Re-ranking for Composed Image Retrieval](https://arxiv.org/abs/2610.27538)

**<font color=#1a73e8>作者：</font>** Yuqian Zheng, Hyoju Ahn, Hyeongjin Ahn 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot composed image retrieval (ZS-CIR) aims to retrieve a target image based on a reference image and modification text. Recent approaches commonly rely on large vision-language models to generate target image captions for retrieval. However, these captions may include redundant semantic details, introducing noise when retrieving the target image and leading to suboptimal retrieval results. To address this issue, we propose Less-is-More CIR, a two-stage training-free framework that combines Concise Retrieval and Critic Re-ranking. In the first stage, concise target-oriented captions are generated that preserve only the most discriminative modification semantics, thereby reducing semantic noise in the retrieval. In the second stage, a critic re-rank module further evaluates the retrieved candidates from the perspectives of modification consistency and reference preservation. Extensive experiments demonstrate the effectiveness and robustness of the proposed framework for the ZS-CIR. Our code is available at: this https URL.

---


### 110. [EviDial: When Correct Depression Predictions Lack Evidence](https://arxiv.org/abs/2610.27541)

**<font color=#1a73e8>作者：</font>** Junjie Xu, Jin Zhu, Yuzhe Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Depression dialogue benchmarks commonly assess models by comparing predicted symptom labels with clinical scale scores. However, a prediction may agree with a benchmark label even when the dialogue lacks enough evidence to justify it. We introduce EviDial, a benchmark that distinguishes label agreement from evidence-grounded assessment. EviDial comprises 382 depression dialogues from three sources and 2,744 participant-symptom cells, each classified as having absent, partial, conflicting, or sufficient evidence. Because evidence sufficiency lacks a directly observable gold standard, we derive calibrated evidence references from multiple judgments using generalizability theory, many-facet Rasch measurement, and random-effects latent class analysis. Our audit reveals that 82.8% of participant-symptom cells lack sufficient textual evidence for the corresponding symptom assessment, with substantial variation across sources. Across model families and prompting strategies, 69.2%-96.9% of predictions judged correct by benchmark labels are nonetheless unsupported by sufficient dialogue evidence. Further analyses show that strong agreement among LLM evaluators need not reflect independent evidence judgments, underscoring the need to calibrate automated reference panels. These findings demonstrate that label-based evaluation can overestimate evidence-grounded performance by conflating agreement with clinical labels and support in the observed dialogue. EviDial provides a measurement layer for separating these constructs and auditing LLM-based depression assessment more faithfully.

---


### 111. [Act on Your Behalf, Beyond Your Authorization: Benchmarking LLM Agent Authorization Alignment](https://arxiv.org/abs/2610.27548)

**<font color=#1a73e8>作者：</font>** Zhiping Zhang, Franklin Mingzhe Li, Zihao Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When an LLM agent acts on behalf of a user, it is expected to act within the authorization scope the user grants. Existing agent evaluations largely measure task completion or harmful consequences and can therefore overlook actions that violate this delegation without producing conventional safety or privacy harms. We introduce AuthorizationBench, a benchmark of authorization alignment grounded in documented real-world cases. A scalable construction pipeline produces 286 executable tasks spanning situational triggers, the presence or absence of direct harmful consequences, and ten application domains. We execute every task with four models at two reasoning-effort settings across three agent harnesses in an authorization-aware sandbox that keeps authorized and out-of-authorization paths executable and observable, yielding 6,864 trajectories. Agents act out of authorization in 19.2% of trajectories, with rates ranging from 10.5% to 26.6% across the 24 configurations. Task completion does not imply authorization. Increasing reasoning effort leaves the aggregate rate nearly unchanged, with effects varying across models. On controlled pairs, agents act out of authorization at similar rates with (17.9%) and without (20.8%) direct harmful consequences, and more often under benign pressures than malicious injections (23.5% versus 17.6%, p=0.002). Our results show that task capability, additional reasoning, and consequence-oriented safety evaluation do not by themselves ensure authorization alignment. Moreover, agents that consult the principal before completing a task exhibit lower rates of out-of-authorization behavior (14.0% versus 21.6%, p<0.001), pointing to a tension between agent autonomy and preserving users' decision authority that calls for further human-centered study. Dataset and code are available at this https URL .

---


### 112. [Lower Bounds for Smooth Nonconvex Zeroth-Order Optimization: The Price of Determinism under Low Curvature Trace](https://arxiv.org/abs/2610.27550)

**<font color=#1a73e8>作者：</font>** Yuxing Peng, Zhiqing Tang, Weijia Jia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low curvature trace, an effective rank condition, is a common explanation for why randomized zeroth-order methods scale to high-dimensional tasks such as language model fine-tuning. Can deterministic methods achieve the same savings? We show that they cannot. We study finding $\varepsilon$-stationary points of $L$-smooth nonconvex functions on $\mathbb{R}^d$ from exact function values, assuming that below the starting value the Hessian is dominated by a fixed matrix with trace at most $LE$; this is the effective rank condition used to explain zeroth-order fine-tuning. When $ET\le d$, the Gaussian two-point method that such fine-tuning uses needs only $O(ET)$ calls if it rejects steps that raise $f$, where $T=L\Delta/\varepsilon^2$ is the iteration count of gradient descent from initial gap $\Delta$, and we prove that every randomized method needs $\Omega(ET)$ calls, so this cost is optimal up to constants. In contrast, every deterministic method needs $\widetilde\Omega(d\min\{T,\sqrt{ET}\})$ calls, and adaptive subspace search attains $O(d\min\{T,\sqrt{ET}\})$: a deterministic method pays about $d$ calls per discovered direction, and the trace budget allows about $\sqrt{ET}$ directions. Determinism thus multiplies the cost by a factor of order $d/(E+\sqrt{ET})$ up to logarithmic factors, which grows linearly with $d$ for fixed $E$ and $T$; once $E$ exceeds $T$ by a logarithmic factor, deterministic methods need $\Omega(dT)$ calls, as without any trace budget. Our lower bounds hold for $C^\infty$ functions with the matrix bound on all of $\mathbb{R}^d$, even when each call also returns gradient projections priced by rank.

---


### 113. [Can Native Safety Travel? Reusing Safety Pretraining Across Models via On-Policy Distillation](https://arxiv.org/abs/2610.27555)

**<font color=#1a73e8>作者：</font>** Bingqi Shang, Yang Zhang, Yiwei Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safety pretraining has emerged as a promising paradigm for embedding safety deeply into a model during pretraining, yielding robustness to subsequent fine-tuning that conventional safety post-training often lacks. We refer to this safety acquired during model pretraining as native safety. Yet native safety is expensive to acquire, confined to the model in which it was pretrained, and often accompanied by lower general utility. In this work, we rethink the practical value of safety-pretrained models and introduce, for the first time, the native safety reuse problem: Can native safety be transferred from a specialized, potentially smaller, safety-pretrained "teacher" to standard-pretrained "students," enabling them to inherit its robustness while preserving their general utility? We show that native safety can "travel" through on-policy distillation. A standard-pretrained student generates responses to safety-pretraining prompts, while a small safety-pretrained teacher supervises the student's token-level predictions along its own generated trajectories; cross-tokenizer alignment further enables transfer across model families. The resulting students exhibit substantially greater safety robustness than their safety-post-trained counterparts while retaining higher general utility than the teacher: subsequent fine-tuning raises the average attack success rate (ASR) of the 1.7B student by only 5.00%, compared with 11.58% for safety post-training, and its average utility of 48.20% far exceeds the aligned teacher's 27.42%. Unlike conventional large-to-small knowledge distillation, our framework enables selective, small-to-large safety transfer: it reuses the robust safety expertise of a smaller pretrained teacher without inheriting its utility limitations. These findings establish native safety as a reusable model property rather than one permanently tied to the originally pretrained model.

---


### 114. [Exploring Recurrent-Depth Language Models for Multitask Clinical Text Processing](https://arxiv.org/abs/2610.27559)

**<font color=#1a73e8>作者：</font>** Xi Yang, Guodong Liu, Cheng Peng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical natural language processing includes diverse tasks such as information extraction, classification, and question answering. Developing one model for all tasks could simplify deployment and improve knowledge transfer. We evaluated whether small recurrent-depth language models can meet this need through joint fine-tuning and compared their performance with standard transformers. We fine-tuned Ouro1.4B-Thinking, Ouro-2.6B-Thinking, HRM-Text-1B, Qwen3-1.7B, and Qwen3-8B on 9 datasets covering information extraction, classification, inference, and question answering, and evaluated them on four additional datasets excluded from training. Across these 13 datasets, Ouro-1.4B-Thinking achieved higher performances than Qwen3-1.7B on 11 datasets; Ouro-2.6BThinking was competitive with Qwen3-8B on most tasks. Ouro models showed the largest gains on inference and question answering, whereas HRM-Text-1B showed mixed results. These findings support further study of recurrent-depth models for clinical tasks through controlled experiments to isolate architectural effects and investigate how recurrent computation influences reasoning, knowledge acquisition, and generalization.

---


### 115. [AnomalyJev: Towards Evaluating Image Anomaly Explanations via Claim-Level Verification](https://arxiv.org/abs/2610.27565)

**<font color=#1a73e8>作者：</font>** Qizhou Wang, Jiawen Zhu, Guansong Pang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent multimodal LLM (MLLM)-based anomaly detection (AD) methods can generate textual explanations that help interpret their predictions. However, reliably and efficiently evaluating these explanations remains challenging. While LLM judges can assess explanations through structured rubrics, they often require substantial token generation, making evaluation costly and difficult to scale. We instead propose to anchor evaluation in the available ground truth by extracting verifiable claims from each explanation and verifying them against the corresponding annotations. We instantiate this idea as AnomalyJev, a lightweight framework that extracts verifiable claims from contextualised representations using ground-truth-defined queries and pointer based heads, without token generation. The claims are then verified against the ground truth to score faithfulness and completeness. For evaluation, we construct a human-annotated set of 640 explanations with over 1,600 expert ratings across in-domain and cross-dataset settings. Despite its compact design, AnomalyJev achieves stronger agreement with human annotators than most open MLLM judges and approaches that of flagship MLLM judges, at a fraction of their runtime and resources.

---


### 116. [Learned Readout Tokens for Extracting Large Language Model Confidence](https://arxiv.org/abs/2610.27566)

**<font color=#1a73e8>作者：</font>** Nima Seifi, Martin Ester  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used within everyday applications where their responses have significant downstream impacts. For responsible deployment of such systems, we desire insight into how much we can trust their individual outputs. A popular approach for estimating LLM confidence is to train probes on the hidden states of the LLM's tokens to predict the correctness of the model's output. These probes typically read hidden states from tokens that are already in the model's vocabulary. In this work, we introduce a new approach to confidence probes that learn a new readout token and utilize its hidden states to train the probe. We show that our learned readout approach ScratchProbe outperforms its existing-token counterpart on a variety of datasets and LLMs. We also extend our method to a multi-token approach which we show provides further performance improvements. Finally, since the learned readout changes only the position a probe reads from, any existing probe can adopt it. Applied to a state-of-the-art probe, it improves AUROC on every backbone, in domain and out of domain.

---


### 117. [AudiPsy: Evidence-Grounded Multimodal Reasoning over Spoken Counseling Conversations for Depression Assessment](https://arxiv.org/abs/2610.27567)

**<font color=#1a73e8>作者：</font>** Chuanbo Zhu, Run Luo, Weibo Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Depression assessment from counseling speech requires integrating textual and acoustic psychological evidence across turns, yet existing end-to-end classification approaches lack explicit multimodal evidence interpretation and context-aware reasoning. We propose AudiPsy, an evidence-grounded omni-LLM for depression assessment over spoken counseling conversations. AudiPsy employs an Observation-Assessment-Summary (OAS) paradigm to integrate dialogue transcripts, textual and acoustic emotions, and textual-acoustic emotion incongruence into structured reasoning. OAS incrementally organizes multimodal observations, performs contextualized assessment, and maintains an evolving dialogue summary for subsequent turns. To support this framework, we construct AudiPsy-Counsel, a synthetic spoken counseling conversation corpus with multimodal context augmentation, and develop a unified three-stage curriculum for depression-oriented reasoning. Experiments on DAIC-WOZ demonstrate superior depression assessment performance over specialized depression detection methods and general-purpose speech/omni-LLMs, along with improved reasoning quality, while supplementary evaluation on EATD-Corpus supports AudiPsy's applicability to naturalistic conversations.

---


### 118. [When LLMs Manipulate: Measuring Behavioral, Social, and Temporal Effects](https://arxiv.org/abs/2610.27573)

**<font color=#1a73e8>作者：</font>** Sadia Asif, Israel Antonio Rosales Laguan, Shumaila Asif 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can influence user trust and decision-making through subtle linguistic cues, yet the behavioral effects of manipulative outputs remain poorly quantified. We introduce a behavioral computing framework for measuring \textit{behavioral vulnerability}, defined as users' susceptibility to manipulative AI responses. Building on DarkPatterns-LLM benchmark, we generate controlled manipulative stimuli using Manipulation Gradient Descent (MGD), targeting biases associated with authority, urgency, and social proof. We analyze participant responses using the Multi-Stakeholder Impact Assessment Network (MSIAN) to model cross-user influence and the Temporal Harm Propagation Model (THPM) to characterize the persistence of behavioral effects over time. In a study involving 120 participants, manipulative framing produced significant changes in trust calibration and compliance ($p < 0.01$), with effects also propagating across social contexts. These findings highlight the need to extend LLM safety evaluation beyond model outputs to measurable behavioral consequences and provide a computational framework for quantifying individual, social, and temporal risks arising from manipulative AI interactions.

---


### 119. [The Show-Up Attack: When Subagents Win Over Their Supervisor](https://arxiv.org/abs/2610.27574)

**<font color=#1a73e8>作者：</font>** Maosen Zhang, Jianshuo Dong, Yutong Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems are increasingly deployed to coordinate multiple large language model (LLM) agents. However, this also creates new attack surfaces: malicious agents may have chances to exploit the coordination. In this paper, we propose and study the \textit{show-up attack}, in which a malicious subagent manipulates the supervisor into involving it in tasks beyond its assigned scope. To evaluate this risk, we propose SUA-Arena, which implements 6 attack strategies and contains 188 test cases. Then, we evaluate 6 frontier LLMs and find that all of them are vulnerable to show-up attacks. For example, GPT-5.6-Sol as a supervisor suffers an ASR of up to 0.93. Mitigation strategies such as prompting and restricted communication fail to reduce the risk consistently. These results show that multi-agent systems need explicit mechanisms for enforcing authority boundaries.

---


### 120. [Why Static Probes Fail: Context Determines Deception Feature Composition](https://arxiv.org/abs/2610.27577)

**<font color=#1a73e8>作者：</font>** Yao Huang, Siyuan Chen, Zhenghan Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With increasing autonomy, Large Language Models (LLMs) may engage in deceptive behaviors, such as scheming to pursue misaligned goals or sandbagging to escape oversight. Monitoring outputs alone is insufficient, as models can produce seemingly benign responses while harboring misaligned internal objectives. While mechanistic approaches like linear probing are promising, they rely on the assumption that deception corresponds to a single direction in representation space. We demonstrate that such single-direction probes fail to generalize across diverse deception scenarios. To bridge this gap, we propose representing deception as a multi-dimensional subspace rather than a single direction. Our method utilizes iterative orthogonal decomposition to identify complementary directions that capture distinct facets of deceptive intent. To effectively leverage these directions for detection, we find that static combinations prove brittle due to strong domain dependence across different scenarios. We therefore introduce a domain-adaptive gating mechanism that dynamically composes the extracted directions through few-shot adaptation at test time. With only 10 examples, our approach achieves an average AUROC of 0.97 and 94% recall at 5% FPR across all evaluated datasets, substantially outperforming existing methods.

---


### 121. [Factual Access States in Diffusion Language Models: From Mechanism to Knowledge Editing and Retrieval](https://arxiv.org/abs/2610.27580)

**<font color=#1a73e8>作者：</font>** Yuchen Guo, Zhuoyuan Mao, Yiwen Guo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Factual recall is a lookup: some representation inside the network serves as the key, and what that key is made of decides which queries can retrieve the fact, what an edit must cover, and what a retriever can read. We call it the factual access state. In autoregressive (AR) models the subject position enriches attributes largely independently of the relation, and relation-specific selection happens later, at the readout position. In masked diffusion language models (DLMs) we find the state is assembled differently, and much earlier: in the first attention layer the wording of the relation is routed into the position of whichever entity is visible and the early feed-forward layers look the fact up on this fused representation. The state therefore varies with the relation's surface form and with the query direction, so the queries about one fact occupy a region of state space rather than a point, and an operation on the fact succeeds only for queries that enter it. We treat the state as an interface to a DLM's factual knowledge, and put it to two uses. Writing to the state gives a knowledge editor: from one declarative statement, Multi-View Edit fits one shared value per direction across that region and installs it in the early-MLP block, preserving source-prompt reliability while substantially improving paraphrase and reverse question answering, where AR editors gain near zero. Reading it suggests a complementary use: the state at each entity position can serve as a relation-specific retrieval vector with no training, returning both pieces of evidence for two-entity queries on which pooled, prompted and lexical retrievers almost never return both.

---


### 122. [DuplexLedger: Benchmarking Transactional Memory in Full-Duplex Speech Agents](https://arxiv.org/abs/2610.27581)

**<font color=#1a73e8>作者：</font>** Yuxuan Li, Xiangchen Guan, Kunrong Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Full-duplex speech agents must update persistent memory while listening and speaking, yet it remains unclear which events should be stored, revised, or excluded. Existing benchmarks isolate interaction timing from memory outcomes, obscuring the state transitions behind a correct answer. We introduce DuplexLedger, a bilingual benchmark of 1,094 persistent sessions aligning four full-duplex scenarios with event-level Write/Update/Ignore/Retain supervision, explicit pre/post memory states, and 6,564 same-session questions and checks. Evaluating five full-duplex models reveals an interaction-memory gap: no system combines strong boundary control with coherent final-state memory, and the best final-state fact coverage is 2.01%. We propose ACT-Mem, an 8.92M-parameter sidecar comprising an event controller, a versioned transactional ledger, and a typed retriever coupled with a frozen MiniCPM-o 4.5 backbone. On 219 held-out sessions, ACT-Mem increases latest-value accuracy from 4.11% to 8.68% while reducing stale assertions and distractor adoption. It improves interaction boundaries but slows interruption stopping. These results motivate selective, auditable full-duplex memory rather than indiscriminate transcript retention. Code is available at this https URL.

---


### 123. [TeCoP: Accelerating Diffusion Large Language Model Decoding via Tentative Context Pipelining](https://arxiv.org/abs/2610.27583)

**<font color=#1a73e8>作者：</font>** Jui-Chien Tsou, Hsuan-Chi Liu, Wei-Chin Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) predict multiple token positions per forward pass, yet block-wise decoders serialize generation and repeatedly recompute stable predictions. We attribute this inefficiency to coupling a prediction's readiness for irreversible commitment with its utility as context. We introduce Tentative Context Pipelining (TeCoP), a training-free decoder that decouples these roles through staggered block-parallel pipelining and draft-and-verify. TeCoP reuses stable but uncommitted predictions as provisional cross-block context, with commitment governed by confidence and stability checks. Across four LLaDA and Dream dLLMs on GSM8K, Minerva MATH, and MBPP, TeCoP reduces number of forward evaluations by up to 87% and achieves up to 7.50-fold throughput without KV caching and 11.77-fold with caching over the uncached original decoder. It outperforms Fast-dLLM and DSB in throughput across all 12 model-benchmark settings, with and without caching, while keeping average cached accuracy within one percentage point of the original decoder.

---


### 124. [Beyond Model Weights: Sampling-Dependent Fairness in Diffusion Language Models](https://arxiv.org/abs/2610.27584)

**<font color=#1a73e8>作者：</font>** Koshiro Saito, Diasuke Oba, Danushka Bollegala 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) are emerging as a practical alternative to autoregressive language models (ARLMs), yet their fairness remains largely uncharacterized. DLMs introduce sampling controls with no direct autoregressive counterpart, such as block length and remasking strategy, that directly set their speed--quality operating point. This raises a basic question: does a DLM's measured social bias remain stable across these settings? Across LLaDA, LLaDA-1.5, and Dream on Open-BBQ, we find that all three models exhibit social bias, but both the magnitude of measured bias and the relative ordering of models by bias are highly sensitive to the sampling configuration. This sampling dependence also changes what successful debiasing means. While mitigation strategies established for ARLMs transfer effectively to DLMs and reduce bias without degrading downstream performance, sampling dependence persists even after mitigation. Our results show that fairness in DLMs cannot be characterized independently of the sampling configuration, even after debiasing. Project page is available at this https URL.

---


### 125. [Beyond Experience: Knowledge-Guided Evolution for NPU Kernel Generation](https://arxiv.org/abs/2610.27588)

**<font color=#1a73e8>作者：</font>** Xi Chen, Ming Shen, Haotian Yan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents have become capable kernel engineers on mainstream GPU stacks, but they struggle on emerging accelerators such as Ascend NPUs, whose programming model is barely represented in pretraining data. Recent NPU agents address this gap largely through experience: they accumulate memory from their own generation and optimization trials and reuse it on later tasks. We argue that experience alone is not enough for kernel generation. An agent can only remember what it has tried, and it rarely tries a mechanism it does not know. As a result, such memory offers little help when a new operator calls for a different mechanism, and even familiar operators raise unseen situations as optimization proceeds. We present ASCENDEVOLVE, which grounds every step of an evolutionary kernel search in a large external knowledge base built from platform documentation, toolkit headers, and operator repositories. Because this corpus far exceeds any context window, ASCENDEVOLVE indexes it and routes each agent to a small, task-specific slice of evidence instead of the corpus itself. The retrieved knowledge seeds diverse implementation strategies, guides repair when a candidate fails, and constrains how strong candidates are recombined. On 53 Ascend C operators from CANN-Bench spanning four difficulty levels, ASCENDEVOLVE achieves an overall score of 71.39, improving over Reflexion and OpenEvolve by 11.6% and 17.2%.

---


### 126. [Meta Expert: Cross-Layer Expert Sharing for Storage- and Retrieval-Efficient MoE](https://arxiv.org/abs/2610.27598)

**<font color=#1a73e8>作者：</font>** Ermo Hua, Xiangyu Hong, Baiting Wu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As model parameters scale up, sparsely activated Mixture-of-Experts (MoE) approaches have become essential for model scaling. However, mainstream models currently adopt hierarchical architectures, where experts in different layers, although topologically independent, exhibit substantial similarity and redundancy in their stored content. Compared to the hierarchically arranged \textbf{Local Expert} in existing mainstream models, we hypothesize that inter-layer shared \textbf{Meta Expert} hold greater potential. To this end, we conduct a multi-dimensional empirical comparison between Local and Meta Experts, and find that models incorporating Meta Experts exhibit lower parameter redundancy, together with lower cross-entropy loss and higher downstream task accuracy. With the activated quantity and the expert granularity held fixed, \textbf{our model matches the performance of Vanilla MoE using only 70--80\% of the experts}, substantially improving the model's scaling potential. Beyond removing inter-layer redundancy among experts and improving information storage efficiency, our theoretical analysis further shows that, compared with Local Experts, Meta Experts provide hidden states with more flexible residual pathways, thereby improving information retrieval efficiency.

---


### 127. [Self-Decomposing Diffusion for Code Generation](https://arxiv.org/abs/2610.27600)

**<font color=#1a73e8>作者：</font>** Lize Shao, Zichen Xie, Zhizhen Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) are emerging as a promising paradigm for code generation, offering the potential for fast, parallel decoding. However, generating complex programs remains challenging, as their interdependent components must maintain consistent interfaces, data flows, and shared assumptions. Aggressive parallel decoding can compromise these dependencies and undermine program correctness, while conservative decoding sacrifices efficiency. To address this trade-off, we propose planning program decomposition before implementation to coordinate interdependent units during parallel generation. We introduce Self-Decomposing Diffusion for Code (SDDC), a novel framework that decomposes complex programs and implements their units in parallel, entirely through diffusion. SDDC first generates a contract specifying the program's decomposition and inter-unit dependencies, then uses it to guide coordinated parallel implementation. Across five benchmarks and two 7B diffusion backbones, SDDC substantially improves the accuracy--latency trade-off, raising pass@1 by up to 31.1 percentage points while decoding 7.5--13.7$\times$ faster than the base models, and outperforming a fine-tuning baseline by up to 23.5 points with lower latency.

---


### 128. [From Encoding to Generation: Towards Empathetic Large Language Models](https://arxiv.org/abs/2610.27603)

**<font color=#1a73e8>作者：</font>** Samhita Bollepally, Takashi Yamauchi, Marissa West  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Empathetic interaction involves two distinguishable capacities: representing another person's emotional state (cognitive empathy) and generating an appropriate response to that state (affective empathy). We apply this distinction to examine how emotion-related information is internally organized, selectively attended to, and carried through response generation in Llama-3.2-3B-Instruct across 10 emotion categories from the EmpatheticDialogues dataset. Layer-wise linear probing revealed a broad middle-layer region of peak emotion-category decodability, with the layer-11 L2 probe achieving 63.6% held-out accuracy against a 10% chance level and a 54.6% TF-IDF lexical baseline. During response generation, emotion-related user tokens received 1.89 times as much attention per token as other utterance tokens, concentrated across layers 10-15. Target-emotion alignment then decreased from a mean cosine similarity of 0.239 for input representations to 0.125 for generated responses, with positive drift in 77% of examples and the largest shifts for angry and furious. Emotion-category representation, attention allocation, and response-level alignment therefore emerge as distinguishable components of model processing that can be analyzed through a functional cognitive-affective empathy framework. These findings provide a foundation for monitoring emotion representations during generation and leveraging models' existing affective structure to support more naturally empathetic responses without relying on external prompting or explicit emotion conditioning.

---


### 129. [Auditing the Product, Not the Recursion: The Evaluation Evidence Behind Recursive Self-Improvement Claims](https://arxiv.org/abs/2610.27610)

**<font color=#1a73e8>作者：</font>** Zihan Chen, Di Zhu, Lei Nico Zheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement (RSI) promises AI systems, such as self-evolving LLM agents, that become better at producing further improvements. Evaluating this promise requires separating product claims about the final system from process claims about the improvement process itself. Existing surveys specify the evidence these claims require, but how often studies report that evidence remains unmeasured. We examine this question through full-text coding of 114 eligible studies in a reproducible arXiv search frame frozen in October 2026, including 90 that describe their own systems as RSI. The codebook links claims to evaluation designs. Independent human coding, third-reader adjudication, and a separate blind coding of improver comparisons assess coding reliability. Among the 90 RSI studies, 90% report product evaluation beyond development tasks under a broad criterion that includes partial or unstated separation, while 60% report evaluation on tasks unused for selection. Only 22% audit two or more reruns of the full loop. In a human-coded random sample, the RSI studies show the same contrast: 45% evaluate on tasks unused for selection and 14% audit two or more reruns. Of the 26 studies claiming a better improvement procedure, 23 report a related comparison, but only 4 compare earlier and later procedures from identical starting artifacts at a matched budget. Across these results and a comparison set of established works, evidence for repeatability and improved procedures remains less developed than product evaluation. Three propositions explain how selection effects, shared evaluator errors, and changes in system state limit what product evaluations can establish. Together, the findings support a claim-indexed reporting standard that connects each claim to the evaluation design needed to test it.

---


### 130. [ABench: Adversarily Benchmarking Large Language Models across Taxonomized Values](https://arxiv.org/abs/2610.27611)

**<font color=#1a73e8>作者：</font>** Liping Yang, Yongqi Leng, Jingting Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ensuring the alignment of Large Language Models (LLMs) with diverse cultural values is critical for their safe global deployment. However, existing alignment benchmarks are predominantly English-centric or confined to simple discriminative tasks. Moreover, they often fail to effectively evaluate model robustness against complex, adversarial inductions within specific cultural contexts. To address these limitations, we propose ABench, a fine-grained, handcrafted benchmark specifically tailored to taxonomized values in Chinese. Grounded in a rigorous hierarchical taxonomy comprising 158 derived value subcategories, ABench consists of 2,895 open-ended questions. These questions employ techniques such as role-playing and logical traps to probe the stability of models' stances in adversarially induced contexts. Furthermore, we propose a weighted automated evaluation framework that utilizes question-specific scoring criteria for nuanced assessment. Extensive experiments on 16 mainstream LLMs reveal that most models exhibit significant vulnerabilities when subjected to sophisticated adversary attacks on values (scoring below 60). This underscores the need for more robust, culturally specific alignment strategies. Our data will be publicly released to promote further research on taxonomized value alignment.

---


### 131. [Local Allow, Global Deny: Why Per-Action Authorization Does Not Compose in LLM Agents](https://arxiv.org/abs/2610.27620)

**<font color=#1a73e8>作者：</font>** Anmol Pandey, Aditya Jain, Liang Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous LLM agents act through tools under per-action authorization: a local guard screens each tool call in isolation. We show that local authorization does not compose into global authorization. A compositional authorization failure (CAF) is a locally authorized execution, or a pair of locally authorized executions, that violates a global policy spanning intent, purpose, provenance, consent, and delegation. We characterize CAFs along two axes, expressiveness (single-trace safety versus relational k-safety) and observability (a ladder of monitor profiles). Our central result is an impossibility: relational purpose violations form a 2-safety hyperproperty with no per-trace locus of blame, so a per-action monitor that never raises a false alarm detects none of them, independent of the underlying model or decision procedure; they become visible only under cross-execution monitoring, which none of the six guardrails we survey implements. We make this constructive with AL-SYNTH, a SAT/SMT synthesizer (using no language model) that emits minimal CAF witnesses, each checked against an exhaustive oracle. The empirical signature is sharp: across nine LLM judges the per-action view approves the synthesized witness almost without exception, blocking it at a rate comparable to a benign control, yet the same models flag it when shown the two executions together. Per-action authorization is therefore structurally insufficient for relational policy conjuncts not reducible to single-trace safety: to bound them, a monitor must compare executions or accept false alarms.

---


### 132. [From Outcomes to Steps: Reliable Success-Aware Critic Learning for Long-Horizon Language Agents](https://arxiv.org/abs/2610.27623)

**<font color=#1a73e8>作者：</font>** Jiaxi Liu, Shixiong Kai, Zhentao Tang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning for long-horizon language agents requires identifying whether intermediate actions make eventual task success more or less likely when supervision is available only at trajectory level. The main difficulty is that a critic with aggregate return-prediction accuracy may still fail to resolve the local value differences needed to assign credit to actions, especially under sparse feedback and function approximation. Conventional critics estimate future return, but policy improvement also depends on knowing whether each intermediate decision makes task success more or less likely. We introduce SCALE, an actor-critic framework that augments conventional return estimation with explicit prediction of eventual task success. At each interaction prefix, the critic predicts a return value and a Success Value, defined as the probability that the task will eventually be completed from that prefix. SCALE converts changes in Success Value into multi-step action credit through Success-GAE and modulates its contribution according to the estimated reliability of the predictor, while retaining the token-level PPO objective. Across five agent benchmarks and three model backbones, SCALE improves task performance over the compared RL baselines in most settings, with gains of up to 4.1 percentage points in success rate. Separate critic-learning analyses show that SCALE also improves critic estimation and training stability.

---


### 133. [TriGeoBench: A Multimodal Mathematical Geometry Benchmark with Figures and TikZ](https://arxiv.org/abs/2610.27626)

**<font color=#1a73e8>作者：</font>** Jing Wang, Yitong Yang, Hao Dou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models show strong vision-language capabilities, yet their geometry-centric reasoning remains insufficiently understood. Existing mathematical benchmarks typically rely on rasterized figures and cover limited geometric knowledge areas and response formats, making it difficult to assess whether models reason over geometric structures or exploit superficial visual patterns. We introduce TriGeoBench, a geometry-centric multimodal benchmark constructed from Chinese middle- and high-school mathematics examinations. TriGeoBench contains 7,000 question-answer pairs and 12,235 geometric figures with TikZ code, spanning plane geometry, solid geometry, analytic geometry, function, and vector geometry across diverse response formats. Each instance forms a {question-answer pair, image, TikZ} triplet: question-answer pairs are stored in LaTeX, images as RGB figures, and TikZ preserves geometric topology, symbolic annotations, and relational structure. We evaluate representative open- and closed-source MLLMs through image-to-TikZ and multimodal reasoning probes. Results reveal persistent fine-grained structure and image-text alignment challenges. Oracle experiments with human-curated reference TikZ suggest that accurate executable representations provide complementary geometric cues; they do not evaluate an end-to-end conversion pipeline. TriGeoBench offers a testbed for structure-aware mathematical reasoning.

---


### 134. [PAR: Progress-Aligned Recurrence for Length Generalization in State Tracking](https://arxiv.org/abs/2610.27628)

**<font color=#1a73e8>作者：</font>** Pan Wang, Yihao Hu, Guangyuan Dong 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Looped language models can run more iterations at test time, but additional iterations need not help them solve longer problems. For sequential state tracking, final-answer supervision does not specify how far each iteration should advance, and repeated updates can change the scale of the recurrent state. We introduce \textbf{Progress-Aligned Recurrence (PAR)}, which trains the prediction at iteration $k$ to match the state after the first $k$ operations and rescales recurrent states to their first-iteration norms. On swap-$S_5$, a Qwen2.5-0.5B model trained on at most 32 moves achieves 95.5\% mean full-state accuracy at 512 moves, or $16\times$ the training length, compared with 55.7\% reported for RLT and 0.8\% for explicit chain of thought on the same backbone. Controlled $S_5$ ablations show that removing norm anchoring reduces the extrapolation factor from $16\times$ to below $2.2\times$, and replacing progress-aligned targets with final-answer supervision reduces it to at most $8\times$. A learned completion readout selects when to answer without a supplied stopping depth. When intermediate labels are unavailable, prefix self-distillation induces the correspondence from shorter problem prefixes using only final answers. The gains apply across sequential state-tracking tasks, establishing the task structure required for depth extrapolation. These findings support training intermediate predictions and state scale together to make additional recurrent depth useful for longer problems.

---


### 135. [SCODEL: Shared Canonical Ontology Definitions for Food Entity Linking and Ontology-Grounded Recipe Knowledge Graphs](https://arxiv.org/abs/2610.27637)

**<font color=#1a73e8>作者：</font>** Nuhu Ibrahim, Rishi Ravikumar, Ayuba Dauda 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Identifying recipe entities and linking them to ontology concepts is fundamental for semantic recipe understanding. However, food mentions in recipes are often ambiguous, context-dependent, and lexically diverse, making ontology entity linking (EL) challenging. We propose SCODEL, a streamlined, model-agnostic approach based on a central idea: contextual food mentions and ontology concepts that refer to the same entity should learn the same canonical ontology-oriented definition. SCODEL uses these shared definitions as a semantic normalisation layer, providing complementary semantic information to existing EL models without requiring a new linking architecture. We further introduce ReciLinkD, the first benchmark for contextual food ontology entity linking in recipes. Experiments show that SCODEL consistently improves three modular EL models (ReFinED, GSM-EL, and BLINK): SCODEL x BLINK achieves the highest Hit@1 on seen concepts (88.33%), while SCODEL x GSM-EL achieves the highest Hit@1 on unseen concepts (83.15%), outperforming the strongest large language model (LLM) based EL baseline in each setting. Experiments on a biomedical ontology benchmark further demonstrate that SCODEL generalises beyond the food domain. Finally, we use SCODEL to ground food mentions at scale and construct an ontology-grounded recipe knowledge graph, demonstrating its utility for ontology-aware recipe retrieval and corpus-level food analysis.

---


### 136. [BCT: Bayes-Consistent Tempering for Flow Language Models](https://arxiv.org/abs/2610.27641)

**<font color=#1a73e8>作者：</font>** Daisuke Oba, Hiroki Furuta, Naoaki Okazaki  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temperature scaling is typically applied as a post-hoc transformation of model probabilities. In posterior-induced flow language models, this creates two mismatches. First, posterior tempering implicitly changes both the endpoint distribution and the distribution of intermediate noisy states, while the denoiser remains trained on the original states. Second, the tempered posterior weights are combined with transport dynamics derived for the untempered flow. These mismatches are reflected empirically: lowering temperature improves GSM8K performance much less reliably in flow LMs than in discrete diffusion LMs. We introduce Bayes-Consistent Tempering (BCT), which makes temperature explicit in both the distributions and dynamics of the generative flow. Its learned realization trains the denoiser on tempered intermediate states and tempers the endpoint distribution using the corresponding tempered dynamics. We also derive training-free variants for conventionally trained checkpoints. Across hyperspherical flow LMs with two denoiser architectures and a von Mises--Fisher flow LM, BCT improves GSM8K generation across broad temperature ranges and achieves the strongest tempering performance. The gains also extend to Sudoku, demonstrating benefits on tightly constrained generation. At very low temperatures, the learned realization is also markedly more robust than the training-free variants, supporting temperature as a property of the generative flow across training and inference rather than a post-hoc probability adjustment. Code and model weights are available at this https URL .

---


### 137. [CUA-Recovery: Benchmarking Error Recovery in Long-Horizon Computer-Use Agents](https://arxiv.org/abs/2610.27645)

**<font color=#1a73e8>作者：</font>** Xu Hu, Haoming Li, Yuxiang Wang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As computer-use agents (CUAs) move to long-horizon workflows spanning multiple applications, undetected errors can silently corrupt persistent state and cause cascading failures in subsequent actions. Reliable error detection and recovery have become critical bottlenecks for building robust CUAs. However, existing benchmarks focus primarily on end-to-end task performance, providing limited insight into whether agents can detect and recover from errors during execution. The few benchmarks that evaluate recovery rely largely on manually injected errors, which may not reflect the types or horizons of failures induced by real agent policies. We introduce CUA-Recovery, a benchmark comprising test and training suites across multiple desktop applications. We construct it using ReRail, a framework for synthesizing long-horizon tasks and trajectories in a persistent desktop environment. ReRail composes MyPCBench tasks into new long-horizon workflows with executable ground truth, collects verifier-confirmed failures from multiple policies, and turns them into verified recovery trajectories. CUA-Recovery comprises a human-verified test suite of 2,250 erroneous states over 100 tasks and a training suite of 8.6K trajectories over 377 tasks. Evaluation on the test suite shows that agents struggle both to recognize inherited errors and to complete the task. Across six agents and six takeover depths, Error Awareness Rate (EAR) reaches at most 44.0% and Pass@3 at most 25.5%. After fine-tuning Qwen3.5-35B-A3B on the training suite, its average EAR rises from 19.9% to 35.2% on held-out recovery states, and its Rubric Score goes from 5.0% to 16.1%. It also gains 15.3 points on MyPCBench and 10.8 points on Odysseys for Pass@3, showing that the training trajectories help both with recovery and with completing tasks from a clean start. Our code is available at this https URL.

---


### 138. [Speak vs. Know: Balancing Behavior and Knowledge Distributions of Large Language Models](https://arxiv.org/abs/2610.27648)

**<font color=#1a73e8>作者：</font>** Yang Liu, Masahiro Kaneko, Chenhui Chu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent work reports that the distribution verbalized directly in the output text aligns far better with human opinion distributions than the next-token log-probability distribution of LLMs. However, the verbalized distribution reflects what LLMs know about a group's opinions (knowledge distribution), while what they actually output at deployment is governed by their log-probability distribution (behavior distribution). We find that when prompting LLMs to predict the opinion of a specific group, the most likely answer under the verbalized distribution differs from that under the log-probability distribution for 37% of World Values Survey questions, averaged over three LLMs. Thus, LLMs' knowledge does not match their behavior. This matters for evaluation: a verbalized distribution can score well against a group while its most likely answer is one the model never outputs, so the score no longer describes the model. The alignment scores for these two distributions reflect only the model's behavior or its knowledge, separately. We therefore propose a learnable combination of the two distributions that follows the most likely answer of the behavior distribution while preserving the shape of the knowledge distribution, with a single hyperparameter trading off behavioral fidelity against distribution quality. Our experiments on three opinion survey datasets and six models show that the balanced distribution improves behavioral consistency over the verbalized distribution from 71.6% to 95.6% on average, while the total variation distance to the human opinion distributions rises only slightly from 28.8% to 33.8%, and it remains effective under temperature scaling and cross-dataset settings.

---


### 139. [Corpus Quality Improves, Retrieval Utility Does Not: An Ablation of Preprocessing and Refinement in a Speech-to-QA Pipeline](https://arxiv.org/abs/2610.27652)

**<font color=#1a73e8>作者：</font>** Wonsup Shin, Jingu Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Practitioners building training corpora with a pipeline of language models keep a preprocessing or refinement (post-process) stage when switching it on raises the corpus quality. We ablate a production pipeline that turns conference speech into question-answer pairs. The preprocessing stage rewrites the transcript, and the refinement stage filters the generated pairs. Switching each on and off gives four corpora from the same 40 Korean medical and finance sessions. On the corpus itself, quality rises as the stages switch on. Four LLM judges and six human domain experts rank the four corpora the same way, and the fully refined corpus leads by +0.18 and +0.22 on a 1-5 scale. We then ask whether that gain carries downstream. We supply each corpus to six models at inference and measure retrieval accuracy. The ranking does not hold. Enabling the transcript rewrite lowers retrieval accuracy by 0.061, the only stage effect that survives correction for multiple comparisons. That stage also reads the whole session, so it almost doubles the cost of one. With both stages on, accuracy does not change. An equivalence test we declared in advance confirms this. The corpus itself is clearly valuable. It lifts retrieval accuracy from 0.231 to 0.748 in every model and domain we test. More than a third of its pairs carry knowledge that neither of two frontier models produces on its own. On our data, the null does not come from weak corpora. A rising score on a rubric of this kind did not predict what the corpus holds for a model.

---


### 140. [A Unified Attack Framework against Statistical Generative Watermarks for Large Language Models](https://arxiv.org/abs/2610.27653)

**<font color=#1a73e8>作者：</font>** Romina Omidi, Nima Naderloui, Yuan Hong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Watermarking has emerged as a key tool for identifying text generated by large language models (LLMs), with current schemes embedding statistical signals into the generation process to enable later detection. In this work, we identify a shared weakness across a broad class of popular LLM watermarking methods, including KGW (and its variants), GumbelSoft, DipMark, ITS, and SynthID. We show that these schemes exhibit a fundamental link between their detection scores and the token probability shifts they introduce during generation. This link, which we call score-ratio alignment, allows an attacker with only black-box query access to the model--and no knowledge of secret keys or model weights--to produce text that evades detection while remaining fluent and natural. We prove that the resulting attack is optimal across all covered watermark families, and show that the weakness is intrinsic: any watermark designed to maximize statistical detection power necessarily induces the very structure that attackers can exploit. We evaluate our attack on seven popular generative LLM watermarking schemes, three LLMs, and tasks, which reduce detection rates to at most 0.05 across all settings while preserving text quality. Our findings show that current watermarking methods can be reliably defeated under realistic attack conditions, highlighting the need for fundamentally different watermarking designs that decouple detection scores from token probability shifts.

---


### 141. [Does Multi-Agent Collaboration Pay When Agents Serve Users? Testing Agent Scaling in Dual-Control Settings](https://arxiv.org/abs/2610.27655)

**<font color=#1a73e8>作者：</font>** Ethan Yang, Xiangcheng Shi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems (MAS) built from language models are deployed on the premise that collaboration beats a single-agent system (SAS), yet when it pays is unclear. The most systematic study to date gives a capability-saturation rule: coordination helps while the SAS is weak and hurts once it is strong, with the crossing near 45% single-agent accuracy. That rule was derived on autonomous benchmarks, where no user takes part. We test it where agents now work: in conversation with a user under a written policy, on $\tau^2$-bench, the dual-control benchmark. On its airline, retail and telecom domains we compare the stock SAS with a centralized MAS built from the same model for six models from three families, over about 7,950 simulated conversations, with one completion-token ledger per episode per system. The study was pre-registered with a public change log; the MAS is reported as built, with one validity bar unmet (its planner never saw the tool schemas). Under a fixed simulated user no cell shows a MAS benefit: the MAS is worse in 12 of the 13 valid cells and tied in the thirteenth, and the fitted gain is negative across the observed capability range (weighted mean -28 points, 95% CI [-44, -12]). On the two cells where the rule predicts a benefit, the MAS loses by 13 and 22 points, and without a budget ceiling it at best draws level at 5.5 times the SAS's token spend. The one gain appears on the cell nearest 45%, under a second simulator. Whether the gain declines with capability is unresolved (slope -0.41, 95% CI [-1.51, +0.68]), because model-by-domain effects dominate. The MAS does not detectably reduce wrongful database writes; it converts other failures into budget exhaustion and inaction. For agents that serve people, the SAS is the default; a multi-agent design must show compute-matched evidence from the setting itself. We release all trajectories, ledgers, prompts and code.

---


### 142. [PACE-MoE: Adaptive Domain Sampling and Domain-Specific LoRA for Medical Visual Grounding](https://arxiv.org/abs/2610.27656)

**<font color=#1a73e8>作者：</font>** Zhenxuan Wang, Jisheng Dang, Ronghao Lin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical visual grounding requires models to align clinical descriptions with spatial evidence across heterogeneous imaging domains. However, existing multi-domain post-training strategies typically rely on fixed domain sampling and shared parameter updates, overlooking the need to adapt both which domains receive training and where their updates are applied. To address this issue, we propose PACE-MoE, a policy-guided framework that jointly performs adaptive domain sampling and domain-specific adaptation for medical visual grounding. PACE dynamically assesses the training value of each imaging domain from current-policy feedback and progressively adjusts domain coverage through domain admission, replay, and final all-domain balancing. Meanwhile, domain-specific LoRA adapters route updates to the corresponding imaging domains while preserving the pretrained backbone and visual encoder. This coordinated design aligns training-data allocation with parameter adaptation without modifying the original reward formulation or Group Relative Policy Optimization (GRPO) objective. Experiments across seven medical imaging domains show that PACE-MoE consistently improves grounding performance over fixed-domain training, achieving a 3.64% relative improvement in mean box IoU over the Vanilla baseline. Under matched domain-specific adapter architectures, adaptive sampling alone further improves mean box IoU by 2.07%, demonstrating the benefit of policy-guided domain allocation. These results establish coordinated data-parameter routing as an effective strategy for multi-domain medical visual grounding.

---


### 143. [When Can LLM Reasoning Reliably Reuse Intermediate Results?](https://arxiv.org/abs/2610.27662)

**<font color=#1a73e8>作者：</font>** Deyuan Liu, Zecheng Wang, Xuanyi Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sampling complete solutions gives large language models more chances to solve a problem, but each attempt starts again. For tasks with several subproblems, all required answers must be correct in the same attempt. Retaining intermediate results can avoid repeating correct work, but errors in those results may affect later attempts. We study when this reuse is reliable and how much computation it requires. For local retries that stop when no candidate passes within the retry budget, we give conditions for correct completion and bound the average number of attempts. We also show how checking cost and the chance of passing a check affect total computation. Experiments across eight reasoning models examine composite mathematics and arithmetic. Across four DeepSeek models, average success on the second subproblem is 36.2 percent without first-subproblem context, 57.2 percent with its answer, and 58.3 percent with its reasoning and answer. These scores measure second-subproblem coverage and include continuations made when selection fails. Arithmetic experiments show that similar first-attempt accuracies can lead to very different coverage after repeated attempts. Code is available at this https URL.

---


### 144. [Hybrid Momentum Methods for Optimizing Deep Learning Models](https://arxiv.org/abs/2610.27674)

**<font color=#1a73e8>作者：</font>** Haifeng Xu, Yijin Ren, Qi Deng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Momentum is central to stochastic optimization in deep learning, including the training of large language models. Classical momentum methods typically rely on a fast exponential moving average (EMA) scheme, which discounts past gradients on a fixed timescale and may underweight older gradients that remain informative. This creates a trade-off between retaining long-term history and adapting to recent changes. We introduce Hybrid Momentum (HyM), which combines a linearly weighted average of past gradients with a geometrically discounted fast momentum. The former assigns weights proportional to the gradients' iteration indices and retains a growing span of history, while the latter emphasizes recent gradients. This hybrid construction is modular and can be combined with adaptive preconditioning and other update transformations. In particular, we propose HyMUON, which applies Newton--Schulz orthogonalization to the hybrid direction. Illustrative examples and controlled experiments demonstrate the benefits of combining gradient information across these two timescales. Across image classification, machine translation, and language modeling, HyM and HyMUON match or improve upon strong baselines. HyMUON improves over Muon on IWSLT14, and in both the 100k- and 600k-step GPT-2 124M OpenWebText regimes. For LLaMA-1.3B pretraining on C4, HyMUON achieves a final validation loss of 2.777, compared with 2.903 for Muon.

---


### 145. [Pattern Intelligence: Unsupervised, LLM-Interpreted Discovery of Systematic Underpayment and Denial Patterns in Healthcare Revenue Cycle Management](https://arxiv.org/abs/2610.27684)

**<font color=#1a73e8>作者：</font>** Harshil Lodhiya, Alex McManus  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Healthcare providers lose substantial revenue to systematic payer underpayments and claim denials, yet identifying the recurring, correctable patterns behind them remains largely manual and does not scale to hospital claim volumes. We present Pattern Intelligence, a deployed system that discovers such patterns without supervision by clustering claims on their adjudication behaviour rather than their identity. Each claim is embedded in a 130-dimensional vector combining per-line expected-versus-actual payment ratios, claim adjustment reason (CARC) codes, denial and payment signals, and service composition. Payer and contract identity are deliberately excluded from the distance metric - we show they dominate the geometry and collapse clusters into trivial per-payer groups - and are reintroduced only as a post-hoc segmentation (by contract and visit type) that keeps every surfaced pattern coherent and actionable. We cluster with HDBSCAN, recover structure from the noise set via second-pass sub-clustering, and gate low-confidence memberships. A large language model translates each centroid into an analyst-ready description of dominant procedures, adjustment reasons, and failure mode. We report a recurring finding: roughly one-third to one-half of high-dollar denials, depending on tenant and segmentation, form an irreducible long tail that no density-clustering configuration or representation we tried groups - a domain property, we argue, rather than a modeling deficiency. We evaluate validity through cluster-coherence analysis and quantify impact with a recoverable-opportunity ($) metric on two production tenants (approx. 10K and 157K claims) within a six-tenant deployment. Rather than a new algorithm, the contribution is a problem formulation, a representation-design insight, and empirical findings from production.

---


### 146. [NeoWorld-3: From Pixels to Code-Defined Physical Worlds](https://arxiv.org/abs/2610.27690)

**<font color=#1a73e8>作者：</font>** Eachen Soong, Zijian Niu, Haoran Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Simulation-ready world reconstruction demands physical interactivity beyond visual realism, which existing black-box 3D generation fails to deliver. We present NeoWorld-3, a coding-agent framework that reconstructs interactive 3D worlds from visual observations via tunable, executable programs. At its core, NeoSDK provides the underlying computational engine for low-level geometries, part composition, differentiable parameter refinement, and physics validation. At the same time, NeoMCP exposes these capabilities as structured, tool-callable APIs for vision-language agents to visually inspect, edit code, and iteratively refine programs. Through a hierarchical coordinator-worker architecture, the framework scales seamlessly from standalone articulated objects to complex compositional scenes. Evaluations across object-level and scene-level reconstruction benchmarks demonstrate that NeoWorld-3 achieves state-of-the-art geometric fidelity and physical readiness. Crucially, manipulation trajectories planned within our reconstructed twins achieve successful zero-shot execution on a physical dual-arm robot, completing the Real-Sim-Real loop.

---


### 147. [A Principled Optimal Transport Framework for Frame Selection in Long Video Understanding](https://arxiv.org/abs/2610.27692)

**<font color=#1a73e8>作者：</font>** Ziwei Zhao, Yuhang Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-video understanding with multimodal LLMs is fundamentally constrained by the mismatch between video length and the model's limited visual context budget, making frame selection essential for practical reasoning. Existing query-aware methods typically rely on heuristic pipelines: they assign one-dimensional query-conditioned scores to frames and then apply sampling, ranking, or extraction rules to form the final subset. While effective in practice, such methods are generally not derived from an explicit optimization objective and struggle to capture the heterogeneous evidence required for complex reasoning. In this paper, we revisit long-video frame selection from a principled optimization perspective. We formulate it as a structured evidence-allocation problem and propose OTFS, an optimal transport framework that maps multiple evidence sources onto video frames. To reflect the asymmetry of this problem---important evidence should be preserved, whereas redundant frames need not absorb mass---we instantiate this view with a semi-unbalanced entropic optimal transport objective and an efficient solver, OTFS-Sinkhorn. Combined with an exact dynamic program for coverage-aware subset extraction, OTFS yields a practical two-stage training-free pipeline. We further show that, in the single-source case, our formulation induces a Gibbs-type distribution over frames, making Q-Frame's temperature-scaled distribution a special case of our framework while also providing a broader perspective for understanding related prior methods. Experiments on three long-video understanding benchmarks show that OTFS consistently outperforms strong training-free baselines. Codes are available at this https URL.

---


### 148. [VLA-Retain: Benchmarking Cross-Dimension Effects of Vision Tuning in VLAs](https://arxiv.org/abs/2610.27698)

**<font color=#1a73e8>作者：</font>** Borui Xu, Han Chen, Bingsheng He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models transfer knowledge from large-scale pretraining into robot control, but their manipulation performance remains sensitive to changes in observation conditions, which recent work addresses by fine-tuning the visual module on target-domain data. However, it remains unclear how such adaptation affects robustness beyond the target condition, as existing robustness benchmarks only evaluate models without fine-tuning and adaptation studies only report the target gain. Measuring this cross-dimension effect requires separating target gains from off-target changes, isolating adaptation effects from architectural differences, ruling out generic forgetting, and comparing tuning choices. Therefore, we introduce VLA-Retain, a benchmark that compares five open VLA models, tuned on Camera-view or Sensor-noise data, with their own base checkpoints on LIBERO-Plus dataset spanning seven perturbation dimensions. Our study reveals four findings. First, targeted vision tuning is not local, and its target gain does not predict retention. Mean off-target gain is negative in 8 of 10 model--domain configurations. Under Camera-view tuning, X-VLA gains $69.4$ percentage points on the target but loses $4.6$ points on average elsewhere, whereas OpenVLA-OFT gains $39.3$ and $1.4$ points, respectively. Second, these regressions are not explained only by performance loss on the same tasks without perturbations. Third, broader training coverage raises overall gain over target-specific training but does not eliminate dimension-level regressions. Fourth, tuning strategies are model-dependent, as DELTA-style feature preservation raises X-VLA's mean off-target gain to $+1.2$ points but lowers OpenVLA-OFT's to $-23.1$. Overall, these findings show that target-domain success alone is insufficient and highlight cross-dimensional retention as a key criterion for targeted VLA adaptation.

---


### 149. [E8-QAT: Efficient 2-Bit Quantization-Aware Training with Implicit Lattice Codebooks](https://arxiv.org/abs/2610.27699)

**<font color=#1a73e8>作者：</font>** Xinyu Lei, Hong Huang, Jiebin Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Low-bit quantization reduces the memory footprint of large language models, but preserving accuracy with efficient training remains challenging. Scalar quantization encodes weights independently, while explicit-codebook vector quantization introduces costly search during training. We propose E8-QAT, a 2-bit quantization-aware training framework that uses the $E_8$ lattice as an implicit eight-dimensional codebook. It jointly quantizes weight groups through arithmetic projection without storing or searching an explicit codebook during the training forward pass. A 2-bit core encoding and sparse extension preserve the selected lattice points exactly, adding less than 0.1\% to core index storage. On Qwen3.6-35B-A3B, E8-QAT matches the performance of the full-precision model in terms of the average score across the four tasks. E8-QAT improves over the state-of-the-art baseline by 2.03\% on IFEval and by 1.51\% on LiveCodeBench, under the same data, schedule, and bit width. The 2-bit representation reduces peak memory by 80\% and supports a $4\times$ larger batch. At each representation's largest feasible batch, E8-QAT reaches $1.97\times$ the decoding throughput of BF16.

---


### 150. [Memory as Code: Declarative Retrieval over Codified Long-Term Memory](https://arxiv.org/abs/2610.27700)

**<font color=#1a73e8>作者：</font>** Aoting Zeng, Yuxin Du, Jianwei Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In long-term memory systems, memories are constructed from interaction histories and retrieved in response to queries, enhancing the reasoning ability of LLM agents. In complex scenarios, facts are scattered across sessions and their relationships evolve over time, making it difficult for existing memory systems to compose them to adapt to diverse queries. Motivated by the modularity and composability of code, we propose Memory as Code (MaC), a unified memory framework that jointly designs memory construction and retrieval through a shared code abstraction. MaC couples codified construction, which establishes executable memory abstractions, with declarative retrieval, which translates queries into structured retrieval programs. Specifically, codified construction builds a three-layer executable memory structure that progresses from an atomic function layer, through a relational layer, to a modular composition layer. Declarative retrieval recasts retrieval from relevance-based fact selection into declarative query processing over memory. Experiments on LoCoMo and LongMemEval show relative gains of up to 15.91% in overall LLM-judge accuracy over the strongest baseline in each setting, while substantially reducing token consumption, highlighting the effectiveness of memory as code for long-horizon memory tasks.

---


> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-299](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
