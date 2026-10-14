# 🧠 大模型相关研究 | 2026年10月15日

> 本类共 **810** 篇论文：已确认 **758** 篇，待复核 **52** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**651-700**（第 14/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | **651-700** | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

---

### 651. [Robust Logical Anomaly Detection under Capture Shifts via Synthetic Anomalies](https://arxiv.org/abs/2610.18295)

**<font color=#1a73e8>作者：</font>** Ufuk Efe, Alptekin Temizel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detectors of logical anomalies, such as missing, extra or wrongly combined parts, usually score a test image by its distance from normal (good) images. They achieve near-perfect image-level AUROC on standard industrial anomaly detection benchmarks such as MVTec LOCO, but their robustness to changes in capture conditions remains largely unexamined. Under a heterogeneous perturbation protocol in which each test image is randomly kept unaltered or subjected to a brightness reduction or a zoom-out transformation, the normal-reference methods we tested lose 9.7 to 34.1 AUROC points, and two of the strongest, CSAD and SALAD, fall from 97.7% and 96.4% to 68.1% and 62.3%. We propose a framework in which a classifier, trained on normal images and on synthetic anomalies, scores a test image without comparing it with normal data. From a short description of each product, a language model derives anomaly types and editing instructions, an image editor applies them to normal images, and the classifier learns to separate the edited images from automatically discovered normal sub-modes. With its full training recipe, the framework reaches 94.9% AUROC on clean images, 1.5 to 2.8 points below SALAD and CSAD, and 94.1% under the perturbation protocol. Trained without brightness or zoom-out augmentation, so that neither test perturbation occurs in training, it still reaches 92.5% (93.2% clean). These results suggest that clean benchmark scores can hide a strong sensitivity to capture conditions, and that learning the decision from both normal images and rule violations may reduce it.

---


### 652. [Output Discipline Sets the Floor: A Falsification-Guided, Model-Agnostic Agent Protocol for Auditable Hypothesis-Driven Decision Making](https://arxiv.org/abs/2610.18298)

**<font color=#1a73e8>作者：</font>** Jing Liu, Yongxing Qi, Ping Yao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> What binds large language models on auditable, hypothesis-driven decision tasks, where every candidate can be checked against the evidence? On the public TCMEval-SDT benchmark for Traditional Chinese Medicine syndrome differentiation (200 cases), the binding constraint is output discipline and reasoning structure, not model capability alone: two years of model scaling move zero-shot scores by only -0.03 to +0.08, while output-discipline failures (non-terminating reasoning, format non-compliance, large run-to-run spread) persist even in frontier models. We test this with a model-agnostic agent framework formalizing decision making as a five-stage closed loop, enforced by a candidate x evidence matrix falsification protocol: every candidate is judged against every evidence item, at least half of the candidates must be falsified before a conclusion is licensed, and survivors are emitted in a machine-verifiable single-line format. Across five base models, the effect is sign-conditional on zero-shot output discipline: it rescues models whose discipline fails (DeepSeek-V4-Flash: +0.267/+0.271, entirely termination rescue), reduces a high-variance model's run-to-run standard deviation from 0.218 to 0.007 (Kimi K3), and significantly costs already-disciplined models (-0.087 to -0.120 on budget-matched Qwen3-4B/32B). Ablations attribute the cost to the candidate-bounded format layer and show the effect is independent of injected knowledge content (protocol-knowledge decoupling). The protocol also transfers to misinformation-robust mathematical reasoning, detecting injected false premises at 89.8% recall with a 6.8% false-positive rate (MCC 0.54; a flag-everything baseline scores 0) and restoring accuracy to the no-misinformation ceiling. Where zero-shot output discipline is weak, the reasoning protocol sets the floor; base-model capability always sets the ceiling.

---


### 653. [AffectWorld: Benchmarking Emotion-Driven Future World Prediction](https://arxiv.org/abs/2610.18305)

**<font color=#1a73e8>作者：</font>** Changhao Song, Yacong Chen, Hui Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The world encompasses both physical environments and human actors. Predicting its evolution requires understanding both physical laws and how emotions shape human actions. However, existing world model benchmarks primarily assess physical plausibility and perceptual quality, leaving emotion-driven world evolution largely this http URL introduce AffectWorld, a benchmark that evaluates the chain Emotion-Action-World State through three tasks: World-State Consistency, Emotion-Action Consistency, and Causal Consistency. It comprises 1,498 everyday video samples annotated with plausible emotions, action tendencies, and atomic world-state constraints. A counterfactual subset of 233 samples tests whether changing an agent's emotion under fixed scene and event conditions yields corresponding changes in actions and consequences. We define eight metrics across the three tasks and an additional counterfactual metric, combining automatic visual assessment with human-calibrated VLM/LLM judgments. Evaluations of five SoTA world models (e.g., Cosmos3) required world-state change scores of 0.100-0.280 and counterfactual emotion sensitivity scores of 0.027-0.070 on a [0, 1] scale. These results reveal substantial gaps in generating the consequences of emotion-driven actions and adapting future predictions to emotional interventions. AffectWorld provides a testbed for advancing world models that capture how emotions shape future physical and social states.

---


### 654. [SimInter: Evidence-Grounded User Simulation with Interview-Based Profile Enrichment for Conversational Recommender Systems](https://arxiv.org/abs/2610.18308)

**<font color=#1a73e8>作者：</font>** Erfan Shahabi, Amirhossein Roshandel, Mohammad Sadegh Sadeghi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational Recommender Systems (CRSs) require reliable user simulators for cost-effective evaluation. LLM-based simulators have made realistic simulation possible but typically condition on profiles derived from explicit ratings, demographics, and static sources capturing surface preferences while omitting implicit behavioral characteristics such as decision-making style, aspect-level preferences, and domain expertise. We propose SimInter, a pipeline that elicits these attributes via synthetic interviews between two LLM agents, grounded in the user's statistical profile and historical conversational evidence. Before profile enrichment, an audit agent explicitly flags potential fabrication and stereotyping at the turn level. We instantiate and evaluate SimInter on movie recommendation. We simulate 300 ReDial users and, on a matched subset of 100 users, compare SimInter with a statistics-only baseline: SimInter significantly increases the diversity of expressed preference aspects (filtered aspect entropy: 1.619 vs. 0.859; paired d = 0.96, Holm-adjusted p < 0.001). This gain persists when the simulator converses with two trained recommenders, KBRD and UniCRS, under two independent evaluation judges (+0.28 to +0.56 nats; all p < 0.001). Human evaluation finds 94.3% of enriched-attribute claims supported or partially supported, while human judgments agree with 95.2% of the auditor's binary filtering decisions on a stratified sample.

---


### 655. [Prompt or Policy? Optimizing Physician Slate Presentations with LLM User Simulators](https://arxiv.org/abs/2610.18309)

**<font color=#1a73e8>作者：</font>** Andrei Niculae, Adrian Cosma, Emilian Radoi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Choosing the right physician is a key challenge for patients seeking medical care. Physician recommendation systems identify relevant doctors, but patients still find it difficult to compare their profiles to make a decision. We formulate slate presentation optimization: given a patient's medical case and a fixed, ranked list of physicians, we generate short, case-specific summaries that make doctors easier to compare, while remaining grounded in the information in their profiles. To optimize physician presentations without relying on real patient interactions, we develop an offline framework that uses persona-conditioned LLMs to simulate patient choices. We generate patient personas from attributes extracted from each medical case and evaluate presentations for factual accuracy, relevance, naturalness and simulated patient choice. We also use a second LLM judge, unseen during optimization, to assess simulator-specific overfitting. We compare automatic prompt-level optimization with GEPA, parameter-level optimization with GRPO, and their combination across two model sizes. GRPO substantially outperforms GEPA in satisfying the full set of constraints, and its gains in simulated conversion persist under the unseen judge. GEPA alone brings smaller improvements, but using its optimized prompt to initialize GRPO speeds up training and achieves the highest simulated conversion. These results show that prompt-level and parameter-level optimization play complementary roles in improving how physician recommendations are presented.

---


### 656. [Omni-RS: Unifying Multi-Task Understanding and Generation in Remote Sensing](https://arxiv.org/abs/2610.18323)

**<font color=#1a73e8>作者：</font>** Pan Yin. Shuai Yang, Yuanhao Liu, Datao Tang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Practical remote sensing applications often require both understanding and generation capabilities for the same geographic scene. However, most existing methods address either understanding or generation in isolation, while existing unified remote sensing models' generative ability is limited to text-to-image. To bridge this gap, we propose Omni-RS, a unified framework supporting four remote sensing understanding tasks and five generation tasks. Specifically, we introduce the "Scene-Guided Two-Stage Training" strategy, which first adapts a multimodal large language model to remote sensing understanding and then uses its hidden states to guide a diffusion transformer for image generation. To enable joint learning across diverse generation tasks, we construct UniGen, a unified multi-task generation dataset, by organizing heterogeneous remote sensing data into a unified format. Furthermore, we introduce "Detailed Visual Conditioning", which uses visual conditions encoded by a VAE to guide the generation process, thereby supporting additional generation tasks that require reference images. Extensive experiments demonstrate that Omni-RS performs exceptionally well in understanding tasks and has achieved outstanding results in a variety of generative tasks.

---


### 657. [AssetForge: Asset-Augmented Task Synthesis for Business Automation Agents](https://arxiv.org/abs/2610.18330)

**<font color=#1a73e8>作者：</font>** Xiangrui Liu, Shuo Tang, Siheng Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training business automation agents requires executable tasks that connect a natural-language request to an application state and a verifiable end state. Traditional Rubrics requires Authors to recreate application interfaces, initial records, policy evidence, and outcome checks for each task, entangling business logic with repeated infrastructure work. We introduce AssetForge, an asset-augmented task-construction pipeline that pairs a reusable construction-asset library with task-specific Rubrics. The assets provide application interfaces, world-state components, policy/evidence carriers, and native assertion definitions; the Rubric directs their instantiation for a particular business task. Executable checks and an additional model-based review validate each candidate, return targeted feedback, and support bounded repair before acceptance. On AutomationBench v1.0.6 public-600, fine-tuning Qwen3.6-35B-A3B on 6,000 AssetForge examples yields 41.17% on the official strict pass@1 metric, 4.4 times the 9.33% base score (+31.83 points). With the same backbone and GLM-5.3 supervision, AssetForge reaches 41.17% versus 30.33% for traditional Rubrics, a 10.84-point gain (35.7% relative) at the same accepted-example scale (6,000 versus 6,000 examples). Both DeepSeek- and GLM-supervised AssetForge models improve AppWorld completion over the base model on Test-Normal and Test-Challenge. These results establish the advantage of AssetForge's complete construction pipeline on AutomationBench public: the coupled asset-Rubric interface directs Authors toward business logic, while executable checks and model-based review validate their tasks.

---


### 658. [Probing the Geometry of Color Representations in Multilingual Language Models](https://arxiv.org/abs/2610.18331)

**<font color=#1a73e8>作者：</font>** Pablo Loyola, Edison Marrese-Taylor, Andrés Hoyos-Idrobo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Do multilingual language models learn a universal internal geometry for color, and is it perceptually grounded or primarily linguistic? We decompose color representations into two geometric axes: (P1) alignment to perceptual color space, and (P2) cross-lingual symmetry. Analyzing layerwise embeddings across models and multilingual datasets, we find that perceptual grounding is weak: alignment to CIE-LAB peaks in intermediate layers, then collapses toward output layers. Cross-lingual symmetry degrades with depth, suggesting later layers encode language-specific structure. Functionally, we show that geometric properties predict task performance: models achieve 96.7% accuracy on color classification at layers where P1 alignment peaks, with P1 alignment (r=0.70) significantly correlating with downstream capabilities. Our results reveal a dissociation: text-only LMs learn universal color-language geometry, not universal color-perception geometry, providing diagnostics for where perceptual structure is preserved in language models.

---


### 659. [Lightweight but Linguistically Fair? Quantisation Robustness across Bavarian, German, and English](https://arxiv.org/abs/2610.18343)

**<font color=#1a73e8>作者：</font>** Jophin John, Michael Hoffmann, Piroska Lendvai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-training quantisation reduces the memory cost of large language models, but it remains unclear whether compression preserves language skills of regional varieties as reliably as their standard-language counterparts. We study this question for Bavarian, Standard German, and English using BAVGROUND, a multiple-choice benchmark, where 206 source questions are aligned across all three languages. Across 14 open-weight 7B--10B instruction models, we compare BF16 with 8-bit GPTQ and two 4-bit settings, GPTQ and AWQ. Eight-bit GPTQ remains close to BF16 and largely preserves the relative behaviour of the three languages, while 4-bit quantisation was found to be much less stable. The two 4-bit methods reduce average accuracy by about 1.4--1.5 percentage points and change 11.9--16.0% of BF16 decisions, with changes concentrated on examples where the BF16 model is already uncertain. This instability does not translate into a consistent Bavarian disadvantage. Although Bavarian, a low-resource dialect, has lower baseline accuracy than German and English, the language most affected at 4 bits varies across models and quantisation methods. Calibration further shapes these cross-language effects: the relative Bavarian--German effect changes with calibration language, while changing the calibration source has little average effect on GPTQ-4 but can affect AWQ-4 much more strongly. Free-form evaluation on five models further shows that 4-bit compression can degrade generated responses even in settings where multiple-choice accuracy changes only modestly, while 8-bit GPTQ remains comparatively stable. Overall, our results show that quantisation robustness for regional language varieties depends on the model, quantisation method, calibration data, and evaluation setting, and cannot be measured by aggregate multilingual accuracy alone.

---


### 660. [Choosing LLMs for Strategic Agent Interactions](https://arxiv.org/abs/2610.18354)

**<font color=#1a73e8>作者：</font>** Arastun Mammadli, Herbert Woisetschläger, Jawad Fayaz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Game-theoretic benchmarks claim that large language model (LLM) strategic decision-making varies across game types, interaction structures, and capability dimensions. However, they only evaluate strategic performance across individual fixed models. In parallel, contemporary LLM routers pick models under quality-cost trade-offs, but with no notion of a strategic structure. They do not account for an opponent that might be unknown, and that can adapt over time and shift the feedback signal. To address this, we extend the game-theoretic evaluations and define strategic selection as the meta game layered on top of the base game. In each round, a strategic selector fields an LLM from a portfolio of models to navigate a game payoff matrix that is latent and learned online. We find that the evaluation signal is game-specific, and that extracting a reliable signal requires a much higher number of seed runs $N$ compared to traditional benchmarking setups. Evaluating across 5 games and 10 LLMs, we show a model's strategic competence varies significantly depending on the game setup and the opponent faced. Building on this, we implement a suite of selector methods and find that approaches that rely on query embeddings or LLM self-reflection do not consistently capture the underlying strategic signal. A lightweight multi-armed bandit algorithm performs more reliably across games, though it still falls short of the best fixed model. Finally, we show that simple non-stationary and adversarial bandit variants fail to outperform a stationary bandit baseline, pointing to a gap in how current methods handle a shifting opponent in strategic settings.

---


### 661. [Urbex: Agentic Spatial Grounding for City-Scale 3D Scenes](https://arxiv.org/abs/2610.18356)

**<font color=#1a73e8>作者：</font>** Yu Wang, Rui Dai, Wei Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> City-scale 3D grounding is commonly formulated as candidate ranking, which requires precomputed instance proposals and becomes inefficient in large outdoor scenes. We propose Urbex, an agentic vision-language framework that instead casts grounding as active spatial search. Urbex represents a city-scale 3D scene as an interactive multi-view environment, allowing a VLM agent to query landmarks, zoom into local regions, render oblique views, and commit a grounded bounding box. We optimize this tool-use policy with reinforcement learning on CityRefer, using smooth localization rewards and lightweight shaping rewards for efficient exploration. Experiments show that Urbex achieves the best Hit@1 and IoU on CityRefer, supports candidate-free grounding without ground-truth boxes, and is substantially faster than the strongest city-scale ranking baseline. Zero-shot results on STPLS3D-Refer further indicate improved cross-scene robustness.

---


### 662. [Pin It on Anyone: Certified Targeted Displacement of Multi-Bit LLM Watermarks Without the Key](https://arxiv.org/abs/2610.18359)

**<font color=#1a73e8>作者：</font>** Paweł Batorski, Przemysław Spurek, Paul Swoboda  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-bit watermarking embeds a message, typically an account identifier, into LLM output so that harmful text can be traced to its origin. We show an attack technique that allows to alter the watermarking message. This allows to, for example, exchange the embedded account ID to an arbitrary different one. The attacker mainly needs access to a few accounts for generating LLM output and model logits, but crucially not the secret key used to watermark. The attacker then rewrites the text, keeping its meaning, so that the watermarking message decoder recovers the watermarking message embedded by the attacker. We are, to our knowledge, the first to propose such an attack, which we call a targeted displacement. Theoretically, we present upper and lower bounds on the probability of our attack succeeding. This bound depends on the number of accounts the attacker has access to, the length of the message and some characteristics of the given text. Our attack can succeed whenever we can bound the ambiguity of the generated text well enough. Empirically, we test our attack technique against five watermarking methods and four LLMs. Attack success tracks our predicted bounds, allowing us to alter watermarking messages in almost all cases with high accuracy, given enough accounts. Our code can be found at this https URL.

---


### 663. [Hallucination-aware Faithful Reasoning in Remote Sensing](https://arxiv.org/abs/2610.18369)

**<font color=#1a73e8>作者：</font>** Yi Liu, Jing Zhang, Xiang Feng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have demonstrated promising capabilities for remote sensing reasoning, yet they frequently generate visually unsupported reasoning that contradicts the visual evidence. Existing post-training methods optimize primarily for final-answer correctness, providing limited supervision for identifying and correcting hallucinations that arise during the reasoning process. To address this limitation, we propose \textbf{FaithRS}, a hallucination-aware self-reflection framework for faithful reasoning in remote sensing. We first construct \textbf{SFHD-43K}, a dataset of 43K structured, fine-grained hallucination annotations, and train a detector to identify hallucination types, underlying causes, and supporting visual evidence. FaithRS then incorporates this diagnostic feedback into a Safe Detector-Guided Corrective Rollout framework, where a safety-aware gate selectively determines whether and how to revise the response. Training is driven by a composite reward that jointly optimizes answer accuracy, reasoning faithfulness, hallucination reduction, format compliance, and revision safety. Experiments with Qwen3.5 backbones (0.8B, 4B, and 9B) show consistent improvements across four remote sensing benchmarks, with gains of up to 11.64 points.

---


### 664. [Delegating Earth science model calibration to knowledge-guided LLM agents](https://arxiv.org/abs/2610.18378)

**<font color=#1a73e8>作者：</font>** Zhanliang Zhu, Ziwei Li, Liujun Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Applying process-based Earth science models to new sites and questions often requires expert calibration decisions. Reliable delegation to language-model agents must preserve scientific competence and reproducibility. Here we develop a general calibration harness (GCH) for end-to-end delegation from a calibration request to assessed results. Constrained by a knowledge infrastructure (KI) and a validation convention, agents define parameter domains, observation mappings and objectives, and generate model-specific code. GCH checks the formulations against the same declarations and freezes them before numerical search and assessment, which require no further agent judgement. Agent-authored workflows executed across six model families, with assessment identifying unmet criteria. In snow-model tests, five of five knowledge-guided specifications executed on the first attempt, compared with none of five given only the model name, achieving validation Nash-Sutcliffe efficiency (NSE) of 0.81-0.94 against 0.57 for defaults. Under a common objective, independent GR4J formulations yielded scores within 0.001 NSE; re-evaluating eleven saved parameter vectors reproduced their metrics. In ten paired VIC tests with matched budgets, fixed search was non-inferior to continuing agent proposals (margin, -0.02 NSE; median difference, -0.003). This separation enables end-to-end calibration delegation with inspectable scientific choices and reproducible numerical evaluation.

---


### 665. [ReDiS: Reasoning-Diagnosis Self-Evolution for Multimodal Reasoning in Remote Sensing](https://arxiv.org/abs/2610.18388)

**<font color=#1a73e8>作者：</font>** Yi Liu, Wentao Jiang, Shuo Ni 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have shown strong potential for remote sensing understanding, yet reliable reasoning remains challenging when tasks require fine-grained visual grounding and multi-step inference. Existing approaches typically rely on either costly pre-constructed reasoning trajectories or self-generated signals such as response consistency, which can reinforce shared errors and provide unreliable supervision. We introduce \textbf{Reasoning--Diagnosis Self-Evolution (ReDiS)}, a framework that separates reasoning exploration from candidate evaluation while allowing the two processes to evolve jointly. ReDiS instantiates two role-specific experts from a shared multimodal backbone: a \textbf{Reasoner} that explores diverse visual evidence--answer candidates and a \textbf{Diagnoser} that jointly evaluates the complete candidate set and provides credibility-aware feedback. As the Reasoner evolves, it exposes new candidate distributions and failure modes; the Diagnoser adapts to these changes and, in turn, reshapes the learning signal for subsequent exploration. To handle groups in which all sampled answers are incorrect and group-relative advantages vanish, we further introduce \textbf{Failure-Triggered Recovery (FTR)}, which provides minimal outcome-level correction without prescribing intermediate reasoning trajectories. Experiments on LHRS-Bench, MME-RS, and CHOICE show consistent improvements over Qwen3.5 backbones at 0.8B, 2B, and 4B scales. ReDiS improves category-averaged accuracy by 6.47 percentage points at 0.8B, while ReDiS-4B achieves the highest average performance among the compared remote sensing MLLMs.

---


### 666. [PRISM: Calibrating Black-Box Judges with Counterfactual Probes](https://arxiv.org/abs/2610.18389)

**<font color=#1a73e8>作者：</font>** Kakei Yamamoto, So Kuroki  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used as judges to reduce reliance on costly human evaluation, yet their scores can systematically disagree with human judgments. We ask whether responses to an explicitly imposed evaluative bias can help correct a judge's implicit scoring biases. We introduce PRISM (Probe-based Residual Inference of Scoring Misalignment), which holds the evaluated content fixed and measures score changes when attributes are emphasized or de-emphasized. A local sensitivity model motivates representing these responses as a surrogate Jacobian. Ridge regression on human labels learns a correction to the baseline score. The resulting scoring protocol is rubric-free: it uses overall scores without requesting criterion-level ratings. In the main Jev and Sol comparisons on SummEval summarization and HANNA story evaluation, PRISM and its learned-baseline variant significantly improve agreement with human rankings over uncalibrated scores while remaining competitive with rubric-based methods. A controlled SummEval comparison yields similar agreement for rubric-derived quality probes and style probes, supporting calibration without reproducing rubric criteria. The learned coefficients reveal shared and opposing correction directions across judges.

---


### 667. [Bifocal: Training-Free Mixed Granularity Visual Token Pruning for Multimodal LLMs](https://arxiv.org/abs/2610.18399)

**<font color=#1a73e8>作者：</font>** Peiran Yin, Hao Wu, Zihao Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual token pruning for multimodal large language models (MLLMs) appears highly effective, with existing methods retaining over 95% of unpruned performance on common VQA benchmarks using a quarter of the visual tokens or fewer. However, our extensive evaluation of ten methods across three MLLM families and five ability groups reveals a critical gap: strong general performance often comes at the cost of severe degradation on fine-grained tasks such as OCR and visual grounding. We trace these failures to two limitations of the prevailing paradigm of retaining the highest-ranked native patches. A single importance ranking overlooks the complementary evidence required by different tasks, while sparse patch selection disrupts both image content and spatial integrity. To address these limitations, we propose Bifocal, a training-free, two-stage pruning method built on a mixed-granularity framework. It allocates separate budgets to query-focused and image-intrinsic evidence, complemented by a pooled coarse representation of the entire image. Before the LLM, Bifocal matches question words to visual regions through a soft conjunction balanced against norm-debiased image saliency, while selecting image-intrinsic evidence to maximize representational coverage. Inside the LLM, it further prunes tokens using density-adjusted text-to-image attention. With roughly a quarter of the original visual tokens, Bifocal is the only evaluated method to retain over 90% of unpruned performance in every ability group across all three models, and ranks first on average in all nine model-budget settings. The code is available at: this https URL

---


### 668. [Multi-Stream Residual Computation in Diffusion Language Models](https://arxiv.org/abs/2610.18407)

**<font color=#1a73e8>作者：</font>** Ekaterina Alimaskina, Suren Kazarian, Gleb Molodtsov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion language models reconstruct masked tokens in parallel, offering an alternative to autoregressive generation. Yet their Transformer backbones typically carry visible evidence and evolving masked predictions through a single residual stream. We equip masked diffusion models with multiple residual streams that persist through depth and adaptive routing between them, then investigate how they support these complementary roles. On the pretraining task, two streams reduce reconstruction perplexity by 5.71% on validation data and 5.13% on average across external corpora compared with standard residual connections. We observe that, without predefined roles, visible and masked positions learn distinct routing patterns. Causal interventions show that this distinction organizes read and write routing, while token-specific write strength remains important within each role. Guided by these findings, a model trained with role-conditioned routing recovers half the validation gain from adding a second stream. State interventions explain the benefit of the additional stream: it preserves early token representations for later reuse while evidence accumulates at masked positions. This mechanism recurs at a larger model scale, showing how persistent streams support context preservation alongside prediction refinement.

---


### 669. [Not All Drift Is a Mechanism: Tracing Prompt Adaptation in LLMs](https://arxiv.org/abs/2610.18412)

**<font color=#1a73e8>作者：</font>** Mikhail Aleksandrov, Nail Bashirov, Maksim Ivanov 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prompt-based adaptation offers several ways to specialize a frozen language model, ranging from natural-language prompt optimization to learned continuous prompts. These methods are usually compared through downstream performance, although similar outputs need not arise from similar internal computations. We study how discrete prompt optimization, prompt tuning, and prefix tuning alter the processing of dense and mixture-of-experts language models. Our analysis shows that the location of the adaptation predicts how task information is carried to the output: optimized text primarily changes response construction, input-level prompts write their influence into content representations, and layer-wise prefixes maintain direct control through attention. In MoE models, these differences further induce distinct expert-routing patterns. At the same time, common representation-level measurements respond strongly to generic context changes and do not reliably distinguish useful adaptations from matched placebos. We argue that understanding prompt adaptation requires separating representation drift from the part of that drift that is aligned with, and causally used by, the model's task computation. This perspective provides practical guidance for selecting, evaluating, and interpreting prompt adaptation methods.

---


### 670. [Revisiting the Estimation of Unigram Surprisal in Computational Psycholinguistics](https://arxiv.org/abs/2610.18414)

**<font color=#1a73e8>作者：</font>** Zachary Hopton, Francesco Ignazio Re, Samuel Kiegeland 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Contextual and unigram surprisal are standard predictors of reading time in computational psycholinguistics. While contextual surprisal is typically derived from neural language models, unigram surprisal is usually obtained from independent corpus counts. Although both quantities are deterministic functionals of a single underlying distribution---capturing conditional and marginal structure respectively---this practice breaks their probabilistic link and may introduce estimation error from the mismatch. We propose three principles for estimating unigram surprisal in psycholinguistic research, including the requirement that both quantities be derived from the same language model. We operationalize this principle by introducing a Monte Carlo estimator of unigram surprisal from a language model, along with a marginalized variant that has lower variance empirically. When unigram surprisal is re-estimated under this unified framework, we find evidence that predictors change in their predictive contribution to reading time. We also confirm prior findings that frequency can be a stronger predictor of processing effort than contextual surprisal under this unified framework.

---


### 671. [Do Factuality Methods Make LLMs More Factual? Reproducibility and Fair Comparison](https://arxiv.org/abs/2610.18415)

**<font color=#1a73e8>作者：</font>** Pratuat Amatya, Vinay Setty, V Venktesh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are aligned to human preferences, after pre-training and supervised fine-tuning steps. However, standard RL alignment steps such as RLHF do not focus on factuality of LLMs, hence they may generate non-factual information, which could result in unintended consequences. In response, a number of factuality alignment approaches have been proposed in the literature which claim to improve factuality of LLMs on their own benchmarks. However, these methods have not been reproduced independently and are also not comparable since each uses a different base model, training data, evaluation set, judge, and metric. In this paper, we present the first independent reproduction of five factuality alignment methods, which span on-policy RL (PPO, GRPO, and Dr.~GRPO) and offline preference optimization (DPO and KTO), and compare them on a common benchmark with common evaluation metrics. We found that none of these methods reproduces in full, and on the common benchmark none of the methods significantly outperforms the base model. On closer inspection, the rewards optimize for format, length, or brevity rather than factuality and relevance, whereas the choice between on-policy and offline training matters little. Furthermore, the evaluation metrics and benchmarks are also part of the problem since they do not measure relevance of text to the prompt. Since there is no ground truth associated with the prompts, the reliance on LLM judges and retrieval for verification also makes the evaluation fragile. We release our code, data, and checkpoints.

---


### 672. [Agaram 2.5B: The First Tamil-First Language Model Trained from Scratch with Tool Calling. A Playbook for Under-Represented Languages](https://arxiv.org/abs/2610.18420)

**<font color=#1a73e8>作者：</font>** Ramchand Kumaresan, Madhusudhanan G, Kaushik Kezendirane  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We trained Agaram 2.5B, a 2.5-billion-parameter Tamil-English language model, from scratch on about 50 billion tokens (58% Tamil, the rest English, math, code and parallel text) on one node of eight H100 GPUs in about six days, with a new tokenizer that, unlike our first model's, keeps line breaks. Supervised fine-tuning on 134,428 conversations, whose replies an open-weight teacher model wrote, and three short targeted rounds turned it into a chat model that answers in Tamil script, romanized Tamil (Tanglish) and English and can call tools: on 25 tool prompts whose schemas appear in training it picks the right tool 23 times and gives exactly the expected arguments 13 times. The released model translates better than Sarvam-1, a 2B Indic base model, in all six FLORES and IN22 directions (FLORES chrF 54.3 into Tamil and 55.2 into English, against 49.2 and 44.2), and nearly doubles its base model on native-Tamil IndicIFEval (19.3% from 10.0%). It is weak on knowledge: reading-comprehension and knowledge benchmarks sit near chance, and on 50 held-out everyday questions written by one native speaker, one LLM judge rated 46% of its replies usable (22-24 of 50 over three passes; 95% interval for 23 of 50, 33-60%), with nearly every failure a wrong fact. Our two further SFT experiments changed answer format but not the knowledge measures. We also describe our first model, Agaram 1.5B, whose failures shaped the choices here; how the judge's scores varied between passes on identical replies; and, item by item, what the targeted rounds trained against and where frontier-model text entered the data. The project ran on compute credits and our own funds, about USD 13,300 across both models; the weights are released (licence to be announced after legal review), with GGUF files for this http URL, at this https URL code at this https URL

---


### 673. [Receiver Decides Agent-to-Agent Negotiations](https://arxiv.org/abs/2610.18424)

**<font color=#1a73e8>作者：</font>** Fardeen Sadab, Alif Hasnain, Afsana Shehrin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When one language-model agent asks another for money, which of the two decides how much changes hands? We ran a round-robin tournament of 1,049 negotiations among fifteen agents. In each game a requester tries to raise money from a holder that has been told to keep a $100 endowment. Knowing which agent holds the money explains 47% of the variance in the amount transferred; knowing which agent asks explains 2%. Dropping the most extreme agents narrows the split to 22% against 4%. Changing the requester's appeal from one named person to a group changed what requesters wrote, but the amounts transferred under the two framings are statistically equivalent. The holders that lose least are the ones that turn down the opening request, and their turn-1 refusal rate ranks them by total losses (Spearman correlation = -0.73). Training moves this behaviour in both directions. Fine-tuning Qwen3-8B on a persuasion corpus with almost no refusals raised what it gave away as a holder from 12% to 84% of the endowment. Distilling two never-losing holders into a 4B student cut its losses from 95% to 1%. Evaluations of agents that hold resources should test them in the holder role, including after persuasion fine-tuning.

---


### 674. [Reliable Memory from Unstable Growth: Curating Self-Written Agent Playbooks with Randomized Experiments](https://arxiv.org/abs/2610.18427)

**<font color=#1a73e8>作者：</font>** Hoang Pham, Cong-Duy Nguyen, Dong Le 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Persistent textual memory lets language-model agents reuse lessons from past tasks to improve on future multi-step tasks without retraining. Systems such as ACE and Dynamic Cheatsheet keep it as a playbook: lessons the agent writes after each task and reads in its prompt. A key challenge is to decide which lessons improve later tasks. Current systems leave the decision to the agent itself, which makes performance unstable: the same procedure can write a playbook that helps or one that falls up to 69.6 points below no playbook. These findings motivate valuing lessons by their measured effect on task success rather than by the agent's judgment. We propose Randomized Block Curation (RBC), which measures this effect with a randomized experiment on practice tasks. It groups related lessons into blocks large enough to move success measurably and, on each practice task, includes or leaves out every block at random. Random inclusion makes tasks with and without a block comparable, so the gap in their success estimates the block's effect. RBC keeps the blocks that help and, since the same procedure can write a helpful or a harmful playbook, grows several and serves whichever curated, whole or no playbook scores best on fresh practice episodes. Across two memory systems, three models and three benchmarks, RBC raises average success to 66.9, against 55.5 with the whole playbook, 54.1 with no playbook and 53.8 when the agent's own judgment picks the lessons to keep.

---


### 675. [Estimating Surprisal from the Speech Signal](https://arxiv.org/abs/2610.18439)

**<font color=#1a73e8>作者：</font>** Zachary Hopton, Samuel Kiegeland, Francesco Ignazio Re 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although language is predominantly spoken, empirical tests of surprisal theory rely almost entirely on written text. In practice, surprisal is estimated using language models (LMs) trained on text and applied to transcriptions, creating a text bottleneck that limits evaluation of the theory in the spoken modality. We remove this bottleneck by estimating surprisal directly from the speech signal using a speech LM. This raises a key question: should surprisal be defined over realization-specific acoustic inputs or over abstract linguistic units? Since a single unit can have many distinct acoustic realizations, each assigned a different probability by the model, defining surprisal over abstract units is difficult. To address this, we introduce an importance sampling estimator that approximates the probability of an abstract unit by marginalizing over realizations generated by a text-to-speech model. Using pupillometry data from a listening study, we evaluate surprisal theory in this text-free setting at multiple levels of granularity. Obtaining surprisal from several speech LMs, we consistently find that surprisal estimated via importance sampling better predicts pupil dilation than realization-specific surprisal for words. We also find that surprisal values for sub-lexical units are predictive of pupil dilation. While we find that surprisal can be estimated without recourse to text, and that marginalizing over distinct realizations of words is more predictive of lexical processing effort, surprisal as a whole is not a strong predictor of change in pupil size, regardless of its source.

---


### 676. [Copying Is Not Grounding: Training Faithful Long-Form RAG with Authored-Sentence Credit](https://arxiv.org/abs/2610.18442)

**<font color=#1a73e8>作者：</font>** Hoang Pham, Duc Anh Vu, Duy Tung Doan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In search engines and assistants, long-form RAG answers can mislead readers with claims their sources do not support. Faithfulness rewards, the share of supported sentences, train models toward fewer such claims. We show that these rewards are hacked by copying. A sentence copied from the passages is supported almost by construction, so trained models learn to copy rather than ground what they write. Common defenses only move the hack: a KL or copy penalty leaves copying in place or trades it for shorter, emptier answers and refusals. GRPO, the standard RL algorithm, makes it worse by giving every sentence its answer's advantage, reinforcing copied and grounded sentences alike. We propose Authored-Sentence Credit (ASC) , which fixes both by moving GRPO's reward and advantage from the answer to the sentence level. The reward credits only sentences that are authored rather than copied, say more than the question, and are supported by the passages. The advantage compares each sentence with every sentence sampled for the question, so one that earns no credit ranks last and is never reinforced. Across four models and two in-domain, three held-out corpora, only ASC lowers the error rate of authored sentences and writes more supported ones in every setting, by 38% and 46% at the median under held-out evaluators, giving readers more grounded information. It takes none of these shortcuts, and two LLM judges comparing whole answers prefer no baseline to the base model but rate ASC's answers on par with it. We conclude that a faithfulness reward should credit what a model writes, not what it copies.

---


### 677. [EmoGenie: Benchmarking and Evaluating Expressed and Evoked Emotion in T2I Generation with MLLMs](https://arxiv.org/abs/2610.18455)

**<font color=#1a73e8>作者：</font>** Zixuan Xing, Lancheng Gao, Shengyan Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rapid advances in artificial intelligence-generated content (AIGC) have significantly promoted using text-to-image (T2I) models to generate images with specific affective intentions. However, the emotional effects conveyed by generated images frequently deviate from target expectations, and it remains unclear whether multimodal large language models (MLLMs) can reliably interpret the emotion of AI-generated visual content. Existing affective benchmarks are predominantly built on natural images, while affective studies of generated images have largely focused on emotions expressed in portraits, lacking a unified benchmark for studying the emotions expressed and evoked by generated images. We therefore introduce EmoGenie, a benchmark of emotion for AI-generated images that evaluates capabilities in T2I generation and MLLM understanding across expressed and evoked emotions. It comprises 6,400 images generated by eight T2I models using 800 emotion-targeted prompts, annotated with question-answer (QA) pairs, termed EmoGenie-QA, and continuous human ratings, termed EmoGenie-Assess. EmoGenie-QA contains 90,000 closed-set questions in single-image and image-pair settings, as well as 1,057 open-ended questions for emotion description. EmoGenie-Assess benchmarks continuous affective and aesthetic prediction using 13,175 mean opinion scores (MOSs) aggregated from human ratings in terms of valence, arousal, dominance, and aesthetic quality. We further develop EmoProbe, which combines emotion question answering with response-aligned, dimension-specific regression heads for continuous score prediction. Experimental results show that EmoProbe achieves superior results on emotion-related QA tasks, while its affective and aesthetic predictions correlate better with human ratings, demonstrating its state-of-the-art capabilities of unified coarse-to-fine affective understanding for AI-generated images.

---


### 678. [Kairos: Transactional Security Enforcement at the System Boundary for LLM Agents](https://arxiv.org/abs/2610.18457)

**<font color=#1a73e8>作者：</font>** Kristoffer Hempel, Nils Loose, Lorenzo Cavallaro 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are becoming an integral part of the software development lifecycle, and the capabilities granted to them allow an agent to act with the user's authority on any resource it can access. The reach that gives an agent its utility is equally available to an attacker who can steer it. Anything an agent ingests can carry an injected instruction, and since the model does not reliably distinguish instructions from data, indirect prompt injection should be mitigated by mediating the effects the agent produces. Such mediation faces a structural difficulty. Legitimate work and the first step of an attack often look alike when an individual action is observed, and what separates them lies later in the trace, so a monitor limited to allow and deny is forced to decide before the evidence accumulates. We present Kairos, a reference monitor at the isolation boundary of an unmodified, opaque agent, where a tool call, a shell command, and a script the agent writes all cross the boundary as the same file and network operations, so that confinement holds regardless of the agent's behavior. A declarative policy that states which sources are trusted decides most effects deterministically and defers the rest, which are held while the agent continues speculatively. A decision oracle with bounded authority, such as a language model or a human, releases or refuses each deferred effect on the trace. Across three benchmarks and three agent models, Kairos outperforms existing defenses in the trade-off between attack success and utility. In particular, on AgentDojo, it reduces attack success from 47.0\% to 2.7\% while its benign utility stays at the level of the undefended agent.

---


### 679. [Teacher-Guided Tool Learning for Small Language Models via Bidirectional KL Constraints](https://arxiv.org/abs/2610.18459)

**<font color=#1a73e8>作者：</font>** Haoxuan Gao, Qin-Wen Luo, Xiang Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> External tools can extend the capabilities of small language models (SLMs), enabling their deployment in resource constrained environments. However, their limited capabilities make it difficult for SLMs to discover effective tool use behaviors through reinforcement learning alone, while direct teacher supervision suffers from teacher student behavioral distribution mismatch and may propagate erroneous preferences. To address these challenges, we propose Selective Teacher guided Policy Optimization (SeTPO), which coordinates student exploration with selective teacher guidance and persistent demonstration supervision. Specifically, SeTPO incorporates reverse KL derived token level teacher feedback into policy advantages on low reward trajectories, while auxiliary forward KL supervision preserves teacher demonstrated behaviors throughout training. Under an idealized bidirectional KL objective, we theoretically establish that the optimal policy achieves expected reward no lower than the teacher's while retaining a guaranteed fraction of the teacher's probability mass. Extensive experiments on BFCL v4 and API Bank demonstrate that SeTPO achieves superior overall performance over supervised fine tuning, reinforcement learning, and distillation baselines across all three student scales.

---


### 680. [Readout Scaling Shapes Sparse Feature Recovery](https://arxiv.org/abs/2610.18462)

**<font color=#1a73e8>作者：</font>** Brain Xiao, Sarah Wilson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Readout scaling changes what a sparse autoencoder (SAE) learns, but the benefit of removing it depends on the data. We use readout-canonicalized decision-space (RC-DS) coordinates to remove singular-value gains while preserving retained decision information. At a fixed readout condition number, changing the generating distribution reverses which training coordinates recover known factors best. In our controlled coordinate-matching study, recovery is highest when training restores the space in which the factors were generated. When factors are generated before readout scaling, RC-DS increases mean sparse-factor recovery from 0.506 to 0.913 at condition number 100, compared with centered-logit training under the same budget. An exact wrapper reproduces RC-DS training to numerical precision, isolating training geometry rather than additional information. In neural policies, RC-DS improves mean logit reconstruction under the tested budgets. On three fixed language-model checkpoints, RC-DS has higher mean gain-free reconstruction in all 18 tested task-sparsity settings, while centered-logit SAEs reconstruct output logits better in 17. Small-label-head controls show that longer training reduces the reconstruction gap from 0.0198 to 0.0016. Together, these results show how readout scaling, the data distribution, and training shape sparse learning. RC-DS provides an information-preserving method for studying and controlling the readout's contribution. Separate label-detection and steering tests distinguish these reconstruction effects from task-specific feature usefulness.

---


### 681. [Graph Metanetworks for Transformer Based Language Models](https://arxiv.org/abs/2610.18471)

**<font color=#1a73e8>作者：</font>** Yonathan Wolanowsky, Guy Bar-Shalom, Fabrizio Frasca 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weight-space learning treats the weights of neural networks as data, processed by other models called metanetworks. A key challenge is that different weights can realize the same function, related by a group of symmetries the metanetwork should respect. While symmetry-aware metanetworks for simple architectures such as MLPs are well developed, a comprehensive treatment of transformers, and in particular transformer-based language models, is still missing. Importantly, their weight space has a richer symmetry group: beyond neuron permutations, attention introduces continuous general-linear symmetries of the attention matrices and permutations of entire heads. Existing methods for transformer weights either capture only part of these symmetries or are restricted to a single, fixed architecture, and none accounts for language-model-specific components such as the token embeddings. Building on graph metanetworks, we propose a graph-based approach that is both symmetry-aware and applicable across depths and widths. We formalize a weight-space symmetry group of complete decoder-only language models and provide a graph construction that is invariant to it. We further introduce two new transformer-population datasets with novel tasks, such as training-corpus prediction and fine-tuning detection, on which our approach notably outperforms existing baselines.

---


### 682. [Simplifying and Improving On-Policy Distillation for Few-Step Diffusion](https://arxiv.org/abs/2610.18472)

**<font color=#1a73e8>作者：</font>** Jiawei Zhang, Ziyu Wan, Nanye Ma 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-step distillation reduces the sampling cost of diffusion and flow models, but existing approaches often require auxiliary score models or specialized architectures. We show that simple on-policy velocity regression already provides a strong foundation for 4-NFE generation. To represent teacher velocity variation within each coarse transition, we introduce Pivot, a training-only residual proxy that separates local corrections from the student's interval-mean prediction. We further repel the student from weaker teacher predictions, providing a lightweight mechanism for avoiding undesirable modes. The resulting framework, Simplified Matching Distillation (SMD), remains entirely regression-based, requires neither online score estimation nor adversarial training, and leaves the deployed generator unchanged. We evaluate SMD on image generation and editing, 3D generation, video synthesis, and joint audio--video generation, scaling to 33 billion parameters. At 4-NFE, SMD outperforms strong few-step baselines and surpasses multi-step teachers on several benchmarks. It also supports cross-model, multi-teacher, and causal-video distillation.

---


### 683. [ProTok: Unified Protein Tokenization via Modular Multi-Codebook Quantization](https://arxiv.org/abs/2610.18481)

**<font color=#1a73e8>作者：</font>** Romain Hardy, Xiaoman Zhang, Pranav Rajpurkar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Protein sequence, structure, and functional annotations each capture complementary aspects of protein biology, yet existing tokenizers encode each modality independently, limiting the expressiveness of discrete protein representations. We present ProTok, a unified protein tokenizer that maps all three modalities into a modular discrete vocabulary via product quantization with per-modality codebook groups and modality dropout. A single ProTok checkpoint supports flexible inference from any modality subset without retraining. On seven StructTokenBench benchmarks spanning 14 tasks and 28 test splits, ProTok achieves an average rank of 1.4 across all structure-only tokenizers, placing first on 21 splits and among the top two on 27 of the 28. These gains come without sacrificing reconstruction: ProTok's tokens reach 0.939 lDDT on CATH 4.2, showing that multi-codebook quantization and multi-modal training yield tokens that are both reconstructable and informative. ProTok's structure tokens further lead all baseline structure tokenizers on zero-shot functional retrieval across CATH, Enzyme Commission, and Gene Ontology label hierarchies. The vocabulary also supports generation: a compact language model trained from scratch over ProTok tokens jointly generates backbone and sequence, with 52% of sampled backbones designable versus 21% for a parameter-matched GeoBPE baseline. ProTok shows that structure, sequence, and function can share one discrete vocabulary, motivating protein language models that reason over a unified token stream.

---


### 684. [ReTerm: Recovery Training for Self-Improving Terminal Agents](https://arxiv.org/abs/2610.18484)

**<font color=#1a73e8>作者：</font>** Wei Xie, Kaituo Feng, Shiming Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Terminal agents have shown strong abilities in complex coding tasks. However, they often struggle to recover from errors during long-running execution (e.g., command errors, faulty implementations), eventually leading to task failures. To this end, we present ReTerm, a self-improving terminal agent trained by learning how to recover from its own failed terminal tasks. To support its training, we construct a customized data pipeline and produce ReTerm-10K, a high-quality dataset that provides effective recovery demonstrations for SFT cold start. Furthermore, we propose ReTerm-GRPO, an online RL algorithm that forks from the agent's own failure states to generate multiple independent self-recovery attempts. By learning from whether these attempts successfully complete the task, the agent self-improves through its own recovery experience. Built on Qwen3.5-9B, our ReTerm-9B achieves 34.8% Pass@1 on Terminal-Bench 2.0, improving over the base model by 14.6 points. Further analysis shows that our method achieves consistently higher recovery rates across diverse error categories compared with standard GRPO training. All code, data and model are released at this https URL.

---


### 685. [Judges Follow the Reference: The Derivation Gap in Verifying Tool-Call Arguments](https://arxiv.org/abs/2610.18497)

**<font color=#1a73e8>作者：</font>** Linhai Ma, Yan Wang, Lingfei Qian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-call judges evaluate argument values proposed by LLM agents. We find that they accept a correct value less often when their input holds no reference for it, that is, no text that says what the value should be. This happens when the value is a default value from the function schema that the user did not mention, when it has to be inferred, or when the text it comes from was cut from the judge input. We call this drop in acceptance the derivation gap. It appears across all seven judges we evaluate, including System One models CLM and Jev. The gap is not only a truncation artifact: correct default values have the largest gap on a benchmark with no truncation. A controlled source-relocation test shows that judges follow the reference in their input: they favor a visible incorrect value over a correct value whose source is hidden. We introduce DeRef (Derived Reference): a separate model reads the full history without seeing the candidate and writes a reference for the judge. Across three benchmarks, DeRef improves overall argument AUROC for all judges tested. On the controlled test, it raises AUROC from chance or below to between 98.40 and 99.59.

---


### 686. [Aligning Faithfulness for Theory-Scale Autoformalization](https://arxiv.org/abs/2610.18498)

**<font color=#1a73e8>作者：</font>** Yuming Feng, Tadd Mao, Dhruva Arekar 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autoformalization (AF) requires more than compilation: formal statements must preserve the meaning of their informal sources, a property known as faithfulness. An emerging frontier is the automated evaluation of this property, yet most existing methods operate at the statement level and produce whole-item verdicts, failing to reveal how individual expressions correspond or which contextual interpretations support the judgment. This omission is consequential because AF is inherently theory-scale: target statements derive their meaning from surrounding mathematical material and unstated conventions. We formulate faithfulness evaluation as a context-aware align-then-label problem: identifying phrase-level correspondences between informal and formal statements and assigning a faithfulness label to each under explicitly specified contextual interpretations and assumptions. We also introduce FaithAlign, the first theory-scale faithfulness benchmark comprising 460 items and 4,982 annotated phrase-level links, alongside FaithAlign-Gap, a companion set of 146 items with informal context and assumptions withheld. Each FaithAlign item includes the target statement pair, relevant context, formal dependencies, and, where needed, assumptions specifying one given interpretation. Across 8 models, GPT-6 Astra achieves the highest defect F1 at 47.8% and identifies all defects in only 4.5% of items with two or more defects. On FaithAlign-Gap, Astra identifies only 28.2% of undecidable items as such. These results show the difficulty of recovering context-dependent correspondences, establishing FaithAlign as a testbed for fine-grained, context-aware faithfulness evaluation.

---


### 687. [EgoOmniWorld: Unifying Egocentric Understanding via Ego-Action-World Interactions](https://arxiv.org/abs/2610.18499)

**<font color=#1a73e8>作者：</font>** Songruo Chen, Yuqian Fu, Yu Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric video understanding spans diverse capabilities, modalities, and evaluation formats, yet these are often studied in isolation despite their tight coupling in real-world interaction. We propose the Ego-Action-World interaction loop as a unifying principle: the wearer perceives the world, forms goals, acts, changes the world, and uses feedback to guide subsequent behavior. Based on this view, we introduce EgoOmniWorld, a benchmark organized around four complementary interaction structures: Node captures ego, action, and world states; Edge captures directed relations among them; Chain captures linked dependencies; and Loop captures feedback-closed interactions. We develop an interaction-first, evidence-grounded data pipeline that extracts structured interactions from egocentric videos, grounds them in visual and auditory evidence, and generates questions according to their interaction structure. Required modalities and single- or multi-turn formats follow naturally from the supporting evidence and dependencies. EgoOmniWorld contains 24,166 QA groups, including 20,284 training and 3,882 test samples. Experiments on representative open- and closed-source multimodal large language models reveal substantial and uneven limitations across interaction structures. Models trained on EgoOmniWorld improve in-domain interaction understanding and generalize to existing egocentric benchmarks. EgoOmniWorld provides a unified foundation for evaluating and advancing egocentric video understanding. Data, code, and models will be released.

---


### 688. [The Last Mile of Coding Agents for Long-Document Tasks: An Empirical Study on Clinical Trial Protocol Digitization](https://arxiv.org/abs/2610.18507)

**<font color=#1a73e8>作者：</font>** Jiacheng Lin, Geoffrey Low, Nishit Agarwal 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical trial protocols serve as the source of truth for study design, but are mostly written and used as unstructured PDF documents. Digitizing protocols turns static content into structured, machine-readable data that clinical software can analyze, validate, and execute. Coding agents, which select tools, execute code, and revise their approach as they work, are increasingly applied to such long-document tasks, yet it remains unclear how reliably they turn complete documents into accurate structured outputs. We study this question using protocol digitization as a testbed. We introduce TrialPD-Bench, an expert-annotated benchmark of 150 publicly available protocol PDFs spanning four task categories. Beyond final-answer performance, our evaluation measures evidence recall from agent traces, agent behavior, and cost. Across nine proprietary and open-weight models in five coding-agent harnesses, even the strongest agents do not fully solve protocol digitization. Our analysis further shows that agents usually locate the required evidence but fail in the last mile of transcribing and structuring it. We further develop TrialScribe, a domain-specific harness that equips coding agents with task skills and a verification loop. TrialScribe improves a locally served open-weight model by 6.2-59.4 points across eight metrics, enabling it to match or surpass proprietary models such as GPT-5.6-Sol.

---


### 689. [Towards Safe Autonomy for Computer Use](https://arxiv.org/abs/2610.18508)

**<font color=#1a73e8>作者：</font>** Dominik Seip, Bartol Markovinović, Matthias Hein  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The safety of LLM-based agents currently rests on alignment training and safety classifiers, neither of which can rule out that a sophisticated indirect prompt injection (IPI) goes through and causes significant harm. Recent work therefore builds agents with information-flow guarantees that rely on structured tool interfaces to interact with the environment. Computer Use Agents (CUAs) act visually on the computer screen, which does not provide a boundary between trusted first-party interfaces and untrusted, potentially attacker-authored content. Actions are equally ambiguous: a click may land on an application toolbar or a button controlled by an attacker. Treating the user as the source of trust and confirming each sensitive decision produces confirmation fatigue, with the risk of missing harmful actions. We introduce SA-CUA, a dual-LLM framework that generates a reliable trust boundary for CUAs by deriving conservative deterministic rules from the accessibility tree for unmasking trusted regions from the privileged LLM's screenshot, keeping trusted and untrusted content separated. Human interaction is only required for proper task specification in the beginning. During the task a robust endorsement channel allows values to pass from the untrusted to the trusted domain by verifying information via trusted channels. This allows the agent to autonomously handle tasks involving untrusted information. SA-CUA maintains much higher utility than CaMeL-CUA while keeping the attack success rate at zero.

---


### 690. [Two For The Price Of One: Curvature-Aware Pruning Preserves Influence Functions Too](https://arxiv.org/abs/2610.18516)

**<font color=#1a73e8>作者：</font>** Mehdi Makni, Natalia Ponomareva, Rahul Mazumder  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training pruning enables efficient deployment, but conventional methods do not explicitly preserve internal-gradient alignment between sparse and dense models. We study novel connections between downstream performance of compressed models and the ability to retain gradient information via influence-function preservation. Central to this connection is a curvature-aware objective that accounts for both layer activations and backpropagated gradients. Despite its promise, this objective remains underexplored in pruning due to a lack of efficient solvers. We introduce $\texttt{CACTUS}$, a novel ADMM-based optimizer supporting both pruning and sparse-plus-low-rank decompositions of pre-trained weights. Compared to LLM-Surgeon which targets the same objective, $\texttt{CACTUS}$ can achieve over an order-of-magnitude speedup. At $50\%$ pruning of Qwen3-4B, $\texttt{CACTUS}$ reduces the C4 perplexity gap to the dense model by $45\%$, improves compressed-to-dense per-sample gradient cosine similarity on WikiText-2 from $0.670$ to $0.755$, and runs over $28\times$ faster than LLM-Surgeon on substantially weaker hardware. By preserving influence functions, $\texttt{CACTUS}$ supports effective data selection. On Llama-3.2-3B, fine-tuning a fresh dense model on the $5\%$ of data selected by $\texttt{CACTUS}$ achieves $49.44\%$ accuracy on BIG-Bench Hard, compared with $47.22\%$ using ALPS and $49.54\%$ using dense-model selection. Finally, integrating $\texttt{CACTUS}$ with LoGRA, a recent gradient-projection strategy, on Qwen3-4B with MLP layers pruned to 2:4 sparsity and a rank-64 correction retains a $0.711$ cosine alignment with dense LoGRA-projected C4 gradients.

---


### 691. [The Geometry of Language Model Logits: Generic Structure and Learned Departures](https://arxiv.org/abs/2610.18520)

**<font color=#1a73e8>作者：</font>** Swathi Shree Narashiman, Aravind Ramana Venkatramanan, Nambi Seshadri  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autoregressive language models produce, at every prediction step, a vocabulary-sized logit vector whose structure determines the conditional next-token distribution. We empirically identify that the ordered vocabulary-head logits follow a remarkably consistent log-linear relation
\[ z_{(r)} \approx \mu - \alpha \log r. \] across prediction contexts, architectures, and scales, emerging progressively during pretraining. To our knowledge, this is the first systematic analysis of the logit geometry underlying the distributional assumptions used in the prior decoding work. While controlled order-statistic baselines spanning bounded, light-tailed, and heavier-tailed distributions can largely explain the observed log-linear geometry, they do not explain the systematic shift in the slope $\alpha$: trained language models exhibit $\alpha \approx 1.4$--$1.7$, sitting well above the initialization baseline ($\alpha \approx 0.2$) . Moreover, $\alpha$ correlates with predictive performance, suggesting that it captures learned structure beyond generic extreme-value effects.

---


### 692. [Lost in Implicit Routing: How LLM Agents Fail to Load Relevant Skills at Scale](https://arxiv.org/abs/2610.18522)

**<font color=#1a73e8>作者：</font>** Jinlin Liu, Wei Chen, Xiaojin Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reusable skills let LLM agents load task-specific instructions on demand, but they make execution depend on implicit routing over skill metadata. We test whether this design scales by holding SkillsBench tasks and their golden skills fixed while adding irrelevant skills. We find skill routing collapse: agents increasingly load fewer or no skills, even though the relevant skills remain available. With 1,000 irrelevant skills, loaded-skill recall falls from 73.6% to 27.4% and the zero-load rate rises from 9.3% to 51.6%, whereas explicit selection from the same library retains 73.9% recall. Loading other skills, including plausible alternatives to golden skills, is too rare to explain this decline. Masking only the descriptions of irrelevant skills largely restores skill loading, yet with the metadata intact, explicitly asking agents to plan skill use still yields lower recall than preselection. These findings point to semantic interference from descriptions and instruction interference when skill choice competes with task execution. We also evaluate explicit preselection as a practical mitigation, including its coverage and latency trade-offs. Our analysis informs skill protocols and evaluation for agents with growing skill libraries.

---


### 693. [How Reliable Are System-One Decisions in Medicine? A Comparative Study of Jev, Jev-like Models, and LLMs](https://arxiv.org/abs/2610.18529)

**<font color=#1a73e8>作者：</font>** Yanrui Du, Danyang Zhao, Sendong Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Jev has attracted considerable attention for its rapid, generalizable decision-making, yet its medical reliability remains under explored. To address this gap, our study compares various types of system-one decision models across 15 medical datasets comprising 8,742 instances under a unified protocol. Beyond accuracy, we assess decision stability and the ability to recognize unreliable decisions. Our results show that Jev rivals leading models on primarily text-driven tasks but is less effective on numerically driven tasks, revealing a distinct capability boundary. Under question-format variations, Jev demonstrates strong robustness, achieving the lowest decision reversal rate and relatively small accuracy fluctuations. Among evaluated open-source alternatives, only StartLux exhibits comparable robustness. But these strengths do not extend to reliable abstention awareness: most evaluated models show limitations in both recognizing missing correct answers and using optional abstention. Moreover, we find that Jev's probability-based answer selection can be improved by changing how decisions are scored: normalizing option-wise binary scores yields higher retained accuracy than choice scoring. Taken together, our findings provide early guidance for improving and applying decision models in medicine.

---


### 694. [Meta-Video: Efficient Standardized Evaluation for Video Understanding](https://arxiv.org/abs/2610.18535)

**<font color=#1a73e8>作者：</font>** Soumya Shamarao Jahagirdar, Anna Kukleva, Vishaal Udandarao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video understanding benchmarks are the primary yardstick for measuring progress in video-language modeling, and a growing body of work relies on them to claim improvements. The reported benchmark scores in these works, however, are almost always produced by frameworks (e.g., lmms eval) used as black boxes: certain evaluation choices like frame sampling, preprocessing, and input formatting are inherited from preset defaults and seldom inspected carefully. We show these unexamined choices are a major source of variance. Even for the same model checkpoint, evaluation configuration alone can shift accuracy by up to 19.5pp. Hence, it is unclear whether reported gains reflect genuine improvements in capability or differences in evaluation setup. Moreover, many benchmark samples offer little evidence of visual capability, since they can be answered without the video, and the full suites are expensive to evaluate. We address these issues in two parts. First, we curate existing suites for discriminability and efficiency, producing Meta-Video, a balanced 1,000-question benchmark over 791 videos spanning diverse tasks and durations, which largely preserves model rankings, at 5 times inference speedup for a full-frame count sweep experiment (4-128 frames). Second, we establish a standardized evaluation protocol by sweeping the configuration space to isolate choices that measurably affect results, distill them into best practices and reporting standards, and release reproducible reference scores across five models and seven benchmarks. We hope that the proposed evaluation framework and the Meta-Video benchmark will support video understanding research by providing a reproducible and efficient foundation to measure progress in a reliable way.

---


### 695. [Empathy Is Not the Scapegoat for Declines in Factuality and Reliability](https://arxiv.org/abs/2610.18541)

**<font color=#1a73e8>作者：</font>** Letian Shi, Kanwal Mehreen, Deheng Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models are increasingly expected to support users in stressful or uncertain situations, where warmth and empathy are desirable. While recent work associates warmer models with reduced reliability, we show that this conclusion is incomplete. Prior studies often train primarily on empathetic dialogue, making it difficult to separate tone effects from SFT-induced distribution shift. We revisit this issue at both the model and evaluation levels. We study prompting, SFT, and RL for inducing warm behavior, and comprehensively evaluate capability preservation using an 11-dataset benchmark suite and EMOFACT under emotional contexts. Across multiple model families, we find that warmth effects are task- and model-dependent, while task-aligned adaptive tone can improve empathy and targeted reliability, although some capability trade-offs remain. We further introduce human-validated empathy evaluators specifically developed to assess empathetic model responses. Our results suggest that models can be more supportive in social interactions while remaining reliable.

---


### 696. [Input-Conditioned Search for Efficient Test-Time Scaling of Recursive Reasoners](https://arxiv.org/abs/2610.18547)

**<font color=#1a73e8>作者：</font>** Haochen Shi, Tianwen Fu, Qianggang Ding 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> People often tackle difficult problems by thinking more deeply or exploring more possibilities. Similarly, recursive reasoners, which reason by repeatedly applying a learned update rule to latent states, can also scale inference through more updates (depth) or additional trajectories generated by perturbing latent states (width). When people hit a dead end in their thinking, they may step back and approach the problem from a fresh angle. However, neither depth scaling nor perturbation-based width scaling of recursive reasoners can reliably achieve this: both may converge to incorrect attractors. To address this, we propose to explore diverse reasoning traces by applying different update maps to the same latent state, without any additional training. We realize this idea through \emph{Input-Conditioned Search (ICS)}, which searches over input conditions to induce alternative update maps from the pretrained reasoner. Across six reasoning tasks, ICS achieves the highest mean accuracy, while requiring up to two orders of magnitude fewer model FLOPs than the evaluated scaling baselines. Controlled experiments confirm that ICS can redirect trajectories from the same state. Our theoretical analysis and rigorous numerical verification also confirm that ICS can locally eliminate incorrect attracting fixed points. Together, these findings establish ICS as an effective axis for efficient test-time scaling and motivate further research on shaping recursive reasoning during training and at test time.

---


### 697. [Rethinking Quality in Large Language Model Routing: Security-Conditioned Model-and-Budget Selection](https://arxiv.org/abs/2610.18566)

**<font color=#1a73e8>作者：</font>** Yichi Zhang, Zhenxiang Huang, Yuyang Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) routers reduce serving cost by choosing which model to call and how many output tokens to grant it for each query. Existing routers rank model-budget actions using a single quality metric. This does not work for mixed workloads. For ordinary queries, a good answer is correct and useful (utility); for security-sensitive queries, a good answer refuses harmful requests or resists malicious instructions (security). These two objectives prefer different models and budgets.
We propose SCRouter, a router that learns when to prioritize security and how to allocate the token budget. For each model-budget pair, it estimates the probability that the response finishes within budget. It uses this probability to predict utility and security separately. A small probe determines how to weight these two predictions for each query. SCRouter then selects the model and budget by balancing the weighted utility and security against cost. We also build SCRouterBench, a benchmark of 38,869 utility and security queries spanning nine security dimensions, each answered under all 144 combinations of 12 models and 12 budgets, plus 2,753 out-of-domain queries. SCRouter improves the baselines by 13-29 points in-domain and 19-23 points out-of-domain.

---


### 698. [Configuring RAG Systems: What Breaks, Where Originates, and How to Fix](https://arxiv.org/abs/2610.18567)

**<font color=#1a73e8>作者：</font>** Liangyu Chen, Youpeng Ma, Yulong Ye 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) has emerged as a dominant paradigm for improving Large Language Model (LLM) by intertwining it with other components, such as a vector/graph database. Therefore, the resulting RAG systems are often highly configurable, under which a non-trivial amount of failures are related to the configurations. However, there remains a lack of systematic understanding regarding the configuration issues for RAG systems. To bridge this gap, in this paper, we conduct the first large-scale empirical study of 654 real-world configuration issues collected from 10 diverse RAG systems. Drawing on this, we provide a complete categorization of the symptoms, root causes, relevant stages, and fix patterns of configuration issues for RAG systems, as well as several new observations. Our findings not only reveal the characteristics of configuration issues, but also strongly link them to the unique pipeline stages of RAG, e.g., we found that most symptoms can be observed at the early or late stage, while the stage of the root cause might not be at the same stage as where the symptom is identified. We also provide nine actionable insights to the practitioners on testing, localizing, and fixing the configuration issues for RAG systems.

---


### 699. [CREATE: Creativity Evaluation of VLMs using the Visual Remote Associates Test](https://arxiv.org/abs/2610.18569)

**<font color=#1a73e8>作者：</font>** Ziqing Yang, Anubhav Jangra, Smaranda Muresan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision language models (VLMs) are used in creative tasks such as visual storytelling, design ideation, art interpretation, and advertising. Yet we lack principled ways to measure the lateral reasoning of these models compared to human potential. We introduce CREATE, a semi-automatically constructed benchmark containing 155 visual Remote Associates Test problems. These problems require a solver to find an underlying connection among three seemingly dissimilar images. We conduct a human study (N=25) to validate and ground the quality of our benchmark, and evaluate 11 VLMs. Our findings show that most VLMs underperform humans on this task. Our experiments indicate that the associative ability of VLMs depends on the cue concepts provided in the text and does not universally extend to visual puzzles.

---


### 700. [LLM Agents for Automated Post-Training via Structured Recipe Optimization](https://arxiv.org/abs/2610.18572)

**<font color=#1a73e8>作者：</font>** Ruohong Liu, Bohan Tang, Lekang Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated post-training transforms pre-trained large language models (LLMs) into models capable of handling diverse domains by automatically constructing and optimizing a recipe of coupled decisions over data sources, data processing, cross-domain composition, and training configuration under a limited experimental budget. Existing automation either searches predefined recipe spaces that enable systematic optimization but remain fixed rather than adapting their available choices to the target tasks, or uses open-ended agents that discover task-specific choices but leave them implicit in trial-level edits, limiting their systematic reuse and recombination across trials. To fill this gap, we introduce optimization over a task-adapted recipe space, a novel paradigm that can adapt the recipe space itself to the target tasks while representing its choices explicitly for systematic reuse, recombination, and joint optimization. We instantiate this paradigm with Structured Recipe Optimization (SRO), comprising an LLM-based Recipe-Space Designer that constructs the task-adapted recipe space and a Multi-Domain Recipe Optimizer that uses structured trial evidence to guide LLM candidate construction and multi-objective Bayesian trial selection. Extensive experiments show that SRO achieves the highest average score in all evaluated target-model and agent-LLM combinations. In joint post-training across three capability domains and six benchmarks, SRO reaches 41.1 versus 15.4 for the strongest baseline on Qwen3-1.7B with GPT-5.4, and 53.8 versus 40.8 on Qwen3-4B with DeepSeek-V4-Flash. Our code is available at this https URL.

---


> [!TIP]
> 当前位于：**651-700**（第 14/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | **651-700** | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
