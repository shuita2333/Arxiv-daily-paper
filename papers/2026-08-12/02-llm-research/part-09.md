# 🧠 大模型相关研究 | 2026年08月12日

> 本类共 **438** 篇论文：已确认 **404** 篇，待复核 **34** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**401-438**（第 9/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-438**

---

### 401. [DistMoE: Private-data Rehearsal-free Routing in Mixture-of-Experts for Distributed Instruction Tuning](https://arxiv.org/abs/2608.09907)

**<font color=#1a73e8>作者：</font>** Mainak Singha, Niccolò Biondi, Elisa Ricci 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have shown strong multimodal instruction-following ability, but adapting them to diverse visual-language domains typically assumes centralized data access and costly joint training. This is restrictive when data is distributed across private, domain-specific, or permission-limited clients. To this end, we propose DistMoE, a mixture-of-experts (MoE) approach for distributed visual instruction tuning. In each layer of the language decoder it augments the public feedforward network (FFN) with a client-specific private FFN expert, with the goal to acquire domain-specific knowledge. However, independent expert training causes the private FFNs to learn representation of different scale and magnitudes, making merging the experts difficult. To reduce client-specific drift, we introduce a public-anchored expert composition stage that updates only routers and lightweight private projection adapters on a mix of local client data and public data, via an isotropic regularization loss, therefore making it cross-client rehearsal-free composition. During inference, DistMoE performs modular routing over public and private experts, enabling token-wise domain composition without explicit domain labels. Experiments across diverse visual-language benchmarks show that DistMoE enables flexible expert reuse, effective domain adaptation, and competitive performance while preserving modular control over client-specific knowledge. Codes are available at this https URL.

---


### 402. [From Values to Benchmarks: Evaluating Large Language Models for Governmental Use in Dutch](https://arxiv.org/abs/2608.09925)

**<font color=#1a73e8>作者：</font>** Laurens Samson, Iva Gornishka, Gossa Lô 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly being deployed in governmental settings, yet few existing evaluation frameworks jointly reflect the values of public administration and the linguistic requirements of non-English contexts. We present the "Grip on LLMs" framework, a systematic evaluation suite for Dutch governmental use developed in collaboration with domain experts from a major Dutch municipal organisation. Through an advisory board process, user research, and a survey of the users of a civil-servant chatbot, we identify six evaluation dimensions (factuality, honesty, social bias, energy consumption, cost, and training data transparency) and operationalise them into a benchmark suite covering more than 30 multilingual and Dutch-specific models. Our results reveal that no single model excels across all dimensions, and that trade-offs are unavoidable: higher quality consistently comes at greater environmental impact and financial cost, while bias remains largely independent of both. We further find that factuality (whether a model answers correctly) and honesty (whether a model acknowledges what it does not know) are governed by distinct properties, with high factuality not implying high honesty. To make these findings actionable for non-technical audiences, we release a publicly accessible, user-friendly model overview designed for the full range of stakeholders involved in governmental LLM selection, from engineers to policymakers.

---


### 403. [Multimodal Model Diffing for Feature Discovery and Control](https://arxiv.org/abs/2608.09928)

**<font color=#1a73e8>作者：</font>** Hunar Batra, Lachin Naghashyar, Ashkan Khakzar 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) exhibit strong visual understanding, yet the internal features that cause these behaviors remain difficult to identify, audit, or control. While applicable to post-hoc inspection, hidden states that are decomposed into interpretable feature directions using sparse autoencoders (SAEs) neither readily isolate which features are changed by multimodal training, nor are they directly useful for targeted control. We introduce MMDiff, a multimodal model-diffing framework that trains multimodal SAEs and turns them into feature-level interfaces for discovering and controlling multimodal behavior. MMDiff supports three uses: (i) feature isolation, by diffing a base-LM SAE against its multimodal-adapted counterpart to identify features altered by multimodal training; (ii) task-specific feature detection, via per-token contrastive firing analysis that isolates causal features; and (iii) feature-level control, by causally removing or steering the discovered feature directions. We train multimodal SAEs for three MLLM families, LLaVA-MORE, PaliGemma 2, and InternVL3.5, and evaluate on visual-spatial understanding, multimodal safety, and OCR. MMDiff discovers sparse, causally specific features whose removal selectively degrades target behaviors by an average of 12% on spatial tasks and 17% on OCR, and reduces attack success rate by 24% on multimodal safety attacks, with no impact on VQA performance. Steering these features improves spatial and OCR accuracy by +3.6% and +1.8% on average over a standard single-layer steering baseline. These results show that multimodal SAEs can serve not only as interpretability tools, but as mechanisms for auditing, steering, and controlling MLLMs behavior toward safer and more capable generations.

---


### 404. [Perception Before Supervision: Self-Contained Visual Distillation from Counterfactual Blind Spots](https://arxiv.org/abs/2608.09931)

**<font color=#1a73e8>作者：</font>** Shravan Venkatraman, Omkar Thawakar, Ritesh Thawkar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-improvement for multimodal large language models (MLLMs) is typically driven by reward-based methods that provide only coarse scalar feedback. Distillation offers a richer alternative through dense token-level supervision, but in the visual domain it usually depends on privileged context constructed using external annotations and tools, or stronger models. We introduce \textbf{CVPD} (Contrastive Counterfactual Visual Process Distillation), which, to the best of our knowledge, is the first fully self-contained framework for dense, on-policy, token-level visual self-distillation for MLLMs. CVPD identifies visual blind spots where zooming into a region changes and sharpens the model's answer distribution, while removing the same region leaves the full-image behavior largely unchanged. Such regions reveal perceptual information that the model can encode but fails to consistently utilize under full-image conditioning. We propose a three-gate Counterfactual Criterion that identifies these regions directly from the model's own responses and converts them into dense contrastive supervision for self-distillation. On Qwen3-VL-8B-Instruct, CVPD outperforms six self-evolving baselines across twelve benchmarks, including methods that rely on external GPT-4o supervision, without a single regression. It achieves gains of $+3.60$ on OCRBench, $+3.38$ on MMStar Fine-Grained Perception, and $+3.08$ on MMStar Logical Reasoning, while maintaining or improving performance on broader multimodal benchmarks.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 405. [Protecting patient privacy in clinical foundation models: Technical and legal perspectives](https://arxiv.org/abs/2608.07705)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Sana Tonekaboni, Lena Stempfle, Sasha Ronaghi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical foundation models trained on large-scale patient data are increasingly used for decision support, screening, and public health. As deployment expands, privacy risk increasingly arises from model-mediated leakage, yet its prevalence and severity remain poorly quantified. Models can disclose sensitive training artifacts, enabling patient re-identification in ways not captured by data-handling controls alone. Existing frameworks, including HIPAA and GDPR, offer limited guidance for such indirect threats. We propose a practical framework for assessing privacy risk in clinical foundation models and illustrate realistic leakage scenarios across deployment settings, map them to legal regimes, and outline complementary technical and legal mitigations. Our analysis provides a context-aware risk assessment grounded in realistic usage to preserve the value of medical foundation models while rigorously safeguarding patient privacy.

---


### 406. [QuantumMind: Constraint-Grounded Agentic Reasoning for Speedup Analysis in Quantum Computing](https://arxiv.org/abs/2608.07743)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yijing Zuo, Zhe Fu, Zihan Nie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Identifying a meaningful quantum speedup requires more than matching a classical problem to a familiar quantum primitive: the claim must preserve the task, respect access and output models, expose required promises, and remain within a defensible complexity scope. We present QuantumMind, an auditable agentic workflow for generating and conservatively screening quantum-acceleration hypotheses. A fixed sequence of typed, role-specialized actions formalizes the public task, analyzes structure and classical bottlenecks, matches a source-linked registry of quantum primitives and barriers, and constructs a scoped candidate scheme. A deterministic ten-check validator assigns the authoritative verdict; completed states are compiled into a Quantum Acceleration Evidence Graph and passed through a downward-only research screen that cannot strengthen the decision. We evaluate QuantumMind against seven task-adapted prompting and agentic controls on 582 identical open-discovery tasks. Under the frozen Open-Discovery Score (ODS), QuantumMind obtains 53.1 mean ODS, exceeding the strongest baseline by 17.3 points (48.2% relative), and wins 355 of 582 paired tasks against that baseline. It passes the graph audit on 99.8% of tasks, compared with 43.6% for the strongest baseline, and ranks first in all seven task families. The results indicate that typed state transitions and deterministic evidence control contribute beyond fluent generation alone.

---


### 407. [DINO-3DRA: Leveraging 2D Foundation Model Semantics for 3D Cerebral Aneurysm Segmentation](https://arxiv.org/abs/2608.07767)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jiayang Lu, Fengming Lin, Alejandro F. Frangi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate aneurysm segmentation in 3D rotational angiography (3DRA) is hindered by extreme class imbalance, morphological similarity to vessels, and absent large-scale 3D pretraining. 2D vision foundation models encode dense structural priors from 1.7 billion images, yet naïve slice-wise transfer fragments anatomical continuity and destabilises optimisation. We propose DINO-3DRA, a dual-path framework achieving effective cross-dimensional semantic transfer by injecting frozen DINOv3 features into a 3D U-Net backbone via Room-Lite spatial mixing and calibrated residual fusion. On multi-centre 3DRA data, DINO-3DRA achieves state-of-the-art aneurysm segmentation (Dice: 0.758; HD95: 2.75 mm; +13% over nnU-Net) with only 5.72M trainable parameters. Ablation studies confirm that gains arise from structured cross-dimensional transfer rather than loss design alone, with bridged foundation features improving anatomical continuity between aneurysms and parent vessels. Without fine-tuning on CADA and SHINY-ICARUS, DINO-3DRA eliminates all catastrophic failure cases observed in baseline architectures, demonstrating robust generalisation across heterogeneous imaging protocols.

---


### 408. [Mobility, Memory, and Network Structure in Agent-Based Models of Convention Tipping and Convergence](https://arxiv.org/abs/2608.07810)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Joe Shymanski, Garrick Springer, Sandip Sen  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Tipping-point dynamics describe the critical conditions under which a committed minority drives a population to abandon an established convention in favor of a new one. We present a transparent agent-based model of this process, in which agents hold one of two behavioral states and a mobile committed minority attempts to overturn the incumbent convention. Our goal was to examine how localized mobility, bounded agent memory, and network topology jointly influence the tipping threshold. Using a custom agent-based simulation framework, we found that in many configurations, tipping becomes effectively inevitable: given sufficient time, the population always converges to the minority state. This observation motivated a complementary analysis focused on the pace of convergence rather than its feasibility. We introduce a unified predictive model that accurately estimates how structural and behavioral parameters determine the time required for complete adoption, showing that mobility is the dominant accelerator while memory and connectivity modulate convergence in systematic ways. Together, these results extend classical tipping-point research by linking structural and behavioral factors not only to the likelihood of convention change but also to the timescale on which it unfolds. While we frame the model in terms of convention-like binary behavioral adoption, the same mechanisms bear on norm change and other contagion-like social processes.

---


### 409. [On the use of foundation models in cognitive science](https://arxiv.org/abs/2608.07812)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Raj Sanjay Shah, Alex Warstadt, Michael Frank 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A host of recent studies have evaluated the cognitive and developmental alignment of Foundation Models (FMs). These investigations include evaluations of their correspondence to adult performance across a range of cognitive domains, as well as whether aspects of model training track children's cognitive development. However, using FMs as candidate cognitive models poses significant methodological and conceptual challenges. A key question underlies this effort: under what conditions does behavioral alignment justify treating FMs as explanatory models of cognition? In this paper, we articulate a four-stage inferential framework for evaluating FMs as cognitive and developmental models: adapting human experimental tasks to model-compatible formats, specifying linking hypotheses that map model outputs to human measures, evaluating behavioral correspondence, and comparing across candidate models or manipulations. We clarify the role of linking hypotheses in mapping model outputs to human behavioral measures, identify challenges that constrain alignment claims, and propose principles for theory-driven and comparative evaluation. Throughout, we argue that behavioral fit alone is insufficient. Alignment becomes scientifically meaningful only when embedded within explicit theoretical commitments, theory-diagnostic tasks, and systematic contrastive evaluation across candidate models.

---


### 410. [Distilling CT Foundation Models into Editable Concept Bottlenecks for Lung Nodule Malignancy Prediction](https://arxiv.org/abs/2608.07857)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Fakrul Islam Tushar, Stephen Adamo, Geoffrey D. Rubin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models provide transferable CT representations, but predictions based directly on these embeddings are difficult to interpret. We developed concept bottleneck models that map two frozen CT foundation-model representations to eight radiologist-defined pulmonary-nodule attributes and predict malignancy from the estimated concepts and nodule size. The models included CT-FM, a whole-CT self-supervised encoder using a 96^3-voxel nodule-centered patch, and FMCIB, a nodule-focused contrastive encoder using a 50-mm crop. Eight ridge-regression concept heads were trained on 2,610 LIDC-IDRI nodules. Malignancy models were trained on LUNA25 and evaluated on a held-out internal test set and the external DLCS cohort. Concept fidelity was assessed using five-fold cross-validated R^2, and malignancy discrimination was assessed using AUROC with 95% confidence intervals estimated by patient-grouped bootstrap resampling. Concept fidelity was modest but higher for FMCIB than CT-FM for subtlety (R2, 0.24 vs. 0.11), spiculation (0.17 vs. 0.08), texture (0.17 vs. 0.07), and lobulation (0.15 vs. 0.05). Internally, the CT-FM and FMCIB concept+size models achieved AUROCs of 0.86 (95% CI, 0.80-0.92) and 0.86 (0.79-0.92), respectively. Externally, AUROCs were 0.72 (0.68-0.75) and 0.73 (0.70-0.76), compared with 0.73 for nodule size alone and 0.60 and 0.67 for the corresponding embedding only probes. Additive predictions could be decomposed into feature-level contributions and modified through controlled concept interventions. Concept bottlenecks provided transparent malignancy predictions with discrimination similar to nodule size alone, while differences in concept fidelity suggest that concept recovery depends on the underlying foundation-model representation.

---


### 411. [REIN: Bridging the Gap between Reasoning and Reliability via Reflection and Abstention Alignment](https://arxiv.org/abs/2608.07931)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhengze Huang, Luyang Yu, Di Hong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large reasoning models (LRMs) are prone to hallucination, which undermines their reliability and poses challenges for safe deployment. Hallucinations in LRMs arise from two distinct failure sources: reasoning hallucination, where flawed inference steps propagate to an incorrect conclusion, and knowledge hallucination, where the model lacks the requisite factual knowledge to answer the query. To address reasoning hallucination, we propose REIN, an alignment framework that trains LRMs to produce a structured reasoning sequence, $\texttt{<think>} $$\rightarrow$ $\texttt{<reflection>} $$\rightarrow$ $\texttt{<answer>}$, enabling explicit self-reflection before committing to a final answer. To address knowledge hallucination, REIN introduces a reward mechanism that encourages explicit abstention (e.g., "I don't know") when none of the sampled reasoning chains yields a correct answer, allowing the model to refrain from unsupported predictions. Extensive evaluations on mathematical and commonsense reasoning benchmarks show that REIN consistently improves selective accuracy, reduces incorrect-but-self-endorsed responses, and maintains high coverage compared with competitive baselines. Notably, REIN achieves these gains within a single forward pass, without requiring process supervision, inference-time controllers, external search, or multi-round critiques. Experiments on multiple backbones show that REIN reduces the hallucination proxy by $58\sim72\%$ relative to the base models while maintaining $86\sim91\%$ average coverage, and improves selective accuracy on attempted questions by $6.6\sim14.2\%$.

---


### 412. [Ground-Truth Neighborhood Regularization for Reinforcement Learning Post-Training of Time Series Foundation Models](https://arxiv.org/abs/2608.08010)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jianqi Zhang, Xingyu Zhang, Zeen Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series forecasting (TSF) plays an important role in a wide range of real-world applications. Recently, time series foundation models (TSFMs), pretrained on large-scale datasets, have demonstrated strong generalization capabilities and emerged as an important paradigm for TSF. Reinforcement learning (RL) post-training has consequently attracted growing attention as a means of further improving their performance on downstream tasks. However, we find that, in certain forecast regions, RL post-training may gradually shift the output distributions of TSFMs away from the ground truth, thereby limiting their performance. We refer to this phenomenon as \textbf{suboptimal collapse}. Our analysis suggests that difficulty in initially sampling high-quality trajectories near the ground truth is an important contributing factor to suboptimal collapse. To address this issue, we propose Ground-Truth Neighborhood Regularization (GTN-R) for RL post-training of TSFMs. GTN-R uses the ground truth as a reference for locating high-quality regions and guides the model's probability mass toward the ground-truth neighborhood. This increases the probability of sampling high-quality trajectories, mitigates suboptimal collapse, and improves performance. Moreover, GTN-R can be flexibly integrated into various RL methods for TSFMs. Extensive experiments show its effectiveness.

---


### 413. [Thought-Level Beam Search for Reasoning](https://arxiv.org/abs/2608.08020)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Lijie Yang, Hongyin Luo, Tri Dao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-time compute scaling is a primary driver of performance in large reasoning models (LRMs), but extreme inefficiency bounds current approaches, shifting the critical question from \emph{how much} compute to spend, to \emph{where} to allocate it. We formalize test-time reasoning as a constrained compute allocation problem over partial trajectories. Under a fixed hardware budget, existing paradigms fail to actively allocate the compute to the most promising partial progress: traditional parallel sampling treats traces independently and induces severe memory bottlenecks, while subtractive pruning starves hardware and fails to actively and sufficiently shift the output distribution. To overcome this dichotomy, we introduce Gambit, an inference algorithm that executes \emph{thought-level beam search}. By periodically pruning unpromising trajectories and immediately branching from high-quality prefixes, Gambit dynamically concentrates compute onto the most promising reasoning traces via a light-weight scorer probing hidden states while maintaining continuous high hardware utilization. Extensive evaluations across multiple models and benchmarks demonstrate that Gambit strictly dominates existing baselines. Under identical hardware constraints, our method yields up to a +6.7\% absolute accuracy gain on HMMT-24 and +3.3\% on AIME-25 over pruning baselines, delivers $>2\times$ higher throughput on trace completion, and reduces total token consumption by up to 68.5\% relative to standard parallel sampling.

---


### 414. [EFFEKT: Efficient Federated Knowledge Transfer to Foundation Models](https://arxiv.org/abs/2608.08138)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Matteo Caligiuri, Francesco Barbato, Pietro Zanuttigh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent data protection laws have accelerated the adoption of Federated Learning (FL) for privacy-preserving decentralized training. Nevertheless, increasing model sizes impose substantial computational demands on client devices, limiting FL applicability in resource-constrained settings. We introduce a novel multi-domain federated learning framework in which lightweight client-side proxy models collaborate with a server-side Foundation Model (FM) to learn new concepts without sharing private data. Our approach, EFFEKT, enables efficient server-side training of domain-specific LoRA adapters while preserving feature-space alignment between the FM and proxy extractors via novel bi-directional cross-distillation strategies. Experiments on multiple real-world datasets and deployments on low-power edge devices demonstrate improvements over state-of-the-art baselines in most considered domains while maintaining lightweight computation at the client side.

---


### 415. [DoGMA: A Central-Dogma-Guided Foundation Model for Multi-Omics Alignment and Multi-Task Learning in Oncology](https://arxiv.org/abs/2608.08148)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Junfei Ling, Bangzheng Pu, Bingsen Xue 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attention mechanisms have been widely utilized in modern deep learning, and many existing multi-omics models inherit their conventional use to allow unrestricted bidirectional interactions. However, the fundamental logic of life is directional. Existing designs often overlook the directionality suggested by the central dogma, potentially limiting transfer across heterogeneous cancers, downstream tasks, and incomplete modality this http URL this work, we present DoGMA, a central-dogma-guided foundation model for pan-cancer multi-omics analysis, arguing that robust transfer requires representations with domain-specific inductive bias. Concretely, we build it on a Transformer-MoE architecture where directed attention biases inter-omics communication toward central-dogma information flow. We further pretrain our model with masked hierarchical omics reconstruction to guide it toward learning central-dogma-consistent interactions. Across diverse downstream tasks, including cancer representation learning, survival prediction, and metastasis prediction, DoGMA consistently demonstrates strong predictive performance. Ablations and analyses further suggest that the performance gains arise from the synergy between central-dogma-guided directed attention and reconstruction-based pretraining, which together promote more biologically consistent cross-omics information exchange. Overall, DoGMA demonstrates that domain-specific inductive biases can improve the robustness and transferability of multi-omics foundation models, offering new insights into the design of attention mechanisms for multi-omics representation learning.

---


### 416. [FemWear: A Specialized Wearable Foundation Model for Women's Health](https://arxiv.org/abs/2608.08244)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yifan Wang, Chenzhong Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> General wearable foundation models are pretrained across broad sensor streams and populations, but are not designed around women's-health tasks. We introduce FemWear, a specialized wearable foundation model that parameter-efficiently repurposes a pretrained multimodal wearable backbone. FemWear retains the patch projection and Transformer encoder, training 239,236 parameters (1.11% of a 21.54M-parameter encoder) through low-rank residual adapters and causal task-family heads. It learns one shared longitudinal representation for menstrual, symptom, affective, sleep/recovery, autonomic, activity, and pregnancy-related outcomes. We evaluate six cohorts with 63 comparable primary metrics, including 33 from women's-health cohorts, while retaining the 32-task OpenMHC ability-retention benchmark. On a fixed participant split over three seeds, FemWear improved cycle-phase macro-F1 by 8.15% and reduced mean absolute error for cramps, mood symptoms, and sleep problems by 9.32%, 5.80%, and 9.43%, respectively. In a stricter 42-participant nested leave-one-participant-out audit, 24-hour onset, 72-hour onset, and cramps retained positive changes of 2.87%, 6.35%, and 2.19%; phase, mood, and sleep were neutral or negative, and no endpoint had a strictly positive corrected confidence interval. Capacity-matched experiments outperformed a latest-day multilayer perceptron but not shared-GRU or multi-gate mixture-of-experts baselines. Train-only calibration reduced onset expected calibration error by 84.2--88.2% with zero temporal-nesting violations. FemWear enables targeted transfer and coherent probability outputs for women's-health research, but does not establish universal performance dominance or clinical validity.

---


### 417. [SuperLocalMemory 4.0: The Governed Memory Operating System for AI Agents](https://arxiv.org/abs/2608.08253)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Varun Pratap Bhardwaj, Garima Singh, Arun Pratap Bhardwaj  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are becoming shared infrastructure, yet durable memory is commonly assembled from separate retrieval, governance, and operational components. We present SuperLocalMemory 4.0, a governed, local-first memory operating system for AI agents. The system combines dense semantic, BM25 lexical, temporal, Hopfield-associative, and spreading-activation retrieval through reciprocal-rank fusion; a governed learning and behaviour layer; bi-temporal recall; multi-scope personal, shared, and global memory; role-based access control; GDPR-oriented export and verified erasure; audit trails; and a deployment-context EU AI Act checklist.
V4 introduces a reliability spine for its primary write path: generation-fenced admission, a policy registry, verifiable memory transactions with per-projection apply, verify, compensate, and erase owners, and hash-checkable completion manifests. The runtime is available through CLI, MCP, an HTTP daemon, a dashboard, editor integration, and framework adapters, and supports fully local, local-with-on-device-model, and provider-assisted modes.
We evaluate eleven fault-injection and mechanism scenarios, each repeated 200 times. The released evidence bundle reports 2,200 of 2,200 deterministic repetitions upholding their scoped component properties. The governed write envelope measured 3.522 ms at p50 and 5.297 ms at p99, versus 1.835 ms and 2.569 ms for the ungoverned baseline, corresponding to in-process control-plane overheads of 1.687 ms at p50 and 2.728 ms at p99. These are scoped component and mechanism measurements, not an end-to-end multi-process or external retrieval-accuracy benchmark. The paper consolidates prior SuperLocalMemory work on privacy-preserving multi-agent memory, information-geometric retrieval, and the V3.3 Living Brain lifecycle.

---


### 418. [A continually expandable foundation model for brain MRI](https://arxiv.org/abs/2608.08319)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Michail Mamalakis, Carmen Jimenez-Mesa, Yonghao Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Brain magnetic resonance imaging (MRI) is central to neuroscience and clinical assessment, but models are commonly developed for individual diseases, populations or imaging protocols. Foundation models promise more general representations, yet they are usually pretrained once and can lose earlier capabilities when updated with new data. Here we show that Alcmaeon, a three-dimensional brain MRI foundation model pretrained without manual labels on more than 425,000 volumes and derived imaging maps, can be expanded sequentially across clinical domains. Alcmaeon combines volumetric encoding and latent diffusion generation with Graph-Blueprint Pruning (GBP), which protects network modules important to earlier domains while leaving the remaining capacity trainable. Across expansion from healthy ageing and neurodegeneration to developmental, psychiatric and tumour imaging, GBP showed less forgetting than sequential adaptation and elastic weight consolidation across voxel-level reconstruction measures, with its largest advantage after adaptation to tumour imaging. The blueprints provided an inspectable record of how model capacity was protected and reused. Representations from different model levels supported image synthesis, disease classification, survival modelling and postoperative prediction, although no single representation was optimal for every task. These findings provide a route towards brain MRI foundation models that can grow with emerging data while retaining earlier capabilities.

---


### 419. [VOICE: A Vision-Omics Foundation Model Integrating Direct and Retrieval-Based Prediction of In-situ Single-Cell Gene Expression](https://arxiv.org/abs/2608.08366)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xin Luo, Yicheng Tao, Haoxuan Zeng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial transcriptomics can resolve gene expression at single-cell resolution, but it is costly, limited to targeted panels of a few hundred to a few thousand genes, and applicable to only a small number of samples. H&E imaging, by contrast, is cheap and collected routinely at scale. This makes predicting single-cell expression directly from morphology a practical way to bring molecular analysis to large tissue archives. We therefore present VOICE, a multimodal foundation model that predicts single-cell gene expression from H&E images using paired Xenium data. VOICE first aligns cell centered H&E morphology from a pathology foundation model with single-cell expression embeddings from a transcriptome foundation model, trained using contrastive learning over 23 million cells. Next it predicts expression through two branches. One branch directly regresses expression from morphology. The other branch retrieves measured expression from similar reference cells, recovering genes that do not have morphological signal. Because genes vary in morphological predictability, VOICE fuses the two branches with a per-gene weight. After training, VOICE generalizes to heldout patients, slides, and partially overlapping gene panels from Xenium, and it consistently outperforms prior single-cell expression prediction methods on seven metrics.

---


### 420. [Aero Realtime: Fully Aligned Input-Output Streams for Low-Latency Streaming Multimodal Generation](https://arxiv.org/abs/2608.08469)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Kaichen Zhang, Wei Huang, Keming Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing streaming multimodal models process observations incrementally but still follow a turn-based prefill-then-decode pattern, making them non-duplex: new observations cannot naturally enter an active generation stream. Proactive alternatives use micro-turn polling or external response gates, which fragment continuous interaction, decouple response timing from language generation, and complicate KV-cache-friendly serving. We introduce Aero Realtime, a 4B streaming multimodal model with a duplex architecture for realtime generation. Aero Realtime aligns video, audio, and textual output on a shared temporal grid, where each approximately 80-ms audio slot predicts either a lexical token or a silence token. This allows input and output to advance together, enabling one autoregressive objective to learn both when to respond and what to generate. During inference, Aero Realtime appends only the newest multimodal slot, carries forward the previous output state, and reuses the KV cache for efficient incremental execution. We further provide a complete training and serving recipe, including realtime QA construction, slot-aligned supervision, hardware-aware distributed training, and resumable inference. On four NVIDIA A6000 workstation GPUs, Aero Realtime maintains 84-ms median and 173-ms P95 processing lag over 20 minutes of a continuously streamed video, remaining within 200~ms of the source timeline. These results demonstrate the feasibility of fully aligned input-output modeling for duplex, proactive, and hardware-aligned multimodal interaction.

---


### 421. [PAST: Privileged Adaptation from Complete Student Trajectories for On-Policy Self-Distillation](https://arxiv.org/abs/2608.08726)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yangyang Feng, Zhuoyan Feng, Junlan Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) uses a privileged teacher to supervise a reasoning model on prefixes sampled from its own rollouts. Yet each rollout also reveals how the student's response unfolds and whether it succeeds, student-specific hindsight that standard OPSD does not use to form the teacher. We introduce Privileged Adaptation from Student Trajectories (PAST), which treats each completed student trajectory as additional privileged information for the OPSD teacher while leaving the student's distillation prefixes unchanged. PAST preserves the student's next-token distribution on correct trajectories and uses failed trajectories to adapt the teacher toward verified success under student-proximity regularization. We characterize what such a trajectory-conditioned teacher can transfer to a prefix-only student. Forward-KL distillation projects the teacher distributions to their conditional arithmetic mean given the prefix. This projection separates trajectory-specific variation that remains privileged from the mean policy shift available to the student. For correct trajectories, the unclipped population objective also has the frozen student as an ideal distributional fixed point. Across three mathematical reasoning benchmarks, PAST improves the Avg@12 macro average over Vanilla OPSD by 5.6 percentage points. A $2\times2$ factorial study shows gains from both complete-trajectory access and teacher adaptation, while trajectory removal and shuffling confirm that the adapted teacher uses the matching hindsight context.

---


### 422. [AnchorFold: A Focus-Then-Fold Framework via Recursive Attention Propagation for Efficient Multi-Vector Visual Document Retrieval](https://arxiv.org/abs/2608.08732)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Haoyu Zuo, Yibo Yan, Xin Zou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-vector vision-language retrievers enable fine-grained Visual Document Retrieval (VDR) through late interaction, but storing and scoring hundreds of visual patch embeddings per page incurs substantial overhead. Existing training-free methods rely on pruning or merging: pruning degrades sharply under aggressive compression, whereas merging does not explicitly prioritize important regions when forming representatives. We introduce AnchorFold, a training-free focus-then-fold framework for document-side index compression. AnchorFold applies Recursive Attention Propagation over visual self-attention graphs, performing multi-step propagation within each attention head and integrating scores across heads and layers. The focus stage selects the highest-centrality tokens as anchors. The fold stage assigns remaining tokens to their most similar anchors in the normalized retrieval space and summarizes each anchor-centered group through centrality-weighted aggregation. This preserves non-anchor contributions while concentrating capacity on structurally important tokens. Across ViDoRe v1/v2 and REAL-MM-RAG with three diverse retrieval backbones, AnchorFold consistently outperforms all evaluated training-free baselines at $\gamma \leq 0.20$. On ViDoRe v1/v2, it retains 98.3% of full-index NDCG@5 on average at $5\times$ compression, achieving near-lossless compression, and 92.4% at $20\times$ compression.

---


### 423. [Hybrid Neural-Classical Correction for Frozen Time Series Foundation Models: A Comprehensive Ablation Study on High-Frequency Stock Prediction](https://arxiv.org/abs/2608.08825)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Kasun Dewage, Suranadi De Silva, Shankhadeep Mondal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models for time series forecasting demonstrate impressive zero-shot generalization but often underperform on specialized domains such as high-frequency finance. We present a comprehensive study of hybrid neural-classical correction for adapting frozen TimesFM (200M parameters) to stock return prediction during the volatile opening trading hour. We compare two neural correction architectures - AttnCorrect (multi-head self-attention, approximately 471K parameters) and GatedLinear (low-rank bilinear projection with gating, approximately 49K parameters) - each augmented with Random Forest residual learning. Through systematic ablation across 10 major technology stocks (NVDA, MSFT, AAPL, GOOG, GOOGL, AMZN, META, AVGO, TSLA, NFLX) spanning 2 million data points, we reveal critical insights: (1) The hybrid neural-classical approach achieves 0.597 pooled correlation and 6.4x mean per-day correlation improvement over frozen TimesFM; (2) Classical residual learning (Random Forest) provides the largest single-component contribution, matching or exceeding the neural correction component; (3) Simpler neural architectures surprisingly outperform complex ones when classical residual learning is removed; (4) Self-attention provides the largest neural-only contribution. GatedLinear+RF achieves best overall performance with 9x fewer neural parameters than AttnCorrect+RF. We report three complementary correlation metrics - mean per-day, cross-day cumulative, and pooled - to provide a complete picture of predictive quality. Our results provide practical guidance: effective foundation model adaptation requires careful integration of neural and classical components, with classical methods playing a crucial complementary role.

---


### 424. [Damage Classification for 3D Point Cloud Data via 3D Data Analysis and Vision Foundation Model-based 2D Projections](https://arxiv.org/abs/2608.08955)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Evan Perez, Kalelo Dukuray, Erika Ardiles-Cruz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained damage classification of 3D point cloud data (PCD) remains a persistent challenge, constrained by high computational demands and limited labeled data. This study examines two methods: 3D PCD-based damage assessment (3PDA) algorithm and 2D projection damage assessment (2PDA) In our 3PDA analysis algorithm, TDA is used to derive compact representations of 3D PCD segmented by pointNet, which are then integrated with anomaly detection algorithms to quantify structural degradation. We show that TDA effectively compresses geometric structure from VFM-segmented components into discriminative feature vectors and that anomaly detection models can reliably distinguish components with varying damage severity using only 3D PCD inputs. In the 2D projection analysis algorithm, we leverage large VFMs for granular damage detection by projecting 3D PCD into 2D views. These projections allow VFM based models to achieve competitive classification performance while requiring only a fraction of the computational cost associated with full 3D data processing. Our results demonstrate that 2D VFM pipelines in 2PDA can perform strongly on fine-grained damage classification tasks, highlighting their viability as lightweight, resource-efficient alternatives to traditional 3PDA architectures. Comparative evaluation shows that the 3PDA attains higher accuracy but only for a narrow subset of object geometries and at substantially higher computational cost due to its reliance on TDA and the scarcity of high-fidelity 3D datasets. In contrast, the 2PDA algorithm yields slightly lower accuracy but offers an order of magnitude reduction in time complexity and generalizes across a far broader range of object categories.

---


### 425. [How Far Do Foundation Models Transfer to Infant Signals? A Cross-Dataset Transfer Audit with a Unified Need Ontology](https://arxiv.org/abs/2608.08989)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Wu Hangyu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Public infant cry corpora are small, label-incompatible, and almost always evaluated one corpus at a time. We ask what this practice hides and what fixes it. Across four cry corpora screened by a multi-level leakage audit (byte-level and embedding-level deduplication plus a within-corpus train-test near-duplicate audit), we probe four frozen encoders and a handcrafted baseline under a unified five-class need ontology and shared task formulations. The audit exposes what single-corpus evaluation conceals: within-domain macro-F1 swings by 0.57-0.80 for the same encoder, cross-corpus transfer is negative on average (negative-transfer ratio 0.19-0.35, significant in 18 of 30 directed cells, BH-FDR), and 349 content-identical clip groups carry conflicting metadata labels across corpus distributions. The same audit, however, reveals a consistent way forward. Transfer into the noisiest corpus is consistently positive in effect size at matched training size and after near-duplicate removal, offering a practical recipe for small, noisy corpora. Frozen probes saturate at modest label budgets, while stabilized fine-tuning wins with full labels; domain-adaptive pretraining significantly beats stabilized fine-tuning at 5-10-shot (the 1-shot advantage is not robust to optimization-seed variance) but shows no significant advantage at 50-shot or beyond. In the tested binary, shared-label settings, ontology-mapped joint training wins in all four encoder-by-target combinations, whereas naively merging unmapped labels costs up to 37 F1 points. We release the ontology, mapping code, and audit pipeline, turning incompatible cry corpora into a usable joint-training resource.

---


### 426. [Triple Expert Learning from Noisy Labels for Semi-Supervised Vision Foundation Model Adaptation](https://arxiv.org/abs/2608.09052)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xuanyu Liu, Zheng Fang, Hongyang He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semi-supervised adaptation of vision foundation models (VFMs) commonly freezes the pretrained backbone and updates lightweight modules such as LoRA. However, pseudo-labels have mixed reliability, and a single LoRA adapter must absorb reliable, ambiguous, and noisy gradients in the same low-rank space. This can make VFM adaptation sensitive to pseudo-label noise. We propose \textbf{TriNoL}, a \textbf{Tri}ple-expert learning framework from \textbf{No}isy \textbf{L}abels for semi-supervised VFM adaptation. TriNoL routes unlabeled samples into three confidence regions and assigns them to three LoRA experts: a Positive Expert for high-confidence pseudo-labels, an Alignment Expert for medium-confidence ambiguous samples, and a Negative Expert for low-confidence noisy samples. The VFM backbone remains frozen, and only the LoRA experts and classifier head are updated. By separating different pseudo-label reliability regions into specialized adaptation paths, TriNoL improves robustness to noisy supervision while keeping the training cost low.

---


### 427. [CodecArena: Codec Quality Assessment via Visual Reinforcement Learning](https://arxiv.org/abs/2608.09139)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jiaye Fu, Weiqi Li, Qiankun Gao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video coding is advancing into the low and ultra-low bitrate regime, driven by end-to-end codecs that replace the hand-crafted pipeline with jointly optimized neural networks and generative codecs that exploit the priors of video generation models. Yet the dominant metrics, LPIPS and DISTS, measure feature and texture similarity rather than content fidelity: a reconstruction that hallucinates a wrong face or blurs text into convincing strokes can still score well, even when a human rejects it instantly. To address this, we propose CodecArena, the first vision-language framework for video coding quality assessment, casting codec evaluation as source-conditioned comparative reasoning between a reference and its reconstructions. We optimize CodecArena with Facet-GRPO, a visual reinforcement learning scheme that aligns pairwise codec preferences while grounding the verdict in five fidelity facets: identity, objects, text, texture, and temporal consistency. Its facet-anchored reward uses automatically derived facet directions as weak anchors, rather than human per-facet labels, to prevent any single sub-score from dominating the holistic preference and to yield interpretable fine-grained quality judgments. To support training and evaluation in this underexplored regime, we construct two complementary resources: CodecArena-1K, a fully automatic preference dataset of 1,500 comparison groups built from traditional, neural, and generative codec reconstructions with fused vision-language and objective supervision; and CodecArena-Bench, a human-ranked benchmark with source-disjoint videos for fair out-of-domain evaluation. Extensive experiments demonstrate that CodecArena achieves state-of-the-art agreement with human judgments on source-disjoint content across diverse codecs and bitrates, surpassing perceptual metrics and prior vision-language evaluators.

---


### 428. [RAGMesh with FaME-G2E: Long-Form Text-Driven 3D Face Generation and Editing](https://arxiv.org/abs/2608.09186)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hao Li, Ju Dai, Feng Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-driven 3D face generation and editing remains challenging due to the difficulty of translating long-form descriptions into fine-grained facial geometry. Existing methods primarily align global textual semantics with facial structures but often struggle to capture subtle local deformations, such as eyebrow tension, cheek contraction, and asymmetric mouth motions, resulting in limited geometric fidelity and editing precision. To facilitate fine-grained text-driven facial modeling, we first construct FaME-G2E, a large-scale multimodal dataset containing detailed text--mesh annotations and paired text--blendshape samples for unified 3D facial generation and editing. Based on this dataset, we propose RAGMesh, a retrieval-augmented framework that leverages text-correlated geometric priors to improve high-fidelity facial synthesis and editing. Specifically, the Multi-Scale Retrieval Fusion (MSRF) module retrieves semantically consistent global and regional facial priors and fuses them in the blendshape space, suppressing conflicting local deformations while preserving coherent deformation patterns. Furthermore, we introduce Adaptive RAG-guided Supervision (AdaRAGS), a region-aware constraint that explicitly aligns textual semantics with corresponding facial regions, enhancing regional controllability and editing accuracy. Extensive experiments on FaME-G2E demonstrate that RAGMesh achieves superior performance over state-of-the-art methods in local geometric accuracy, text-guided controllability, regional editing precision, and inference efficiency. Video demo is available at this https URL, and the source code and dataset will be released upon paper acceptance.

---


### 429. [SoftmaxGRPO: Learning to Reason using Softmax Advantage Group Estimation](https://arxiv.org/abs/2608.09271)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jefferson Hernandez, Jaywon Koo, Zilin Xiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group-based reinforcement learning objectives such as GRPO can allocate learning signal poorly across prompt difficulty: under binary rewards, group normalization induces a divergent weighting on easy prompts. We introduce Softmax Advantage Group Estimation (SoftmaxGRPO), a drop-in alternative that replaces z-score-normalized group advantages with temperature-scaled softmax advantages, keeping weights bounded regardless of prompt difficulty. For binary rewards, we derive the exact finite-group population objective and identify MaxRL as its low-temperature limit. For bounded scalar rewards, we show that the large-group update exactly optimizes a log-moment-generating-function objective, while a universal finite-group scalar objective cannot exist without additional assumptions on the reward distribution. Empirically, SoftmaxGRPO reallocates measured gradient budget away from near-solved prompts and consistently improves over GRPO under identical rewards. It reaches 51.8% on DeepMath with verifiable rewards and improves a 1.5B instruction-tuned model from 35.0% to 68.0% on Poetry using only lightweight text-similarity rewards.

---


### 430. [GeoPhysAdapter: Scale-Matched Geophysical Adaptation for Cross-Domain Landslide Mapping with Vision Foundation Models](https://arxiv.org/abs/2608.09325)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhihang Liu, Mei-Po Kwan, Jinlin Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Newly triggered landslides rarely carry immediate annotations, so cross-domain transferability determines the value of landslide mapping for emergency response and regional risk assessment. Vision foundation models have strengthened representational transfer, yet on unseen regions, events, and data sources they still generate high-confidence false alarms. Terrain, material, and rainfall triggering can constrain such errors, but their supports are local, regional, and event-scale, so that resampling onto a 10~m grid misaligns them with the segmentation decision unit and compounds the uncertain geographic context problem (UGCoP). We propose GeoPhysAdapter, which anchors on a frozen vision foundation model, restricts terrain, material, and triggering to dense spatial guidance, regional modulation, and event-timing forcing, and applies bounded adaptation at two decision units, the pixel and the candidate landslide body, reverting exactly to the visual prediction where support is insufficient. On an event-isolated PILD dataset of four public sources, 55 global landslide events, and 7,890 test samples, 70.3% of cross-domain false-positive mass lies in near-pure spurious bodies of median equivalent diameter 207m, matching coarse-prior support rather than the pixel. Pixel-level adaptation removes a net 507,817 erroneous pixels and reduces error by 7.76%, whereas raising the decision unit to the candidate body, under identical samples, anchor, and baseline, increases error reduction to 23.99%, approximately 3.1 times the pixel-level effect, improves IoU by 0.031 (14.2% relative), and corrects 9.92 pixels per pixel harmed. The data and code are publicly available at: this https URL.

---


### 431. [Foundation Models are Implicit Deepfake Detectors](https://arxiv.org/abs/2608.09427)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Stefan Smeu, Dragos-Alexandru Boldisor, Elisabeta Oneata 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained self-supervised representations have emerged as a core component of current deepfake detection methods, yet it remains unclear which of their properties make real and fake media distinguishable. In this work, we uncover a surprisingly consistent phenomenon: across multiple pretrained models, datasets, and both image and video domains, fake samples systematically produce lower-magnitude representations than their real counterparts. Motivated by this finding, we formulate deepfake detection as an anomaly detection problem and show that simple statistics of feature magnitude achieve competitive performance with far more sophisticated deepfake detection methods. We further investigate the origin of this effect and demonstrate that reduced feature magnitude is primarily associated with semantic shifts introduced by fake content, while low-level generative fingerprints play a comparatively smaller role. Finally, we show that this discriminative signal strengthens as the size of the underlying foundation model grows, suggesting that advances in representation learning naturally translate into stronger zero-shot deepfake detectors.

---


### 432. [MixFormer: Linear Transformer with Mixture of Memory Experts](https://arxiv.org/abs/2608.09468)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yu Guo, Lei Duan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State Space Models (SSMs), as a mainstream research direction of linear Transformers, aim to achieve higher efficiency than standard Transformers in long-context modeling. However, existing SSMs suffer from limited input adaptivity and constrained memory capacity, leading to information loss when modeling ultra-long sequences. To address these limitations, we propose MixFormer, a novel linear Transformer that integrates a Mixture-of-Memory-Experts (MoE) mechanism. Specifically, the model maintains differentiated memory states through multiple collaborating memory experts and employs a novel Time-Aware Linear Attention (TALA) mechanism, which leverages learnable exponential decay functions and positional biases to dynamically update memory. This design enables the model to selectively reinforce important historical information while effectively mitigating memory dilution, substantially improving long-range dependency modeling. Experiments on long-sequence text and image generation tasks demonstrate that MixFormer not only achieves significant performance gains but also provides a more sustainable computational backbone for the next generation of web infrastructure.

---


### 433. [Dual-Adversarial Safety Alignment: Cultivating Intrinsic Threat Comprehension in LRMs](https://arxiv.org/abs/2608.09542)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hongli Shen, Shaopeng Fu, Qinbo Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large reasoning models (LRMs) achieve remarkable success on complex tasks but remain vulnerable to harmful prompts that induce unsafe outputs. Recent methods align LRMs using direct refusals or safety rationales, yet often focus on prompt patterns rather than intrinsic attack mechanisms. As a result, these pattern-centric alignments struggle to generalize across diverse jailbreaks, compromising adversarial robustness and reasoning utility. We propose AdvSafe, a dual-adversarial framework that enables LRMs to internalize unsafety knowledge by explicitly deconstructing adversarial mechanisms. This moves beyond pattern-dependent traces, fostering robust cognitive defense without compromising reasoning utility. Our pipeline operates via a two-phase adversarial game. First, in adversarial synthesis, an autonomous agent dynamically crafts deceptive jailbreak prompts, adapting its strategies to breach a strong teacher model. Second, in adversarial extraction, the breached teacher executes a cognitive counter-attack. For every successful jailbreak, the teacher unmasks the camouflage, explaining why the attack succeeds and how such prompts can be identified and mitigated. This dual-adversarial process yields a compact reasoning dataset capturing rich, generalizable unsafety knowledge. Student models trained on this dataset implicitly acquire safety alignment through intrinsic threat comprehension. Experiments show that with only 1K synthesized samples, AdvSafe-aligned LRMs achieve significantly stronger jailbreak robustness than existing baselines, with almost no utility degradation. Furthermore, AdvSafe improves robustness against out-of-distribution prompts, demonstrating that learning unsafety knowledge enables a superior robustness-utility trade-off and generalizes beyond seen attack patterns.

---


### 434. [PressureMesh: 3D Human Mesh Estimation from Multi-Device Pressure Images](https://arxiv.org/abs/2608.09550)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Changhai Ma, Ziyu Wu, Yunkang Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human pose monitoring is crucial in fields such as rehabilitation assessment and human-computer interaction. Due to its privacy-preserving nature, pressure-based human pose monitoring has become a primary approach for unobtrusive sensing. However, existing methods are generally limited to a single device, which restricts the effective monitoring range. To address this limitation, we propose MDP-Net, an end-to-end network capable of directly estimating human meshes from temporal pressure data across multiple devices. We introduce a multimodal fusion mechanism inspired by the Mixture of Experts (MoE) framework to achieve effective complementarity and enhancement of cross-device pressure information. To support the training and evaluation of MDP-Net, we constructed MDP, a high-quality multi-device temporal pressure dataset that includes various pose labels such as 2D/3D joints and human meshes. Experimental results demonstrate that MDP-Net achieves a joint position error of 12.6 cm on the MDP dataset. These results prove that fusing multi-device pressure information is an effective and promising new solution for daily human pose monitoring.

---


### 435. [LoRA-based Adaptation Alone Is Not Enough: Understanding the Limits of Foundation Models for Face Presentation Attack Detection](https://arxiv.org/abs/2608.09633)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Peter Lorenz, Anjith George, Marcel Sébastien  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face presentation attack detection (PAD) aims to reliably detect a wide range of presentation attacks. While PAD methods achieve strong performance within individual datasets, their performance degrades under cross-dataset evaluation. Variations in sensors or lighting conditions can reduce the effectiveness of detectors from near-perfect to nearly random. Foundation models (FMs) have emerged as a promising alternative because typical PAD datasets, such as the MCIO benchmarks (MSU-MFSD, CASIA-FASD, Replay-Attack, and OULU-NPU), are small relative to the scale used for web-based pretraining. However, existing PAD systems primarily focus on CLIP-based foundation models, while overlooking other FMs with different architectures and training procedures. This study addresses this question by systematically evaluating 32 FMs. Zero-shot prompting achieves performance near chance across model families and scales. The vision encoders, when low-rankadapted (LoRA) with fewer than 1% trainable weights, achieve below 2% intra-dataset ACER in most cases, while cross-dataset ACER is substantially higher. LoRA primarily refines the decision boundary within a dataset, suggesting that pretrained representations and the adaptation dataset play a larger role in cross-dataset generalization than the evaluated lightweight adaptation strategy.

---


### 436. [LookAgain: Closed-Loop GUI Grounding with Visually Grounded Reflection](https://arxiv.org/abs/2608.09723)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Renshan Zhang, Haoyang Meng, Yixiao He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent graphical user interface (GUI) grounders have significantly advanced single-shot accuracy on standard benchmarks, yet their performance degrades sharply on small targets, densely packed controls and out-of-distribution interfaces. We attribute this gap to a paradigmatic limitation shared by existing approaches: none of them treats a produced coordinate as a hypothesis to be reflected upon and revised under new visual evidence. This manifests as three coupled issues: 1) Lack of post-hoc reflection. The prediction is frozen at the moment of emission, leaving no internal mechanism to challenge or refine it. 2) Visual evidence decoupled from the prediction. The auxiliary visual evidence is gathered to support the upcoming coordinate rather than to scrutinise the one already committed to. 3) Refinement over views, not over predictions. The iterative zoom-in refines the inspected region instead of inheriting a previous coordinate as a spatial prior to be corrected. In this paper, we propose LookAgain, a closed-loop GUI grounder driven by post-prediction visual reflection. LookAgain reformulates grounding as a multi-turn predict-look-again-refine process with two primitives: "locate" posts a coordinate hypothesis, renders a marker on the image and appends a local patch of the predicted region. It anchors the next reasoning step to the previous prediction as a spatial prior; "confirm" accepts or reject the hypothesis and terminates the procedure. We train the LookAgain grounder with SFT on constructed reflective trajectories as a cold start, followed by GRPO with terminal grounding correctness as the sole reward. Extensive experiments show that LookAgain consistently improves performance on both refusal-aware and general GUI grounding benchmarks, achieving state-of-the-art results. Comprehensive ablations further verify the effectiveness of the proposed framework.

---


### 437. [Disentangling Co-Occurring Retinal Pathologies with Saliency-Guided Sparse Expert Routing](https://arxiv.org/abs/2608.09752)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Nagur Shareef Shaik, Jeongwoo Park, Yeong-Jin Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retinal fundus images frequently exhibit multiple co-occurring pathologies, yet standard deep learning classifiers apply static, identical computation to every image regardless of the underlying disease distribution. We propose a novel architecture that resolves this via sparse conditional computation, pairing a Guided Context Gating (GCG) spatial attention front-end with a sparsely-routed Mixture-of-Experts (MoE) block operating over feature tokens. Crucially, this routing yields an interpretable, data-driven decomposition. Expert allocation is significantly disease-dependent (p < 0.001), with the healthy Normal state and morphologically distinct pathologies (e.g., ERM, AMD) isolating to dedicated experts. On a five-class, patient-disjoint 5-fold cross-validation benchmark, our model achieves 0.912 +/- 0.008 macro AUC and 0.653 +/- 0.014 macro F1. Furthermore, Grad-CAM++ and post-MoE t-SNE visualizations confirm that expert routing aligns with localized lesions and geometrically maps co-occurring cases between their constituent clusters, positioning sparse MoE as an interpretable approach to multi-disease retinal screening.

---


### 438. [CEAA: A Cognitive Embodied Agents Architecture for Interactive Computing Systems](https://arxiv.org/abs/2608.09848)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Aimilios Hadjiliasi, Louis Nisiotis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The development of embodied Intelligent Virtual Agents (IVAs) that have cognitive capabilities in real-time interactive virtual environments remains a challenge, even with today's advancements in technology. Existing architectures are often focused on either the implementation of low-level reactive control systems that are constrained by commercial game engines, or high-level representations of reasoning models that can be difficult to implement in virtual worlds. This paper builds on that notion and proposes a modular cognitive architecture for deploying embodied IVAs. This architecture builds on existing, pre-established frameworks such as the Sense-Think-Act paradigm and the Belief-Desire-Intention cognitive model, among others, and aims to provide a reusable implementation-oriented framework as a template for deploying IVA "brains" in interactive 3D computing systems. The proposed architecture contributes by providing a modular, implementation-oriented framework for the deployment of embodied, cognitive-capable IVAs and bridges the gap between high-level agent reasoning models with real-time embodied execution, for scalable, adaptive, and explainable agents in complex interactive virtual environments.

---


> [!TIP]
> 当前位于：**401-438**（第 9/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-438**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
