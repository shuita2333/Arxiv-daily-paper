# 🧠 大模型相关研究 | 2026年09月16日

> 本类共 **368** 篇论文：已确认 **345** 篇，待复核 **23** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-368](./part-08.md)

---

### 1. [When Can You Trust Your Synthetic Users? Diagnostics and Corrections for LLM Consumer Panels](https://arxiv.org/abs/2609.13148)

**<font color=#1a73e8>作者：</font>** Robson Tigre, Hugo Gobato Souto  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed as synthetic consumer panels, promising $97\%$ cost reductions over traditional surveys. Yet aggregate validation metrics conceal systematic failures: variance compression, coefficient sign-flips, subgroup error balloons of 10--30 percentage points, and global corrections that worsen demographic bias. We provide a formal framework for deciding when to trust, correct, or abandon LLM-generated consumer data. The framework decomposes synthetic-panel bias into covariate and concept shift, develops testable diagnostics with interpretable decision thresholds, and supplies a doubly robust AIPW estimator requiring only a small calibration sample ($n = 50$-$300$). We validate on three testbeds. In controlled simulations the decision rule achieves $100\%$ accuracy (180/180 replications). On the American National Election Study with pre-existing LLM failures, it correctly flags heterogeneous concept shift and reduces naive bias by $92.9-99.6\%$. On the Twin-2K-500 consumer pricing dataset (172,884 paired human and GPT-4.1-mini responses), it correctly routes full-sample estimation to Trust and subgroup targeting to Correct, with $83-94\%$ bias reduction.

---


### 2. [BudgetBench: A Budget-Tiered Protocol and Pilot Harness for Memory Strategy Evaluation in Local Large Language Model Agents](https://arxiv.org/abs/2609.13149)

**<font color=#1a73e8>作者：</font>** Aditya Karnam Gururaj Rao, Arjun Jaggi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For local large language model agents, active context is a scarce resource: memory capacity, prefill latency, cache growth, and service objectives all constrain how many input tokens each call can afford. We present BudgetBench, an active-budget protocol and reference harness that treats the per-call input-token budget as the independent variable when comparing memory strategies. Holding the model, task, sampler, and decoding fixed, it sweeps budgets over 2K, 4K, 8K, 16K, and 32K tokens and records quality, budget utilization, latency, and, as a first-class outcome, budget-violation rates. The core contribution is this reusable measurement surface: a swappable MemoryStrategy contract, explicit budget enforcement, deterministic or versioned graders, prompt-audit metadata, and reproducibility artifacts, released at this https URL.
We substantiate the protocol with pilot studies rather than final rankings. Across a local qwen2.5:1.5b pilot (89 items each on SWE-bench Verified and LongBench v2), a hosted 50-item Qwen3 30B-A3B LongBench replication with exact tokenization, and a 500-item LongMemEval oracle study scored by the official GPT-4o evaluator, the harness exposes budget-compliance failures, non-monotonic quality curves, and operating points that single-budget evaluation hides. The budgeted-versus-full-context direction remains unresolved: the local slice is near-null and the hosted replication favors full context in point estimate. We report results transparently, including that the early pilot's tokenizer approximation undercounts some served-model prompts, so its violation rows are tokenizer-approximation diagnostics, not claim-bearing results; all timings are operational diagnostics. The reusable contribution is the protocol, harness, and failure-reporting discipline needed to scale fixed-budget memory-strategy evaluation.

---


### 3. [PhysMent: An Interactive Approach For LLM Reasoning In Physics Problems](https://arxiv.org/abs/2609.13152)

**<font color=#1a73e8>作者：</font>** Joseph Chan, Utkarsh Jha, Xiyin Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) perform strongly on static science benchmarks, yet their ability to reason about the physical world through active experimentation remains poorly understood. We introduce PhysMent, a benchmark that evaluates LLM physical reasoning via iterative, toolmediated interaction with a MuJoCo physics simulator. Unlike static benchmarks that supply all quantities upfront, PhysMent requires models to discover information by applying forces, querying object states, advancing time, and modifying scene geometry before answering. The benchmark comprises 105 scenes of classical mechanics, organized across four difficulty regimes (Easy/Hard and Single/Multi), three scene modalities (standard, object creation, hidden objects), and a scene-manipulation category, evaluated with a six-dimensional scoring framework. Results show that current models perform reasonably well on qualitative single-concept tasks (up to 80% accuracy) but degrade substantially on quantitative tasks that demand precise, multi-step experimental procedures: most models fall below 30% on the hardest single-concept category, where the bottleneck is procedural (adaptive multi-step tool use) rather than conceptual load. Across the seven models, accuracy ranges from 25% to 67%, with failures due to premature answer submission, inefficient exploration, and inconsistent grounding in simulator feedback rather than conceptual gaps.

---


### 4. [Lexical Prompt Compression for Large Language Models: A Training-Free, Deterministic Pipeline with Empirical Pareto Analysis Across Eleven Task Categories](https://arxiv.org/abs/2609.13154)

**<font color=#1a73e8>作者：</font>** Shamin Chokshi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have made prompts increasingly large and complex. Techniques such as chain-of-thought reasoning (Wei et al., 2022) and in-context learning (Brown et al., 2020) frequently push real-world prompts past several thousand tokens, increasing inference cost and latency. Learned compression methods such as LLMLingua (Jiang et al., 2023) and Selective Context (Li et al., 2023) achieve high compression ratios but require auxiliary language models and are non-deterministic. We ask a complementary question: how far can a training-free, fully deterministic, CPU-only pipeline based on classical lexical NLP be pushed before output quality degrades significantly? Eleven toggleable lexical transformations - stopword removal, filler-phrase deletion, contraction and abbreviation substitution, part-of-speech-based pruning, lemmatization, WordNet-driven synonym shortening, and named-entity preservation - are assembled into a configurable pipeline. Fifteen configurations are evaluated on 1,242 English-only prompts from six sources (Dolly-15k, LMSYS-Chat-1M, WildChat-1M, MMLU, GSM8K, HellaSwag), spanning eleven automatically derived task categories, yielding 18,630 paired GPT-4o-mini completions. Output preservation is measured using BLEU, ROUGE-1/2/L, BERTScore-F1, and SentenceBERT cosine similarity. The most aggressive configuration achieves a mean token reduction of 40.3% (sigma = 9.2) at a BERTScore-F1 of 0.876 against the original-prompt output; a stopword-only configuration achieves 29.6% reduction at 0.913. The compression-versus-fidelity Pareto frontier is characterized per task category, with commonsense reasoning a systematic failure mode under aggressive compression. All code, prompts, and per-cell results are released for reproducibility.

---


### 5. [PAUSE: A Privacy-Preserving Self-Reflection Tool for AI-Associated Cognitive Offloading](https://arxiv.org/abs/2609.13155)

**<font color=#1a73e8>作者：</font>** Mahbub Ul Alam  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Cognitive offloading is the use of external aids, such as notes, calculators, or search engines, to reduce mental effort. Large language models (LLMs) extend this to thinking itself, and by AI-associated cognitive offloading, I mean the pattern where a person routinely substitutes LLM output for their own reasoning, idea generation, learning, or communication. Recent empirical work reports associations between some patterns of LLM use and changes in critical thinking effort, neural engagement during assisted tasks, creative diversity, learning behaviour, and social dependence. Validated instruments for AI reliance, dependence, and literacy have begun to appear. I describe PAUSE (Patterns of AI Use: Self-Examination), a privacy-by-design web tool (link: this https URL) that occupies a different niche from these. It is a lightweight, non-diagnostic reflection aid for private individual use. PAUSE is organised around how a person's own LLM use may relate to cognitive offloading across four everyday domains ('reasoning & critical thinking', 'creativity & originality', 'research & learning', and 'social & communicative capacity'). It delivers a short, free, no-login self-check, scores it entirely in the browser, and returns descriptive, domain-aware reflections. The self-check pairs reverse-scored behavioural items with a claim-evaluation reasoning probe, an alternative-uses creativity probe, and a small retrospective before-and-after block. PAUSE does not assume that AI use is harmful. It only addresses where AI substitutes for effort a person may want to preserve. The application is privacy-preserving by design: scoring is deterministic and runs client-side, no personal data is required, nothing is transmitted or stored beyond the browser session, and no LLM is involved in production. PAUSE is a self-reflection tool. It is not a validated psychological instrument.

---


### 6. [TestHallVQA: Exploring LVLMs' Document-Level Reasoning under Redundant Contexts from Scientific Exams](https://arxiv.org/abs/2609.13158)

**<font color=#1a73e8>作者：</font>** Yongqi Yu, Yu Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Vision--Language Models (LVLMs) are increasingly expected to perform visual question answering (VQA) over planar media. However, existing planar VQA benchmarks typically emphasize isolated challenges: some emphasize long-document understanding with limited reasoning depth, while others require complex visual reasoning but remain restricted to single-page, noise-free settings. Moreover, through theoretical analysis, we identify the impact of irrelevant visual tokens, which leads to measurable performance degradation but has received little attention with respect to systematic quantification. To address these limitations, we introduce TestHallVQA, a multi-image VQA benchmark that simultaneously embodies document-level scale and the difficulty of human examinations, while providing comprehensive task coverage. Leveraging TestHallVQA's ability to controllably inject multi-level contextual redundancy, we further propose a novel metric, F1-R\textsuperscript{2}, which jointly quantifies LVLMs' computational reasoning capability and their evidence retrieval robustness against document-level redundancy. Extensive experiments and analyses on mainstream LVLMs reveal their latent deficiencies across multiple dimensions, offering concrete insights and directions for future research. The associated datasets, code, and complete theoretical derivations are available at this https URL.

---


### 7. [LLMs Unplugged: Teaching Resources for a ChatGPT World](https://arxiv.org/abs/2609.13183)

**<font color=#1a73e8>作者：</font>** Ben Swift  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are everywhere, yet many learners lack a concrete mental model of how they generate text. This paper presents LLMs Unplugged, an unplugged set of activities that teaches the training-to-generation loop (and beyond) using hand-built n-gram models and simple weighted sampling. Workshops based on these resources have been delivered to over 400 participants across secondary, tertiary, and executive-education contexts, and participants report that the activities demystify LLMs by reframing them as probabilistic "next word generation" at scale. All resources are freely available under a Creative Commons license at this http URL, with a modular design that supports anything from a one hour crash course to a several-day intensive workshop.

---


### 8. [LLMs or Naive Bayes? Old Gems or New Ways](https://arxiv.org/abs/2609.13185)

**<font color=#1a73e8>作者：</font>** Mohammad Firas Sada, Dmitry Mishin, John Graham 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) prompt a recurring question in research computing: should classical methods like Naive Bayes (NB) be retired? We benchmark Complement Naive Bayes against zero-shot and few-shot LLMs spanning four model families and a 37x range in scale (27B to a 1T-parameter mixture-of-experts) across text classification tasks. LLMs dominate only in zero-data regimes (98.0% vs 88.2% on Amazon Polarity sentiment), and even that win is contamination-prone: on a low-contamination sentiment task NB beats the zero-shot LLM (81.7% vs 73.0%). However, once labeled data is available (e.g., AG News), NB reaches 89.1% accuracy, statistically indistinguishable from the zero-shot 27B LLM (89.0%) and better than the 397B frontier model (84.8%), at thousands of samples/sec on a commodity CPU. Fine-tuned DistilBERT reaches 90.6% but at far lower throughput than NB at batch size 1 (Table 2). Our measured GPU throughput analysis shows small-LLM batched inference is 40-486x slower than NB CPU inference (the multiplier depends strongly on the host CPU), exposing a structural gap bounded by memory bandwidth, with roughly two orders of magnitude lower energy per sample. For resource-constrained HPC practitioners performing text classification with labeled data, NB remains the optimal choice. We show the decision line is task-dependent (NB reaches LLM parity around $N \sim 10^4$ labels for topic classification, while zero-data sentiment favors the LLM at all N tested) and provide a Kubernetes Helm operator that automates model selection using configurable thresholds and verifiable Prometheus metrics.

---


### 9. [Evaluating LLM-Generated Rules for Heart Disease Prediction](https://arxiv.org/abs/2609.13192)

**<font color=#1a73e8>作者：</font>** Feisal Alaswad, Batoul Aljaddouh, Maher Alrahhal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study compares traditional machine learning models and Large Language Model (LLM)-generated rule-based systems for heart disease prediction using the UCI Heart Disease dataset. Several classifiers, including Logistic Regression, K-Nearest Neighbors (KNN), Support Vector Machine (SVM), Naive Bayes, Decision Tree, and Random Forest, were evaluated alongside rule-based systems generated using GPT-4o and Claude Sonnet 4.6. Model performance was assessed using accuracy, precision, recall, and F1-score metrics. Experimental results show that traditional machine learning models consistently outperform LLM-generated rule-based systems in predictive performance. Random Forest achieved the best overall performance with 90.2% accuracy, a precision of 0.829, perfect recall of 1.0, and an F1-score of 0.906. Naive Bayes followed closely with 88.5% accuracy and an F1-score of 0.881. In contrast, the LLM-generated rule models achieved lower performance, with Claude Sonnet 4.6 reaching 80.3% accuracy (F1-score: 0.833) and GPT-4o obtaining 70.5% accuracy (F1-score: 0.690). Despite the performance gap, the LLM-generated rules provide interpretable IF-THEN diagnostic logic that enhances explainability and transparency in clinical decision-making. These findings highlight the trade-off between predictive performance and interpretability in medical artificial intelligence systems. The complete implementation of all experiments, including machine learning models and LLM-derived rule classifiers, is publicly available in the GitHub repository at this https URL .

---


### 10. [Criticality in Dissimilar Decomposition and Undersampling of Random Datasets with Anomalies](https://arxiv.org/abs/2609.13201)

**<font color=#1a73e8>作者：</font>** Ghurumuruhan Ganesan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training datasets for upcoming LLMs would include a significant amount of AI text/image data generated from current LLMs. In such a scenario, it is important to understand how this affects batch decompositions and thereby, the performance of the resultant new LLM. In this paper, we consider AI generated data as anomalies ``linked" to main data points and study decomposition and undersampling properties of the overall random dataset. We use redundancy graphs and iteration techniques to obtain bounds for the minimum size of a strongly dissimilar (SD) decomposition and demonstrate a phase transition phenomena, wherein the minimum size is essentially determined by the \emph{main} data points when the number of anomalies is small and is ``taken" over by the anomalies above a certain threshold. We also establish a size criticality result for the strong similarity of a randomly undersampled dataset and illustrate our results with examples involving categorical datasets, whose overall space size is much larger than the size of the dataset.

---


### 11. [Part Grounding, Not Action Knowledge: Locating the Bottleneck in VLM Affordance Prediction](https://arxiv.org/abs/2609.13225)

**<font color=#1a73e8>作者：</font>** Sarthak Sattigeri  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Benchmarks agree that vision-language models reason poorly about low-level manipulation, but an aggregate accuracy score does not say which step fails. We separate two steps that affordance questions conflate: identifying which part of an object to act on, and knowing what action that part requires. Across 19 articulated objects we asked eight models, spanning three developers, what motion a robot should apply. Under an open prompt, push was produced once in 64 evaluations where it was correct, despite being correct for 8 of 19 objects and appearing in the offered label set every time. Inspecting the outputs showed why: models described a different part than the one being scored, e.g. explaining how to pick up a camera rather than press its button. Naming the target part raises action accuracy by 0.32 to 0.63 for every model, from 0.158-0.474 to 0.684-0.947, and push recall from 0-1/8 to 7-8/8. No model beats a constant answer that ignores the image under the open prompt; once the part is named, all eight do. Asked to describe the same part in free prose with no label set, models produce pressing language for 6 to 8 of 8. These results are hard to reconcile with missing action knowledge, and instead point to part grounding as the dominant bottleneck, a pattern that holds across all three model families and does not diminish with capability. Naming the part supplies the grounding variable, so this bounds what a perfect part detector would offer rather than demonstrating a general model of mechanics. Two supporting results agree: on real photographs only three of eight models localize grasp points better than a constant baseline, and on rendered objects none do. We also document two measurement errors of our own, a threshold that let a constant baseline score 0.929 and a labelling rule wrong on 4 of 19 objects, both caught only by testing our numbers against trivial alternatives.

---


### 12. [Don't Just Look, Intervene: Perturbation Based Region Labeling for VQA Images](https://arxiv.org/abs/2609.13228)

**<font color=#1a73e8>作者：</font>** Marko Jojic, Zhaonan Li, Ben Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Language Models (VLMs) should rely on visual evidence that directly determines the correct answer, but supervision for grounding visual reasoning is often expensive to obtain manually or tied to dataset-specific annotation primitives. We instead introduce model-causal visual evidence as an annotation target, defined as the set of image regions whose counterfactual intervention changes a model's answer distribution for a given image-question pair. Based on this principle, we introduce Counterfactual Search for Grounding Regions (CSGR). CSGR is a scalable pipeline that proposes candidate regions, perturbs them, measures their effect on answer sensitivity, and aggregates this evidence across multiple judges to approximate answer-critical regions in VQA data. To assess whether CSGR annotations contain a useful supervision signal, we plug them into three existing grounding-aware training routines: attention steering, Visual CoTfinetuning, and latent visual reasoning. These experiments test whether the proposed annotation scheme can provide a useful supervision signal across multiple ways of consuming region labels, rather than introducing a new way of using them. Across competing automatic region-labeling mechanisms, CSGR annotations provide the most consistent gains over Cross Entropy-only finetuning in both in-domain and out-of-domain evaluations, indicating that the proposed labeling scheme captures useful region-level information.

---


### 13. [Clinical Reasoning Under a Partially Observed Objective in Cone Beam CT Report Generation](https://arxiv.org/abs/2609.13238)

**<font color=#1a73e8>作者：</font>** Ajo Babu George, Govind Arun, Sidharth N Krishna 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Maxillofacial report generation from cone beam computed tomography is scored here by a composite objective placing 80% of its weight on a large language model judgement of factual entailment and 20% on lexical overlap, of which only the lexical fifth is visible during development. The grader's BLEU-4 and METEOR routines are reproduced in pure Python and match the reference to machine precision, and an offline entailment surrogate, which tells a report written for one patient from one written for another at an area under the curve of 0.987, makes the composite objective cheap enough to optimise directly. Over the 622-case public release, a report selected against the visible lexical ranking scores 0.2909, whereas one selected against the composite objective scores 0.4122, because pursuing n-gram overlap drives entailment precision from 0.522 down to 0.266. A 29 million parameter encoder fine-tuned on the release reaches a prevalence-weighted out-of-fold area under the curve of 0.486 over 985 statements, indistinguishable from the corpus prior, while nine numbers read from the image header reach 0.945 for mandible coverage and 0.872 for condyle coverage, and acquisition centre alone predicts sentence choice at 0.718 against 0.663 for the image-derived model, identifying dictation convention rather than anatomy as the quantity the lexical metrics reward. The delivered system emits eight unconditional statements and five gated on header geometry under polarity, laterality and tooth-level consistency constraints, and reaches METEOR 0.3542 over 50 held-out cases from an unseen centre. The dataset and code are available at this https URL

---


### 14. [ArtSociety: Multi-Agent Multimodal Collaboration for Art Emotion Understanding](https://arxiv.org/abs/2609.13240)

**<font color=#1a73e8>作者：</font>** Jian Li, Fanfan Ji, Jinxiang Lai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The AffectiveArt Multidimensional Art Emotion Understanding task asks to jointly predict an artwork's fine-grained emotion (12 classes, 1549:1 head-to-tail ratio), binary valence/arousal, and five attribute-grounded descriptions -- sub-tasks that exhibit strong empirical trade-offs, so the single-model solutions we tried do not jointly optimize all of them well. We present ArtSociety, a multi-agent framework that assembles heterogeneous multimodal experts -- a DINOv2-Giant vision agent (A1), a scene-grounded CoT fine-tuned MLLM (A2), and three closed-source reasoning agents (A3-A5) -- and coordinates them with two training-free controllers: (i) a rare-class-aware voting arbiter that lowers the agreement threshold for tail emotions, exploiting decorrelated error patterns across agent families; and (ii) a description-first reasoning agent whose DESCRIBE-then-CLASSIFY chain of thought forces visual evidence before label commitment, yielding near-perfect grounded descriptions. A task-routing policy directs the hard emotion task to the full five-agent ensemble while assigning the near-saturated valence/arousal and generative description tasks to the single strongest reasoning agent. On the official test set (1,000 artworks), ArtSociety achieves an Overall Score of 0.8870 (Classification 0.7789, Description 0.9952). An eleven-variant ablation study reveals that, once method and scale saturate at around 0.76, the decisive gains come from agent collaboration and data-side supervision -- a 30B MoE model trained on older data does not outperform an 8B model trained on better data. Code is available at this https URL

---


### 15. [Evaluation of MLLM-Agnostic Plug-and-Play Keyframe Selection Methods for Long Video Understanding](https://arxiv.org/abs/2609.13250)

**<font color=#1a73e8>作者：</font>** Dilip Sarkar, Md. Safayet Islam, Liang Liang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) cannot process every frame of a long video because of limitations in visual-token and computational budgets. Three primary approaches have been proposed to enhance their long-video understanding capabilities: (i) Retraining an MLLM on a large video corpus and/or extending its input length; (ii) Training an adapter for a specific MLLM that takes the entire video and the query as input and selects the most relevant video frames; and (iii) Developing a training-free, plug-and-play (PaP) adapter that is MLLM-agnostic. We refer to the third approach as PaP keyframe selection. A PaP method may use only candidate video frames without considering the query, or it may use both candidate video frames and the query. The first approach is prohibitively expensive. The second approach requires substantial training time and computational resources, but it is accessible to many because an adapter contains significantly fewer trainable parameters than an entire MLLM. The third approach has the lowest computational cost and is therefore broadly accessible. To the best of our knowledge, only five PaP methods have been reported within the past year. All of these methods have been evaluated on one or more video question-answering benchmarks and have demonstrated improvements in long-video understanding. However, the methods were evaluated on different benchmarks using different MLLMs. We present a comprehensive evaluation of these five methods using three MLLMs across three long-video understanding benchmarks. Our results show that QAaF achieves the best performance in 13 of the 15 aggregate evaluation settings, while FOCUS ranks second overall. These results provide a common experimental reference for comparing training-free keyframe-selection methods for MLLMs.

---


### 16. [Preserving Subject-Clarity in Image Outpainting with Multiscale Wavelet Supervision](https://arxiv.org/abs/2609.13251)

**<font color=#1a73e8>作者：</font>** Abhilash Neog, Taewan Kim, Yi Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Commercial and advertising images are frequently affected by poor framing, partially cropped subjects, truncated text or logos, and insufficient context, all of which can reduce subject clarity, i.e., the ability of an image to clearly communicate its primary subject. Image outpainting offers a scalable solution by extending image boundaries and recovering missing content and context. However, existing diffusion-based outpainting methods often produce visually plausible completions while degrading subject fidelity through structural inconsistencies, semantic drift, or loss of fine-grained detail. To address this limitation, we propose a subject clarity outpainting framework that combines vision-language model (VLM)-guided semantic conditioning with multiscale wavelet supervision for subject-localized detail preservation. To support training, we develop a subject-centric data curation pipeline that constructs subject-intersecting outpainting pairs from advertising and natural images. The resulting objective introduces no additional inference cost and is designed to be compatible with diffusion-based backbones. Across four advertising and natural-image benchmarks, our method improves subject clarity, reducing subject-centered DreamSim error and FID on average by 3.0% and 2.4% over matched supervised fine-tuning, and by 10.8% and 7.7% over the strongest state-of-the-art approach per dataset, respectively.

---


### 17. [(How) Do MLLMs Report Bistable Images Like Humans?](https://arxiv.org/abs/2609.13254)

**<font color=#1a73e8>作者：</font>** Ryota Takatsuki, Tomoki Doi, Amane Watahiki 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bistable images such as the duck-rabbit are classic stimuli in which one image supports multiple mutually incompatible interpretations, typically reported one at a time in humans. We ask whether multimodal large language models (MLLMs) show similar report behavior and what internal computations support it. Using the LLaVA family, we study two tractable dimensions: modulability, whether reports can be biased by bottom-up visual cues and top-down linguistic priors, and exclusivity, whether responses commit to a single interpretation. We test both on the canonical duck-rabbit and on synthetic Visual Anagrams to mitigate memorization confounds. Behaviorally, both visual and linguistic manipulations systematically shift reports in human-consistent ways, while responses remain predominantly exclusive. Mechanistically, these effects arise from competing image-token representations, distinct pathways for bottom-up and top-down modulation, and a link between exclusive reporting and object-count encoding. Code and data are available at this https URL.

---


### 18. [Sampling headroom is not selection gain: a compute-value audit of test-time scaling for video world models](https://arxiv.org/abs/2609.13257)

**<font color=#1a73e8>作者：</font>** Yuhua Jiang, Junjie Lu, Feifei Gao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time scaling (TTS) can improve generation only when additional compute produces better candidates and the system can reliably identify them. This distinction is especially important for video world models, where a wider sample pool may contain stronger rollouts without improving the output that is ultimately selected. We introduce the Compute-Value Audit (CVA), a sequential framework that asks whether extra sampling creates opportunity, observable signals provide a reliable state, that state supports a beneficial action, and the resulting gain exceeds the full entry fee of generation and verification. On 192 Physics-IQ scenes, expanding the pool from 4 to 16 candidates increases oracle quality by +9.23 IQ (95% CI [+7.44, +11.14]), but Flow, Cycle, and VideoReward fail to recover this headroom reliably. Across three generators, none of twelve adaptive-depth policies outperforms uniform compute; they recover only 42-69% of the measured entry fee. A matched-60-NFE Predict-and-Perturb intervention on VideoPhy2 is likewise negative across three fresh-seed replicas. These negative results are not universal: anchor-explorer passes all four stages in a sparse PRM800K setting, MMLU-Pro exposes the gap between predictive state and useful action, and a privileged paired future establishes a positive video upper bound. Together, these results show that sampling headroom has deployment value only when it can be converted into a reliable decision whose benefit survives the complete compute charge. Code is available at this https URL.

---


### 19. [Interpretable Temporal Video Reasoning with EventGraph and EventField](https://arxiv.org/abs/2609.13258)

**<font color=#1a73e8>作者：</font>** Durgendra Narayan Singh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a structured temporal video reasoning pipeline built around a discrete EventGraph, a continuous EventField, and a human-readable EventGlyph view. On a calibrated EPIC-KITCHENS subset of 10 videos and 50 temporal reasoning questions, EventField+Glyph achieves 0.98 overall accuracy, which is higher than the caption baseline by +0.40 (paired p = 1.1 \times 10^{-5}) and direct VLM-only QA by +0.20 (p = 0.0063) on this subset. We further evaluate annotation-source variations, including manual, heuristic, and heuristic+Gemini pipelines, and find that the best structured method stays above the caption baseline across settings. We also include cross-video pair benchmarking and an appendix gallery of glyph outputs for all studied videos. Overall, the results indicate that structured temporal representations can support both performance and inspectability by preserving symbolic structure, capturing temporal continuity, and providing human-readable diagnostics for video reasoning.

---


### 20. [TryOnReward: Learning Foveated Consistency for Reinforcement Fine-Tuning of Virtual Try-On](https://arxiv.org/abs/2609.13259)

**<font color=#1a73e8>作者：</font>** Xueheng Li, Yong Liu, Xiaolong Fu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Virtual Try-On (VTON) aims to dress a person with the reference garment, producing visually reasonable results aligned with human preferences. Turning this preference-oriented goal into an actionable objective relies on a scoring function aligned with human taste. However, classic fidelity metrics exhibit weak correlation with human judgments, and generic VLMs fail to provide the discriminative granularity demanded by try-on quality evaluation, which hinges on faithfully preserving garment and person details. This shortcoming is further exacerbated in the reinforcement fine-tuning (RFT) optimization and leads to severe reward hacking. To this end, we present TryOnReward, a fine-grained reward model tailored for VTON. Built on a vision-language backbone, it adopts a foveation calibration objective that grounds each quality dimension in the relevant region to avoid global shortcut learning. Meanwhile, TryOnReward jointly optimizes pairwise preferences and per-dimension quality scores via margin-aware supervision, leveraging both relative and absolute quality signals. For model training and evaluation, we build TryOnReward-100K, a human-annotated per-dimension rating dataset, alongside TryOn-Bench and TryOnRewardBench, two benchmarks covering diverse real scenarios. Extensive experiments confirm that TryOnReward significantly outperforms generic judges in human preference alignment, and when serving as the RFT reward function, it consistently yields human-preferred try-on results across multiple baselines.

---


### 21. [From Process Loss to Assembly Bonus: Human-Grounded Diagnosis of Multi-Agent LLM Collaboration](https://arxiv.org/abs/2609.13261)

**<font color=#1a73e8>作者：</font>** Ala N. Tak, Teruhisa Misu, Kumar Akash 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly used for collaborative problem solving and human-group simulation. This makes outcome-only evaluation insufficient: if LLM groups are used as models of human groups, we need to know whether they succeed or fail through human-like deliberative mechanisms. We compare human group chats with matched LLM deliberation traces on Wason-style deductive reasoning, then test whether the same process signatures generalize to analogical, abductive, and analytical tasks. Humans and LLMs show the same assembly bonus asymmetry: discussion improves the average member more often than the best initial member. Initial-answer diversity accounts for the effect of model heterogeneity, increasing movement in both corrective and destructive directions. The main differences are process-level. Compared with humans, LLM groups follow majorities more often, surface less unique information, and converge earlier; correct minority signals succeed mainly when re-expressed early. Interventions motivated by human group-decision research yield modest improvements in collective outcomes, but do not remove the coordination bottleneck. Together, these results suggest that LLM groups can reproduce some outcome-level patterns of human deliberation while diverging in the mechanisms that generate assembly bonus and process loss, with implications for group simulation and human-AI collaboration.

---


### 22. [Structure-Token Evidence-Anchored Reasoning for Scientific Chart Understanding](https://arxiv.org/abs/2609.13267)

**<font color=#1a73e8>作者：</font>** Alberlucia Rafael Soarez, Camila Ferreira, Daniel Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scientific charts encode quantities in axes, legends, and geometric marks, yet large vision-language models still treat them as natural photographs. Visual in-context examples do not expose the coordinate frame; unconstrained chain-of-thought can name a plausible number that was never read from a bar. We present STEER (Structure-Token Evidence-anchored Reasoning), which freezes a Llama-3.2-Vision encoder and inserts three modules: a chart structure graph encoder (CSGE) that binds ticks, legend items, and marks; evidence-anchored step reasoning (EASR) that forces every arithmetic step to cite a graph node; and weak-parser strong-reasoner alignment (WPSR) that uses a specialized table extractor only as a teacher of node attributes. On ChartQA, STEER reaches 82.70 average relaxed accuracy versus 80.16 for ChartGemma and 76.40 for a LLaVA-CoT backbone trained on the same mix. Gains widen on CharXiv reasoning (33.60 vs. 29.20 InternVL Chat V1.5) and ChartQAPro CoT (40.70 vs. 37.17 Qwen2-VL-7B), where OCR shortcuts disappear. Ablations show that dropping node serialization or numeric candidate constraints undoes most of the reasoning lift.

---


### 23. [Capability-Routed Visual Retrieval and Evidence Threading for Long-Context Document Question Answering](https://arxiv.org/abs/2609.13268)

**<font color=#1a73e8>作者：</font>** Amirul Rahman, Aisha Karim, Kenji Nakamura 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Annual reports, diligence packs, and infographic dashboards bury numbers in page images: axes, cell grids, and footnotes that OCR pipelines flatten and that page-level visual retrievers still treat as interchangeable in-context examples. We keep a frozen Qwen2.5-VL-7B-Instruct generator and a ColPali / VisRAG-Ret page index, and insert three modules. A capability-aware visual router (CAVR) tags each retrieved page as text, table, chart, layout, or mixed and mixes specialist experts before generation. Weak-to-strong page selection (WSPS) distils a frozen 7B answerability teacher into a 3B selection head so ranking is no longer a single InfoNCE score. Visual evidence threading (VET) builds layout-anchored paths of length at most three and lets the generator read the thread rather than a flat top-$k$ list. On gold-page DocVQA / ChartQA / InfographicVQA the 7B system reaches 96.3 / 90.1 / 85.4. Under the VisRAG top-3 protocol the mean generation accuracy is 62.74 versus 59.39 for the same backbone with concatenation. On MMLongBench-Doc retrieve-then-read, F1 moves from 19.2 to 22.6 and multi-page accuracy from 16.4 to 21.2. ViDoRe nDCG@5 after WSPS reranking is 83.6, with TAT-DQA financial reports at 70.4.

---


### 24. [RxScribe Bench: A Multi-Axis Benchmark for Evaluating Vision-Language Models on Indian Outpatient Prescriptions](https://arxiv.org/abs/2609.13280)

**<font color=#1a73e8>作者：</font>** Somil, Vijay Saini, Vidit Verma 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prescription transcription errors are not interchangeable. A model that fabricates a drug and a model that misreads a legible dose pose very different clinical risks, yet prescription-transcription accuracy is typically reported as a single blended figure that treats the two as equivalent. We introduce RxScribe Bench, a benchmark for evaluating vision-language models on handwritten prescription digitization that decomposes performance into four axes tied to clinical severity, rather than folding everything into a single aggregated score. Given only a prescription image and an output schema, a model produces a structured record, which is then compared field by field against a human-authored ground truth of identical shape, with each field also labeled for visibility and legibility. The four axes isolate distinct failure modes, namely Correctness, Hallucination, Engagement, and Robustness. The Robustness axis withholds its hard-field results rather than reporting one when the supporting sample falls below a minimum-evidence threshold. We evaluate frontier vision-language models on real prescriptions across independent cold runs per image, and find that no single model wins across all four axes.

---


### 25. [LLaDA-UI: Bringing Block-wise Diffusion to Vision-Language GUI Agents](https://arxiv.org/abs/2609.13287)

**<font color=#1a73e8>作者：</font>** Zhangxuan Gu, Haoxing Chen, Qi Qin 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) achieve high decoding efficiency through block-parallel, arbitrary-order generation, making them attractive for latency-sensitive applications. GUI agents represent a natural testbed for this paradigm, as they must repeatedly perceive screen states and emit structured, spatially grounded actions in real time. However, whether dLLMs can be extended into capable multimodal GUI agents while preserving their parallel decoding advantage remains an open question. We present LLaDA-UI, a 16.7B-parameter MoE-based, block-wise diffusion vision-language GUI agent. LLaDA-UI follows a two-stage training pipeline: general multimodal pre-training aligns a native-resolution vision encoder with the LLaDA2.0-mini-base diffusion language backbone, followed by GUI-agent supervised fine-tuning on diverse mobile, desktop, web, and grounding data. Across widely adopted grounding benchmarks and navigation benchmarks spanning multiple platforms, LLaDA-UI substantially outperforms Qwen2.5-VL-7B and surpasses Qwen3-VL-8B on four of six reported GUI benchmarks. These results establish block-wise diffusion as a practical generative paradigm for multimodal GUI agents.

---


### 26. [Target-Checked Reliability Score Refinement for Video Question Answering](https://arxiv.org/abs/2609.13288)

**<font color=#1a73e8>作者：</font>** Guoxiang Ren, Rohitash Chandra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video-language models can answer multiple-choice questions with high confidence yet be wrong. We study whether answer-level reliability scores can be improved under target shift without retraining the models or changing their answers. We collect option-probability lists from three fixed video-language models under four deterministic video samplings and represent cross-view changes and cross-model agreement as a response graph. Using a labeled target pilot, we compare the original score, defined as the probability assigned to the chosen answer, with a histogram-based gradient-boosting (HGB) score trained on the development datasets and a regularized logistic-regression score trained on the target pilot. A candidate replaces the original score only when repeated video-level checks indicate a positive, stable improvement. We develop this rule on public VideoQA benchmarks and Video Hallucination Diagnosis (VHD), a controlled diagnostic dataset for shared high-confidence errors. Ranking quality is measured by the area under the risk-coverage curve (AURC), where lower is better. On a held-out 963-question HERBench split, the method reduces mean AURC across the three models by 16.64% (95% confidence interval (CI), 12.12 to 22.61%); the smallest model-level gain is 11.39%. On a separate held-out 911-question Perception Test split, the mean reduction is 18.87% (95% CI, 15.43 to 22.14%). For InternVL3.5, the target check retains the original scores. Using the same outputs, the method outperforms seven training-free baselines in mean AURC on both datasets. It also improves AUROC, reduces calibration error, and lowers the error rate at 50% coverage by 6.50 and 6.58 percentage points.

---


### 27. [Harnessing Image Question Dependence for Better VLM Test-time Reinforcement Learning](https://arxiv.org/abs/2609.13296)

**<font color=#1a73e8>作者：</font>** Xinrui He, Ting-Wei Li, Junting Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time reinforcement learning can adapt vision-language models (VLMs) to unlabeled target data, but its effectiveness is fundamentally limited by the reliability of self-generated learning signals. To assess the reliability of consensus-based learning signals, we analyze VLM test-time reinforcement learning across diverse VQA datasets and model sizes, revealing two limitations. First, gains from consensus-based test-time training largely come from answer normalization rather than content correction. Second, many initial VLM responses are incorrect due to the model's limited ability to jointly use the image and the question; consensus rewards derived from these outputs may preserve the resulting grounding errors rather than correct them. Motivated by these, we propose TTIQ, a test-time reinforcement learning framework that harnesses image-question dependence for better vlm adaptation. TTIQ teacher-forces each sampled response under the original image-question pair and its image- and question-ablated variants, using the resulting token-level likelihood changes to estimate dependence on each input. It combines image and question dependence with calibrated confidence to construct a response-level reward that favors jointly grounded responses, and uses the token-level signals to assign greater positive policy credit to tokens supported by both inputs. This design favors responses that are jointly grounded in the image and the question and sufficiently confident, rather than merely popular. Experiments across eight VQA datasets and multiple VLM sizes show that TTIQ achieves the best average performance at every model scale. It further generalizes across VLM families, while models trained on one dataset improve performance on unseen datasets without further training.

---


### 28. [AI Use Conditions and Perspective Diversity in Ethical Decision-Making: A Pilot Study of Human Reasoning Processes](https://arxiv.org/abs/2609.13302)

**<font color=#1a73e8>作者：</font>** Byeongmu Choi  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative artificial intelligence (AI) is increasingly used to support human decision-making, yet less attention has been paid to how AI may influence the reasoning processes that precede final judgments. This pilot study explored whether different AI-use conditions were associated with differences in reasoning breadth during ethical decision-making. Twenty-nine participants completed an ethical dilemma under one of three conditions: AI-Prohibited (n = 10), AI-Optional (n = 10), or AI-Mandatory (n = 9). Responses were evaluated by three independent blind coders using two exploratory measures: the Counterargument Diversity Score (CDS) and Perspective Diversity Index (PDI). Participants across conditions generally converged on similar ethical conclusions, most commonly favoring disclosure and customer protection. However, participants in the AI-Mandatory condition considered a broader range of perspectives, including legal, regulatory, organizational, technical, and ethical viewpoints. A statistically significant overall difference in PDI scores was observed across the three conditions, whereas differences in CDS were not statistically significant. These findings suggest that generative AI may not necessarily alter final ethical judgments but may be associated with broader exploration of perspectives prior to reaching those judgments. Given the small sample size, the findings should be interpreted cautiously and examined in larger studies.

---


### 29. [GroundBench: A Factorized, Counterfactual Benchmark for Locating VLM Affordance Failures](https://arxiv.org/abs/2609.13308)

**<font color=#1a73e8>作者：</font>** Sarthak Sattigeri  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A companion evaluation found that naming the target part in a manipulation prompt increased action accuracy by 0.32-0.63 across eight vision-language models, with no model outperforming a constant baseline until the part was named. However, naming the part supplies information that a real system must infer, confounding visual grounding, mechanical reasoning, and category-to-action association. We introduce GroundBench, a diagnostic benchmark that separates these explanations through six branch-and-merge conditions, each adding a controlled information bundle, and a counterfactual re-ask targeting a real alternate part visible in the same image. Across three OpenAI models and 1,068 predictions, supplying the target region without its identity leaves action accuracy at or below the 0.53 majority baseline (0.26, 0.26, and 0.53), although the models largely reproduce the supplied region. Supplying identity without location instead yields 0.74, 0.68, and 0.68. Every above-baseline gain in this curated set occurs where the supplied part category itself determines the action. A no-vision control leaves GPT-5's scores unchanged or improved, providing evidence consistent with substantial category-to-action association. GPT-4o mini declines on one condition, so this interpretation is not universal. Adding joint type and motion axis does not improve accuracy across six model-stratum comparisons. On 74 counterfactual pairs from 32 objects, GPT-5 achieves 0.86 pair-weighted compliance with a 0.07 shortcut rate but fails all observed push-to-lift-vertical cases. GroundBench identifies which supplied information changes affordance behavior and tests whether apparently grounded performance can be reproduced through textual shortcuts.

---


### 30. [SkillAtlas: An Attack Trace Library for Agent Skills](https://arxiv.org/abs/2609.13353)

**<font color=#1a73e8>作者：</font>** Yuxin Tian, Zenghao Duan, Liang Pang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent skills are reusable units for language-model agents, but their risks emerge through model decisions, user context, tool calls, and execution feedback rather than through stable signatures or a single sandbox run. Existing static, dynamic, and benchmark-style evaluations rarely preserve public evidence that can be inspected, searched, and reused. We present SkillAtlas, a hosted attack trace library that converts private agent-skill security report bundles into reviewed, redacted, and searchable public cases. The library contains 3,014 cases, 6,589 traces, 151,131 steps, 233 affected skills, and 8 risk categories; 42.5% of successful cases first become successful after a non-success initial round, and trajectory-grounded labels improve pre-execution guard accuracy to 0.770.

---


### 31. [ZGCM-1: A Fully Open and Extremely Efficient Foundation Model for Math and Agentic Search](https://arxiv.org/abs/2609.13356)

**<font color=#1a73e8>作者：</font>** Jiyan He, Guang Liang, Hao Liu 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this work, we present ZGCM-1, a fully open 7B dense foundation model trained from scratch with extreme data, system, and algorithmic efficiency. ZGCM-1 is founded on a core premise: compact models cannot passively memorize the open web, but can overcome parametric capacity limits by coupling deliberate internal thinking with active external tool use. To support this paradigm across a 256K context, we develop an end-to-end, high-efficiency open training recipe: Architecture & System Co-design: interleaved gated sliding-window and full attention, and a stable FP8 Muon optimizer; Progressive Curriculum & MDP Mid-Training: context scaling across 16K, 64K, and 256K, and the reformulation of interaction traces into Markov Decision Processes. Furthermore, we establish an AI-native R&D workflow where agent swarms autonomously manage cluster operations, data curation, and rapid diagnostic evaluation. Extensive evaluations show that ZGCM-1-7B is competitive across 7B model family on general benchmarks. On several challenging mathematical reasoning and agentic search suites, it remains competitive with frontier models orders of magnitude larger, such as Qwen3-235B-A22B and GLM-5.1. We also show that our pre-training design offers a ~4.2x efficiency improvement in 16K pre-training time-to-loss. Across the full development lifecycle, we distill eight actionable empirical findings-spanning architectural scaling, SFT quality pruning, long-context generalization, and agentic co-training dynamics. To facilitate community research, we open-source model weights from the pre-training, mid-training, and post-training stages, intermediate checkpoints, training code, per-stage data and data recipes, and W&B logs.

---


### 32. [RFCLLM: Evaluating LLMs' Reasoning Ability of Network Protocol State Machines](https://arxiv.org/abs/2609.13389)

**<font color=#1a73e8>作者：</font>** Anqi Chen, Dan Goldwasser, Cristina Nita-Rotaru  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mapping textual specifications into formal representations is essential for ensuring the correctness of protocol designs and implementations. LLM-generated mappings, used for networking security or testing, are assumed to capture a perfect understanding of the specification, which may not hold in practice. The goal of this paper is to assess the extent to which LLMs can interpret the specification correctly. We examine the degree to which an LLM's implicit representation of a finite-state transition system-defined via natural language descriptions-aligns with a manually generated ground-truth model. We designed 4 tasks and 1482 task queries for 16 protocols. We evaluated different judge biases, observed the inherent difficulty gaps between tasks, looked into the effect of 4 context types, and the influence of protocol characteristics. Our work contributes to a step toward verifying whether LLMs can really be trusted in FSM (Finite State Machine) reasoning of protocol specifications.

---


### 33. [Task-Aware Federated Fine-Tuning for MoE-based Large Language Models](https://arxiv.org/abs/2609.13395)

**<font color=#1a73e8>作者：</font>** Tingqi Wang, Hongyu Ke, Haoxin Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) has become a widely adopted architecture for Large Language Models (LLMs), as it improves model capacity while limiting computational overhead through sparse expert activation. This property makes MoE-based LLMs particularly attractive for resource-constrained distributed environments. However, federated fine-tuning of MoE-based LLMs remains challenging under heterogeneous client data. Since clients often correspond to different task preferences, directly aggregating their local updates may weaken expert specialization and introduce conflicting update directions on shared experts. To address these challenges, we propose FedTAR, a task-aware federated fine-tuning method for MoE-based LLMs. FedTAR establishes the association between local updates and task preference via routing outputs. Specifically, we apply Singular Value Decomposition (SVD) to both routing features and local updates to extract low-dimensional task coordinates and update directions. Based on the task coordinates, FedTAR performs intra-cluster aggregation among clients with similar task preferences and inter-cluster aggregation across different task groups. The aggregated update is then reconstructed through the learned task-to-update mapping, ensuring that the final update remains aligned with task-specific optimization directions. In this way, FedTAR preserves expert specialization and mitigates destructive interference among heterogeneous clients. We evaluate FedTAR on four benchmark tasks under different non-IID settings. Experimental results demonstrate that FedTAR consistently outperforms strong federated fine-tuning baselines and achieves state-of-the-art performance.

---


### 34. [Specification Oracles](https://arxiv.org/abs/2609.13415)

**<font color=#1a73e8>作者：</font>** Atticus Cull, Justin McCarthy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Specifications face a basic tradeoff: leave details out, and important questions go unanswered; record every detail separately, and the specification becomes large and prolix. We investigate whether a language model can serve as a compact, living specification oracle by learning facts about a target and answering questions about it directly. We compare two ways of storing the learned facts: external text notes and changes to the model's weights. Across four families of 596-fact worlds and two Qwen2.5 model sizes, weight-only oracles benefited substantially more from structure: with the 7B model, their accuracy integrated across storage capacities was 18.5 percentage points higher on structured than unstructured worlds, compared with 1.1 points for note-sheet oracles. This advantage came at a substantial storage cost, with the smallest adapter requiring approximately 175 KiB compared with a maximum note budget of 16 KiB. Adapted weights therefore exploited latent structure more successfully, while external notes required substantially less object-specific storage.

---


### 35. [Vibe Patenting: Evaluating LLM Judges for Professional Patent-Drafting Agents](https://arxiv.org/abs/2609.13422)

**<font color=#1a73e8>作者：</font>** Toshiaki Koike-Akino, Vlad Blaykhman, Ye Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM judges are increasingly used to evaluate and improve AI-generated outputs, yet their reliability for complex professional work remains unclear. We study this problem through Vibe Patenting, an end-to-end patent-drafting testbed for AI-agent evaluation. A separately-invoked LLM judge evaluates generated patent drafts and provides structured feedback for iterative revision. Across multiple inventions and drafting-agent configurations, judge-guided revision consistently improves judge-assessed quality, while unguided revision tends to saturate. Notably, iterative judge feedback enables a low-reasoning agent to approach the performance of a substantially more expensive high-reasoning agent. Stronger models and increased reasoning generally improve judge-assessed drafting quality, while domain-specific agentic workflows provide further gains. We validate the judge against independent evaluation by a professional patent attorney and find meaningful but strongly metric-dependent agreement and systematic calibration differences. These results highlight both the utility and limitations of LLM judges as evaluators and optimization signals for complex professional workflows.

---


### 36. [ReCAST: Reward Credit Assignment across Timesteps for Online Diffusion Reinforcement](https://arxiv.org/abs/2609.13425)

**<font color=#1a73e8>作者：</font>** Yihang Chen, Yuanhao Ban, Kuei-Chun Kao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training diffusion models with multiple rewards requires distinguishing user preference from reward informativeness. User preference determines how much each reward should contribute to the overall objective; reward informativeness determines when its feedback is useful during denoising. Some rewards can meaningfully evaluate a sample as soon as global structure emerges, but others become informative only when the sample is nearly clean. To address both questions jointly, we propose ReCAST (Reward Credit ASsignment across T}imesteps), the first method, to our knowledge, for per-reward, timestep-dependent credit assignment in diffusion reward fine-tuning. ReCAST separates user preferences from temporal allocation through a reward-by-timestep weight matrix $W$, whose row sums match the user-specified reward budgets $\lambda$, while its column sums are equal, assigning the same total weight to each denoising step. Under these marginal constraints, ReCAST allocates weight according to each reward's informativeness, quantified by its Rényi discriminability gain at each step. These gains telescope to the total discriminability between the reward-induced positive policy and the current policy, providing a basis for temporal credit assignment. We evaluate ReCAST by training SD3.5-Medium under two distinct four-reward settings, each across five reward budgets $\lambda$. ReCAST improves the training rewards in one setting and matches them in the other, improves every held-out judge in both, and is preferred by an independent LLM-as-a-Judge. Together, these results show that ReCAST yields improvements that generalize beyond the training rewards and support its core principle: assigning each reward greater weight at the denoising timesteps where its feedback is most informative.

---


### 37. [Toward Self-Adaptive Physical AI: Can LLM Agents Manage Long-Horizon Physical Tasks?](https://arxiv.org/abs/2609.13436)

**<font color=#1a73e8>作者：</font>** Varun Kaushik, Yayun Tan, Xiaofan Yu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents offer a promising path toward autonomously managing long-term physical tasks without human intervention. However, physical tasks require agents to continuously observe the environment, make consequential actions, and remain effective as the environment changes. Existing approaches either require substantial data and retraining, or primarily focus on agents operating in the virtual world. In this work, we explore the feasibility of building a self-adaptive physical AI agent that manages long-term physical tasks in a zero-shot manner and adapts to environmental changes without human intervention. We design a multi-agent framework that integrates planning, tool calling, observation, and verification, and evaluate it on agricultural tasks against reinforcement learning (RL) agents under different weather patterns. Our results show that zero-shot LLM agents can achieve comparable management outcomes to RL agents under the same weather pattern and adapt more effectively than RL when evaluated under a shifted environment, highlighting a promising path toward self-adaptive physical AI agents.

---


### 38. [Learning to Solve Hard Problems in RL for LLMs by Never Giving Up](https://arxiv.org/abs/2609.13443)

**<font color=#1a73e8>作者：</font>** Michael Noukhovitch, Hamish Ivison, Nathan Lambert 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We demonstrate that training LLMs with RL does not improve performance equally across a dataset. RL shows large improvements on easy problems that an LLM is already good at solving, but small improvements on hard problems. We call this the Matthew Effect in RL for LLMs, after the phenomenon of cumulative advantage from economics and network science summarized as "the rich get richer". The naive explanation is that hard problems require more compute to find a solution. We argue that modern RL methods are exacerbating the issue by wasting too much compute on easy problems and instead should dynamically reallocate how they use compute. We introduce Never Give Up (NGU), a simple adaptive sampling method that keeps generating samples for a problem until one is correct. By leveraging asynchronous RL, this naturally uses fewer samples to filter out easy problems and allocates more compute to solving harder problems. We investigate the design choices that affect NGU, such as off-policy robustness, and develop a set of best practices. On the math benchmark Deepscaler, NGU improves performance per compute, especially on harder problems. On a recent coding task, Manufactoria, standard GRPO with a per-test reward fails to fully solve problems that have a range of easy and difficult tests. NGU iteratively improves, solving harder and harder tests, until it learns to fully solve coding problems.

---


### 39. [Causal Analysis and Mitigation of Spurious Onsets in Full-Duplex Speech LLMs](https://arxiv.org/abs/2609.13445)

**<font color=#1a73e8>作者：</font>** Kento Nishi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech-to-speech LLMs like Moshi, and its derivative PersonaPlex, can listen and speak concurrently through full-duplex generation. However, they can begin speaking inappropriately during prolonged user silence: under digital-zero input, Moshi and PersonaPlex initiate speech in 12/40 and 11/40 five-minute continuations, respectively. What causes this spurious speech? We investigate two hypotheses: either repeated sampling selects speech despite persistently low onset probabilities, or conditioning on the model's nonspeech outputs causes an abrupt spike in onset probability. We find that, at every observed onset, speech probability spikes by over nine orders of magnitude in one 80-ms frame, supporting the latter hypothesis. Then, to suppress these onsets without blocking genuine responses, we ask a causal counterfactual question: is the model responding to user speech, or would its next-token distribution remain similar if the preceding user input were muted? Accordingly, we suppress onsets whose distributions change little under this intervention. Across 40 held-out trials per model with realistic microphone noise, our method suppresses 13/13 Moshi and 9/9 PersonaPlex spurious onsets, while preserving 40/40 genuine responses per model. Our inference-time method requires no retraining and runs in real-time, with 95th-percentile decision time below 61 ms, within the 80-ms frame budget. Our code is available at this https URL.

---


### 40. [Hindsight Bias in Clinical Temporal Reasoning: How Future Data Exposure Affects Large Language Model Judgment](https://arxiv.org/abs/2609.13454)

**<font color=#1a73e8>作者：</font>** Misaki Matsuura, Sayantan Kumar, Ojas Kadam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical decisions are prospective, but clinical language models are often evaluated on retrospective records that reveal the final diagnosis, treatment response, and outcome. Such evaluations may reward the use of future information rather than reasoning under the uncertainty present at the decision point. We introduce a paired benchmark for measuring outcome-conditioned shifts consistent with hindsight bias in clinical temporal reasoning. It contains 171 case reports from the PubMed Central Open Access Subset---40 sepsis and 131 GLP-1/diabetes cases---represented as both textual narratives and human-annotated and LLM-generated textual time series (TTS). For each case, questions are tied to a clinically meaningful cutoff and paired with a prospective reference answer and an outcome-consistent \emph{hindsight trap}. Models answer each question using either a TTS truncated at the cutoff or the complete timeline; additional conditions vary the narrative source (original or synthetic) and TTS annotation source (human or LLM). We evaluate accuracy (Acc), hindsight trap rate (HTR), answer instability rate (AIR), and hindsight bias rate (HBR), each of which captures different signals of hindsight bias. Across GPT 5.6 Sol, Gemma 4, GLM 5.2, and Opus 5, full timeline exposure produces consistent hindsight-sensitive shifts, while temporal masking reduces bias without lowering accuracy.

---


### 41. [TimeThink: Eliciting Compositional Reasoning in Timeseries Large Language Models](https://arxiv.org/abs/2609.13457)

**<font color=#1a73e8>作者：</font>** Sudarshan Regmi, Arvind Pillai, Yu Yvonne Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Timeseries multimodal large language models (TS-MLLMs) have recently begun leveraging the reasoning capabilities of large language models (LLMs) for question-answering tasks. However, these models often fail to capture dynamic temporal patterns, providing only implicit reasoning that lacks the underlying explanations critical for high-stakes applications like healthcare. While reinforcement learning (RL)-based timeseries language models aim to address this, they often fall short because they are trained on narrow, in-distribution data and struggle with out-of-distribution compositional questions. To address these challenges, we present TimeThink, a synthetic framework for eliciting compositional timeseries reasoning. Core timeseries primitives (e.g., trend, seasonality) are domain-independent and can be deterministically generated. Guided by this premise, TimeThink first designs a synthetic data generator that produces atomic and composite question-answer pairs, providing objective ground truth with reasoning traces. Building on this framework, TimeThink employs a reinforcement learning with verifiable rewards (RLVR) training strategy that encourages explicit reasoning. Unlike template-reliant methods, this approach enables the model to learn the underlying logic of composition rather than simply imitating traces. Extensive experiments show that TimeThink, trained only on synthetic data, significantly outperforms strong baselines on both synthetic and real-world benchmarks.

---


### 42. [Root-Cause Attribution Is a Search Problem: Continual Search for Long-Horizon Agent Failures](https://arxiv.org/abs/2609.13463)

**<font color=#1a73e8>作者：</font>** Harsh Raj, David Lee, Anas Mahmoud 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The increasing deployment of AI agents in long-horizon tasks yields massive execution logs. Diagnosing failures within these records is crucial for reliability, as it transforms outcome-level signals into actionable interventions. The sheer scale of the data renders human review impractical, driving the need for automated root-cause attribution (RCA). However, automated RCA methods using LLMs suffer from low diagnostic accuracy, especially as execution traces grow larger. They struggle because relevant information is often sparse, distributed across distant actions, and disconnected from the visible failure, reducing root-cause attribution to a massive search problem. Existing RCA methods typically rely on one-shot LLM judgments to diagnose failures from execution traces. While effective for shorter trajectories, these judges tend to settle on a plausible diagnosis early, leaving critical evidence in longer traces unexamined. We introduce Continual Search, an iterative framework that nudges the judge, over successive turns, to keep searching for unresolved diagnostic evidence. We evaluate Continual Search across four existing RCA benchmarks. Recognizing the lack of massive execution traces in current benchmarks, we introduce MegaRCA-Mix to evaluate RCA at scale. MegaRCA-Mix provides a challenging testbed of 50 human-annotated failure trials spanning long-horizon, execution-heavy tasks. Across multiple benchmark suites and model families, Continual Search consistently improves attribution performance. On MegaRCA-Mix, for example, it improves GPT-5.5's F1 score by more than 40\%, from $0.349$ to $0.498$. More interestingly, within the same model family, lower-tier models can even surpass their higher-tier counterparts, demonstrating that effective search supersedes raw model scale.

---


### 43. [OrchSLM: Probing the Dynamics of Small Language Model Orchestration](https://arxiv.org/abs/2609.13470)

**<font color=#1a73e8>作者：</font>** Chengxi Zhang, Yu Yao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Although large language models (LLMs) have demonstrated remarkable capabilities, their reliance on cloud-scale infrastructure poses fundamental challenges for deployment in agentic pipelines, including latency, privacy, connectivity, and substantial computational cost. Small language models (SLMs) offer a compelling alternative: recent studies suggest that many repetitive and narrowly scoped subtasks in agentic workloads may be better served by specialized SLMs than by monolithic LLMs. However, the limited capacity and context windows of SLMs can constrain long-horizon reasoning and interaction-heavy orchestration strategies such as iterative verification and debate. This motivates a complementary, non-interactive paradigm in which heterogeneous SLMs independently generate candidate solutions and a router orchestrates their cached samples without further model interaction. To further understand the mechanisms of such orchestration, we introduce OrchSLM, a routing framework that unifies existing non-interactive orchestration methods and exposes their underlying design choices as controllable parameters. Using OrchSLM as a systematic probe, we reveal how orchestration behavior emerges from diverse knobs, including the task structure, model-pool composition, and multi-agent consensus.

---


### 44. [Grounded Adjudication of Variations across Extracted TimeLines (GAVEL): Comparing Clinical Timelines Against Their Case Reports](https://arxiv.org/abs/2609.13475)

**<font color=#1a73e8>作者：</font>** Jack Cummins, Sayantan Kumar, Ketan Tamirisa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing pipelines for clinical timeline extraction from case reports are evaluated using an expert reference and are limited by imperfect reference annotations and imprecise event alignment. We developed GAVEL, an LLM judge protocol that compares two timelines with the case report and returns a discrepancy type, verdict, and report passage for each difference. We evaluated the event matcher, reviewed 2,738 findings from GPT5.6sol and DeepSeek V3.2, ranked six LLM extractors and two human annotators, and tested GAVEL guided merging. True match rates were 60% immediately below and 48% immediately above the 0.10 cutoff. Manual review confirmed 89.4% and 88.6% of findings. Across 126 reports, merged timelines were preferred in 77.0% of comparisons (95% CI, 69.8 to 84.1%) and reduced discrepancies attributed to the evaluated timeline from 7.63 to 0.85 per report. GAVEL supports report-based comparison and revision without treating either timeline as ground truth.

---


### 45. [A Hybrid Hierarchical 1D-CNN-BiLSTM Framework for Extractive Summarization of Biomedical and Clinical Text](https://arxiv.org/abs/2609.13481)

**<font color=#1a73e8>作者：</font>** Saad Bin Ather, Muhammad Saif, Ali Hassan Khan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models have made abstractive summarization remarkably fluent, but generated summaries can hallucinate facts, posing serious risks in biomedical and clinical domains. We address this by removing generation from the pipeline and framing summarization as extractive sentence selection. Our Hybrid Hierarchical CNN-LSTM Summarizer uses stacked multi-kernel convolutions to compose sentence-level embeddings into richer inter-sentence representations, followed by a bidirectional LSTM to model long-range dependencies across the document. A lightweight scoring head assigns per-sentence importance scores and is trained end-to-end with binary cross-entropy against oracle extractive labels. At inference, a dynamic mean-plus-standard-deviation threshold with a top-3 fallback selects sentences directly from the source and chronologically reorders them into the final summary. Since every output sentence is copied from the input, the model avoids generation-induced factual drift. On PubMed, our architecture outperforms isolated CNN and LSTM baselines, while ablations show that wider convolutional receptive fields improve sentence scoring. On MIMIC-CXR and MIMIC-IV BHC, the model performs well on unstructured narratives but defaults toward positional baselines on highly templated reports. These results suggest that structural constraints can provide a reliable path toward factually grounded summarization systems that are trustworthy by design rather than by correction.

---


### 46. [Generative AI and Extended Reality in Collaborative Architectural Design Education: An Exploratory Studio Study](https://arxiv.org/abs/2609.13494)

**<font color=#1a73e8>作者：</font>** Yao Xiao, Max Chen, Yichen Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Architectural design education relies heavily on visual ideation and representation to support collaborative learning in studio environments. Recent advances in generative artificial intelligence (GenAI) and extended reality (XR) offer new opportunities for rapid idea exploration and immersive spatial visualization. This exploratory mixed-methods classroom study investigated how GenAI-assisted multi-user XR influenced collaborative architectural conceptual design. We developed GenARch, a pipeline that integrates GenAI-based visual generation with collaborative XR environments, and deployed it in an undergraduate architectural design studio. Twenty-seven students formed seven self-selected design teams; four teams incorporated GenARch into their usual course workflow to support collaborative ideation and visualization, while three teams continued the same course workflow without GenARch. Pre- and post-intervention surveys assessed design self-efficacy, attitudes toward collaborative learning, and teamwork; a seven-member panel evaluated team design presentations; and GenARch teams participated in group interviews. The quantitative results showed larger relative declines in confidence and outcome expectancy for the GenARch condition and a positive difference-in-differences estimate for perceived conflict management, while panel-rated presentation outcomes were not significantly different between conditions. Interviews indicated complementary roles for the technologies: GenAI supported idea externalization and visual reference generation, whereas XR supported spatial, contextual, and scale-based evaluation. Students also reported challenges related to control, dimensional fidelity, shared attention, and motion comfort. These findings highlight both opportunities and limitations when GenAI and XR are incorporated into collaborative design education.

---


### 47. [A Three-Axis Stress Test of LLM vs Classical ML for Network Intrusion Detection under Distribution Shift and Adversarial Evasion](https://arxiv.org/abs/2609.13511)

**<font color=#1a73e8>作者：</font>** Muhammad Ebad Atif, Muhammad Haider Ali  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly benchmarked against classical machine learning for network intrusion detection (NIDS), almost always using same-dataset evaluation, and that protocol turns out to be incomplete. Evaluating XGBoost and RoBERTa-LoRA on two independently collected NetFlow v2 networks across three axes (same-dataset performance, cross-dataset transfer, and adversarial evasion) reveals no universal winner. The two models are statistically tied same-dataset. XGBoost wins decisively under cross-dataset distribution shift, by 15 points of F1 and 25 points of balanced accuracy; on the target network RoBERTa-LoRA's false positive rate reaches 0.78, leaving it barely above chance despite a superficially moderate F1. RoBERTa-LoRA wins decisively under adversarial evasion, by roughly 17 points of F1 at a representative mid-range perturbation strength, while both models hold false positive rates below 0.01 throughout. The model an evaluator would recommend therefore depends entirely on which axis is tested, not on same-dataset accuracy alone. A staged feature-leakage ablation improves cross-dataset transfer non-monotonically, indicating the leakage signal is distributed across the feature representation rather than confined to a few columns, and cross-dataset transfer between our two networks is strongly directional. These results argue for evaluating NIDS models along multiple independent robustness axes, and with more than one metric per axis.

---


### 48. [Adaptive Phase-Switching for Communication-Efficient Federated LoRA Fine-Tuning](https://arxiv.org/abs/2609.13512)

**<font color=#1a73e8>作者：</font>** Jerry Adams Franklin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated fine-tuning of large language models with low-rank adaptation reduces per-client trainable parameters, but client-to-server communication remains the dominant cost. Existing accounting for federated LoRA protocols omits the asymmetric transition round when a protocol changes aggregation mode, and reports savings that ignore grouped-query attention shapes. This paper measures per-round upload and download bytes for a bidirectional B-only federated LoRA protocol and places five methods, three from prior work, on a single communication-quality frontier. The frontier has a knee, which an adaptive phase-switching aggregator, ReverseAdaptive, locates by monitoring the relative improvement in global training loss against a dimensionless threshold rather than by fixing a phase boundary in advance. On TinyLlama-1.1B-Chat with Alpaca, ReverseAdaptive attains 40.5 percent measured round-trip savings over FLoRA at a held-out instruction-following loss cost of 0.0063. It outperforms FFA-LoRA, which freezes the first of the two LoRA factors at initialization, by 0.0182 in held-out loss, more than twenty times the largest per-method seed standard deviation on that metric, so learning that factor before freezing it produces better adapters. The same threshold transfers across model scales without retuning, and the quality cost of the transition is stable across the two datasets tested.

---


### 49. [From Token Probabilities to Semantic Constraints: Towards Declarative Probabilistic Evaluation of Language Models](https://arxiv.org/abs/2609.13520)

**<font color=#1a73e8>作者：</font>** Kyle Richardson, Cullen Anderson, Pranav Balakrishnan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Large Language Models have improved rapidly, many fundamental questions remain about how to evaluate the knowledge and reasoning abilities they acquire, and how such evaluations relate to the learning signals used in pre-training. In this paper, we propose ModelLog, a declarative probabilistic framework for pre-training evaluation that makes the semantic structure of model behavior explicit and provides new formal tools for relating evaluation to learning. ModelLog specifies evaluation targets as symbolic constraints over token-level predictions and measures how strongly a model's distribution satisfies those constraints. We explore the framework through a new suite of tasks targeting negation, mutual exclusivity, and consistency, finding systematic failures that are difficult to characterize through token likelihood or answer accuracy alone. We further show that these evaluation scores can also be interpreted as losses, whose gradients reflect logical strength, informativeness, and variable-level sensitivity. This links evaluation and learning through a shared semantics, suggesting evaluation methods that diagnose model behavior while also helping to clarify the semantic structure of learning.

---


### 50. [Generative Interpretability via Scalable Neuro-Symbolic Models](https://arxiv.org/abs/2609.13529)

**<font color=#1a73e8>作者：</font>** Xiaocong Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As the use of Large Language Models moves from chatbots into agentic systems, where outputs become actions with irreversible consequences on reality, the existing paradigm on AI Interpretability research, post-hoc interpretability, is structurally inadequate for safe and trustworthy model deployment: it explains behavior after the fact but cannot audit or intervene in an inference computation before it commits to an output. We therefore argue for a shift toward \emph{generative interpretability}, an architectural property under which a model's inference pass natively exposes semantically meaningful checkpoints that are human-understandable and amenable to causal intervention. We show the merits of generative interpretability as comparison to other interpretability research paradigms, and propose Neuro-Symbolic Models as a concrete instantiation.

---


> [!TIP]
> 当前位于：**1-50**（第 1/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-368](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
