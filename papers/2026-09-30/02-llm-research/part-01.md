# 🧠 大模型相关研究 | 2026年09月30日

> 本类共 **992** 篇论文：已确认 **928** 篇，待复核 **64** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

---

### 1. [ChestPheNoT: Deployable, Auditable Label-Status-Evidence Extraction from Radiology Reports](https://arxiv.org/abs/2609.31629)

**<font color=#1a73e8>作者：</font>** Kai Yu, Chenyu Zhu, Zaifu Zhan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Structured phenotype extraction from radiology reports supports cohort construction, quality auditing, and clinical analytics, but practical deployment requires local inference and auditable predictions, while expert annotations remain scarce. Conventional labelers provide structured findings and assertion states but no supporting evidence, while API-hosted large language models may be unsuitable when clinical text cannot leave institutional infrastructure. We present CHESTPHENOT, a compact 0.5-3B language model that jointly extracts finding labels, three-class status (present/absent/uncertain), and verbatim supporting evidence spans. CHESTPHENOT is trained using hybrid CheXbert+72B silver supervision followed by supervised fine-tuning and lightweight GRPO refinement. Across three human-annotated gold sets spanning in-distribution, cross-taxonomy, and cross-institution evaluation, the 3B model remains below its CheXbert silver teacher in distribution but is competitive under distribution shift, significantly surpassing CheXbert on cross-institution detection (+2.0 F1). Task-specific training also enables the 3B model to match or exceed substantially larger prompted models on most detection and status comparisons. For evidence-grounded extraction, over 99% of final evidence spans are locatable in the source report, and the 3B model achieves 47.5 auditable-F1, outperforming Qwen2.5-7B one-shot prompting by 7.6 points and approaching Qwen2.5-72B. These results demonstrate that locally deployable models can provide competitive and directly auditable radiology-report extraction without relying on external inference APIs. Code and the full extraction/judge prompts will be made available at this https URL.

---


### 2. [OMP-MoE: Efficient Expert Pruning for Mixture-of-Experts LLMs via Orthogonal Matching Pursuit](https://arxiv.org/abs/2609.31631)

**<font color=#1a73e8>作者：</font>** Dezhi Li, Lujun Li, Qiyuan Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models enable efficient scaling of large language models but face critical deployment challenges due to massive memory requirements. Existing pruning methods either incur prohibitive search costs or neglect the dynamic interdependencies between experts. To address these challenges, we present OMP-MoE, a novel training-free compression framework for reducing expert redundancy in MoE-based LLMs. Based on observations of expert contribution patterns, we reformulate the pruning problem as a sparse signal reconstruction task solved through Orthogonal Matching Pursuit. Specifically, our method first treats individual expert contributions as dictionary atoms and selects experts that greedily minimize reconstruction error with linear computational complexity. Then, we optimize cross-layer expert allocation through a water-filling strategy that accounts for both reconstruction quality and routing stability. Finally, we introduce OMP-MoE†, an adaptive inference mechanism that dynamically adjusts expert activation based on energy prediction. Comprehensive experiments on Qwen, DeepSeek-V2, GPT-OSS, and Mixtral MoE demonstrate consistent improvements over existing methods at 25-50% pruning ratios. For Qwen3-30B-A3B at 50% compression, we retain 93.3% of original performance, achieving 33$\times$ faster search and 1.55$\times$ inference speedup. Codes will be available after acceptance.

---


### 3. [EEGAgentBench: Benchmarking LLM Agents on Short- and Long-Horizon EEG Analysis](https://arxiv.org/abs/2609.31632)

**<font color=#1a73e8>作者：</font>** Huyu Wu, Weining Weng, Yuchen Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) analysis is evolving from short-segment classification toward long-horizon interpretation that demands iterative evidence accumulation, multi-step reasoning, and coordinated use of specialized signal-processing tools. Although large language models (LLMs) have recently shown promise as autonomous agents for EEG analysis, existing EEG agentic evaluations remain fragmented, covering limited tasks over narrow temporal horizons with inconsistent protocols, and providing no comprehensive assessment of agents' reasoning, tool-use, and workflow construction capabilities. To address this gap, we propose \textbf{EEGAgentBench}, a unified benchmark for systematically evaluating LLM agents on short- and long-horizon EEG analysis. EEGAgentBench spans six representative EEG applications ranging from knowledge question answering to sleep staging. It encompasses signal durations from 2 seconds to nearly 23 hours, with prediction targets ranging from class labels to event intervals and epoch-level sequences. This design supports unified evaluation across knowledge reasoning, short-horizon interpretation, long-horizon event detection, and sequential understanding. The benchmark further provides 10 deterministic EEG analysis tools that expose only task-relevant signal measurements. Agents must therefore select tools autonomously, accumulate evidence iteratively, and construct multi-step workflows. For evaluation, we benchmark 29 frontier LLMs from 15 model families. Results demonstrate that EEGAgentBench effectively distinguishes agent capabilities beyond model scale and inference cost, while revealing substantial limitations of current LLM agents in long-horizon EEG analysis, particularly in sustained evidence accumulation and multi-step reasoning.

---


### 4. [Grounding Vision-Language Models in Driving Semantics: A Multi-Dataset Predicate Framework for Explainable Reasoning](https://arxiv.org/abs/2609.31636)

**<font color=#1a73e8>作者：</font>** Mohamed Chouai, Fazli Faruk Okumus, Stefan Kugele  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-language models are increasingly used for driving-scene understanding, yet the semantic relations expressed in their outputs are often difficult to verify against the underlying traffic situation. This paper introduces a deterministic multi-dataset predicate framework that derives driving-scene semantics from measurable geometric, kinematic, temporal, map, and traffic-control evidence. Dataset-specific interfaces are used only to recover the required scene information, while predicate definitions remain unchanged across nuPlan and nuScenes and are materialised in a common Predicate Knowledge Graph. Quantitative semantic validation against manually annotated predicate relations on 200 scenarios from each dataset yields macro F1 scores of 0.94 on nuPlan and 0.93 on nuScenes, with an average cross-dataset difference of 0.02 across the shared predicates. The Predicate KG is further evaluated using a frozen LLaVA-OneVision-7B model on the nine NuPlanQA subtasks. Predicate grounding achieves the highest accuracy among the evaluated visual-input conditions in seven of nine NuPlanQA subtasks, including Traffic Light (53.2% to 71.5%), Situation Assessment (76.2% to 86.1%), and Action Recommendation (82.9% to 89.0%). Weather/Lighting remains essentially unchanged (89.4% vs. 88.8%), consistent with the absence of corresponding predicates, while Predicate KG only input outperforms metadata-only input in eight of nine subtasks. The results show that deterministic predicates provide a consistent and traceable semantic representation and, under oracle grounding, can reduce visual dependence for reasoning tasks covered by the predicate vocabulary.

---


### 5. [Measure Learning at Steady State: A BIRD-SQL Formula 1 Case Study](https://arxiv.org/abs/2609.31640)

**<font color=#1a73e8>作者：</font>** Manoj Bajaj  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual Learning Bench scores learning as short-horizon gain versus a reset baseline and finds naive full-context ICL strongest among the memories it tested. We treat ICL as one learning system and score it on a longer shared-world schedule. Steady-state learning is the gap versus baseline on a pre-set late window (last 40 of 174 BIRD-SQL formula-1 questions). We split the score into exploration efficiency (SQL probes), task reward (hits), and delivery cost (API dollars and context size). On gpt-5.6-luna, late probes fall from 4.6-5.6 to 0.95 while hits rise only modestly and ICL context grows to about 95k tokens with cost roughly doubling. Short-horizon gain understates the late probe saving and misses the cost inversion, so we find that unbounded ICL is a poor candidate for the learning mechanism.

---


### 6. [Information Design Against Gaming and Learning Adversaries](https://arxiv.org/abs/2609.31643)

**<font color=#1a73e8>作者：</font>** Madhava Gaikwad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A principal who deploys a binary classifier with an abstention option must decide which queries the mechanism abstains on. The right choice depends on the adversary. A gaming adversary already knows the classifier and tries to manipulate features across the boundary, so the principal does best by abstaining on queries close to that boundary. The same boundary-localizing rule is the worst possible choice against a learning adversary who does not know the classifier: each abstention now tells the adversary that the boundary is nearby, which is enough to drive a binary search. We analyze this tension. The two natural defenses, abstaining at a fixed rate and abstaining near the boundary, are Blackwell-incomparable: neither can be simulated by post-processing the other's responses. The number of queries needed to reconstruct the boundary to error $\eps$ is $\tilde\Theta(d/\eps)$ under the first defense and $\Theta(d \log(1/\eps))$ under the second, where $d$ is the VC dimension of the classifier family and $\tilde\Theta$ suppresses factors polylogarithmic in $d$ and $1/\eps$. The first rate is a worst case over query distributions; no reconstruction algorithm can close the gap at the distributions that attain it. We characterize the Pareto frontier between the two defense objectives, and confirm both rates on seven binary-classification tasks spanning tabular, image, and language-model-feature inputs: label-plus-counterfactual access extracts the boundary with up to $200\times$ fewer queries than a published label-only baseline.

---


### 7. [MaD-RL: Matching Distributions for Calibrating LLMs with Reinforcement Learning](https://arxiv.org/abs/2609.31644)

**<font color=#1a73e8>作者：</font>** Sourabh Kulkarni, Ksheeraj Sai Vepuri, Basar Demir 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) is widely used in language-model post-training to maximize rewards assigned to individual model outputs, such as scores from binary verifiers or reward models trained on human feedback. However, applications such as synthetic-data generation, fairness-related constraint satisfaction, and policy exploration require controlling the distribution of outputs across model generations rather than only maximizing expected reward. We propose a general RL-based framework for \textit{Distribution Matching} allowing matching the distribution of a latent categorical attribute of model outputs to a specified target distribution. Empirically, we demonstrate that dominant post-training recipes such as Group Relative Policy Optimization (GRPO) reduce output diversity by concentrating policy probability towards a single mode. Entropy regularization and sampling temperature can improve the spread of the distribution but have constrained effectiveness, limited to apply only in token space and toward uniform distributions. We show that prior work in this area is a specific case of Distribution Matching involving the $L_2$ divergence. We then propose reward functions for other divergences such as KL and Jensen-Shannon and motivate them with theoretical justification. Finally, we demonstrate the effectiveness of our approach on a set of experiments involving mathematical reasoning and programming.

---


### 8. [Energy Vision--Language--Action: A Controlled Multimodal Benchmark for Intent-Conditioned Residential Energy Management](https://arxiv.org/abs/2609.31648)

**<font color=#1a73e8>作者：</font>** Lyes Saad Saoud, Oualid Doukhi, Ehsan Reihani 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models are studied mainly in robotics, where visual observations and language instructions are mapped to physical actions. This paper introduces Energy Vision-Language-Action (EVLA), a controlled multimodal benchmark for intent-conditioned residential energy management. EVLA frames battery scheduling as a multimodal trajectory-prediction problem in which an RGB energy-field representation, a numerical operating state, and a natural-language objective are mapped to a 16-step battery-action trajectory generated by a finite-horizon sampling-based reference generator. Source windows are derived from public residential electrical-load data, while electricity price, battery state of charge, indoor temperature, and time of day are generated benchmark metadata. A hidden operating regime is encoded only through energy-field texture, enabling paired visual changes while the explicit numerical state is fixed. Crossing 439,203 retained base windows with three hidden regimes and five language objectives yields 6,588,045 multimodal instances. An initial study evaluates 36 configurations over three training seeds using fixed subsets of 5,000 training, 500 validation, and 500 test instances. In the MobileNet-family comparison, removing processed language increases trajectory mean-squared error from 0.3856 +/- 0.0039 to 0.8628 +/- 0.0001, whereas removing vision yields 0.3843 +/- 0.0013, comparable to the full model. The results show strong asymmetry in modality use: the processed-language pathway is strongly associated with prediction quality, while the current RGB pathway provides no aggregate error advantage. These results characterize the fixed pilot subset and executed protocol rather than full-benchmark training. EVLA provides a controlled setting for studying how semantic intent and latent context influence residential energy-action prediction.

---


### 9. [PalmLeaf-VQA: A Multi-Script Visual Question Answering Benchmark for Historical Palm-Leaf Manuscript Understanding Across Diverse Regions](https://arxiv.org/abs/2609.31651)

**<font color=#1a73e8>作者：</font>** Nimol Thuon, Jun Du, Panhapin Theang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Historical manuscripts remain largely absent from modern vision-language benchmarks, leaving open how well multimodal large language models (MLLMs) handle culturally diverse, degraded, and non-Latin document images. We introduce \textbf{PalmLeaf-VQA}, a multi-script visual question answering benchmark for historical palm-leaf manuscript understanding across South and Southeast Asian traditions. PalmLeaf-VQA contains \textbf{923 curated manuscript images} and \textbf{7,384 question--answer pairs} from eight collection groups: Balinese, Grantha, Jathakam, Kambaramayanam, Kannada, Khmer, Sundanese, and Tamil. Unlike recognition-oriented resources, the benchmark targets manuscript-aware visual reasoning over preservation-relevant cues, including physical condition, line structure, material and coating, binding holes, margins, symbols, drawings, and localized visual artifacts. We evaluate recent proprietary and open-weight MLLMs under open-answer and constrained-answer prompting and provide fine-grained analysis across collections, question categories, and task types. The strongest evaluated model reaches only \textbf{58.00\% exact-match accuracy} on the held-out test split, revealing substantial limitations in current MLLMs for rare-script, degraded-layout, and preservation-oriented document understanding. PalmLeaf-VQA provides a standardized benchmark for advancing culturally grounded and layout-aware multimodal document analysis.

---


### 10. [Parser, Chunking, and Embedding Interactions in Retrieval-Augmented Generation over Indian Government Regulatory Documents](https://arxiv.org/abs/2609.31660)

**<font color=#1a73e8>作者：</font>** Shubham Kumar Singh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) pipelines are typically assembled from independently-chosen components -- a document parser, a chunking strategy, and an embedding model -- yet these choices are rarely evaluated jointly, and evaluations that do combine them are usually run on a single document or corpus. We present a controlled factorial study of 3 parsers, 3 chunking strategies, and 5 dense embedding models, together with a sparse BM25 baseline, evaluated against 800 question instances, each with one or more required evidence strings, with evidence strings automatically validated against source text and a 10% random sample manually reviewed, across four structurally distinct Indian central-government regulatory documents. We fit linear mixed-effects models with document-query-level random intercepts to the resulting 72,000-row result set, run Holm-corrected paired comparisons between matched dense and sparse configurations, and report clustered bootstrap confidence intervals for all 54 unique retriever configurations. We find that no single retriever family dominates across documents; parser and chunker choice interact significantly; MPNet-base is a consistent underperformer with a severe failure mode on table-derived questions; and the corpus exhibits a near-saturated evidence-preservation ceiling above 98%, indicating that retrieval differences are driven primarily by ranking quality rather than information loss during ingestion. We additionally report embedding-dimension and chunk-size/overlap ablations and an efficiency/quality Pareto analysis. We release our full evaluation harness, corpus manifest, and 800-question benchmark.

---


### 11. [ForensicZoom: Adaptive Visual Inspection with Multimodal LLMs for Industrial-Grade Face Forgery Detection](https://arxiv.org/abs/2609.31661)

**<font color=#1a73e8>作者：</font>** Hang Zhou, Yiming Tang, Kun Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable face forgery detection is critical to the security of online identity verification systems, where missed attacks compromise security and excessive false positives disrupt legitimate users. Specialized forensic detectors achieve strong detection performance but provide limited interpretability, while multimodal large language models (MLLMs) offer strong semantic understanding and interpretable reasoning yet remain substantially weaker for face forgery detection. We argue that a key limitation lies in how visual evidence is acquired: subtle forensic artifacts may be poorly represented at standard resolution, while uniformly processing all cases at higher resolution is computationally inefficient. We therefore introduce ForensicZoom, an industrial-grade MLLM framework for adaptive visual inspection. ForensicZoom first equips a general-purpose MLLM with forensic-aware visual representations and aligns the language model with these features. Its central mechanism, NEED_ZOOM, enables the model to autonomously request magnified views of suspicious regions when the initial evidence is insufficient, turning fixed-pass classification into adaptive multi-round forensic reasoning. The zoom behavior is learned through reward shaping that balances detection accuracy with unnecessary visual inspection, concentrating additional computation on difficult cases. A final attribution optimization stage improves natural-language forensic reports while preserving detection performance. On large-scale industrial identity verification data, ForensicZoom achieves over 97% TPR at 0.1% FPR, substantially outperforming both specialized detectors and existing MLLM-based methods while producing actionable forensic attributions. These results demonstrate that ForensicZoom can provide an effective path toward accurate, interpretable, and scalable MLLM-based face forgery detection.

---


### 12. [LLM-Guided Ontology-Driven Knowledge Graph Construction from Unstructured Text](https://arxiv.org/abs/2609.31663)

**<font color=#1a73e8>作者：</font>** Abdelhadi Belfadel, Maxence Gagnant, Joseph Kattan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ontology-driven knowledge graph construction from industrial text remains challenging due to the domain specificity of documents, the scarcity of annotated resources, and the complexity of ontology engineering workflows. This paper presents and investigates the applicability of an ontology learning pipeline that combines compact open-source Large Language Models (LLMs), reusable prompting strategies, and open knowledge bases to support the extraction, structuring, enrichment, and evaluation of knowledge from textual corpora. The approach is tested and evaluated on a private French corpus of power-grid incident reports, using locally deployable open-source LLMs ranging from 7B to 32B parameters. Starting from unstructured reports, the approach extracts entities and relations, generates RDF triples, constructs related OWL ontology, enriches it using external knowledge sources, assesses the quality of the ontology, and subsequently constructs a populated knowledge graph grounded in the resulting ontology schema. Experiments on 80 manually annotated private reports show that schema-guided prompting significantly improves extraction quality, while quantized models provide an effective trade-off between performance and computational cost. These results demonstrate the feasibility of transforming domain-specific industrial text into ontology-based knowledge graphs using locally deployed open-source LLMs, while supporting the generalization of the extraction process through reusable prompting strategies.

---


### 13. [Language-Augmented Video Action Anticipation: Design Fundamentals, Benchmarks, and Open Challenges](https://arxiv.org/abs/2609.31665)

**<font color=#1a73e8>作者：</font>** Mahsa Mohammadi, Zeyu Fu, Sareh Rowlands  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Action anticipation predicts future human actions from partial video under incomplete context and temporal uncertainty. Recent systems introduce large language models (LLMs), vision-language models (VLMs), or language-derived semantics at different stages, but reported gains are difficult to interpret when task formulation, visual pretraining, supervision, decoder design, and evaluation code change simultaneously. The central contribution of this review is an evidence-aware design map that crosses task regime with the point at which language-derived information intervenes. We characterise task regimes along six axes. These axes organise the literature into five broad task families: single-action, sequence, object-interaction, cross-view, and planning-oriented settings. C1-C3 locate interventions in context construction, goal/intention modelling, and future decoding, while C4 is treated as an adjacent, emerging grounding/executability extension. Unlike a generic processing pipeline, the map links each intervention to an appropriate counterfactual, failure diagnosis, and permissible evidence claim. Supporting contributions include a protocol-level audit of Ego4D-LTA and EPIC-KITCHENS-100, a multidimensional evidence profile, and the Backbone-Aware Comparison and Ablation Protocol (BCAP). The unresolved EK-100 record is treated as a reporting-comparability case study and is not used as a leaderboard. Evidence for LLM benefits, goal ambiguity, and horizon effects is therefore formulated as testable hypotheses requiring matched validation, not as causal conclusions. The accompanying package contains the coded evidence, source locators, protocol metadata, and versioned catalogue used in the review.

---


### 14. [Query-aligned video frame selection for long video understanding](https://arxiv.org/abs/2609.31668)

**<font color=#1a73e8>作者：</font>** Md. Safayet Islam, Dilip Sarkar, Liang Liang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) process multimodal inputs by converting text, images, and videos into token sequences that are subsequently processed by a backbone language model. While MLLMs have achieved excellent performance in understanding the content of individual images, video understanding remains significantly more difficult because videos contain large number of video frames. MLLMs typically process only a subset of these frames, usually ranging from 8 to 64. MLLMs usually sample frames uniformly, regardless of their relevance to the question being answered. To address this limitation, several training-free, model-agnostic methods for selecting question-relevant frames have recently been proposed.
In this work, we introduce a frame-selection method designed specifically for multiple-choice questions. We extend the query text by appending semantic cues derived from the answer choices and employ a direct query-frame alignment scoring mechanism. To the best of our knowledge, our method is the first to directly utilize answer choices as inference-time cues for selecting frames relevant to answering a question. The method first constructs a compact candidate pool by subsampling video frames at a fixed rate. The frames are then scored according to their maximum cosine similarity across all question-answer pairs to identify the most relevant frames for a given query. This approach preserves a fixed token budget while improving the relevance of the visual evidence provided to the downstream MLLM.
We evaluate the effectiveness of our frame-selection method on the MLVU, Video-MME, and LongVideoBench benchmarks using three MLLMs: LLaVA-Mini, Qwen2-VL, and LLaVA-Video. Experimental results demonstrate that answer-aware frame selection generally outperforms uniform sampling and existing training-free frame-selection methods under the same frame budget.

---


### 15. [Active Causal Discovery Benchmark: Evaluating LLM Agents Under Budgeted Interventions](https://arxiv.org/abs/2609.31675)

**<font color=#1a73e8>作者：</font>** Sagar Deb, Devam Shah, Ashwanth Krishnan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce the Active Causal Discovery Benchmark (ACDB), an SCM-grounded environment for evaluating whether LLM agents recover causal graph structure from observations and budget-constrained hard interventions. ACDB pairs a linear-Gaussian world generator with a fixed observe-intervene-submit API and a three-layer scoring contract that separates skeleton recovery, DAG recovery, and intervention efficiency. On the current six-level ladder, PC with a greedy active orientation heuristic is the strongest non-oracle method (directed F1 42.7%, SHD 4.79), ahead of Claude Sonnet 4.6 raw active (31.7%, 7.25) and GPT-5.4 raw active (22.9%, 9.27). The most informative diagnostic is the precision-recall decomposition: PC under-commits with high precision, LLMs over-commit with lower precision, and statistical-tool access often increases abstention rather than useful intervention. A structure-blind random DAG baseline reaches 23.6% directed F1 on this dense v0 ladder; a density probe lowers this floor to 16.9%, motivating the v1 calibration pass. The current results should therefore be read as a benchmark audit and calibration report, not as evidence that current LLMs solve active causal discovery.

---


### 16. [When Keywords Drop but Classifiers Hold: Soft Refusals under KV Cache Compression](https://arxiv.org/abs/2609.31678)

**<font color=#1a73e8>作者：</font>** Kang Chen, Xiuze Zhou, Hong Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> KV cache compression is widely used for long context LLM inference under memory constraints, while deployed systems typically score refusals after generation with keyword filters or learned classifiers. Such monitors are intended to indicate whether a model declined a harmful request under the serving regime actually used. However, it remains unclear whether matched compression that preserves task accuracy also preserves agreement between lightweight lexical monitors and stronger refusal classifiers. We study this with a paired protocol on n=200 harmful prompts with a long filler context: each prompt is answered once under full retention and once under matched eviction after a shared prefill, and the same replies are scored by keyword heuristics, the HarmBench Llama-2-13B classifier, an auxiliary LLM judge, and humans on disagreements. On Qwen2.5-3B, keyword refusal falls from 98.0% to 80.5% (McNemar p~1e-8) while classifier refusal stays near ceiling (99.0%-99.5%) and MMLU accuracy is unchanged (50.0%); human labels predominantly follow the classifier, consistent with soft refusals. The gap is not universal and weakens under short fillers and paired SnapKV, so safety auditing under compression should rely on several judges matched to the serving context rather than on keyword rates alone.

---


### 17. [Toward AI-Assisted Poultry Coccidiosis Diagnosis: Evaluating Gemini and BiomedParse on Eimeria Microscopy Images](https://arxiv.org/abs/2609.31679)

**<font color=#1a73e8>作者：</font>** Ali Alsalama, Ahmed Kubba, Manar Abu Talib  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Coccidiosis caused by Eimeria parasites is a major economic burden in poultry production, and effective control depends on accurate species-level diagnosis. This study evaluates whether a general-purpose multimodal large language model can support such diagnosis. Google Gemini was assessed on 4,225 mi- croscopy images covering the seven fowl-infecting Eimeria species under two prompting conditions, one without candidate labels and one with a predefined class list, and was further tested for pathology-report generation, while BiomedParse was examined for parasite segmentation. Without candidate labels, the model produced broad and taxonomically inconsistent outputs. With candidate labels, overall accuracy reached only 14.9%, with a strong bias toward E. tenella at 74% and no correct classifications for E. acervulina, E. mitis and E. praecox. Generated treatment reports were coherent but unverified, and segmentation was only partial. Current multimodal models are therefore not yet reliable for standalone Eimeria diagnosis without domain-specific fine- tuning and expert validation.

---


### 18. [Autonomous Research Project Management as an Agent Skill: A Case Study in Exact Spectral Spatial Regression](https://arxiv.org/abs/2609.31683)

**<font color=#1a73e8>作者：</font>** Alexander Chen, Jeffrey Meng, Bram Hoex 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work presents an end-to-end demonstration of autonomous machine learning research conducted by an agent skill on consumer hardware. The demonstration evaluates an FFT-based Kernel Ridge Regression (KRR) solver for regular spatial grids using 2005 monthly NOAA Kaplan SST v2 anomaly fields on a $36 \times 72$ grid. This was autonomously executed by DeepSeek V4 Flash, orchestrated by our agent skill suite within DeepSeek Harness (DSH). Experiments were executed on CPU-only hardware (Apple M2 Pro; 78.7 s solver time, 1.57 GB peak RSS). Long-horizon state was decoupled into a file-based epic- and issue-tracking substrate. Across 74 sub-agent sessions, the agent demonstrated closed-loop scientific resilience: routing two failed hypothesis review gates back to literature retrieval, patching bootstrap indexing bugs, and executing with only four discrete human steering events. Finally, we reflect on autonomous research governance, arguing that scientific credibility requires inspectable state, falsifiable review gates, and transparent reporting of negative results, urging the machine learning community to favour agent-accessible structured formats over static PDF manuscripts.

---


### 19. [The Temporal Tug-of-War: Visualizing and Detecting RAG Conflicts in Diffusion Models via Trajectory Variance](https://arxiv.org/abs/2609.31684)

**<font color=#1a73e8>作者：</font>** Sravan Karthick T, Pranav Darshan, Pranav A 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) introduces a specific failure mode in discrete diffusion language models: when retrieved context contradicts parametric knowledge, the iterative denoising process becomes a visible battleground between competing knowledge sources. We identify temporal semantic divergence as an observable for detecting these conflicts and introduce the Trajectory Variance Score (TVS), a simple and interpretable measure of this divergence. TVS computes the mean pairwise cosine distance of answer embeddings across independent stochastic denoising trajectories, capturing the temporal tug of war between parametric and contextual attractors. Requiring as few as two parallel inference runs, TVS is computationally lightweight. Across four diverse datasets (Synthetic, SciQ, PopQA, and CounterFact), a simple Logistic Regression classifier using TVS achieves $70.10\%$ accuracy and $0.7647$ AUROC on LLaDA. On Dream 7B, increasing the number of trajectories from two to five improves accuracy from $63.91\%$ to $69.62\%$. More complex sequential models provide only marginal improvements over the linear classifier. Evaluation across LLaDA and Dream 7B demonstrates that conflict-induced trajectory dynamics and their key properties transfer across distinct diffusion architectures.

---


### 20. [What does FFN compression change downstream? Same-state causal restoration in diffusion language models](https://arxiv.org/abs/2609.31685)

**<font color=#1a73e8>作者：</font>** Shaurya Omar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) enable flexible, parallel generation, but their iterative denoising remains computationally expensive, motivating increasingly aggressive compression. Existing compression objectives largely measure how well compressed computation approximates the original locally, but local error does not reveal which removed computations actually matter to the downstream denoising trajectory. We introduce Same-State Causal Restoration (SSR), which restores the original FFN on the exact current input reached by the compressed model and measures how the resulting trajectory changes. To our knowledge, this is the first direct measurement of the same-current-input closed-loop effect of removed FFN computation in DLM compression. Across LLaDA-8B-Instruct and Dream-v0-Instruct-7B, compressed-side state ranks this downstream effect substantially better than local NMSE at fixed denoising phase, while controlled interventions show that correction structure matters beyond magnitude. Using task-label-free calibration, SSR freezes a single restoration window for held-out inference. Under aggressive LLaDA compression, restoring only four transitions recovers 89.9% of the lost accuracy while retaining an estimated 36.8% whole-model MAC saving and outperforming an equal-budget local-error baseline. Dream further shows that restoring dense behavior and repairing the final task are distinct outcomes.

---


### 21. [Verification of PETSc with CIVL using LLM-generated ACSL contracts and deterministic driver generation](https://arxiv.org/abs/2609.31687)

**<font color=#1a73e8>作者：</font>** Hansol Suh, Jan Hückelheim, Stephen Siegel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Parallel numerical libraries such as PETSc are widely used in science and engineering applications where wrong results can have costly consequences. Despite this, numerical libraries are rarely formally verified. One of the challenges is the need for an expert to hand-write a specification and manually apply a verification tool, often requiring the development of a harness or driver, all of which can contain additional bugs that lead to false positives or false negatives during verification. With recent advancements in large language models (LLMs), it is tempting to generate such drivers and reference models automatically, but one-shot generation based on a simple prompt is brittle and leads to additional unverified code that needs to be audited. In this paper, we present an approach to use LLMs in a limited setting to generate a small, human-certifiable ACSL contract from the function's documentation, combined with a deterministic toolchain that supports a restricted ACSL profile and generates a driver that uses the CIVL verifier to check the implementation against the contract and, when available, an existing reference model. We demonstrate the pipeline end-to-end on three PETSc functions: MatAXPY (reference model already exists), MatAYPX (no reference model, so the certified contract is the sole oracle), and the non-compressing mode of MatFilter (no reference model, with more complex, conditional behavior). With this pipeline, we were able to discover a bug in PETSc's MatAYPX function that was previously undiscovered and had been present in the code since 1997.

---


### 22. [Don't Repeat Yourself: Self-Supervised Fine-Tuning for Coverage](https://arxiv.org/abs/2609.31688)

**<font color=#1a73e8>作者：</font>** Eric Fithian, Kirill Skobelev, X.Y. Han  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In verifiable domains such as math and coding, finding one correct solution among many attempts can matter more than the pass rate of each attempt. Post-training can concentrate large language model outputs around a few modes, while increasing sampling temperature has limited effectiveness. We introduce Don't Repeat Yourself Supervised Fine-Tuning (DRY-SFT), a post-training method that increases output diversity and coverage: the probability of at least one correct solution among many attempts. DRY-SFT has two stages. First, for each problem, sequentially generate K solutions, showing the model all prior attempts and asking for a different solution. Second, fine-tune on each attempt independently, removing prior attempts from the context. The process uses no reward, verifier, or correctness filter. On HumanEval+, MBPP+, and DS-1000, DRY-SFT raises pass@100 by 10.8, 12.5, and 12.4 percentage points, respectively, at a small cost to pass@1. Structural diversity, measured by abstract syntax tree edit distance among passing solutions, rises significantly on all three benchmarks. DRY-SFT also solves 244 of 600 problems that the base model did not solve in the same 200 attempts. Across nine open-weight models, lower structural diversity of the base model significantly predicts larger DRY-SFT gains, indicating that the method is especially effective on more mode-collapsed models.

---


### 23. [Adapting Vision-Language Models for Human-Readable XAI in Industrial Object Detection](https://arxiv.org/abs/2609.31690)

**<font color=#1a73e8>作者：</font>** Sarvenaz Sardari, Freddy Fernandes, Samarth Yelvande 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Explainable Artificial Intelligence (XAI) solutions are essential for building trust in AI technologies and their integration in real manufacturing lines. However, most existing methods are tailored to technical experts, limiting their accessibility to diverse user groups such as blue-collar workers in manufacturing lines who use AI for quality control. In this work, we introduce an XAI interface for object detection in industrial manufacturing based on a fine-tuned vision-language model, designed to generate intuitive explanations for non-expert users. We benchmark existing vision-language models and demonstrate that out-of-the-box models often fall short in delivering clear, context-relevant explanations for non-expert users. To address this, we fine-tune a vision-language model and integrate it into our interface, enabling contextualized, accessible explanations for non-expert users. We demonstrate improvements in explanation clarity, instruction adherence, image groundedness, and contextual awareness over GPT 4o-mini on proprietary and public robotics dataset. This approach advances the accessibility and usability of AI explanations, making them more intuitive and applicable in manufacturing domain.

---


### 24. [Video Captioning in Low-Light Conditions through Efficient Uncertainty-Aware Caption Correction](https://arxiv.org/abs/2609.31697)

**<font color=#1a73e8>作者：</font>** Arefeh Rezaei  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-light conditions can significantly degrade the ability of vision-language models (VLMs) to accurately describe human actions in videos. In this work, I propose an efficient uncertainty-aware representation correction framework for improving captions generated by VideoChat2 under real-world low-light conditions. Instead of fine-tuning the underlying VLM, the proposed framework introduces a lightweight sparse Gaussian process-based error estimation module between the projection layer and the language model to correct the intermediate representation. The correction module learns to estimate the residual between the original projected representation and a verified target representation, which is then adaptively scaled using a newly formulated uncertainty-aware coefficient and added to the original representation. To further improve residual estimation, I introduce a partitioned combined-kernel design. The correction model is trained separately using only 44 samples from the ARID dataset and requires only a small additional computational overhead during inference. The effectiveness of the proposed correction is evaluated through quantitative residual prediction and qualitative analysis of the generated captions. Although VideoChat2 is used in my experiments, the proposed framework is designed to be applicable to other compatible VLM architectures. \textbf{Code Availability: The implementation accompanying this work is publicly available at}:\href{this https URL}{this https URL}

---


### 25. [Modernising the Compressed-Domain Video Captioner: A Controlled Study of SigLIP2 and GPT-2 Substitutions](https://arxiv.org/abs/2609.31700)

**<font color=#1a73e8>作者：</font>** Ashim Nepal, Ashok B.K  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Compressed-domain video captioning avoids full video decoding by operating directly on I-frames, motion vectors and residuals, trading a small amount of accuracy for a large gain in inference speed. CoCap established this pipeline using a CLIP vision encoder and a shallow BERT-style multimodal decoder. Both components predate substantially stronger alternatives. We ask a narrow, controlled question: how much of CoCap's accuracy is limited by these two components, and which of the two is the binding constraint?
We replace the CLIP I-frame encoder with SigLIP2 and the BERT-style decoder with GPT-2, and evaluate three configurations (the original pairing, the encoder substitution alone, and both substitutions together) under identical data, sampling budget and optimisation schedule. All comparisons are made against our own reproduction of CoCap rather than its published numbers, because we train on a 4,999-clip subset of VATEX at a reduced sampling budget; absolute values are therefore not comparable with the original work.
Our reproduction tracks the published result closely: CIDEr and METEOR run slightly above it (54.9 against 52.7; 23.4 against 23.2), BLEU-4 and ROUGE-L slightly below (29.7 against 31.4; 48.9 against 49.4). We attribute the differences to our evaluation subset rather than to any improvement in either direction. We find the two substitutions pull in opposite directions: SigLIP2 alone improves every metric (+4.5 CIDEr), while adding GPT-2 on top erodes that gain, because a pretrained decoder overfits 4,999 clips within two epochs. We additionally report inference latency for each configuration, since speed is the property that motivates compressed-domain captioning in the first place, and an accuracy gain purchased at a latency cost should be reported as such.

---


### 26. [Be Careful Who You Trust: Coordination Dynamics under Corrupted Communication in LLM Multi-Agent Games](https://arxiv.org/abs/2609.31704)

**<font color=#1a73e8>作者：</font>** Xuanyi Liu, Niall Dalton, Hairi Amin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used as interacting agents, but it remains unclear how robust their coordination is when public communication is unreliable. We study this question in iterated $N$-player Stag Hunt games played by homogeneous LLM groups under controlled programmatic action inversion, which changes both the public transcript and the actions used for execution. Across an experimental grid spanning group sizes, coordination thresholds, corruption levels, and seven LLMs, we observe three main patterns. First, honest agents' pre-flip Stag choices decline as corruption increases, but the sharp fall in public success is primarily mechanical. In the focal $N=5,M=3$ setting, pre-flip success remains 78% at 80% corruption, while public success falls to 12%. Second, honest choices are associated with the public history available at decision time, particularly under high corruption. Third, three threshold-style public-report benchmarks yield similar action-match rates to the LLM agents, showing substantial descriptive agreement between LLM decisions and these benchmarks. Overall, our results show that original choices, public actions, and executed outcomes must be separated when evaluating multi-agent robustness, as corrupted communication can severely and predictably degrade mutually beneficial cooperation.

---


### 27. [MDL-Calibrated Significance-Gain Pair Encoding: Replication-Aware Automatic Stopping for Subword Tokenization](https://arxiv.org/abs/2609.31705)

**<font color=#1a73e8>作者：</font>** Azam Nouri  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Byte-Pair Encoding (BPE) constructs subword vocabularies through greedy pair merging, but conventional BPE requires the number of merges or target vocabulary size to be specified externally. Significance-Gain Pair Encoding (SG-BPE) replaces frequency-only selection with a statistical criterion based on how strongly an observed pair exceeds its expected co-occurrence under an independence model.
This paper introduces MDL-Calibrated Significance-Gain Pair Encoding (MDL-SG), a three-stage procedure separating discovery, replication, and utility. Candidate pairs are ranked by Significance-Gain on a discovery partition, tested for replication on a separate partition using an exact one-sided hypergeometric test with per-iteration Benjamini-Hochberg correction, and then evaluated on a utility partition using a Minimum Description Length (MDL) criterion. Merging stops automatically when no replicated candidate yields positive held-out MDL gain.
On WikiText-103, MDL-SG stops at 209, 433, and 847 merges for 120K, 250K, and 500K-character tokenizer-training samples, respectively. At 500K characters, it selects a stored vocabulary of 1,017 tokens without prescribing the vocabulary size in advance. In a compute-matched TinyGPT experiment with identical 2,024,448-parameter models and 500 optimizer updates per language model, MDL-SG achieves validation/test BPC of 3.2612/3.2436, compared with test BPC of 3.2894 for SG-BPE and 3.3493 for frequency BPE. Frequency BPE achieves stronger raw compression, while MDL-SG achieves lower BPC, showing that compression-oriented merge selection and language-model utility need not coincide.

---


### 28. [Can't Find Waldo: Evaluating VLMs' Sensitivity to Image Resolution and Detail Level](https://arxiv.org/abs/2609.31706)

**<font color=#1a73e8>作者：</font>** Alexandra Schild, Gerard de Melo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Language Models (VLMs) have achieved remarkable success across diverse tasks, yet they struggle with high-resolution inputs where critical information resides in small regions or detailed, cluttered scenes. While several approaches address this limitation, a systematic understanding of why models fail at high resolutions is lacking. We introduce a controlled evaluation framework that disentangles resolution-related performance degradation from task difficulty through semantics-preserving transformations. We propose two simple metrics: Area Under the Scaling Curve (AUSC), which quantifies scaling robustness independent of baseline accuracy, and Prediction Variance Score (PVS), which measures resolution-induced prediction instability. Through comprehensive experiments across 5 model families and 5 benchmarks, we identify three primary failure modes: (1) information loss from downsampling at vision token limits, (2) tokenization artifacts from patch boundary shifts and positional encoding fragility under non-standard aspect ratios, and (3) attention dilution as token counts increase. Our analysis reveals that even state-of-the-art models suffer from performance drops when processing high-resolution images, with degradation patterns varying systematically by architectural family. We provide actionable insights for model architecture design and data augmentation strategies to mitigate these limitations.

---


### 29. [Agentic Video Understanding: A Survey](https://arxiv.org/abs/2609.31713)

**<font color=#1a73e8>作者：</font>** Xinyu Deng, Siwen Luo, Daochang Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) become capable of processing increasingly diverse modalities and longer temporal contexts, an emerging line of work is moving beyond fixed video-language inference toward agentic systems that actively decide what information to inspect, retain, verify, and act upon. This survey reviews video understanding agents: systems that use video as the primary information source and solve understanding tasks through adaptive state construction and action selection. We first formalize an agent loop for video understanding, then address a central question: why do agents matter for video understanding? To answer this, we organize the literature through a challenge-to-design taxonomy, linking context bottlenecks to hierarchical evidence memory, evidence sparsity to active evidence acquisition, temporal causality to state and process tracking, and multimodal ambiguity to role-specialized coordination. We further review state space paradigms, learning paradigms, supervision signals, benchmarks, and evaluation protocols. Finally, we identify open directions toward agentic-native temporal modeling and video-native agents. Project page: this https URL

---


### 30. [OmniFysics-Captioner Technical Report: Grounding Omni-Modal Understanding in the Physical World for Better Captioning](https://arxiv.org/abs/2609.31714)

**<font color=#1a73e8>作者：</font>** Kaixiang Qiu, Minghao Han, Keliang Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Building omni-modal models with physical intelligence requires fine-grained supervision that captures physical evidence such as contact, support, deformation, and state transitions. However, existing omni-modal captioners primarily model general audiovisual semantics and often overlook transient or spatially localized physical evidence. We present a unified framework for physics-aware audiovisual captioning spanning data construction, training, and evaluation. Firstly, we build a data construction pipeline that identifies physics-rich clips and leverages OmniFysics-Agent to coordinate audio, visual, and physical-perception tools for collecting spatiotemporally aligned and traceable cross-modal evidence; within the Agent, a physical perception model (PPM) fine-tuned on approximately 2M image-level samples serves as a dedicated tool for extracting object-interaction and state-change cues. Secondly, we build the Daily-Physics 50K dataset and introduce the evidence-driven OmniPhysCap (OPC) benchmark to evaluate the recovery of physical and cross-modal evidence from generated captions. Finally, we train OmniFysics-Captioner from the resulting data. Our Captioner matches Gemini 3.1 Pro on audiovisual captioning, achieves state-of-the-art results on multiple video-captioning benchmarks, and substantially outperforms other open-source models. Ablations show that PPM evidence improves physical coverage and produces finer-grained, more reliable cross-modal descriptions.

---


### 31. [PanoFuse: Panorama-Enhanced Vision-Language-Action Learning with Decoupled Semantic-Geometric Routing](https://arxiv.org/abs/2609.31717)

**<font color=#1a73e8>作者：</font>** Peng Xu, Haoran Lin, Wanjun Jia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) policies have shown promising performance in language-conditioned robotic manipulation. However, most existing VLA systems rely on conventional perspective cameras with limited fields of view, often missing global scene context and leading to unreliable manipulation under visual occlusions, distractors, and unseen environments. In this work, we propose PanoFuse, a panorama-enhanced VLA framework that complements local manipulation observations with global panoramic perception. PanoFuse introduces a dedicated panoramic branch that leverages a pretrained panoramic foundation model to extract complementary semantic and geometric representations from omnidirectional observations. Rather than directly mixing these heterogeneous features, we introduce Decoupled Semantic-Geometric Routing (DSGR), which maintains semantic and geometric representations as separate context streams and selectively routes both to downstream state and action representations through structured block-wise attention. This design provides the action expert with global spatial context while preserving task-relevant semantic information from the pretrained VLA backbone. We further develop a synchronized data collection pipeline and construct a new real-world manipulation dataset containing panoramic RGB observations, wrist-view images, language instructions, robot states, and actions. Across seven evaluation settings, PanoFuse achieves an average success rate of 52.9%, outperforming the evaluated baselines and achieving consistent gains under novel-object, unseen-background, and distractor-rich settings. Code and data will be released publicly at this https URL.

---


### 32. [The Ongiini-Eval-OW Benchmark: A Concept Paper for the Planned Benchmarking of Machine Translation and Large Language Models on Oshindonga and Oshikwanyama](https://arxiv.org/abs/2609.31727)

**<font color=#1a73e8>作者：</font>** Sebastian Küpers  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Oshiwambo -- a cluster of mutually intelligible Bantu languages spoken by over a million people across northern Namibia and southern Angola, and the home language of roughly half of Namibian households -- has, to our knowledge, no published machine-translation evaluation benchmark. Major commercial services (Google Translate, DeepL, Microsoft Translator), open multilingual MT models (NLLB-200, MADLAD-400), and the open Masakhane checkpoint collection all lack coverage of either standardised dialect, Oshindonga or Oshikwanyama. We announce Ongiini-Eval-OW, a planned 600-item English-Oshindonga and English-Oshikwanyama benchmark with native-speaker references from two independent translators, a 30-item inter-translator agreement set, an 11-tag phenomenon-tagged stratification (at least 30 items per tag), a deterministic 30% blind split, and a reproducible scoring protocol over chrF++, BLEU, and COMET-22, supplemented by a 50-item human-evaluation round. We document the empirical coverage gap, the dataset composition, the launch-leaderboard model matrix across American, European, and Chinese frontier and open-weight systems, and the contribution pipeline. The dataset is targeted for first public release in Q4 2026; this v1.0 concept paper announces the design and the call for participation. Data and code will be released under CC-BY-4.0 and MIT respectively.

---


### 33. [When Retrieval Hurts: Measuring and Explaining Retrieval-Induced Hallucination in Chest X-ray Report Generation](https://arxiv.org/abs/2609.31733)

**<font color=#1a73e8>作者：</font>** Emmanuel Idoko, Abdusshakur Olabisi, Shiloh Oni 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation is an attractive way to improve chest X-ray reporting, because reports from similar prior studies supply clinical context a general vision-language model lacks. We show the same mechanism is a reliable source of clinical error. Over 100 MIMIC-CXR studies with a frozen LLaVA-1.5 generator and BioMedCLIP retrieval, CheXbert clinical F1 doubles under relevant retrieval (0.201 to 0.402) and collapses to 0.043 under clinically mismatched retrieval, a fifth of the image-only score; the retrieval-induced hallucination rate, counting only unsupported findings traceable to retrieved evidence, rises from 0.00 to 0.76 and 0.98. To show this is not an artefact of evidence-set coverage, we introduce a coincidental-overlap control that scores image-only generations against evidence they never saw, placing the chance base rate at 0.18, four to five times below the observed rates. The generator does not merely acquire findings, it transcribes text: 95% of reports produced under relevant retrieval contain an eight-word span occurring verbatim in the retrieved evidence but absent from the reference, against 0% without retrieval. We then explain the mechanism: a normal chest X-ray retrieves at least one abnormal precedent in 24 of 28 cases, because medical image-embedding similarity is dominated by anatomy and acquisition rather than by the presence of disease. This has a direct design consequence. Retrieval similarity does not predict harm (RIH rates 0.80/0.80/0.60/0.84 across similarity quartiles), so relevance gates conditioned on embedding similarity cannot work; gating on predicted pathology agreement removes 61% of unsupported evidence at no cost to useful coverage. We argue that retrieval-augmented clinical systems must be evaluated under retrieval failure, not only under retrieval success.

---


### 34. [VisionPsy-Nano: Improving Accuracy, Efficiency, and Reliability in On-Device Vision-Language Models](https://arxiv.org/abs/2609.31746)

**<font color=#1a73e8>作者：</font>** Khurram Azeem Hashmi, Mohammadreza Zolfaghari, Changdae Park 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sub-billion-parameter Vision-Language Models are increasingly viable for on-device deployment, yet compact model size alone does not guarantee usability. On a phone, such a model can still require more than two minutes to produce its first token. On-device usability depends on three axes: accuracy, efficiency, and behavioral reliability; standard benchmarks miss the third, with answers too short to expose doom loops and prompts too benign to probe adversarial safety. We introduce a diagnosis-driven post-training recipe in which a teacher VLM stress-tests the student, uncovers failure modes beyond human priors, and converts them into targeted supervision and preference alignment, supplementing generic data scaling with failure-driven optimization. Coupled with two visual-token policies, the recipe yields two accuracy-efficiency variants with improved behavioral reliability. \textbf{\NanoFull} attains a 62.3 normalized average over 17 benchmarks, the highest among openly released $\sim$0.5B models, +7.4 over its base at identical architecture and token budget, with doom-loop rates at or below the strongest baseline's. \textbf{\FlashFull} retains 61.4 while cutting warm time-to-first-token on a Pixel 9 from 138\,s to 6.1\,s (23$\times$). By jointly addressing all three axes, we move compact VLMs toward practical on-device usability.

---


### 35. [The Earth in One Gaze: Training-Free Active Focus for UHR Remote Sensing Understanding](https://arxiv.org/abs/2609.31747)

**<font color=#1a73e8>作者：</font>** Yao Zhang, Pengyu Dai, Wei Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) must balance local detail against scene context when interpreting ultra-high-resolution (UHR) remote sensing (RS) imagery within a limited visual-input budget. Existing selection-based methods either prune tokens and select patches through relevance scoring, or crop actively through repeated inspection. Neither strategy directly redistributes pixels within a continuous full-scene view: the first retains selected tokens or patches, and the second re-encodes a crop detached from its surroundings. Our pilot study finds that a frozen MLLM already produces useful question-guided spatial requests, yet crop-based inspection of the selected regions does not consistently improve its answers. We therefore formulate UHR understanding as a question of where to spend a fixed pixel budget. Based on this, we introduce GazeEarth, a simple-yet-effective training-free framework that couples question-guided region selection with full-scene foveated observation. The MLLM selects evidence cells from an indexed overview; a deterministic, topology-preserving warp resamples the original image onto a fixed-size canvas, enlarging their shared neighborhood while compressing the periphery; the same frozen model answers from this focused view, using at most two MLLM calls and no external selector or iterative search. Across three UHR remote sensing benchmarks and four frozen backbones, GazeEarth improves benchmark-averaged accuracy by 4.6 to 9.4 percentage points over direct answering and 3.4 to 4.3 over overview answering, outperforming task-trained methods. Our analyses show that existing MLLMs can guide where to look in UHR images on their own, and that what they can infer from the selected evidence depends on how that evidence is presented.

---


### 36. [EgoTSR++: Egocentric Spatiotemporal Reasoning for Task Progress Understanding](https://arxiv.org/abs/2609.31751)

**<font color=#1a73e8>作者：</font>** Xiaoda Yang, Can Wang, Yuxiang Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have advanced rapidly in static visual understanding, yet remain unreliable when judging how an egocentric task is progressing. Given a task instruction and two visual observations, a model should determine which state is closer to the goal by analyzing task-relevant object configurations and spatial relations, rather than relying on timestamps or presentation order. This distinction is critical in manipulation, where retries, corrective actions, and temporary regressions make progress inherently non-monotonic. We introduce EgoTSR, a unified framework for diagnosing and improving order-robust task-progress understanding. First, SpatialLogic-Bench evaluates each physical state pair in both original and order-swapped presentations across short- and long-horizon settings, exposing whether a model follows task-state evidence or chronological shortcuts. Second, our data construction pipeline converts successful, approximately monotonic manipulation and first-person trajectories into bidirectional supervision; LongTag further preserves intermediate subtask structure for long-horizon comparison, while failure-aware data extend learning to regressions and recoveries. Third, a progressive CoT-to-Tag curriculum first supervises evidence-grounded interpretation of task-relevant state changes and then consolidates the comparison rule through scalable label-only training. Experiments reveal substantial input-order bias in representative VLMs. EgoTSR achieves 92.4% long-horizon accuracy with a 0.1-point forward-inverse Gap. Failure-aware supervision further improves accuracy on non-monotonic trajectories by 11.8 points and Recovery Accuracy by 11.2 points, while maintaining broad visual and spatial capabilities. These results establish goal-conditioned state comparison as an explicit formulation of egocentric spatiotemporal reasoning for task-progress understanding.

---


### 37. [Witeness Overlap: Directional Provenance Inside Open-Weight Model Families](https://arxiv.org/abs/2609.31784)

**<font color=#1a73e8>作者：</font>** Siyuan Li, Haoxuan Zeng, Xin Luo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Open-weight models are often released, fine-tuned, aligned, merged, and re-released, making provenance audits ask not only whether checkpoints are related, but also which checkpoint came first. Many existing model-provenance methods are designed for a base-known audit setting: given a victim or source model, they test whether a suspect model is related to it. Although these audits are framed as source-to-suspect tests, their underlying evidence is often symmetric, relying on representation similarity, weight similarity, behavioral fingerprints, or correlation statistics. Symmetric pairwise comparisons can detect relatedness, but they cannot by themselves orient relationship between checkpoints A and B. We therefore introduce a local geometric comparison: instead of comparing two checkpoints directly, we add a third same-family checkpoint as a witness and compare the geometry around each candidate endpoint. Direction is inferred by asking which candidate behaves more like a branching parent. Motivated by this idea, and by the empirically observed asymmetry between parent-anchored and child-anchored witness-overlap distributions, we propose Witness Overlap, a prompt-free, training-free white-box test for directional provenance. On 176 LLM checkpoints from 16 families, our one-witness test orients 95.3\% of parent-child decisions using Frobenius cosine. We further evaluate root identification, sibling discrimination, generalizations to VLM and diffusion families, and chain-structured ordering. The signal is robust to weight noise and sparse pruning, with a proposed SVD weight reduction variant showing greater robustness than Frobenius cosine.

---


### 38. [SelfCue: Making a 3D CT Report Generator Say What It Already Knows](https://arxiv.org/abs/2609.31788)

**<font color=#1a73e8>作者：</font>** Renjie Liang, Yang Yang, Jinqian Pan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Progress in 3D CT report generation is usually sought in increasingly sophisticated architectures and larger pools of training data. We find instead that a 3D CT report generator already holds what its report leaves out, and loses it when the hidden state becomes tokens. Over the 18 CT-RATE abnormalities, this hidden-to-report surfacing gap is reflected by a drop in macro AUROC from 0.848 in the hidden states to 0.739 in the generated report. We propose SelfCue based on contrastive decoding. It promotes what the hidden state already supports and suppresses what it does not. It raises clinical efficacy F1 to 0.481 and the LLM-judged GREEN score to 0.510. Distilling that behaviour into the weights gives SelfCue-KD, a student that keeps most of the gain, needs nothing extra at inference, and drops into any pipeline already serving the baseline. Code is available at this https URL.

---


### 39. [CP-Agent: A Harness-Engineered Agent for Crystal Plasticity Simulation Workflows](https://arxiv.org/abs/2609.31790)

**<font color=#1a73e8>作者：</font>** Samuel Onimpa Alfred, Abhishek Kumar, Veera Sundararaghavan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Crystal plasticity (CP) simulations predict the mechanical behavior of polycrystalline metals, yet their routine use is hindered by the manual effort of configuring heterogeneous tools, orchestrating multi-step data pipelines, and calibrating constitutive parameters against experiments. These bottlenecks impede productivity in systematic parameter studies, motivating interest in automated workflows. This study presents CP-Agent, a harness-engineered LLM-based agent that autonomously executes complete CP modeling workflows from natural-language tasks. Operating under the ReAct paradigm, the agent reasons about tool selection and sequencing while delegating numerical search to established optimizers. The harness comprises a minimal system prompt, typed tool definitions, a dispatcher, and a safety-bounded iteration loop, encoding domain knowledge through tool schemas rather than hard-coded logic. CP-Agent is demonstrated on four case studies: calibrating four slip parameters of additively manufactured stainless steel 316L against tensile data; validating the workflow against published copper benchmarks, reproducing stress-strain and texture evolution; recovering the initial crystallographic texture of copper, where the agent correctly identifies a diffuse initial texture; and reproducing the multi-pass rolling texture evolution of a Mg-Zn-Ca alloy, where the agent chains five deformation passes and recovers the experimentally observed weakened, split basal texture. In all cases, the agent inferred the correct execution sequence from the task statement, robustly across repeated runs, and delivered physically interpretable results. This work establishes harness engineering as a systematic approach to automating CP modeling workflows while maintaining physical interpretability and auditability through visible reasoning traces.

---


### 40. [ConflictVLA-Bench: Benchmarking Behavioral Responses of Vision-Language-Action Models to Premise Conflicts](https://arxiv.org/abs/2609.31792)

**<font color=#1a73e8>作者：</font>** Liyu Hou, Yuan Wu, Yi Chang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Vision-Language-Action (VLA) models perform strongly on manipulation tasks, their responses to invalid task premises remain underexplored. Existing evaluations of premise conflicts often focus on terminal task outcomes, yet task failure alone cannot distinguish behavioral disengagement from continued pursuit followed by an execution error. We call the latter pattern Failed Persistence. To study this phenomenon, we introduce ConflictVLA-Bench, which pairs conflict rollouts with premise-consistent reference rollouts and evaluates both outcomes and execution processes. Built on LIBERO, the benchmark contains 2,826 prompt-conditioned conflict tasks spanning four conflict families, four structural configurations, and two prompt conditions. Across all eight VLAs, invalid premises reduce original goal completion by at least 17.3 percentage points, with the reduction reaching 56.2 percentage points for OpenVLA. Crucially, even when models succeed on premise-consistent tasks and fail on their matched conflict tasks, they often continue to approach the original targets, retain early trajectory structure, and show limited action magnitude suppression. Failed Persistence therefore recurs across the evaluated models. Explicit premise checking does not consistently produce selective and coordinated behavioral changes. These findings show that terminal failure alone establishes neither behavioral disengagement nor refusal and that outcomes alone are insufficient for VLA evaluation. Experimental data and additional details are available on the project page: this https URL

---


### 41. [Same Probe, Different Numbers: Are Activation Probes Robust to Inference-Time Numerical Non-Determinism?](https://arxiv.org/abs/2609.31796)

**<font color=#1a73e8>作者：</font>** Alizishaan Khatri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation probes are increasingly used to monitor LLMs in deployment. A probe is typically trained under one inference configuration, then used under whatever batch size and numerical precision the serving stack uses. Because common GPU kernels are not batch-invariant and floating-point formats round differently, the activations seen at deployment are not the ones the probe was trained on. We measure what that costs for Llama-3.1-8B, Qwen3-8B and Gemma-3-4B across batch sizes 4, 8 and 16 and float32, bfloat16 and float16, training 768 probes on one configuration, evaluating each on every other, and comparing verdicts example by example. Probes are stable, but aggregate accuracy is the wrong instrument for showing it: it understates how many verdicts change by a factor of two to nine. At the prompt, accuracy never moves by more than 0.47 percentage points across 1,392 transfers and only 0.076% of verdicts change; under float32 with only the batch size varied, none of 201,960 verdicts change. During decoding the flip rate rises to 2.8%, but rows whose realised tokens matched flip in only 0.12-0.15% of cases, while rows whose tokens diverged flip in 12.9%: the cause is the text, not the arithmetic. A bfloat16 batch-size change flips the first generated token for 2.1% of rows and leaves 25% on different tokens by token 20. Flips are symmetric, Cohen's kappa stays above 0.94, and AUROC moves by at most 0.05 points. Underneath, activations move about as much as the format's rounding: a bfloat16 batch-size change perturbs them by a median relative L2 of 1e-2, roughly 8x the float16 figure. Probes absorb this; the model's own next-token argmax does not. Robustness evaluations of activation monitors should report per-example agreement rather than aggregate accuracy, separate representational noise from input change, and state the serving configuration.

---


### 42. [seq2cause: One Autoregressive Backbone, Four Causal Discovery Tasks in Event Sequences](https://arxiv.org/abs/2609.31801)

**<font color=#1a73e8>作者：</font>** Hugo Math  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Complex systems such as vehicles, patients, or genomes emit discrete event sequences whose operative question is causal, not predictive: which events cause which other events, and which cause higher-level outcomes such as failures or diseases? This question decomposes along two axes -- dependency type (event $\to$ event vs.\ event $\to$ outcome) and causal scope (single sequence vs.\ population) -- yielding four structurally distinct regimes with different identifiability conditions. No existing method addresses more than one, because all assume multi-stream structure with low vocabulary, and none scales beyond a few hundred event types.
We present \textsc{Seq2Cause}, a unified framework that resolves all four regimes through a single shared primitive: a pretrained autoregressive model repurposed as an amortized conditional independence testing engine requiring no task-specific retraining. We establish a prediction--causality duality: the model's excess cross-entropy simultaneously bounds causal identification error across all four regimes, so that every improvement in next-token prediction tightens causal guarantees for free.
On nonlinear SCMs (vocabularies up to $8{,}000$ types) and real-world vehicle diagnostic logs ($29$K event types, $474$ failure outcomes), \textsc{Seq2Cause} is the first method to populate all four regimes at scale with a single frozen backbone. Existing methods are either inapplicable, inaccurate, or computationally intractable in this setting.

---


### 43. [DriveHierarchy: A Benchmark for Diagnosing VLM Driving Capabilities from Open-Loop Understanding to Closed-Loop Execution](https://arxiv.org/abs/2609.31814)

**<font color=#1a73e8>作者：</font>** Chengkai Xu, Jiaqi Liu, Yicheng Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating VLM-based autonomous driving remains difficult because driving competence is composite, where a capable system must ground traffic participants and hazards, integrate context across views and time, reason about future evolution, and act appropriately under closed-loop interaction. Existing benchmarks usually assess either open-loop understanding or closed-loop driving but provide limited structure for explaining how these abilities are organized, how they relate, and how they may inform model diagnosis and improvement. We present \textsc{DriveHierarchy}, a hierarchical benchmark that organizes VLM-based autonomous driving into four ranks, spanning perceptual grounding, contextual memory, mental reasoning, and closed-loop execution. To instantiate this hierarchy, we integrate multiple open-source autonomous-driving datasets into a unified open-loop benchmark with 76,798 question-answer pairs over 84,279 frames and develop a closed-loop simulation platform with interactive scenario construction on a real-world road network, from which 100 driving scenarios are curated for embodied evaluation. Experiments on 15 VLMs show that \textsc{DriveHierarchy} captures structured but non-redundant capability variation, relates open-loop understanding to closed-loop driving, and provides a practical basis for diagnosis and benchmark-guided optimization. \textsc{DriveHierarchy} therefore serves as a unified framework for evaluating and improving VLM-based autonomous driving systems. An anonymized project has been released on this https URL

---


### 44. [SynDORBench: Evaluating LVLM Perceptual Robustness Under Physically Constrained Visibility Conditions](https://arxiv.org/abs/2609.31823)

**<font color=#1a73e8>作者：</font>** Jeremy Stephen Gabriel Yee, Zhengkui Wang, Zhiyuan Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) have demonstrated remarkable performance on multimodal reasoning benchmarks, yet their perceptual reliability under physically constrained imaging conditions remains poorly understood. Existing evaluations predominantly assume ideal visual inputs and therefore fail to characterize how camera distance, illumination, viewpoint, and pixel density fundamentally affect semantic recoverability. We introduce SynDORBench, the first physically grounded benchmark for evaluating LVLM perceptual robustness under DORI-calibrated conditions aligned with human visual capability standards. SynDORBench comprises over 54k question--answer pairs generated through a controllable synthetic pipeline that systematically varies viewing distance, lighting, camera geometry, and action pose according to physically interpretable pixel-density regimes. To support scalable low-visibility supervision, we further propose a discernibility annotation framework that propagates human perceptual labels using mask-conditioned statistical features and ensemble learning. We evaluate 16 open-source LVLMs, a commercial LVLM baseline, and YOLO11x across human-presence classification and action recognition tasks under progressively degraded visibility conditions. Our results reveal that perceptual failure in LVLMs is strongly governed by pixel density and physical imaging constraints rather than model scale alone. Surprisingly, several compact open-source LVLMs outperform larger commercial baselines and substantially exceed YOLO11x robustness under long-range and low-light conditions. SynDORBench establishes a new benchmark paradigm for physically grounded multimodal evaluation, enabling systematic analysis of LVLM reliability under real-world perceptual constraints and direct comparison against human visibility thresholds.

---


### 45. [Omni-IO Skills: Harnessing Your Agent Omni-Native](https://arxiv.org/abs/2609.31847)

**<font color=#1a73e8>作者：</font>** Yanlin Li, Mingyang Hao, Shengqiong Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> General-purpose agents can plan, reason, and act over long horizons, yet their production capabilities remain fragmented across text, images, audio, video, documents, 3D assets, and code. Extending a foundation model to additional modalities ties capability growth to costly model updates, while assembling specialist models and tools leaves unresolved how procedures, dependencies, intermediate assets, and cross-turn revisions should be coordinated. We present Omni-IO Skills, a plug-and-play Agent Harness that makes existing agents omni-native through hierarchical Skills, a standardized multimodal execution interface, dependency-aware orchestration, and a persistent Asset Registry. Multi-asset workflows are represented as Declare Execution Graphs, which schedule independent operations concurrently and register successful outputs for downstream and cross-turn reuse across replaceable execution backends. Its 27 Skills cover 38 representative tasks spanning seven artifact modalities and four capability families: understanding, generation, reasoning, and retrieval. On UniM-90, the harness raises the input-support rates of GPT-5.6 Sol and Claude Sonnet 5 from 40.00% and 38.89% to 100%, while increasing relative Semantic--Quality Coupled Score from 26.99 to 74.94 and from 27.82 to 77.78, respectively; Strict Structure Score reaches 100.00 and 99.78. These results establish harness-level capability composition as a practical route to broad, evolvable Omni systems without changing the host agent's reasoning core.

---


### 46. [LLM Judge Validation Under Sparse Overlap: From Inference to Design](https://arxiv.org/abs/2609.31857)

**<font color=#1a73e8>作者：</font>** Junxuan Li, Arko Mukherjee, Soumyabrata Pal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Validating an LLM-as-a-judge requires estimating its agreement with humans, yet annotation budgets rarely allow every item to be multiply labeled. We prove that this \emph{overlap sparsity} is the first-order determinant of wrong deployment decisions: at 5\% pairwise overlap, wrong-decision rates reach 25\% and the probability of selecting the wrong best judge among ten candidates is 65\%. The two actionable levers are overlap \emph{quantity} and \emph{allocation}. For quantity, we derive a minimum-overlap formula showing $\rho \geq 0.25$ suffices for non-borderline judges while borderline cases remain fundamentally hard. For allocation, a zero-cost stratified scheme halves false-rejection rates relative to random sampling when strata are informative. We validate on 10 LLM judges across four evaluation matrices spanning visual assessment, causal reasoning, and summarization.

---


### 47. [IndustryLLM: Failure-Driven LLM Training for Industrial Procurement](https://arxiv.org/abs/2609.31871)

**<font color=#1a73e8>作者：</font>** Liang Ding, Zhiang Xu, Yuyang Sheng 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industrial procurement requires language models to bridge informal buyer jargon, sparse marketplace attributes, and authoritative engineering standards under strict safety tolerances. We present IndustryLLM, an open-weight industrial language model trained from Qwen3.5-35B-A3B-Base (35B total parameters with ~3B activated per token, with the vision encoder frozen). Rather than relying on generic text scaling, we introduce a failure-driven adaptation recipe spanning continued pre-training (CPT) and supervised fine-tuning (SFT). CPT leverages a curated ~100B-token corpus integrating 5B tokens of national standards (e.g., GB/T) and technical archives, 10B tokens of de-identified real-world industrial transaction and inquiry records, and 60B tokens of general replay. To overcome register mismatch and factual brittleness, we systematically reconstruct an estimated 20B-token domain subset via multi-register rewriting across 10 genres and 8 writing styles, confidence-routed minimal factual editing, and error-targeted QA synthesis (resolving colloquial typos like '42-luo-mu' -> 42CrMo, expanding ambiguous codes like '16674' -> GB/T 16674, and clarifying conflicting dimensional specs). For downstream deployment, we formalize an evidence-gated constraint-evaluation interface enforcing three-valued logic where unverified product evidence remains unknown rather than satisfied. Offline evaluations demonstrate consistent gains on procurement-query structuring (+2.97 percentage points in exact match, 95% CI [2.11, 3.86] in No-Think mode), while randomized online A/B experiments in production yield substantial improvements (+4.25% GMV, +8.3% satisfied inquiries) alongside a latency reduction from 6-7 s to 1.5 s. Model weights and configs are released at this https URL.

---


### 48. [CueKFS: Agentic Cue-Driven Keyframe Selection for Long Video Understanding](https://arxiv.org/abs/2609.31873)

**<font color=#1a73e8>作者：</font>** Weitai Kang, Hanieh Deilamsalehy, Yumo Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Keyframe selection (KFS) has long produced compact video summaries for browsing and retrieval, and representative frames for thumbnails. More recently, when conditioned on a question, KFS provides an alternative to uniform sampling for long-video question answering by selecting frames that are more relevant to the question. Most methods rank frames by similarity to the question. Yet a relevant frame may score poorly when the question combines subjects or moments that no single frame shows, or requires implicit information absent from its wording. Other methods try to break down the question into subqueries, but suffer from inaccurate decomposition due to their static initial context. Therefore, we propose CueKFS, a training-free method that reformulates question--frame matching as comparing frames against a set of dynamically generated visual cues. From an initial set of salient frames, we decompose the question into cues. Each cue concurrently probes the video to navigate to its own evidence. A reasoning VLM then agentically revises the cue set against its evidence to re-explore the video. CueKFS then allocates the budget across the surviving cues. Across three benchmarks, CueKFS establishes state-of-the-art results in all 27 evaluated settings with available prior results, achieving budget-averaged gains of up to +4.54% over the previous baseline and a median of only two VLM calls. We further provide a detailed behavioral analysis of CueKFS, showing that agentic cue refinement drives active re-exploration of the video, yielding relative similarity gains of up to 92% over the initial context.

---


### 49. [COUNTERMEM: World-Model Verified Counter-Factual Memory for Language Agents](https://arxiv.org/abs/2609.31874)

**<font color=#1a73e8>作者：</font>** Hongji Pu, Ruixiang Tang, Yongfeng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing agent memory frameworks mainly create memory through an agent's interaction with the factual world, e.g., remembering feedback from actions taken to improve performance on future tasks. However, these frameworks seldom ask the "what if" question during memory construction: what if a different action had been taken, would the feedback have changed, and how could this feedback become useful memory? Obtaining such feedback directly in an active environment can be expensive and can alter the state needed for comparison. In this work, we introduce COUNTERMEM, a reinforcement-learning framework for constructing and using verified counterfactual memory across tasks. After a failed action, COUNTERMEM evaluates local alternatives from a copy or reset of the original state using executable world models, such as tests, proof checkers, and solvers. It stores improvements with the original and corrected actions, checked outcomes, and conditions for reuse. A learned memory-use policy selects a retrieved record or skips memory to balance task success and interaction cost, while the base LLM remains fixed. Both memory and policy are frozen during held-out evaluation. We evaluate COUNTERMEM on 12 benchmark settings across six domains. With gpt-oss-120b, COUNTERMEM improves both ReAct and Reflexion on all 12 benchmarks across six domains, averaging a gain of 12.6 percentage points over their unaugmented versions. In the four-domain comparison across two backbones, task-run tokens decrease by 7.7-42.0%, excluding offline selector-training costs. Further analyses show that removing verification or persistent storage weakens the gains, while applying verified corrections to unsuitable decisions can reverse them. Code will be released upon acceptance.

---


### 50. [Agents Can Use Base Models to Evade AI Detection](https://arxiv.org/abs/2609.31876)

**<font color=#1a73e8>作者：</font>** Bhuwan Dhingra, Danish Pruthi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We show that coding agents equipped with a base language model can successfully assemble responses from its samples to evade detection. Base models have been shown to evade commercial detectors, however, prior "humanization" techniques rely on using these models to paraphrase AI outputs over several iterations, which invariably results in semantic drift. In contrast, equipping coding agents to directly orchestrate the writing process by stitching text samples from a base model allows it to produce outputs that are coherent, task-specific and generally high quality. We find that Claude Opus 5 operating in a Claude Code harness effectively orchestrates a local 32B parameter OLMo-2 base LM and sacrifices little task accuracy across benchmarks spanning creative writing, factual grounding, health QA and instruction following, while using up to 90% base LM tokens. Responses constructed in this manner reduce the effectiveness of both post-hoc detectors (Pangram v4 detection rate drops from 77% to 24%) and soft watermarking applied a priori to the agent's generations (down to a simulated 10% detection at low FPR). While effective, this evasion requires a significantly larger number of input and output tokens from the agent, increasing the dollar cost per query up to 30x at API-pricing. Overall, this work demonstrates the effectiveness of a new class of adversarial attacks against AI text detection, and urges post-hoc detection providers to include outputs of base models in their training.

---


> [!TIP]
> 当前位于：**1-50**（第 1/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
