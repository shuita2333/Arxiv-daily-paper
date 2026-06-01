# 🧠 大模型相关研究 | 2026年06月02日

> 本类共 **168** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-168](./part-04.md)

---

### 1. [QASM-Eval: A Dataset to Train and Evaluate LLMs on OpenQASM-3 Beyond Quantum Circuits](https://arxiv.org/abs/2605.30358)

**<font color=#1a73e8>作者：</font>** Zhenxiao Fu, Lei Jiang, Fan Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantum computing remains in the Noisy Intermediate-Scale Quantum (NISQ) era, where the performance is highly constrained to noise. Addressing the limitation often requires hardware-facing capabilities beyond gate-sequence circuit specification, including mid-circuit measurement and classical feedback for quantum error correction (QEC), precise timing control for dynamical decoupling (DD), and pulse-level waveform access for calibration. OpenQASM-3 was introduced to expose exactly these capabilities, providing a hardware-level programming interface. However, despite the rapid progress of large language models in code generation, there is still no dataset specifically designed to train and evaluate LLMs on OpenQASM-3 programs that involve its advanced hardware-oriented features. To address this gap, we introduce QASM-Eval, the first comprehensive dataset designed to train and evaluate LLMs on OpenQASM-3. Rather than focusing on quantum algorithm design or reasoning, QASM-Eval explicitly targets the language's hardware-facing features. QASM-Eval comprises an expert-verified test set of 100 tasks and a training set of 4,000 tasks, systematically covering classical logic, timing scheduling, pulse control, and complex real-world workflows. To automatically validate generated programs, we check syntax, quantum states and program timeline using an extended verifier. Our evaluation reveals that while state-of-the-art LLMs struggle heavily in OpenQASM-3 coding tasks, targeted fine-tuning on QASM-Eval yields significant gains. QASM-Eval provides a crucial benchmark and training foundation to accelerate the development of reliable LLM assistants for hardware-facing quantum programming in NISQ era. Data and code: this https URL

---


### 2. [When LLMs Learn to Be Consistently Wrong: A Multi-Model Study of Linear Representations of Synthetic Deception](https://arxiv.org/abs/2605.30381)

**<font color=#1a73e8>作者：</font>** Vahideh Zolfaghari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deceptive alignment, in which models maintain accurate internal representations while deliberately producing false outputs, remains a central challenge in AI safety. While strategic deception is the primary long-term concern, synthetic dishonesty - induced via direct optimization on incorrect answers - provides a controlled testbed for studying the representational basis of learned deception. We introduce a multi-model paradigm in which honest and deceptive variants of five transformer models (Pythia-1.4B, Gemma-2-2B/9B, Qwen2.5-7B, Llama-3.1-8B) are fine-tuned using LoRA on the same question distribution. Linear probes trained on mean-pooled hidden states detect synthetic dishonesty with near-perfect AUC (greater than or equal to 0.99) as early as layers 1-3 in four architectures, while Pythia-1.4B reaches a peak of 0.705. Logistic regression probes consistently match or outperform MLP probes, supporting the Linear Representation Hypothesis. Probes trained on TruthfulQA generalize with near-zero loss (Delta AUC approx. 0) to held-out MMLU subjects. Late-layer representations show strong robustness to Gaussian noise, with Gemma-2 models exhibiting exceptional stability. Mechanistic analysis of Fisher Discriminant Ratio, effective rank, centroid geometry, directional stability, cross-domain alignment, and calibration (ECE) reveals two regimes: representational collapse in Pythia/Llama/Qwen versus high-dimensional preservation in Gemma-2. Across all models, the dishonesty direction consolidates progressively in deeper layers, with optimal calibration (ECE less than 0.01 except Pythia) achievable in layers 1-4. These results demonstrate that robust, domain-invariant dishonesty representations can be rapidly entrenched via modest supervised fine-tuning, with implications for activation-based monitoring.

---


### 3. [LLMs Without Deep Neural Networks: New Architecture, Benefits and Case Study](https://arxiv.org/abs/2605.30385)

**<font color=#1a73e8>作者：</font>** Vincent Granville  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The purpose of this article is to provide validation to my deep neural network alternative in the context of LLMs. Very recently, there has been a significant interest by Chinese researchers in a model called RBF network, as a substitute to standard DNNs, with increased explainability and higher accuracy. It turns out that my new model, discovered independently, is based on the exact same machinery. But with a major twist: it does not need DNN as it finds the global optimum of the loss function in closed form, in one iteration, thus eliminating the tedious training step. Here I provide a high-level overview of my technology, with case study and comparison to similar methods.

---


### 4. [Social Reasoning in Machines: Investigating Collective Truth-Seeking Dynamics in Large Language Model Debate](https://arxiv.org/abs/2605.30391)

**<font color=#1a73e8>作者：</font>** Tom Pecher  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Human reasoning has long been theorised to operate socially, not through isolated individual cognition, but through collective adversarial discourse, a framework known as the Argumentative Theory of Reasoning (ATR). Rather than relying on individual "intellectualist reasoners" as the primary vehicle for truth-seeking, ATR reconceptualises truth as an emergent property of social epistemology: the product of imperfect individual reasoning refined under the adversarial pressure of debate. This distributed method of collective intelligence has guided humanity to ever-greater epistemic heights and underpins the foundational principles of all democratic systems. This thesis breaks new ground by, for the first time, simulating ATR through the multi-agent debate (MAD) of large language models (LLMs). With rigorous empirical analysis, we demonstrate that, when correctly engineering an epistemically diverse set of models, LLM-MAD can significantly improve truth-seeking performance on questionnaire-based tasks, even when individual debate participants exhibit limited standalone performance. Furthermore, we present strong empirical evidence that this performance gain is mechanistically grounded in the central principles of ATR, suggesting that collective reasoning may be universally favourable over individualist reasoning, rather than a quirk in biology or evolution. Finally, drawing on our analysis of debate dynamics, we propose a novel benchmarking methodology that leverages LLM-MAD to measure intrinsic model properties (such as hallucination propensity) in order to compare models in ways that current static benchmarking approaches cannot support.

---


### 5. [NumLeak: Public Numeric Benchmarks as Latent Labels in Foundation Models](https://arxiv.org/abs/2605.30393)

**<font color=#1a73e8>作者：</font>** Anany Kotawala  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Public numeric benchmarks appear in pretraining, so an evaluation that conditions on a date may be measuring memorized recall rather than out-of-sample skill. We introduce NumLeak, a measurement framework that combines API-boundary probes on production models with a white-box controlled validation on an open causal LM. Top-tier frontier LLMs recall the Fama-French market excess return at 3-seed pooled Pearson r=0.97-0.99 while staying within 0.15 within-25bps on the five sibling factors; comparable fidelity appears on U.S. unemployment, CPI inflation, and NOAA temperature. On a recent-release holdout, parse rate collapses to 21-57% but r stays at approximately 0.99 on months answered, the refuse-or-recall asymmetry a memorized channel predicts. The white-box experiment reproduces the dose-response, and logprob ranking detects memorization that open-ended generation misses, implying closed-API black-box probes understate the channel. A Sonnet "date to market-sentiment" regression that correlates with true Mkt-RF at r=0.74 collapses to r=0.02 once the model's own recall is residualized out. A one-line system-prompt defense blocks 99.8% of a non-adaptive single-turn suffix attack set at near-zero utility cost on conceptual and historical-narrative queries

---


### 6. [Protocol for evaluating ChatGPT in biomedical association generation and verification using a RAG-enabled, cross-model majority voting workflow](https://arxiv.org/abs/2605.30400)

**<font color=#1a73e8>作者：</font>** Ahmed Abdeen Hamed, Luis M. Rocha  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a protocol to evaluate ChatGPT's ability to generate disease-centric biomedical associations. It outlines how we generate the associations, validate the biological entities using biomedical ontologies, and verify associations using literature. The protocol includes a self-consistency strategy to assess generative reliability across ChatGPT models. To address ontology exact-match limitations, we provide a use case performing semantic verification through a workflow enabled by Retrieval-Augmented Generation (RAG) powered by open-source large language models (LLMs). This enables LLMs to establish truth over content generated by other LLMs and expose hallucination.

---


### 7. [Exploring Autonomous Agentic Data Engineering for Model Specialization](https://arxiv.org/abs/2605.30407)

**<font color=#1a73e8>作者：</font>** Yujie Luo, Xiangyuan Ru, Jingsheng Zheng 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have demonstrated strong performance on general tasks, while often struggling to adapt to specialized domains without high-quality domain-specific data. Existing LLM-based data curation methods primarily rely on human-designed workflows, leaving it unexamined whether LLMs can autonomously execute an end-to-end data engineering pipeline for model specialization. We formalize \textbf{Autonomous Agentic Data Engineering}, a novel task designed to evaluate LLMs as autonomous data engineers that drive model specialization through end-to-end data curation. We frame data as an optimizable component and study agents that plan, generate, and iteratively optimize training data across multiple domains, guided by post-training performance improvement. Experiments show that autonomous LLM data engineers yield substantial gains, as GPT-5.2 constructs a training curriculum that improves a student model by \textbf{57.29\%}, entirely through iterative, agent-driven data adaptation. By illuminating both potential and bottlenecks, our study establishes autonomous data engineering as a measurable capability and charts a path toward agent-driven model specialization\footnote{Code will be released at this https URL.}.

---


### 8. [Domain Adaptation and Reasoning Frameworks in Language Models: A Controlled Experiment with Historical Cosmology](https://arxiv.org/abs/2605.30415)

**<font color=#1a73e8>作者：</font>** Francesco De Bernardis  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate how domain adaptation reshapes explanatory behavior in language models using historical cosmology as a controlled setting. In Phase 1, we train a small language model from scratch on a pre-Copernican corpus from which explicit heliocentric references were removed, and evaluate whether Earth-motion or heliocentric continuations nevertheless emerge. In Phase 2, we fine-tune a larger pretrained model using QLoRA on the same corpus in order to study how adaptation modifies explanatory framing and cosmological stance. Model outputs are evaluated using an LLM-as-judge framework that labels both cosmological stance (geocentric, heliocentric, or ambiguous) and explanatory frame (premodern versus modern). In the constrained setting of Phase 1, the smaller models occasionally generate local Earth-motion continuations, but these remain globally unstable and insufficient to support coherent cosmological reasoning. In Phase 2, fine-tuning induces a large and statistically significant shift toward premodern explanatory framing, while the conditional cosmological stance distributions remain comparatively stable within those frames. As a result, increases in geocentric outputs arise primarily from redistribution over explanatory regimes rather than from direct modification of stance. These results suggest that domain adaptation may primarily reshape the linguistic frameworks from which continuations are generated, with changes in stance emerging secondarily from those shifts.

---


### 9. [LongDS-Bench: On the Failure of Long-Horizon Agentic Data Analysis](https://arxiv.org/abs/2605.30434)

**<font color=#1a73e8>作者：</font>** Kewei Xu, Xiaoben Lu, Shuofei Qiao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world data analysis is inherently iterative, yet existing benchmarks mostly evaluate isolated or short interactive tasks, leaving agents' ability to track evolving analytical context over long horizons untested. We introduce LongDS, a benchmark for long-horizon, multi-turn data analysis where agents must maintain, update, restore, and compose evolving analytical states. LongDS comprises 68 tasks constructed from real-world Kaggle notebooks, spanning 2,225 turns across six domains including Geoscience, Business, and Education. Tasks are designed around state-evolution patterns (e.g., counterfactual perturbation, rollback, multi-state composition), with an average dependency span of 11.3 turns. Evaluating five state-of-the-art models, we find that the best model reaches only 48.45% average accuracy, performance drops nearly 47 points from early to late turns, and long-horizon errors account for 52%--69% of failures. Further analysis shows that additional agent steps do not necessarily improve performance, suggesting that the key bottleneck is maintaining a correct analytical state rather than increasing interaction budget. We release LongDS to support research on reliable long-horizon agentic data analysis. Code and data will be released at this https URL.

---


### 10. [Bounded Behavioral Indistinguishability for Black-Box LLM Distillation](https://arxiv.org/abs/2605.30448)

**<font color=#1a73e8>作者：</font>** Munawar Hasan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Black-box LLM distillation is usually evaluated as an output-matching problem: a student is considered successful when its responses are semantically similar to, or task-consistent with, those of a teacher. However, output similarity does not imply that the student is behaviorally indistinguishable from the model it imitates. We introduce bounded behavioral indistinguishability, formalized as $(\epsilon,q,t,\mathbb{A})$-behavioral indistinguishability over an explicit prompt distribution, where $\epsilon$ bounds distinguishing advantage, $q$ bounds oracle queries, $t$ bounds computation, and $\mathbb{A}$ denotes the adversary class.
We instantiate this notion on Qwen and Llama teacher-student pairs using a controlled $5,000$-prompt behavioral probe suite. For each family, we compare the teacher with both the base student and the LoRA-distilled student, measuring whether distillation reduces distinguishability rather than merely improving similarity. LoRA raises semantic similarity from $0.788$ to $0.862$ for Qwen and from $0.814$ to $0.874$ for Llama. Yet adversarial evaluation reveals remaining behavioral differences: learned discriminators retain nonzero advantage, and pairwise category analysis shows artifacts concentrated in style/format, robustness, and domain-technical prompts. A pairwise teacher-identification adversary confirms this trend. With a different-family Llama judge and A/B-swap consistency filtering, Qwen distinguishing advantage drops from $0.158$ for the base student to $0.081$ after LoRA distillation. Query-budget experiments show that disagreement-guided acquisition does not consistently outperform stratified random sampling, indicating that coverage and diversity remain strong baselines. Our results show that semantic fidelity is useful but insufficient: black-box LLM distillation requires bounded, adversarial, and category-aware evaluation.

---


### 11. [Can LLM Teams Play What? Where? When?](https://arxiv.org/abs/2605.30459)

**<font color=#1a73e8>作者：</font>** Anastasia Kotelnikova, Viktor Byzov, Maria Dolzhenkova 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) remain limited on tasks requiring indirect reasoning, cultural knowledge, and coordinated hypothesis testing. We investigate whether team-based interaction improves LLM performance in What? Where? When? (ChGK), a quiz game designed to reward collective reasoning. We introduce three team strategies: Voting, Silent Team (the captain observes final answers), and Talkative Team (the captain observes both answers and rationales). To minimize data leakage, we evaluate these strategies on a dataset consisting of 572 ChGK questions released in 2025. Using six recent large-scale open models, we show that team-based strategies outperform single-model baselines, yielding gains of up to 20 percentage points in accuracy. The best team achieves 44.23% accuracy, and approaches human team performance on questions with available human statistics. Analysis of inter-model diversity reveals that disagreement strongly predicts lower accuracy, but explanatory communication substantially mitigates performance drops. We further examine captain behavior and find no evidence of self-preference bias; access to peer rationales improves captain judgments. Overall, LLM teams function primarily as answer selection and error-filtering mechanisms rather than generators of novel solutions. Our findings highlight the importance of interaction and suggest adaptive strategies as a promising direction for multi-agent systems.

---


### 12. [Clustering Guided Domain-Specific Pretrained Foundation Model Very High-Resolution Arctic Remote Sensing](https://arxiv.org/abs/2605.30467)

**<font color=#1a73e8>作者：</font>** Amal S. Perera, Chandi Witharana, Elias Manos 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This study introduces a novel Arctic-focused remote sensing foundation model (RSFM) by combining diversity-aware regional-scale image curation with masked autoencoder (MAE) self-supervised pretraining of a Vision Transformer (ViT) encoder for very-high-spatial-resolution (VHSR) satellite image analysis. Spectral and acquisition-metadata descriptors were used in a scalable affinity-propagation clustering workflow to select approximately 3 million chips from 267 TB of Vantor VHSR imagery This curation strategy was designed to reduce oversampling of visually repetitive or low-information areas while preserving broad scene diversity across the study domain. We pretrained a ViT-Large encoder on the curated corpus using a domain-adapted MAE reconstruction objective, producing Arctic-specific transformer weights for downstream feature mapping. The pretrained encoder was integrated into an existing location-aware detection and segmentation framework and evaluated across four hand-labeled Arctic datasets. Compared to ImageNet-initialized ViT-Large baseline, Arctic MAE pretraining produced consistent improvements in foreground mean F1 scores of 0.87, 0.72, 0.93, and 0.87, for infrastructure, IWP, RTS, and TCNs, with approximately 5-8 percentage increase. The proposed model also outperformed Prithvi-EO-2.0 in all downstream comparisons, with the smallest gain corresponding to at least a 15 percentage improvement mean F1, suggesting that domain-specific self-supervised pretraining on curated Arctic VHSR imagery provides more transferable representations for fine-scale Arctic mapping than a general-purpose Earth observation foundation model. These results demonstrate that optimizing the pretraining data distribution at regional scale, while keeping the architecture and MAE objective fixed, can produce a reusable Arctic-domain encoder for multiple VHSR remote sensing applications.

---


### 13. [Your Multimodal Speech Model Says I Have a Face for Radio](https://arxiv.org/abs/2605.30472)

**<font color=#1a73e8>作者：</font>** Maya K. Nachesa, Vlad Niculae, Vagrant Gautam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large neural models have become better at language tasks, researchers are increasingly building multi- and omnimodal models that handle more modalities of data. One example is the expansion of speech recognition models to audio-visual data for noise mitigation and multimodal subtitling. While performance and bias have been studied extensively in the single-modality regime, it is unknown how new modalities affect this, even though they produce biases in humans. We therefore propose the first bias evaluation of multimodal speech recognition, where we create videos pairing different faces with the same audio, and measure changes in speech transcription accuracy. We find large quality-of-service differences across mWhisper-Flamingo and Gemini models, with drops of up to 4.05 word error rate points, across self-declared gender, ethnicity, and their intersection. Our findings point to a priority for developers to evaluate, fix, and communicate such limitations, as providing more signals through additional modalities is not necessarily better, and may even lead to biased outcomes.

---


### 14. [When English Rewrites Local Knowledge: Global Narrative Dominance in Large Language Models](https://arxiv.org/abs/2605.30481)

**<font color=#1a73e8>作者：</font>** Md Arid Hasan, Ruwad Naswan, Farhan Samir 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are widely used as cross-lingual knowledge interfaces. However, culturally grounded questions often reflect globally dominant narratives rather than local contexts. We study this failure mode as \textit{global narrative dominance} in Bangla, a low-resource cultural context. We introduce \texttt{CulturalNB}, a dataset of 717 manually curated Bengali cultural instances with parallel Bangla--English question--answer pairs and supporting evidence, metadata, and sociocultural annotations. Using question-only and evidence-based prompting, we evaluate nine state-of-the-art LLMs with human and two independent LLM judges across metrics for cross-lingual consistency, language anchoring, global substitution, institutional bias, and epistemic perspective coverage. Results show that questions asked in English systematically increase global substitution and institutional framing while reducing local perspective coverage. Local evidence improves factual consistency and perspective coverage, but does not eliminate language-induced epistemic shifts. These findings suggest that cultural failures in LLMs are not only missing-knowledge errors but also failures of grounding and narrative prioritization.

---


### 15. [Configurable Reward Model for Balanced Safety Alignment](https://arxiv.org/abs/2605.30487)

**<font color=#1a73e8>作者：</font>** Zhengping Jiang, Mehran Khodabandeh, Akash Bharadwaj 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aligning large language models (LLMs) to heterogeneous and rapidly evolving safety requirements remains a critical challenge. Existing instruction-tuned LLMs and standalone safety classifiers often fail to generalize to new safety configurations, motivating the need for Reward Models (RMs) that are explicitly configurable to changing specifications. We introduce the Configurable Safety Reward Model (CSRM), which is jointly optimized for calibrated safety compliance and reward modeling. Our approach is supported by configuration-targeted data augmentation that enforces instruction adherence while preserving relative severity structure. The resulting RM is sensitive to fine-grained safety configurations and conversational nuances, substantially improving generalization to previously unseen safety configurations. CSRM achieves state-of-the-art performance on recent configurable safety benchmarks, including CoSApien (94.6% F1) and DynaBench (75.8% F1), without requiring additional human annotation. When used for downstream safety alignment, CSRM yields LLMs with a significantly improved helpfulness-safety tradeoff compared to existing baselines.

---


### 16. [CanLegalRAGBench: Evaluating Retrieval-Augmented Generation on Canadian Case Law](https://arxiv.org/abs/2605.30497)

**<font color=#1a73e8>作者：</font>** Ethan Zhao, Maksym Taranukhin, Wei Cui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> RAG-based legal assistants have been growing in popularity, but LLM hallucinations remain a key issue and potentially undermines justice. While benchmarks have been developed to evaluate progress, many rely on synthetic queries rather than realistic legal scenarios. Moreover, Canadian law remains underrepresented in existing evaluations. To address this gap, we introduce CanLegalRAGBench, a Canadian legal QA benchmark based on realistic queries and expert-annotated answers grounded in case law. Our evaluation shows that retrieval performance is sensitive to design choices and that open-source embedding models are competitive with closed source models. However, it also reveals the limitation of automatic evaluations that penalize systems for retrieving alternative relevant documents. We also find that generated answers often diverge from gold responses, either with hallucinations or by producing overly detailed or irrelevant content, with 8-29% of claims not being supported by the retrieved documents. We hope this benchmark will help drive continued progress in addressing limitations of legal RAG systems.

---


### 17. [Linear Ensembles Wash Away Watermarks: On the Fragility of Distributional Perturbations in LLMs](https://arxiv.org/abs/2605.30501)

**<font color=#1a73e8>作者：</font>** Zhihao Wu, Gracia Gong, Qinglin Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Watermarking embeds statistical signatures in AI-generated text for detection and attribution. We reveal a fundamental vulnerability: when users access multiple models (today's reality), watermarks trivially fail. Watermarks perturb output distributions away from the original, and in competitive markets, these perturbations are typically independent across providers. We theoretically prove that averaging output probability distributions recovers the unwatermarked distribution with up to a second-order error term. Empirically, simply averaging 3-5 models cancels out these perturbations. We introduce WASH (Watermark Attenuation via Statistical Hybridisation), which solves practical challenges in ensemble generation: vocabulary misalignment and tokenisation differences across heterogeneous models. Experiments across six watermarking schemes and three LLMs show that averaging across 3 models suppresses detection z-scores from 5-300 to below 2 (below the detection threshold of 4) and reduces TPR at 5% FPR to below 50%, while improving quality by 27.5% and running 6 times faster than the best baseline on the long sequence generation. Our results suggest that robust AI-text detection via watermarking requires either accepting this fundamental vulnerability or unprecedented coordination among model providers.

---


### 18. [Auditing LLM Benchmarks with Item Response Theory](https://arxiv.org/abs/2605.30504)

**<font color=#1a73e8>作者：</font>** Sander Land, Daniel M. Bikel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM benchmark labels are frozen at release and silently propagated into downstream benchmarks, errors and all. We introduce an Item Response Theory-based indicator that surfaces likely mislabels at 95% precision in the top 200 examples across seven preference and multiple-choice benchmarks using responses from 114 models, outperforming a supervised classifier. We trace these errors to mechanical labeling heuristics, upstream annotation mistakes inherited unchanged from source datasets, and fundamentally ambiguous items without a defensible single label. The same model fit reveals that reward models specialize in stylistic preference rather than factual knowledge, and identifies one frontier reward model that agrees with detected mislabels at 78% accuracy versus 38% for its peers, consistent with benchmark contamination or benchmark-specific over-optimization.

---


### 19. [PhyDrawGen: Physically Grounded Diagram Generation from Natural Language](https://arxiv.org/abs/2605.30512)

**<font color=#1a73e8>作者：</font>** Nafiul Haque, Syed Nazmus Sakib, Shifat E Arman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generating physics diagrams from text requires strict adherence to physical laws. While current generative models produce visually plausible outputs, they systematically hallucinate force vectors, ignore conservation laws, and violate geometric constraints. We present PhyDrawGen, a neuro-symbolic pipeline that decouples semantic scene understanding from physical constraint satisfaction. First, a large language model extracts a typed scene graph from the problem text. A deterministic solver then converts this graph into a Planar Straight-Line Graph (PSLG), encoding force balance, optical paths, and field topologies as exact geometric primitives. Finally, a fine-tuned Qwen-VL model implements a visually grounded propose-verify loop to iteratively correct any constraint violations. Evaluated on a benchmark of 1,449 problems spanning mechanics, optics, and electromagnetism, PhyDrawGen significantly outperforms GPT-5-image, Gemini 2.5 Flash, and Gemini 3 Pro, demonstrating robust physical accuracy even on unusual-object problems.

---


### 20. [Evaluating using Mock Tool Calls to Quarantine Untrusted Prompt Inputs](https://arxiv.org/abs/2605.30521)

**<font color=#1a73e8>作者：</font>** David Gros, Adam Gleave  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models must frequently process untrusted inputs, such as judging an answer from another model or running tasks like spam and harm classifiers while under adversarial pressure. These inputs are often string-formatted directly into a prompt template, leaving systems fragile to manipulation. Current LLM specs from major providers like OpenAI distinguish trustworthiness along an Instruction Hierarchy, from System messages (most trusted) to Tool Results (least trusted). A possible natural mitigation is to wrap untrusted content in a mock tool call as a quarantine. We explore this hypothesis with an automated redteaming search over static attack strings across seven models and three LLM-as-a-Judge tasks. Counter to our hypothesis, tool-wrapping does not broadly improve robustness. On a binary evaluation task (GSM8K grading) it typically increases attack success rates, an apparent inversion of the instruction hierarchy. On scalar and pairwise tasks the effect is smaller and model-dependent, with no tested model reliably helped, and several showing inversion. We recommend evaluating this limitation in deployed systems, and longer-term, pursuing stronger Instruction Hierarchy training or new untrusted-input primitives.

---


### 21. [Representation Collapse in Sequential Post-Training of Large Language Models](https://arxiv.org/abs/2605.30524)

**<font color=#1a73e8>作者：</font>** Yichen Liu, Mingyu Chen, Hao Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models are now adapted through chains of post-training stages rather than through a single instruction-tuning pass. This paper studies whether such sequential post-training gradually compresses internal representations into low-rank, anisotropic, and homogeneous feature spaces. We define a measurement suite for hidden states, logits, token trajectories, and LoRA updates, and we use it to analyze supervised fine-tuning, preference optimization, safety/refusal tuning, math and code specialization, and long chain-of-thought tuning under controlled stage orderings. The central hypothesis is that excessive representation concentration is not merely a geometric curiosity: it predicts reduced plasticity during later adaptation, weaker out-of-domain generalization, and poorer calibration. We further evaluate lightweight interventions, including mixed-domain replay, feature refresh, representation diversity regularization, and LoRA update decorrelation, as ways to preserve future learnability without giving up the behavioral gains of post-training.

---


### 22. [Measuring, Localizing, and Ablating Alignment Signatures in LLMs](https://arxiv.org/abs/2605.30526)

**<font color=#1a73e8>作者：</font>** Aniket Anand, Janvijay Singh, Zhewei Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Aligned language models often exhibit a recognizable AI-like style, yet its connection to post-training and internal representations remains poorly understood. In this work, we study whether post-training introduces or amplifies AI-like stylistic regularities and whether these regularities have a localized internal signature. To this end, we compare human text, base-model generations, and aligned-model generations under matched human-source prefixes. Aligned generations show lower human-corpus affinity and higher AI-detection rates than base generations, suggesting that post-training shifts generated text away from human-corpus style and toward detector-visible AI-like text. We then introduce PASTA (Post-training Alignment Signature Targeted Ablation), a training-free method that estimates a post-training alignment signature from aligned-base residual contrasts and ablates the corresponding direction during decoding. Across 11 aligned models and 6 AI detectors, PASTA lowers the detection rate for most aligned models; this effect transfers well across detectors and is not reproduced by random directions. Qualitative analysis suggests that PASTA generations remain relevant and coherent while exhibiting greater stylistic variation. Together, these results show that AI-like stylistic effects of post-training can be measured, localized, and causally tested through activation ablation.

---


### 23. [The Long-Term Effects of Data Selection in LLM Fine-Tuning](https://arxiv.org/abs/2605.30537)

**<font color=#1a73e8>作者：</font>** Yuxin Yang, Aoxiong Zeng, Xiangquan Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data selection is increasingly used to reduce the cost of large language model (LLM) fine-tuning, with recent methods prioritizing samples by current utility, diversity, quality, or influence. This paper studies a different question: when fine-tuning occurs over multiple stages, can selection strategies that look optimal now make the model less adaptable later? We introduce a long-horizon view of LLM data selection in which a selector is evaluated not only by immediate task performance, but also by future adaptation speed, forgetting, capability imbalance, and out-of-distribution robustness. We compare representative random, loss-based, gradient-based, diversity-based, quality-based, and utility-diversity selection families under a unified multi-stage protocol. Through controlled experiments designed to instantiate this protocol, we show how short-term selectors can exhibit rank reversal: they improve the current stage while slowing subsequent learning and increasing forgetting. We formalize this behavior as \emph{myopic selection}, provide a simple local analysis of why it can occur, and propose a diagnostic Long-Horizon Aware Selection (LHAS) objective that augments immediate utility with coverage, future-proxy transfer, and anti-concentration terms. The study argues that data selection should be evaluated as a training intervention that shapes the model's learning trajectory, rather than only as a local data-efficiency mechanism.

---


### 24. [A Theory-Guided LLM Pedagogical Agent for STEM+C Scaffolding Without Over-Reliance](https://arxiv.org/abs/2605.30539)

**<font color=#1a73e8>作者：</font>** Clayton Cohn, Surya Rayala, Siyuan Guo 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> LLM pedagogical agents are proliferating, yet recent findings have raised questions about their adherence to established theories of learning and, by extension, their educational value. Concerns regarding cognitive offloading, over-reliance, and "gaming" behaviors persist and remain largely unaddressed. In response, we developed Copa, an agentic, multi-agent, multimodal Collaborative Peer Agent for STEM+C learning. Copa is built on top of the Evidence-Decision-Feedback (EDF) framework, grounding its interactions in Social Cognitive Theory and Social Constructivism and promoting sense-making through adaptive, dialogic support rather than answer-seeking. In an authentic high school computational-modeling study (n=33 dyads), we demonstrate that Copa (1) supports students' confidence building and ability to verbalize conceptual understanding without causing dependence; and (2) provides adaptive feedback personalized to learners that is interpretable with respect to students' multimodal input data. These findings position theory-guided, multimodal LLM agents as a promising path toward classroom AI integration that amplifies students' reasoning rather than replacing it.

---


### 25. [Physically Viable World Models: A Case for Query-Conditioned Embodied AI](https://arxiv.org/abs/2605.30542)

**<font color=#1a73e8>作者：</font>** Adam J. Thorpe, Stepan Tretiakov, Cheng-Hsi Hsiao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models for embodied AI must be physically viable: constructed to answer intervention queries by representing the physical structure governing action outcomes, rather than merely predicting future observations. Existing observation-predictive world models can produce visually plausible but physically wrong rollouts. This failure is structural; distinct physical systems can look identical yet diverge under intervention. We expose this problem with controlled benchmarks that fix the visible scene while varying latent physics. We show that such models may recommend infeasible actions, mispredict interaction outcomes, or certify unsafe behavior. We argue that embodied AI requires world models that identify the simplest physical abstraction sufficient to answer an intervention query. Such a model comprises modular components, including environment representation, latent state and parameter estimation, action specification, interventional dynamics, and query-level response. An autonomous orchestrator should identify the relevant abstraction and compose compatible learned and structured components per query. When closed-form physics is unavailable, uncertain, or costly, the transition model may be analytic, simulated, learned, or hybrid, but it must preserve the structure that determines interventional outcomes. This decomposition makes the model interpretable, its components verifiable, and its outputs auditable against the query. It also provides a design principle for new world models and a feasibility test for existing ones: the right abstraction is not the most detailed model of the world, but the simplest model that preserves the distinctions relevant to the query. We demonstrate this approach on queries that existing systems fail to answer correctly, and outline how an orchestrator can dynamically assemble and adapt physically viable models for planning, control, and verification.

---


### 26. [Supervised Training Rapidly Degrades Early Visual Cortex Alignment Across Biologically Plausible Learning Rules](https://arxiv.org/abs/2605.30556)

**<font color=#1a73e8>作者：</font>** Nils Leutenegger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Random, untrained neural networks consistently match or exceed trained networks in representational similarity to early visual cortex. This puzzling finding challenges the assumption that learning improves brain alignment. We investigate it by tracking representational similarity analysis (RSA) alignment to human fMRI data across training for four learning rules: backpropagation (BP), feedback alignment (FA), predictive coding (PC), and spike-timing-dependent plasticity (STDP). Using 720 object images from the THINGS database and fMRI data from three subjects across six visual ROIs, we measure Spearman correlations between model and brain representational dissimilarity matrices at eight training checkpoints (epochs 0-40). We find that (1) a single epoch of training reduces V1 alignment by 25-90%, depending on the learning rule; (2) backpropagation reduces V1 alignment most severely (delta r = -0.080), while predictive coding and STDP preserve substantially more (delta r ~ -0.04); and (3) a weaker, opposite tendency appears in object-selective cortex (LOC), where BP shows the largest increase in alignment during training, although the absolute change is small. These results suggest that untrained architectures capture low-level visual statistics through inductive biases alone, and that global error signals (BP) reshape early representations more aggressively than local learning rules (PC, STDP), which better preserve brain-like structure.

---


### 27. [VLM3: Vision Language Models Are Native 3D Learners](https://arxiv.org/abs/2605.30561)

**<font color=#1a73e8>作者：</font>** Zhipeng Cai, Zhuang Liu, Yunyang Xiong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Language Models (VLMs) enable a unified model to solve various vision tasks through prompting. They have shown promising performance in semantic understanding. However, 3D understanding still largely relies on expert vision models with complex task-specific designs. The key argument this work wants to make is that VLMs are native 3D learners. Our in-depth large scale study shows that 1) focal length unification, 2) text-based pixel reference and 3) data mixture and scaling, are all you need for effective 3D learning. Model architecture changes, large models, heavy data augmentations, and complex losses including the regression formulation, many of which form the foundation of expert vision models, are actually not necessary conditions. As a result, we propose VLM3, a scalable method with the simplest design that enables standard VLMs to master diverse 3D tasks. VLM3 not only advances the VLM depth estimation accuracy by a large margin (0.84 -> 0.9), but also enables diverse 3D tasks such as pixel correspondence, camera pose estimation and object-level 3D understanding, matching expert vision model accuracy while maintaining standard architectures and text-based training. We believe VLM3 opens up a new paradigm for simple and scalable 3D learning.

---


### 28. [Generating and Refining Dynamic Evaluation Rubrics for LLM-as-a-Judge](https://arxiv.org/abs/2605.30568)

**<font color=#1a73e8>作者：</font>** Zijie Wang, Eduardo Blanco  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-Judge is a scalable alternative to human evaluation, yet existing rubric-based methods rely on human-annotated data such as reference answers or expert-crafted rubrics. We propose to automatically generate fine-grained evaluation rubrics without any human annotation. Our training-free method generates rubrics at dataset-specific and instance-specific granularities, achieving performance competitive with existing methods across four benchmarks. We further present a method that iteratively fine-tunes a rubric generator model via meta-judge reward signals. The fine-tuned generator outperforms all existing baselines in both pairwise and pointwise evaluation. Notably, a fine-tuned 14B rubric generator outperforms a much larger proprietary model at rubric generation, showing the effectiveness of our fine-tuning strategy.

---


### 29. [ReGuLaR: Relation-Grounded Latent Reasoning for Large Vision-Language Models](https://arxiv.org/abs/2605.30587)

**<font color=#1a73e8>作者：</font>** Zihu Wang, Karthik Somayaji N.S, Peng Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) reasoning has significantly improved the reasoning ability of large vision-language models (LVLMs) by verbalizing intermediate reasoning steps in natural language. However, such discrete textual rationales are often insufficient for encoding continuous visual evidence. Recent work addresses this limitation by moving reasoning into continuous latent space. Despite promising progress, existing methods leave latent reasoning insufficiently connected to the compositional and relational structure of visual evidence. To address this gap, we introduce ReGuLaR, a relation grounded latent reasoning framework that explicitly grounds latent states in these critical yet overlooked visual evidence. ReGuLaR uses a training-time ReGFormer to focus latent reasoning on question-relevant objects and inter-object relations, while at inference time the model reasons and generates answers without invoking the ReGFormer. To support training ReGuLaR, we construct RGROUNDING-351K, a real-world vision-language dataset annotated with key object bounding boxes and inter-object relations. Extensive experiments across diverse benchmarks show that ReGuLaR consistently outperforms existing approaches and achieves state-of-the-art performance. We include our code in the submission and will release the code and training data publicly upon acceptance.

---


### 30. [ImmigrationQA: A Source-Grounded Dataset and Small-Model Adaptation for U.S. Immigration Law](https://arxiv.org/abs/2605.30589)

**<font color=#1a73e8>作者：</font>** Nazarii Shportun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> U.S. immigration law spans thousands of pages of official policy, federal regulations, and procedural guidance that change frequently and carry high stakes for petitioners who lack legal representation. We describe the construction of ImmigrationQA, a source-grounded question-answering dataset of 17,058 pairs across 13 immigration subdomains, and the fine-tuning of a Llama 3.2 3B Instruct model on that dataset using parameter-efficient LoRA. The corpus was assembled from 11 primary and secondary sources -- including the USCIS Policy Manual, 8 CFR, BIA precedent decisions, and community Q&A -- yielding 10,056 validated canonical documents and 18,308 text chunks. Structured QA pairs were generated from these chunks using Claude Sonnet 4.6 via five mode-specific prompts, with 22 pairs rejected for insufficient source-span overlap. The fine-tuned model was evaluated against a held-out split of 993 pairs using LLM-as-judge scoring on a 101-example stratified sample. The fine-tuned model scored a mean of 1.08/3.0 (16.8% fully correct; 101-example stratified eval) versus the Llama 3 8B base model at 0.85/3.0 (4% fully correct), a relative improvement of 27% in mean score; a zero-shot Claude Sonnet baseline scored 1.52/3.0 (25% fully correct). The fine-tuned model shows concentrated improvement in procedural subdomains (travel documents, adjustment of status, nonimmigrant visas) while remaining weak on complex legal reasoning and time-sensitive statistics. The full pipeline ran for approximately $29 in cloud compute. All artifacts -- dataset, model, code, and prompt templates -- are publicly released. The system is not a substitute for legal counsel and does not reflect regulatory changes after the corpus crawl date.

---


### 31. [Counterfactual Evaluation Reveals Hidden Capability Profiles in Clinical LLMs and Agents](https://arxiv.org/abs/2605.30590)

**<font color=#1a73e8>作者：</font>** Matt Turk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Two clinical AI systems can score nearly identically on coverage-based rubrics yet behave radically differently when their patient inputs change: one updates its recommendations to match the new clinical signal, while the other produces the same output regardless. We introduce the Causal Sensitivity Score (CSS), a pre-registered interventional metric that mutates oncology tumor-board cases along five clinically meaningful dimensions - biomarker flips, prior-treatment failures, biomarker removals, surgery-status changes, and stage perturbations - and scores whether each model updates its recommendations in the pre-registered correct direction using a {0, 0.5, 1.0} scale. Benchmarked against the Consensus Match Score (CMS), a coverage-based weighted recall metric, six frontier models from three labs evaluated in single-shot inference across 224 cases rank in nearly opposite orders: all six models change rank, the CMS-worst model becomes CSS-best, and one upper-mid CMS model ranks last on CSS. We further surface a universal safety blind spot: every frontier model fails on surgery-status interventions (at most 17.2% CSS on Family D), a finding CMS does not expose. The metric also transfers to tool-using agents: in a ReAct-style experiment, tool use improves CSS for five of six models (+2.5 to +20.3 percentage points), yet the lowest-CSS model retrieves the same chart sections and still fails to update its recommendations - revealing a structural responsiveness deficit visible only under counterfactual evaluation. Cross-judge replication and three-rater medical-professional validation confirm the aggregate findings. Interventional pre-registered metrics like CSS complement coverage-based evaluation for clinical AI agents: they capture responsiveness that coverage metrics miss and offer a candidate dense reward signal for future agentic RL systems.

---


### 32. [Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities in Self-Evolving LLM Agents](https://arxiv.org/abs/2605.30621)

**<font color=#1a73e8>作者：</font>** Minhua Lin, Juncheng Wu, Zijun Wang 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly deployed as systems built around editable external harnesses, including prompts, skills, memories and tools, that shape task execution without changing model parameters. Harness self-evolution adapts such agents by updating these harnesses from execution evidence. Yet it remains unclear whether a model's base capability in task-solving predicts its capabilities in harness self-evolution: which models produce useful harness updates, and which actually benefit from them? We analyze two harness self-evolution capabilities: (i) harness-updating, the capability to produce useful persistent harness updates from execution evidence; (ii) harness-benefit, the capability to benefit from updated harnesses during task solving. Our analysis reveals two findings. First, harness-updating is flat in base capability: models from different capability tiers produce harness updates that lead to surprisingly similar gains; even Qwen3.5-9B's updates yield gains comparable to those of Claude Opus~4.6. Second, harness-benefit is non-monotonic in base capability: weak-tier models benefit little from updated harnesses, mid-tier models benefit most, and strong-tier models benefit less than mid-tier. We trace low gains at the weak tier to two failure modes: weak-tier models may fail to activate relevant harness artifacts, or activate them but fail to follow them faithfully. These findings suggest investing capability budget in the task-solving agent rather than the evolver, and targeting harness invocation and long-horizon instruction following in agent training. Our source code is publicly available at this https URL.

---


### 33. [The Architecture of Errors: From Universal Impossibility to Patch-Local LLM Reliability](https://arxiv.org/abs/2605.30628)

**<font color=#1a73e8>作者：</font>** Mikhail L. Arbuzov, Lee Mosbacker, Sisong Bei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Universal LLM reliability is not a finite-library problem: across all possible tasks, tools, schemas, knowledge sources, and evaluator expectations, new intervention-distinguishable failure modes can appear without bound, so no finite intervention dictionary can guarantee bounded residual error for every such mode. But deployed systems do not operate over the whole universe. They operate inside operationally bounded patches (legal review, medical RAG, code repair, customer-support agents, contract extraction) with recurring tasks, schemas, tools, and evaluator expectations. Within such patches, empirical evidence suggests failures are sparse, repetitive, and concentrated in a small recurring catalogue, so reliability becomes a local catalogue-discovery and intervention-coverage problem rather than an exponential token-length problem. We formalize this transition with two propositions and one corollary. Proposition 1 is the worst-case-mode-wise negative result: no finite intervention dictionary covers every distinguishable failure mode of an unbounded domain. Corollary 1 is the inverse-discovery implication: the logarithmic upper bound on mode discovery cannot accommodate linearly more distinct tail modes without exponentially more observed hard-failure events. Proposition 2 is the positive patch-local result: under log active-mode exposure and head-heavy coverage, a sufficient per-hard-decision intervention budget grows polylogarithmically in sequence length and becomes domain-constant once the patch catalogue saturates. The framework relocates rather than dissolves long-context difficulty: where the number of hard decisions itself grows with task length, reliability remains hard; the contribution is to identify the on-axis intervention rather than to make those regimes easy.

---


### 34. [Rationalize: Shared Semantic Reasoning for Human-AI Alignment](https://arxiv.org/abs/2605.30632)

**<font color=#1a73e8>作者：</font>** Aritra Dasgupta, Naga Datha Saikiran Battula, Avina Nakarmi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We introduce Rationalize, a role-pair framework for shared semantic reasoning between humans and AI models in data-driven sensemaking. Building on ideas in human-machine teaming and critical thinking, we conceptualize human-AI interaction as a series of complementary role pairs (Explorer-Guide, Investigator-Informant, Teacher-Student, Judge-Advocate) operating in a shared reasoning space. In this space, human analysts and AI models (such as LLMs) make purposes, questions, assumptions, evidence, inferences, and implications explicit, facilitating alignment not only at the output level but at the level of rationalization of intent and action by each side. We relate these role pairs to the bidirectional human-AI alignment framework, illustrating how "aligning AI to humans" and "aligning humans to AI" differ by role, and sketch a collaborative research agenda for alignment design and assessment using element-level and role-specific approaches.

---


### 35. [CellBRIDGE: Learning Cellular Trajectories via Interaction-Aware Alignment](https://arxiv.org/abs/2605.30635)

**<font color=#1a73e8>作者：</font>** Silas Ruhrberg Estévez, Nicolas Huynh, Tennison Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inferring dynamics from population snapshots is a fundamental challenge in machine learning and biology. In scRNA-sequencing (scRNA-seq), destructive measurements preclude direct tracking of individual cells across time, making trajectory inference underdetermined. Optimal Transport (OT) provides a principled framework for snapshot alignment, but a long-standing modeling question is which cost functions yield biologically meaningful couplings. Standard OT approaches rely on gene-expression distances, implicitly treating cells as independent points and neglecting structured cell-cell communication mediated by ligand-receptor signaling. We introduce CellBRIDGE (Cell-Based Regularized Interaction-Driven Gene Expression), which augments feature-based OT with a directed, typed interaction cost derived from ligand-receptor activity. By explicitly modeling cell-cell communication, CellBRIDGE improves cross-snapshot couplings and downstream trajectory estimates across synthetic and real scRNA-seq datasets relative to feature-only baselines. Notably, CellBRIDGE enables mechanistically interpretable in silico perturbations: on lung cancer data, silencing specific ligand-receptor pairs induces trajectory shifts that recapitulate expected effects of targeted pathway inhibition.

---


### 36. [EHRBench: An Automated and Reliable EHR-based Benchmark for Clinical Decision Making with LLMs](https://arxiv.org/abs/2605.30637)

**<font color=#1a73e8>作者：</font>** Yuzhang Xie, Keqi Han, Yunpeng Xiao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical decision-making (CDM) is central to real-world clinical workflows, where clinicians infer diagnoses, select treatments, or anticipate future health outcomes under incomplete evidence. LLMs are increasingly used to support these decisions due to strong language capabilities, broad biomedical knowledge, and efficiency, yet the reliability of LLMs on real-world clinical decision tasks remains insufficiently understood. To evaluate CDM models, especially LLM-based models, an ideal and practical medical decision benchmark should be constructed via an automated yet reliable pipeline to ensure both scale and quality. Moreover, the grounding of a CDM benchmark in real patient EHRs can better support evaluation on practical CDM tasks that require substantive biomedical knowledge and clinical inference. To fill the gaps, we introduce EHRBench, an automated and reliable EHR-grounded benchmark for evaluating LLM-based clinical decision-making at scale. To ensure scalability and reliability, EHRBench is constructed through an EHR-LLM-KB(knowledge-base) interaction pipeline. For efficiency, we use a specialized LLM to automatically convert encounter-level EHR trajectories into structured templates and deterministically instantiate the templates into QA items. In parallel, we apply systematic KB-based verification and enrichment to filter hallucinated or ambiguous relations and to improve reliability. Using this pipeline, we construct nearly 1M (960,067) QA items spanning three core inference-required clinical decision tasks: diagnosis, treatment, and prognosis. We benchmark more than 30 representative LLMs on EHRBench and provide detailed analyses of performance and robustness. The results show consistent capability trends across settings, further validating the reliability of EHRBench and highlighting actionable gaps toward clinically reliable LLM systems.

---


### 37. [PInVerify: An Offline Embodied Benchmark for Active Instance Verification](https://arxiv.org/abs/2605.30639)

**<font color=#1a73e8>作者：</font>** Yuhang Jiang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied agents have made strong progress in navigating to target objects, but reaching the goal vicinity does not guarantee that the agent has found the correct instance: subtle attribute differences (e.g., "white floral" vs. "white striped") often require close-range, multi-view inspection. We address this gap with Active Instance Verification (AIV), a task in which an agent actively selects viewpoints around a candidate object to decide whether it matches a fine-grained natural-language description. We formalize AIV as a finite-horizon decision process and introduce PInVerify, an offline embodied benchmark for AIV: 3,000 evaluation episodes across 18 object categories, delivered as multi-view captures with a 6-sector navigation topology that exposes trap views (navigable but uninformative) and unreachable sectors. As reference baselines we build a training-free pipeline and a LoRA-fine-tuned end-to-end agent around open-source multimodal large language models (MLLMs) at on-device scale ($\leq$8B parameters), with attribute decomposition, a visibility-weighted multi-view tracker, and three next-best-view (NBV) strategies. In our evaluation across Qwen3-VL (4B/8B), SenseNova-SI-1.2-InternVL3-8B, CLIP, and SigLIP2, the best MLLM-based baseline exceeds the best embedding baseline by 4.9 pp; GT-box ablations show a +3.1 pp detection gap; and we do not observe reliable gains from active viewpoint selection within the tested NBV strategies. A LoRA-fine-tuned agent (SFT+GSPO) reaches 85.6%. PInVerify aims to support further work on active, fine-grained semantic verification in embodied AI. Code: this https URL.

---


### 38. [COFT: Counterfactual-Conformal Decoding for Fair Chain-of-Thought Reasoning in Large Language Models](https://arxiv.org/abs/2605.30641)

**<font color=#1a73e8>作者：</font>** Arya Fayyazi, Mehdi Kamal, Massoud Pedram  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can reveal and amplify societal biases during chain-of-thought (CoT) generation. We present COFT (Chain of Fair Thought), a training-free decoding method that applies token-level fairness control at decode time, with distribution-free marginal validity guarantees (under exchangeability) for any frozen causal language model. COFT operates in three stages. First, it creates a masked counterfactual prompt by replacing sensitive spans with neutral tokens. Second, it compares the factual and masked logit distributions through lightweight logit fusion to attenuate attribute-driven biases. Third, it uses dual-branch split-conformal calibration to certify per-step candidate token sets at a user-chosen risk level. We evaluate COFT across six models and multiple bias benchmarks. Our method reduces standard bias metrics by 30-55% (median 38%) while preserving task utility and language quality. Reasoning accuracies remain unchanged within run-to-run noise margins. The computational overhead is modest, equivalent to one additional cached forward pass (<=11%). COFT offers a clear, auditable path to safer CoT generation with significant bias reduction, negligible utility loss, and no requirement for retraining, auxiliary classifiers, or weight access.

---


### 39. [Same Patient, Different Words, Different Diagnosis? Evaluating Semantic Stability in Clinical LLMs](https://arxiv.org/abs/2605.30646)

**<font color=#1a73e8>作者：</font>** Mahdi Alkaeed, Adnan Qayyum, Nabeel Abo Kashreef 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used in clinical applications. However, their behavior remains highly sensitive to subtle linguistic variations, such as rephrasing or syntactic variation. This sensitivity poses risks in safety-critical healthcare settings, where semantically equivalent inputs should produce consistent predictions. However, a key challenge is to ensure that prompt variations truly preserve clinical meaning, as embedding-based similarity metrics often fail to capture distinctions involving negation, temporality, or severity. To address this limitation, we propose a semantic verification framework based on Natural Language Inference (NLI) to filter meaning-preserving prompt variations, which are further refined using an LLM-as-a-judge and audited by a clinical expert. In addition, we introduce three metrics to quantify model sensitivity: MeaningPreserving Variation Sensitivity (MVS), confidence variation (\Delta C), and Worst-Case Instability (WCI). We evaluate 16 open-source general-purpose (GP) and medical LLMs within the same model families and parameter scales, using reformulated prompts derived from the DiagnosisQA and MedQA datasets. Our results demonstrate that robustness differences between domain-specific (DS) models are mixed and highly model-dependent, i.e., domain specialization does not consistently improve or reduce robustness to meaning-preserving prompt reformulations. Several DS models rank among the most robust (when compared with GP counterparts), and strong GP baselines remain competitive as well.

---


### 40. [Counterfactual Graph for Multi-Agent LLM Calibration](https://arxiv.org/abs/2605.30653)

**<font color=#1a73e8>作者：</font>** Jiatan Huang, Mingchen Li, Ziming Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems often treat agreement as evidence: when many agents in a panel give the same answer, that answer is assumed to be more reliable. We show that this assumption can fail after agents communicate. Communication can induce correlated failures and false consensus, so the same vote share may reflect reliable agreement in one topology but over-confidence in another. We propose CAGE-CAL, a counterfactual agent-graph calibration framework for multi-agent LLMs. For each query, CAGE-CAL compares an observed post-communication agent graph with a matched counterfactual no-communication graph, capturing both pairwise failure correlations and group-level dependencies. Rather than simply counting how many agents agree, CAGE-CAL estimates the counterfactual shift between observed and no-communication dependence, and calibrates confidence accordingly. Across five benchmarks, CAGE-CAL improves reliability discrimination with competitive ECE, and its calibrated confidence further improves topology selection over the best fixed-topology strategy.

---


### 41. [EUDAIMONIA: Evaluating Undesirable Dynamics in AI](https://arxiv.org/abs/2605.30654)

**<font color=#1a73e8>作者：</font>** Jun Rui Huang, Wang Bill Zhu, Ziyi Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as conversational partners for companionship, emotional disclosure, and interpersonal advice, but the social dynamics of these interactions can create harms that are not captured by capability-oriented or traditional safety evaluations. We introduce the Social AI Design Code, a framework for evaluating whether LLMs align with user welfare in social interactions, including whether they encourage harmful intimacy, dependence, or prolonged engagement. To evaluate these risks in natural and diverse user-LLM interactions, we operationalize the code with EUDAIMONIA, a benchmark of 969 user inputs and 3,147 design-requirement violation checks built from WildChat through weak-to-strong filtration, multi-model relabeling, and controlled rewriting. Evaluating 22 recent LLMs, we find that even the strongest models, Claude-Opus-4.7 and GPT-5.5, violate 30.7% and 27.2% of checks, respectively. Extended thinking does not reduce violation rates, suggesting that these failures are persistent social-alignment problems rather than deficits solvable through test-time reasoning alone.

---


### 42. [TeachObs: A Human-Validated Benchmark for Multimodal Teaching Observation and Model Evaluation](https://arxiv.org/abs/2605.30673)

**<font color=#1a73e8>作者：</font>** Yeil Jeong, Youngjin Yoo, Seobin Sohn 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Classroom videos contain observable teaching practices, but their pedagogical and visual signals are rarely organized in forms suitable for model evaluation. We present \textit{TeachObs}, a human-validated benchmark for multimodal teaching observation in classroom videos. \textit{TeachObs} includes 30 public lesson videos from eight countries divided into 5,158 fixed 15-second scenes. Seven researchers annotated each scene with 39 binary observation codes, covering 20 visual codes, such as gesture, board work, pointing, and visual materials, and 19 nonvisual codes, such as instruction, monitoring, questioning, feedback, and reflection. Gold segment labels are constructed using reliability- and prevalence-aware rules based on Krippendorff's alpha. In addition to segment-level labels, three expert raters produced lesson-level ratings and qualitative evaluations of instructional design, instructional delivery, learner response, learning materials, and lesson closure across the 30 lessons, with rater coverage detailed in the body. Using these two human reference layers, we evaluate five vision-capable frontier LLMs across three tracks - text-only segment coding, text + frame segment coding, and lesson-level coverage scored under an LLM-as-judge protocol - and find that no single model consistently outperforms others across all three tracks, that adding a mid-frame inflates both true and false attributions per scene, and that model evaluations over-rate procedurally clear lessons relative to expert raters. \textit{TeachObs} therefore supports both fine-grained annotation benchmarking and whole-lesson evaluation, showing where AI systems can assist classroom video analysis and where expert judgment remains necessary across varied subjects, classroom formats, and annotation difficulty levels.

---


### 43. [Human-Alignment, Calibration, and Activation Patterns in Large Language Model Uncertainty](https://arxiv.org/abs/2605.30675)

**<font color=#1a73e8>作者：</font>** Kyle Moore, Jesse Roberts, Daryl Watson 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Uncertainty Quantification is a large and growing subfield of large language model behavioral analysis. Primarily to recognize and combat hallucination, the field has largely focused on measuring and improving calibration, the accuracy of uncertainty judgments to task efficacy. In this work, we investigate the relatively underexplored question of how similar large language model uncertainty is to human uncertainty. We investigate the presence and strength of human-similar uncertainty signals, deemed uncertainty alignment, in large language model overt behavior and internal activation patterns. We identify whether the models show evidence of simultaneous alignment and calibration on a variety of datasets covering both multiple choice and open ended factual recall. And we characterize the effect of instruct fine-tuning on each of these facets.

---


### 44. [ElasticMem: Latent Memory as a Learnable Resource for LLM Agents](https://arxiv.org/abs/2605.30690)

**<font color=#1a73e8>作者：</font>** Tao Feng, Chongrui Ye, Tianyang Luo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term memory is essential for LLM agents to reason coherently across extended interactions, personalize responses, and reuse past experience. However, existing memory-augmented methods typically treat memory as a fixed resource: text-space approaches concatenate retrieved memories into the context window, causing substantial token overhead and sensitivity to noisy evidence, while latent-space approaches reduce textual cost but still rely on rigid retrieval or fixed-capacity memory interfaces. This creates a mismatch between query-dependent memory utility and fixed memory allocation. We propose ElasticMem, a memory-augmented LLM framework that learns to use memory as an elastic latent resource. ElasticMem builds an offline latent memory bank with retrieval keys and content caches, retrieves memories adaptively from the reasoner's hidden state, assigns each retrieved memory a variable latent budget through a learned policy, and injects selected latent states as soft memory tokens for generation. The full memory-use process is optimized with downstream task rewards through group-relative policy optimization. We evaluate ElasticMem on MemorySuite, covering memory-intensive QA and embodied agent control. Across Qwen2.5-3B-Instruct and Qwen2.5-7B-Instruct backbones, ElasticMem improves weighted average QA accuracy by 26.2% and 24.6%, and improves ALFWorld success rate by 66.3% and 27.2%, respectively, over the strongest baselines, while achieving the lowest ALFWorld token cost. Ablations and qualitative analyses further show that adaptive retrieval and elastic budget allocation help ElasticMem prioritize useful evidence and transferable plans beyond rigid cosine similarity. Our code for ElasticMem will be released at this https URL.

---


### 45. [Seeing Before Agreeing: Aligning Multi-Agent Consensus with Visual Evidence](https://arxiv.org/abs/2605.30698)

**<font color=#1a73e8>作者：</font>** Yuhan Wang, Shuochen Chang, Yalin Feng 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have achieved strong performance on visual question answering (VQA). To mitigate individual hallucinations and blind spots, aggregating diverse perspectives via multi-agent collaboration has emerged as a promising paradigm. While this approach has shown great success in textual QA, its potential in the multimodal domain remains under-explored. Existing multi-agent VQA methods predominantly adapt text-centric protocols, focusing on textual discussions while ignoring the alignment of visual information. In this work, we reveal a key insight: answer-level agreement is insufficient for reliable multi-agent VQA; \textit{aligned visual evidence} -- shared support from the image regions agents rely on -- is essential for trustworthy consensus. To leverage this insight, we propose EAGLE (\textbf{E}vidence-\textbf{A}ligned \textbf{G}rounded mu\textbf{L}ti-agent r\textbf{E}asoning), a training-free evidence-centered framework for coordinating multiple VLM agents. EAGLE explicitly exposes each agent's grounding regions as visual evidence, enables mutual verification over the evidence, and uses evidence consistency to guide final decision-making. Experiments on six VQA benchmarks show that EAGLE achieves best average performance across domains while remaining lightweight, interpretable, and practical for deployment.

---


### 46. [Equivariant Latent Alignment via Flow Matching under Group Symmetries](https://arxiv.org/abs/2605.30705)

**<font color=#1a73e8>作者：</font>** Sunghyun Kim, Jaehoon Hahm, Jeongwoo Shin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geometry-aware generative models and novel view synthesis approaches have shown strong potential in visual fidelity and consistency. In parallel, equivariant representation learning has emerged as a powerful framework for constructing latent spaces where analytically known group transformations could act directly, capturing geometric structure in data and enhancing both interpretability and generalization in novel view synthesis. However, we identify that existing approaches often suffer from latent misalignment, a discrepancy between the intended group action and the actually required transformations in the latent space. Consequently, the learned latents often fail to consistently preserve the equivariant relations imposed by the underlying group symmetry. To address this, we propose Residual Latent Flow, a flow-based framework that corrects the misaligned latents, thereby improving compliance with the underlying equivariance relation. Our comprehensive experiments show that our method significantly reduces latent misalignment and improves novel view synthesis quality, under rotation groups SO(n).

---


### 47. [SAGE: A Novelty Gate for Efficient Memory Evolution in Agentic LLMs](https://arxiv.org/abs/2605.30711)

**<font color=#1a73e8>作者：</font>** Sijia Wang, Dhanajit Brahma, Ricardo Henao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agentic LLMs must continuously decide whether newly extracted facts should be added, merged with existing memories, or ignored, yet prior work has focused more on retrieval and storage than on principled write-side control. We frame memory evolution as a novelty-detection problem and propose SAGE, a Spherical Adaptive Gate for memory Evolution that scores candidate facts with a von Mises-Fisher-based density estimator over memory embeddings and routes them with an adaptive threshold that tracks memory-store geometry. SAGE resolves clearly novel facts as ADD, clearly redundant facts as NOOP, and sends only uncertain cases to an LLM merge step, reducing expensive write-time reasoning. On LoCoMo, SAGE achieves the best average token-F1 against Mem0 on all seven open-weight backbone comparisons, while on GPT-4o-mini it reduces add-phase API cost by 3.4$\times$ and add-phase latency by 2.5$\times$ with only a small average judge-score gap. As a drop-in binary gate for A-Mem, SAGE skips roughly 16-18% of LLM calls across five models with minimal quality change on open-weight backbones. These results suggest that novelty-aware write control is a practical lever for improving both memory quality and system efficiency in long-term agentic memory.

---


### 48. [ExpGraph: Model-Agnostic Experience Learning with Graph-Structured Memory for LLM Agents](https://arxiv.org/abs/2605.30712)

**<font color=#1a73e8>作者：</font>** Tao Feng, Chongrui Ye, Tianyang Luo 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents have shown strong capabilities in reasoning, tool use, and multi-step interaction, but they often solve tasks from scratch and fail to reuse successful strategies or failure lessons from prior experience. Fine-tuning on collected experience can improve reuse, but it is inflexible when stronger or more suitable executors emerge. We propose ExpGraph, a model-agnostic experience learning framework that enables frozen and replaceable LLM executors to improve through external experience reuse without parameter updates. ExpGraph summarizes historical trajectories into reusable skills and failure lessons, organizes them as nodes in a self-evolving experience graph, and retrieves useful experiences through graph diffusion and utility-aware ranking. A lightweight retrieval copilot is trained with reinforcement learning using feedback that compares executor performance with and without retrieved experiences, while the graph is updated online from downstream task outcomes. We evaluate ExpGraph on ExpSuite, covering question answering, mathematical reasoning, code generation, and multi-step agentic environments including ALFWorld and AppWorld. ExpGraph improves over the strongest baseline by 12.2% and 4.7% on static tasks with smaller and larger executors, and by 21.4% and 12.7% in agentic environments, while reducing average interaction steps by 12.7% and 21.6%. Ablations show that graph-structured experience, utility-aware ranking, and adaptive retrieval jointly enable effective experience reuse across diverse tasks and executor models.

---


### 49. [Diversity Matters: Revisiting Test-Time Compute in Vision-Language Models](https://arxiv.org/abs/2605.30713)

**<font color=#1a73e8>作者：</font>** Yijie Tong, Yifan Hou, Shaobo Cui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time compute (TTC) strategies have emerged as a lightweight approach to boost reasoning in large language models (LLMs). However, their application and benefits for vision-language models (VLMs) remain underexplored. We present a systematic study of TTC across seven VLMs and six benchmarks, specifically analyzing feature-based scoring and majority voting methods. We find that feature heuristics fail and voting yields only modest gains in single-model settings. We theoretically show that this limitation stems from a lack of prediction diversity: when outputs are highly correlated, voting provides little benefit. In contrast, multi-model ensembles offer richer diversity, yet standard majority voting fails to account for varying model capabilities. To address this, we propose Entropy-based TTC (ETTC), which selects the most confident prediction based on predictive entropy. Our method reduces to majority voting in the single-model case, but in model ensembles, it leverages confidence disparities to prioritize stronger models. We prove that ETTC outperforms majority voting under mild assumptions and empirically demonstrate that it consistently surpasses both voting and the best individual model. Crucially, our results show that smaller models can synergistically enhance larger ones, unlocking ensembling gains not achievable with standard strategies.

---


### 50. [Simple Token-Efficient Vision-Language Model for Case-level Pathology Synoptic Report Generation](https://arxiv.org/abs/2605.30716)

**<font color=#1a73e8>作者：</font>** Zhiyuan Yang, Jiahao Cheng, Vincent Quoc-Huy Trinh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating clinically useful pathology reports for pathology cases from whole-slide images (WSIs) is challenging due to gigapixel resolution, long visual-token sequences, and the complexity of case-level reasoning, where a single case may contain multiple WSIs with heterogeneous tissues and ambiguous findings. We present a simple token-efficient vision--language model for case-level synoptic report generation that remains practical under constrained GPU memory. Our architecture follows a minimal three-component design: a frozen pathology patch encoder, a lightweight two-layer MLP vision-language aligner, and a large language model decoder, with an explicit WSI marker token to separate slides within a case. Training proceeds in two supervised stages: (1) aligner-only WSI captioning using heterogeneous WSI-text pairs, and (2) case-level supervised fine-tuning on case-report pairs for structured report generation. To reduce sequence length, we represent each slide using $512 \times 512$ patches at $5\times$ magnification, which reduces the average sequence length by up to $64\times$ times compared to the commonly used $20\times$ patches. Combined with efficient training techniques, we enable practical training with only half a NVIDIA H100 GPU. Across both training stages, our approach achieves high ROUGE-L/METEOR/BLEU-4 scores while being substantially more efficient in memory and runtime. In AI-based evaluations, our model is consistently preferred over strong baselines. Extensive ablations characterize performance-efficiency trade-offs and identify simple choices that improve robustness in multi-WSI settings. Overall, this work provides a strong, reproducible baseline for efficient pathology report generation, lowering the barrier to multi-WSI VLM research under limited compute.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-168](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
