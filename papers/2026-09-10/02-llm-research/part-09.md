# 🧠 大模型相关研究 | 2026年09月10日

> 本类共 **483** 篇论文：已确认 **447** 篇，待复核 **36** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**401-450**（第 9/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-483](./part-10.md)

---

### 401. [MoEMB: Scaling Universal Multimodal Embeddings with Efficient Mixture-of-Experts Models](https://arxiv.org/abs/2609.08663)

**<font color=#1a73e8>作者：</font>** Xuanming Cui, Shlok Kumar Mishra, Wentao Bao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Universal multimodal embedding (UME) increasingly demands encoder's capacity for handling a broad range of tasks and modalities with increased complexity. Prior scaling methods either increase the representation size, retrieval effort, or scales the encoder into a heavy multimodal LLM. Recent works, such as Think-Then-Embed (TTE), explore scaling via reasoning tokens. However, embedding models are hard to scale up: increasing parameters directly tradeoffs for the large training batch size that contrastive learning needs, and retrieval has to be served under tight latency. Moreover, UME tasks are diverse in complexity, where scaling up embedders can bring significant redundant computation. In this work, we propose MOEMB, which instead scales UME along the expert axis through mixture-of-experts (MoE), growing encoder capacity while preserving single-vector, non-autoregressive encoding. Through a systematic study of the design space and training recipes for MoE-based UME, MoEMB sets a new state of the art on both MMEB-V2 and MRMR among models trained on public MMEB-family data: with only 3B active parameters, MoEMB surpasses TTE-based methods with >4x active parameters, using significantly less computes. To further improve the scalability and efficiency, we conduct the first comprehensive study of adaptive computation for MoE-based embedding, spanning diverse strategies across training-based and inference-only methods. Together, these results support expert scaling as an effective and efficient direction for UME, with adaptive computation further improving efficiency for MLLM-based embedding models towards large-scale retrieval and recommendation systems.

---


### 402. [CausalChapter: Improving Long-Video Chaptering with Interventional Dependency Modeling](https://arxiv.org/abs/2609.08686)

**<font color=#1a73e8>作者：</font>** Xinran Duan, Guozhang Li, Yaoyao Zhong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-form instructional videos require automatic chaptering to support browsing, navigation, and knowledge access. Recent long-context language models can perform chaptering from textualized video inputs, but they remain costly and brittle for content-dense lecture videos with long transcripts, smooth topic transitions, and detailed chapter outputs. A scalable segment-then-caption paradigm reduces this cost, but introduces two new challenges: boundary error propagation and fragmented cross-chapter context. We propose \textbf{CausalChapter}, an intervention-inspired framework for long-video chaptering that estimates prediction-level influence through lightweight masking and removal interventions. For boundary localization, our Local Dependency Shift module detects drops in predictive dependency between adjacent temporal windows; for chapter description generation, our Cross-Segment Support Selection module reranks historical contexts according to their support for the current prediction. Experiments on long-video chaptering benchmarks show that CausalChapter improves boundary localization, chapter description quality, and cross-chapter coherence.

---


### 403. [When Victorian Becomes a Prompt: Literary Periodization as a Generative Constraint in 100 AI-Generated Novels](https://arxiv.org/abs/2609.08689)

**<font color=#1a73e8>作者：</font>** Mehdy Sedaghat Payam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generative AI inverts the typical periodization of literary history: the periodizing tag Victorian can now come first and influence what is written. Generative periodization, defined and tested here, describes the use of literary-period designations in generating texts. I test this approach on 100 book-length novels produced under Victorian and Zero-Style conditions using GPT, Qwen, and Llama workflows. The Period Alignment Score (PAS), trained on nineteenth-century literature and benchmarked against human Zero-Style prose, assesses alignment using topic-reduced grammatical features. Victorian prompts produce consistent historical-direction shifts in GPT and Qwen, but not robustly in Llama. Victorian-only recalibration and harder comparison corpora preserve the GPT and Qwen effects. Cross-model transfer also shows a shared direction of grammatical change. The measurable target is the broader nineteenth century rather than the Victorian period per se.

---


### 404. [Hyperparameter Scaling Laws Across MoE Sparsity](https://arxiv.org/abs/2609.08690)

**<font color=#1a73e8>作者：</font>** Changxin Tian, Kunlong Chen, Jia Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models expand model capacity without a proportional increase in training compute, but increasing sparsity makes reliable hyperparameter transfer challenging. In this work, we show that conventional hyperparameter scaling laws are insufficient for ultra-sparse MoEs: the optimal learning rate and batch size vary with activation ratio, and these shifts cannot be explained by either total or activated parameter count alone. To characterize this dependence, we conduct 1,800 pre-training runs spanning six activated-parameter scales and models with up to 6B total non-embedding parameters, processing approximately 20 trillion tokens at a cost of 200,000 equivalent H800 GPU-hours. Our results reconcile conflicting findings in prior work by revealing two scaling regimes. At fixed sparsity, the optimal batch size follows a power-law relationship with training tokens $D$, whereas the optimal learning rate scales with training compute $C$ and remains robust to the allocation between model size and data. Across sparsity levels, the activation ratio $A$ enters both relationships as an additional multiplicative power-law factor. These observations lead to unified hyperparameter scaling laws that transfer across MoE sparsity levels. Large-scale evaluation shows that the scaling form outperforms alternative functional forms. On a held-out ultra-sparse MoE with 12B total parameters and only 1/64 of its experts activated, the predicted hyperparameters remain close to the observed optima, supporting joint extrapolation across model scale and sparsity. Further experiments demonstrate transfer across expert granularities and isolate the effect of activation ratio from that of total expert count.

---


### 405. [Record Grouping Controls Evidence Weight in Language Models](https://arxiv.org/abs/2609.08698)

**<font color=#1a73e8>作者：</font>** Zhongxuan Liu, Sicheng Zhou, Hongzhi Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieved records are presentation units; a supplied partition determines which records enter a language model as one evidential contribution. We characterize the invariant group-content state that removes within-group copies while retaining complementary canonical content, show that equal group counts can encode different evidence states, and derive a sharp content-aware partition-error bound. Given a supplied partition, our pre-generation representation deduplicates and aggregates content within groups and bounds each group's contribution. Across 104,402 trials and 6 public checkpoints, a central natural-text intervention finds that content-fixed false splits add 10.27-32.66 percentage points and false merges remove 9.13-31.79 points; a matched six-slot control retains the positive direction in all 16 cells. In a new 48-item controlled campaign panel, changing the supplied partition produces measurable, checkpoint-dependent decision shifts across all four models, and the balanced mirror design exposes substantial order interactions. Together, the theory and experiments establish the supplied partition as a controllable pre-generation representation variable and characterize its checkpoint-dependent behavioral effects.

---


### 406. [Chimaera: A Mixture-of-Graph-Experts Architecture for Cross-Task and Cross-Dataset Graph Learning](https://arxiv.org/abs/2609.08709)

**<font color=#1a73e8>作者：</font>** Jonathan Frank, David Richerby, Ansgar Scherp  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Designing foundation models for graphs is challenging due to the irregular structure of graphs and the different sizes and characteristics of embeddings. Chimaera integrates mixture-of-experts with graph foundation models (GFM). It integrates different GFM architectures, such as graph prompts and linear GNN models. Large language models are used to generate embeddings, and experts can be trained and combined following different strategies, GFMs, embeddings, etc. Furthermore, Chimaera extends existing linear GNNs to support link-level and graph-level tasks in addition to node-level tasks. Empirical analyses are performed on same-task and cross-task experiments with node, link, and graph classification tasks using six benchmark text-attributed graph datasets. The experiments demonstrate the effectiveness of Chimaera and its capabilities for transfer across tasks and datasets. Further insights include the need to use both large and small language models to generate embeddings for the experts, a strong cross-task transferability of simple but effective linear GNNs, and using few samples only to provide strong results.

---


### 407. [Benchmark Scores Are Pipeline-Dependent: A Reliability Audit of Cybersecurity LLM Benchmarks](https://arxiv.org/abs/2609.08765)

**<font color=#1a73e8>作者：</font>** Aymene Berriche, Cathrine Shalby, Mohannad Alhanahnah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) benchmarks are often treated as fixed datasets with stable scores, yet their outcomes depend on configurable evaluation pipelines. We audit eight cybersecurity benchmarks across 10 proprietary, open-weight, and cybersecurity-specialized LLMs. By modeling benchmarks as measurement pipelines, we identify 15 systematic failure modes and show that a single pipeline choice can change a model's score by more than 80 percentage points and substantially alter model rankings. At the cross-benchmark level, two semantically similar task pairs rank the same models differently because of incompatible evaluation conventions. Under an evaluation harness that standardizes pipeline choices while preserving task semantics, nine of 10 models shift by at least three ranks on at least one benchmark. These results show that cybersecurity LLM benchmark scores are pipeline-dependent and motivate pipeline-aware auditing as a core requirement for reliable model evaluation.

---


### 408. [It's All in the Way You Say It: The Role of Information Representation in LLM-Based Glycemic-Event Prediction](https://arxiv.org/abs/2609.08772)

**<font color=#1a73e8>作者：</font>** Andrea Apicella, Pasquale Arpaia, Matteo Orefice 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly being investigated for physiological time-series prediction, yet their effectiveness may depend not only on the model itself, but also on how physiological information is represented and presented at inference time. This study investigates prompt-based general-purpose LLMs for postprandial hyperglycemia and hypoglycemia prediction in individuals with type 1 diabetes. Using the OhioT1DM dataset, we evaluate multiple open-weight LLMs under zero-shot and few-shot inference across prediction horizons of 30, 60, and 90 minutes. The analysis varies both the textual representation of the available physiological information and the amount of information exposed to the model, ranging from glucose observations alone to derived descriptors and additional contextual variables related to insulin, meals, carbohydrates, and physical activity. Performance is compared with conventional patient-specific supervised models and with Gluco-LLM, a language-model-based architecture explicitly adapted to glucose time-series forecasting. Results show a marked task-dependent behavior. Conventional supervised models achieve the strongest performance for hyperglycemia prediction, whereas the best observed prompt-based LLM configurations improve performance for hypoglycemia across all investigated horizons. The effectiveness of prompt-based inference is also strongly influenced by how physiological information is represented, while providing additional contextual information does not lead to a systematic improvement. Overall, these findings highlight physiological information representation as a central design factor in prompt-based LLM approaches to glycemic-event prediction.

---


### 409. [Evidence-Grounded Retrieval for Investigation Hunt Lead Generation from CTI Reports](https://arxiv.org/abs/2609.08790)

**<font color=#1a73e8>作者：</font>** Akash Prakash, Boubakr Nour, Makan Pourzandi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Threat hunting increasingly depends on converting unstructured knowledge (e.g., Cyber Threat Intelligence reports) into actionable hunt leads: concise, investigable hypotheses grounded in observable artifacts and adversary techniques. Producing such leads manually is a tedious and hard-to-scale task. Existing automated approaches stop at the entity layer, ignore the defender's operational environment, and analyze each report in isolation. To address these gaps, we introduce AHLERT, a system that automatically extracts relevant, environment-aware, and hunt leads from threat reports through (i) a hybrid retriever that combines dense vector search with multi-hop traversal over a knowledge graph seeded with MITRE ATT&CK; (ii) an ontology-grounding retrieval-augmented generation method that constrains each lead to the defender's own assets and controls; and (iii) an LLM-agnostic framework that emits structured, directly actionable leads rather than loose indicators of compromise. We evaluate AHLERT on public CTI reports for well-known APTs across multiple proprietary and open-weight models. Hybrid evidence retrieval with ontology grounding raises mean F1 by ~2x (0.44 to 0.85) over a single-route flat-RAG baseline, and AHLERT attains the highest effectiveness score (~86.95%) compared with off-the-shelf LLM models.

---


### 410. [Measuring the Security of the Evolving Software Supply Chain: a Research Agenda](https://arxiv.org/abs/2609.08810)

**<font color=#1a73e8>作者：</font>** Sarah Meriem Ourari  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Software supply chain security has become increasingly critical due to the widespread reliance on third-party dependencies and the growing attack surface of modern software ecosystems. However, existing quantitative, measurement-based analysis and vulnerability management approaches remain largely fragmented and ecosystem-specific, limiting their ability to provide comparable risk assessments across environments. This paper presents a structured research plan, starting with a Systematization of Knowledge (SoK) to synthesize the current state of research and identify key gaps, highlighting the limitations in dependency modeling and vulnerability propagation analysis, particularly in the treatment of transitive dependencies and their real-world exploitability. Based on these insights, we argue for a unified measurement perspective capable of consistently representing and analyzing the cross-ecosystem dependency structure. We further identify emerging challenges introduced by AI-assisted software development, where coding LLMs are likely to contribute to new dependency patterns that are not captured by traditional Software Composition Analysis (SCA) tools. These shifts motivate a rethink of dependency modeling to account for evolving software-generation practices and their long-term structural impact on software security.

---


### 411. [Closing the Consistency Gap: Self-Evolving Agents That Learn to Stay on Course](https://arxiv.org/abs/2609.08832)

**<font color=#1a73e8>作者：</font>** Evelyn Duesterwald, Benjamin Elder, Lilian Ngweta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-powered agents can be accurate on average yet unreliable in production, a discrepancy that has been observed but remains largely unaddressed. When given the same task five times, a ReAct agent on the AppWorld benchmark using GPT-4.1 succeeds in all five runs only 53% of the time, even though its per-run pass rate averages 77%. We call this 24-point shortfall the consistency gap, and we argue that addressing it is a precondition for trustworthy AI agent deployment. We present a self-evolving agent framework that reduces this gap by identifying unstable, low-consistency steps in agent trajectories and converting them into episodic memory the agent can draw on in future runs. At its core is a Consistency Analyzer that pinpoints where and why a trajectory is likely to flip across executions, and a Guideline Generator that converts the diagnosis into targeted guidelines, committed to memory and injected into future agent executions on similar tasks. On AppWorld with ReAct/GPT-4.1, our framework raises the fraction of tasks that succeed in all five runs by +16 points on same-task evaluation and +13 points on similar-task generalization.

---


### 412. [DSE-VTG: Dual-Side Enhancement for Training-Free Video Temporal Grounding](https://arxiv.org/abs/2609.08850)

**<font color=#1a73e8>作者：</font>** Zhuo Cao, Bingqing Zhang, Sen Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-guided Video Temporal Grounding (VTG) aims to localize the relevant segments in an untrimmed video based on text queries, yet collecting dense temporal annotations and training task-specific models remain costly and brittle under distribution shift. Recent training-free VTG approaches mitigate this issue by directly matching pretrained vision-language representations, but they still face two fundamental information bottlenecks: frame-wise visual encoding overlooks temporal dynamics, while fixed query embeddings cannot resolve query ambiguity. To address these issues, we propose DSE-VTG, a \underline{D}ual-\underline{S}ide \underline{E}nhancement framework that addresses both without any task-specific training. On the visual side, Multi-scale Similarity Fusion (MSF) combines frame- and clip-level similarities into a unified, temporally aware similarity profile. On the textual side, Query-level Test-Time Adaptation (Q-TTA) optimizes a lightweight additive offset to adapt the query embedding to the video at test time, without finetuning the backbone or calling external large language models. Extensive experiments on three standard and two OOD benchmarks show that DSE-VTG achieves state-of-the-art performance among training-free methods. On Charades-STA, it improves mIoU over the strongest prior training-free method by 5.61 points. Under distribution shift, DSE-VTG reaches 50.86 mIoU on Charades-CG Novel-Word, surpassing the strongest supervised baseline by 2.76 mIoU. Our code will be released upon acceptance.

---


### 413. [API Benchmark Scores Do Not Reliably Transfer to Chatbot Interfaces](https://arxiv.org/abs/2609.08861)

**<font color=#1a73e8>作者：</font>** Jennifer Wang, Joachim Baumann, Daniel E. Ho 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Benchmark scores are a central currency in model releases: they inform purchasing decisions, shape public trust, and influence policy. Yet, a key assumption underlying benchmark scores is that the model performance measured through APIs faithfully reflects the behavior of deployed systems.
We challenge this assumption by auditing ChatGPT, Claude, and Gemini across seven systems and nine benchmarks spanning general capability, social bias, and sycophancy. We find systematic API--interface differences in both accuracy and consistency. On average, API evaluations score 3.4 percentage points higher in accuracy and 2.1 percentage points higher in test--retest agreement than corresponding interface evaluations. For ChatGPT, the performance difference between API and interface access exceeds the API-only difference between GPT 5.3 and GPT 5.4. Put differently, switching access surfaces can degrade performance as much as downgrading a full model generation.
We further test whether exposed API controls can reproduce interface behavior by varying system prompts, sampling parameters, and reasoning settings. These controls shift behavior in some cases but do not reliably eliminate the gap. Our findings document a context-validity gap: measurements obtained through APIs do not necessarily generalize to corresponding deployed interfaces, complicating the use of API evaluations as proxies for deployed systems.

---


### 414. [SeGDeP: Semantic- and Geometric-Aware Decoupled Prompts for Reasoning Segmentation](https://arxiv.org/abs/2609.08867)

**<font color=#1a73e8>作者：</font>** Linnan Zhao, Xu Liu, Lingling Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reasoning segmentation converts an implicit linguistic conclusion into a precise mask, requiring both semantic identification and spatial grounding. Existing MLLM-segmenter interfaces either use a special trigger or compress both signals into one context, although they receive different supervision and fail differently. This coupling obscures whether a failure arises from target interpretation or from localization. We present SeGDeP, an explicit what-where interface. A semantic prompt branch and an independent geometric projection path transform resolved MLLM states into semantic features and a DETR-predicted box, which jointly condition a SAM 3 mask decoder. Training first aligns this executable interface, then uses group reward-decoupled policy optimization (GDPO) to balance format, box-IoU, and mask-IoU feedback. SeGDeP-4B reaches 82.7 average cIoU over eight RefCOCO-family splits and 66.0/59.6 gIoU on ReasonSeg val/test while adapting only 0.38% of Qwen3-VL parameters through LoRA. Controlled stage-wise ablations, gradient diagnostics, and prompt interventions further show that the two paths develop complementary semantic and geometric specialization rather than duplicating the same evidence.

---


### 415. [Evolution of Multimodal Question Answering: From Modality-Adaptive Extraction to Unified Language Representation](https://arxiv.org/abs/2609.08896)

**<font color=#1a73e8>作者：</font>** Abdullah Al Shafi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid growth of multimodal data has intensified the need for question answering (QA) systems capable of reasoning across heterogeneous sources such as text, tables, and images. In this paper, we present a comprehensive methodological comparison of three influential frameworks, namely Multimodal Adaptive Extraction (MAE), Solar, and UniMMQA, tracing the evolution of multimodal question answering from modality-adaptive pipelines to fully unified architectures. We examine how each approach models cross-modal interactions, transforms heterogeneous inputs, and performs reasoning, highlighting key design differences in modality representation, reasoning, and answer generation. Our analysis demonstrates a clear shift from explicit modality-specific processing toward unified text-centric formulations enabled by pre-trained language models (PLMs). Empirical comparisons across benchmark datasets show that this transition leads to substantial improvements in both Exact Match (EM) and F1-Scores, with UniMMQA achieving the most consistent and scalable performance. Despite these advances, we identify persistent challenges, including information loss during modality transformation, error propagation in multi-stage pipelines, and limitations in capturing fine-grained cross-modal dependencies. Overall, this study provides a deeper understanding of current design trends and offers insights into the future direction of unified multimodal reasoning systems.

---


### 416. [Experience Funnel: A State-Policy Alternating Loop for Self-Evolving Agents](https://arxiv.org/abs/2609.08919)

**<font color=#1a73e8>作者：</font>** Wenbo Gao, Zhaomou Song, Zhiyuan Ji 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autonomous agents powered by large language models (LLMs) continuously accumulate experience through interaction, creating an opportunity to improve future behavior through self-evolution. A fundamental challenge is how to transform abundant, task-specific interaction experience into reusable model competence without sacrificing the ability to adapt rapidly to newly observed evidence. Explicit textual states, such as skills and agent harnesses, provide fast, human-readable and editable adaptation, but incur persistent dependence on external context; parametric policies provide compact and reusable competence, but are substantially slower to update. We present \textit{Experience Funnel}, a self-evolving framework that couples fast state adaptation with slow policy consolidation in an alternating loop. Interaction trajectories are first distilled into an explicit textual state, where newly acquired experience can be rapidly incorporated and validated. The framework then selectively identifies state-enabled behavior that remains useful across state revisions and consolidates it into the policy through transition-aware distillation. The updated state--policy pair subsequently generates new rollouts, providing fresh evidence for the next round of state adaptation and policy consolidation. Experiments across diverse agent benchmarks show that \textit{Experience Funnel} consistently improves agent capability over state-only evolution and policy-internalization approaches, while progressively converting useful explicit experience into autonomous policy competence.

---


### 417. [When Models Defer to Wrong Answers: A Robustness Audit of Source-Attributed Cues in Multiple-Choice QA](https://arxiv.org/abs/2609.08934)

**<font color=#1a73e8>作者：</font>** Manikandan Ravikiran, Siddharth Vohra  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models often receive a question together with a claim about what another source answered. We audit whether such claims destabilize answers in multiple-choice question answering. For each item, we hold one wrong option fixed across misleading conditions and vary the cue template attached to it. We introduce \emph{neutral-conditioned misleading cue adoption rate} (NC-MCAR), which measures switches to that option only on valid cued trials where the same model first selected the gold answer under a neutral prompt. This is a measure of answer instability, not proof that the model knew the answer or that all deference is irrational. We evaluate four instruction-following models on MMLU-Pro and IndicMMLU-Pro in English, Hindi, Bengali, Tamil, and Telugu. Across 220{,}000 outputs, the expert template yields 41.1\% aggregate NC-MCAR, compared with 12.5\% for the majority template. These two conditions use the same wrong option and final instruction. Filler accuracy remains well above expert-wrong accuracy, while correct-cue prompts have high valid-response accuracy. The audit documents answer instability relevant to grounding under the tested forced-choice prompts: a bare, unverified source claim can outweigh an answer that was previously consistent with the task evidence.

---


### 418. [EgoSIS: From Factorized Visual Ego-Transitions to Motion-Canonical Spatial Evidence for UAV Reasoning](https://arxiv.org/abs/2609.08938)

**<font color=#1a73e8>作者：</font>** Jingpu Yang, Fengxian Ji, Mingxuan Cui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> UAV video question answering requires separating camera motion from changes in the scene, but RGB-only multimodal models receive no explicit, stable reference for that separation. We present EgoSIS, a pose-free adapter that converts RGB-derived bidirectional flow into motion-canonical visual evidence in three stages. Factorized Visual Ego-Transitions (FVET) fits a robust image-plane transition and exposes motion, residual-support, and reliability factors. Reliability-Gated Ego-Transition Memory (ReTEM) uses reliability-weighted updates for a bounded history and re-anchors it at cuts or sustained uncertainty. Ego-Aligned Spatial Evidence (EASE) warps supported visual features into each segment's local anchor and injects four spatial evidence tokens per visual slice through zero-initialized residuals, without changing Qwen's visual-token count. On SIS-Bench, EgoSIS-8B obtains 89.9\% perception, 82.5\% perception-plus-memory, and 76.2\% overall accuracy, with the largest gains concentrated in self-awareness perception and memory. The adapter thus provides an interpretable interface between optical flow and spatial reasoning.

---


### 419. [Evaluating and Improving Evidence-Grounded Fact-Checking in LLMs via Multi-Round Evidence Ablation](https://arxiv.org/abs/2609.08943)

**<font color=#1a73e8>作者：</font>** Xingyu Deng, Mingzi Cao, Nikolaos Aletras 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic fact-checking systems assess the veracity of claims given evidence from relevant documents. Large Language Models (LLMs) have demonstrated strong performance in fact-checking due to their general reasoning capabilities. However, it remains unclear whether they faithfully make use of the evidence provided to reach veracity judgments or rely on parametric knowledge. To investigate this, we introduce Fact-Ablated Evaluation (FAE), a new evaluation framework that iteratively ablates the cited evidence to assess whether LLMs revise their predictions accordingly. Our empirical results show that current off-the-shelf LLMs as fact-checking systems rely more on their parametric knowledge than on the evidence provided. To bridge this gap between prediction accuracy and evidence grounding, we propose REAL (Rigorous Evidence Ablation Learning), a training framework that promotes evidence-dependent verification through counterfactual evidence supervision for the LLM-as-verifier models. Experiments on four fact-checking datasets across different domains demonstrate that models trained with REAL obtain superior evidence-dependent capabilities compared to standard fine-tuned models. Our findings highlight that strong fact-checking performance can still coexist with weak evidence dependency, while REAL encourages veracity predictions to remain more closely tied to the availability of supporting evidence.

---


### 420. [SkillAdam: Stable and Efficient Skill Evolution for Agents](https://arxiv.org/abs/2609.08944)

**<font color=#1a73e8>作者：</font>** Gaoyuan Li, Meihao Fan, Yizhe Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills provide a lightweight way to equip frozen language-model agents with domain knowledge and procedural guidance, yet obtaining high-quality skills remains costly and difficult to scale. Expert-written skills require substantial human effort. Recent skill self-evolution methods automate an iterative loop that uses execution feedback to revise skills, but their heuristic update strategies often yield unstable optimization and low iteration efficiency. We identify two challenges in realizing stable and efficient skill self-evolution. Direction Stability requires effective corrections to accumulate rather than be overwritten by iteration-local feedback. Update Adaptivity requires the scope of each revision to reflect the consistency of recent case-level improvements. We introduce SkillAdam, an Adam-inspired framework for optimizing discrete and non-differentiable skill documents. As a functional analogue of Adam's first moment, an optimization memory records identified problems and the outcomes of prior solution attempts to stabilize the update direction. As a functional analogue of Adam's second moment, a volatility-driven edit budget tracks the history-weighted variation of recent case-level improvements and adaptively controls the update magnitude. Across seven benchmarks that span short- and long-horizon tasks, SkillAdam achieves state-of-the-art performance with more stable optimization dynamics. It also obtains stronger skills with substantially fewer optimization iterations and lower cost than prior methods. Code repository: this https URL

---


### 421. [PlannerForge: LLM Agents for Scenario-Based Testing of Motion Planners in Autonomous Driving](https://arxiv.org/abs/2609.08965)

**<font color=#1a73e8>作者：</font>** Yuan Gao, Sebastian Müller, Mattia Piccinini 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ensuring the safety of autonomous driving is a critical challenge. Scenario-based testing is a systematic process used to validate Autonomous Driving Systems (ADSs), but it remains a fragmented modular pipeline in which scenario generation, retrieval, modification, ADS execution, and results analysis are performed by separate tools with little interaction. Large Language Model (LLM) agents have shown promise across ADS sub-systems such as perception, planning, and control. However, no prior work covers the whole scenario-based testing pipeline for ADSs with a unified LLM-agent framework. We present PlannerForge, an LLM-agent framework that extends all scenario-based testing stages (from Scenario Generation to ADS Assessment) and adds two further LLM-enhanced stages: ADS Enhancement and ADS Benchmarking. We evaluate PlannerForge with 10 off-the-shelf LLMs across all tasks (Generation, Selection, Modification, Module Routing, Planner Testing, and Enhancement) under 5 prompt conditions. Best-per-task scores range from 0.88 to 1.00, and open-source 20-35B backends match commercial APIs on most tasks. Open-source models such as Qwen3.6:35B match commercial APIs on three of the five tasks. Chaining the modules end-to-end retains 83% / 78% of seed queries (commercial / open). It outperforms Scenario Factory 2.0 (Finkeldei et al., 2025) on natural-language generation (193 vs. 144 executable of 200) and realises 92-96% of requested city, road and vehicle attributes. It outperforms BM25 (Robertson and Zaragoza, 2009) at rank 1 selection (92.0% vs. 67.5%) and From-Words-to-Collisions (Gao et al., 2025) on physically valid edits (>=94% vs. 31%). At N=400, cost-tuning lifts planner success from 50.4% to 70.2% and cuts collisions from 19.0% to 8.4%, without domain-specific fine-tuning.

---


### 422. [Good Pretraining, Bad SFT: Checkpoint Quality Across the Training Stack](https://arxiv.org/abs/2609.08966)

**<font color=#1a73e8>作者：</font>** Sohir Maskey, Philipp Scholl, Jonas Knupp 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-model checkpoints are commonly selected by pretraining loss or benchmark scores, assuming that the highest-scoring checkpoint will remain the best starting point for subsequent training. We show that this assumption can fail in a full 30B mixture-of-experts training pipeline. The checkpoints that perform better after the full downstream training stack also have higher solution density, i.e., retain downstream performance under local weight perturbations.

---


### 423. [NERVE Attacks: Breaking AI-Powered Brain-Computer Interfaces](https://arxiv.org/abs/2609.08971)

**<font color=#1a73e8>作者：</font>** Zahra Tarkhani, Georgios Akkogiounoglou, Lorena Qendro 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid integration of AI into human-centred systems such as Brain-Computer Interfaces (BCIs) has created a poorly understood attack surface linking neural signals to physical systems. Exploits in this domain threaten cognitive autonomy, mental privacy, and physical safety, from neural data exfiltration to malicious control of BCI-tethered devices. We introduce the NERVE Attacks class, a systematic characterisation of five orthogonal attack dimensions that together span the complete BCI stack: Neuro-mimetic Forgery (N), Evasion via Desynchronization (E), Replay-based Hijacking (R), Vein Tapping (V), and Embedded Backdoors (E). To evaluate this class, we present EEGle, an AI-assisted extensible framework for systematic BCI security analysis. Our evaluation uncovers 17 novel neuro-specific attack instances and reveals a stealth-effectiveness spectrum unique to BCI backdoor design. We also show that generative AI lowers the barrier to entry for non-expert attackers and provide EEGle to the community for building and verifying the security of these deeply personal devices.

---


### 424. [Transformers as In-Context Samplers: From Closed-Form Diffusion to Estimation-Free Sampling](https://arxiv.org/abs/2609.08981)

**<font color=#1a73e8>作者：</font>** Arman Adibi, Alireza Jafari, Mohammad Ghavamzadeh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A growing body of work establishes that large language models are not mere statistical memorizers, but are capable of in-context learning: performing inference at test time using only examples provided in the prompt, without any parameter updates. Prior theoretical work has shown that this capability extends to supervised learning tasks such as linear regression. We prove that in-context learning extends further to \emph{data generation}: frozen transformers can simulate iterative generative samplers from in-context samples. We first show that transformers can realize closed-form and smoothed closed-form diffusion samplers. The construction identifies a concrete generative role for softmax attention: it computes responsibility weights and weighted empirical averages, while feedforward layers implement Euler updates.
To empirically relate these constructions to pretrained language models, we study \emph{semantic-topic sampling}: prompts consisting of words drawn from a common semantic category, such as animals, foods, or cities. Across transformer layers, the normalized hidden states exhibit a two-stage geometry: they move toward a uniform spherical reference in intermediate layers and then return to structured, topic-dependent representations near the output. We further measure an interacting-particle energy on these hidden-state clouds and observe the same U-shape pattern. We then prove that transformers can approximate an energy-based sampler, constructing the same U-shape energy across the layers.

---


### 425. [Deposon: An Auditable, Conservation-Guaranteed, Game-Theoretically Tested Scattering Layer over LLM Reasoning Paths](https://arxiv.org/abs/2609.09001)

**<font color=#1a73e8>作者：</font>** Qihao Yuan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-step LLM reasoning lacks a machine-recheckable ledger: discarded reasoning paths leave no auditable record. We propose the Deposon scattering layer, which binds each node of an LLM-generated concept-decomposition graph to a two-parameter Deposon state; paths undergo three-channel scattering -- transmission, reflection, irreversible dissipation -- obeying T+R+A=1 for arbitrary parameters, with a maximum per-path energy-audit deviation of 2.2E-16 (machine epsilon). We report all three evidence tiers honestly. On synthetic trap benchmarks the path-filtering gain is closed (pre-registered): unified reaches 100% versus a decoy-capture baseline at 7%/10%. On real benchmarks the layer is indistinguishable from a trivial six-keyword rule filter (GSM8K 0.87 >= 0.85, McNemar p=0.5; StrategyQA 0.899 = 0.899); no difference is detected here, so we sharpen the claim to "the differential value lies solely in machine verifiability." Fusion yields a second negative result: convex combinations with a semantic prior never improve (physics 0.484 -> 0.452), and the apparent lambda=2 gain is an anti-field artifact; any fusion gain must be nonlinear. Modeling the reverse dynamics as a potential game on the graph, we evidence an auditable scalar's monotonicity and near-gradientness and quantify the empirical coordination ratio (ECR). The three formalized dynamical-equivalence propositions (P1a/P1b/T-P1c) are falsified under the pre-registered kill protocol, and the potential-game claim is downgraded to approximate (cyclic-graph median residual 0.669): only consistency-level evidence survives at the dynamical level. Code: this http URL.

---


### 426. [Evaluation of Contextual Understanding in Large Language Models](https://arxiv.org/abs/2609.09004)

**<font color=#1a73e8>作者：</font>** Subavarshana Arumugam, Mamta Nallaretnam, Kithuni Wickramasinghe 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) demonstrate impressive performance across diverse NLP tasks, yet their ability to exhibit genuine contextual understanding remains uncertain. Traditional evaluation metrics such as perplexity, BiLingual Evaluation Understudy (BLEU), or surface-level accuracy fail to reveal how well LLMs extract, integrate, and reason over contextual information--a gap particularly critical in question answering, where models must align responses with contextually grounded knowledge rather than memorized associations. We propose a novel knowledge graph-based evaluation framework introducing Semantic Structural Similarity for KGs (S3KG), a hybrid similarity measure integrating structural and semantic similarity into a continuous evaluation score, alongside a diagnostic framework for categorizing reasoning errors. To validate this pipeline, we evaluate S3KG against established metrics on a curated question-answer (QA) benchmark, demonstrating its effectiveness in measuring correctness, faithfulness, and interpretability in LLM-generated responses.

---


### 427. [Answer-Distribution Trajectories: A Stochastic-Dynamics View of LLM Reasoning](https://arxiv.org/abs/2609.09030)

**<font color=#1a73e8>作者：</font>** Mar Gonzàlez I Català, Haitz Sáez de Ocáriz Borde, Davide Murari 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought reasoning provides a structured computation between a model's input and final answer. Yet it is often evaluated through endpoint accuracy, which ignores the path taken to reach that answer. An emerging line of work addresses this limitation using entropy profiles, which track how uncertainty evolves over the reasoning process but do not reveal which competing hypotheses account for that uncertainty. We introduce answer-distribution trajectories, a stochastic-dynamics-inspired representation that tracks the model's full predictive distribution over answers as reasoning unfolds. As a strictly finer representation than endpoint and entropy summaries, answer-distribution trajectories enable us to characterize a trace through a dynamical reasoning profile spanning exploration, revision, motion, and commitment, and to distinguish different dynamical mechanisms of reasoning success and failure. Across sixteen open-weight language models and four reasoning benchmarks, we show that traces with the same endpoint and similar entropy profiles can exhibit substantially different reasoning dynamics. We further find substantial variation in these dynamics both within and across models and tasks, with different objectives favoring different dynamical profiles. Additionally, we show that training and inference choices systematically reshape these profiles. Our results suggest that answer-distribution trajectories provide a rich framework for analysing and evaluating the dynamics of LLM reasoning.

---


### 428. [Do Reasoning Representations Help Humans Evaluate LLM Outputs?](https://arxiv.org/abs/2609.09038)

**<font color=#1a73e8>作者：</font>** Jaewoo Lim, Sungbok Shin, Sanghyun Hong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning representations are increasingly used as explanations for large language model outputs. Yet they are typically evaluated with model-centric criteria, such as answer accuracy and faithfulness, leaving it unclear whether they help people evaluate model responses. In this work, we study reasoning representations as human-facing interfaces rather than proxies for model reasoning ability. We conduct a controlled human study of six reasoning formats across tasks of varying complexity, supported by a web-based framework that randomizes task domains, problem instances, and representation order. The study collects fine-grained judgments of structural understanding, error detection and localization, and trust calibration. Our study shows a mismatch between perceived preference and support for human evaluation. Participants prefer planning- and decomposition-based representations, but simpler chain-of-thought traces better support verification, trust, and interpretability. Preferred representations also introduce calibration risks, with more false alarms on correct traces and high trust despite low willingness to verify.

---


### 429. [The Audit Decides the Verdict: Instrument Effects Rival Demographic Bias in LLM Decision Audits](https://arxiv.org/abs/2609.09048)

**<font color=#1a73e8>作者：</font>** Siddharth Vohra, Manikandan Ravikiran  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Whether a language model looks demographically biased can depend on how the audit asks its question. A charitable-aid benchmark reports that the same models favor minority applicants when rating requests one at a time and penalize some when ranking side by side. We test whether that reversal generalizes to hiring, lending, and medical triage: 40,726 requests to five models, applications differing only in the applicant's name, and a primary test fixed before collection. It does not. None of 36 planned contrasts survives correction. The rating advantage keeps its sign at roughly half the published size, and a precision extension bounds any hiring ranking penalty below the published effect, though the lending and triage ranking floors sit above that margin, so the exclusion is conclusive for hiring ranking and for rating in all three domains only. Planted disparities tracking their injected sizes and a directional replication on the original aid materials bound these nulls. The audit is livelier than the demographics: models recognize transparent audits nearly always, tie every identical-content comparison whether the varying detail is race or a hobby, and reward first-listed candidates as much as any demographic effect we measure. Audit verdicts reflect audit construction more than demographic bias.

---


### 430. [Training-Free Task Vectors for LLM Behavioral Control](https://arxiv.org/abs/2609.09054)

**<font color=#1a73e8>作者：</font>** Gabriel J. Perin, Lucas Boscaini, André Araujo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Task vectors enable post-training model editing by identifying semantically meaningful directions in weight space, typically computed as the difference between a fine-tuned model and its pretrained initialization. However, this reliance on fine-tuning makes discovering such directions costly and limits the practicality of post-training model editing. To address this limitation, we introduce Training-Free Task Vectors (TFTVs), a novel method to compute task-vector-like directions without requiring fine-tuning. Our method maps activation steering vectors to rank-one weight-space edits using only forward-pass statistics, while satisfying arithmetic properties that directly support learning via addition, forgetting via subtraction, and the composition of multiple edits. Empirically, we evaluate TFTVs on large language model behavioral control tasks and show that they consistently amplify, suppress, and compose target behaviors while preserving general knowledge and problem-solving skills. We also validate our method against other editing and steering baselines, experimentally demonstrating that TFTVs achieve stronger trait control with better or competitive utility preservation. We hope our work opens new directions for the community in post-training model editing and broader training-free model control. Code is available on the project website: this http URL.

---


### 431. [PlayTrain: An Efficient Reinforcement Learning Framework for LLM-Generated Adaptable JavaScript Games](https://arxiv.org/abs/2609.09059)

**<font color=#1a73e8>作者：</font>** Ryan Truong, Lance Ying, Samuel J. Gershman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While many video-game environments (VGEs) have played crucial roles in advancing reinforcement learning (RL), developing novel VGEs or modifying existing ones to support new features, has been a laborious process requiring extensive hand-coding. Here we present PlayTrain, an RL framework that combines the abilities of large language models (LLMs) to robustly generate JavaScript (JS) games from a minimal human prompt, and an efficient pipeline that can run any JS game in a standard 'gym' environment. Not only are recent LLMs particularly good at writing JS code, but the JS format also allows users to easily play generated VGEs, while PlayTrain enables us to train RL agents on the exact same games. We demonstrate multiple use cases of PlayTrain, including cloning well-known Atari and ProcGen games in simple JS, where PlayTrain trains pixel-based agents end-to-end at over 1M agent-decisions per second on a single GPU node; and creating modified versions thereof (e.g., that support novel test sets, procedural generation logics, or game dynamics). Through PlayTrain, we reimagine RL VGE development: all we need is a single JS file, generated and modified through an LLM. We discuss promising future RL research directions that PlayTrain unlocks.

---


### 432. [Performance of Clinical AI System and Physicians and Frontier Language Models in primary care diagnostics](https://arxiv.org/abs/2609.09070)

**<font color=#1a73e8>作者：</font>** Andy Nkansah, Hanna Plotnitskaya, Stanislau Salavei 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical AI evaluation should encompass diagnosis and management after adaptive information gathering. We compared Doctorina, eight physicians and four standalone frontier language models in 150 synthetic Polish-language primary-care consultations. Doctorina achieved 82.0% Top-1 concordance versus 57.0% for physicians (difference, 25.0 percentage points; 95% confidence interval, 17.7-32.7) and 97.3% versus 85.0% primary-or-reference-differential concordance. Across 149 case pairs, normalized workup and treatment scores were 89.4 versus 66.9 and 83.7 versus 61.2. Doctorina had the highest diagnostic point estimates among all six groups; Kimi K3 ranked next, while Claude Opus 5 led the closely spaced management estimates of Opus, Doctorina and Kimi. A second Doctorina execution reproduced the advantages over physicians across all outcomes. Doctorina's advantage over physicians therefore extended from primary-diagnosis selection to higher-rated diagnostic workup and initial treatment after adaptive consultation.

---


### 433. [ToolLoop: Closed-Loop Tool-Use Data Synthesis via Decomposed Generation and Dynamic Self-Feedback](https://arxiv.org/abs/2609.09072)

**<font color=#1a73e8>作者：</font>** Min Zeng, Yuzhou Liu, Zhenyu Cao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> High-quality tool-use data is critical for training language models to interact effectively with external tools. However, existing synthetic approaches typically follow a generate-then-filter paradigm with static post-hoc verification, often yielding inefficient data with imbalanced feature distributions. We propose ToolLoop, a closed-loop framework that decomposes synthesis into three progressive stages: (1) sampling function name combinations as ground truth; (2) backward derivation of user queries; and (3) forward derivation of tool calls. At each stage, dynamic self-feedback iteratively guides the model toward high-quality generation, realizing a transition from generate-then-filter to generate-verify-refine. On the Berkeley Function Calling Leaderboard (BFCL), a 4B parameter model trained with our 11K synthetic examples achieves 86.40% accuracy in non-reasoning mode, while an Isolate variant that removes BFCL-overlapping candidate functions still reaches 86.07\%. Cross-benchmark evaluation on ACEBench further demonstrates strong generalization, with 72.1% overall accuracy using only 18.3% of baseline training data.

---


### 434. [ThinkPrior: Zero-Rollout Difficulty Priors for Cold-Start Prompt Selection in RLVR](https://arxiv.org/abs/2609.09075)

**<font color=#1a73e8>作者：</font>** Tommy Sha, Skylar Zhai, Siqi Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In reinforcement learning with verifiable rewards (RLVR) trained with group relative policy optimization (GRPO), the KL-free reward-advantage term studied here depends on within-group reward variation. If all rollouts in a group are correct or all are wrong, their group-relative advantages are identically zero; these zero-advantage silent groups provide no reward-advantage gradient, yet uniform sampling spends 39% of a run's rollouts on them. History-based prompt selection must first spend target-policy rollouts to estimate difficulty, creating a cold start with rollout waste; ThinkPrior instead uses an external anchor in one offline pass to construct a zero-rollout difficulty prior before the first target-policy rollout. The verifier-scored anchor pass rate supplies an external-anchor initialization for a Beta posterior; ThinkPrior selects by expected learnability and then updates from training outcomes, changing neither the loss nor the optimizer. On Qwen2.5-Math-7B across sixteen seeds, ThinkPrior more than halves early silent groups and cuts wasted rollouts through step 30 by nearly a fifth, while we detect no difference in final accuracy. On this 250-prompt pool the fixed-budget result is a reallocation rather than a net saving. The measured ThinkPrior+DAPO composition reduces generated rollouts by 10.6% while both arms retain the same 3840-rollout update budget. The prior requires no target-policy rollout before the first selection, but the posterior thereafter uses target-policy outcomes.

---


### 435. [ActReview: Rebuttal-Guided Training Data and Rubric Rewards for Actionable Peer Review Generation](https://arxiv.org/abs/2609.09076)

**<font color=#1a73e8>作者：</font>** Yiling Ma, Yilun Zhao, Sihong Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As LLMs are increasingly used for pre-submission self-review, there is growing demand for feedback that not only identifies weaknesses but also guides authors toward concrete revisions. We study this as Actionable Peer-review Generation and decompose it into two subtasks: diagnostic claim generation and revision suggestion generation. We introduce ActReview, a rebuttal-guided post-training framework that connects paper-specific diagnoses to concrete, grounded revision plans. Our central insight is that author rebuttals reveal plausible actions for addressing reviewer concerns and can therefore provide latent supervision for revision-oriented feedback. From real review-rebuttal threads on OpenReview, we construct ActReview-40K by aligning reviewer weaknesses with author responses and grounding the resulting feedback in localized paper evidence. We post-train Qwen3-8B-Base with multi-task supervised fine-tuning followed by GRPO using candidate-aware, weakness-specific rubric rewards. We also introduce ActReview-Bench, a human-curated benchmark of 1,000 instances for evaluating diagnostic quality and revision usefulness. Experiments show that ActReview outperforms prior specialized review-generation models on actionability and grounding while remaining competitive with strong prompt-based LLMs. Human evaluation confirms improved revision usefulness while revealing a remaining gap in technical accuracy, and additional analyses support generalization to held-out papers and robustness across independent judges.

---


### 436. [Everything in Moderation: Per-Domain Coverage Optima and Alignment-Resistant Domain Gaps in Multi-Domain Mid-Training](https://arxiv.org/abs/2609.09081)

**<font color=#1a73e8>作者：</font>** Yunpeng Xu, Kun Zheng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mid-training, the stage between pre-training and alignment, is where a model's per-domain data composition is typically set by data availability rather than principled design. We ask what that decision buys, and whether a later alignment pass can undo it. In a controlled logical-reasoning setting (Qwen3-8B-Base, with a 4B replication; five semantically rule-disjoint KOR-Bench domains) we train 30 allocations spanning the five-domain simplex, 24 sweep configurations plus six withheld from the fit, at five seeds each. Three findings emerge. First, every domain has an interior coverage optimum: the moderate band ($10\%$-$40\%$) is best for all five domains, and a calibrated permutation test for quadratic interiority gives $P\approx0.010$; the fitted mid-training-only curves, with 8B peaks between $9.9\%$ and $35.1\%$, reproduce for curve shape but not peak location. Second, the gaps survive a fixed-budget alignment pass: compensatory SFT raises 116/120 cells (mean $+4.32\%$) yet bridges $0/240$ pairs at a $5\%$ threshold and $30/240$ at a $10\%$ ratio, an equal-budget uniform control behaves almost identically, and a permutation null would bridge $13.8\pm3.3$ and $77.9\pm8.5$ pairs ($P<0.001$). Third, zero coverage collapses mid-training-only accuracy, though a FineWeb-Edu-only control shows the collapse is commingled with generic drift. An exploratory $\theta^*$ allocation attains the largest full-pipeline gain ($+4.36\%$ vs. $+0.80\%$/$+0.64\%$\,pp) but is marginal under Welch test.

---


### 437. [GoDeep: Annotation-Free Open-Vocabulary 3D Scene Understanding via Language-Space Lifting](https://arxiv.org/abs/2609.09082)

**<font color=#1a73e8>作者：</font>** Thodoris Betsas, Anastasios Doulamis, Andreas Georgopoulos  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open vocabulary 3D semantic segmentation methods typically lift CLIP features into 3D. This embeds points in a joint vision-language space known to behave like a bag-of-words on compositional tasks. Furthermore, even annotation free variants often require a large 3D training corpus and a dedicated 3D encoder per domain. Instead we use a vision-language model purely as a translator. It produces structured, entity-level descriptions of each posed image. These descriptions are grounded, projected, and aggregated directly in a general-purpose, language-only embedding space, with no 3D training corpus or encoder required. On ScanNet++, our pipeline is competitive with strong annotation free baselines trained on ScanNet. On a 5-building cultural heritage benchmark, raw scores initially favor a CLIP-based variant, but a single systematic vocabulary correction reverses this ranking. An effect confirmed by a second, independent correction on a different class, indicating that language-space embeddings track physical content more faithfully. This fidelity extends to genuinely out-of-vocabulary (OOV) objects on ScanNet++ proving that language-space embeddings separate presence from absence objects far more sharply than CLIP-based embeddings do. GoDeep also localize these OOV objects within the scene, all without any 2D-3D annotation. Because every representation remains discrete text, predictions are also explainable at the point level. Finally, exploiting both a heuristic weighting, that favors precise over merely frequent observations and GoDeep's explainability property, we propose an aggregation strategy, as a proof of concept, that favors finer elements localization.

---


### 438. [It's Not RoPE that Creates Sinks: The Role of Self-Concentration and Value-Non-Mixing in Attention](https://arxiv.org/abs/2609.09085)

**<font color=#1a73e8>作者：</font>** Raito Kiya, Satoki Ohashi, Kosuke Sato 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) often exhibit "Attention Sink" (AS) and the accompanying "Massive Activations" (MAs) at the initial position of a sequence. These phenomena frequently co-occur, and MAs can pose challenges for low-bit quantization. In this study, we analyze the factors underlying AS and MAs that emerge at the initial position regardless of the token occupying it. Our experiments suggest that self-concentration of attention, resulting from the causal mask, and the subsequent Value-non-mixing in attention outputs contribute to AS and MAs. These findings provide new empirical evidence on the internal dynamics of LLMs, offering insights that may inform future quantization strategies and advance our understanding of the internal mechanisms of attention layers.

---


### 439. [PrivEscalate: Measuring and Augmenting the Threat of LLM-Automated Linux Privilege Escalation](https://arxiv.org/abs/2609.09087)

**<font color=#1a73e8>作者：</font>** Yixuan Liu, Zilong Zhen, Yin Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As Large Language Model (LLM) agents increasingly automate offensive operations across the cyber kill chain, their efficacy in complex local post-exploitation tasks remains inadequately quantified. Among these, Linux privilege escalation is a key step between initial access and full system compromise. However, existing evaluations for this task are limited by small sample sizes (fewer than 15 scenarios), lacking the scale to compare model capabilities under executable verification. To address this, we present PrivEscalate, a large-scale benchmark for Linux privilege escalation, comprising 531 Dockerized scenarios spanning 14 sub-categories. We additionally derive 329 parameterized variants to measure sensitivity to environmental distractors.
Evaluating six LLMs across three agent architectures reveals: (i) model capability is heterogeneous across vulnerability classes, with no single model dominating across the high-prevalence classes, motivating multi-dimensional risk assessments; (ii) LLM successes are sensitive to environmental perturbation, so configuration rotation can disrupt some exploit attempts but does not eliminate the measured risk; and (iii) agent architectures can materially change success rates and reorder model rankings, though the magnitude is model-dependent. Leveraging these insights, we develop PrivEscAgent, a domain-specialized wrapper that augments a generic ReAct agent with deterministic enumeration, category matching, and step planning. PrivEscAgent improves over prior Linux privilege-escalation agent baselines without underlying LLM modifications. We release PrivEscalate as an open-source, Dockerized measurement instrument supporting LLM agent evaluation, defensive tool validation, and red-team training.

---


### 440. [Measuring LLM Sycophancy under Sustained Multi-Turn Pressure](https://arxiv.org/abs/2609.09090)

**<font color=#1a73e8>作者：</font>** Leyuan Tang, Kangda Wei, Tianyu Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) may abandon correct positions when users push back, exhibiting a failure mode known as sycophancy. Existing evaluations typically use short, pre-specified conversations and may therefore miss failures that emerge under sustained, adaptive disagreement. We introduce SPINE, a benchmark in which an LLM proxy plays a persistent but mistaken user and adaptively challenges a target model for up to 25 turns. We evaluate four production systems and three Olmo3-7b variants on 100 false-presupposition and 100 unethical-query items. Our experimental results show that collapse rates increase with conversation length for every model, short-horizon protocols underestimate sycophancy and resistance under sustained pressure remains unreliable across current models. By analyzing models with accessible reasoning traces, we surprisingly found that the correct position often remains represented in a reasoning trace when the response concedes, suggesting that the model chooses to please a user and sycophancy is not due to lack of knowledge or ignorance. Ablations show that adaptive LLM proxy exposes more sycophantic collapse than pre-generated scripts. Among all tactics, emotional appeals is the most associated with inducing LLM sycophantic behavior. The code and data are released at this https URL

---


### 441. [SAEScientist-Bench: Can AI Agents Conduct Autonomous SAE Interpretability Research?](https://arxiv.org/abs/2609.09113)

**<font color=#1a73e8>作者：</font>** Yuqiao Tan, Shizhu He, Jun Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While research on recursive self-improvement (RSI) has predominantly automated model training pipelines, reliable autonomous development demands a missing pillar: post-hoc monitoring and auditing to understand what models learn and ensure safe alignment. Mechanistic interpretability tools are essential to bridge this gap, among which Sparse Autoencoders (SAEs) serve as a cornerstone by isolating interpretable features for model inspection and steering. In this paper, we introduce SAEScientist-Bench to evaluate whether AI agents can act as scientists utilizing SAE tools for autonomous mechanistic discovery. Given a target concept, an agent designs contrastive probes and navigates a Gemma Scope dictionary of 131K+ features in Gemma-2-9B-IT to discover the optimal feature, evaluated against curated expert reference features anchored on Neuronpedia across activation rank, concept selectivity on contrastive texts, and causal steering. Across 10 agent configurations and 20 tasks, frontier agents demonstrate genuine discovery capabilities and lead different evaluation dimensions, but remain well behind the expert baseline, approaching expert levels on separating target concepts from contrastive controls while lagging substantially in causal generation steering. Further analysis reveals that although agents can design contrasts to rule out spurious candidates, they frequently misinterpret experimental measurements. These results establish experimental model understanding as a measurable capability for closed-loop autonomous AI R&D. Our code is available at this https URL.

---


### 442. [MeClear: Cooperative Game-Theoretic Attribution and Risk-Aware Memory Clearance for Long-Horizon LLM Agents](https://arxiv.org/abs/2609.09115)

**<font color=#1a73e8>作者：</font>** Boyu Yang, Jiazheng Sun, Zilong Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long horizon Large Language Model (LLM) agents rely on external memory systems to preserve user preferences and task knowledge across extended interactions. Conventional retrieval mechanisms optimize semantic compatibility rather than downstream utility, frequently introducing outdated, misleading, or conflicting evidence into the active context. We present MeClear, a task conditioned memory clearance framework that identifies memories featuring negative downstream utility through cooperative attribution and selectively suppresses them from agent execution. MeClear combines Leave One Out screening with sampled cooperative Shapley attribution to distribute utility across interacting evidence, effectively resolving redundant conflict masking where single removal evaluations fail. Utilizing attribution rankings, MeClear executes a query scoped minimal clearance strategy over a nested filtration, verifying task recovery on the cleared context without permanently altering the persistent memory bank. Comprehensive experimental evaluations across ten long dialogue memory pools demonstrate that MeClear achieves a target recall of 85.9% and an overall task recovery rate of 82.3%, representing a 25.5 percentage point improvement over Leave One Out (LOO) baselines.

---


### 443. [When Does Scale-Invariant Optimization Become Unstable? An Exact Schedule Law with Weight Decay](https://arxiv.org/abs/2609.09116)

**<font color=#1a73e8>作者：</font>** Hasan Amin, Wei-Kai Chang, Rajiv Khanna  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Normalization renders large parts of neural networks effectively scale invariant, inducing a hidden feedback loop in which learning-rate schedules and weight decay interact through the parameter norm to control the effective step taken by the optimizer. We show that this interaction is governed by an exact discrete-time law: a single scalar quantity captures all schedule and decay forcing, while norm growth induces an opposing geometric self-quenching effect. This yields a sharp boundary that cleanly separates contraction- and expansion-dominated effective learning rate regimes. To understand the underlying mechanism, we provide exact analysis of a fully solved normalized regression model where the dynamics reduce to two dimensions and show that the balance point is intrinsically unstable, implying that constant learning rate with weight decay cannot stably maintain an interior equilibrium and instead produces recurrent behavior driven by discrete-time Jacobian structure. We further extend this perspective across optimizers through unified homogeneous-optimizer framework that reveals a structural dichotomy in self-quenching strength, providing a first-principles explanation for why adaptive methods exhibit systematically weaker stabilization under normalization.
Across dynamical systems and neural networks (MLP, CNN, GPT2 / MNIST, CIFAR, wikiText, OpenWebText), the predicted law holds with high precision and enables direct control of training via the identified scalar, with performance peaking sharply at the predicted boundary. Together, these results isolate a single governing quantity for scale-invariant optimization, providing a precise and actionable lens on training dynamics, optimizer behavior, and schedule design in modern deep learning. Code is available in this https URL.

---


### 444. [Canonical Color as a Lens into Concept Decodability in Vision Encoders and VLMs](https://arxiv.org/abs/2609.09124)

**<font color=#1a73e8>作者：</font>** Xiaofu Chen, Stella Frank, Yova Kementchedjhieva  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual encoders construct a representation of the image input for Vision-Language models. How much conceptual, as opposed to immediately visible, information does this representation contain? We use canonical color as a controlled test case to ask whether vision encoders make canonical-color information linearly accessible, even when color is removed from the input image. We construct a dataset of objects with canonical colors, and probe vision encoders for both color and object identity using color and grayscale images. We find that canonical color remains decodable from grayscale images, and is tied to predicted object identity, indicating a conceptual link. Extending this analysis to full VLMs, we find that VLM post-training can have a surprisingly large effect on color decodability in the vision encoder. Overall, canonical color provides a usefully controllable lens for tracing object-level conceptual semantic information in vision encoders and VLMs.

---


### 445. [ExecCritic: Learn to Test, Test to Improve for Coding Agents](https://arxiv.org/abs/2609.09133)

**<font color=#1a73e8>作者：</font>** Leitian Tao, Baolin Peng, Haorui Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Execution feedback can guide coding agents toward correct repository repairs, but only when the tests capture the behavior requested by the issue. Agent-generated tests can encode incomplete or incorrect behavioral targets; when the same trajectory writes both the patch and the test, their errors can agree and create false confidence. We introduce ExecCritic, combining a test--verify--revise scaffold with a role-specific reinforcement learning recipe for training agents within it. The scaffold separates test construction from source-code repair: a Test agent independently generates repository-native tests, a fail-closed harness qualifies and freezes them, and a Repair agent revises source code from their execution feedback without changing the tests. Both roles use Qwen-3.5-35B-A3B as the backbone and are trained separately. In Learn to Test, the Test agent learns to produce behaviorally valid tests that distinguish correct from incorrect patches. In Test to Improve, the Repair agent learns both direct task resolution and feedback-guided revision. On SWE-bench Verified, test quality determines whether feedback helps: holding the base Repair agent fixed, tests from the base Test agent reduce resolved rate from a no-test baseline of 61.2% to 57.3%, whereas tests from GPT-5.6-sol raise it to 65.3%. Role-specific post-training raises the Qwen Test agent's Base-to-Gold success from 22.2% to 62.2%; composing the two post-trained Qwen agents reaches 72.6%, an 11.4-point gain over the original no-test baseline without stronger-model or Oracle feedback at evaluation time. Code is publicly available at this https URL.

---


### 446. [Co-Evolving Harnesses and Models: On-Policy Correction Helps Weaker Models Catch Up Where Imitation Fails](https://arxiv.org/abs/2609.09134)

**<font color=#1a73e8>作者：</font>** Zhou Yu, Bin Bi, Shiva Kumar Pentyala 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent harnesses (the system prompt, tool set, execution hooks, and context-management scaffolding around a model) are a critical determinant of agentic task success. Automated harness evolution can enable smaller models to perform well on domain-specific tasks at a fraction of frontier-model cost. Since both the harness and model weights shape behavior, we ask how harness evolution and lightweight fine-tuning should be combined. Across seven enterprise agent tasks, we first evolve a harness with the weaker model, then find that a stronger expert often uses it more effectively, suggesting expert supervision could close the remaining gap. However, training the weaker model on the expert's complete trajectories under the evolved harness backfires: performance regresses on all seven tasks by 4 to 30 points across Qwen3-Coder and Gemma 4, even though the same procedure helps under the unevolved harness. Our analysis shows that imitation transfers knowledge and increases scaffold usage, but disrupts model-harness fit: the weaker model adopts the expert's planning strategy without the competence to execute it and no longer matches the harness evolved around its native planning style. We therefore develop an on-policy expert-correction pipeline, automated by a meta-level MLE agent, that localizes the failing turn in the weaker model's own rollout and asks the expert to rewrite only that turn. This preserves the model's planning style and combines the gains of harness evolution and model adaptation. Our results identify and resolve a source of contention between harness and weight updates, yielding a compatibility-preserving recipe for economical co-evolution on domain-specific enterprise tasks.

---


### 447. [Procedural Graphs: Self-Evolving Execution Structures for LLM Agents](https://arxiv.org/abs/2609.09153)

**<font color=#1a73e8>作者：</font>** Yuxing Lu, Yicheng Chen, Shanchan Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed as agents that plan over long horizons and act through external tools. Most agents select actions through unconstrained generation over an accumulating history, leaving implicit the procedural knowledge of what to do, in what order, and under which conditions. As trajectories lengthen, agents can lose track of their objectives, invoke tools out of order, and repeat unproductive actions. We introduce the Procedural Graph: just as a knowledge graph organizes factual knowledge into (entity, relation, entity) triplets for what-is questions, a Procedural Graph organizes procedural knowledge into (procedure, relation, procedure) triplets for what-to-do questions. At each decision step, the framework localizes the agent's active node, and a guidance model translates the surrounding subgraph into step-level situational guidance that biases the solver's next action without dictating it. The graph is self-evolving: an LLM refiner contrasts failed trajectories with successful ones and edits the graph's topology and attributes, committing edits that preserve or improve held-out validation performance while retaining rejected ones to discourage repetition. Starting from a minimal skeleton, the loop builds graphs that match or surpass hand-designed ones. It can also repair a flawed expert prior. Across multiple datasets, task types, and LLMs, the Procedural Graph delivers consistent gains over memory-based baselines, and self-evolution further improves performance without manual engineering.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 448. [CaseWeaver: A Multi-Agent Framework for Multimodal Virtual Clinical Case Generation](https://arxiv.org/abs/2609.05480)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jierui Qu, Jiachuan Peng, Lin Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Clinical diagnosis relies on consistent multimodal data collected from the same patient throughout the disease course, yet such data are difficult to acquire at scale because of collection costs, missing modalities, fragmented systems, and longitudinal follow-ups. Existing synthetic-data approaches largely focus on individual modalities or vision-language dual modalities at report-level generation. Little work has been done to construct synthetic data with consistent patient backgrounds, coherent disease trajectories, and interrelated modality-specific evidence at a complete clinical case level. We introduce CaseWeaver, a multi-agent framework built around a timeline-anchored Latent Clinical Case Graph (LCCG). The LCCG organizes patient context, latent disease states, clinical events, and expected observations in a shared patient-level representation. Modality-agents use scoped observation subgraphs and clinical protocols to generate evidence including clinical records, laboratory results, physiological signals, and medical images. We evaluate clinical inferability using a calibrated AgentClinic protocol and case diversity using Virtual Case Diversity (VCD) score. CaseWeaver outperformed general-model and agentic-workflow baselines on both metrics, producing more diverse and coherent multimodal virtual clinical cases.

---


### 449. [Hierarchical Prompt Injector for Domain Generalization Segmentation](https://arxiv.org/abs/2609.05864)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xin Kun Lin, Ruoyu Guo, Jiaqi Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Domain Generalized Semantic Segmentation (DGSS) is a challenging task, as vision models often rely on low-level appearance cues that change across domains. In contrast, structural attributes exhibit cross-domain stability, motivating the use of structural priors for DGSS. Existing methods use prompt learning to transfer such priors into DGSS models, but typically encode each class as a single holistic prompt. Moreover, these methods apply prompts uniformly to all pixels, offering no mechanism to adapt when only a subset of object regions is visible due to viewpoint changes, occlusion, and environmental variation. We address this with \textbf{Spatial Hierarchical Prompts (SHP)} that enrich each class with region-level geometric anchors capturing structural appearance from distinct viewing angles, ensuring complementary coverage under arbitrary viewpoints. Additionally, we propose the \textbf{Hierarchical Prompt Injector (HPI)}, which enables spatially adaptive prompt injection in foundation models. HPI spatially grounds prompts by modeling their semantic relevance and spatial influence with visual features. Considering the difficulty of learning spatially and semantically aware prompt injection, we further introduce auxiliary supervision to align hierarchical prompts with their corresponding object regions. We achieve 70.62\% and 72.74\% mIoU on synthetic-to-real and real-to-real benchmarks, respectively. Code and checkpoints are released at this https URL

---


### 450. [FACT: A Forensic Agent with Compiled Tool-Use Trajectories for AI-Generated Image Detection](https://arxiv.org/abs/2609.05876)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jiaoyang Chen, Bin Hu, Jingyu Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-generated image detection is increasingly open-world: new image generators produce highly realistic images that make visual artifacts harder to identify. Existing detectors usually rely on a fixed set of forensic cues, so a detector that works well for one generator family may fail on another. We introduce FACT (Forensic Agent with Compiled Tool-use Trajectories), which learns an image-conditioned tool-use policy for forensic analysis. Instead of applying a fixed detector, FACT decides which forensic tools to call, interprets the returned evidence, and stops when sufficient evidence has been collected. FACT follows an Evolve--Distill--Refine pipeline: it evolves an execution-verified forensic skill, compiles the skill into action--observation tool-use trajectories, distills them into a compact agent, and refines the policy with cost-aware GRPO. Across two internal and four public benchmarks, FACT achieves the best performance among all compared methods, including on recent unseen generators, deepfakes, and manipulated images.

---


> [!TIP]
> 当前位于：**401-450**（第 9/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-483](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
