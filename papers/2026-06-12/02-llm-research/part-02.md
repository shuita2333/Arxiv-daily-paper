# 🧠 大模型相关研究 | 2026年06月12日

> 本类共 **128** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-128](./part-03.md)

---

### 51. [Multi-Agent Reasoning with Adaptive Worker Allocation for Stance Detection](https://arxiv.org/abs/2606.11609)

**<font color=#1a73e8>作者：</font>** Meysam Sabbaghan, Arman Zareian Jahromi, Doina Caragea  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Stance detection requires identifying an author's position toward a target, often from short-form texts where stance is implicit, indirect, or rhetorically framed. Although large language models (LLMs) achieve strong performance on this task, single-pass prompting can be brittle when multiple interpretations are plausible. Existing aggregation strategies, such as majority voting or self-consistency, improve robustness by combining labels, but they discard the intermediate reasoning needed to resolve conflicting interpretations.
We introduce a multi-agent reasoning framework with adaptive worker allocation for stance detection that shifts aggregation from label-level voting to reasoning-level synthesis. The framework employs a Manager-Worker architecture in which a Manager adaptively allocates a variable number of Worker agents based on input complexity. Each Worker analyzes the input from a distinct perspective and produces a reasoning-only explanation without emitting a stance label; the Manager then synthesizes these explanations to produce the final prediction.
We evaluate the proposed framework on SemEval-2016, P-Stance, and COVID-19 Stance using Llama, Mistral, and Gemini. Results show that the framework yields the largest gains on implicit and context-dependent stance cases, achieving 86.07 Macro-F1 on COVID-19 and 82.90 on SemEval-2016, while remaining competitive on more explicit stance datasets such as P-Stance. These findings suggest that adaptive reasoning-level aggregation is most beneficial when stance cannot be reliably inferred from surface cues alone.

---


### 52. [Information-Theoretic Decomposition for Multimodal Interaction Learning](https://arxiv.org/abs/2606.11614)

**<font color=#1a73e8>作者：</font>** Zequn Yang, Yake Wei, Haotian Ni 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal learning hinges on capturing redundant, unique, and synergistic information across modalities, which collectively constitute multimodal interactions. A critical yet underexplored challenge is that these implicit interactions vary dynamically across samples. In this work, we present the first systematic, information-theoretic analysis highlighting why learning these dynamic, sample-specific interactions is critical for effective multimodal learning. Our analysis further reveals deficits in conventional paradigms at learning these distinct interaction types: modality ensemble approaches struggle to capture synergy, while joint learning paradigms often under-utilize redundant information. This highlights the need for an approach that can adaptively learn from different interaction types on a per-sample basis. To this end, we propose Decomposition-based Multimodal Interaction Learning (DMIL), a novel paradigm that explicitly models and learns from sample-specific interactions. First, we design a variational decomposition architecture to isolate the constituent interaction components. Second, we employ a new learning strategy that leverages these explicit interaction components in a fine-tuning process to achieve comprehensive interaction learning. Extensive experiments across diverse tasks and architectures demonstrate that DMIL consistently achieves superior performance by adapting to holistic sample-specific interactions. Our framework is flexible and broadly applicable, establishing an interaction-centric paradigm for multimodal learning. The code is available at this https URL.

---


### 53. [TimeRouter: Efficient and Adaptive Routing of Time-Series Foundation Models](https://arxiv.org/abs/2606.11625)

**<font color=#1a73e8>作者：</font>** Kanghui Ning, Yushan Jiang, Kashif Rasul 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series foundation models (TSFMs) are increasingly explored as predictive experts within emerging agentic time-series systems. However, TSFMs exhibit heterogeneous inductive biases, and no single model consistently dominates across forecasting regimes, making expert selection a critical challenge. Existing systems often delegate this decision to LLM-based controllers, incurring substantial inference overhead. We present TimeRouter, an efficient routing framework that leverages empirical complementarity across a pool of pretrained TSFMs through lightweight discriminative routing, selective gating, and ensemble fallback. Concretely, TimeRouter combines a learned routing head, a selective gate, and an ensemble fallback, enabling adaptive expert selection without invoking an LLM at inference time. TimeRouter achieves state-of-the-art performance on the GIFT-EVAL leaderboard, with an LB MASE of 0.6765. Beyond benchmark performance, our ablation studies provide empirical insights into TSFM routing design, highlighting the importance of pool composition and selective gating. Taken together, these results position TimeRouter as a modular and lightweight routing layer for future agentic time-series systems built upon foundation-model pools. Our code is available at this https URL.

---


### 54. [Adapting Vision-Language Models from Iconic to Inclusive for Multi-Label Recognition Without Labels](https://arxiv.org/abs/2606.11626)

**<font color=#1a73e8>作者：</font>** Cheng Chen, Jingyu Zhou, Yifan Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding multi-label images remains a challenging task in computer vision. With the rapid progress of vision-language multimodal learning, vision-language models (VLMs) enable zero-shot recognition without labeled data. However, due to their intrinsic design, these models often prioritize the most iconic object and omit other contextual positives. This intrinsic bias conflicts with the nature of multi-label learning, thereby limiting their applicability. In this work, we propose an unsupervised framework that adapts VLMs from iconic recognition toward inclusive understanding, enabling label-free multi-label image recognition. Our approach consists of two key stages, ``cutting'' and ``sewing'': In the cutting stage, we present the multi-sampling response estimator to prevent the model from concentrating only on one single object. In the second sewing stage, the multi-object blend adaptation is introduced to adjust the labels to better conform to the multi-label distribution while preserving the intrinsic characteristics of the original model within only one epoch. Extensive experiments show that our framework significantly outperforms existing unsupervised approaches on four public datasets, even surpassing several representative weakly supervised baselines. These results demonstrate the potential of adapting pre-trained VLMs for more comprehensive visual understanding without manual annotations. Our code is publicly available at this https URL.

---


### 55. [Architecture-Aware Reinforcement Learning Makes Sliding-Window Attention Competitive in Math Reasoning](https://arxiv.org/abs/2606.11634)

**<font color=#1a73e8>作者：</font>** Kai Liu, Peijie Dong, Xinchen Xie 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid progress of reasoning and agentic large language models (LLMs) has increased the demand for long-context inference, but self-attention (SA) scales quadratically with context length.
To address this, we study SWARR (Sliding-Window Attention with Reinforced Adaptation for Math Reasoning), a practical recipe for adapting SWA models to mathematical reasoning. SWARR has two stages: (1) efficient conversion from a pretrained SA model to SWA with supervised fine-tuning (SFT), which avoids pretraining a new base model, and (2) policy adaptation with reinforcement learning (RL).
We find that SWA still underperforms SA after SFT, and we hypothesize that this gap is caused in part by a data-architecture mismatch: most SFT data are prepared for SA models and may contain long-range dependencies that are difficult for SWA to model. Because on-policy RL optimizes self-generated trajectories under the SWA constraint, it can adapt trajectories to better match SWA.
Experiments on mathematical reasoning benchmarks show that this recipe substantially narrows the gap between SWA and SA, recovering much of the accuracy lost during SWA conversion while preserving the efficiency benefits of linear-complexity attention. Our central contribution is the empirical finding that RL changes the conclusion one would draw from conversion and SFT alone about SWA's viability for math reasoning.

---


### 56. [TAROT: Task-Adaptive Refinement of LLM-prior Graphs for Few-shot Tabular Learning](https://arxiv.org/abs/2606.11640)

**<font color=#1a73e8>作者：</font>** Ruxue Shi, Yili Wang, Mengnan Du 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Few-shot tabular learning provides a cost-effective approach for real-world applications where annotation is costly and collecting sufficient samples for new tasks is difficult. Existing Traditional and LLM-based methods have demonstrated effectiveness in few-shot scenarios. However, traditional methods need additional training on unlabeled or generated data, which incur significant computational overhead. In addition, LLM-based methods that directly feed raw tabular data into LLMs raise privacy and compliance concerns. More importantly, both paradigms largely overlook the semantic relationships between features, which provide structural and semantic prior for constructing a semantic graph. Semantic graph is essential for modeling meaningful feature interactions in few-shot scenarios. In this paper, we propose TAROT, a GNN-based framework that encodes the structural and semantic prior by constructing and refining a task-adaptive semantic graph from this prior, thereby improving predictive performance in few-shot tabular learning. TAROT first encodes heterogeneous tabular data into unified node semantic representations via a Unified Semantic Tabular Node Encoder (USTNE). Then, it prompts LLMs to infer the semantic relationship between features based on the task description and feature names to construct a semantic graph. To mitigate structural noise introduced by the hallucination of LLMs, TAROT introduces Task-adaptive Semantic Graph Refinement that prunes spurious or task-unrelated edges and adds missing task-related ones, aligning the graph structure with the downstream objective. Finally, a GNN performs message passing over the refined graph to capture task-related semantic dependencies for prediction. Extensive experiments on various few-shot tabular learning benchmarks demonstrate the superior performance of TAROT, establishing it as a state-of-the-art approach in this domain.

---


### 57. [Improving Cross-Format Robustness in Language Models with Multi-Format Training](https://arxiv.org/abs/2606.11643)

**<font color=#1a73e8>作者：</font>** June M. Liu, Shaomian Zheng, He Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models often remain sensitive to answer format: a question solved correctly in one form may fail in another semantically equivalent form. To study this gap, we define cross-format robustness as the extent to which a model answers the same underlying question consistently across formats. We then compare full-format training with FormatMix, which expands only a subset of training items into multiple equivalent formats using either random or targeted selection. Across GLM4 and Llama-3.1, multi-format supervision consistently improves both task performance and cross-format robustness, whereas Multiple-choice question (MCQ)-only supervision alone brings little benefit and can even reduce robustness. We further find that expanding only about 30% of the training set into multiple formats often recovers most of the gain from full-format training, and this effect appears across the model families and sizes we study. These results suggest that format diversity, rather than additional supervision alone, is the key driver of robustness. That lightweight multi-format augmentation is a practical way to make LLMs less sensitive to answer format without changing the base model.

---


### 58. [IAPO: Input Attribution-Aware Policy Optimization for Tool Use in Small Multimodal Agents](https://arxiv.org/abs/2606.11652)

**<font color=#1a73e8>作者：</font>** Yifan Yang, Zhen Zhang, Jiayi Tian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper investigates reinforcement learning (RL) methods for improving tool-calling capabilities in multimodal small language model (SLM) agents. While existing works have explored various reward designs to improve agentic tool-calling ability, these approaches face inherent limitations for SLM training, especially under multimodal scenarios. First, many existing methods evaluate tool use correctness through exact matching against certain ground-truth or predefined formats. However, this assumption is often unsuitable for multimodal tasks, where multiple tool use paths may be valid and annotated tool trajectories are typically unavailable. Second, such sparse and brittle binary rewards provide little guidance on how to improve the underlying decision process, making them particularly difficult for multimodal SLM to learn from. To address these issues, we propose Input Attribution-Aware Policy Optimization (IAPO), an RL algorithm for improving tool use in multimodal SLM by aligning the model's attribution across input components with that of a stronger teacher. Experiments on Qwen2.5-VL-3B show that the proposed method improves visual question answering accuracy by an average of 3% across six test sets compared with existing visual tool use work, by helping the model attend to the most relevant input evidence.

---


### 59. [Sparse probes and murky physics: a case study of interpretability challenges in a foundation model for continuum dynamics](https://arxiv.org/abs/2606.11657)

**<font color=#1a73e8>作者：</font>** Katherine Rosenfeld, Maike Sonnewald  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative AI emulators are increasingly used in scientific domains where we already have strong theory, benchmarks, and physical intuition. This raises a central evaluation and interpretability question: when a foundation-style model can reproduce known continuum dynamics, what internal mechanism supports that behavior, is the internal behaviour consistent with known physics, and how does it relate to where the emulator succeeds or fails? We investigate a cross-domain foundation model for continuum dynamics, Walrus by Polymathic, using mechanistic interpretability guided by physical principles. We apply a sparse autoencoder (SAE) to probe a selected layer, and address the practical challenge of triaging a large feature set (over 20,000) using enstrophy as a physically grounded metric. As a deliberately simple testbed, we focus on shear flow and compare feature recruitment across multiple shear-flow setups, i.e. parameter values in the numerical simulation. Across setups we find evidence of piecewise consistency, with subsets of features recurring in similar roles, but this structure is intermittent and does not map cleanly onto standard physical decompositions. In parallel, direct comparisons between numerical simulation and the emulator reveal systematic output-level discrepancies, including regimes where energy/structures become too diffuse or too localized. We connect parts of these discrepancies to changes in specific SAE feature usage. Our work highlights open questions for scientific foundation models: how to robustly prioritize mechanistically meaningful features, how to separate stable structure from analysis artifacts (including single-layer and SAE limitations), and how to use established benchmarks to decide when "different" internal representations are genuinely informative rather than merely effective.

---


### 60. [Lung-R1: A Knowledge Graph-Guided LLM for Pulmonary Diagnostic Reasoning](https://arxiv.org/abs/2606.11675)

**<font color=#1a73e8>作者：</font>** Haoyang Zeng, Yuanxi Fu, Rongzhen Li 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diagnosing pulmonary diseases requires integrating heterogeneous evidence amid phenotypic variability and cross-disease overlap. Although large language models (LLMs) have shown progress on pulmonary knowledge question answering (QA) and information-processing tasks, reliable pulmonary diagnosis requires patient-specific, relation-aware reasoning over electronic medical record (EMR) evidence rather than isolated knowledge recall. We define this gap between pulmonary knowledge and case-level diagnostic reasoning as the Pulmonary Knowledge-to-Diagnosis Gap. To address it, we introduce LungKG, the first structured pulmonary knowledge graph for diagnostic knowledge organization and record-grounded reasoning. LungKG contains 59,038 nodes and 164,308 edges across 15 entity types and 112 relation types, serving as both a reusable pulmonary knowledge resource and the foundation for LungKG-guided model adaptation. Built on LungKG, we propose Lung-R1, a LungKG-guided pulmonary LLM trained through KG-constrained reasoning-chain construction and KG-guided reinforcement learning. In a 20-system evaluation, Lung-R1-14B achieves state-of-the-art performance across Choice, Pulmonary-QA, and EMR Diagnosis, reaching an EMR Diagnosis score of 4.3583 and surpassing the strongest non-Lung-R1 baseline by 0.1476 points. These results demonstrate the value of LungKG-guided training for EMR-based pulmonary diagnosis.

---


### 61. [Can AI Reason Like an Urban Planner? Benchmarking Large Language Models Against Professional Judgment](https://arxiv.org/abs/2606.11678)

**<font color=#1a73e8>作者：</font>** Yijie Deng, He Zhu, Wen Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Problem, Research Strategy, and Findings: The rise of large language models (LLMs) raises a key question for urban planning: which forms of professional planning knowledge can AI replicate, and which still require human judgment? Although AI tools are increasingly used in planning practice, there is still no systematic framework for testing whether they can reason with the contextual sensitivity, value awareness, and institutional literacy central to planning expertise. This paper introduces Urban Planning Bench (UPBench), a domain-specific evaluation framework that assesses LLM reasoning through a 4x5 matrix of four knowledge pillars and five cognitive levels adapted from Bloom's revised taxonomy. Evaluating 25 LLMs with automated scoring and expert review, we find a non-monotonic cognitive curve: models perform better on higher-order analytical tasks than on factual recall and integrative judgment. This suggests that planning knowledge often treated as lower-order is deeply shaped by institutional, jurisdictional, and temporal context, making it hard for LLMs to generalize. We summarize these limits as four epistemic diagnostics: regulatory hallucination, conceptual conflation, wickedness paralysis, and phronetic deficit.
Takeaway for Practice: The findings support differential delegation in planning. LLMs can assist with cross-disciplinary synthesis, literature review, scenario generation, and preliminary policy analysis. However, they remain unreliable for jurisdiction-specific regulation, normative conflict resolution, and context-sensitive procedure. Agencies should require verification for AI-assisted regulatory analysis, while planning education should emphasize institutional literacy, normative judgment, and contextual sensitivity.

---


### 62. [Organize then Retrieve: Hierarchical Memory Navigation for Efficient Agents](https://arxiv.org/abs/2606.11680)

**<font color=#1a73e8>作者：</font>** Hao-Lun Hsu, Nikki Lijing Kuang, Boyi Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents struggle with long-horizon tasks due to their inherent statelessness, requiring all task-relevant information to be encoded in growing input contexts. The resulting degraded reasoning quality, increased inference cost, and higher latency necessitate efficient working memory mechanisms. However, existing approaches either rely on lossy compression or similarity-based retrieval, which often fail to capture temporal structure and causal dependencies required for multi-step agentic tasks. In this work, we present HORMA, a Hierarchical Organize-and-Retrieve Memory Agent that organizes experience into a file-system-like hierarchical structure, where summarized entities are linked to the corresponding raw trajectories, enabling efficient access without losing detailed information. HORMA decomposes working memory into two stages: structured memory construction and navigation-based retrieval. The construction module iteratively refines how experiences are structured by distinguishing between failures caused by missing information and those caused by misleading or overloaded context. The navigation module retrieves task-relevant context by traversing the hierarchy using a lightweight agent trained with reinforcement learning to select minimal yet sufficient context, thereby reducing latency along the critical execution path. Across ALFWorld, LoCoMo, and LongMemEval, HORMA improves task performance under constrained context budgets while requiring at most 22.17% of the baseline token usage in long conversation tasks. Compared to existing methods, it consistently achieves better efficiency-performance trade-offs and generalizes effectively to unseen tasks.

---


### 63. [Parameter-Efficient Adapter Tuning for Tabular-Image Multimodal Learning](https://arxiv.org/abs/2606.11682)

**<font color=#1a73e8>作者：</font>** Jiaqi Luo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tabular-image multimodal learning aims to improve predictive modeling by jointly using structured tabular attributes and visual data. Although pretrained encoders provide strong modality-specific representations, full fine-tuning can be computationally expensive, while keeping encoders frozen may limit task-specific adaptation. We propose the Tabular-Image Adapter (TI-Adapter), a modality-specific adapter-based fine-tuning framework for efficient multimodal adaptation. TI-Adapter freezes the pretrained tabular encoder and learns an adapter after the extracted tabular embedding, while adapting the image branch with embedding-level and bottleneck-level adapters instead of full fine-tuning. Experiments on 20 tabular-image datasets show that TI-Adapter achieves competitive or better predictive performance than full fine-tuning while using substantially fewer trainable parameters. Ablation studies further demonstrate the importance of adapter placement for balancing performance and practical efficiency.

---


### 64. [Layer-Isolated Evaluation: Gating the Deterministic Scaffold of a Production LLM Agent with a No-LLM, Regression-Locked Test Harness](https://arxiv.org/abs/2606.11686)

**<font color=#1a73e8>作者：</font>** Sawyer Zhang, Alexander Wang, Sophie Lei  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> End-to-end task-success is the dominant way to evaluate LLM agents, but one aggregate number tells you that an agent regressed, not where. We present layer-isolated evaluation: a deployed ordering agent is decomposed into a fixed taxonomy of layers (ontology, intent, routing, decomposition, escalation, safety, memory, and cross-cutting envelope/defense), each exercised by its own assertion slice in a deterministic, no-LLM "pure" mode. The pure suite (238 cases across 23 slices; 225 run in 2.39 s, ~10 ms/case) runs in CI on every change against a locked per-slice baseline. We validate by controlled regression injection, degrading one layer at a time across seven non-safety layers. The effect we did not design in is masking: the aggregate pass-rate barely moves (-1.7 to -5.9 pp for six local regressions), while the matching slice craters (-25 to -91 pp). A layer's slice reacting to its own fault is partly by construction; the measured results are (i) the aggregate masking and (ii) that damage stays off the other slices: the injected layer's slice is the single worst-hit in 5 of 7 cases and top-3 in 7 of 7 (mean rank 1.29 of 19). Localization replicates on a second, structurally different tenant (Starbucks SG): all seven matching slices crater, so it is not a single-catalog artifact. We position it as a concrete, deterministic instantiation of the component-level evaluation EDDOps prescribes but leaves unimplemented, with CheckList as ancestor and as the deterministic mirror image of whole-workflow stochastic mutation testing. Our contributions: (a) a fully decomposed, sub-second, no-LLM per-layer harness for a production agent, (b) a coverage-honesty test-adequacy criterion that refuses to score an unexercised layer, and (c) the regression-injection demonstration that per-slice baseline-locked gates localize regressions an aggregate metric masks.

---


### 65. [Substrate Asymmetry in User-Side Memory: A Diagnostic Framework](https://arxiv.org/abs/2606.11712)

**<font color=#1a73e8>作者：</font>** Youwang Deng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> User-side memory in LLMs is typically scored as a single "personalization" capability: given a user's history, is the output more user-aware? We show this aggregate metric hides opposite-direction failures. Memory factorises into at least three orthogonal axes -- behavioral consistency (style, voice), factual presence (recall facts in history), and factual absence (abstain when a fact is absent) -- and no single substrate wins all three. Comparing per-user gamma-LoRA (a small LoRA adapter trained on each user's history; gamma denotes per-user, not per-task) against BGE-large dense top-K retrieval on a controlled 50-user synthetic corpus and a real-data probe (LaMP-3), we find gamma-LoRA decisively wins behavioral style while RAG decisively wins factual absence -- and the same query-projection cells in attention layers 21-35 causally load-bear both effects in opposite directions (zeroing those LoRA weights raises absence-probe TPR by +33 pp and drops presence-probe TPR by 20 pp). On the more heavily RLHF-tuned Llama-3.1-8B-Instruct the asymmetry strengthens, not heals: parametric memory's behavioral advantage collapses while its absence-calibration deficit against retrieval widens -- an alignment tax on parametric user-memory. On real-data LaMP-3, gamma-LoRA underperforms a majority baseline; a 9-condition mitigation sweep diagnoses this as instruction-following collapse, not substrate failure (a 9x2 cross-product shows the eval-time {1..5} logit mask drives main_acc to >=0.995 on every recipe), and the best training-time fix replicates bit-identically on Llama. Finally, substrate-selection routing is question-classification, not calibration: a 110M DistilBERT on the question text alone beats every logit-based router. We contribute the diagnostic framework, the diagnosed real-data negative, the alignment-tax replication, and the routing-as-classification finding.

---


### 66. [Ouroboros-Spatial: Closing the Data-Model Loop for Spatial Reasoning](https://arxiv.org/abs/2606.11719)

**<font color=#1a73e8>作者：</font>** Enhan Zhao, Wei Wu, Yuanrui Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial reasoning remains a persistent challenge for multimodal large language models (MLLMs). Existing approaches largely rely on large-scale, statically curated datasets, where all training samples are treated uniformly regardless of the model's evolving capabilities. This static paradigm is inherently data-inefficient: training capacity is often spent on samples that are either trivial or overly difficult for the model at its current stage. To address this limitation, we propose Ouroboros-Spatial, a self-evolving training framework in which the model plays dual roles as a proposer and a solver. In each iteration, a frozen proposer generates spatial question-answer (QA) pairs from 3D scene metadata and raw video frames, together with executable code for deriving reliable ground truth. A learnable solver is then fine-tuned on the accepted samples, and its per-sample prediction confidence is used as a difficulty signal. This signal is fed back to the proposer in the next iteration, guiding it to generate questions better matched to the solver's current capabilities. Through this closed-loop design, the training distribution co-evolves with model ability, reducing redundant trivial examples while filtering out ambiguous or uninformative samples with limited learning value. Across six spatial reasoning benchmarks, Ouroboros-Spatial substantially improves Qwen3-VL-4B and Qwen3-VL-8B while using an order of magnitude fewer training examples than recent large-scale curated datasets. On VSI-Bench, it yields absolute gains of 9.9 and 6.8 points for the 4B and 8B models, respectively, enabling both to outperform a wide range of strong open-source and proprietary baselines.

---


### 67. [ICA Lens: Interpreting Language Models Without Training Another Dictionary](https://arxiv.org/abs/2606.11722)

**<font color=#1a73e8>作者：</font>** Sida Liu, Feijiang Han  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Finding interpretable directions in language-model representations is critical for understanding and controlling model behavior. Sparse autoencoders (SAEs) have become the standard tool for this purpose, but using them as the default first lens often requires training, storing, and evaluating large overcomplete dictionaries. This bottleneck limits rapid exploration and raises a fundamental question: how much interpretable structure is already visible from activation geometry before training another neural dictionary? Our intuition is simple: many interpretable directions are selective on tokens, and these directions should look less Gaussian than random directions. We therefore revisit independent component analysis (ICA), a classical method for finding non-Gaussian directions, as a compact lens for language-model interpretability. We find that ICA has been underestimated for LLM interpretability, because prior uses often relied on off-the-shelf ICA implementations that are brittle on LLM activations and lacked systematic tools for inspecting and evaluating the recovered directions. To bridge these gaps, we introduce ICALens, the first practical workflow for stable, efficient, and auditable ICA analysis of LLM representations. It combines an optimized GPU-parallel FastICA pipeline with LLM-specific stability recipes and better fitting diagnostics, enabling efficient and reliable layer-wise analysis. Across GPT-2 Small, Gemma 2 2B, and Qwen 3.5 2B Base, ICALens efficiently recovers compact, human-interpretable directions without per-layer gradient-based dictionary training. On SAEBench, ICA is competitive with public SAEs in sparse probing and outperforms them in targeted probe perturbation under small-to-medium budgets. These results suggest that ICA should not be viewed as a weak baseline, but as an efficient and complementary first lens for exploring language-model representations.

---


### 68. [From Prompts to Tokens: Internalizing Causal Supervision in Vision-Language Model for Multi-Image Causal Reasoning](https://arxiv.org/abs/2606.11745)

**<font color=#1a73e8>作者：</font>** Haoping Yu, Yuanxi Li, Jing Ma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual causal reasoning is essential for understanding and intervening in the physical world, requiring identification of causal variables from visual inputs and reasoning over intervention effects. Despite recent progress, large vision--language models (VLMs) remain brittle at such tasks, especially for interventional and counterfactual queries over multi-image inputs. Most existing explorations inject causal knowledge via textual prompts, leaving causal mechanisms external to model execution and limiting reliable control during inference. To address this problem, we propose BridgeVLM, which internalizes visual causal reasoning by inducing a causal graph from multi-image inputs and converting it into structured Causal Tokens executed by RAMP layers injected into the LLM decoder for causal message passing. We further introduce a unified training interface M3S for fine-grained causal supervision from different granularities (local/global level). BridgeVLM achieves 54.4% accuracy on intervention tasks on CausalVLBench (vs. 33.2% with prompt-level supervision), improves results on Causal3D from 43.6% to 49.0%, and substantially improves causal structure learning on CausalVLBench ($F_1$: 33.4% $\rightarrow$ 75.1%).

---


### 69. [Automated Creativity Evaluation of Language Models Across Open-Ended Tasks](https://arxiv.org/abs/2606.11762)

**<font color=#1a73e8>作者：</font>** Min Sen Tan, Zachary Kit Chun Choy, Syed Ali Redha Alsagoff 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have achieved remarkable progress in language understanding, reasoning, and generation, sparking growing interest in their creative potential. Realizing this potential requires systematic and scalable methods for evaluating creativity across diverse tasks. However, most existing creativity metrics are tightly coupled to specific tasks, embedding domain assumptions into the evaluation process, and limiting scalability and generality. To address this gap, we introduce an automated, domain-agnostic framework for quantifying LLM creativity across open-ended tasks. Our approach separates the measurement apparatus from the creative task itself, enabling scalable, task-agnostic assessment. Divergent creativity is measured using semantic entropy, a reference-free and robust metric for novelty and diversity, validated against human annotations, LLM-based novelty judgments and baseline diversity measures. Convergent creativity is assessed via a novel retrieval-based multi-agent judge framework that delivers context-sensitive evaluation of task fulfilment with over 60% improved efficiency. We validate our framework in three qualitatively distinct domains: problem-solving (MacGyver), research ideation (HypoGen), and creative writing (BookMIA), using a broad suite of LLMs. Empirical results show that our framework reliably captures key facets of creativity, including novelty, diversity, and task fulfilment, and reveal how model properties, such as size, temperature, recency, and reasoning, impact creative performance. Our work establishes a reproducible and generalizable standard for automated LLM creativity evaluation, paving the way for scalable benchmarking and accelerating progress in creative AI.

---


### 70. [SVoT: State-aware Visualization-of-Thought for Spatial Reasoning via Reinforcement Learning](https://arxiv.org/abs/2606.11770)

**<font color=#1a73e8>作者：</font>** Chao Lei, Yanbei Jiang, Markus Hiller 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spatial reasoning remains a challenge for Multimodal Large Language Models (MLLMs), as it requires reliable multi-hop inference over both intermediate states and state transitions. Current studies often leave intermediate states unverified and treat state transitions as implicit processes, which limits reliability in multi-hop spatial reasoning. To address this, we propose State-aware Visualization-of-Thought (SVoT), a reinforcement learning framework that generates interleaved, verifiable intermediate states and visualizations. SVoT integrates transition reasoning chains into the generation processes, enabling the model to verify action preconditions and effects through interleaved textual and visual reasoning. We train SVoT via Group Relative Policy Optimization (GRPO), instantiating verification through reward design and evaluating the efficacy of different fine-grained rewards. As existing benchmarks reduce state transitions to single-variable updates, substantially simplifying the problems, we establish five domains by extending classical environments and introducing two novel domains, Pacman and Gather, that require multi-object interactions and numerical reasoning. These domains support systematic evaluation of multi-hop spatial reasoning with quantitative verification of generated intermediate states and transition reasoning. SVoT with transition-aware supervision achieves state-of-the-art performance across the introduced domains, yielding up to a 65% absolute accuracy gain on out-of-distribution test sets.

---


### 71. [Lius: Translation Model Based Instructional Lingustic Using Continual Instruction Tuning In Kupang Malay](https://arxiv.org/abs/2606.11786)

**<font color=#1a73e8>作者：</font>** Joanito Agili Lopo, Yunita Sari, Guntur Budi Herwanto  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) offer new potential for translation tasks but often experience performance degradation when handling low-resource languages. To address this limitation, we propose an approach for fine-tuning LLMs on a low-resource language, Kupang Malay. Our approach involves designing a set of instructions by leveraging explicit lexical and semantic features from a bilingual dictionary, and introducing Continual Instruction Tuning (CIT), a training paradigm that enables iterative instruction-based training. Experimental results demonstrate that our model, named Lius, yields notable improvements over standard instruction-tuned models by outperforming 4-6 points, and surpassing both Neural Machine Translation (NMT) and Multilingual LLM models by 10-13 points on several evaluation metrics. These findings highlight the potential of our approach to mitigate the reliance on large-scale parallel data in low-resource language translation.

---


### 72. [MultiToP: Learning to Patch Visual Tokens to Mitigate Hallucinations in Video Large Multimodal Models](https://arxiv.org/abs/2606.11792)

**<font color=#1a73e8>作者：</font>** Yuansheng Gao, Wenbin Xing, Jiahao Yuan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Large Multimodal Models have achieved remarkable progress in video understanding, yet they remain prone to hallucinations, where generated responses are not faithfully supported by the input video. In this paper, we propose MultiToP, a multimodal-context-aware visual token patching framework that mitigates hallucinations by refining unreliable visual tokens before language generation. MultiToP introduces a lightweight Visual Token Patcher to predict token-level replacement distributions and selectively substitute unreliable visual tokens with a dynamic global patch token. To train the patcher effectively, we further propose information-guided rank calibration, which uses answer-conditioned frame-level information cues derived from the backbone to guide token replacement. Combined with ground-truth answer supervision and sparsity regularization, MultiToP enables localized visual evidence refinement without modifying the original model. Extensive experiments demonstrate that MultiToP effectively reduces hallucinations on Vript-HAL with negligible inference overhead, improving the F1 scores of Qwen3-VL-4B-Instruct by 50.60% over the vanilla model. Meanwhile, MultiToP preserves general video understanding ability, yielding an 18.58% relative accuracy gain on ActivityNet-QA for Video-LLaVA-7B.

---


### 73. [Multimodal Ordinal Modeling of Alzheimer's Disease Severity Using Structural MRI and Clinical Data](https://arxiv.org/abs/2606.11794)

**<font color=#1a73e8>作者：</font>** Boris-Stephan Rauchmann, Jonathan Laib, Buse Ercik 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neurodegenerative diseases such as Alzheimer's disease (AD) require accurate and scalable tools for assessing disease severity, yet current clinical staging remains time-intensive and prone to variability. We propose an attention-enhanced multimodal machine learning framework with ordinal regression for automated and interpretable AD severity staging. The framework integrates T1-weighted MRI with demographic and genetic variables and compares unimodal and multimodal architectures using ordinal and non-ordinal prediction heads. Models were trained and validated using cohort-stratified splits derived from the ADNI, AIBL, and NIFD datasets. A strictly held-out test set was constructed using subjects excluded from all training, validation, preprocessing, and hyperparameter tuning procedures, with subject-level splitting employed throughout to prevent data leakage. Among unimodal approaches, the T1-weighted MRI model achieved slightly higher adjacent-stage accuracy (0.963) and agreement with clinical staging (QWK 0.444) than the tabular model (QWK 0.433). Integrating imaging, demographic, and genetic information improved overall performance. The multimodal non-ordinal baseline achieved the lowest prediction error (MAE 0.340), whereas the ordinal multimodal model achieved the highest adjacent-stage accuracy (0.970) and strongest agreement with clinical staging (QWK 0.549). These findings indicate that ordinal formulations better capture the ordered structure of the CDR scale and yield predictions more consistent with clinical staging. Explainability analyses using Grad CAM++ and SHAP demonstrated anatomically and clinically plausible model behavior, supporting transparent decision-making. Overall, attention-based multimodal learning with ordinal regression represents a robust, interpretable, and scalable approach for automated AD severity staging and AI-assisted clinical decision support.

---


### 74. [External Experience Serving in Production LLM Systems: A Deployment-Oriented Study of Quality-Cost Trade-offs](https://arxiv.org/abs/2606.11806)

**<font color=#1a73e8>作者：</font>** Lin Sun, Heming Zhang, Xiangzheng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Production LLM systems accumulate reusable operational experience, but the practical deployment issue is not merely whether such experience can help. It is how different serving strategies trade off quality against online cost under realistic constraints. Injecting external experience can improve task quality, yet it also increases prompt burden, latency, and serving pressure. We study \textit{external experience serving} as a deployment-oriented quality-cost trade-off problem. We evaluate this question in a real production moderation setting, with tool-use and GPQA as supporting contrast tasks that expose different output-cost regimes. We compare no-experience baselines, random experience controls, global prompt injection, and retrieval-based selective injection, and analyze both task quality and serving cost. The results show that, once experience becomes case-dependent, selective retrieval provides a stronger operating point than unconditional global injection. They further show that retrieval quality matters more than simply increasing Top-$K$, and that the same serving policy can exhibit substantially different cost-benefit profiles across short-output and decode-heavy regimes. These findings suggest that external experience is best treated as a selective, cost-aware serving decision rather than as a universal add-on. Overall, in the settings studied here, external experience pays off only when both the serving interface and the task-specific cost structure make its quality gains worth the online cost.

---


### 75. [WorldReasoner: Evaluating Whether Language Model Agents Forecast Events with Valid Reasoning](https://arxiv.org/abs/2606.11816)

**<font color=#1a73e8>作者：</font>** Yizhou Chi, Eric Chamoun, Zifeng Ding 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Forecasting real-world events requires language-model agents to reason under uncertainty from incomplete, time-bounded information. Yet evaluating whether agents genuinely forecast requires more than final-answer accuracy: a model may be correct by recalling memorized training facts, citing fabricated evidence, or producing an unsupported causal story. We present WorldReasoner, an evaluation framework for temporally valid event forecasting. Each task gives an agent a resolved forecasting question, a simulated forecast date, and access only to evidence available before that date; after resolution, the framework scores the submitted probability, cited evidence, and optional causal event graph. WorldReasoner reports three complementary axes: outcome quality against resolved answers, evidence quality over cited sources, and reasoning quality against post-resolution hindsight graphs. The benchmark is built by an agentic construction pipeline that generates forecasting questions, collects time-stamped evidence, and builds hindsight reference graphs at scale, yielding 345 resolved tasks derived from 14,141 articles with graphs covering 8,087 extracted events. Across six controlled agent settings, temporally valid retrieval is the strongest driver of outcome accuracy; causal graph construction improves key-event recovery; and correct graph-enabled forecasts are more strongly grounded in key events and relevant sources, yet agents still struggle to convert grounded evidence into calibrated probabilities.

---


### 76. [Task-Aware Structured Memory for Dynamic Multi-modal In-Context Learning](https://arxiv.org/abs/2606.11853)

**<font color=#1a73e8>作者：</font>** Zhirui Chen, Ziwei Chen, Ling Shao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal large language models (MLLMs) depend on in-context learning (ICL) for rapid task adaptation, but their scalability is severely limited by finite context windows and the growing cost of key-value (KV) caches in long multi-modal sequences. Existing memory compression approaches typically rely on rigid token removal or sample-dependent importance estimation, which introduces bias, disrupts semantic structure, particularly for visual representations, and yields static memories that cannot adapt to new queries. We introduce TASM (Task-Aware Structured Memory), a training-free framework that addresses these limitations through task-aware, structure-preserving, and dynamically accessible memory construction. TASM employs task-vector guided compression to replace sample-specific signals with a task-level direction that captures shared relevance across demonstrations. To preserve the underlying manifold, it applies semantics-aware token merging via bipartite graph matching, aggregating tokens without destructive pruning. Finally, TASM structures memory into a hierarchy comprising a compact Core Memory and a Latent Bank, facilitating query-adaptive dynamic retrieval. Evaluations confirm TASM maintains high performance under heavy compression, effectively balancing efficiency with adaptability.

---


### 77. [Fine-tuning Multi-modal LLMs with ART: Art-based Reinforcement Training](https://arxiv.org/abs/2606.11854)

**<font color=#1a73e8>作者：</font>** Michal Chudoba, Sergey Alyaev, Petra Galuscakova 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> There are two main Parameter-Efficient Fine-Tuning (PEFT) techniques for Large Language Models (LLMs). While Low-Rank Adaptation (LoRA) introduces additional weights between the LLM layers, Soft Prompting introduces additional fine-tuning-specific raw tokens to an LLM input. However, both require modification to the computational graphs of precompiled, preoptimized LLMs. As a result, neither is fully supported in high-throughput engines like vLLM. We propose fine-tuning with ART (Art-based Reinforcement Training). The method injects information into a frozen Multimodal Large Language Model (MLLM) by optimizing only its raw visual input, thus enabling the soft-token approach on pre-compiled computational graphs. It relies on backpropagation of gradients back into a plain pixel array and thus supports any fine-tuning objective. Moreover, the optimized visual input can be stylized as task-relevant computational artworks. The approach's effectiveness is confirmed for different sizes of a popular open Qwen architecture and for several textual benchmarks. Specifically, ART reaches accuracy competitive with LoRA across mathematics and structured-tool-use benchmarks.

---


### 78. [Task-Aligned Stability Analysis of Vision-Language Models for Autonomous Driving Hazard Detection](https://arxiv.org/abs/2606.11889)

**<font color=#1a73e8>作者：</font>** Everett Richards  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly used for scene understanding in autonomous driving, but robustness analysis often relies on task-agnostic embedding stability alone. We study whether corruption-induced embedding drift predicts changes in a task-aligned hazard score derived from CLIP image-text similarities. Using controlled corruptions on BDD100K road scenes, we compare embedding drift against margin drift, defined as the change in hazard score under perturbation. The relationship is highly corruption-dependent: some families exhibit strong coupling between representation drift and decision drift, while others induce hazardous decision instability despite relatively modest embedding change. Furthermore, corruption families differ in failure direction: most suppress hazard detections via false negatives, while occlusion instead triggers false alarms, suggesting that benchmark design should account for asymmetric failure modes, not just overall instability rates. These results suggest that robustness benchmarks should include task-aligned stability measures in addition to embedding-level perturbation statistics.

---


### 79. [Beyond representational alignment with brain-guided language models for robust reasoning](https://arxiv.org/abs/2606.11893)

**<font color=#1a73e8>作者：</font>** Mingqing Xiao, Kai Du, Zhouchen Lin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The correspondence between large language models (LLMs) and the neural mechanisms underlying human higher-order cognition remains insufficiently characterized. Given that language and reasoning in the human brain appear dissociable, an open question is whether LLMs align with neural signals from reasoning-related regions and whether such signals can improve them. Here, focusing on deductive reasoning, we show that LLM internal representations are not only partially aligned with task-fMRI activity but can also be directly enhanced by these signals. Using a neural-predictivity metric, we find that LLMs explain a substantial fraction of the explainable variance in reasoning-related regions at the aggregate level, whereas predictivity within specific reasoning types is lower, indicating both alignment and divergence. Building on this, we propose a brain-guided framework: we steer model representations along directions induced by the joint structure of model and brain representations, applying intervention at inference and fine-tuning during training. We demonstrate that task-evoked brain signals can directly enhance LLM reasoning, yielding gains orthogonal to language-only supervision across 10 LLMs (1.5B-72B), with transfer across reasoning types and up to 13\% absolute accuracy gain. Our results advance LLM-brain correspondences from correlation to guidance, establishing a brain-signal-driven pathway toward more robust and cognitively aligned AI.

---


### 80. [GraspLLM: Towards Zero-Shot Generalization on Text-Attributed Graphs with LLMs](https://arxiv.org/abs/2606.11898)

**<font color=#1a73e8>作者：</font>** Hengyi Feng, Zeang Sheng, Meiyi Qiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Research on Text-Attributed Graphs (TAGs) has gained significant attention recently due to its broad applications across various real-world data scenarios, such as citation networks, e-commerce platforms, social media, and web pages. Inspired by the remarkable semantic understanding ability of Large Language Models (LLMs), there have been numerous attempts to integrate LLMs into TAGs. However, existing methods still struggle to generalize across diverse graphs and tasks, and their ability to capture transferable graph structural patterns remains limited. To address this, we introduce the GraspLLM, a framework that combines Graph structural comprehension with semantic understanding prowess of LLMs to enhance the cross-dataset and cross-task generalizability. Specifically, we represent node texts from different graphs in a unified semantic space with a frozen general embedding model, on top of which we perform motif-aware contrastive learning across multiple motif-induced adjacency matrices to extract dataset-agnostic structural information. Then, with our proposed optimal contextual subgraph, we extract the most contextually relevant subgraph for each target node and align these subgraphs to the token space of LLM via an alignment projector. Extensive experiments on TAG benchmark datasets spanning diverse domains reveal that GraspLLM consistently outperforms previous LLM-based methods for TAGs, especially in zero-shot scenarios, highlighting its strong generalizability across different datasets and tasks. Our code is available at this https URL.

---


### 81. [The Art of Interrogation: Consistency Amplifies Factuality in Spatial Reasoning](https://arxiv.org/abs/2606.11918)

**<font color=#1a73e8>作者：</font>** Theo Uscidda, Marta Tintore Gazulla, Maks Ovsjanikov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current Large Reasoning Models (LRMs) exhibit remarkable general capabilities but significantly underperform in spatial reasoning tasks. Existing approaches treat this gap as a knowledge deficit, relying on supervised fine-tuning (SFT) to ingest labeled spatial data from external vision sources or synthetic engines. In contrast, we argue that for many tasks, spatial reasoning capabilities are already present in pre-trained LRMs but require alignment through logical coherence under geometric 2D and 3D constraints. In this work, we propose a self-supervised reinforcement learning (RL) framework that targets the internal reasoning process without requiring ground-truth annotations. By formalizing the notion of consistency verifiers -- reward functions that check for geometric and semantic consistency under transformations -- we demonstrate that models can improve their spatial reasoning abilities. We use both image transformations, like flipping, and textual transformations, like swapping the order of objects in the question, and propose a new optimal transport-based RL strategy, OT-GRPO, which is a minimal-matching variant of group relative policy optimization tailored to pairwise verifiers. We show that this label-free consistency training approaches the accuracy of models trained with ground-truth supervision and achieves similar generalization across diverse tasks and data domains.

---


### 82. [Corpus Augmentation for Sign Language Translation via LLM-Guided Video Stitching](https://arxiv.org/abs/2606.11925)

**<font color=#1a73e8>作者：</font>** Zsolt Robotka, Ádám Rák, Jalal Al-Afandi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sign language translation (SLT) converts sign language video into spoken language text and holds significant promise for improving accessibility and enabling communication between signing and non-signing communities. While large weakly-aligned datasets have enabled pre-training at scale and gloss-free methods have reduced reliance on expert annotation, high-quality parallel sign video-text pairs for fine-tuning remain scarce, limiting generalisation on long-tail vocabulary and unseen constructions. We propose a corpus augmentation approach that requires no additional human annotation, external sign-language video corpora, or generative video models, relying only on the existing gloss-annotated training corpus and an LLM for sentence generation: per-gloss clips are extracted from training videos via CTC forced-alignment, novel gloss-sentence pairs are generated by a corpus-anchored LLM, and synthetic sequences are assembled through random sentence sampling and clip assignment. The resulting synthetic RGB video-text pairs are architecture-agnostic at the downstream training stage and can be consumed directly by RGB-based SLT models, or converted into pose or feature representations by pipelines that derive such inputs from video. Sincan et al. re-evaluated five recent gloss-free methods under strictly identical conditions; the largest verified gain over the GFSLT-VLP baseline was only 0.98 BLEU-4. Our augmentation, applied within the same framework, achieves +2.92 BLEU-4 without any change to architecture or training protocol. We further identify that synthetic data harms vision-language pretraining despite improving its objectives, and that optimising clip transitions for visual smoothness is counter-productive under L2-based criteria; we propose that abrupt boundaries may act as a form of implicit regularisation. Code is available at this https URL.

---


### 83. [Frozen Multimodal Embeddings for Personality and Cognitive Ability Assessment in Asynchronous Video Interviews](https://arxiv.org/abs/2606.11930)

**<font color=#1a73e8>作者：</font>** Kuo-En Hung, Hung-Yue Suen, Shih-Ching Yeh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Predicting psychological traits from asynchronous video interviews (AVIs) is a challenging multimodal learning problem because labeled datasets are limited while each response contains high-dimensional visual, acoustic, and verbal signals. This paper presents our solution for the ACM Multimedia AVI Challenge 2026, which evaluates two tasks: Track~1 predicts self-reported HEXACO personality traits from personality-related interview responses, and Track~2 classifies cognitive ability levels from structured AVI responses. We treat the problem as a small-sample representation learning task. Instead of fine-tuning large pretrained models, we use frozen multimodal encoders, including CLIP for visual features, Whisper for acoustic features and transcripts, and RoBERTa, E5, and DeBERTaV3 for textual representations, followed by low-capacity downstream models. For Track~1, our trait-specific regression and late-fusion system achieves an average validation MSE of 0.2696, improving over the official baseline of 0.3334. Ablation results show a three-step improvement from a global model (0.3189), to per-trait modeling (0.2871), to per-trait late fusion (0.2696), corresponding to a 19.1\% relative MSE reduction over the official baseline. For Track~2, a compact subject-attribute baseline reaches 0.5781 accuracy, while our multimodal ensemble reaches 0.5313, both above the official baseline of 0.4062. We interpret this result as evidence of possible subject-attribute shortcuts in the validation split rather than robust cognitive inference from AVI content. Overall, our findings suggest that AVI-based psychological assessment benefits from trait-specific multimodal modeling, but cognitive ability prediction requires careful control of dataset shortcuts.

---


### 84. [Semantic Grading of Written Answers in Low-Resource Language Bangla Using a Fine-Tuned Lightweight Language Model](https://arxiv.org/abs/2606.11931)

**<font color=#1a73e8>作者：</font>** Meherun Farzana, Aniket Joarder, Mahmudul Hasan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Bangla is among the world's most widely spoken languages, yet it remains underserved in educational NLP research. In many remote and rural regions, access to qualified subject teachers is limited, and written answers are consequently graded largely by hand, restricting timely and consistent feedback. Automatic assessment is challenging because semantically correct responses can vary substantially in surface form. We present a bilingual (Bangla-English) evaluation system designed for low-resource educational settings that prioritizes semantic correctness over lexical overlap. Our approach fine-tunes a lightweight language model to grade each response using the question, reference answer, and student answer, producing a numeric score and concise, context-grounded feedback suitable for classroom deployment. We also construct a synthetic bilingual dataset to enable controlled training and evaluation. Across proprietary and open-source LLMs evaluated under a unified protocol, our QLoRA-tuned Qwen3-8B confirms consistent improvement by producing the most leakage-resistant feedback (RoRa = 0.819) in synthetic evaluation and the strongest agreement with human scores (rho = 0.936, MAE = 0.725) in a dedicated human study.

---


### 85. [uva-irlab-conv at SemEval-2026 Task 8: Multi-Turn RAG with Learned Sparse Retrieval and Listwise Reranking](https://arxiv.org/abs/2606.11945)

**<font color=#1a73e8>作者：</font>** Simon Lupart, Kidist Amde Mekonnen, Zahra Abbasiantaeb 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This report describes our participation in SemEval-2026 Task 8 on multi-turn retrieval and question answering. The task evaluates conversational systems across four domains (finance, cloud documentation, government, Wikipedia), and includes unanswerable queries where the available collection does not contain sufficient evidence to produce a complete response. We propose a multi-turn retrieval-augmented generation pipeline that combines learned sparse retrieval with LLM-based reranking and generation. Using sparse retrieval as the primary retrieval method, we leverage its strong generalization across domains. In addition, we make use of the long-context capabilities of LLMs for conversational query rewriting, pointwise and listwise reranking, and generating the final response, each conditioned on the full conversational history. This multi-step design enables effective integration of conversational context throughout retrieval and generation, improving robustness across domains.

---


### 86. [Decoding Multimodal Cues: Unveiling the Implicit Meaning Behind Hateful Videos](https://arxiv.org/abs/2606.11953)

**<font color=#1a73e8>作者：</font>** Junyu Lu, Deyi Ji, Liqun Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hateful videos have become prevalent on online platforms, highlighting an urgent need for effective detection. However, existing studies primarily focus on binary classification and fail to provide contextual rationales that reveal the implicit meanings behind these judgments, significantly undermining model explainability. To fill this gap, we aim to achieve explainable hateful video detection, enabling models to provide contextual rationales that integrate relevant evidence and logical reasoning alongside decisions. This approach can comprehensively enhance the understanding of video content and the explainability of the decision-making process. We first introduce two datasets, Ex-HateMM and Ex-ImpliHateVid, for explainable hateful video detection. Each dataset provides fine-grained annotations of multimodal harmful elements, along with contextual rationales. We then propose an Information Augmentation and Reasoning Enhancement (IARE) framework designed for explainable detection. The framework employs an information augmentation phase that leverages the multimodal chain-of-thought to integrate harmful elements, thereby enriching rationale evidence. Additionally, IARE incorporates a reasoning enhancement phase, in which Direct Preference Optimization guides the model toward correct reasoning paths and away from incorrect ones, thereby improving the logical coherence of its justifications. We conduct extensive experiments on the two datasets, comparing multiple baselines with our proposed IARE framework. The results demonstrate that IARE achieves state-of-the-art performance while also generating accurate rationales.

---


### 87. [Categorical Prior Lock-in: Why In-Context Learning Fails for Structured Data](https://arxiv.org/abs/2606.11961)

**<font color=#1a73e8>作者：</font>** Antonio Pelusi, Stefano Braghin, Alberto Trombetta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as conditional generators for structured data, relying on in-context learning (ICL) to adapt to new distributions without parameter updates. We investigate the limits of ICL for structured generation under distribution mismatch, using high-cardinality tabular data as a controlled test case, and identify a structural failure mode we term \textit{categorical prior lock-in}: the inability of ICL to update the model's prior over token distributions inherited from pre-training. Across two 7B-parameter open-weight models, ICL improves numerical fidelity with additional examples but exhibits a sharp ceiling on categorical distributions, failing to reproduce rare classes entirely. Parameter-efficient fine-tuning (LoRA) overcomes these limitations but introduces measurable memorization risk and, in some cases, destabilizes structured output generation, highlighting a fundamental trade-off between adaptability and privacy.

---


### 88. [ParseFixer: An Agentic Framework for Document Parsing via Selective Multimodal Correction](https://arxiv.org/abs/2606.11977)

**<font color=#1a73e8>作者：</font>** LeKai Yu, Hao Liu, Kun Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this report, we present our third-place solution for the DataMFM Challenge Track 1: Document Parsing. This track requires models to recover structured Markdown documents from document page images while preserving textual content and document structure. To address the complementary requirements of accurate content recovery and faithful structure reconstruction, we propose ParseFixer, an agentic framework for backbone parsing and selective correction. ParseFixer consists of two key modules: Full-Page Backbone Parsing (FBP) and Agentic Selective Correction (ASC). FBP produces stable initial Markdown outputs with MinerU2.5 Pro, while ASC detects high-value parsing failures and repairs them through a verify-and-rollback correction process. By placing selective multimodal correction after open-source backbone parsing, ParseFixer improves the recovery of key document elements without rewriting reliable backbone predictions. On the test set, our final system achieves an overall score of 61.78 and ranks third in Track 1, demonstrating its effectiveness for accurate document parsing. Our code will be released at: this https URL.

---


### 89. [Time-Series Foundation Model Embeddings for Remaining Useful Life Estimation](https://arxiv.org/abs/2606.11990)

**<font color=#1a73e8>作者：</font>** Amir El-Ghoussani, Michele De Vita, Ronald Naumann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Remaining Useful Life (RUL) prediction is essential for industrial predictive maintenance, yet many learning-based approaches rely on extensive feature engineering or large labeled datasets to train task-specific sequence models. In this work, we introduce a lightweight learning approach, in which we leverage a frozen pretrained time-series foundation model (TSFM) and combine it with a small regression head for RUL estimation from multivariate sensor streams. More specifically, we use Chronos-2 as a frozen backbone to extract context window features and train a lightweight regression neural network for RUL prediction. Experiments on real-world industrial sensor data from two device types show that Chronos-2 features consistently improve over recurrent, convolutional, Transformer-based, and gradient-boosting baselines under the same preprocessing and evaluation protocol. We further analyze the impact of context length and find that performance improves significantly with longer histories, indicating that TSFM representation offer a practical and data-efficient alternative for RUL estimation in industrial settings.

---


### 90. [Bootstrapped Monitoring: Leveraging Transparent Reasoning to Oversee Stronger AI Agents](https://arxiv.org/abs/2606.11998)

**<font color=#1a73e8>作者：</font>** Frank Xiao, Mary Phuong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Trusted monitoring is a cornerstone of AI control. However, as frontier models grow more capable, the increasing capabilities gap between trusted and untrusted models may render trusted models unreliable monitors. We introduce \emph{bootstrapped monitoring}, a protocol that addresses this by inserting a stronger, intermediate untrusted model with transparent chain-of-thought reasoning into the oversight chain. The untrusted monitor ($U_m$) evaluates the agent's actions, while a weaker trusted model ($T$) oversees $U_m$'s reasoning to detect collusion. We evaluate bootstrapped monitoring on multi-turn software engineering tasks (BashArena) across multiple agents and monitors. Bootstrapped monitoring substantially improves catch rates over trusted-only monitoring, even when the untrusted monitor actively colludes with the agent, provided we have access to its raw chain-of-thought. Our results suggest that bootstrapped monitoring can extend the useful lifetime of trusted models in control as AI capabilities advance.

---


### 91. [Tabular Foundation Models for Clinical Survival Analysis via Survival-Aware Adaptation](https://arxiv.org/abs/2606.12006)

**<font color=#1a73e8>作者：</font>** Minh-Khoi Pham, Luca Cotugno, Alina Sirbu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting time-to-event outcomes such as mortality is a fundamental task in clinical decision-making, commonly addressed through survival analysis. While classical statistical and deep learning approaches have been widely studied, they typically require task-specific training and sufficient labeled data. Recent advances in tabular foundation models offer a new paradigm by learning general-purpose representations for structured data. However, their applicability to censored time-to-event prediction in clinical settings remains underexplored, as typical applications are restricted to discrete classification rather than survival analysis tasks.
In this work, we propose a lightweight adaptation approach for applying tabular foundation models to clinical survival analysis by directly training a survival-aware head on top of the pretrained representations. We study representative architectures, including TabPFN, TabDPT, and TabICL, and adapt them using a multi-task logistic regression (MTLR) head to model right-censored time-to-event outcomes. We evaluate this approach on a diverse set of public survival benchmarks and two large-scale ICU cohorts, MIMIC-IV and eICU.
Our results show that this transfer learning approach achieves competitive or superior performance compared to strong baselines. On MIMIC-IV, TabDPT-FT-MTLR reaches a C-index of 0.856, corresponding to a relative improvement of +1.4% over the best non-FM baseline (DeepSurv, 0.844) and +6.7% over the best zero-shot model (0.802). On eICU, TabICL-FT-MTLR achieves 0.797, yielding gains of +1.7% (DeepSurv, 0.784) and +6.4% (0.749), respectively. These findings highlight the importance of combining pretrained tabular representations with survival-aware objectives and suggest that tabular foundation models provide a practical and effective alternative for clinical survival prediction.

---


### 92. [MODF-SIR: A Multi-agent Omni-modal Distilled Framework for Social Intelligence Reasoning](https://arxiv.org/abs/2606.12018)

**<font color=#1a73e8>作者：</font>** Shang Ma, Jisheng Dang, Wencan Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose a multi-agent collaborative framework built upon a lightweight Multimodal Large Language Model (MLLM), specifically designed for social intelligence reasoning. A key feature of our approach is that both the training and inference phases are augmented via knowledge distillation. Within this architecture, multi-modal data pertinent to social intelligence is precisely localized. Furthermore, relevant long-tail events are identified, extracted, and rendered as formatted, explicit text. This formatting strategy prevents critical long-tail information from being overshadowed by head events and environmental noise during the tokenization process. Specifically, we integrate Test-Time Adaptation (TTA) across the entire reasoning pipeline, encompassing the extraction and representation of long-tail events, Chain-of-Thought (CoT) prompting, and self-reflection. This TTA mechanism is also distillation-enhanced, utilizing Low-Rank Adaptation (LoRA) to fine-tune the foundation model exclusively for instance-level reasoning. Extensive evaluations against various open-source and proprietary AI models across multiple benchmarks demonstrate the effectiveness of the proposed framework. With around 30% of training data from IntentTrain, we achieve state-of-the-art results. Codes are available at this https URL, demo is available at this https URL, LoRA is available at this https URL and the dataset for training router is available at this https URL.

---


### 93. [A Lightweight Multi-Agent Framework for Automated Concrete Barrier Design](https://arxiv.org/abs/2606.12040)

**<font color=#1a73e8>作者：</font>** Wanting Wang, Xiye Ma, Yuyang He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The design of reinforced concrete highway barriers is a safety-critical process that requires strict compliance with regulatory provisions such as the AASHTO-LRFD bridge design guidelines. Current engineering practice relies heavily on manual, iterative, and heuristic calculations to satisfy complex nonlinear material and mechanics constraints. Although Large Language Models (LLMs) demonstrate strong generative capabilities, their direct application to structural engineering remains limited by hallucination risks and insufficient physical grounding. To address these challenges, this study proposes a novel "generation-evaluation-optimization" closed-loop framework for automated concrete barrier design using the multi-agent orchestration capabilities of AutoGen. Experimental results demonstrate that the proposed agentic framework achieves over 98% design accuracy, significantly outperforming standalone general-purpose LLMs. More importantly, the study reveals that design performance is not necessarily correlated with model scale, where an 8B-parameter lightweight model could outperform unconstrained 631B-parameter flagship models. This finding highlights the potential to substantially reduce computational costs while improving the accessibility of AI-assisted engineering tools for industry applications. The source code for the proposed multi-agent design framework is available at the project GitHub repository: this https URL. Keywords: Structural Engineering; Multi-Agent Systems; Large Language Models; Concrete Barrier Design; AutoGen; Design Automation.

---


### 94. [Tac-DINO: Learning Vision-Tactile Features with Patch Alignment](https://arxiv.org/abs/2606.12069)

**<font color=#1a73e8>作者：</font>** Hong Li, Yankang Dong, Yue Xu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Touch is the primary medium through which humans interact with the environment. Currently, tactile learning mainly focuses on image-level pretraining or alignment. However, tactile signals correspond to local object contact, while research into scale alignment and holographic matching remains limited and proper datasets and benchmarks also lack. To bridge this gap, we first construct a data collection system to acquire a large-scale tactile dataset, with over 20 K tactile contacts from 505 real-world objects. Building on this dataset, we design a Vis-Tac Holographic Matching Benchmark to evaluate vision-tactile local-to-global alignment ability. Then we propose Vision-Tactile Patch Alignment (VTPA) methods for vision-tactile representation learning. Experiments demonstrate that these exceed the performance of methods without alignment and align with whole-object images.

---


### 95. [World Model Self-Distillation: Training World Models to Solve General Tasks](https://arxiv.org/abs/2606.12072)

**<font color=#1a73e8>作者：</font>** Sebastian Stapf, Pablo Acuaviva Huertos, Aram Davtyan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained video generators are promising visual world models that exhibit emergent task-solving abilities; however, their reliance on detailed textual descriptions limits their direct use for planning and decision-making. Existing approaches either outsource this reasoning to language or vision-language models, or rely on supervised fine-tuning with paired task-execution videos, which are costly to collect and difficult to scale. We propose a scalable framework that elicits task-solving ability in such models by combining self-distillation with reinforcement learning. Given an unlabeled scene image, a vision-language model generates a candidate task and a detailed step-by-step solution. The solution conditions a pretrained video diffusion model, the Demonstrator; we distill its behavior into an Executor conditioned only on the image and a short task prompt. This transfers execution knowledge from caption-guided generation to instruction-conditioned task solving without curated task-video supervision. We further improve the Executor with reinforcement learning from VLM feedback, exploiting the asymmetry between judging whether a sampled video satisfies a task and generating the solution. Experiments on our proposed WorldTasks-Benchmark and the DreamGen robotics benchmark show that the Executor surpasses the Demonstrator under our VLM-based evaluation protocol and transfers competitively to robotic tasks.

---


### 96. [MSUE: Multi-Modal Soccer Understanding Expert](https://arxiv.org/abs/2606.12106)

**<font color=#1a73e8>作者：</font>** Litao Li, Yibo Yu, Yufeng Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents our solution to the 2026 SoccerNet VQA Challenge. We first develop a cost-effective data synthesis pipeline driven by a Vision-Language Model (VLM), which systematically restructures raw domain data into diverse VQA samples, including concise answers and long-form responses. Second, we propose MSUE, a multi-expert question answering architecture that employs a Large Language Model (LLM) to dynamically dispatch questions to text, image, and video experts. These experts are instantiated as a strong text baseline Gemini3-Flash, a fine-tuned Qwen3-VL, and an external knowledge base, respectively, working collaboratively to enhance VQA performance. MSUE achieves an accuracy of \textbf{0.95} on the challenge benchmark, securing third place in the leaderboard.

---


### 97. [Augmenting Molecular Language Models with Local $n$-gram Memory](https://arxiv.org/abs/2606.12113)

**<font color=#1a73e8>作者：</font>** Xinni Zhang, Zijing Liu, He Cao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformer-based language models for SMILES strings suffer from a locality gap: standard character-level tokenization fragments chemically meaningful motifs, forcing models to repeatedly learn local syntax at the expense of long-range dependencies. To address this without disrupting standard tokenizers, we propose MolGram, which integrates a conditional $n$-gram memory module into molecular language models. MolGram maps local string patterns to learned embeddings via scalable hash lookups and dynamically injects this regional context into hidden states. Evaluations across three tasks, including unconditional molecule generation, forward reaction prediction, and single-step retrosynthesis, show that MolGram consistently improves performance. Crucially, our analyses demonstrate that MolGram outperforms baselines with 3$\times$ more parameters, establishing explicit local pattern memory as a highly efficient inductive bias.

---


### 98. [Detecting Sensitive Personal Information in Japanese Pre-Training Corpora for Large Language Models](https://arxiv.org/abs/2606.12114)

**<font color=#1a73e8>作者：</font>** Rei Minamoto, Yusuke Oda, Daisuke Kawahara  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sensitive personal information can appear in large-scale pre-training corpora for large language models (LLMs). Detecting and filtering such information is therefore essential to ensure compliance with privacy regulations and prevent unintended information leakage. However, in contrast to English and other languages, research into sensitive personal information has been limited in the Japanese language. In this study, we focus on sensitive personal data defined as special care-required personal information (SCPI) under Japan's Act on the Protection of Personal Information (APPI). We construct an SCPI dataset using LLM-based annotation and train machine learning models to rapidly detect SCPI in text. As a result, our SCPI classifier can effectively identify information related to SCPI. This study is the first to explore SCPI detection in Japanese text corpora, highlighting the challenges of accurate detection.

---


### 99. [Soft-Prompt Tuning for Fair and Efficient LLM Benchmark Evaluation](https://arxiv.org/abs/2606.12117)

**<font color=#1a73e8>作者：</font>** Selen Erkan, Bastian Boll, Kristian Kersting 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Benchmark scores often misrepresent a large language model's (LLM's) knowledge, because they rely, e.g., on the model's ability to follow specific formatting requirements. This especially penalizes base models that may know the correct answers but lack the ability -- typically introduced in post-training -- to structure them as instructed. To overcome this, we propose soft-prompt tuning, an efficient, fair, and architecture-agnostic model evaluation. By optimizing only 10 soft-prompt vectors (roughly 0.0006% parameters for a 7B model) over a short tuning period, we adapt models to specific benchmark formats, closing gaps in format-following and ensuring that underlying knowledge is accurately reflected in benchmark scores. This allows one to fairly compare different base models -- trained with various pre-training recipes -- on benchmarks without the need for full post-training. We evaluated soft-prompt tuning across 7 models and 7 datasets. The results show that (a) soft-prompt tuning saturates format-following within 80 steps (~640 samples) making it highly efficient, (b) soft-prompt tuning significantly outperforms zero- and few-shot prompting, surfacing base model knowledge that standard prompting misses, that (c) even post-trained models can benefit from soft-prompts to maximize format compliance, and that (d) soft-prompted base model performance predicts post-trained model rankings more reliably than zero- and few-shot baselines, offering a low-cost proxy for downstream model quality. Our contributions include (1) metrics which disentangle format-following and knowledge accuracy, (2) a fairer benchmarking protocol of LLM knowledge, and (3) a cost- and memory-effective recipe to identify optimal pre-training strategies early in LLM development.

---


### 100. [Q-Fold: Query-Aware Focus-Context Spatio-Temporal Folding for Long Video Understanding](https://arxiv.org/abs/2606.12125)

**<font color=#1a73e8>作者：</font>** Biao Tang, Xu Chen, Shuxiang Gou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-video understanding remains challenging for multimodal large language models, because temporally extended videos often contain thousands of frames and are therefore expensive to process exhaustively. Existing methods usually construct compact visual inputs from long videos under a limited visual budget. However, most of them still follow a frame-centric paradigm and apply similar representations to retained content regardless of its importance. This makes it difficult to preserve both high-fidelity visual evidence and broad temporal coverage. To address this issue, we propose Q-Fold, a training-free input construction framework for long-video understanding. Instead of treating isolated frames as the basic modeling unit, Q-Fold operates on contiguous temporal segments and constructs a heterogeneous Focus--Context representation under query guidance. Query-relevant segments are preserved as high-fidelity Focus Frames, while less relevant segments are folded into chronology-preserving contextual layouts. In this way, Q-Fold preserves critical visual evidence and broad temporal coverage, while better maintaining local temporal continuity within short segments. Experiments on four long-video benchmarks with multiple Video-MLLMs show that Q-Fold consistently improves performance without increasing the input budget. Notably, it achieves gains of up to 9.1 percentage points on an ultra-long video benchmark. Code will be made publicly available.

---


> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-128](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
