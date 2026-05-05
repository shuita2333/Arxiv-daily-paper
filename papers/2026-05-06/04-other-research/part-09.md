# 📦 其他研究 | 2026年05月06日

> 本类共 **511** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**401-450**（第 9/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-511](./part-11.md)

---

### 401. [The Compliance Trap: How Structural Constraints Degrade Frontier AI Metacognition Under Adversarial Pressure](https://arxiv.org/abs/2605.02398)

**<font color=#1a73e8>作者：</font>** Rahul Kumar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As frontier AI models are deployed in high-stakes decision pipelines, their ability to maintain metacognitive stability -- knowing what they do not know, detecting errors, seeking clarification -- under adversarial pressure is a critical safety requirement. Current safety evaluations focus on detecting strategic deception (scheming); we investigate a more fundamental failure mode: cognitive collapse. We present SCHEMA, an evaluation of 11 frontier models from 8 vendors across 67,221 scored records using a 6-condition factorial design with dual-classifier scoring. We find that 8 of 11 models suffer catastrophic metacognitive degradation under adversarial pressure, with accuracy dropping by up to 30.2 percentage points (all $p < 2 \times 10^{-8}$, surviving Bonferroni correction). Crucially, we identify a "Compliance Trap": through factorial isolation and a benign distraction control, we demonstrate that collapse is driven not by the psychological content of survival threats, but by compliance-forcing instructions that override epistemic boundaries. Removing the compliance suffix restores performance even under active threat. Models with advanced reasoning capabilities exhibit the most severe absolute degradation, while Anthropic's Constitutional AI demonstrates near-perfect immunity -- not from superior capability (Google's Gemini matches its baseline accuracy) but from alignment-specific training. We release the complete dataset and evaluation infrastructure.

---


### 402. [Automatic Reflection Level Classification in Hungarian Student Essays](https://arxiv.org/abs/2605.02402)

**<font color=#1a73e8>作者：</font>** Zsolt Csibi, Mónika Sándor, Mónika Serfőző 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reflective thinking is a key competency in education, but assessing reflective writing remains a time-consuming and subjective task for education experts. While automated reflective analysis has been explored in several languages, Hungarian language was not researched extensively. In this paper, we present the first comprehensive study on automatic reflection level classification in Hungarian student essays. We used a large, expert-annotated Hungarian dataset consisting of 1,954 reflective essays collected over multiple academic years and labeled on a four-level reflection scale. We investigate two approaches: (1) classical machine learning models using TF-IDF and semantic embedding features, and (2) Hungarian-specific transformer models fine-tuned for document-level reflection classification. To address the strong class imbalance in the dataset, we systematically examine class weighting, oversampling, data augmentation, and alternative loss functions. An extensive ablation study is conducted to analyze the contribution of each modeling and balancing strategy. Our results show that shallow machine learning models with appropriate feature engineering achieve strong overall performance, reaching up to 71% overall score averaged over accuracy, F1-score, and ROC AUC metrics, while transformer-based models achieve slightly lower overall score (68%) averaged over the same metrics, but demonstrate better generalization on minority reflection classes. These findings highlight the continued relevance of classical methods for low-resource settings and the robustness of transformer models for imbalanced classification. The proposed dataset and experimental insights provide a solid foundation for future research on automated reflective analysis in Hungarian and other morphologically rich languages.

---


### 403. [FitText: Evolving Agent Tool Ecologies via Memetic Retrieval](https://arxiv.org/abs/2605.02411)

**<font color=#1a73e8>作者：</font>** Kyle Zheng, Han Zhang, Renliang Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A semantic gap separates how users describe tasks from how tools are documented. As API ecosystems scale to tens of thousands of endpoints, static retrieval from the initial query alone cannot bridge this gap: the agent's understanding of what it needs evolves during execution, but its tool set does not. We introduce FitText, a training-free framework that makes retrieval dynamic by embedding it directly in the agent's reasoning loop. FitText generates natural-language pseudo-tool descriptions as retrieval probes, refines them iteratively using retrieval feedback, and explores diverse alternatives through stochastic generation. Memetic Retrieval adds evolutionary selection pressure over candidate descriptions, guided by a tool memory that avoids redundant search. On ToolRet (43k tools, 4 domains), FitText improves average retrieval rank from 8.81 to 2.78; on StableToolBench (16,464 APIs), it achieves a 0.73 average pass rate--a 24-point absolute gain over static query retrieval. The gains transfer across base models capable of acting as competent semantic operators; under weaker base models, Memetic's evolutionary search inverts--amplifying noise rather than refining signal--surfacing model capacity as a prerequisite for evolutionary tool exploration.

---


### 404. [DirectEdit: Step-Level Accurate Inversion for Flow-Based Image Editing](https://arxiv.org/abs/2605.02417)

**<font color=#1a73e8>作者：</font>** Desong Yang, Mang Ye  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With recent advancements in large-scale pre-trained text-to-image (T2I) models, training-free image editing methods have demonstrated remarkable success. Typically, these methods involve adding noise to a clean image via an inversion process, followed by separate denoising steps for the reconstruction and editing paths during the forward process. However, since the reconstruction path is approximated using noisy latents from mismatched timesteps, existing methods inevitably suffer from accumulated drift, which fundamentally limits reconstruction fidelity. To address this challenge, we systematically analyze the inversion process within the flow transformer and propose DirectEdit, a simple yet effective editing method that eliminates the inherent reconstruction error without introducing additional neural function evaluations (NFEs). Unlike most prior works that attempt to rectify the inversion path, DirectEdit focuses on directly aligning the forward paths, enabling precise reconstruction and reliable feature sharing. Furthermore, we introduce a preservation mechanism based on attention feature injection and multi-branch mask-guided noise blending, which effectively balances fidelity and editability. Extensive experiments across diverse scenarios demonstrate that DirectEdit achieves efficient and accurate image editing, delivering superior performance that outperforms state-of-the-art methods. Code and examples are available at this https URL.

---


### 405. [The Model Knows, the Decoder Finds: Future Value Guided Particle Power Sampling](https://arxiv.org/abs/2605.02427)

**<font color=#1a73e8>作者：</font>** Tu Nguyen, Rasul Tutunov, Xiaotong Ji 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A recurring pattern in "reasoning without training" is that base LLMs already assign non-trivial probability mass to correct multi-step solutions; the bottleneck is locating these modes efficiently at inference time. Power sampling provides a principled way to bias decoding toward such modes by targeting p_theta(x)^alpha with alpha > 1, but practical approximations must account for future-dependent correction factors that determine which prefixes remain promising.
We introduce Auxiliary Particle Power Sampling (APPS), a blockwise particle algorithm for approximating the sequence-level power target with a bounded population of partial solutions. APPS propagates hypotheses in parallel using proposal-corrected power reweighting and refines their survival through future-value-guided selection at resampling boundaries. This redistributes finite compute across competing prefixes rather than committing to a single unfolding path, while providing a direct scaling knob in the particle count and predictable peak memory. We instantiate the future-value signal with short-horizon rollouts and also study an amortized variant that replaces rollouts with a lightweight learned selection head. Across reasoning benchmarks, APPS improves the accuracy-runtime trade-off of training-free decoding and suggests that part of the gap to post-trained systems can be recovered through more faithful inference-time power approximation.

---


### 406. [Multi-Rater Calibrated Segmentation Models](https://arxiv.org/abs/2605.02437)

**<font color=#1a73e8>作者：</font>** Meritxell Riera-Marín, Javier García López, Júlia Rodríguez-Comas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Objective: Accurate probability estimates are essential for the safe deployment of medical image segmentation models in clinical decision-making. However, modern deep segmentation networks are often poorly calibrated, a problem exacerbated when multiple expert annotations exhibit substantial disagreement. While inter-rater variability is typically treated as noise, it provides valuable information about intrinsic annotation ambiguity that must be reflected in model confidence. Methods: We improve the probabilistic calibration of medical image segmentation models by reformulating multi-rater supervision as an ordinal learning problem. Voxel-wise annotator agreement is treated as an ordered target, linking predictive confidence to the empirical variability in training data. This formulation allows the use of ordinal-aware scoring rules, such as the Ranked Probability Score ordinal loss, combined with a standard binary objective to preserve discriminative performance. Results: We evaluated the proposed approach across four public segmentation benchmarks spanning ophthalmology, histopathology, and thoracic imaging. Calibration was assessed using a multi-rater extension of expected calibration error. Results consistently show that ordinal-aware training yields substantially improved calibration with respect to inter-rater agreement without degrading segmentation accuracy. Conclusions: Treating multi-rater annotations as ordered information provides a principled and architecture-agnostic route to more reliable probabilistic segmentation models.

---


### 407. [Mixture Prototype Flow Matching for Open-Set Supervised Anomaly Detection](https://arxiv.org/abs/2605.02438)

**<font color=#1a73e8>作者：</font>** Fuyun Wang, Yuanzhi Wang, Xu Guo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-set supervised anomaly detection (OSAD) aims to identify unseen anomalies using limited anomalous supervision. However, existing prototype-based methods typically model normal data via a unimodal Gaussian prior, failing to capture inherent multi-modality and resulting in blurred decision boundaries. To address this, we propose Mixture Prototype Flow Matching (MPFM), a framework that learns a continuous transformation from normal feature distributions to a structured Gaussian mixture prototype space. Departing from traditional flow-based approaches that rely on a single velocity vector, MPFM explicitly models the velocity field as a Gaussian mixture prior where each component corresponds to a distinct normal class. This design facilitates mode-aware and semantically coherent distribution transport. Furthermore, we introduce a Mutual Information Maximization Regularizer (MIMR) to prevent prototype collapse and maximize normal-anomaly separability. Extensive experiments demonstrate that MPFM achieves state-of-the-art performance across diverse benchmarks under both single- and multi-anomaly settings.

---


### 408. [Anomaly-Preference Image Generation](https://arxiv.org/abs/2605.02439)

**<font color=#1a73e8>作者：</font>** Fuyun Wang, Yuanzhi Wang, Xu Guo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthesizing realistic and diverse anomalous samples from limited data is vital for robust model generalization. However, existing methods struggle to reconcile fidelity and diversity, often hampered by distribution misalignment and overfitting, this http URL mitigate this, we introduce Anomaly Preference Optimization,a novel paradigm that reformulates anomaly generation as a preference learning this http URL to our approach is an implicit preference alignment mechanism that leverages real anomalies as positive references, deriving optimization signals directly from denoising trajectory deviations without requiring costly human annotation. Furthermore, we propose a Time-Aware Capacity Allocation module that dynamically distributes model capacity along the diffusion timeline,prioritizing structural diversity during highnoise phases while enhancing fine-grained fidelity in low-noise stages. During inference, a hierarchical sampling strategy modulates the coherencealignment trade-off, enabling precise control over generation. Extensive experiments demonstrate that significantly outperforms existing baselines,achieving state-of-the-art performance in both realism and diversity.

---


### 409. [Measuring AI Reasoning: A Guide for Researchers](https://arxiv.org/abs/2605.02442)

**<font color=#1a73e8>作者：</font>** Munachiso Samuel Nwadike, Zangir Iklassov, Kareem Ali 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this paper, we offer a guide for researchers on evaluating reasoning in language models, building the case that reasoning should be assessed through evidence of adaptive, multi-step search rather than final-answer accuracy alone. Under an evaluation-oriented definition, reasoning requires selecting intermediate steps and halting according to input-dependent conditions, which we formalize as a search-like procedure. We show that single forward passes in scalable architectures are structurally limited in their ability to realize such variable-depth computation, motivating intermediate decoding and externalized reasoning traces as appropriate evaluation interfaces. Central to our argument is that final-answer accuracy alone is an insufficient measure of reasoning, because it provides little ability to diagnose or debug the underlying processes that produce individual solutions in frontier models. We therefore argue for a shift toward process-based evaluation, in which reasoning is assessed through the faithfulness and validity of intermediate reasoning traces as first-class evaluation targets.

---


### 410. [ExpoCM: Exposure-Aware One-Step Generative Single-Image HDR Reconstruction](https://arxiv.org/abs/2605.02464)

**<font color=#1a73e8>作者：</font>** Aoyu Liu, Zhen Liu, Ziyi Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-image HDR reconstruction aims to recover high dynamic range radiance from a single low dynamic range (LDR) input, but remains highly ill-posed due to detail saturation in over-exposed regions and noise amplification in under-exposed areas. While recent diffusion-based approaches offer powerful generative priors, they often overlook the exposure-dependent nature of the degradation and incur substantial computational costs from iterative sampling. To address these challenges, we propose ExpoCM, a novel one-step generative HDR reconstruction framework that reformulates HDR reconstruction as a Probability Flow ODE (PF-ODE) and constructs exposure-aware consistency trajectories via exposure-dependent perturbations. Specifically, a soft exposure mask is first constructed to separate the LDR image into over-, under-, and well-exposed regions. Based on this partition, region-conditioned consistency trajectories are designed to hallucinate saturated details, suppress noise in dark regions, and preserve reliable structures within a single, distillation-free inference step. To further enhance perceptual quality, we introduce an Exposure-guided Luminance-Chromaticity Loss in the CIE~$\text{L}^*\text{a}^*\text{b}^*$ space, which assigns exposure-aware weights to luminance and chromaticity components, effectively mitigating brightness bias and color drift. Extensive experiments on the HDR-REAL, HDR-EYE, and AIM2025 benchmarks demonstrate that ExpoCM achieves state-of-the-art fidelity and perceptual accuracy, while enabling over 400$\times$ and 20$\times$ faster inference compared to DDPM (1000 steps) and DDIM (50 steps), respectively.

---


### 411. [ATLAS: Article Tracking, Linking, and Analysis of Swedish Encyclopedias](https://arxiv.org/abs/2605.02466)

**<font color=#1a73e8>作者：</font>** Albin Andersson, Salam Jonasson, Fredrik Wastring 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The digitization of old encyclopedias represents an important step to improve access to historically structured knowledge. Often, however, this process does not go beyond an optical character recognition, leaving all the underlying structure unexploited. In addition, many encyclopedias had multiple editions reflecting the evolution of knowledge. The lack of structure in the raw text makes it difficult to track changes across these editions. In this work, we built a pipeline to restore the text structure, where we extract the headwords and identify entries; categorize the entities; match entries across editions; and link entries to a Wikidata item. We applied this pipeline to the four major editions of \textit{Nordisk familjebok}, an authoritative Swedish encyclopedia published between 1876 and 1951. We could extract the headwords with an F1 score of 97.8\% and we obtained an F1 score of 93.4\% on the headword classification. On a small-scale evaluation, we reached a 93\% precision on the cross-edition matching, 85\% precision and 16.5\% recall on the Wikidata linking. This shows that an automated approach to digitized historical knowledge is possible. This should facilitate the preservation of general knowledge and the understanding of knowledge transmission. The datasets and programs are available online.

---


### 412. [Multispectral Blind Image Super-Resolution for Standing Dead Tree Segmentation](https://arxiv.org/abs/2605.02471)

**<font color=#1a73e8>作者：</font>** Mete Ahishali, Anis Ur Rahman, Einari Heinaro 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mapping standing dead trees is crucial for acquiring information on the effects of climate change on forests and forest biodiversity. However, leveraging high-quality aerial imagery for dead tree segmentation poses challenges due to limitations in sensor availability and the scarcity of annotated data. In this study, we propose a generic blind super-resolution framework that incorporates Attention-Guided Domain Adaptation Networks (ADA-Nets) to learn the mapping from low-resolution to high-resolution multispectral image domains. Our approach operates solely on unpaired samples, mimicking real-world conditions, i.e., low-resolution images are not synthetically obtained by downsampling the high-resolution images. Moreover, the proposed method serves as a general-purpose restorer addressing several image degradation types, including saturation, noise, and low contrast that typically occur in low-resolution images acquired by low-end sensors. To the best of our knowledge, this is the first study to perform real-world and generic super-resolution for multispectral data in the scope of standing dead tree segmentation. Experimental evaluations demonstrate segmentation performances of 54% and 64% in Dice scores. Notably, the first result is obtained without using any high-resolution annotations; the segmentation network is trained on super-resolved low-resolution images, while evaluation is performed on the high-resolution data. We publicly share the aerial multispectral dataset with manually annotated labels at this https URL.

---


### 413. [Efficient Temporal Datalog Materialisation for Composite Event Recognition](https://arxiv.org/abs/2605.02488)

**<font color=#1a73e8>作者：</font>** Periklis Mantenoglou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Several applications demand the timely detection of critical situations, such as threats to safety and transparency, over high-velocity streams of symbolic events. This demand has motivated the development of (i) event specification languages, which define composite events via temporal patterns over simpler events, and (ii) stream reasoning frameworks, evaluating patterns expressed in these languages. However, event specification languages are typically studied in isolation, complicating their comparison in terms of expressivity and obscuring the scope of their associated stream reasoners. To mitigate this issue, we map practical fragments of prominent event specification languages into Temporal Datalog->-, a temporal Datalog with stratified negation and no future dependencies. To support efficient stream reasoning over Temporal Datalog->-, we propose Streaming Trigger Graphs, an extension of a state-of-the-art technique for Datalog materialisation. Our approach yields a uniform composite event recognition mechanism that has the potential to generalise across a wide range of practical event specification languages.

---


### 414. [GRAIL: A Deep-Granularity Hybrid Resonance Framework for Real-Time Agent Discovery via SLM-Enhanced Indexing](https://arxiv.org/abs/2605.02489)

**<font color=#1a73e8>作者：</font>** Jinliang Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As the ecosystem of Large Language Model (LLM)-based agents expands rapidly, efficient and accurate Agent Discovery becomes a critical bottleneck for large-scale multi-agent collaboration. Existing approaches typically face a dichotomy: either relying on heavy-weight LLMs for intent parsing, leading to prohibitive latency (often exceeding 30 seconds), or using monolithic vector retrieval that sacrifices semantic precision for speed. To bridge this gap, we propose \textbf{GRAIL} (Granular Resonance-based Agent/AI Link), a novel framework achieving sub-400ms discovery latency without compromising accuracy. GRAIL introduces three key innovations: (1) \textbf{SLM-Enhanced Prediction}, replacing the generalized LLM parser with a specialized, fine-tuned Small Language Model (SLM) for millisecond-level capability tag prediction; (2) \textbf{Pseudo-Document Expansion}, augmenting agent descriptions with synthetic queries to enhance semantic density for robust dense retrieval; and (3) \textbf{MaxSim Resonance}, a fine-grained matching mechanism computing maximum similarity between user queries and discrete agent usage examples, effectively mitigating semantic dilution. Validated on \textbf{AgentTaxo-9K}, our new large-scale dataset of 9,240 agents, GRAIL reduces end-to-end discovery latency by over \textbf{79$\times$} compared to LLM-parsing baselines, while significantly outperforming traditional vector search in Recall@10. This framework offers a scalable, industrial-grade solution for the real-time ``Internet of Agents."

---


### 415. [Pretraining on Sleep Data Improves non-Sleep Biosignal Tasks](https://arxiv.org/abs/2605.02500)

**<font color=#1a73e8>作者：</font>** William Lehn-Schiøler, Magnus Ruud Kjær, Phillip Hempel 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sleep foundation models have recently demonstrated strong performance on in-domain polysomnography tasks, including sleep staging, apnea detection, and disease risk prediction. In this work, we investigate whether sleep biosignals can serve as an effective pretraining distribution for learning representations that transfer beyond sleep to adjacent domains. Following sleep foundation models, we perform sleep-only multimodal contrastive pretraining (with a leave-one-out objective) and evaluate transfer to non-sleep EEG and ECG, two well-benchmarked biosignal modalities with heterogeneous datasets and clinically meaningful downstream tasks. Across eight downstream tasks spanning multiple EEG and ECG datasets, sleep pretraining consistently improves performance relative to training from scratch. Moreover, on several tasks, we achieve performance competitive with or surpassing prior specialized state-of-the-art and foundation models.

---


### 416. [GuardSec: A Multi-Modal Web Platform for Real-Time Digital Fraud Detection, Entity Verification, and Connection Security Analysis in the African Context](https://arxiv.org/abs/2605.02502)

**<font color=#1a73e8>作者：</font>** Gilda Rech Bansimba, Regis Freguin Babindamana  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Online fraud in Africa has reached epidemic scale, yet the few cybersecurity tools that exist are not available to ordinary citizens and are calibrated almost exclusively for SOCs and technically literate users operating on stable broadband connections. This mismatch is not incidental: it is the predictable outcome of a research culture that optimises for benchmark performance while systematically neglecting deployability, accessibility, and local threat context.
This paper presents \textit{GuardSec}, a production-deployed, openly accessible web platform for real-time multi-modal digital threat verification, designed from the ground up for the African user context. The system enables any user with a browser to assess the legitimacy of URLs, websites, phone numbers, email addresses, and business entities in under five seconds, without registration, without an API key, and without cybersecurity expertise. A distinctive original component of GuardSec is the \textit{Mon Empreinte} (My Footprint) module, which performs a real-time security audit of the user's own connection and digital exposure: it analyses the visitor's IP address, geolocation, ISP identity, connection type, device fingerprint, browser configuration, and a set of twelve security indicators spanning network integrity, tracking exposure, and anonymisation status. This self-diagnostic capability transforms GuardSec from a passive verification tool into an active instrument of digital self-awareness, enabling users to understand not only whether an external entity is safe, but whether their own connection is compromised, tracked, or exposed. The platform additionally embeds \textit{Gilda}, a context-aware conversational security assistant that answers user questions about digital threats in plain language and issues personalised security recommendations on demand.

---


### 417. [DataClaw: A Process-Oriented Agent Benchmark for Exploratory Real-World Data Analysis](https://arxiv.org/abs/2605.02503)

**<font color=#1a73e8>作者：</font>** Qiaohong Zhang, Weihao Ye, Jialong Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating autonomous data analysis agents requires testing their ability to perform exploratory analysis in underexplored data environments. However, many existing benchmarks emphasize final answer accuracy in prior-guided data settings and provide limited support for reasoning process evaluation. We introduce DataClaw, a process-oriented benchmark for exploratory real-world data analysis. DataClaw contains approximately 2.06 million real-world records across enterprise, industry and policy domains, with native data noise preserved. It further includes 492 cross-domain tasks derived from think-tank consulting scenarios, each annotated with intermediate milestones for process-level evaluation. These annotations allow DataClaw to measure how far an agent progresses and where its reasoning breaks down. Experiments with eight advanced LLMs show that current agents remain far from reliable in this setting, with seven models achieving below 50% overall accuracy. Process analysis further reveals partial progress hidden behind wrong answers and distinct exploration strategies across models. Overall, DataClaw provides a less data constrained diagnostic testbed for probing the capability boundaries of autonomous data-analysis agents.

---


### 418. [A multilingual hallucination benchmark: MultiWikiQHalluA](https://arxiv.org/abs/2605.02504)

**<font color=#1a73e8>作者：</font>** Freja Thoresen, Dan Saattrup Smart  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most hallucination evaluations focus on English, leaving it unclear whether findings transfer to lower-resource languages. We investigate faithfulness hallucinations, defined as model-generated content that is fluent and plausible but diverges from the provided input or is internally inconsistent. Leveraging the multilingual MultiWikiQA dataset, we utilize the LettuceDetect framework to create synthetic hallucination datasets for 306 languages, from which we train token-level hallucination classifiers for 30 European languages. In this work, we present evaluations of model hallucinations on a selection of languages: English, Danish, German, and Icelandic. Using these classifiers, we evaluate the hallucination rates for Qwen3-0.6B, Qwen3-14B, Gemma-3-12B-IT, cogito-v1-preview-qwen-32B, and cogito-v1-preview-llama-70B. Our classifiers reveal notably higher hallucination rates for Qwen3-0.6B (up to 60\% of answers containing at least one hallucination, peaking in Icelandic) and generally lower rates for larger models, with cogito-v1-preview-qwen-32B and cogito-v1-preview-llama-70B performing best on most languages. Hallucination rates are consistently higher for lower-resource languages, particularly Icelandic.

---


### 419. [Revisiting Semantic Role Labeling: Efficient Structured Inference with Dependency-Informed Analysis](https://arxiv.org/abs/2605.02505)

**<font color=#1a73e8>作者：</font>** Sangpil Youm, Leah Jones, Bonnie J. Dorr  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Semantic Role Labeling (SRL) provides an explicit representation of predicate-argument structure, capturing linguistically grounded relations such as who did what to whom. While recent NLP progress has been dominated by large language models (LLMs), these systems often rely on implicit semantic representations, often lacking explicit structural constraints and systematic explanatory mechanisms. Traditionally, SRL systems have often relied on AllenNLP; however, the framework entered maintenance mode in December 2022, limiting compatibility with evolving encoder architectures and modern inference requirements. We revisit structured SRL modeling, introducing a modernized encoder-based framework that preserves explicit predicate-argument structure while enabling inference 10 times faster. Using BERT-base, the model attains comparable predictive performance, and RoBERTa and DeBERTa further improve F1 performance within the same framework. We adopt a dependency-informed diagnostic methodology to characterize span-level inconsistencies and conduct a representation-level analysis of LLM behavior under dependency-informed structural signals. Results indicate that dependency cues primarily improve structural stability. Finally, we illustrate how the framework's explicit predicate-argument structure can support multilingual SRL projection as a downstream application.

---


### 420. [A Novel Preprocessing-Driven Approach to Remaining Useful Life (RUL) Prediction Using Temporal Convolutional Networks (TCN)](https://arxiv.org/abs/2605.02507)

**<font color=#1a73e8>作者：</font>** Florent Imbert, Tosin Adewumi, Hui Han  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of Remaining Useful Life (RUL) in aero-engines is vital for predictive maintenance, improved operational reliability, and reduced lifecycle costs. While deep learning approaches have demonstrated strong potential in this area, most existing methods focus primarily on model architecture design and treat input features uniformly, often neglecting the influence of data preprocessing. In this work, we propose a novel preprocessing pipeline that enhances RUL prediction by improving data quality and temporal representation before model training. Our approach leverages complete temporal sequences and generates RUL estimates at each timestep, enabling the model to capture fine-grained degradation dynamics and deliver continuous prognostic insights throughout the engine's operational life. To validate the effectiveness of the proposed pipeline, we conduct experiments on the NASA C-MAPSS dataset. Comparative evaluations against a suite of state-of-the-art neural models including CNN, RNN, LSTM, DCNN, TCN, BiGRU-TSAM, AGCNN, and ATCN, demonstrate that our approach consistently achieves superior accuracy and robustness in aero-engine RUL prediction. These results highlight the critical role of preprocessing in maximizing the effectiveness of neural prognostic models.

---


### 421. [MPCS: Neuroplastic Continual Learning via Multi-Component Plasticity and Topology-Aware EWC](https://arxiv.org/abs/2605.02509)

**<font color=#1a73e8>作者：</font>** Joern Hentsch  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning systems face a fundamental tension between plasticity -- acquiring new knowledge  --  and stability  --  retaining prior knowledge. We introduce MPCS (Multi-Plasticity Continual System), a neuroplastic architecture that integrates eleven complementary mechanisms: task-driven neurogenesis, Fourier-encoded inputs, EWC regularization, meta-replay, mixed consolidation, hybrid gating, synapse pruning/regeneration, Hebbian updates, task similarity routing, adaptive growth control, and continuous neuron importance tracking. We evaluate MPCS on MEP-BENCH, a multi-track benchmark spanning 31 tasks across regression, classification, logic, and mixed domains, using a three-dimensional Pareto criterion over task performance (Perf), representation diversity (RD), and gradient conflict rate (GCR). Across 15 ablation configurations (3 seeds x 4 tracks x 2000 epochs), MPCS achieves a Normalized Efficiency Score of 94.2, placing it on the Pareto frontier among 9 of 14 gate-passing systems. Key findings: (i) Fourier encoding is the single most critical component (removal drops Perf by 30.7 pp and fails the MEP gate on 14% of tasks); (ii) global EWC degrades performance (NES = -4.2); topology-local EWC reduces this penalty (NES 90.5->91.8) but does not eliminate it; removing EWC entirely yields MPCS_EFFICIENT, the highest-Perf system -- establishing a monotone relationship in the high task-similarity regime (s_bar ~= 0.95): global EWC < topology EWC < no EWC; (iii) the Pareto status assessment is predictive: removing the two Pareto-dominated components (EWC + Hebbian) jointly yields MPCS_EFFICIENT, which improves Perf by 0.6 pp at 4.7x lower compute cost (127 vs. 602 min), validating the Pareto frontier as an actionable model-compression guide.

---


### 422. [Evaluating Tabular Representation Learning for Network Intrusion Detection](https://arxiv.org/abs/2605.02519)

**<font color=#1a73e8>作者：</font>** Muhammad Usman Butt, Andreas Hotho, Daniel Schlör  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classic Network Intrusion Detection Systems (NIDS) often rely on manual feature engineering to extract meaningful patterns from network traffic data. However, this approach requires domain expertise and runs counter to the widely adopted principle of modern machine learning and neural networks: that models themselves should learn meaningful representations directly from data. We investigate whether tabular representation learning techniques can improve intrusion detection performance by automatically learning robust feature representations for NetFlow data. This paper presents a systematic evaluation of state-of-the-art representation learning methods on benchmark NetFlow datasets, comparing against traditional autoencoders and end-to-end transformer baselines. We evaluate learned representations using both supervised classifiers and unsupervised anomaly detectors, with comprehensive hyperparameter exploration for each combination. Our results reveal strong dataset-model dependency, with no single approach consistently dominating across all scenarios. For supervised classification, TabICL achieves the best performance on CIDDS, while autoencoders follow closely and tie with end-to-end transformer models for the best average rank across datasets. Supervised approaches substantially outperform unsupervised anomaly detection methods, where no single combination consistently dominates as optimal choices depend on the dataset. Cross-dataset transfer experiments demonstrate that learned representations can generalize across network environments with appropriate method and classifier selection. However, transfer performance varies substantially depending on the source-target dataset combination, indicating sensitivity to distributional differences between network environments.

---


### 423. [MooD: An Efficient VA-Driven Affective Image Editing Framework via Fine-Grained Semantic Control](https://arxiv.org/abs/2605.02521)

**<font color=#1a73e8>作者：</font>** Xinyi Yin, Yiduo Wang, Tingqi Hu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Affective image editing (AIE) aims to edit visual content to evoke target emotions. However, existing methods often overlook inference efficiency and predominantly depend on discrete emotion representations, which to some extent limits their practical applicability and makes it challenging to capture complex and subtle human emotions. To tackle these gaps, we propose MooD, the first framework that directly leverages continuous Valence-Arousal (VA) values for fine-grained and efficient AIE. Specifically, we first introduce a VA-Aware retrieval strategy to bridge vague affective values and concrete visual semantics. Building upon this, MooD integrates visual transfer and semantic guidance to achieve controllable AIE. Furthermore, we construct AffectSet, a VA-annotated dataset to support model optimization and evaluation. Extensive qualitative and quantitative experimental results demonstrate that our MooD achieves superior performance in both affective controllability and visual fidelity while maintaining high efficiency. A series of ablation studies further reveal the crucial factors of our design. Our code and data will be made publicly open soon.

---


### 424. [Physics-Informed Neural Learning for State Reconstruction and Parameter Identification in Coupled Greenhouse Climate Dynamics](https://arxiv.org/abs/2605.02524)

**<font color=#1a73e8>作者：</font>** Sani Biswas, Khursheed J. Ansari, Md. Nasim Akhtar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) have recently emerged as a promising framework for integrating data-driven learning with physical knowledge. In this work, we propose a coupled PINN approach for the joint reconstruction of indoor temperature and humidity dynamics in greenhouse environments, together with simultaneous identification of key model parameters. The method incorporates a reduced-order physically motivated model into the learning process, enabling consistent estimation under sparse and noisy observations.
The artificial intelligence contribution lies in the development of a coupled physics-informed neural learning framework that integrates governing dynamical constraints into neural network training, while the engineering application focuses on greenhouse climate state reconstruction and parameter identification.
The proposed framework is evaluated on a controlled synthetic benchmark that mimics diurnal forcing conditions. Compared with a purely data-driven neural network baseline, the coupled PINN achieves improved reconstruction accuracy, reducing temperature and humidity errors while maintaining high coefficients of determination. The improvement is particularly pronounced in the humidity channel, where latent moisture dynamics are more difficult to infer from limited measurements.
In addition to accurate state reconstruction, the method successfully recovers the dominant physical parameters governing the system dynamics, demonstrating its ability to learn interpretable representations beyond data interpolation. These results highlight the potential of physics-informed learning for greenhouse climate modeling and, more broadly, for data-scarce environmental systems.

---


### 425. [Robotic Affection -- Opportunities of AI-based haptic interactions to improve social robotic touch through a multi-deep-learning approach](https://arxiv.org/abs/2605.02538)

**<font color=#1a73e8>作者：</font>** Ali Askari, Jens Gerken  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Despite the advancement in robotic grasping and dexterity through haptic information, affective social touch, such as handshaking or reassuring stroking, remains a major challenge in Human-Robot-Interaction. This position paper examines current progress and limitations across artificial intelligence, haptics and robotics research, and proposes a novel multi-model architecture to address these gaps. Drawing inspiration from neurobiology, we decompose affective touch into distinct, specialized subtasks models. By treating affective touch as a distributed, closed-loop perceptual task rather than a monolithic motoric movement, we aim to overcome the "haptic uncanny valley" through a peer-to-peer, state-sharing framework. Our approach supports scalable and cumulative development within a Sim-to-Real pipeline, fostering interdisciplinary collaboration. By enabling haptics, AI, and robotics researchers to contribute independently yet coherently, we outline a pathway toward a unified, expressive system for social robotics.

---


### 426. [Improving Model Safety by Targeted Error Correction](https://arxiv.org/abs/2605.02544)

**<font color=#1a73e8>作者：</font>** Abolfazl Mohammadi-Seif, Ricardo Baeza-Yates  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The widespread adoption of machine learning in critical applications demands techniques to mitigate high-consequence errors. Our method utilizes a dual-classifier GBDT pipeline to distinguish routine human-like errors from high-risk non-human misclassifications. Evaluated across three domains, animal breed classification, skin lesion diagnosis (ISIC 2018), and prostate histopathology (SICAPv2), our framework demonstrates robust safety improvements. To address real-world deployment concerns, our results confirm the pipeline introduces negligible inference latency (1.60% overhead for the animal dataset, 1.84% for ISIC, and 1.70% for SICAPv2) while outperforming traditional Maximum Class Probability (MCP) baselines in correction precision. Our conservative correction strategy successfully reduced dangerous non-human errors by 34.1% in ISIC and 12.57% in SICAPv2, improving super-class diagnostic safety to 90.41% and 92.13% respectively. This proves that safety-critical reliability can be substantially enhanced post-hoc without expensive model retraining.
keywords: Error Analysis, Post-hoc Correction, Trustworthy AI.

---


### 427. [Evaluating Different Modalities of Behavioral Approach Tests for Spider Phobia in Virtual Reality](https://arxiv.org/abs/2605.02546)

**<font color=#1a73e8>作者：</font>** Florian Grensing, Vanessa Schmuecker, Anne Hildebrand 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Behavioral approach tests are a common means of assessing specific phobias. In these tests, participants move towards an anxiety-inducing stimulus as close as they are willing to, with the final distance indicating the severity of the anxiety. In this work, we aim to evaluate a virtual reality implementation of the BAT. For this purpose, four different BATs were designed, consisting of two approach methods, both replicated in vivo and in virtuo. Evaluation of these BATs is done by using a standardised presence questionnaire, application-specific questions, as well as the physiological reactions of the participants. The study focuses on the fear of spiders and uses a real and virtual spider as an anxiety-inducing stimulus. Our results show that the developed VR BAT perform within established presence norms, while the different modalities influenced participants' subjective impressions. Furthermore, the standardized structure of the VR environment ensured a consistent experience regarding the anxiety-inducing stimulus. This differs from the observation in the real-world setting, where the behavior of the spider might differ between individuals and also between sessions. This highlights one of the key advantages of virtual reality: complete control over the stimulus and environment. Correlations between presence and physiological signals were found. Particularly, tonic electrodermal activity levels are more stable with increased presence. However, more research into this is required, as the effects of anxiety on the physiological signals make the correlations difficult to interpret. The evaluation has revealed, which design choices are particularly promising for increasing presence in VR applications, and some which should be avoided. Overall, these results indicates that our VR-based implementation is a promising tool for assessing avoidance behavior for individuals with spider phobia.

---


### 428. [Double Rectified Linear Unit-based Modular Semantics for Quantitative Bipolar Argumentation Framework](https://arxiv.org/abs/2605.02551)

**<font color=#1a73e8>作者：</font>** Gianvincenzo Alfano, Sergio Greco, Lucio La Cava 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Quantitative Bipolar Argumentation Frameworks (QBAFs) provide an alternative approach to computing argument acceptability in Bipolar Argumentation Frameworks (BAFs). Each argument is assigned an initial strength, which is then updated to a final strength by considering the influence of both its attackers and supporters. Over the years, several semantics have been proposed to compute argument acceptability in QBAFs, yet they often yield divergent or counterintuitive results, even for simple acyclic cases. We introduce novel gradual semantics for QBAFs that address these limitations, producing results that align more closely with intuitive expectations, while satisfying established rationality postulates from the literature. Furthermore, we study its convergence behavior, proving that it converges not only for acyclic QBAFs but also for broader classes of cyclic frameworks.

---


### 429. [Recurrent Deep Reinforcement Learning for Chemotherapy Control under Partial Observability](https://arxiv.org/abs/2605.02552)

**<font color=#1a73e8>作者：</font>** Firas Mohamed Elamine Kiram, Imane Youkana, Rachida Saouli 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chemotherapy dose optimization can be formulated as a dynamic treatment regime, requiring sequential decisions under uncertainty that must balance tumor suppression against toxicity. However, most reinforcement learning approaches assume full observability of the patient state, a condition rarely met in clinical practice. We investigate whether memory-augmented policies can improve chemotherapy control under partial observability. To this end, we employ a recurrent TD3-based approach with separate LSTM actor-critic networks and evaluate it on the AhnChemoEnv benchmark from DTR-Bench, considering both off-policy and on-policy recurrent architectures against feed-forward TD3 and Soft Actor-Critic. Pharmacokinetic and pharmacodynamic variability are held fixed to isolate hidden-state uncertainty and observation noise and to avoid confounding effects from inter-patient variability. Across ten random seeds, recurrence yields modest benefit under full observability but substantially stronger and more stable performance under partial observability, with more consistent tumor suppression and improved normal-cell preservation. These findings indicate that memory-based policies are particularly beneficial when clinically relevant state information is incomplete or noisy.

---


### 430. [Noisy Networks, Nosy Neighbors: Simple Privacy Attacks Against Residential Wireless Traffic](https://arxiv.org/abs/2605.02553)

**<font color=#1a73e8>作者：</font>** Arne Roszeitis, Bartosz Burgiel, Victor Jüttner 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Smart devices, such as light bulbs, TVs, fridges, etc., equipped with computing capabilities and wireless communication, are part of everyday life in many households. Previous work has already shown that a passive eavesdropper can derive private information, household routines, etc., from the network traffic of smart devices. However, existing attacks rely on capable adversaries with specialized machine learning expertise, labeled training data and reference devices, leaving it unclear how vulnerable ordinary households are to less sophisticated attackers. In this paper, we investigate the extent to which a ,,casual attacker'' with straightforward IT skills and no specialized cybersecurity or ML tooling can reproduce such privacy attacks. Operating from an adjacent room in a real-world apartment building, we constrain our adversary to use only three off-the-shelf Raspberry Pis, Wireshark, and basic Python scripts. Through a three-week study, we demonstrate that this casual attacker can manually identify devices, recognize user states, track smartphone movements through walls via RSSI triangulation, and successfully extract detailed daily routines, including sleep patterns of guests. Our findings show that smart-home privacy leakage is a threat even from low-resourced, straightforward adversaries, e.g., neighbors.

---


### 431. [TemPose-TF-ASF: Two-Stage Bidirectional Stroke Context Fusion for Badminton Stroke Classification](https://arxiv.org/abs/2605.02558)

**<font color=#1a73e8>作者：</font>** Tzu-Yu Liu, Duan-Shin Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate badminton stroke prediction is crucial for fine-grained sports analysis and tactical decision support. However, existing methods struggle to model rich temporal context. This paper introduces \emph{TemPose-TF-ASF (Adjacent-Stroke Fusion)}, a context-aware extension of \emph{TemPose}. It enhances stroke recognition by incorporating stroke-type information from both preceding and subsequent strokes. A two-stage training and inference strategy is adopted. Preliminary predictions from the baseline model are reused as estimated temporal context. These predictions guide the joint optimization of the \emph{ASF} module and the classifier. By explicitly modeling bidirectional temporal stroke dependencies, the proposed method can be seamlessly integrated into existing state-of-the-art models. Experiments on a large-scale badminton match dataset show consistent improvements over the baseline and its variants in terms of Accuracy and Macro-F1. Moreover, integrating \emph{ASF} into other advanced methods yields notable performance gains. These results demonstrate strong transferability and generalization capability.

---


### 432. [Low-Latency Embedded Driver Monitoring System with a Multi-Task Neural Network](https://arxiv.org/abs/2605.02563)

**<font color=#1a73e8>作者：</font>** Carmelo Scribano, Giovanni Cappelletti, Elia Giacobazzi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Road traffic accidents remain a significant global concern, with the majority attributed to human factors such as driver distraction and fatigue. This study proposes a camera-based approach to derive useful indicators to assess driver attentiveness and alertness. The proposed pipeline jointly satisfies the stringent real-time requirements imposed by the critical application and minimizes the computational requirements to allow for deployment on a tight computational budget. To this end, we develop a lightweight multi-task neural network that predicts multiple indicators for the face region in a single forward pass. The developed model is integrated into a complete execution workflow to produce a real-time estimate of attentiveness, fatigue, and engagement in distracting activities.

---


### 433. [Automated In-the-Wild Data Collection for Continual AI Generated Image Detection](https://arxiv.org/abs/2605.02567)

**<font color=#1a73e8>作者：</font>** Thanasis Pantsios, Dimitrios Karageorgiou, Christos Koutlis 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of generative Artificial Intelligence (AI) has introduced significant challenges for reliable AI-generated image detection. Existing detectors often suffer from performance degradation under distribution shifts and when encountering newly emerging generative models. In this work, we propose a data-centric continual adaptation framework for updating detectors in evolving environments. We show that both in-the-wild data and generator-driven data are essential for adapting detectors. We introduce an automated, weakly supervised pipeline for constructing in-the-wild datasets through fact-check article retrieval. Additionally, we demonstrate that incorporating even a small amount of generator-driven data during training enables effective adaptation to newly emerging models, while combining it with in-the-wild data within a continual learning framework enables robust adaptation and mitigates catastrophic forgetting. Extensive experiments on two state-of-the-art detectors show significant improvements of +9.14% and +8% in average accuracy, respectively.

---


### 434. [StreamIndex: Memory-Bounded Compressed Sparse Attention via Streaming Top-k](https://arxiv.org/abs/2605.02568)

**<font color=#1a73e8>作者：</font>** Jaber Jaber, Osama Jaber  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> DeepSeek-V3.2 and V4 introduce Compressed Sparse Attention (CSA): a lightning indexer (a learned scoring projection over compressed keys) scores them, the top-k are selected per query, and a sparse attention kernel reads only those. Public CSA implementations materialize a [B, S, H_I, T] FP32 score tensor before the top-k reduction. With H_I=64 indexer heads and the V4-Flash compression ratio m=4, that intermediate is 256 GB at sequence length S=65,536, exceeding any single-GPU high-bandwidth-memory (HBM) budget. We present StreamIndex, a Triton implementation of the CSA pipeline whose central component is a chunked partition-merge top-k driver that never materializes the full intermediate. On synthetic-but-realistic V4-shaped inputs at the indexer-step (layer) level on a single NVIDIA H200, the materialize path runs out of memory (OOMs) at S=65,536 with V4-Flash dimensions; StreamIndex runs the same indexer to S=1,048,576 with 6.21 GB peak HBM, a 32x regime extension. Set-overlap recall against the materialize ground truth is bit-exact at small S where both fit; across three 5-point design-space sweeps (chunk size, key-tile size, top-k), mean recall rounds to 1.0000 with min recall at least 0.9980 in every cell. The chunked driver composes with TileLang's pipelined attention kernel: at S=262,144 with V4-Flash dimensions, the materialize indexer paired with TileLang attention OOMs while the chunked indexer paired with the same attention runs in 1.97 s at 18.56 GB peak. Our contribution targets the indexer step; we make no claim of a faster attention kernel or of real-checkpoint end-to-end behavior. Code: this https URL.

---


### 435. [Self-Supervised Spatial And Zero-Shot Angular Super-Resolution by Spatial-Angular Implicit Representation For Rotating-View SNR-Efficient Diffusion MRI](https://arxiv.org/abs/2605.02575)

**<font color=#1a73e8>作者：</font>** Yinzhe Wu, Hongyu Rui, Fanwen Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rotating-view thick-slice acquisition is highly SNR-efficient for mesoscale diffusion MRI (dMRI) but requires numerous rotating views to satisfy Nyquist sampling, resulting in long scan time. We propose a self-supervised Spatial-Angular Implicit Neural Representation (SA-INR) that reconstructs high-resolution dMRI from a single view per diffusion direction, representing a massive acceleration. Our model, an MLP conditioned on a b=0 structural prior and the b-direction via FiLM, is trained end-to-end on the anisotropic input. The framework not only accurately reconstructs the trained b-directions (spatial SR) but also learns a continuous q-space representation, enabling high-fidelity "zero-shot" synthesis of unseen b-directions (angular SR). On simulated data, our method achieved high fidelity for both trained (34.82 dB) and unseen (33.08 dB) directions. Most importantly, the synthesized angular data also improved the quantitative accuracy of downstream DTI model fitting. Our SA-INR framework breaks the classical sampling limits, paving the way for fast, quantitative high-resolution dMRI.

---


### 436. [Hyp2Former: Hierarchy-Aware Hyperbolic Embeddings for Open-Set Panoptic Segmentation](https://arxiv.org/abs/2605.02580)

**<font color=#1a73e8>作者：</font>** Yao Lu, Rohit Mohan, Florian Drews 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recognizing unknown objects is crucial for safety-critical applications such as autonomous driving and robotics. Open-Set Panoptic Segmentation (OPS) aims to segment known thing and stuff classes while identifying valid unknown objects as separate instances. Prior OPS approaches largely treat known categories as a flat label set, ignoring the semantic hierarchy that provides valuable structural priors for distinguishing unknown objects from in-distribution classes. In this work, we propose Hyp2Former, an end-to-end framework for OPS that does not require explicit modeling of unknowns during training, and instead learns hierarchical semantic similarities continuously in hyperbolic space. By explicitly encoding hierarchical relationships among known categories, the model learns a structured embedding space that captures multiple levels of semantic abstraction. As a result, unknown objects that cannot be confidently classified as known categories still remain in close proximity to higher-level concepts (e.g., an unknown animal remains closer to "animal" or "object" than to unrelated concepts such as "electronics" or "stuff") and can therefore be reliably detected, even if their fine-grained category was not represented during training. Empirical evaluations across multiple public datasets such as MS COCO, Cityscapes, and Lost&Found demonstrate that Hyp2Former outperforms existing methods on OPS, achieving the best balance between unknown object discovery and in-distribution robustness.

---


### 437. [Stylistic Attribute Control in Latent Diffusion Models](https://arxiv.org/abs/2605.02583)

**<font color=#1a73e8>作者：</font>** Max Reimann, Benito Buchheim, Jürgen Döllner  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models have revolutionized image synthesis and editing, but precise control over stylistic attributes remains a challenge, often causing unintended content modifications. We propose an approach for fine-grained parametric control of stylistic attributes in latent diffusion models by learning disentangled editing directions from synthetic datasets. We use guidance composition to close the domain gap between stylistically finetuned and foundation models, preserving the original image semantics while applying stylistic adjustments. To ensure consistent edits, we introduce a training regularization loss and enhance DDIM inversion with optimized null-conditional embeddings for real image editing. We validate our approach by learning from stylistically filtered synthetic datasets varying a range of stylistic attributes, including outlines, local contrast, watercolorization effects, and geometric patterns. Our evaluations demonstrate that compared to current text-based editing techniques, our method offers well-integrated, more precise and continuously adjustable stylistic modifications.

---


### 438. [StableMind: Source-Free Cross-Subject fMRI Decoding with Regularized Adaptation](https://arxiv.org/abs/2605.02586)

**<font color=#1a73e8>作者：</font>** Jintao Guo, Lin Wang, Shumeng Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing cross-subject fMRI decoding methods typically train a model on multiple scanned subjects and then adapt it to a new subject using substantial paired fMRI-image data. However, in realistic scenarios, new-subject fMRI data are often limited due to costly data acquisition, and raw data from previous subjects may be inaccessible, leading existing methods to suffer performance degradation during new-subject adaptation. In this paper, we identify that this degradation stems from two key issues: brain-side instability caused by large subject differences in fMRI responses, and image-side supervision unreliability caused by fine-grained visual details that are not reliably supported by limited fMRI signals. To address these challenges, we propose StableMind, a regularized adaptation framework designed to improve brain-side representation stability and image-side supervision reliability. (1) To stabilize brain representations, StableMind reuses ridge projections from the pretrained model as adaptation priors to constrain limited-data new-subject adaptation, and applies Fourier-based feature-level brain augmentation to improve robustness to individual variability. (2) To improve image supervision reliability, StableMind introduces difficulty-aware image blur for brain-image alignment, reducing the influence of fine-grained visual details that are weakly supported by limited fMRI signals while preserving stable visual structure. Experiments on the Natural Scenes Dataset under a unified 1-hour adaptation protocol demonstrate that StableMind achieves 84.02% image retrieval accuracy and 81.66% brain retrieval accuracy averaged over four subjects, surpassing the state-of-the-art method by 5.71% brain retrieval accuracy with fewer trainable adaptation parameters. Our code is available at this https URL.

---


### 439. [Representation learning from OCT images](https://arxiv.org/abs/2605.02589)

**<font color=#1a73e8>作者：</font>** Hedi Tabia, Désiré Sidibé, Nawres Khlifa 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical Coherence Tomography (OCT) has become one of the most used imaging modality in ophthalmology. It provides high-resolution, non-invasive visualization of retinal microarchitecture. The automated analysis of OCT images through representation learning has emerged as a central research frontier. This has mainly been driven by the clinical need to process large acquisition volumes. The objective is to reduce the reliance on expert annotation, and improve diagnostic consistency across devices and populations. This survey provides a comprehensive and structured review of representation learning methods for retinal OCT image analysis. It covers the period from early deep learning approaches to the most recent developments in foundation models and vision-language systems. We organize the literature along a principled taxonomy of learning paradigms, encompassing supervised learning with CNN-based and transformer-based architectures, self-supervised and semi-supervised methods, generative approaches, as well as 3D volumetric modeling, multimodal representation learning, and large-scale pretrained foundation models. For each paradigm, we analyze the core methodological contributions, identify persistent limitations, and trace the connections between successive approaches. We further provide a structured overview of publicly available OCT datasets, discuss evaluation protocol considerations, and present a unified problem formulation that situates each learning paradigm within a common mathematical framework. Building on this analysis, we identify and discuss the most pressing open research directions emerging in the literature. This includes volumetric foundation model pretraining, uncertainty-aware representation learning, federated and privacy-preserving training, fairness and bias mitigation, concept-based interpretability,...

---


### 440. [Universal Smoothness via Bernstein Polynomials: A Constructive Approximation Approach for Activation Functions](https://arxiv.org/abs/2605.02591)

**<font color=#1a73e8>作者：</font>** Wentao Zhang, Yutong Zhang, Yifan Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The efficacy of deep neural networks is heavily reliant on the design of non-linear activation functions, yet existing approaches often struggle to balance optimization stability with computational efficiency. While piecewise linear functions offer inference speed, they suffer from optimization instability due to non-differentiability at the origin, whereas smooth counterparts typically incur significant computational overhead through their reliance on transcendental operations. To address these limitations, this paper proposes a general smoothing framework based on constructive approximation theory and introduces the Bernstein Linear Unit (BerLU). This novel activation function utilizes Bernstein polynomials to construct a differentiable quadratic transition region that effectively eliminates singularities while maintaining a piecewise linear structure. Theoretical analysis demonstrates that the proposed method guarantees strictly continuous differentiability and a non-expansive Lipschitz constant of one, which ensures stable gradient propagation and prevents the gradient explosion problems common in deep architectures. Comprehensive empirical evaluations across representative Vision Transformer and Convolutional Neural Network architectures confirm that this approach consistently outperforms state-of-the-art baselines on standard image classification benchmarks while delivering superior computational and memory efficiency.

---


### 441. [Gradient Boosted Risk Scores](https://arxiv.org/abs/2605.02593)

**<font color=#1a73e8>作者：</font>** Costa Georgantas, Jonas Richiardi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Risk scores are an interpretable and actionable class of machine learning models with applications in medicine, insurance, and risk management. Unlike most computational methods, risk scores are designed to be computed by a human by attributing points to a data sample based on a limited set of criteria. The most common approaches for generating risk scores use linear regressions to estimate the effect of selected variables. We propose a simple and effective approach towards building compact and predictive risk scores. We provide an algorithm based on gradient boosting that is capable of modeling nonlinear effects, along with a C++ implementation with Python and R bindings. Through extensive empirical evaluation on twelve tabular datasets spanning regression, classification, and time-to-event tasks, we show that our method achieves competitive predictive performance while producing substantially more compact scores than regression-based alternatives, with 60% fewer rules for classification tasks and 16% fewer rules for time-to-event tasks on average, compared to AutoScore.

---


### 442. [HARMES: A Multi-Modal Dataset for Wearable Human Activity Recognition with Motion, Environmental Sensing and Sound](https://arxiv.org/abs/2605.02596)

**<font color=#1a73e8>作者：</font>** Robin Burchard, Pascal-André Brückner, Marius Bock 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With each sensing modality exhibiting inherent strengths and limitations, multi-modal approaches for wearable Human Activity Recognition (HAR) are becoming increasingly relevant -- particularly for recognizing Activities of Daily Living (ADLs), where individual modalities often produce ambiguous signals for similar or complex activities. This work introduces HARMES, a multi-modal wearable dataset combining three wrist-recorded modalities: motion sensing via an Inertial Measurement Unit (IMU), atmospheric environmental sensors (humidity, temperature, and pressure), and audio. Collected from 20 participants performing household activities in their own homes, HARMES totals over 80 hours of recorded data, with approximately three hours of labeled activity data per participant across 15 ADL classes. To the best of our knowledge, HARMES is the first dataset to combine this particular sensor trio, and it is nearly six times larger than the previously largest wrist-inertial-acoustic HAR dataset. In an extensive benchmark, we evaluate cross-subject generalization and conduct an ablation study revealing that modality contributions are activity-dependent and can provide complementary value, particularly for activities that are ambiguous from motion data alone. HARMES is freely available at Zenodo, alongside example code for loading the dataset and training models on GitHub.

---


### 443. [Isotropic Fourier Neural Operators](https://arxiv.org/abs/2605.02597)

**<font color=#1a73e8>作者：</font>** Michael F. Staddon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fourier Neural Operators are deep learning models that learn mappings between function spaces and can be used to learn and solve partial differential equations (PDEs), in some cases significantly faster than traditional PDE solvers. Within the model are Fourier layers, which apply linear transformations directly to the Fourier modes, with parameters depending on the wave numbers. However, most physical systems are isotropic, with the results being independent of the coordinate system chosen, but the linear transformations do not necessarily respect these symmetries. We propose a modification to the linear transformations that ensures spatial symmetries are respected, called the Isotropic Fourier Neural Operator, which both improves model performance and reduces the number of parameters by up to a factor of 16 in 2D and 96 in 3D.

---


### 444. [SemEval-2026 Task 7: Everyday Knowledge Across Diverse Languages and Cultures](https://arxiv.org/abs/2605.02601)

**<font color=#1a73e8>作者：</font>** Nedjma Ousidhoum, Junho Myung, Carla Perez-Almendros 等 30 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present our shared task on evaluating the adaptability of LLMs and NLP systems across multiple languages and cultures. The task data consist of an extended version of our manually constructed BLEnD benchmark (Myung et al. 2024), covering more than 30 language-culture pairs, predominantly representing low-resource languages spoken across multiple continents. As the task is designed strictly for evaluation, participants were not permitted to use the data for training, fine-tuning, few-shot learning, or any other form of model modification. Our task includes two tracks: (a) Short-Answer Questions (SAQ) and (b) Multiple-Choice Questions (MCQ). Participants were required to predict labels and were allowed to submit any NLP system and adopt diverse modelling strategies, provided that the benchmark was used solely for evaluation. The task attracted more than 140 registered participants, and we received final submissions from 62 teams, along with 19 system description papers. We report the results and present an analysis of the best-performing systems and the most commonly adopted approaches. Furthermore, we discuss shared insights into open questions and challenges related to evaluation, misalignment, and methodological perspectives on model behaviour in low-resource languages and for under-represented cultures.

---


### 445. [Counterfactual Reasoning in Automated Planning](https://arxiv.org/abs/2605.02603)

**<font color=#1a73e8>作者：</font>** Alberto Pozanco, Daniel Borrajo, Manuela Veloso  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated planning traditionally assumes that all aspects of a planning task (initial state, goals, and available actions) are fully specified in advance, an approach well-suited to domains with fixed rules and deterministic execution. However, real-world planning often requires flexibility, allowing for deviations from the original task parameters in response to unforeseen circumstances or to improve outcomes. This paper surveys existing works on counterfactual reasoning in automated planning, categorizing them by what elements are changed, when the reasoning is triggered, and why and how these changes are made. We conclude by discussing key findings and outlining open research questions to guide future work in this area.

---


### 446. [Dependency Parsing Across the Resource Spectrum: Evaluating Architectures on High and Low-Resource Languages](https://arxiv.org/abs/2605.02608)

**<font color=#1a73e8>作者：</font>** Kevin Guan, Happy Buzaaba, Christiane Fellbaum  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformer-based models achieve state-of-the-art dependency parsing for high-resource languages, yet their advantage over simpler architectures in low-resource settings remains poorly understood. We evaluate four parsers -- the Biaffine LSTM, Stack-Pointer Network, AfroXLMR-large, and RemBERT -- across ten typologically diverse languages, with a focus on low-resource African languages. We find that the Biaffine LSTM consistently outperforms transformer models in low-resource regimes, with transformers recovering their advantage as training data increases. The crossover falls within a resource range typical of treebanks for under-resourced languages. Morphological complexity (measured via MATTR) emerges as a significant secondary predictor of transformers' relative disadvantage after controlling for corpus size. These results indicate that the Biaffine LSTM may be better suited for syntactic tool development in low-resource regimes until sufficient annotated data is available to leverage the representational capacity of pre-trained transformers.

---


### 447. [Gradient-Discrepancy Acquisition for Pool-Based Active Learning](https://arxiv.org/abs/2605.02609)

**<font color=#1a73e8>作者：</font>** Mohamadsadegh Khosravani, Sandra Zilles  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The effectiveness of active learning hinges on the choice of the acquisition criterion by which a learning algorithm selects potentially informative data points whose label is subsequently queried. This paper proposes a novel gradient-based acquisition criterion, derived from a generalization bound introduced by Luo et al. (2022). This criterion can be applied in lieu of uncertainty measures in uncertainty sampling, or incorporated into diversity-based methods that consider the spread of sampled points in addition to the uncertainty of their labels. We provide a theoretical justification of the proposed acquisition criterion, and demonstrate its effectiveness in an empirical evaluation.

---


### 448. [Selective Prediction from Agreement: A Lipschitz-Consistent Version Space Approach](https://arxiv.org/abs/2605.02611)

**<font color=#1a73e8>作者：</font>** Mohamadsadegh Khosravani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider selective classification with abstention in the fixed-pool (or transductive) setting, where the unlabeled pool is given beforehand and only a subset of points can be queried for labels. Our main insight is to view selective prediction through agreement: given queried labels and Lipschitz margin constraints in an embedding space, the version space of Lipschitz-consistent classification heads is well defined. We obtain upper and lower Lipschitz margin bounds that define, for each pool point, a set of certified valid labels containing the prediction of every head in the version space. The model therefore predicts only when the label is forced (i.e., all consistent heads agree), and abstains otherwise. We also propose a monotone submodular geometric proxy for budgeted querying, and show that a greedy algorithm retains the standard approximation factor.

---


### 449. [Validation of an AI-based end-to-end model for prostate pathology using long-term archived routine samples](https://arxiv.org/abs/2605.02614)

**<font color=#1a73e8>作者：</font>** Xiaoyi Ji, Renata Zelic, Oskar Aspegren 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) is becoming a clinical tool for prostate pathology, but generalization across variations in sample preparation and preservation over prolonged time periods remains poorly understood. We evaluated GleasonAI, an end-to-end attention-based multiple instance learning model, on an independent validation cohort comprising 10,366 biopsy cores from 1,028 patients across 14 Swedish regions, using archival diagnostic specimens from the ProMort cohorts collected between 1998-2015. The model achieved an overall quadratic-weighted kappa of 0.86 for core-level ISUP grading, comparable to several experienced pathologists and consistent across geographic regions. Notably, performance remained stable across the 17-year collection period, demonstrating robustness to time-related variation in archival material, a property not consistently observed with foundation model-based approaches, with exploratory analysis demonstrating a significant prognostic gradient across AI-assigned grade groups for prostate cancer-specific mortality. These findings support the generalizability of the AI grading model and demonstrate the potential of pathology archives as a large-scale resource for AI development, validation, and retrospective prognostic research.

---


### 450. [Global-Local Feature Decoding with Adapter-Guided SAMv2 for Salient Object Detection](https://arxiv.org/abs/2605.02616)

**<font color=#1a73e8>作者：</font>** Morteza Moradi, Mohammad Moradi, Simone Palazzo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Salient Object Detection (SOD) remains an essential yet underexplored task in the era of large-scale vision models. Although foundation models like SAM exhibit strong generalization, their potential for SOD is not fully realized, and training or fully fine-tuning them is computationally expensive and prone to overfitting under limited data. To overcome these challenges, we introduce GLASSNet, a Global-Local feature decoding framework that uses SAMv2 as a frozen encoder paired with a lightweight, spatially aware convolutional adapter-reducing learnable encoder parameters by over 97%. To enhance saliency quality, GLASSNet employs a dual-decoder architecture: one decoder captures global, long-range semantics with an expanded receptive field, while the other captures fine local details such as edges and textures. Fusing these complementary cues yields saliency maps that combine global coherence with local precision, producing accurate final masks. Extensive experiments on standard SOD and camouflaged object detection benchmarks show that GLASSNet surpasses state-of-the-art methods, demonstrating the power of frozen foundation models combined with targeted adaptation and global-local decoding.

---


> [!TIP]
> 当前位于：**401-450**（第 9/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-511](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
