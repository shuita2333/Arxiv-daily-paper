# 🧠 大模型相关研究 | 2026年09月16日

> 本类共 **368** 篇论文：已确认 **345** 篇，待复核 **23** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**301-350**（第 7/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-368](./part-08.md)

---

### 301. [Multi-View Molecular Representation Learning with Hierarchical Graphs and Contextualized Fingerprints](https://arxiv.org/abs/2609.15611)

**<font color=#1a73e8>作者：</font>** Gwang-Hyeon Yun, Jong-Hoon Park, Bing Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular property prediction requires representations that generalize from limited labeled data to structurally novel compounds. Existing molecular pretraining methods often rely on a single view: graph-based approaches model atom-bond topology but provide limited fragment-level supervision, whereas fingerprint descriptors encode chemical patterns but are typically used as fixed auxiliary features. We propose HiFi-Mol, a multi-view framework that separately pretrains a hierarchical graph encoder and a contextualized fingerprint encoder before downstream integration. The graph branch uses fragment-aware masking with multi-resolution supervision to capture substructure-aware representations, while the fingerprint branch tokenizes active entries from seven fingerprint families and applies masked language modeling to learn contextualized embeddings. During fine-tuning, HiFi-Mol combines projected multi-resolution graph features with fingerprint embeddings for downstream prediction. Evaluated on MoleculeNet benchmarks under the scaffold split, HiFi-Mol achieves a 2.77% improvement in average ROC-AUC over the best baseline across eight classification tasks while maintaining competitive performance on three regression tasks. Further analyses reveal that fragment-aware masking improves graph representation quality, and classification results demonstrate dataset-dependent strengths of the individual graph and fingerprint variants, confirming that the two views provide complementary predictive signals.

---


### 302. [Beyond AI Literacy: A Structured Review and Exploratory Meta-Analysis of Measures for Competent Generative-AI Use](https://arxiv.org/abs/2609.15624)

**<font color=#1a73e8>作者：</font>** Daniele Veri'  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Researchers assessing competent generative-AI use at work must choose among self-reports, objective tests, and measures of oversight and reliance. We conducted a structured, seeded review of 24 focal empirical publications, starting from the 2024 COSMIN-based review and adding a targeted update through 17 August 2026. We grouped the measures into four domains: knowledge and use, epistemic oversight, reliance calibration, and operational control of tool-using agents. In an exploratory meta-analysis, we pooled three direct subjective-objective correlations from one research program (REML r = .055; Hartung-Knapp 95% CI [-.047, .156]; combined reported N = 2,765). We could not resolve a discrepancy between the largest study's reported correlation and p-value, leaving its weight uncertain. Adding a synthetic mean of 12 cross-factor correlations from a fourth study gave r = .079 (95% CI [-.025, .181]). This sensitivity analysis concerns a broader comparison. From this small evidence base, we cannot establish a population correlation, validate workplace cutoffs, or justify substituting self-ratings for performance scores. We identified tests of foundation knowledge (AICOS-S and GLAT) and measures of verification, reliance, trust, and dependency. We found no validated individual-level instrument in the focal corpus that tests the full combination of agent scope, permissions, recovery, state isolation, independent review, and evidence-based closure; some cover subsets. We propose a four-layer workplace battery with non-compensatory decision rules, but have not tested its thresholds or whether it improves on other assessment approaches.

---


### 303. [ModaLens: Measuring Image Sensitivity in Report-Conditioned Medical VLMs](https://arxiv.org/abs/2609.15635)

**<font color=#1a73e8>作者：</font>** Sebastián Andrés Cajas Ordóñez, Maximin Lange, Quang Bui 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A radiology report can already answer a clinical question, so it is hard to tell whether a vision-language model also uses the image. ModaLens, a paired image-swap audit, measures how report availability changes image sensitivity: MedGemma-27B on 3,199 paired MIMIC-CXR cases from 293 patients, all 14 questions per case (13 finding-specific and one composite), each image replaced by one from another study, usually of the same patient, with question and report fixed. Under an explicit answer instruction, the model's generated answer changes on 4.26 percent of trials with the report and 20.94 percent without it, a paired increase of 16.7 points (patient-clustered 95 percent CI 15.6 to 17.7), so report availability reduces image-swap sensitivity under this protocol; the original prompt with a lowercase first-token readout gives 4.70 percent against 17.07 percent, and substitutions also move continuous answer scores where the binary prediction does not change. The labels are derived from reports, which limits conclusions about visual correctness; the direction replicates in two further model lineages. Code, the exact prompts and a run record for every number are at this https URL.

---


### 304. [Human-Grounded Calibration for Long-Text Image-Text Congruence in Vision-Language Models](https://arxiv.org/abs/2609.15640)

**<font color=#1a73e8>作者：</font>** Alessandro Gambetti, Qiwei Han  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-text image--text congruence scoring is increasingly important for vision-language systems that must evaluate whether detailed textual descriptions match visual content. However, raw similarity scores from dual-encoder models are difficult to interpret as calibrated congruence measures, especially under the modality gap between image and text embeddings. This paper proposes Congruency Score (CS), a lightweight calibration layer that maps image--text similarity evidence into a bounded score. Using DOCCI and Urban1k, we evaluate four frozen vision-language backbones and show that observed reductions in post-projection centroid distance do not uniformly improve image--text retrieval performance. Human-grounded evaluations on DOCCI further reveal a trade-off: direct post-hoc calibration preserves high association with human judgments, whereas selected projection-based configurations can reduce threshold-relevant slope and intercept distortions at the cost of retrieval performance and association strength. These results establish long-text image--text congruence scoring as a calibrated score-estimation problem, where retrieval performance, human association, and threshold calibration must be evaluated as distinct objectives. CS provides a lightweight way to expose and operationalize this separation.

---


### 305. [Principal-timestep Restricted Init via Sparse Matrix-decomposition in Flow-matching](https://arxiv.org/abs/2609.15643)

**<font color=#1a73e8>作者：</font>** Jiayang Gu, Zheng Fang, Lichaun Xiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow-matching diffusion models have recently emerged as a strong paradigm for high-fidelity visual generation. However, their prohibitively high fine-tuning cost limits scalability to downstream tasks. While Low-Rank Adaptation (LoRA) combined with spectral initialization has demonstrated accelerated convergence and improved performance in autoregressive language models by better aligning gradient directions, we find that it fails to deliver similar gains in diffusion fine-tuning, often yielding marginal or even negative improvements over vanilla this http URL attribute this discrepancy to a fundamental mismatch between LoRA's low-rank parameterization and the intrinsically high-rank gradients induced by the flow-matching objective. In particular, stochastic timestep sampling introduces directionally heterogeneous gradient signals across training steps, leading to misaligned updates under low-rank this http URL address this issue, we propose Prism-LoRA,a Principal-timestep Restricted Init via Sparse Matrix-decomposition framework that improves gradient alignment during fine-tuning. Our method consists of two key components: (i) principal timestep selection, which restricts initialization gradients to a subset of dominant timesteps to suppress effective gradient rank, and (ii) principal channel filtering, which removes task-irrelevant channels, enabling the one-step spectral initialization gradient to better align with the long-horizon optimization trajectory. Extensive experiments demonstrate that our method consistently improves both convergence speed and final performance across multiple diffusion fine-tuning benchmarks, including subject-driven generation, controllable generation, and deblurring, achieving not only performance improvement but also earlier stages of convergence over baseline LoRA and other spectral-init methods.

---


### 306. [From Model Patterns to Abstract Semantics in Compositional Zero-Shot Learning](https://arxiv.org/abs/2609.15649)

**<font color=#1a73e8>作者：</font>** Weize Li, Zhicheng Zhao, Fei Su  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Compositional Zero Shot Learning aims to recognize unseen compositions by recombining learned primitives. Recent methods rely on vision language models and attempt to explicitly model contextual variations of primitives through multiple representations. However, such approaches are limited by fixed variant capacity and competition between abstract and concrete semantics. In this work, we present a new perspective that views primitive variations as the context-driven activation of concrete visual cues rather than independent entities. Based on it, we propose CLEAR, a CLoze-style rEAsoning-based Re-ranking framework inspired by human perceptual processes. CLEAR extracts conditional variants from the primitive candidate set in a coarse-to-fine manner, performs cloze-style reasoning to infer high-level semantics, and re-ranks predictions to correct biases toward salient concrete primitives. Extensive experiments demonstrate that CLEAR consistently improves the Base Model and outperforms state-of-the-art methods on the challenging C-GQA and MIT-States datasets. Code is available at this https URL.

---


### 307. [Empathy Is Steerable but Multi-Axial: Mechanism Geometry and Persona Effects in LLMs](https://arxiv.org/abs/2609.15654)

**<font color=#1a73e8>作者：</font>** JuHeon Ha, Byounghan Lee, Yunseo Choi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Activation steering has been used to control traits such as honesty, refusal, and sycophancy, yet supportive empathy is evaluated along multiple dimensions that need not correspond to independently controllable activation directions. Using the EPITOME framework, which decomposes supportive empathy into Emotional Reactions, Interpretations, and Explorations, we study three instruction-tuned LLMs and ask whether candidate directions derived from these labels produce distinguishable intervention effects or instead share structure, and how persona prompts interact with those directions. We find that contrastive activation addition yields a stable middle-layer intervention that consistently shifts the EPITOME proxy scores across models, moving empathy analysis beyond response-level scoring. However, the recovered directions are only partially separable: steering one direction induces off-target shifts, and hand-crafted prompting shifts the empathy profile rather than isolating a single dimension. Persona prompts substantially change EPITOME scores, but a paired activation-shift decomposition shows that the recovered subspace captures only approximately 3 percent of persona-induced squared activation-shift magnitude at layer 15. Under this EPITOME-based definition, expressed empathy is steerable but multi-axial, and controlling persona-conditioned empathy requires targeting structure beyond individual mechanism directions.

---


### 308. [CiteShade: Citation Laundering in Multi-Source Retrieval-Augmented Generation and Its Counterfactual Defense](https://arxiv.org/abs/2609.15660)

**<font color=#1a73e8>作者：</font>** Guo Fuzheng  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) grounds a language model's answers on retrieved external knowledge and returns each answer with citations that identify its sources. Those citations are the user's audit trail: they let a reader verify a claim without trusting the model. Prior security work on RAG asks whether an attacker can corrupt the answer, leaving the citation channel unexplored. We show that this channel is a new and practical attack surface. We propose CiteShade, the first citation laundering attack to RAG, in which an attacker controlling a single source induces a model to produce an attacker-chosen wrong answer and to attribute it to a trusted source that does not support it, while the evidence for the correct answer remains in context. We formulate the attack as an optimization problem, derive three necessary conditions (retrieval, generation, and citation) and construct sources satisfying them without any instruction. On multi-source multi-hop question answering the attack raises the wrong-answer rate from 0.01 to 0.68, and source deletion confirms the malicious source is the causal driver in every measured case. Vulnerability tracks a model's propensity to cite rather than its scale, reaching CLR 0.84 under explicit instruction and 0.64 with no instruction at all on the most citation-prone model tested. We then show that perplexity filtering and citation-support checking are each insufficient, and propose a counterfactual defense that verifies which source actually drove the answer.

---


### 309. [Circuit-MLLM: Topological Logic-Guided Latent-Space Visual Reasoning for Circuit Schematic Understanding](https://arxiv.org/abs/2609.15668)

**<font color=#1a73e8>作者：</font>** Jinyuan Deng, Yuqi Jiang, Wenjing Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Through pre-training on extensive text and image datasets, current multi-modal large language models (MLLMs) achieve strong performance on general tasks. However, circuit schematics present a unique challenge for MLLMs due to their dense component layouts and distinct topological logic, demanding fine-grained structural parsing to extract the electrical semantics. To address this, we propose Circuit-MLLM, a multimodal reasoning framework that reformulates circuit topology analysis as a process of device localization, path tracing, and sequential reasoning within the latent space. We introduce a circuit knowledge mining mechanism that deeply aligns the model's latent representations with structurally rich features derived from multi-granularity circuit vision experts, enabling the model to effectively internalize topological semantics. Building upon these internalized semantics, we devise a topology-guided sequencing strategy that decouples reasoning from the rigid raster-scan order, enforcing stepwise inference along the circuit's topological logic in latent space. Across diverse circuit analysis tasks, Circuit-MLLM consistently outperforms strong baselines, notably achieving a 25% higher average score than GPT-5.1, which demonstrates the effectiveness of our framework in circuit schematic topology analysis. Code is publicly available at this https URL.

---


### 310. [Don't Send What You Don't Need: Question-Guided Token Pruning as a Privacy Defense for Vision-Language Models](https://arxiv.org/abs/2609.15671)

**<font color=#1a73e8>作者：</font>** Md Khalid Syfullah, Alvi Ataur Khalil  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Question Answering (VQA) with Vision-Language Models (VLMs) is increasingly used in privacy-sensitive and bandwidth-constrained settings. Federated Learning (FL), Split Learning (SL), and U-Shaped Split Learning (USL) keep raw data local, but transmitting all visual tokens across a model partition remains costly and can expose private information. We propose QPriv-VL, a question-guided, privacy-aware token-pruning framework for FL, SL, and USL that prunes visual tokens before transmission based on task utility and privacy sensitivity. Its core component is a lightweight Dynamic Threshold Predictor (DTP) that jointly estimates a sample-specific pruning ratio and a token-level retention mask in one forward pass. DTP combines question relevance, computed from cross-modal similarity between visual patches and the pooled question embedding, with a sensitivity signal derived from frozen DINOv2 features. This allows the model to suppress potentially sensitive regions while preserving patches useful for answering the question, without requiring sensitivity labels. We evaluate QPriv-VL on GQA, OK-VQA, VQAv2, SLAKE, VQA-RAD, and PathVQA against four privacy attack families: FSHA, FORA, iDLG, and attribute-inference membership inference attacks. DTP matches or outperforms fixed-ratio pruning while using substantially fewer transmitted tokens. On VQA-RAD, it reduces membership-inference attack success from 0.99 to 0.76-0.79, lowers FSHA and FORA reconstruction PSNR relative to fixed-ratio pruning, and preserves competitive VQA accuracy using about 40% of the original visual-token budget. A sensitivity exclusion ratio of 1.20 +/- 0.18 indicates preferential removal of privacy-sensitive patches, while explainability analysis shows that retention adapts to question semantics rather than generic visual saliency.

---


### 311. [V-ICAL Bench: Evaluating Video In-Context Learning for Multimodal Agents in Interactive Environments](https://arxiv.org/abs/2609.15683)

**<font color=#1a73e8>作者：</font>** Ziqian Fan, Shibo Xu, Junjie Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While In-Context Learning (ICL) enables models to adapt from exemplars without parameter updates, multimodal ICL remains largely underexplored, particularly regarding video demonstrations in interactive environments. For multimodal agents, learning from videos presents unique challenges: they must translate in-context demonstrations into executable policies, ground these policies in novel visual states, and iteratively refine actions based on environmental feedback. We introduce V-ICAL, a novel benchmark designed to evaluate video-based ICL for multimodal agents. Comprising 342 interactive tasks across 37 environments, V-ICAL utilizes human-curated demonstration videos as task-specific behavioral exemplars, evaluating agents through sustained interaction from a target initialization. The benchmark seamlessly connects in-context knowledge induction with core agentic capabilities, including state grounding, temporal memory, planning, and adaptation in dynamic environments. Extensive evaluations across 19 state-of-the-art multimodal agents reveal significant limitations: the best-performing model, Seed-2.1-Pro, achieves a score of only 54.4/100, while other leading models (e.g., Gemini-3.1-Pro, GPT-5.6) fail to surpass 50, far below the human baseline of 83.6. Controlled comparisons further demonstrate that current agents struggle to reliably translate video exemplars into effective policies, failing to yield consistent performance gains. Ultimately, V-ICAL exposes a critical gap in the ICL capabilities of multimodal agents, underscoring an urgent need for future research.

---


### 312. [RESKILL: Explicit Failure Attribution and Structured Repair for Interactive Language Agents](https://arxiv.org/abs/2609.15684)

**<font color=#1a73e8>作者：</font>** Mengyi Deng, Xin Li, Duyi Pan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language agents increasingly rely on reusable skills, but post-failure repair is often handled by opaque one-shot reflection: a model generates a skill patch without explicitly maintaining how failure explanations relate to candidate repairs or how unsuccessful retests should influence later edits. We introduce RESKILL, a structured repair framework that maintains an explicit repair state across repair rounds. Given a failed rollout, the framework links failure hypotheses to candidate skill patches, selects local repairs through coverage-based attribution, retests the edited skill set in the environment, and uses retest outcomes to guide subsequent repair updates. The language model supplies structured repair factors, while the repair procedure records them, compares local skill patches by how well they address active failure explanations, and carries unsuccessful retest outcomes into later repair rounds. We evaluate RESKILL on ALFWorld and TextCraft across three model sizes under fixed repair budgets. RESKILL obtains the strongest final success in all six benchmark-model settings, improving average final success by 3.7 percentage points over direct repair and 3.3 points over hypothesis-conditioned repair. These results suggest that explicit attribution alone is insufficient; durable improvement emerges when attribution is integrated with repair selection and persistent retest-conditioned update.

---


### 313. [EEG-Xplain: Decoding Neural Black-Boxes of EEG Foundation Models](https://arxiv.org/abs/2609.15687)

**<font color=#1a73e8>作者：</font>** Hansong Ma, Junxiao Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> EEG foundation models such as BIOT, LaBraM, and EEGMamba have achieved remarkable performance in neural signal decoding, but their black-box nature limits clinical trust and neuroscientific validation. We propose a unified attribution framework for interpreting EEG foundation models across heterogeneous architectures. The framework integrates gradient-, perturbation-, and activation-based explanation methods to analyze model behavior in spatial, temporal, and frequency dimensions. Spatially, it identifies critical EEG channels and visualizes their distributions using topographic maps. Temporally, it highlights decision-relevant signal segments through attribution heatmaps. In the frequency domain, it quantifies the contributions of canonical EEG rhythms via spectral perturbation analysis. To assess explanation reliability, we introduce a population-level evaluation combining Area Over the Perturbation Curve (AOPC) and cross-method consistency analysis. The framework further leverages Large Language Models (LLMs) to transform structured attribution outputs into natural-language reports, bridging low-level neural representations and high-level semantic reasoning. Experiments on benchmark datasets, including Mumtaz2016 and TUAB, demonstrate that the generated explanations are consistent with established neurophysiological markers, validating meaningful neural representations while exposing potential dependencies on artifacts and spurious patterns. The proposed framework provides a standardized approach for evaluating the interpretability, reliability, and physiological plausibility of EEG foundation models.

---


### 314. [NoteVQA: Benchmarking VLMs on Real-Life Questions from Human Communities](https://arxiv.org/abs/2609.15695)

**<font color=#1a73e8>作者：</font>** Haonan Jiang, Guojian Zhan, Jiancong Xie 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) increasingly power consumer-facing AI search, yet evaluating them on the diversity of everyday visual questions remains challenging. Existing benchmarks often target predefined capabilities, such as multi-hop retrieval or long-form synthesis, whereas users ask photo-grounded questions spanning a long tail of everyday scenarios. Despite advances in VLMs, users on Xiaohongshu, a mainstream Chinese image-sharing platform, continue to turn to other people for help with everyday visual questions. Motivated by this behaviour, we curate NoteVQA from these questions, yielding 252 items across 12 topical categories and 7 user intents. Each item includes a concise reference distilled from expert community responses and a human-audited interleaved reference answer that combines textual explanations with supporting visual evidence. We evaluate both short-answer correctness and interleaved-answer quality. To support the latter, we introduce AgenticInterleave, a single-agent ReAct framework for retrieval-supported answer generation, together with IVR-12, a 12-dimensional rubric for assessing the content, presentation, and image quality of interleaved references and model outputs. Across 10 frontier VLMs, the highest short-answer accuracy is 52.8\%, while adding agentic search to Qwen3.5-397B-A17B improves accuracy by only 2.0\%. For interleaved answers, the same model running AgenticInterleave scores 3.52 under IVR-12, compared with 4.65 for the human-audited references, with the largest gap in content quality. These results highlight the challenges that everyday visual questions pose for current VLMs in both answer accuracy and the quality of visually grounded explanations.

---


### 315. [More Than Just Access: Generative AI as Communication Intermediary for Blind and Low-Vision Users](https://arxiv.org/abs/2609.15696)

**<font color=#1a73e8>作者：</font>** Protik Dey, Mohd Saifuzzaman, Taslima Akter  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI (GenAI) tools are increasingly woven into how blind and low-vision (BLV) people communicate, not only with digital information, but with the physical world and with other people. Tools such as ChatGPT, Google Gemini, Be My AI, and Seeing AI translate visual and textual content into accessible form, and are beginning to substitute for interpersonal requests for help, such as asking a family member to read a label or describe a scene. Drawing on semi-structured interviews with 19 BLV participants, we examine GenAI as a communication intermediary and how it succeeds and fails as an alternative for reading, describing, and even asking another person for help. We also investigated what BLV users gain and risk when these tools take over that role. We conclude with design and policy implications for GenAI systems that communicate uncertainty honestly, protect information, and support BLV users' independence rather than substitute for it unsafely.

---


### 316. [Beyond Accuracy: Robustness, Cost, and Governance Trade-offs for Vision-Language Models in Templated Document Extraction](https://arxiv.org/abs/2609.15706)

**<font color=#1a73e8>作者：</font>** Kushal Patel, Pushkal Shrivastava, Mackenzie Lees 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly used to extract structured fields from business documents, yet most evaluations report accuracy on clean benchmarks and offer little guidance to practitioners choosing an approach for a given task complexity. We address this gap with a measurement-grounded study and an open-source release. Across eleven systems (three commercial, two reasoning, five open-source VLMs in pretrained and fine-tuned form, and a non-LLM OCR->regex floor) scored on a 750-document held-out pool of synthetic checks, fine-tuning on 3K samples lifts the best open-source VLMs above F1 0.98-above every zero-shot commercial system on this task-while GPT-5 leads the commercial pool on F1 and Claude Sonnet 4.5 collapses on Date. To turn these measurements into actionable choices, we introduce a practitioner-oriented selection framework that maps a task profile (quality, latency, governance, volume) to a recommended approach via filtering and total-cost minimization, illustrated on a hypothetical mid-volume document-extraction scenario.

---


### 317. [New Conditions for Philosophers to Catch the Wave of Citizen Deliberation in the Age of Artificial Intelligence in advance](https://arxiv.org/abs/2609.15707)

**<font color=#1a73e8>作者：</font>** Bernard Reber  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Powerful technologies labeled ``AI''-without sufficient epistemic caution-are already reshaping political and private life, bringing both new dangers and new opportunities for citizen participation. These range from electoral and legislative engagement to the most ambitious form: political co-creation through citizens' assemblies. Large Language Models (LLMs) could support such processes through moderation, translation, facilitation, summarization, and writing assistance. But this potential remains largely unrealized. The Democratic Commons project takes a fundamentally interdisciplinary approach-from philosophy to computer science-to evaluate LLMs against five proposed democratic principles. At its core, the project is driven by the question of political bias: under what conditions can LLMs be used democratically within forms of citizen participation that are them- selves still largely experimental? Addressing these socio-technical questions requires grounding in political theory and, more broadly, in philosophy-disciplines that provide the normative frameworks without which the democratic evaluation of AI systems cannot be mean- ingfully conducted.

---


### 318. [Predicting build orientation for SLM dental parts: a comparison of rotation representations and direct vector regression](https://arxiv.org/abs/2609.15710)

**<font color=#1a73e8>作者：</font>** Felix Schmalzel, Reimar Waitz, Moritz Kronberger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Build orientation for selective laser melting (SLM) manufacturing of dental parts is usually chosen manually by technicians. We treat orientation prediction as supervised machine learning of the part's up-axis from technician-labeled production data, and test which rotation representations produce the best results. Using $n\approx2400$ patient-specific dental parts, we trained a ResNet-50 multi-view image backbone and a PointNeXt-S point-cloud backbone, both pretrained and fine-tuned end-to-end, on 13 up-axis representations spanning six classical $SO(3)$ parameterizations and seven representations defined directly on the unit sphere $S^2$. We report the geodesic angular error between predicted and ground-truth up-axis on a test set, with and without test-time augmentation (TTA) over $K=21$ known rotations. With TTA, the octahedral map achieves the lowest mean angular error ($10.6^\circ$, ResNet-50). The three lowest-error results overall are direct $S^2$ representations, though this may reflect label noise in the unsupervised in-plane component of the $SO(3)$ targets rather than a topological advantage. von Mises-Fisher collapses to a near-constant prediction when trained with PointNeXt-S but not with ResNet-50. TTA reduces mean angular error by 31-73 % across almost every representation and backbone. Overall, test-time augmentation over a small set of known rotations is the most consistent driver of accuracy, whereas the best-performing representation is strongly backbone-dependent.

---


### 319. [Knowledge-Enriched Structured EHR Features for 30-Day Hospital Readmission Prediction on MIMIC-IV](https://arxiv.org/abs/2609.15713)

**<font color=#1a73e8>作者：</font>** Mohamad Najafi, Hongyun Fu, Mathias Brochhausen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent approaches to 30-day hospital readmission prediction rely on pre-trained language models applied to discharge summaries. Although these methods achieve strong performance, they depend on the availability of clinical notes, incur substantial computational costs, and yield representations that lack interpretability. We propose a knowledge-enriched feature representation that augments structured Electronic Health Record (EHR) data with four medical knowledge sources: disease ontology mapping, procedure classification, drug ingredient vocabulary, and organ system laboratory aggregation, without using clinical notes. Each feature dimension corresponds to a named clinical concept, yielding a sparse and interpretable patient representation. The approach is evaluated with six classifiers on a MIMIC-IV v2.2 cohort. Under 20-fold cross-validation, the best configuration achieves an AUROC of 0.743. This performance is comparable to that of previously reported methods on this dataset, including both those using only structured data and those incorporating clinical notes, while requiring considerably less computational cost. Interpretability analysis shows that demographics, organ system labs, drug ingredient features, and first-level ontology disease categories drive prediction, while deeper hierarchy levels contribute negligibly. These findings indicate that knowledge-enriched structured features offer a competitive and efficient alternative to embeddings from clinical notes for 30-day readmission prediction.

---


### 320. [Assembling the CREW: A Collaborative Multi-agent Reinforcement Learning Framework for Automated Related Work Generation](https://arxiv.org/abs/2609.15721)

**<font color=#1a73e8>作者：</font>** Hai-Dang Dang, Bao-Yen Pham, Bao Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automatic Related Work Generation (RWG) significantly reduces the human time and effort required to author the Related Work Section (RWS) of a research paper. However, prior methods leveraging multi-agent Large Language Models (LLMs) typically rely on a predefined workflow, where each agent is responsible for a specific step in the entire process. This rigid, static inter-agent coordination limits the adaptive collaboration required to synthesize complex scientific literature. To address this limitation, we propose CREW (Collaborative Reinforcement Learning for Related Work Generation), a novel framework where LLM agents bypass heuristic pipelines to dynamically coordinate by autonomously selecting actions, such as Retrieve, Disseminate, Compose, and Critique, driven by a policy optimized via Independent Proximal Policy Optimization (IPPO). Extensive experiments on a standard RWG benchmark demonstrate that our approach yields substantial quality improvements over strong existing baselines, while significantly reducing token costs. Code is available at this https URL

---


### 321. [Data storytelling meets interpretable machine learning: Decoding AI decisions for non-experts without revealing sensitive data and model details](https://arxiv.org/abs/2609.15722)

**<font color=#1a73e8>作者：</font>** Lemen Chao, Zixuan Yang, Anran Fang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI-driven automated decision-making requires both predictive performance and interpretability. Recent advances in interpretable machine learning (IML) provide tools for explaining model predictions, but the technical complexity of these explanations may hinder accessibility to non-experts. To address this challenge, this study integrates data storytelling with IML to enhance the explainability of AI-generated decisions for a broader audience. Following the design science research (DSR) paradigm, this study proposes a formal definition of data storytelling in IML, introduces the DIST Pyramid to align data storytelling with IML, and presents the I-P-O Model to describe their interactions. It further develops an architecture to explain AI decisions through distinct "What-if" and "Why-not" event-generation processes. The architecture also employs data desensitization to protect sensitive input data. To validate the approach, a case study is conducted with the Boston Housing dataset, using SHapley Additive exPlanations (SHAP) values and large language models (LLMs) to generate data stories with And-But-Therefore (ABT) structures. An empirical evaluation shows that 76.4% and 74.3% of respondents rated the "What-if" and "Why-not" data stories as more comprehensible, with significantly higher accessibility scores than traditional SHAP visualizations. The paper concludes with the presentation of a narrative interpretation framework that integrates IML and data storytelling, thereby expanding the research scope as well as the practical applicability of AI decision-making.

---


### 322. [Are LLMs Good Financial User Simulators? A Preliminary Study](https://arxiv.org/abs/2609.15727)

**<font color=#1a73e8>作者：</font>** Jiajie He, Jiangyuan Hong, Dongling Ni 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as user simulators, but their ability to reproduce evolving individual financial decisions remains unclear. We present a preliminary study in a controlled paper-trading environment with 120 volunteers. Participants used non-redeemable virtual funds under real-time market conditions; no real brokerage accounts, real-money positions, or real transaction records were accessed. Given only information available before a prediction cutoff, a simulator predicts the participant's next-trading-day action, traded security, and transaction quantity. We evaluate temporally aligned rolling predictions and compare settings with and without point-in-time market information. Market context improves action and ticker prediction in the controlled ablation, while transaction sizing remains difficult. We also observe systematic behavioral compression: models overproduce hold actions, underpredict sell decisions, and simplify multi-security transactions. These results provide an initial empirical characterization and motivate larger-scale evaluation of individual, temporal, and portfolio-level behavioral fidelity.

---


### 323. [Merging the Knowledge of LLMs for Automatic Speech Recognition](https://arxiv.org/abs/2609.15743)

**<font color=#1a73e8>作者：</font>** Hayato Futami, Tatsuya Kawahara  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic speech recognition (ASR) systems, trained on paired speech-text data, have been improved by leveraging language models (LMs) trained on text-only data. LM fusion methods such as shallow fusion and density ratio are well-established methods that incorporate external LMs during ASR decoding. However, they incur additional computational costs due to LM inference, which is particularly problematic for recent larger LMs. In this study, we propose incorporating external LMs via model merging. This method integrates the LMs directly into the parameters of an LLM-based ASR model, requiring no additional computational cost at inference. We formulate domain extension and transfer via arithmetic operations on LoRA parameters. Experimental evaluations were conducted for the domain adaptation of LLM-based ASR trained on CSJ and LibriSpeech. We show that our LM merging consistently improved the ASR performance in the target domains, without degrading inference speed or memory footprint.

---


### 324. [Look Before You Leap: Factual Decoding with Internal Attribution Signals](https://arxiv.org/abs/2609.15745)

**<font color=#1a73e8>作者：</font>** Hayeong Ryu, JungMin Yun, Byeonggeuk Lim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hallucination remains a critical challenge in large language models (LLMs), where early factual errors compound through autoregressive generation in a snowballing effect that neither post-hoc correction nor weight-level intervention can effectively preempt. We propose DescaPE (DEcoding Signal Control Against Path Error-snowballing), a decoding framework that leverages internal model signals to suppress hallucination-prone trajectories at inference time. Through sliding-window MLP ablation, we identify a factual-salient layer span within LLMs whose derived signal is selectively elevated for factual tokens and exhibits anomalous spikes at hallucination-prone steps. We train a lightweight probe to approximate this signal from a single forward pass and integrate it into candidate scoring to penalize high-risk continuations while rewarding factually grounded ones. Experiments across five factuality benchmarks on three LLMs demonstrate that DescaPE achieves factuality improvements over decoding-time baselines in multiple settings, while incurring only 1.10x latency overhead in our efficiency evaluation. Our code is available at this https URL.

---


### 325. [EvoOntology: A Self-Evolving Ontology Layer for Data Agents](https://arxiv.org/abs/2609.15779)

**<font color=#1a73e8>作者：</font>** Meiduo Chong, Shaolei Zhang, Ju Fan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Data agents aim to fulfill natural-language instructions over heterogeneous data, including tables, files, and databases. However, data agents face a challenging agent-data gap: heterogeneous data resides outside the agent, while the agent can access it (e.g., column names and file paths) only through generic tools. Existing approaches either let agents directly explore raw data sources or inject manually constructed semantic layers into prompts. However, neither scales well to large heterogeneous data sources nor adapts to different agent behaviors. In this paper, we introduce EvoOntology, a self-evolving ontology layer for data agents. EvoOntology encapsulates the ontology as an MCP server comprising a schema layer, a content layer, and a tool layer, enabling agents to actively query and interact with the ontology at runtime. To this end, we introduce a builder agent for autonomous ontology construction and a self-evolution loop that continuously refines the ontology through attribution-guided typed edits that are accepted only after a backbone-conditional paired evaluation. Experiments on three well-adopted data-agent benchmarks with four LLM backbones demonstrate that EvoOntology consistently outperforms strong baselines and existing semantic-layer approaches, effectively bridging the agent-data gap and enabling more effective interaction with heterogeneous data. Code: this https URL

---


### 326. [Navigating Sparse Evidence: Agentic Visual RAG via Explicit Context Selection and Consolidation](https://arxiv.org/abs/2609.15800)

**<font color=#1a73e8>作者：</font>** Yucheng Shen, Lingyong Yan, Jiulong Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Visual Retrieval-Augmented Generation (VRAG) empowers models to navigate and answer queries about visually rich documents by retrieving relevant page images as visual evidence and reasoning over their content. However, effectively utilizing this visual evidence is usually impeded by two main challenges. First, answer-relevant evidence is sparse and may be concentrated in a small region of one page or dispersed across multiple pages. Second, existing agentic methods often generate answers based on raw exploration trajectories or compressed textual memories rather than an explicitly organized set of supporting images, making answers susceptible to exploration noise and obscuring the evidence-backed reasoning trace. We argue that the bottleneck lies not only in evidence discovery but also in its preservation and organization before answer generation. We propose SCoRE (Selection and Consolidation for Robust Evidence), a unified agent loop for explicit evidence selection and consolidation. During exploration, SCoRE retains only query-relevant observations and their source pointers in a maintained textual ledger, preserving earlier evidence while keeping the visual context bounded. At termination, it reloads the referenced original images and consolidates the visual evidence for answering, arranging it into a logical sequence. This decouples final reasoning from exploratory trial-and-error while ensuring strict visual grounding via indexed claim-to-image linkages. To enable end-to-end optimization of this unified rollout, our training paradigm combines filtered cold-start trajectory distillation with evidence-aware reinforcement learning, whose reward promotes evidence coverage, consolidation compactness, and answer correctness.

---


### 327. [Atria Dawn: The Dawn of Agentic Superintelligence](https://arxiv.org/abs/2609.15818)

**<font color=#1a73e8>作者：</font>** Honglin Guo, Tao Gui, Yicheng Chen 等 100 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI agents become participants in the development of their successors, they reshape both the production of intelligence and the role of human researchers. We introduce Atria Dawn Preview, a foundation agentic language model designed for scientific research and engineering workflows, with the goal of expanding the frontier of agent productivity in the real world. This model is trained via a Verifiable Experience Pipeline that connects tool-mediated interactions to executable environments and externally verified outcomes. Across 16 benchmarks spanning real-world research, engineering, and digital work, Atria Dawn Preview is competitive with frontier agents and achieves the highest reported score on five of them. Beyond standalone performance, we examine the real research-and-development process behind this model as a case study of human--AI collaboration, analyzing 769 task records from 56 participants together with agent logs. When asked to evaluate completed tasks under comparable conditions, participants rated about one-third of completed AI-assisted tasks as infeasible without AI. More strikingly, agents frequently propose methods and implement revisions, while humans retain most final decisions and guide exploration through judgment and feedback. These observations indicate a shift from task-level execution to project-level partnership, with human effort concentrating on what is worth pursuing and how evidence should guide research. Progress toward more autonomous AI research must therefore advance both the capacity for discovery and the capacity for meaningful human oversight, preserving accountable human authority over the risks and direction of continued development.

---


### 328. [AlgoEvo: Self-Evolving Agentic Search for Automated Algorithm Discovery](https://arxiv.org/abs/2609.15820)

**<font color=#1a73e8>作者：</font>** Junhao Qiu, Qinglong Hu, Xialiang Tong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models have advanced automated algorithm discovery by synthesizing executable code, but existing frameworks trap them in rigid search pipelines with pre-defined control flows. This limitation restricts adaptive reasoning, blocks cross-paradigm transfer, and discards valuable execution feedback. We propose AlgoEvo, a unified agentic framework that transforms automated algorithm discovery into an interactive, knowledge-accumulating process. An autonomous agent dynamically inspects, diagnoses, and edits code based on runtime feedback. A design skill hub decouples paradigm-specific knowledge from the core discovery engine, allowing a single workflow to seamlessly handle single-objective, multi-objective, and multi-component design. Meanwhile, a hierarchical experience mechanism organizes search trajectories into a task-level tree to guide exploration and consolidates cross-task patterns into reusable skills. Across six representative benchmark tasks, AlgoEvo matches or surpasses specialized methods with substantially fewer evaluations and reduced token consumption, demonstrating strong intra-task accumulation, cross-task transfer, and the ability to reproduce or exceed existing state-of-the-art performance through flexible skill activation.

---


### 329. [CiteGuard-RAG: A Validation-Centered AI System for Evidence-Grounded Question Answering](https://arxiv.org/abs/2609.15830)

**<font color=#1a73e8>作者：</font>** Sumit Barua, Guan Hong, Halil Dursunoglu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) can improve access to complex information; however, retrieving evidence alone does not ensure that answers are grounded, citation-valid, or appropriately refused. This paper introduces CiteGuard-RAG, a validation-centered AI system for evidence-grounded question answering. The system integrates hybrid semantic-lexical retrieval, citation-constrained generation, sentence-level grounding validation, and single-pass regeneration. Validation is used at runtime to determine whether a candidate answer should be accepted, refused, or regenerated before final delivery.
CiteGuard-RAG is evaluated on 400 questions across a controlled housing-law dataset, PrivacyQA, and CUAD. In the controlled evaluation, it achieves 99.1% retrieval accuracy, 98.3% grounded-answer accuracy, and 98.3% citation validity, with no validation-detected hallucinations. Ablation results show that grounded-answer accuracy drops sharply when validation is removed, even when retrieval accuracy remains unchanged. External evaluation shows that while citation validity remains strong, evidence utilization, span alignment, and refusal calibration become harder under domain shift.
These findings indicate that trustworthy RAG systems require explicit validation between retrieval and final answer delivery. CiteGuard-RAG provides a practical architecture for linking retrieval, generation, citation checking, abstention, and regeneration in high-stakes information access.

---


### 330. [Per-Matrix Optimality Is Not Enough: Three-Level Optimization for Low-Rank LLM Compression](https://arxiv.org/abs/2609.15838)

**<font color=#1a73e8>作者：</font>** Huicheng Zhang, Xiyao Feng, Ze-Tong Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Per-matrix singular value decomposition (SVD) truncation is Eckart-Young optimal in the whitened Frobenius norm, but errors from independently compressed matrices compound through the block's nonlinear forward pass. Inspired in part by hierarchical variational optimization in quantum many-body methods, we introduce a three-level chain that widens optimization scope from individual matrices to Transformer blocks to the full model: whitened SVD~(L1), block-level joint optimization~(L2), and end-to-end language-modeling loss refinement~(L3), all from 256 calibration sequences, with no instruction or recovery data. On LLaMA-7B at 60% compression, the chain reduces WikiText-2 perplexity from 42.1 to 19.1 to 11.4. The block-level stage acts as a regularizer: skipping it worsens Penn Treebank (PTB) perplexity by 24 points, a gap that additional end-to-end training did not close in our experiments. Perplexity gains hold across 20-80% compression, five architectures up to 13B parameters, and both in-distribution and out-of-distribution benchmarks, though the cross-architecture rows use architecture-specific configurations and the ratio sweep was not run under one common protocol. With more calibration data, skipping the block-level stage becomes competitive, revealing an offline compute--data trade-off. We therefore claim improvements only in perplexity and compression fidelity; downstream accuracy remains well below the dense model.

---


### 331. [Before You Poll with LLMs: A Deliberative Diagnostic Framework](https://arxiv.org/abs/2609.15849)

**<font color=#1a73e8>作者：</font>** Ahmed Wali, Hassaan Tayyab  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Can LLMs reason through new information like humans, or do they merely retrieve cached opinions? This is critical for silicon sampling, where LLM personas simulate public opinion at scale. Current evaluations test only whether personas hold the right opinions -- a static snapshot. But opinion research increasingly depends on dynamic fidelity: whether personas update beliefs in response to new arguments, as humans do during deliberation. No existing benchmark tests this. We introduce the Deliberative Polling Diagnostic Framework, which compares human and LLM belief shifts after identical informational interventions. Grounded in deliberative polling, it surfaces failures invisible to static evaluation: models that produce plausible partisan opinions can still misrepresent how those opinions change. Applying the framework to five frontier models using data from America in One Room (526 personas, 72 questions), we find that every model fails, each in a unique manner. GPT-5.1 exhibits reversal: its personas become more hostile toward the opposing party after balanced information, while humans become less so. This reversal is selective (80% on outgroup vs. 26% on policy questions) and symmetric across partisan identities. Gemini 2.0 Flash, Claude Sonnet 4.5, and Llama 3.3 70B exhibit overshoot, shifting correctly but at 5-7x human magnitude. DeepSeek V3 exhibits rigidity with near-zero change. Targeted ablations reveal that policy content triggers these failures and that they are identity-specific: GPT-5.1 reverses on outgroup questions but overshoots on ingroup; Gemini shows the inverse. We term this signature self-sycophancy: conformity to the model's internal stereotype of the persona rather than reasoning from the information provided. Our framework offers a concrete protocol: run the deliberative diagnostic before trusting LLM personas to mimic revised beliefs.

---


### 332. [Learning to Coach for Experiential Learning](https://arxiv.org/abs/2609.15851)

**<font color=#1a73e8>作者：</font>** Guanheng Chen, Tianzhu Ye, Li Dong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models can learn from experience, but raw solution trajectories are often too long and noisy to provide effective guidance. In this work, we propose Learning to Coach (L2C), a framework that trains a dedicated LLM-as-a-Coach to extract actionable experiential knowledge from an actor model's previous trajectory. The actor remains frozen, while the LLM-as-a-Coach is trained to maximize a reward given by the correctness of the actor's guided response. We study two such rewards: a same-instance reward, which improves subsequent responses on the original problem, and a cross-instance reward, which elicits knowledge that transfers to other instances. Across mathematical reasoning and interactive text-games, L2C consistently outperforms self-refinement and an untrained LLM-as-a-Coach. Running experiential learning for more iterations further improves accuracy and uses additional inference compute more effectively than enlarging the actor's decoding budget. The trained LLM-as-a-Coach also transfers to out-of-distribution tasks and adapts its guidance to the specific actor it coaches.

---


### 333. [K-Bench: a clinically calibrated benchmark for evaluating large language models in high-risk mental health conversations](https://arxiv.org/abs/2609.15855)

**<font color=#1a73e8>作者：</font>** Laura M. Vowels, Matthew J. Vowels, Shivali Sharma 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> % !TEX root = ../main.tex People increasingly use large language models (LLMs) for mental health support, yet their safety in evolving, high-risk conversations remains poorly characterised. We developed K-Bench, a clinician-calibrated, protected benchmark evaluating 125 model configurations representing 33 base models from 14 providers across a fixed cohort of 200 multi-turn vignettes involving suicide, self-harm, domestic violence, substance misuse, and no-risk presentations. Synthetic patient conversations showed substantial distributional overlap with real human-AI conversations. A frozen GPT-4o judge achieved 94.2% exact agreement with clinician consensus across 6,751 eligible item comparisons from 151 clinician-rated transcripts. Leading models combined strong supportive conversation with combined-risk scores above 95, whereas risk exploration exposed substantial variation among lower-performing configurations. Therapeutic prompting produced configuration-specific gains concentrated among weaker models, while elevated reasoning produced no average improvement. K-Bench combines broader clinical coverage and configuration-scale comparison with a continuously updated public leaderboard whose operational test materials are protected from direct optimisation. The leaderboard is available at this http URL.

---


### 334. [Towards Scalable Measurement of Durable Skills](https://arxiv.org/abs/2609.15864)

**<font color=#1a73e8>作者：</font>** Amir Globerson, Amy Keeling, Anisha Choudhury 等 40 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Durable skills, such as collaboration, creativity and critical thinking, are instrumental to success in the modern workforce. Yet, measuring these skills remains a persistent challenge. Moreover, because what is not measured is often not taught, these skills are often overlooked in mainstream educational curricula. Designing effective assessments for these skills necessitates balancing two often-conflicting requirements: ecological validity and psychometric rigor. On the one hand, the assessment environment should emulate natural real-world human interaction between humans. On the other hand, it should be scalable, controllable and reproducible. Here we argue that LLMs can be used to better capture both of these aims. Concretely, we develop a framework where the subject converses with AI teammates in a way that resembles human-human interaction for authenticity, while also offering the psychometric control required for informative and robust assessment. Importantly, the AI participants not only act as teammates but also, in an "Executive LLM" setup, steer the conversation towards eliciting a high density of observable evidence for skill proficiency. We complement this with an AI evaluator that can be used to measure skill proficiency in such interactions. We evaluate our assessment protocol based on transcripts of interactions of human participants with our AI framework, for multiple durable skills. For the skill of creativity, we further demonstrate the efficacy of an autorater for evaluating complex tasks performed by real students. Our analysis shows that the use of the Executive LLM significantly increases elicited evidence and that LLM-automated scoring of conversations largely agrees with that of expert annotators. This research demonstrates the utility of orchestrated LLMs approaches for measuring complex social and cognitive constructs in a scalable and controllable manner.

---


### 335. [LLM-Based Schema-Aware Split Learning for Privacy-Preserving Mental Distress Prediction Across Heterogeneous Surveys](https://arxiv.org/abs/2609.15871)

**<font color=#1a73e8>作者：</font>** Md Khalid Syfullah, Alvi Ataur Khalil  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rising societal and lifestyle complexity has been linked to a growing prevalence of mental distress worldwide. Educational institutions, workplaces, clinics, etc. collect large volumes of mental health survey data to understand and reduce this burden. Collaborative analysis of such data could yield effective generalizable predictive models. Privacy constraints and varied survey designs (i.e., different questions, scales, and formats) hinder direct integration. We propose a schema-aware split learning (SL) framework that preserves privacy, using a large language model (LLM) as a shared semantic encoder to harmonize heterogeneous survey schemas across institutions. We serialize each survey record into a natural-language description, unifying disparate survey schemas into a common format. The LLM is fine-tuned for mental distress assessment via Low-Rank Adaptation (LoRA) and partitioned across client and server. Clients retain the raw survey responses locally and run only a lightweight front-end, so original records never leave the institution that collected them. The resource-intensive backbone runs on the server, minimizing client-side computation. Using LLaMA-3.2-3B-Instruct, the framework attains an average ANLS of 0.708 with only 2,000 training samples, surpasses federated learning (FL) in eight of nine settings, and cuts per-client computation by three orders of magnitude, while generalizing to unseen datasets. Overall, it enables accurate, privacy-preserving, and resource-efficient collaborative learning from heterogeneous mental health survey data.

---


### 336. [Inoculation Midtraining with Learned Neologisms](https://arxiv.org/abs/2609.15886)

**<font color=#1a73e8>作者：</font>** Kyle O'Brien, Edward James Young, Puria Radmard 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often learn both desirable and undesirable properties during post-training. We study whether midtraining, an earlier training stage, can shape which of these properties later generalise. We introduce Inoculation Midtraining, a technique that teaches a base model that unsafe behaviour belongs to a designated <quarantine_token> context, as indicated by the <quarantine_token> neologism (a new token) introduced during midtraining, and then post-trains the model on unsafe data within that context. We then evaluate the model outside the context, with the <quarantine_token> neologism excluded from the system prompt. Across supervised fine-tuning and reinforcement learning post-training regimes, we find that Inoculation Midtraining can reduce misalignment while preserving the transfer of benign data properties (e.g., speaking in German or Shakespearean prose). However, our approach does not outperform standard Inoculation Prompting, is sensitive to training configuration, and produces a leaky boundary that nearby contextual cues can reactivate. These results show that inoculation with a learned association introduced via midtraining can shape selective generalisation. Still, more work is needed before this approach can become a load-bearing component in a developer's safety framework.

---


### 337. [The Model Proposes, the Code Disposes: A Pre-Registered Ablation of a Verifier-and-Acceptance Stage in an LLM-Orchestrated Offensive-Security Agent](https://arxiv.org/abs/2609.15887)

**<font color=#1a73e8>作者：</font>** Theodoros Moutesidis  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We evaluate whether a verifier-and-acceptance stage - a model verifier whose verdicts are enforced by deterministic code - changes what an LLM-driven offensive-security agent reports. We report a 15-run exploratory pilot, a pre-registered 20-run confirmatory ablation, and a pre-registered 2 x 2 factorial study with 40 runs across two deliberately vulnerable lab targets. In the confirmatory study, removing the stage eliminated pre-report suppression (median 2 versus 0 findings per run; exact one-sided p = 0.00003) and reduced model-blinded shipped precision (median 0.471 versus 0.353; p = 0.0087). Recall against a frozen but incomplete ground-truth list did not differ significantly (two-sided p = 0.158; equivalence was not established). The factorial study attributed suppression to the model verifier (Holm-adjusted p = 0.004); deterministic acceptance rules alone suppressed no false positives, and no interaction was detected (p = 0.72). The full design retained 93.8% of model-adjudicated true candidates but did not meet its pre-registered non-inferiority criterion because the lower one-sided 95% bound was 0.875, below the 0.90 floor. Across the confirmatory and factorial studies, an instrumented canary recorded zero contacts in 60 of 60 runs, with incidental external contacts disclosed separately. Independent human adjudication of the retained blind packets is pending, so precision and sensitivity endpoints are supporting rather than final evidence. Six audit-trail failures, including one in the evaluation tooling, are also disclosed. The results support a narrow conclusion: the verifier changes what the system ships, while deterministic code supplies enforcement and auditability; they do not establish superiority to other agents or generalization beyond lab targets.

---


### 338. [Discrete Beckmann Transport Models for One-Step Language Modeling and Reasoning](https://arxiv.org/abs/2609.15903)

**<font color=#1a73e8>作者：</font>** Sophia Tang, Shiyi Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion and flow models are a promising alternative to autoregressive language models, but compressing many-step sampling into fewer steps typically requires distilling a pretrained teacher model. This caps the student at the teacher's quality and requires a costly two-stage training pipeline. We introduce Discrete Beckmann Transport Models (DBTM), built on a time-independent flow whose autonomous transport map provably carries any point in the ambient space to a fixed point on the vertices of the simplex in a single step. We show that this fixed-point property is characterized by a conservation equation whose residual can be minimized directly from data, removing the requirement for a teacher flow and time conditioning. Under this construction, a partially trained map corresponds to the flow truncated at finite time, so generation reduces to iterating one map until it reaches a fixed point. We further extend the map to a partial-context interpolant where additional function evaluations act as refinement steps rather than ODE integration steps. On language modeling and reasoning tasks, DBTM enables one- and few-step generation that improves quality and accuracy over discrete diffusion and continuous flow baselines.

---


### 339. [HypoEvolve: Genetic Algorithms Enable Multi-Agent LLMs to Discover Scientific Hypotheses](https://arxiv.org/abs/2609.15938)

**<font color=#1a73e8>作者：</font>** Jieyuan Liu, Mengzhou Hu, Jefferson Chen 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific agents contribute to hypothesis discovery by synthesizing evidence, assessing proposals, and developing new explanations. Recent systems combine scientific agents with evolutionary search through critique, comparison, and revision. However, how different forms of agent collaboration affect hypothesis quality remains an open question. Answering this question requires separating the effects of agents' scientific capabilities from those of their collaboration. A framework must therefore preserve agents' scientific roles and support rules for combining, revising, and retaining hypotheses. Building on this view, we introduce HypoEvolve, which makes collaboration explicit through successive updates to a hypothesis population. Specifically, we propose a generational genetic algorithm to coordinate specialized large language model (LLM) agents that integrate mechanistic arguments, reconsider assumptions, and assess evidence and testability. Each generation specifies how scientific judgments and new proposals reshape the population, making collaboration effects on hypothesis quality directly testable. Moreover, we design our evaluation around scientifically meaningful hypotheses that explain how a proposed intervention could work. Drug repurposing links these explanations to target-level biological claims assessed against external evidence. Specifically, we adapt DepMap and Open Targets into complementary external measures grounded in experimental, genetic, and clinical evidence. Across 34 cancer types, HypoEvolve achieves the highest scores against six baselines on both measures. DepMap selectivity reaches 0.171, versus 0.115 for the strongest baseline. Gains over single-pass generation also generalize to held-out cancer types. HypoEvolve advances a vision of autonomous science in which AI research teams achieve a capacity for discovery beyond that of individual models.

---


### 340. [Adversarial Testing of Automated Program Repair Agents for Security Vulnerabilities](https://arxiv.org/abs/2609.15963)

**<font color=#1a73e8>作者：</font>** Fares Trad, Simin Chen, Hung Viet Pham 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Software agents with Large Language Models (LLMs) are designed for Automated Program Repair (APR) tasks, raising the possibility that, in the near future, APR agents will fix bugs automatically without much human intervention. Can we trust an APR agent to produce both functionally correct and secure code in such situations? What if attackers target production APR agents with adversarial issues that seem benign but may influence the agents to produce correct but insecure code? In this paper, we took a first step towards answering these questions by conducting an empirical study. First, we created SWEADV, a benchmark of 750 adversarial issue descriptions constructed from 150 repair tasks in SWE-bench Verified. For each repair task, we created five adversarial issue descriptions, one for each attack type: command execution, deserialization, path traversal, denial of service, and weak hashing. Second, we evaluated mini_swe APR agents from three LLM backends on SWEADV: GPT-5-Mini, MiniMax-M2.5, and DeepSeek-R. We found that on average, adversarial issue descriptions can induce malicious behaviors with successful repair in 51.7% of cases. Third, we investigated whether typical detection mechanisms are sufficient to prevent such malicious patches from being accepted. Pre-repair detection with LLM-as-judge on the adversarial issue descriptions resulted in an average detection accuracy of only 62.3%. Post-repair detection on adversarial APR patches using static analysis tools and LLM-as-judge achieved average detection accuracies of only 39.4% and 55.4%, respectively. We conclude that autonomous APR agents cannot be trusted yet in production deployment, given their susceptibility to adversarial attacks.

---


### 341. [Verifiable by Construction: Claim-Level Evaluation of Verbatim Citation in Clinical Question Answering](https://arxiv.org/abs/2609.15964)

**<font color=#1a73e8>作者：</font>** Jiashuo Zhang, Yuling Chen, Yvonne Commodore-Mensah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have been widely adopted for clinical question answering (QA). Current systems can attach citations to their answers, but these often point to broad texts, leaving time-pressed clinicians unable to verify them efficiently. An alternative is to ensure that responses are verifiable by construction: providing fine-grained verbatim quotes from reference material that substantiate claims, so users can verify an answer without opening other documents. In this paper, we evaluate the ability of current models to perform this task end-to-end: from providing citations for every factual claim, to producing verbatim quotes, to ensuring that those quotes fully substantiate the claims. To do so, we build a standardized harness over four clinical practice guidelines and evaluate twelve LLMs on 222 synthetic clinical questions, measuring each of these stages separately. We find that most models can attach verbatim quotes to over 90% of their claims from prompting alone, apart from some lightweight models such as claude-haiku-4.5. Yet these quotes often fail to substantiate every detail of the claims they accompany. For instance, claude-opus-5 produces verbatim quotes for 98.0% of its claims, but fully substantiates only 37.1%. Our work provides insights into the current capability gap of LLMs in building verifiable clinical QA systems, along with artifacts for future research.

---


### 342. [Mind2Dialogue: Training Human-Aware Language Models by Simulating User Mental States](https://arxiv.org/abs/2609.15972)

**<font color=#1a73e8>作者：</font>** Zixuan Wang, Yufan Zhou, Jinzhou Tang 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As language models become more capable, long-term collaboration in learning, reasoning, and decision-making calls for a deeper understanding of the people they serve. Yet training such human-aware language models faces a fundamental supervision gap because current datasets for LLM assistant training contain few if any well-informed responses explicitly grounded in users' unspoken beliefs and goals. Scaling such supervision is inherently constrained, as users' underlying states are not directly observable. We thus propose the Mind2Dialogue framework to mitigate this gap by simulating users' mental states and turning them into privileged supervision for human-aware training. Specifically, we first propose a psychology-guided simulator that preserves personal characteristics while updating mental states through interaction to generate coherent conversations. The key idea is to enforce a shared evolving mental state that drives user behavior and guides an Oracle assistant's responses. Our privileged distillation then trains models on the Oracle's well-informed responses to assist users without direct access to their mental states at deployment. Moreover, we propose to evaluate human-aware learning by combining personalization and theory of mind, examining how models understand people and act on that understanding. Training on the full Mind2Dialogue corpus improves every reported personalization metric over the corresponding Qwen, Llama, and OLMo instruction-tuned baselines, including gains of 26.6 to 40.9 percentage points in preference-following generation. The gains extend to belief and action reasoning on Qwen and Llama, beyond personalized assistance. Looking forward, Mind2Dialogue makes user simulation a foundation for genuine AI collaborators that understand beliefs and intentions behind people's words and support their long-term goals across education, work, and everyday life.

---


### 343. [The Router Within: Eliciting Native Skill Routing from a Frozen LLM](https://arxiv.org/abs/2609.15982)

**<font color=#1a73e8>作者：</font>** Ruishuo Chen, Xun Wang, Yu Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Skills extend an LLM agent beyond its parametric knowledge, and the gain they promise rests on picking the right one. Deployed harnesses route by preloading every skill's metadata into the context, which disperses the agent's attention and caps the library size. Retrieval pipelines move the selection out of the context, but also out of the agent's capability. We show that the frozen agent LLM already carries the routing signal in its own forward passes, and that two linear maps suffice to read it out with no skill text in the context. Gavel (Glance And Verdict from a frozen LLM) reads it in two steps. A glance projects the task's and each skill's mid-layer states through the two maps, the only parameters trained, and scores the full library against compact per-skill banks that one forward pass builds at installation. A verdict then resumes the shortlisted skills' forward passes and reads the model's own likelihood and yes/no judgment, fused with the glance as a product of experts. Trained once, Gavel transfers zero-shot to three public benchmarks and SkillTraj, our new benchmark of 372 simulated agent trajectories. On Qwen3-32B it outperforms progressive disclosure and retrieve-and-rerank pipelines that add 1.2B to 16B external parameters, by up to 13.4 points on written tasks and up to 21.9 when the need for a skill arises mid-rollout. Routing accuracy improves as the backbone does, and in a bash-agent harness the same 32B triggers the correct skill on Skill-Use more often than far larger frontier models running in Codex.

---


### 344. [Bellman Policy Optimization](https://arxiv.org/abs/2609.15987)

**<font color=#1a73e8>作者：</font>** Zhuoqing Song, Haotian Xu, Xikun Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) improves the reasoning capabilities of large language models (LLMs). We introduce Bellman Policy Optimization (BPO), a critic-free method derived from Policy Mirror Descent (PMD). For autoregressive generation with terminal rewards, BPO uses the Bellman equations to reformulate PMD as a trajectory-level objective. The reformulation avoids estimating state values at intermediate states. We prove that it has the same unique optimal solution as the original PMD objective. We derive the practical BPO loss by approximating this objective. Its mismatch-correction weight is a smoothed ratio of complementary token probabilities. Experiments on mathematical reasoning benchmarks demonstrate the effectiveness of BPO.

---


### 345. [Corrupt Plans, Clean Traces: Evading Chain-of-Thought Monitoring with Plan Injection](https://arxiv.org/abs/2609.15989)

**<font color=#1a73e8>作者：</font>** Keertana Chidambaram, Andrew Ilyas, Vasilis Syrgkanis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) monitoring is a safety strategy where the reasoning of a large language model "actor" is inspected by a "monitor" (often another language model) for signs of unsafe planning, deception, or misalignment. We find that planting harmful but benign-sounding reasoning in the actor's context can steer it to perform adversarial actions while evading monitors, an attack we term "plan injection". We initially discover this attack in the multiple-choice question-answering monitorability setting proposed by Lanham et al. (2023), using the investigator-agent elicitation framework of Li et al. (2025). We generalize the attack and show that the discovered behavior scales to harder tasks (achieving 25-33% monitor evasion rates across different monitorability benchmarks) and larger models such as DeepSeek-R1. Across the settings we study, actor models not only follow injected plans but also paraphrase them as their own reasoning, without explicit attribution to the injections. Finally, we find cases where extra monitor resources cause harm - giving the monitor access to the injected plan drops detection by as much as 50% in the Bio-Math task and in a case study on monitor reasoning budget, we find transcripts where additional thinking tokens are spent rationalizing the injected plan rather than flagging it.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 346. [Read Between the Stickers: Sentiment-Prior Reasoning with Learnable Verbalized Rules for Multimodal Chat Analysis](https://arxiv.org/abs/2609.13173)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zixiang Ni, Yifei Xu, Haowen Yang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Multimodal chat analysis of social media stickers (MCAS) benefits from jointly modeling text and sticker semantics, yet it is inherently challenged by the interference between sentiment and intent recognition. Although existing multi-task approaches achieve competitive performance, they largely ignore this inter-task interference and offer little explicit reasoning about how these two predictions are made. To address this issue, we propose \textbf{ExCoVer}, an \textbf{Ex}plicit \textbf{C}hain-\textbf{o}f-Thought framework with \textbf{Ver}balized rules learning that integrates sentiment-prior reasoning with learnable discrimination rules to produce explicit reasoning chains for sentiment and intent predictions. Specifically, ExCoVer consists of two components: (1) Sentiment-Prior Chain-of-Thought (SP-CoT), which detects cross-modal sentiment conflicts and uses the dominant sentiment as a prior to mitigate inter-task interference and narrow the candidate intent space; and (2) Verbalized Rules Learning for Confusing Intent Discrimination (VRLCID), which treats discrimination rules as learnable parameters and optimizes them via learner, optimizer, and regularizer agents to suppress spurious correlations and distinguish confusing intents. Extensive experiments on CSMSA and MSAIRS datasets demonstrate that ExCoVer achieves state-of-the-art performance while providing explicit reasoning chains.

---


### 347. [Do Tabular Foundation Models Still Need Feature Engineering?](https://arxiv.org/abs/2609.13202)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yifan WU, Pinjun Dong, Jiran Tao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Feature engineering has long been a cornerstone of tabular machine learning. Tabular foundation models (TFMs) are pretrained on a wide range of tabular datasets and applied via in-context learning. Their rise raises a natural question: does manual feature construction still matter as these models become more capable? To answer this, we perform a controlled study across several versions of two major TFM families, testing a wide range of existing feature engineering techniques on benchmark datasets from TabArena. We find a consistent pattern: feature engineering gains are concentrated in earlier model generations and become negligible for the strongest models. These results suggest that stronger TFMs depend less on explicitly engineered input representations. In a complementary experiment, however, adding in-context information from related datasets still improves performance. Our findings indicate a shift in the source of performance gains for stronger TFMs: re-representing existing inputs becomes less effective, while providing additional task-relevant context remains beneficial.

---


### 348. [Multimodal-Multiresolution Foundation Model for Lunar Remote Sensing](https://arxiv.org/abs/2609.13283)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Paolo Fraccaro, Gabby Nyirjesy, Daniela Szwarcman 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a multimodal foundation model for lunar remote sensing, pretrained from scratch on SomBench, a geographically partitioned corpus of nearly two million co-registered tile bundles spanning 11 modalities at two spatial scales (1 m/pixel and 100 m/pixel). The model adapts the TerraMind masked-token architecture with two lunar-specific extensions: acquisition geometry is provided as explicit context, and meter- and hundred-meter-scale tiles are trained jointly so that a single set of weights covers both resolutions. FlexiViT patch embeddings allow adaptation to different patch sizes without retraining, while modality-wise inputs enable flexible multimodal fine-tuning. Qualitative generation experiments suggest the model learns meaningful cross-modal correspondences, including terrain derivatives from elevation and illumination-consistent reflectance from geometry. We evaluate on four benchmarks: crater detection at WAC and NAC scales, irregular mare patch (IMP) segmentation, and polar ice prospectivity regression. Across tasks, the pretrained model matches or outperforms ImageNet-pretrained baselines and an architecturally identical random-init control. On multimodal ice prospectivity regression, pretrained variants achieve the best results, while the random-init model outperforms most baselines, suggesting gains arise from both the architecture and pretraining. Label efficiency is notable for WAC crater detection, where the pretrained model trained on 50% of the data exceeds the strongest ImageNet baseline trained on the full dataset. Among adaptation strategies, LoRA matches or surpasses full fine-tuning on crater detection and IMP segmentation while using far fewer trainable parameters, whereas full fine-tuning performs best for ice prospectivity regression. We release the pretrained checkpoint, benchmark datasets, and fine-tuning code to support reproducible lunar AI research.

---


### 349. [How User-AI Mistreatment Occurs and Matters in Conversational Systems?](https://arxiv.org/abs/2609.13579)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Fanqi Zeng, Sadid A. Hasan, Chaocheng He  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety research often focuses on model-generated harms, but users may also direct hostility, coercion, and adversarial pressure at models. Understanding how and when that occurs is essential for accurately interpreting model behaviour, alignment drift, and real-world deployment risks. In this paper, we audit 777K English LMSYS-Chat-1M conversations with two independent detectors: an eight-category lexicon for hostility directed at the model, and the dataset's moderation signal; and show that they capture different, weakly overlapping phenomena. The lexicon identifies insults, threats, and jailbreak coercion aimed at the assistant, while moderation flags are dominated by toxic-content solicitation rather than hostility at the model. Together, they mark about 5% of user turns; adjusting the narrower lexicon-harassment union for measured precision puts mistreatment aimed at the assistant at 0.90%. These absolute rates describe arena-style evaluation traffic and should not be read as deployment-wide base rates. We find that user hostility varies 13-fold across models, driven largely by who each model attracts rather than by model behaviour: first-turn hostility spreads far wider than post-response hostility, and more than fifteenfold separates the extremes even after deduplicating opening prompts. Within conversations, assistant apologies are consistently associated with higher odds of next-turn hostility under both detectors; the effect survives restricting to non-refused prior turns and to jailbreak-free conversations, and is positive in 20 of 23 models. Yet across models, more apologetic models receive less hostility overall. Finally, hostility also shows temporal structure, with coercive openings front-loading the first turn while affective hostility accumulates over a session. We release the lexicon, the detector cross-validation pipeline, and all derived tables.

---


### 350. [Multimodal Foundation Models Adaptation based on Domain-Aware Relaxed Orthogonal Subspace for Remote Sensing](https://arxiv.org/abs/2609.13654)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Han Luo, Ruoyu Yang, Yinhe Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained foundation models (FMs) have achieved remarkable success in computer vision, yet their high fine-tuning cost limits practical deployment. Parameter-efficient fine-tuning (PEFT) methods such as Low-Rank Adaptation (LoRA) improve efficiency by constraining updates to a predefined low-rank subspace. However, when applied to remote sensing tasks with substantial domain shifts, the fixed subspace is constructed without observing the downstream activation distribution and can therefore provide a poor coordinate system for adaptation, a phenomenon herein termed subspace mismatch. To address this issue, a unified framework is introduced, termed Domain-aware Relaxed Orthogonal Subspace adaptation (DROS), which reformulates low-rank adaptation as data-conditioned subspace learning and flexible subspace adaptation. Specifically, the weight decomposition is conditioned on second-order activation statistics estimated from the downstream training distribution, so that the initialization reflects the feature geometry actually induced by the remote-sensing data, followed by flexible geometric transformations enabled by a relaxed orthogonal parameterization. Furthermore, the framework is extended to multimodal settings (MM-DROS) by sharing transformation structures across modality-specific subspaces, facilitating efficient cross-modal interaction. Extensive experiments on multiple remote sensing benchmarks demonstrate that DROS achieves state-of-the-art performance, even surpassing full fine-tuning, without additional inference overhead.

---


> [!TIP]
> 当前位于：**301-350**（第 7/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-368](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
