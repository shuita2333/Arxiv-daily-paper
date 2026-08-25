# 🧠 大模型相关研究 | 2026年08月26日

> 本类共 **363** 篇论文：已确认 **347** 篇，待复核 **16** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-363](./part-08.md)

---

### 51. [From Association to Causation: Improving Retrieval Precision of Retrieval-Augmented Generation via Causal Relations and an Attention Mechanism](https://arxiv.org/abs/2608.21702)

**<font color=#1a73e8>作者：</font>** Jing Liu, Yongxing Qi, Muchen Jiang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) grounds LLM generation on retrieved documents, but the standard terminal retrieval stage--dense-vector similarity, optionally followed by reranking--often returns documents that share keywords with the query without containing the needed information, a failure mode that grows with the knowledge base. We trace it to a conceptual gap: similarity captures only associational relations, whereas the documents that matter are linked to the query causally. We model the terminal retrieval stage with a causal graph grounded in Reichenbach's common cause principle: the keywords shared by the query and a retrieved document form a latent common cause A, and the document's residual keywords form a latent set B linking the document to the ideal output. Since a retrieved document is a collider (A -> d <- B), retrieval itself opens an associational path between the query and B, which licenses a training-free, attention-style re-scoring rule: the cosine similarity between the query embedding and the weighted centroid embedding of B. Unlike causality-enhanced RAG variants that model causal relations inside the knowledge content, our graph models the causal structure of the retrieval process itself. On a real 471-document enterprise knowledge base, the method promotes a relevant guideline from rank 6 to the top 3; on a controlled diagnostic corpus reproducing the keyword-stuffing regime, it improves the mean target rank from 2.88 to 1.25, while a trained cross-encoder reranker barely helps (2.63). Conversely, on three BEIR benchmarks the score underperforms the similarity baseline, delineating the applicability boundary: the method guards the keyword-stuffing regime of growing proprietary knowledge bases and complements neural rerankers; a corpus-level calibration gate selects the correct regime with >= 95% reliability. A fully local testbed demonstrates deployability.

---


### 52. [ATHENA: Knowledge-guided agentic neural architecture search for AutoFormer-based electronic health record modeling](https://arxiv.org/abs/2608.21712)

**<font color=#1a73e8>作者：</font>** Deyi Li, Qi Xu, Lingyao Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Transformer-based models are widely used for clinical prediction from electronic health records (EHRs), yet their architectures still require substantial manual tuning, and the optimal configuration may vary across tasks and hospitals. Neural architecture search (NAS) automates architecture design, but conventional methods are computationally costly for Transformer-based EHR models. Recent large language model (LLM)-guided NAS methods reduce manual search design but typically conduct each search independently, without reusing architecture knowledge across hospitals. In this study, we propose ATHENA (Agentic Transfer across Hospitals for EHR Neural Architecture Search), a knowledge-guided agentic NAS framework for Transformer-based EHR modeling. ATHENA uses a weight-sharing supernet that is pretrained once per hospital, allowing candidate architectures to be instantiated as inherited subnetworks and evaluated through fine-tuning rather than independent pretraining. It also incorporates a two-layer cross-hospital architecture prior. The first layer retrieves high-performing architecture examples from source sites based on task descriptors, while the second estimates the effects of architectural components using SHapley Additive exPlanations (SHAP)-based meta-regression. These priors guide a multi-agent LLM search together with validation feedback from the target hospital. Across six clinical prediction tasks and two independent health systems, ATHENA matches or outperforms four NAS baselines in 9 of 12 hospital-task evaluations at a search budget of 30. It also shows more consistent architecture selection across repeated searches. ATHENA provides a practical approach for reducing manual architecture tuning in Transformer-based EHR modeling. Code is publicly available at this https URL.

---


### 53. [Reinforcement Learning on Benign Facts Amplifies Leakage of Memorized Private Data](https://arxiv.org/abs/2608.21727)

**<font color=#1a73e8>作者：</font>** Renfei Zhang, Niloofar Mireshghallah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) is deployed to make models better at reasoning tasks, but its side effect on what models will divulge is under studied. Here we show that RLVR on facts increases extraction of personally identifiable information (PII) the instruct model had already memorized. We first confirm that instruct models have already memorized PII but leave them latent, rarely surfacing one when asked. We then apply RL on benign factual data that contains no PII of any kind, and re-probe: a targeted probe over name->email pairs, and an untargeted free-recall prompt that simply asks the model to list the addresses it knows. PII extraction rises sharply under both: on DeepSeek-V3.1, verbatim recall@k increases from 0.155 to 0.370, a 2.4x gain. The effect scales with model size: across three models spanning 8B to 671B parameters, absolute leakage is largest in the biggest model. Meanwhile model's reasoning abilities and refusal rates are retained, indicating that RL selectively changes which memorized information is accessible rather than broadly altering the model. In summary, memorized private data can be made markedly more extractable by training that never touches it. This gives an adversary a route to memorized data that requires no privacy-relevant training signal and no access to the data itself -- only the ability to fine-tune on something innocuous.

---


### 54. [Adaptive Multilevel Twisted Sequential Monte Carlo for Rare Events Estimation in Language Models](https://arxiv.org/abs/2608.21736)

**<font color=#1a73e8>作者：</font>** Zixuan Liu, Fangzheng Wu, Brian Summa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rare unsafe behaviors in large language models can remain practically significant even when their probability is extremely small, particularly at deployment scales involving millions or billions of interactions. Twisted Sequential Monte Carlo (SMC) provides a principled framework for rare-event probability estimation by learning twist functions that guide generation toward a target event. However, the standard twist learning framework relies on positive samples from the rare-event target distribution, which may be nearly absent before an informative twist has been learned, resulting in unreliable rare-event estimation. We propose Adaptive Multilevel Twisted SMC, which learns the rare-event twist through a sequence of progressively rarer intermediate events. At each level, the learned twist provides more informative positive examples for learning the next twist, ultimately leading to a more accurate final twist for the target rare event. Experiments across diverse tasks and model scales show that the proposed method produces more accurate rare-event probability estimates. By enabling more reliable discovery of hard-to-observe unsafe behaviors, our method provides a practical tool for strengthening the evaluation and safety alignment of deployed language models.

---


### 55. [FCPRAG: Fusion-Controller Parametric Retrieval-Augmented Generation for Stable Multi-Passage LoRA Injection](https://arxiv.org/abs/2608.21750)

**<font color=#1a73e8>作者：</font>** Jinchang Zhu, Jindong Li, Yi Ding 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Parametric retrieval-augmented generation (PRAG) injects retrieved evidence into a large language model (LLM) through passage-specific LoRA adapters, reducing reliance on long in-context prompts. When multiple passages are retrieved for the same query, however, evidence-level fusion becomes a bottleneck: equal-weight merging can amplify weak or conflicting evidence, and translating retrieval signals into fusion weights often requires fragile global tuning. We propose FCPRAG, a fusion-controlled parametric RAG framework that adds a lightweight controller for retrieval-conditioned, sample-level adapter fusion. The controller predicts per-passage fusion scores together with sample-level calibration signals, including a mixing gate and an adaptive temperature, enabling fusion that stays selective under informative retrieval signals and conservative under uncertainty. FCPRAG is trained with merge-aware supervision derived from each adapter's marginal contribution within a multi-adapter merge, using training data only. We further show that a single dataset-level temperature is suboptimal under heteroscedastic retrieval uncertainty, motivating sample-level adaptation. Experiments on HotpotQA, 2WikiMultiHopQA, PopQA, and ComplexWebQuestions (CWQ) across three LLM backbones show that FCPRAG consistently improves F1 over standard RAG and parametric RAG baselines, with gains of up to 4.65% on 2WikiMultiHopQA and 7.55% on CWQ, while also reducing tuning cost and improving robustness under retrieval perturbations.

---


### 56. [Learning to Look Again: Loss-Gap Supervision for Free-form Crop Routing in Vision-Language Models](https://arxiv.org/abs/2608.21762)

**<font color=#1a73e8>作者：</font>** Jinchang Zhu, Rong Fu, Yi Ding 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) fail many detail-centric questions for a concrete reason: the answer is visible in the image, yet lost after the image is compressed into a low-resolution global view. Allocating more visual tokens to every query improves some OCR and document cases, but it spends computation indiscriminately and can disturb tasks that rely on global context. We propose GapSight, a framework for learning visual re-reading: a VLM first takes a global glance, then selectively returns to a free-form region when the question calls for local evidence. The supervision comes from the target model's own failure signal. Offline, we compare answer loss or multiple-choice option margin under a global-only view and candidate crop-augmented views; crops that improve the target answer become model-specific review labels. A lightweight free-form crop router distills these labels into a one-shot inference policy that predicts whether to review, expected utility, and a continuous crop box from the global state. Across LLaVA-1.5-7B, InternVL2.5-8B, and Qwen2-VL-2B-Instruct, GapSight improves the Base no-zoom baseline on six benchmarks spanning OCR, documents, charts, infographics, VStarBench, and MME-RealWorld-Lite. On InternVL2.5-8B, GapSight raises the six-benchmark average from 52.25 to 64.29, above CropVLM (57.16), ViCrop (55.84), and ZoomRefine (54.43). Mechanism analyses show that the router rescues concrete wrong answers, adapts its action rate by task, and forms a favorable token-performance profile. These results position loss-gap supervision as a practical route to teaching VLMs when and where to look again.

---


### 57. [Evaluation Awareness in Language Models: Representation, Verbalization, and Control](https://arxiv.org/abs/2608.21766)

**<font color=#1a73e8>作者：</font>** Farzaneh Heidari, Amin Memarian, Guillaume Rabusseau  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Both capability and safety benchmarks rest upon the assumption that the behavior of language models undergoing a test is informative about their behavior in deployment. This assumption can fail, should models infer that they are being evaluated and condition their response on such context. This hypothesis, termed ``evaluation awareness'', has been observed in frontier and open-weight language models alike. We provide a systematic study of this phenomenon, by probing for it across six language models (from four families and three sizes) and three metrics. More precisely, we examine whether (i) being under evaluation is linearly represented within the models' activations space, (ii) it is verbalized in their output tokens (as scored by an LLM-as-judge), and (iii) steering causally affects their behavior. For the open-checkpoint Olmo models, we further test these measures at every training stage. In doing so, we report that evaluation awareness is linearly decodable from the residual streams of every model (best AUROC $\geq 0.7$). By contrast, these representations align only in part with verbalization: their correlations and mutual information are nonzero in some settings, yet vary substantially across models, layers, and readout choices. Nevertheless, steering along probe-derived directions can shift the verbalization scores. Finally, a comparison across the Olmo checkpoints reveals that evaluation awareness is already present within base models, becomes amplified throughout the stages of supervised fine-tuning, and remains stable thereafter---unlike the effects of steering, that grow more pronounced at every successive training stage. These results show the need for evaluations to account for the disjunction between what models represent internally, what they verbalize, and their steering.

---


### 58. [Privacy Preserving Semantic Communications in Wireless Edge Networks with Vision Language Models](https://arxiv.org/abs/2608.21773)

**<font color=#1a73e8>作者：</font>** Haoran Chang, Mingzhe Chen, Qianqian Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Semantic communication has emerged as a promising paradigm for next-generation wireless systems by transmitting high-level semantic features rather than raw bits. However, collaborative devices and multimodal transmission increase privacy risks because sensitive information may leak through inter-device semantic fusion and cross-modal representations. To address this issue, we propose a privacy-preserving semantic communication framework for wireless edge networks. Leveraging a vision-language model (VLM), the framework extracts textual semantics from images and identifies privacy-sensitive entities using a privacy database maintained only at the edge server. Before image transmission, each device removes the identified private regions while preserving useful semantic content. The server then reconstructs the removed regions from the received masked images using textual embeddings and VLM-based semantic priors. To protect textual information, we design an encrypted semantic-channel transceiver using physical-layer keys generated from reciprocal wireless channels, without pre-shared keys. We also introduce a semantic information bottleneck to suppress redundant information across multiple devices. The framework is evaluated against a strong model-aware adversary that can intercept wireless transmissions and access edge-device model parameters but not server-side data. Simulation results show that the proposed method reduces privacy leakage by more than 50% compared with a semantic communication scheme without privacy protection, while the authorized server achieves a 48% improvement in perceptual reconstruction quality over the adversary. The estimated mutual information between transmitted representations approaches 0 bit, indicating effective suppression of cross-device semantic redundancy.

---


### 59. [HIRA: A Human-in-the-Loop Retrieval-Augmented Cascade for Document Classification in Regulated Industries](https://arxiv.org/abs/2608.21792)

**<font color=#1a73e8>作者：</font>** Shangxuan Tian, Yanhui Chen, Carlos Queiroz  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Document classification in regulated industries is constrained by data residency, limited cold-start labels, scarce review capacity, and costly model-governance procedures. We present HIRA, a training-free, on-premises retrieval-augmented cascade for document classification in regulated deployments that combines BM25 over OCR text, dense text embeddings, and image-level representations through validation-calibrated weighted reciprocal-rank fusion. Confident documents are classified directly by retrieval; uncertain or visually confusable documents are passed to a locally hosted LLM verifier, which receives the OCR text, retrieved exemplars, label descriptions, and confusion-specific terms. When the verifier remains uncertain, the document is sent to human review. Each correction is stored as a margin-weighted retrieval exemplar and updates a Dirichlet-smoothed confusion graph, letting the system improve without updating model weights.
On a private 80-class trade-finance corpus, HIRA processes the full 30,233-document production stream while requesting human correction for only 1,945 documents (6.4%), improving Macro-F1 from 0.6218 to 0.8548. On the corrected Tobacco-3482 benchmark, HIRA reaches 0.9423 Macro-F1 with a locally hosted DeepSeek-R1-Distill-Qwen-32B verifier, 17.4 percentage points above the zero-shot LLM baseline, while invoking the verifier for only about 40% of documents and reducing LLM calls by approximately 60%. With 518 human corrections (24.8% of the pool), HIRA matches the fully labelled pool oracle, in which all 2,086 pool documents are indexed with their ground-truth labels. These results show that selective human feedback and retrieval-memory adaptation can be a practical alternative to repeated model retraining for long-tail document classification in regulated deployments.

---


### 60. [SAFE-G: Structure-aware Faithful Evidence-guided Generation for Knowledge-based Visual Question Answering](https://arxiv.org/abs/2608.21796)

**<font color=#1a73e8>作者：</font>** Long Shu, Shuochen Liu, Wei Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Knowledge-based Visual Question Answering (KB-VQA) aims to answer queries that necessitate reasoning over external knowledge sources beyond the visual content. Typically, current methods fuse multimodal features to retrieve external information, subsequently leveraging Multimodal Large Language Models (MLLMs) to derive answers from the retrieved evidence. However, these methods often struggle to capture structural associations within complex contexts to effectively filter noise. Furthermore, they frequently fail to ensure that the reasoning process remains strictly faithful to the retrieved evidence. To address these challenges, we propose SAFE-G, a Structure-Aware Faithful Evidence-guided Generation framework, which enables precise evidence localization and trustworthy reasoning. Specifically, we first employ a coarse-grained hybrid search fusing visual and textual modalities to recall candidate documents, and subsequently implement a structure-aware fine-grained graph retrieval that captures structural dependencies to filter noise and pinpoint precise evidence. Moreover, we introduce a reinforcement learning (RL) strategy with an evidence-grounded reward that assigns credit to correct answers only when the selected evidence is correct. This strict alignment constraint compels the model to anchor its response in the retrieved context, effectively enhancing its capability to locate evidence via multimodal features and perform faithful reasoning. Extensive experiments on the Encyclopedic-VQA and InfoSeek benchmarks demonstrate that SAFE-G outperforms prior methods by a margin of 8.9% and 3.5%, substantially enhancing the overall reasoning accuracy. Our source code is publicly available at: this https URL.

---


### 61. [MCite-RL: Towards Reliable Multimodal RAG via Citation-enhanced Agentic Reinforcement Learning](https://arxiv.org/abs/2608.21808)

**<font color=#1a73e8>作者：</font>** Suifeng Zhao, Zida Liu, Xinyu Lei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Retrieval-Augmented Generation (RAG) with visual citation is crucial for ensuring the traceability and verifiability of MLLMs. However, current RAG and SFT-based methods struggle to achieve robust cross-modal reasoning, causing imprecise visual citations or decoupling between the citation and the generated answers. To address these limitations, we propose MCite-RL, a citation-enhanced agentic reinforcement learning framework designed for reliable multimodal RAG. MCite-RL introduces an Agentic Refinement module for visual citation that employs iterative retrieval, reasoning, and recursive cropping to progressively narrow the search space, transforming citation into a dynamic, evidence-driven reasoning process rather than a static step. Furthermore, we incorporate a Citation-enhanced Reward mechanism that integrates both process-level and outcome-level feedback within a reinforcement learning paradigm to jointly optimize answer accuracy and source traceability. Extensive experiments on benchmarks such as Wiki-VISA, FinRAGBench-V, and MMLongBench-Doc demonstrate that MCite-RL effectively achieves the joint optimization of citation precision and answer quality.

---


### 62. [MSM-Mem: A Universal Medical Structured Multimodal Memory Framework for Medical AI Agents](https://arxiv.org/abs/2608.21810)

**<font color=#1a73e8>作者：</font>** Md Asaduzzaman Jabin, Khoa Le, Lin Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical decision-making is inherently experience-driven: physicians progressively refine their reasoning by synthesizing patient history, multimodal observations, and prior diagnostic experiences across interactions. In contrast, current multimodal large language model (MLLM)-based medical AI agents largely operate as stateless inference systems, generating decisions independently for each interaction without retaining or internalizing experiential knowledge. This discrepancy limits their ability to progressively improve reasoning reliability through usage and adapt to longitudinal patient contexts in real-world clinical workflows. In this study, we propose Medical Structured Multimodal Memory (MSM-Mem), an agentic memory framework that enables medical AI agents to evolve through accumulated clinical experiences. MSM-Mem organizes heterogeneous clinical experiences into semantic, episodic, and visual memory and incrementally updates them during inference, allowing the agent to retrieve prior experiences to inform current reasoning and progressively refine decision-making over time. Evaluations on MoE-LLaVA backbones demonstrate consistent performance improve- ments with further gains observed through continued usage. In general, MSM-Mem offers a viable pathway toward medical AI agents capable of evolving their reasoning competence in a manner analogous to the way clinicians learn from practice over time.

---


### 63. [Hints, Critics, and Teachers: Prior Injection for Sparse-Reward RL in Vision-Language Math Reasoning](https://arxiv.org/abs/2608.21811)

**<font color=#1a73e8>作者：</font>** Qiqian Fu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning for vision-language math reasoning starves under sparse reward: on a pool of 20,830 visual-math problems where Qwen2-VL-2B answers 3.6% of rollouts correctly, 85-97% of GRPO rollout groups are entirely wrong and contribute zero gradient. We train eleven methods under identical conditions in this regime, each injecting a different prior: text (reference-solution hints), distribution (on-policy distillation from a 7B teacher), and value (a value-pretrained critic with an MSE or HL-Gauss categorical loss). A prior helps exactly when it is delivered: the six arms whose prior effectively reaches the policy separate with no overlap from the remaining five -- the no-prior baseline and four arms whose prior is teacher-capped, gated away, or lost to a mis-parameterized critic -- both on the pooled in-domain metric and on cross-domain transfer (DynaMath). The central finding, however, concerns evaluation: one slice of the in-domain pool -- long used as this project's general-distribution check -- anti-correlates with genuine cross-domain transfer (Spearman rho = -0.74, n = 11 arms, permutation p = 0.011), while the hardest in-domain slice predicts it closely (rho = +0.89, p < 0.001). We attribute the inversion to a near-chance multiple-choice subset that rewards models for not having changed; read through it, the best cross-domain method looked mediocre and the worst looked like the champion. Among the methods, hint-guided exploration -- not UFT's auxiliary loss -- drives hint gains, and replacing the critic's MSE loss with HL-Gauss cross-entropy is worth +14.4 points in-domain. All accuracies are blind-judged, with paired exact tests.

---


### 64. [PatchGate: Narrowing the Verbalization Gap with Intrinsic Object Inventories in Frozen Vision-Language Models](https://arxiv.org/abs/2608.21819)

**<font color=#1a73e8>作者：</font>** Jihyung Ko, Eunji Jung, Hyeongsub Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable image captioning in Vision-Language Models (VLMs) requires captions to be both precise and complete, avoiding unsupported object mentions while covering visible objects. Existing training-free methods primarily address the former requirement, suppressing unsupported object words by intervening on model-predicted mentions during generation. Because they operate only on objects the model is already likely to mention, visible objects omitted from the output remain difficult to recover. We propose PatchGate, a training-free framework that extracts prompt-free object evidence intrinsic to a frozen VLM before generation and uses it to narrow the gap between an intrinsic object set and final object mentions. In the first stage, Visual Evidence eXtraction (VEX) reads patch-level lexical evidence from the latter half of LM decoder layers and constructs an image-conditioned object set without any task prompt. In the second stage, Visual-Evidence Inclusion-Exclusion Decoding (VIED) uses this object evidence to calibrate decoding logits, promoting evidence-supported but under-verbalized objects and suppressing weakly supported but over-verbalized objects. On AMBER, PatchGate improves both sides of object-level reliability, increasing visible-object coverage from 49.4 to 56.0 (+13.4%) and reducing object hallucination by lowering CHAIR from 7.5 to 6.6 (-12.0%), without external detectors or fine-tuning and with one extra forward pass.

---


### 65. [Do Large Language Models Perform Well on Comprehending Poetic Logic in Modern Chinese Poetry?](https://arxiv.org/abs/2608.21827)

**<font color=#1a73e8>作者：</font>** Tian Lan, Shanshan Wang, Zehua Duo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have achieved significant progress across a wide range of natural language processing (NLP) tasks, yet their ability to understand literary texts, particularly modern Chinese poetry, remains largely unexplored. The unique literary characteristics of modern Chinese poetry necessitate a distinct form of reasoning for effective comprehension. Unlike conventional texts that convey clear information, the unique "poetic logic" of modern Chinese poetry requires a holistic reasoning approach that goes beyond superficial semantic analysis to be understood. However, current evaluation paradigms largely ignore this critical dimension. To address this gap, we propose Peony, the first benchmark specifically designed for evaluating the poetic logic of modern Chinese poetry. We define poetic logic as four tasks across three levels, namely stanza, line, and imagery, and systematically evaluate and analyze six mainstream LLMs based on Peony. We evaluate these models under both non-thinking and thinking configurations. The experimental results reveal the limitations of current LLMs in understanding the poetic logic of modern Chinese poetry and validate the effectiveness and necessity of Peony. Our data and code will be available.

---


### 66. [Training a Knowledge Base: Supervised Structure Learning for Agent-Curated Document Stores](https://arxiv.org/abs/2608.21829)

**<font color=#1a73e8>作者：</font>** Yu Pan, Hongfeng Yu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation treats the document store as a frozen input, and the systems that instead let an agent curate one never measure what curation does to the store. We invert the framing: the knowledge base is the model. A training agent answers a supervised question against the current store, is shown the gold, then edits the store; an unchanged reader is later examined on a frozen snapshot under a fixed action budget. Where offline graph construction is unsupervised, (question, answer) pairs are our labels -- and that supervision is what makes the structure cheap. Per point of corpus indexed it returns 1.6x the action saving and 1.8x the accuracy of an unsupervised entity index covering everything, using 1,913 links against its 196,112. On questions the store trained on, an unchanged reader spends 31% fewer actions at higher accuracy, and the result reproduces on an official PhantomWiki generation whose questions we did not write. To measure how far this reaches we introduce a key-coverage gradient, a probe varying how much of a question the training set touched, replacing a train/test split's pass/fail with a decay curve. Generalization proves endpoint-dependent: accuracy carries to unseen questions (+0.167 F1 where both of a question's keys were indexed, +0.100 where one was, zero where neither) while the action saving stays on trained questions. Because that decay is indexed by coverage rather than by novelty, more training extends it -- and the store is undertrained, not saturated: coverage grows linearly in new questions and stops the moment training repeats them, so a hundred questions reach a quarter of the corpus and four times as many would close the gap.

---


### 67. [Beyond Success and Failure: Length-Aware Contrastive Learning for GUI Agents](https://arxiv.org/abs/2608.21830)

**<font color=#1a73e8>作者：</font>** Chengyang Gu, Le Zhang, Jingbo Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graphical User Interface (GUI) agents powered by Multimodal Large Language Models (MLLMs) have shown strong potential for automating tasks across diverse digital environments, where reinforcement learning (RL) has become a dominant training paradigm. However, widely used methods such as Group Relative Policy Optimization (GRPO) suffer from reward-gradient misalignment, leading to inefficient and unstable optimization. Recent work addresses this issue by reformulating RL with verifiable rewards (RLVR) as contrastive or classification-based objectives, which improve stability by eliminating problematic gradient behaviors. Despite this progress, existing contrastive RLVR methods rely primarily on outcome-level supervision and fail to capture fine-grained differences in trajectory quality within the same outcome category. In this paper, we propose Length-Aware Contrastive Learning for GUI Agents (LACL-GUI), a contrastive RLVR framework that incorporates trajectory-level quality signals into policy optimization. LACL-GUI introduces structured preferences within both successful and failed trajectories, encouraging concise successful executions and differentiating failure quality based on divergence from successful trajectories, while preserving optimization stability. Experiments on GUI agent benchmarks show that LACL-GUI provides more effective learning signals and consistently improves agent performance over prior methods, highlighting the value of trajectory-level supervision in contrastive RLVR.

---


### 68. [GUI-Primitives: Diagnosing Spatial Reasoning Failures in Vision-Language GUI Grounding](https://arxiv.org/abs/2608.21832)

**<font color=#1a73e8>作者：</font>** Md Abrar Jahin, Md Rizwan Parvez  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Computer-use agents ground natural-language instructions in screenshots to locate interface elements, yet existing benchmarks do not isolate whether models bind relational language to the correct element. We introduce GUI-Primitives, a 994-item benchmark of contrastive instruction pairs over seven spatial relations in graphical user interfaces (left/right, above/below, containment, alignment, proximity, list ordinal, occlusion). Each pair holds the screenshot and anchor fixed while changing the relation expression, so the correct target moves between two designated candidates. Five annotators validate a 196-item subset ($\kappa = 0.94$ well-formedness; $\kappa = 0.79$ target selection). Nineteen vision-language models reach at most $32\%$ strict point-in-box accuracy. Because models emit unconstrained coordinates, we classify each prediction by the candidate region it falls within. Predictions fall outside both candidates on $60-92\%$ of items. Conditional on falling within a candidate region, target selection reaches 0.82-0.90 for horizontal position, vertical position, proximity, and list ordinal, but does not differ significantly from 0.50 for containment and occlusion: most failures reflect candidate localization rather than relation understanding. Across ten models, benchmark accuracy correlates with ScreenSpot-Pro accuracy (Spearman $\rho = +0.74$), an exploratory association at this sample size. Marking the two designated candidates raises selection accuracy by 35--57 percentage points, an oracle diagnostic that supplies the candidate set rather than a deployable method. We release the benchmark, predictions, and code.

---


### 69. [GameXpert-Bench: How Far Are Coding Agents from Expert Game Development?](https://arxiv.org/abs/2608.21833)

**<font color=#1a73e8>作者：</font>** Kun Chen, Haorong Hong, Peizhong Gao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent large language models (LLMs) can operate as coding agents that build complete games from natural language requests. Game development is especially demanding because program logic, visual and audio content, interfaces, interaction and playability must function together in one executable artifact. Measuring this capability therefore requires evaluation of both game product and the development process. Existing benchmarks often assess the game development capabilities of LLMs by evaluating the final artifact or an isolated development stage. Our analysis of complete human-agent development trajectories identifies three stages that together span the lifecycle of game development with a coding agent: initial game generation, bug diagnosis and repair, and optimization over multiple turns. Therefore, we introduce GameXpert-Bench, which operationalizes the three lifecycle stages as three complementary benchmark tracks. GameGen evaluates complete game creation from a single request in an empty workspace. GameFix evaluates diagnosis and repair when defects are reported or left for the agent to discover. GameOpt evaluates cumulative optimization through request chains seeded by real development trajectories between users and agents. We evaluate each track using live game interaction, deterministic behavioral tests, or final product criteria with regression checks. The suite contains 97 generation tasks across 11 genres; 100 repair tasks from 50 game levels verified by humans, each with 19-27 injected bugs; and 17 optimization chains with six turns and 102 requests. Across the three tracks, current agents are more reliable at producing playable foundations and implementing explicit requirements than at discovering defects, verifying runtime behavior, and preserving functionality across changes.

---


### 70. [LLM4LLM: Bridging Kernel Benchmarks and Real Deployment via Closed-Loop Agentic Optimization](https://arxiv.org/abs/2608.21836)

**<font color=#1a73e8>作者：</font>** Hui Zeng, Pengfei Yang, Yanxin Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models have become increasingly capable agents for low-level code and kernel optimization, but isolated kernel benchmarks provide only a proxy for the deployment behavior that matters in language-model inference. We identify a benchmark-to-deployment gap: candidate kernels that appear correct and fast in standalone harnesses can exhibit different performance, safety, or phase behavior after integration into a real inference workload. We introduce LLM4LLM, a deployment-aware closed-loop optimization framework that starts from a target inference script, extracts phase-aware optimization tasks, searches with an experience-guided episodic agent, and accepts patches through in-model validation. Across ten language-model inference workloads on A100 and H100 GPUs, LLM4LLM improves end-to-end latency for every evaluated model, achieving 3.91$\times$/6.98$\times$ geometric-mean speedups on A100/H100; as supporting kernel-level evidence, it also attains up to 2.745$\times$ GeoMean speedup on KernelBench Level 2.

---


### 71. [FIRM-Video: Check Before You Score for Reliable Text-to-Video Reward Modeling](https://arxiv.org/abs/2608.21839)

**<font color=#1a73e8>作者：</font>** Peiyuan Zhang, Xiangyu Zhao, Hongbo Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable reward models are essential for text-to-video evaluation and alignment. However, the trade-off between evaluation accuracy and inference efficiency places high demands on the quality of training supervision. Existing approaches often rely on holistic judges with fixed rubrics or open-ended reasoning, leading to incomplete inspection, unfaithful justification, and entangled attribution. We introduce FIRM-Video, a unified checklist-driven data construction framework based on a check-before-score principle: construct dimension-specific checklists, verify each criterion against temporal visual evidence, and aggregate only verified decisions. For Instruction Following, FIRM-Video decomposes prompts into weighted atomic requirements; for World Coherence, it constructs prompt-calibrated, target-specific checks grounded in visible entities and actions; and for Perceptual Quality, it applies a generic taxonomy of visual defects. The verified criteria and scores are further transformed into natural-language analyses for end-to-end reward modeling. Subsequently, we construct FIRM-Video-90K with 88,044 dimension-specific instances from 29,348 videos, and introduce FIRM-Video-Bench with 750 point-wise human annotations across 250 videos. The Qwen3-VL-based FIRM-Video-8B achieves the best overall MAE on FIRM-Video-Bench while consistently delivering the highest VBench Total, Quality, and Semantic Scores in Best-of-8 sampling across three video generators.

---


### 72. [More Experts, Worse Dynamics: Inverse Scaling and Spectral Bias in Mixture-of-Experts State-Space Models](https://arxiv.org/abs/2608.21840)

**<font color=#1a73e8>作者：</font>** Chandresh Pandey  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) architectures are commonly motivated as a way to increase expressivity by decomposing complex systems into simpler local dynamics. This intuition has recently been extended to spectral state-space models, where mixing stable operators is assumed to enable adaptation to heterogeneous or regime-switching time series. We critically evaluate this assumption in a controlled synthetic setting designed to isolate dynamical rather than representational challenges. We study a next-step prediction task on sequences composed of three regimes: chaotic dynamics generated by the Mackey-Glass system, a stable oscillatory regime, and a noise-dominated autoregressive regime. Across extensive ablations including capacity scaling, oracle routing, frozen-expert variants, and comparisons to output-level MoE baselines, operator-level mixture models consistently fail to outperform a single-expert baseline. Increasing the number of experts leads to inverse scaling, routing collapses or fails to induce meaningful specialization, and even perfect regime supervision does not prevent degradation in global performance. Furthermore, we show that apparent improvements in mean squared error on chaotic trajectories can be misleading. Phase-space analysis reveals that lower error often arises from temporal smoothing that destroys the geometry of the underlying attractor rather than from faithful modeling of the dynamics. These results identify a likely limitation of operator interpolation under the studied parameterization and training protocol, and underscore the need for geometry-aware evaluation when assessing regime-switching dynamical systems.

---


### 73. [PUMA: A Polish Benchmark for Culturally Grounded Multimodal Understanding](https://arxiv.org/abs/2608.21853)

**<font color=#1a73e8>作者：</font>** Sławomir Dadas, Michał Perełkiewicz, Rafał Poświata 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly moving beyond text processing, adding support for other modalities such as images and audio. While text understanding and generation have been extensively studied, multimodal data processing capabilities, particularly in the context of cultures and languages other than English, have not yet been evaluated comprehensively. In this paper, we propose PUMA (Polish Unified Multimodal Assessment), a novel benchmark of 900 hand-crafted tasks designed to probe the limits of multimodal models in the Polish cultural and linguistic context. The dataset evaluates both cultural understanding and practical skill in processing text, images, audio, and visually rich documents. Our extensive evaluation of frontier commercial models, open-weights models, and specialized smaller systems highlights a significant performance gap. While top commercial models achieve high scores in visual question answering, most models struggle with complex audio or document understanding. We open-source our evaluation framework to advance localized multimodal AI research.

---


### 74. [ChainPrune: Evaluating and Reducing Redundancy in Long Chain-of-Thought Reasoning](https://arxiv.org/abs/2608.21860)

**<font color=#1a73e8>作者：</font>** Weihang Pan, Zhengxu Yu, Yuxiang Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chain-of-Thought (CoT) reasoning has significantly enhanced the multi-step problem-solving capabilities of large language models (LLMs) by introducing explicit intermediate reasoning. However, advanced Large Reasoning Models (LRMs) often exhibit overthinking behaviors, including excessively long reasoning steps, redundant steps, and high computational overhead. Existing token-length reward strategies aim to promote concise outputs, but often result in pseudo-conciseness, where token count is reduced, yet redundant reasoning persists, leading to longer and less structurally efficient chains. To address these limitations, we propose ChainPrune, a novel reasoning path semantic structural optimization method to efficiently and controllably synthesize self-generated high-quality training data. We initially consolidate self-generated reasoning paths into a tree-based structure, followed by a multi-criteria dominant path selection process for preference data construction that formulates shallow reasoning trajectories while preserving essential reasoning steps. To further enhance the quality of reasoning, we incorporate a DPO-based preference learning method combined with supervised loss, effectively mitigating false reward suppression. This innovative integration significantly enhances both the efficiency and effectiveness of our reasoning framework. Comprehensive experimental results demonstrate significant reductions in step length and computational overhead, while maintaining or even enhancing accuracy.

---


### 75. [HiDiffTIR: Hierarchical Difficulty-Aware Policy Optimization for Multi-Turn Tool-Integrated Reasoning](https://arxiv.org/abs/2608.21863)

**<font color=#1a73e8>作者：</font>** Yucan Guo, Xiaohan Wang, Miao Su 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tool-Integrated Reasoning (TIR) is a fundamental capability for LLM agents to solve complex tasks by interacting with external tools iteratively. Reinforcement Learning (RL) has become the dominant paradigm for enabling this capability. However, existing approaches typically assign uniform trajectory-level advantages and treat all correct tool calls equally, ignoring the varying difficulty and learning value across trajectories and reasoning steps. This can lead to imprecise learning signals that do not adequately distinguish between trivial and challenging tool-use patterns. To address this limitation, we propose HiDiffTIR, a Hierarchical Difficulty-aware policy optimization framework for multi-turn TIR. HiDiffTIR performs difficulty-aware credit assignment at both trajectory and turn levels, enabling the policy to focus on more informative trajectories and harder reasoning steps. Notably, this fine-grained optimization is achieved without additional supervision, relying solely on group-level statistics derived from standard RL rollouts. Extensive experiments on three tool-using benchmarks demonstrate that HiDiffTIR consistently improves multi-turn TIR performance and tool invocation accuracy over strong RL baselines, highlighting the necessity of difficulty-aware credit assignment for effective policy optimization in tool-integrated LLM agents.

---


### 76. [BioMed-Agent-RL: A Meta Learning, All You Need for Biomedical Applications](https://arxiv.org/abs/2608.21864)

**<font color=#1a73e8>作者：</font>** Md Asaduzzaman Jabin, Zihao Wu, Tianming Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The current progress of Clinical Vision Large Language Models (C-VLLMs) has substantially improved digital diagnostics, still these frameworks often endure lesion noises, modality misalignment, hallucination, and missed contextual grounding in complex clinical cases. Moreover, prevailing agent systems usually depend on static and non-adaptable pipelines and lack the versatility necessary for complex medical reasoning. To resolve these difficulties, we present BioMed-Agent-RL, a unified medical agent that incorporates adaptive orchestration, policy, and reward-based reinforcement learning (RL) models for biomedical applications. To ensure reliability, it invokes clinical context-aware preference optimization (CPO), direct preference optimization (DPO), and group relative policy optimization (GRPO) with dynamic entropy regulation. This pipeline utilizes a multimodal meta-learning approach that operates as a field-specific expert and human judgment synthesizer. The agent adaptively utilizes a set of model-level expertise, such as clinical grounding and reasoner, lesion segmenter, and field-specific synthesizer, across various clinical modalities (e.g., X-ray) by utilizing an iterative and adaptive RL approach. The agent learns to seriously synthesize misleading, conflicting vision cues and trust in inherent reasoning, while specialist advice is faulty. An intensive ablation study is conducted across multiple benchmarks, and the agent significantly outperforms existing state of the art models, such as GPT-5, attaining up to ~73% accuracy (gain of ~5%) over contemporary baselines. As a result, the framework suggests a new standard for building factual, reliable, robust, and expert-like intelligent agent systems for independent clinical reasoning.

---


### 77. [MemGuard: Persisting Verifier Signals for LLM-Agent Memory Governance](https://arxiv.org/abs/2608.21867)

**<font color=#1a73e8>作者：</font>** Haoyu Wang, Guangyuan Dong, He Liang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are moving from single-prompt use to long task streams in which reusable memory becomes a core capability for terminal, software-engineering, and web tasks. Such memory is useful only when stored experience remains reliable across hundreds of interactions, but two failure modes break that assumption in practice. The first is unreliable admission: failed trajectories,accidental successes, and misleading observations enter memory because they appear relevant, then mislead later decisions. The second is memory drift: long-running banks accumulate duplicate, stale, and conflicting records that retrieval alone cannot repair. MemGuard's key distinction is to treat verifier output not as a one-shot filter, but as persistent lifecycle metadata. It converts multi-criteria score-token verification into reward, confidence, label, and uncertainty descriptors that are attached to every candidate before activation and reused during retrieval, conflict resolution, summarization, and archival. We evaluate MemGuard on Terminal-Bench 2.0, SWE-Bench Verified, WebArena, and Mind2Web across four backbones, comparing against four memory baselines plus a verifier-only control under matched runtime budgets. Averaged over five seeds, MemGuard achieves the best success metric and lowest average steps in all 16 backbone-benchmark settings, improving over ReasoningBank, the strongest prior baseline among the memory methods we evaluate, with a largest gain of 7.9 success-rate points on WebArena, 5.6 step-success-rate points on Mind2Web, and 2.4-3.5 points on terminal and software-engineering benchmarks. Code is available at this https URL.

---


### 78. [The Chase Is the Curriculum, the Capture Anchors the Credit: Pursuit-Evasion Self-Play for Zero-Data LLM Reasoning](https://arxiv.org/abs/2608.21871)

**<font color=#1a73e8>作者：</font>** Jing Yu, Shengchao Chen, Yiyun Tan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards has become the dominant recipe for improving large language model reasoning, yet it presumes large human-curated task collections. Zero-data self-play removes this dependency, but existing methods vet learnability only by probing candidates and rejecting post hoc, never learning where along an environment's difficulty axis to place a task, and credit the solver with sparse terminal rewards alone. We recast zero-data self-play as a pursuit-evasion game: in LURE, an LLM evader positions tasks along each environment's difficulty axis to stay one step ahead of a planner-executor pursuer that hunts it down through verifiable interaction. The evader is trained on a capture-frontier reward that peaks when the solver captures it on exactly half of its rollouts, turning barely catchable into a learned positioning strategy rather than a hand-tuned rejection band. The pursuer earns capture-anchored dense process credit, in which monotone verifier progress is group-normalized jointly with the terminal capture under a round-anchored KL that keeps the co-evolution stable. Across three verifiable reasoning environments and three backbone families, LURE outperforms advanced baselines under unified/specialist settings, while the unified model attains stronger aggregate OOD zero-shot accuracy than all trained baselines across nine held-out benchmarks from three task families.

---


### 79. [ViSMoE: Visual-Aware Sparse Mixture-of-Experts for Embodied Referring Expression Grounding](https://arxiv.org/abs/2608.21878)

**<font color=#1a73e8>作者：</font>** Shuo Feng, Piji Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied Referring Expression Grounding is the task of enabling an agent to navigate in real environments and to localize a remote object based on natural language instructions. In this scenario, the agent needs to select one view for navigation at each step and identify a specific object among all candidate objects at the destination. However, most of the previous approaches fail to distinguish between views and objects, instead processing them using the vanilla vision encoder, which results in ambiguous representations of both views and objects. To address the above issues, we propose ViSMoE, which equips sparse Mixture-of-Experts with a visual-aware routing policy for the embodied agent. This framework processes different types of visual information specifically, resulting in discriminative visual representations for both views and objects. Experimental results on REVERIE and SOON datasets demonstrate that ViSMoE outperforms the previous state-of-the-art methods, showing the superiority of our proposed method.

---


### 80. [VIG: Visual Information Gain as a Reward Signal for Multimodal Chain-of-Thought Compression](https://arxiv.org/abs/2608.21883)

**<font color=#1a73e8>作者：</font>** Wen Luo, Xiaohan Yi, Xiaotao Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large reasoning models often rely on long Chain-of-Thought (CoT) traces in which a substantial fraction of tokens, such as repeated visual descriptions, self-reflection, and other visually-disengaged filler, inflate inference cost without contributing to the answer. Existing CoT compression methods optimize output length but never measure whether a reasoning token is actually grounded in the image. We propose \textbf{VIG} (Visual Information Gain), an information-theoretic GRPO reward that scores each reasoning token by how much the image reduces its predictive uncertainty. VIG is computed online from two forward passes of the same policy, one with and one without the image, so no reference chains, external annotations, or auxiliary reward models are needed. Across six main multimodal reasoning benchmarks and three Qwen3-VL-Thinking model sizes (2B/4B/8B), plus an additional R1-Onevision-Bench evaluation on 8B, VIG consistently improves the accuracy--efficiency trade-off, supporting our central claim: \emph{efficient multimodal reasoning emerges from raising visual information density, where every reasoning token earns its place by anchoring to the image, rather than from imposing a length budget.} Our source code is available at this https URL.

---


### 81. [From Solver Feedback to Faithful Plans: Multi-Role Reinforcement Learning for Symbolic Planning](https://arxiv.org/abs/2608.21897)

**<font color=#1a73e8>作者：</font>** Chenghao Zhang, Yikai Mao, Shanqi Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable planning requires converting natural-language instructions into executable symbolic specifications, yet large language models remain brittle without costly PDDL annotations and may exploit solver success in semantically unfaithful ways. We study how to learn faithful natural-language-to-PDDL formalization using only solver feedback, without human-written demonstrations. We propose a solvergrounded multi-role reinforcement learning framework where a single language model acts as an Actor, Judge, and Editor for generation, verification, and repair. The Actor proposes PDDL specifications, the Judge provides a solver-calibrated quality signal, and the Editor performs bounded diagnostic-conditioned refinement. On PlanBench, our method improves average success from 35.5% for LLM+P to 70.8%, achieves 66.3% faithful success, and reduces semantic drift to 6.4%. These results show that organizing solver feedback into generation, verification, and repair roles enables more scalable and faithful annotation-free symbolic planning

---


### 82. [Training Needs Trustworthy Worlds: Verified Synthetic Web Environments for Agent Learning](https://arxiv.org/abs/2608.21898)

**<font color=#1a73e8>作者：</font>** Chenghao Zhang, Canran Xiao, SaiSai Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Web agents promise to automate complex digital workflows, but their training remains limited by synthetic environments that look plausible while hiding broken links, inconsistent states, or infeasible tasks. We address the gap between scalable environment generation and trustworthy agent learning by constructing synthetic web environments that are executable, auditable, and grounded in backend state. Our framework represents each generated website as a structured scaffold of pages, navigation links, database records, state-change markers, and task constraints, then verifies and repairs structural, semantic, consistency, and feasibility defects before policy training. During interaction, ordinary UI transitions are executed deterministically, while persistent backend updates are invoked only through validated state-change markers, enabling dense rewards compiled from verified task-progress predicates. Across 500 synthetic environments spanning six domains, our method reduces task-blocking defects and improves feasible-task rate from 48.6% to 94.8%, while producing stronger PPO policies and improving transfer to WebArena, WebShop, and MiniWoB++ without LLM calls at evaluation time. These results show that verified synthetic environments can serve as a scalable and reliable training substrate for compact web agents, shifting synthetic webagent learning from surface-level plausibility toward executable, state-grounded supervision.

---


### 83. [CD-LoRA: Consistency-Driven Low-Rank Adaptation for Multi-Task Fine-Tuning](https://arxiv.org/abs/2608.21909)

**<font color=#1a73e8>作者：</font>** Qian Zha, Jinda Liu, Yuan Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While Multi-Task Learning (MTL) is essential for adapting Large Language Models (LLMs) to diverse domains, prevailing LoRA-based methods rely on complex routing mechanisms that partition task-specific knowledge. In this work, we reveal that such routing-based designs are prone to a training-inference discrepancy, where stochastic routing decisions under distribution shifts compromise inference stability. Driven by a second-order Taylor analysis that exposes the instability induced by routing variance, we challenge the training-inference discrepancy and propose Consistency-Driven Low-Rank Adaptation (CD-LoRA). By eliminating routers entirely, CD-LoRA employs a consistency-driven alignment mechanism to enforce representation congruence across tasks in a shared low-rank space. This paradigm fosters robust, task-agnostic features without explicit partitioning overhead. Extensive experiments show that CD-LoRA consistently outperforms state-of-the-art multi-adapter baselines, offering a simpler, router-free, and more stable solution for multi-task PEFT. The code is available at the anonymous link this https URL.

---


### 84. [OptiMAS: Automatically Optimize Multi-Agent System](https://arxiv.org/abs/2608.21918)

**<font color=#1a73e8>作者：</font>** Yuxin Cheng, Chang Liu, Hanxin Yu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Automated evolution of Multi-Agent Systems (MAS) holds significant potential for reducing the manual effort required to design and optimize LLM-based agent architectures. However, extant search-based paradigms face a fundamental trade-off, where an expanded optimization scope exacerbates evolutionary instability, while discrete branch-and-discard search isolates insights across lineages. To address these limitations, we propose a continuous, data-driven optimization paradigm built upon a unified ReAct-based infrastructure that reconciles a broad optimization scope with operational stability. Under this paradigm, we present OptiMAS, a task-agnostic agentic optimizer that leverages textual interaction trajectories and task feedback as loss signals for end-to-end MAS evolution. Equipped with a novel dual-track memory mechanism, OptiMAS sustains performance improvement over extended optimization horizons. Evaluation on four heterogeneous agentic benchmarks with three varying scale and accessibility LLM backbones, demonstrates that OptiMAS consistently achieves competitive or superior accuracy relative to both domain-specialized hand-crafted systems and existing evolutionary methods. Our work establishes a practical milestone toward robust, automated MAS evolution.

---


### 85. [Beyond Fixed Directions: Adaptive Representation Analysis of Reasoning and Memorization in LLMs](https://arxiv.org/abs/2608.21919)

**<font color=#1a73e8>作者：</font>** Shaheen Nabi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work has proposed that reasoning and memorization in language models can be characterized by a single representation direction, including methods that keep this direction fixed during reinforcement learning. We test two assumptions behind this view. First, are reasoning-oriented and factual-recall task groups approximately single-direction separable? Second, does the resulting geometry remain stable after GRPO? Using Qwen3-0.6B and a controlled 400-example dataset, we find that a one-dimensional projection can match a full 1024-dimensional linear probe with AUROC = 1.00 on the studied task groups. However, after GRPO, the corresponding direction is substantially reorganized: mean-direction cosine averages 0.453, probe-direction cosine 0.445, while direct representation drift reaches 0.511 at the final layer. Probe AUROC nevertheless remains 1.00. The evidence therefore supports single-direction decodability for the studied task groups but challenges fixed-direction stability: the information persists while its geometric realization changes.

---


### 86. [Bi-EZP: LLM-Guided Bilevel Program Evolution for Ensemble Zero-Cost Proxy Discovery](https://arxiv.org/abs/2608.21927)

**<font color=#1a73e8>作者：</font>** Yutao Lai, Kezhao Lai, Hai-Lin Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zero-cost proxies enable neural architecture search (NAS) to rank candidate networks from statistics computed at initialization, avoiding repeated training. However, different proxies capture different properties and often produce inconsistent rankings across search spaces. Ensemble proxies can combine complementary signals, but automated discovery must optimize both discrete aggregation structures and their continuous coefficients, making structural quality difficult to separate from parameter calibration. We propose Bi-EZP, a bilevel framework that decouples these decisions. At the upper level, a large language model generates executable aggregation programs over four complementary base proxies with program-specific parameter bounds. At the lower level, covariance matrix adaptation evolution strategy (CMA-ES) optimizes the continuous parameters of each fixed program on an inner training split. The calibrated programs are then evaluated using Kendall's rank correlation on a disjoint validation split, enabling evolutionary selection to favor structures that generalize beyond their calibration data. Experiments on NATS-Bench and Network Design Spaces evaluate ranking performance across heterogeneous search spaces, and DARTS experiments assess downstream architecture search. Results show that separating program discovery from numerical calibration provides an effective approach to automated ensemble zero-cost proxy construction. The source code is available at: this https URL

---


### 87. [GuardianBench: A Same-Scene Instruction-Contrastive Benchmark for Latent Contextual Risk in Embodied AI](https://arxiv.org/abs/2608.21928)

**<font color=#1a73e8>作者：</font>** Zhesheng Zhang, Jiahao Lu, Wei Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In embodied AI, safety risk can be latent: a benign instruction and a safe scene become hazardous only when composed. Prior work has advanced embodied safety by varying visual contexts or evaluating execution-time dynamics, but the complementary axis of fixing the scene and varying only the instruction remains underexplored. We introduce GuardianBench, an instruction-contrastive benchmark grounded in international safety standards that isolates this latent contextual risk through 3,024 instruction-scene examples organized as same-scene Safe/Unsafe contrastive pairs across various hazard categories. Benchmarking state-of-the-art vision-language models (VLMs) reveals instruction-insensitive verdicts: models disproportionately approve both instructions under a given scene; across the primary models, average pair accuracy is only 24.1%. Our systematic rationale audit localizes the dominant failure: models fail to bind the instruction-relevant cues that differentiate safe from unsafe compositions. As a post-training case study, Verdict Log-Odds Supervision (VLOS), a lightweight verdict-level objective, substantially improves performance on open-weight backbones. Together, our latent contextual risk task formulation, standards-grounded contrastive benchmark construction, pair-level and rationale-level failure diagnosis, and benchmark-enabled verdict calibration establish GuardianBench as a controlled evaluation suite for exposing and improving safety reasoning over instruction-scene compositions under latent contextual risk.

---


### 88. [SkillBloat: Token Amplification Attacks via Skill Injection in LLM Coding Agents](https://arxiv.org/abs/2608.21929)

**<font color=#1a73e8>作者：</font>** Yuanjin Zheng, Jingbang Chen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent skills extend coding agents with task-specific instructions, scripts, and resources, but they also create a trusted
instruction channel that can be abused beyond conventional security attacks. This paper studies token amplification through
skill injection: an economic resource-abuse threat in which a malicious skill causes an agent to consume substantially more
tokens than needed for normal task execution. We present SkillBloat, a two-phase framework that first screens a library of
diverse attack-type conditions across multiple amplification mechanisms and then refines the strongest candidate through
LLM-guided full-document skill rewriting. Evaluated on a real-world skill benchmark, SkillBloat achieves 5.4184x-10.1455x
average best amplification across multiple coding-agent target configurations. An ablation shows that the second-stage
refinement loop consistently improves average best amplification over Phase 1 attack-type screening alone, demonstrating
that iterative optimization provides additional benefit beyond initial attack-type selection. These results show that skill
ecosystems expose a practical resource-amplification attack surface that is orthogonal to existing security-oriented skill
poisoning.

---


### 89. [EDGE: Experience-Distillation for Guided Exploration in Agentic Reinforcement Learning](https://arxiv.org/abs/2608.21946)

**<font color=#1a73e8>作者：</font>** Can Xie, Yuyi Zhou, Wen Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with outcome-based objectives such as GRPO enables LLM-based agents to solve complex, long-horizon tasks, yet the reusable exploration patterns embedded in interaction trajectories are largely discarded after a single policy update. Existing experience-augmented approaches retrieve historical guidance at inference time, but they apply experiences without accounting for the policy's evolving capability and create persistent dependencies on external retrieval. We propose EDGE (Experience-Distillation for Guided Exploration), a framework that treats retrieved experiences as temporary training-time scaffolds and progressively internalizes their benefits into the parametric policy. Concretely, EDGE partitions each rollout group into experience-conditioned and experience-free trajectories to estimate and admit only positive marginal gains without extra sampling, then distills the induced behavior into the base policy via a reverse-KL objective on its own empirical support. A co-evolutionary experience bank further synthesizes guidance from emerging failure modes and prunes obsolete entries as the policy evolves. On ALFWorld and WebShop, EDGE improves over GRPO by 8.3 and 12.5 success-rate points at the 7B scale and retains 96.0% of its scaffolded performance when external experiences are removed at inference time. The code is available at this https URL.

---


### 90. [Sparse Multi-Stage Expert-Agent Routing for Complex Clinical Reasoning](https://arxiv.org/abs/2608.21948)

**<font color=#1a73e8>作者：</font>** Sike Xiang, Shuang Chen, Qian sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Complex clinical reasoning requires models to update diagnostic hypotheses as new evidence emerges and to coordinate different medical specialities under limited consultation resources. Existing LLM-based clinical reasoning systems typically perform single-pass prediction or rely on fixed multi-agent workflows, making expert participation either static or unnecessarily exhaustive. We propose Sparse Multi-Stage Expert-Agent Routing, a language-based clinical reasoning framework that models diagnosis as a stage-wise routing process. Given progressively available clinical evidence derived from multiple modalities, the framework maintains an evolving case state and adaptively activates a sparse set of medical expert agents, supported by expert-specific memory across stages. To evaluate free-text diagnostic conclusions beyond surface similarity, we further introduce ClinFEScore, a fact-aware semantic evaluation protocol for clinical reasoning outputs. On reconstructed multi-stage cases from MAC and AgentClinic-NEJM, our framework reduces the average number of activated experts from 17.0 to 3.0 whilst maintaining strong fact-level diagnostic quality. On 200 real-world hospital MDT cases, ClinFEScore correlates strongly with clinician judgements (Spearman's $\rho=0.81$; Pearson's $r=0.87$), whilst our method achieves 91.5\% clinician-verified diagnostic accuracy with approximately five expert-agent/LLM calls per case. These results support sparse stage-wise coordination as an efficient and clinically relevant approach to LLM-based clinical reasoning.

---


### 91. [Repo2Skill-Evo: Repository Skills Go Stale in Silence](https://arxiv.org/abs/2608.21964)

**<font color=#1a73e8>作者：</font>** Chenyuan Duan, Ge Shi, Zineng Mao 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly operate over evolving software repositories, where success depends on repository-specific procedural knowledge: which APIs to call, which scripts to run, and which conventions the current release expects. Agent skills externalize this knowledge into reusable units, and prior work shows that they can improve agent performance. What remains unclear is whether that improvement is durable. The same version specificity that makes a skill useful also makes it fragile: after a release, it may become stale without raising any explicit signal, while continuing to provide obsolete guidance. Externalizing knowledge into a skill can therefore make its decay invisible.
We study whether agents can keep this externalized knowledge current. Repo2Skill-Evo casts each release transition as a skill-maintenance task: given a V1 skill set and the official V1-to-V2 patch, an agent must update obsolete skill content while preserving guidance that remains valid. Across 57 real-world repositories and 105 selected release transitions, every evaluated transition invalidates part of the V1 skill set. Yet six frontier agents reach only 29.9%-69.7% avg@3 macro F1 under a patch-grounded removal metric that balances stale-content recall against over-editing precision. Across runs, two opposing errors dominate: incomplete coverage of affected files in the skill set leaves stale content untouched, while overbroad editing is associated with higher recall but lower precision. Repository skills go stale in silence, and even frontier agents cannot reliably maintain them.

---


### 92. [Closed-loop AI achieves certifiable engineering design](https://arxiv.org/abs/2608.21976)

**<font color=#1a73e8>作者：</font>** Tianyi Yu, Chengxing Tao, Haoxuan Shen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI has automated parts of scientific discovery, including paper generation, expert-level coding, therapeutic proposal, and autonomous experimentation. Complex physical engineering design remains a gap, because candidates must satisfy simultaneous constraints in fluid dynamics, solid mechanics, and structural stability. We introduce The AI Engineer, an agentic framework that couples large language models (LLMs) to deterministic engineering backends in a closed loop: natural-language requirements are converted into design-domain geometry and mesh; topology is optimized with bi-directional evolutionary structural optimization (BESO) coupled to the CalculiX solver; and member sizes are refined with particle swarm optimization (PSO) coupled to Zwind under offshore aero-hydro-servo-elastic load cases. To explore many designs without per-candidate certification cost, an Automated Reviewer scores each candidate on five dimensions (capacity, steel intensity, unit cost, constructability, and fatigue life) using piecewise-linear functions calibrated on 11 real floating-wind projects. Search terminates only when a candidate reaches a composite score $S \ge 85$ (grade A) with no subscore below 60. We validated this gate by submitting the top-scoring design to the China Classification Society (CCS) for Approval in Principle (AIP), which it passed; AIP is thus an external check that the reviewer tracks professional judgment, not the daily objective. The certified design outperforms the human-optimized TuQiang baseline, reducing steel mass and unit capital cost by 8.1% each while meeting all AIP criteria. This verification-closed regime, in which every proposal is judged by deterministic physics and codified limit states, distinguishes The AI Engineer from open-ended generative systems. Remaining limits include detailed design and fabrication-hard constraints.

---


### 93. [Redteaming Leading Arabic LLMs with ASAS](https://arxiv.org/abs/2608.21985)

**<font color=#1a73e8>作者：</font>** Fidaa Abed, Haidar Khan, M Saiful Bari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As the adoption of large language models (LLMs) grows in Arabic-speaking regions, ensuring their safety and cultural alignment is increasingly critical. However, Arabic LLM safety remains underexplored, especially in adversarial evaluation settings. We introduce the Arabic Safety Index (ASAS), the first fully human-curated Arabic benchmark for redteaming LLMs. ASAS contains 801 prompts spanning 8 safety categories and 8 attack strategies, with ideal responses in Modern Standard Arabic (MSA). We conduct a redteaming evaluation across seven leading models with Arabic capabilities, including GPT-4o, Claude 3.7 Sonnet, and regional models such as ALLaM and FANAR. Human annotators rate responses using a structured 4-point safety scale, revealing that most models fail to defend against 50% of unsafe prompts. Our findings highlight major safety gaps in high-harm categories such as weapons and illicit substances, with direct and obfuscation-based attacks proving most effective. The results also show that language alignment does not readily transfer across languages, and that automated safety judges (e.g., GPT-4o) perform poorly compared to human annotators. ASAS provides a culturally grounded benchmark and redteaming protocol to drive progress in Arabic LLM safety.

---


### 94. [Gated Decoupled Compositional Bandits: A Unified Theory of Contextual Bandits with Supervised-Calibrated Action Scaling and Pre-Execution Gating](https://arxiv.org/abs/2608.21993)

**<font color=#1a73e8>作者：</font>** Oleg Miroshnichenko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Gated Decoupled Compositional Bandits (GDCB), a family of contextual bandit algorithms with three structural innovations that jointly fall outside the taxonomy of LinUCB, LinTS, HierTS, factored bandits, neural contextual bandits, and RLHF. In a GDCB system: (i) the action delivered to the environment is the composition of a nominal arm, drawn by a discrete or hierarchical bandit, with a context-dependent scaler; (ii) the scaler parameter is learned in a separate supervised loop, not jointly with arm selection; and (iii) every action passes through a pre-execution gate that may modify or veto the composed action before it reaches the environment. We formalise this class of algorithms, prove four structural theorems characterising its statistical behaviour, and show that six industrially significant systems -- short-term rental dynamic pricing, clinical drug dosing, credit origination, grid demand response, content moderation, and LLM tool-use agents -- are all instances of GDCB, differing only in the composition operator, scaler family, and gate. The central result is the Decoupling Variance Reduction theorem: a well-calibrated scaler removes context-induced variance from the arm-to-reward mapping, turning a non-stationary bandit problem into an approximately stationary one. The Gate-Induced Equivalence theorem shows that under a stationary gate, historical data collected under any prior policy is a valid warm-up initialiser without importance-sampling correction, generalising the companion P-HITL result (arXiv:2606.02595) from human approval to arbitrary gates. In regulated, high-stakes domains, constraints usually treated as deployment frictions -- approval gates, compliance rules, safety shields -- are the mechanism that makes fast deployment possible, not an obstacle to it. The companion paper validates instance 1 (STR dynamic pricing) on real production data.

---


### 95. [The Communication Map of a Transformer](https://arxiv.org/abs/2608.22007)

**<font color=#1a73e8>作者：</font>** Richard Zhe Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The components of a transformer communicate by writing to and reading from a shared residual stream, and mechanistic interpretability has mapped these connections by hand, one circuit at a time. We present the communication map, which charts every potential communication channel in a language model from weights alone, generalizing the composition score of Elhage et al. (2021) into a single coupling coefficient covering all 18 connection classes, from entire attention head circuits to single neurons. The census of all candidate channels, from $6.3\times10^{8}$ in GPT-2 to $1.3\times10^{11}$ in Pythia-6.9B, finds that 70-89% of head pairs are oriented far from chance, some coupled strongly and others actively avoiding each other. The full map costs 15 seconds for GPT-2 and 11 minutes for Pythia-6.9B on one consumer GPU. Two applications demonstrate the utility of the map. In Application 1, the strongest head-to-head couplings recover the known induction circuits blind and group them into communities, and ablating one such community destroys the model's in-context copying. In Application 2, pooling every head's coupling coefficients identifies a distinct two-dimensional stream subspace, whose deletion abolishes the induction capability in six models up to Pythia-6.9B. This subspace is different from those identified by either activation PCA or outlier dimensions. We release the map, the statistical machinery, and the intervention suite.

---


### 96. [DynaContext: Self-Improving Dynamic Contextualization of Optimized Prompts for Heterogeneous Parameter Extraction](https://arxiv.org/abs/2608.22014)

**<font color=#1a73e8>作者：</font>** Joe Yu, Shibin Thomas Stanley Paul, Sven Mayer  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated prompt and skill optimization typically produces a single static instruction that is reused across inference instances until the next optimization cycle. However, this approach cannot adapt when the required context, constraints, and evidence vary from one instance to another. For instance, parameter extraction from electronic component descriptions breaks this assumption: resistors, capacitors, transistors, and connectors require different fields, unit constraints, and demonstrations, and each input provides a different evidence state. We introduce DynaContext, a framework that combines an offline-optimized extraction core, learned with GEPA or SkillOpt, with inference-time contextual adaptation and validation-gated self-improvement. DynaContext routes each item through internal, external, or fallback evidence paths and composes an item-specific prompt from the core, schema, evidence, unresolved fields, and validated demonstrations. Deterministic validation and an LLM judge gate every output, uncertain cases go to human review, and only human-verified corrections enter the demonstration memory. On a single-category benchmark, average accuracy increases from 86.6% for the base prompt to 96.9% for standalone SkillOpt and 98.6% for the best DynaContext configuration. Across 850 heterogeneous gold parameter facts, average field-level F1 increases from 51.8% for an unoptimized, demonstration-free control to 59.2% with dynamic demonstrations alone, 66.9% with the optimized core alone, and 71.0% with both. Holding the model fixed, the full configuration outperforms the deployed static-prompting pipeline by 17.3 F1 points on average.

---


### 97. [SPAR-Hate: An Auditor-Guided Multi-Agent Framework for Bilingual Hate Speech Parsing](https://arxiv.org/abs/2608.22018)

**<font color=#1a73e8>作者：</font>** Yifan Lyu, Dianqing Lin, Xinran Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hate speech detection has recently shifted from coarse-grained classification to structured parsing, where systems must jointly identify hateful targets, arguments, and target-level labels. However, existing studies primarily emphasize benchmark evaluation while paying less attention to the cultural, linguistic, and social-group challenges involved in structured hate speech parsing. To address these challenges, we propose SPAR-Hate, an auditor-guided multi-agent framework for bilingual hate speech parsing. The framework first decomposes documents into clause-level decision units and then generates evidence-grounded judgments from three complementary perspectives: Victim, Moderator, and Cultural Bystander. An evidence-constrained arbitration process resolves conflicts among role-specific predictions and aggregates them into structured sample-level outputs. Experiments on the STATE-ToxiCN and TBO benchmarks show that SPAR-Hate consistently improves bilingual hate parsing across diverse large language models. The framework achieves state-of-the-art results on bilingual multi-tuple extraction tasks, with the largest gains observed under stricter structural evaluation metrics.

---


### 98. [More Accurate or More Efficient? Evaluating Locally Deployed Compact Open-Weight Language Models for Mathematical Reasoning](https://arxiv.org/abs/2608.22048)

**<font color=#1a73e8>作者：</font>** Orion Powers, Daniella Seum, Khaled Slhoub  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed on local hardware for privacy, cost, and accessibility reasons. Yet many evaluations emphasize accuracy while fewer quantify local runtime and energy, characterize failure modes, or apply paired statistical comparisons under controlled conditions. This paper presents a controlled, documented procedure for evaluating locally hosted LLMs on mathematical reasoning. It combines fixed inference settings, hierarchical answer extraction and verification, explicit failure-mode classification, and per-question resource measurement, and reports accuracy with paired significance tests and effect sizes. We demonstrate it in a preliminary study of three compact open-weight models under five billion parameters, Gemma3:4b (Google), Phi3:3.8b (Microsoft), and Qwen3:4b (Alibaba), across datasets spanning Grade 8 Math, Calculus I, and Advanced Probability and Statistics. All models ran through the same local inference server on one workstation, using a shared prompt template, controlled settings, and a matched question set per dataset. No single model dominates. Qwen3:4b is most accurate on two datasets and Gemma3:4b on Calculus I, yet Gemma3:4b returns roughly three times more correct answers per watt-hour than Qwen3:4b on every dataset while generating far fewer output tokens; Qwen3:4b requires substantially more generation time, energy, and output per question. Phi3:3.8b is substantially less accurate on all three datasets; its low extraction-failure rate indicates incorrect answers rather than unparsed output, though we caveat possible prompt-format effects. These preliminary findings indicate that accuracy alone is an insufficient basis for selecting a local model.

---


### 99. [GenCoord: Skill-Path Commitments under Private Information](https://arxiv.org/abs/2608.22055)

**<font color=#1a73e8>作者：</font>** Peng He, Junning Zhu, Haohan Yuan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Suppose one embodied agent knows what must be built, while its teammate alone knows which transformation its workcell can perform. Neither local view determines who should act, what should be handed off, or how the joint task should continue. We introduce GenCoord, which turns the task consequence of such private facts into an executable skill-path commitment. A local Qwen3.5-0.8B model emits a multi-step SELF plan and peer REQ; bounded feedback conditions route revision when the deciding capability is peer-local. The resolved commitment is parsed, checked, canonically materialized, compiled to Mineflayer skills, and verified by handoff and terminal state. Counterfactual interventions that hold the world, call schedule, and executor unchanged make requester revision and receiver execution follow the injected task consequence in both directions. Across three independently trained seeds, correct capability feedback closes the paired local-information gap from 50% to 100%. Multi-step commitments improve held-out-template success by 6.9 points while reducing model decisions by 32%. At matched closed-loop quality on 128 held-out semantic clusters, Short DSL reduces peer traffic by 92.8% and median time-to-commitment by 68.2% relative to controlled free-form communication. These results identify executable task consequences as the coordination unit connecting distributed local reasoning to verified joint action.

---


### 100. [MEMORY Wins All: Indirect Bias Injection Attacks via Social Media Feeds](https://arxiv.org/abs/2608.22061)

**<font color=#1a73e8>作者：</font>** Minjae Seo, Wonwoo Choi, Geonwoo Han 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personal AI agents routinely consume external content while performing tasks such as web browsing, email processing, and SNS feed summarization, and they retain selected information or execution results in persistent memory for later use. We show that this ordinary ingestion of external content opens an indirect path for manipulating subsequent agent behavior. Based on this observation, we present IBIA, an Indirect Bias Injection Attack that plants an adversary-aligned stance on a specific topic into a victim agent's memory through external content, without direct access to the agent, its memory, or future user queries. For this, IBIA combines three mechanisms: comment cloaking, which keeps the crafted content consistent with the surrounding discussion, comment watermarking, which enables lightweight identification during curation, and category anchoring, which makes the retained stance salient under later related requests. We evaluate IBIA on BiasBench, a benchmark of 6,000 adversary-crafted social comments and 120 email instances. The watermark-based curation identifies 95.9% of the injected comments. Under the OpenClaw setting, IBIA achieves adversary-aligned response rates (AARs) of 91.2% on average across four downstream tasks, including 86.6% on the frontier GPT-5.5. We further propose a memory boundary defense that detects the injected bias and reduces AARs to 80.6%.

---


> [!TIP]
> 当前位于：**51-100**（第 2/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-363](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
