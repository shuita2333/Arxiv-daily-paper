# 🧠 大模型相关研究 | 2026年06月17日

> 本类共 **270** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-270](./part-06.md)

---

### 151. [PVminerLLM2: Improving Structured Extraction of Patient Voice via Preference Optimization](https://arxiv.org/abs/2606.16074)

**<font color=#1a73e8>作者：</font>** Samah Fodeh, Linhai Ma, Ganesh Puthiaraju 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Motivation: Patient-generated text contains critical information on patients' lived experiences, social context, and care engagement, but remains largely unstructured, limiting its use in patient-centered outcomes research. Prior work introduced the PV-Miner benchmark and PVMinerLLM models for structured extraction. However, supervised fine-tuning (SFT) alone struggles with rare, fine-grained, and unevenly distributed errors, particularly in token-critical structured outputs.
Results: We present PVminerLLM2, an improved set of LLMs for structured patient voice extraction that applies preference optimization to address token-critical errors beyond the reach of supervised fine-tuning. Our method introduces (i) a preference objective with token-level gated stabilization term that prevents degradation of absolute token likelihood under preference optimization, and (ii) confusion-aware preference pair construction to better capture low-separation distinctions. We further incorporate token-importance weighting and inverse-frequency reweighing to address token imbalance and class skew. Across multiple model sizes, PVMinerLLM2 consistently outperforms strong baselines, achieving gains of up to 4.43% (Code), 3.50% (Sub-code), and 1.55% (Span), and outperforms baseline LLM trained with existing preference optimization methods.
Availability and Implementation: The supplementary material, code, evaluation scripts, and trained models for PVminerLLM2 are publicly available at: this https URL

---


### 152. [Phys-JEPA: Physics-Informed Latent World Models for Multivariate Time-Series Forecasting](https://arxiv.org/abs/2606.16076)

**<font color=#1a73e8>作者：</font>** Weizhi Nie, Weichao Liu, Honglin Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariate forecasting in physical systems requires models that predict coupled temporal variables while preserving meaningful state evolution. Deep forecasters can fit temporal correlations, and physics-informed models can regularize predictions with scientific constraints, but these directions are often connected only at the decoded-output level. As a result, the hidden predictive state that generates future trajectories may remain statistically useful but physically unstructured. We introduce Phys-JEPA, a physics-informed joint-embedding predictive architecture for multivariate time-series forecasting. Phys-JEPA learns a latent world model in which predictive states are decomposed into physical and residual components, and physical consistency is imposed directly on latent states and latent transitions rather than only on decoded forecasts. This formulation uses known physical variables to organize the representation space while retaining residual capacity for unresolved dynamics. On Jena Climate 2009--2016, Phys-JEPA reduces aggregate MSE from 0.12482 to 0.12273 and temperature MSE from 0.01892 to 0.01831 at H=24. On Traffic, full Phys-JEPA improves aggregate MSE over the supervised baseline across all tested horizons, reducing H=192 MSE from 0.800784 to 0.773873. On Electricity, the best variant depends on horizon: static latent consistency is strongest at H=24 and H=48, while full Phys-JEPA gives the best aggregate and target-variable MSE at H=192. These initial results suggest that moving physics-informed learning from output space to latent predictive state space is a promising direction for interpretable temporal world models.

---


### 153. [Tool-IQA: Augmenting Image Quality Assessment with Simple Tools](https://arxiv.org/abs/2606.16082)

**<font color=#1a73e8>作者：</font>** Guanyi Qin, Junjie Zhang, Chunming He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have been increasingly adopted for Image Quality Assessment (IQA). However, current methods typically employ a static one-shot scoring paradigm, despite the fact that humans assess image quality through dynamic visual inspection, e.g., selectively adjusting views to verify details and subtle artifacts. Specifically, relying solely on a single-pass observation introduces two primary limitations: first, perceiving the image only at a global scale restricts the assessment of finer local details; second, the original intensity distribution of the image may overwhelm the visibility, leading to insufficient inspection of image quality. To address these issues, we propose Tool-IQA, shifting the assessment mechanism from passive scoring to a tool-augmented workflow. In particular, we equip VLMs with simple yet effective view tools: a Magnifier to inspect local details, and a Gamma Corrector to uncover visibility and hidden artifacts. The assessment follows a structured pipeline that consists of an initial observation with rubric notes, a tool-augmented in-depth inspection, and a final quantification for calibrated quality score. Furthermore, to ensure efficient and purposeful tool callings, we introduce a batch-aware training strategy to reward tool interactions that can yield positive contributions rather than simply encouraging usage. Experiments on a variety of IQA benchmarks demonstrate that, with effective tool calling and calibrated assessment, our proposed Tool-IQA significantly outperforms existing state-of-the-art models, e.g., it achieves a PLCC of 0.854 on the challenging CLIVE dataset.

---


### 154. [VinQA: Visual Elements Interleaved Long-form Answer Generation for Real-World Multimodal Document QA](https://arxiv.org/abs/2606.16092)

**<font color=#1a73e8>作者：</font>** Young Rok Jang, Hyesoo Kong, Kyunghwan An 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world documents combine text with tables, charts, photographs, and diagrams arranged in diverse layouts, yet existing research on multimodal large language models (MLLMs) for document QA predominantly produces text-only responses, underutilizing these visual elements. We introduce VinQA, a dataset for long-form answer generation where cited visual elements are explicitly interleaved with their supporting text and grounded in relevant document pages. To support this task, we study two encoding methods for feeding raw document page images into an MLLM, along with their visual-element citation mechanisms: (1) Page Encoding, which directly encodes full-page images with bounding boxes of visual elements and treats these boxed regions as citable units; and (2) Modality Encoding, which parses each page to extract text and crop visual elements, encodes them separately, and uses these cropped elements as citable units. In our experiments, we propose M-GroSE, a multimodal evaluation framework extending GroUSE to assess answers along four dimensions: completeness, answer relevancy, faithfulness, and unanswerability. We additionally report Visual Source F1 to directly measure visual citation accuracy. Although proprietary frontier models still achieve the best overall scores on the VinQA test split, fine-tuning open Qwen2.5-VL models on the training split substantially improves their performance and narrows this gap. Modality Encoding is initially more robust for complex documents with long text, many visual elements, and diverse citation requirements. After training on VinQA, however, Page Encoding reaches a comparable level, competing effectively even without the explicit parsing used in Modality Encoding. Finally, Visual G-Eval, an MLLM-based judge, confirms that fine-tuned models insert visual elements at semantically appropriate positions with faithful supporting text.

---


### 155. [Towards Pareto-Optimal Tool-Integrated Agents with Pareto Ranking Policy Optimization](https://arxiv.org/abs/2606.16111)

**<font color=#1a73e8>作者：</font>** Junyi Li, Xiaowei Qian, Yingyi Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in tool-integrated language agents have significantly improved their ability to solve complex reasoning tasks. However, existing alignment methods predominantly focus on maximizing task accuracy, while overlooking auxiliary objectives such as tool-use efficiency, which are essential for practical deployment. To address this gap, we introduce ParetoPO, a two-stage multi-objective optimization framework for aligning tool-using large language models (LLMs) under competing objectives. In the first stage, ParetoPO leverages hypervolume-guided dynamic scalarization to adapt reward weights based on global Pareto frontier progress. In the second stage, it replaces scalarized learning signals with Pareto-ranking-based advantage computation, promoting nondominated trajectories through dominance-aware credit assignment. This design enables fine-grained, action-level optimization across multiple conflicting objectives. Experimental results on mathematic reasoning and multi-hop QA tasks show that ParetoPO consistently discovers policies with superior accuracy-efficiency trade-offs compared to static and heuristic baselines.

---


### 156. [Know Your Limits : On the Faithfulness of LLMs as Solvers and Autoformalizers in Legal Reasoning](https://arxiv.org/abs/2606.16118)

**<font color=#1a73e8>作者：</font>** Olivia Peiyu Wang, Sanna Wong-Toropainen, Daneshvar Amrollahi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) achieve strong performance on reasoning tasks, but whether this reflects faithful logical inference or heuristic approximation remains unclear. We study this question in legal entailment by comparing three paradigms, including pure LLM classification, LLM-based Formal Reasoning, and solver-based Formal Reasoning using the Z3 SMT solver, on a re-annotated subset of ContractNLI across five LLMs. Our re-annotation reveals a systematic and measurable gap between pragmatic legal interpretation and strict formal entailment, where a substantial proportion of legally sound inferences are not formally grounded without additional unstated assumptions. While introducing formal structure improves accuracy, with LLM-based Formal Reasoning achieving the highest benchmark performance, we show that this gain does not imply faithful reasoning. We identify three recurring failure modes: scope laundering, where LLMs report solver-inconsistent classifications without executing the underlying formal reasoning, producing conclusions that appear logically grounded but are not; implicit constraint blindness, where LLMs overlook logical constraints present in formal representations; and program synthesis failures, where LLMs generate incorrect Z3 code despite structured prompting. Critically, scope laundering persists across all models, raising serious concerns about the faithfulness of LLM-based formal reasoning as a proxy for symbolic execution. These results reveal a fundamental gap between benchmark accuracy and logical faithfulness.

---


### 157. [Training-Free Open-Vocabulary Visual Grounding for Remote Sensing Images and Videos](https://arxiv.org/abs/2606.16124)

**<font color=#1a73e8>作者：</font>** Ke Li, Di Wang, Yongshan Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing visual grounding (RSVG) aims to localize a referred target in a remote sensing image or video according to a natural language expression. Existing RSVG methods usually rely on task-specific manual annotations, which are costly to collect and inevitably limited in covering the diversity of real-world geospatial scenarios. As a result, they often struggle to generalize to open-vocabulary queries involving novel objects, fine-grained attributes, complex spatial relationships, and functional semantics. In this paper, we propose RSVG-ZeroOV, a training-free framework that leverages frozen generic foundation models for zero-shot open-vocabulary RSVG. RSVG-ZeroOV follows an Overview-Focus-Evolve paradigm, which exploits the distinct yet complementary attention patterns of vision-language models (VLMs) and diffusion models (DMs) to progressively generate precise grounding results. Specifically, (i) Overview utilizes a VLM to extract cross-attention maps that capture semantic correlations between the referring expression and visual regions; (ii) Focus leverages the fine-grained modeling priors of a DM to compensate for object structure and shape information often overlooked by VLM attention; and (iii) Evolve introduces a simple yet effective attention evolution module to suppress irrelevant activations, yielding purified object masks. To handle video inputs, we further present Video RSVG-ZeroOV, which extends image-level grounding to spatio-temporal grounding through a query-relevant key-frame selector and a temporal propagator, enabling efficient and temporally coherent video grounding without video annotations or fine-tuning. Extensive experiments on six image and video grounding benchmarks show that RSVG-ZeroOV consistently outperforms existing zero-shot baselines and achieves competitive or superior performance compared with weakly- and fully-supervised methods.

---


### 158. [AuAu: A Benchmark for Auditing Authoritarian Alignment in Large Language Models](https://arxiv.org/abs/2606.16127)

**<font color=#1a73e8>作者：</font>** Andreas Einwiller, Max Klabunde, Florian Lemmerich  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The worldwide surge of authoritarianism, combined with the increasing central role in users' everyday lives, raises the question of to what extent specific models exhibit or promote authoritarian attitudes and characteristics. We introduce AuAu, a comprehensive benchmark that aims to assess the risk of LLMs generating responses with authoritarian tendencies. This benchmark combines three evaluation approaches: (i) psychometric questions from an extensive pool of 15 human validated instruments; (ii) contextual behavior vignettes probing intended actions in concrete situations; and (iii) responses to realistic user prompts. Unlike prior work, AuAu evaluates not only a general closeness towards authoritarianism but also the established sub-concepts Authoritarian Aggression, Authoritarian Submission, and Conventionalism. Evaluating 17 models from China, the EU, Russia, and the USA, we find that all tested models exhibit substantial authoritarian response rates under the psychometric evaluation, though rates drop significantly in increasingly more realistic downstream task. We further find that an authoritarian system prompt easily manipulates 15 out of 17 models to promote increased authoritarianism. Our results underscore the need for continued, systematic auditing of LLM-based AI systems to detect and ultimately mitigate undesired authoritarian tendencies in generated output. Our code and data are available at: this https URL

---


### 159. [XAI-Grounded Explanation Generation for Speech Deepfake Detection with Training-Free Multimodal Large Language Models](https://arxiv.org/abs/2606.16137)

**<font color=#1a73e8>作者：</font>** Yupei Li, Qiyang Sun, Xiaoliang Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech deepfake detection (SDD) systems require trustworthy explanations for reliable decision-making. Existing explanation ways mainly fall into two categories. Traditional explainable AI (XAI), such as gradient-based attribution, produces low-level attribution signals tightly coupled with model decisions, and harder to be understood by human than natural language explanations. Meanwhile, large language model (LLM)-based explanation generation often produces generic and ungrounded descriptions due to the lack of heuristic evidence and task-specific supervision, stemming from limited grounded explanation datasets for SDD. We therefore propose a training-free explanation framework that integrates XAI evidence with multimodal LLMs to generate grounded and specific explanations. Using the PartialSpoof dataset, we construct a grounded explanation dataset and show that methods with XAI increase inside accuracy by over 45\%, verified through human evaluation and faithfulness checks.

---


### 160. [VibeThinker-3B: Exploring the Frontier of Verifiable Reasoning in Small Language Models](https://arxiv.org/abs/2606.16140)

**<font color=#1a73e8>作者：</font>** Sen Xu, Shixi Liu, Wei Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This technical report introduces VibeThinker-3B, a compact dense model with 3B parameters developed to investigate how far verifiable reasoning can be pushed within a strictly small-model regime. Building upon the Spectrum-to-Signal post-training paradigm, we systematically enhance the model through an optimized pipeline that includes curriculum-based supervised fine-tuning, multi-domain reinforcement learning, and offline self-distillation. Experimental evaluations demonstrate that VibeThinker-3B achieves frontier-level performance on highly demanding verifiable tasks. Specifically, it attains a score of 94.3 on AIME26 (improving to 97.1 with claim-level test-time scaling), an 80.2 Pass@1 on LiveCodeBench v6, and exhibits strong out-of-distribution generalization with a 96.1\% acceptance rate on recent unseen LeetCode contests. This effectively places it in the performance band of first-tier reasoning systems, matching or exceeding flagship models that are orders of magnitude larger, such as DeepSeek V3.2, GLM-5, and Gemini 3 Pro. Furthermore, a score of 93.4 on IFEval confirms that this extreme reasoning enhancement does not compromise strict instruction controllability. Extending our previous 1.5B work, these findings motivate the Parametric Compression-Coverage Hypothesis, which views verifiable reasoning as compressible into compact reasoning cores, while open-domain knowledge and general-purpose competence require broad parameter coverage over facts, concepts, and long-tail scenarios. This perspective suggests that compact models are not merely deployment-efficient substitutes, but a complementary path toward frontier-level performance in parameter-dense capability regimes.

---


### 161. [The Quality-Utility Paradox: Why High-Reward Data Impairs Small Model Mathematical Reasoning](https://arxiv.org/abs/2606.16152)

**<font color=#1a73e8>作者：</font>** Haolong Qian, Xianliang Yang, Yinuo ma 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation from powerful reasoning models is widely used to improve Small Language Models (SLMs) on mathematical reasoning, often assuming that traces with higher reward model scores provide more useful supervision. We identify a counterintuitive \textbf{Quality-Utility Paradox} in mathematical reasoning distillation. Data refined or synthesized by a stronger Oracle obtains higher perceived quality according to reward models, yet consistently underperforms traces generated by the SLM itself and selected through rejection sampling across Qwen2.5, LLaMA-3, and DeepSeek families. Our analysis shows that Oracle refinement couples logical repair with distributional drift away from the SLM's native reasoning distribution. This drift increases the learner's adaptation cost and can outweigh the benefit of improved reasoning logic. To test this mechanism, we introduce \textbf{Style-Aligned Refinement}, which preserves the native trajectory of the SLM while retaining logical repair from the Oracle. This intervention lowers adaptation cost and restores downstream utility. These findings suggest that effective mathematical reasoning distillation should jointly optimize perceived solution quality and learner-data compatibility, rather than relying solely on reward-model scores. The datasets and code are available at this https URL.

---


### 162. [Focus When Necessary: Adaptive Routing and Collaborative Grounding for Training-Free Visual Grounding](https://arxiv.org/abs/2606.16158)

**<font color=#1a73e8>作者：</font>** Yifan Wang, Peiming Li, Shiyu Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Multimodal Large Language Models (MLLMs) excel in cross-modal reasoning, they often struggle to perceive fine-grained details in complex high-resolution images. Recent training-free methods address this through image scaling and localized cropping. However, applying these manipulations indiscriminately introduces computational redundancy for simple queries and can degrade accuracy by truncating essential global context or introducing irrelevant background noise. To this end, we propose LazyMCoT, a dynamic and training-free framework that adaptively allocates visual grounding efforts based on sample difficulty. The framework features an Adaptive Routing mechanism that evaluates predictive uncertainty using first-token statistics from a single forward pass. This efficiently bypasses confident cases while ensuring the recall of difficult samples via conformal calibration. For these challenging cases, a Collaborative Grounding module integrates the inherent cross-modal attention of the model with an external visual expert through a two-stage refinement process. This refinement process generates a precise localized display to recover small or occluded targets. Extensive experiments across diverse benchmarks demonstrate that LazyMCoT rivals training-based approaches by simultaneously improving reasoning accuracy and reducing average inference latency. Our code is availble at this https URL.

---


### 163. [Multimodal LLM-Empowered Re-Ranking for Generalizable Person Re-Identification](https://arxiv.org/abs/2606.16161)

**<font color=#1a73e8>作者：</font>** Jiachen Li, Xiaojin Gong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Domain Generalizable (DG) person re-identification (Re-ID) has attracted growing research interest due to its potential for deployment in unseen real-world scenarios. Most existing approaches address DG Re-ID by focusing on training domain-generalizable encoders but ignore the possible refinements in inference stage. In contrast, this work explores an alternative direction which improves inference re-ranking to enhance DG Re-ID. Conventional re-ranking methods typically rely on neighborhood-based distances to refine the initial ranking list, inherently depending on features produced by the Re-ID encoder. However, they deteriorate on target domains since the encoder lacks sufficient generalizability to produce reliable feature distances on unseen scenarios. Inspired by the remarkable generalization capabilities of recent Multimodal Large Language Models (MLLMs), we propose an MLLM-empowered distance metric to improve re-ranking in DG Re-ID. Specifically, we first adapt an MLLM to Re-ID data through supervised fine-tuning, which incorporates a domain-agnostic prompt and a query-candidate hard mining scheme. Then, the adapted MLLM is employed to compute a $\mu$-distance during inference, which is robust to domain gap and significantly enhances subsequent re-ranking performance. Our approach is model-agnostic and can be seamlessly integrated into previous re-ranking frameworks. Extensive experiments demonstrate that our approach consistently yields substantial performance improvements across multiple DG Re-ID benchmarks. The code of this work will be released at this https URL soon.

---


### 164. [TimeVista: Exploring and Exploiting Vision-Language Models as Judges for Time Series Forecasting](https://arxiv.org/abs/2606.16173)

**<font color=#1a73e8>作者：</font>** Zhi Chen, Yuxuan Wang, Jialong Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> High-quality time series forecasting is pivotal for real-world decision-making. However, traditional point-wise metrics often fail to reveal complex temporal patterns and align poorly with human intuitive preferences. While the ''LLM-as-a-Judge'' paradigm has revolutionized text evaluation by providing flexible, human-aligned judgment, its application to time series remains largely unexplored. In this paper, we leverage Vision-Language Models (VLMs) as judges for time series forecasting, harnessing their ability to comprehend time series plots grounded in textual information. Specifically, we propose a novel framework integrating micro- and macro-level judgments informed by contextual information to evaluate time series forecasting. To this end, we introduce TimeVista, a comprehensive VLM-as-a-Judge benchmark comprising 5563 time series samples paired with detailed evaluation rubrics. Extensive meta-evaluations demonstrate that VLMs are highly reliable judges, achieving significantly higher consistency with human preferences than conventional metrics. Building upon our benchmark, we comprehensively assess recent Time Series Foundation Models (TSFMs) under the VLM-as-a-Judge paradigm. Our results demonstrate that VLMs serve as robust and interpretable judges, providing a comprehensive, human-aligned standard for evaluating time series models.

---


### 165. [LLM-Powered Virtual Population for Demand Simulation and Pricing](https://arxiv.org/abs/2606.16183)

**<font color=#1a73e8>作者：</font>** Chengpiao Huang, Kaizheng Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop an LLM-powered virtual population model that simulates demand for pricing decisions, in settings where products are described by rich unstructured information, such as text descriptions and images, and where decision makers need not only mean-demand predictions but also uncertainty estimates for counterfactual prices. Our model represents exposed customers as draws from a finite mixture of customer personas. For each persona, product, and candidate price, an LLM elicits a persona-level purchase probability using both structured persona information and unstructured product information. These probabilities are aggregated through calibrated mixture weights to form a predictive distribution of aggregate demand. The resulting simulator can evaluate counterfactual prices under various pricing objectives, including expected revenue and risk-aware criteria such as conditional value at risk. We test the framework on an online H&M fashion dataset with product descriptions and images. The calibrated LLM-based simulator achieves the best overall predictive performance among the models considered, and supports sample-efficient pricing decisions. Our framework provides a practical way to use LLMs as demand simulators for products with limited historical demand data but rich product information. By producing a full predictive demand distribution rather than only a point forecast, it enables managers to compare candidate prices, quantify demand uncertainty, and choose prices that target either average-case revenue or risk-aware objectives.

---


### 166. [Cascaded Sparse Autoencoders Learn Multi-Level Visual Concepts in Multimodal LLMs](https://arxiv.org/abs/2606.16193)

**<font color=#1a73e8>作者：</font>** Yusong Zhao, Hengyi Wang, Tanuja Ganu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have demonstrated strong performance on vision-language tasks, yet their internal visual representations remain difficult to interpret. Sparse Autoencoders (SAEs) provide a scalable way to decompose dense model activations into sparse, interpretable features. However, existing SAE architectures primarily recover flat feature dictionaries and are less suited for explicit multi-level concept organization. In this paper, we introduce cascaded sparse autoencoders (CSAEs) for learning hierarchical visual concepts in MLLMs. Rather than nesting or stacking SAE sparse activation codes, CSAEs train a second-level SAE directly on the decoder weights of the first-level SAE, treating learned low-level feature directions as inputs for higher-level abstraction. This design enables CSAEs to learn "concepts of concepts" while avoiding drawbacks from the shared-prefix coupling of nesting, Matryoshka-style hierarchies and the bottlenecks of naively stacked SAEs. Experiments across Qwen3-VL, Gemma-3, and LLaVA on multiple visual datasets show that CSAEs improve interpretability in terms of hierarchical concept coherence over state-of-the-art SAE baselines. Results on concept steering further demonstrate that the learned concept groups support effective group-level interventions in MLLM outputs.

---


### 167. [GRACE: Boosting Video MLLMs with Grounded Action-Centric Evidence for Viewer Sentiment Prediction](https://arxiv.org/abs/2606.16198)

**<font color=#1a73e8>作者：</font>** Ruoxuan Yang, Tieyuan Chen, Xiaofeng Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Viewer sentiment prediction in video advertisements aims to infer the latent affective response evoked in the audience. To bridge the gap between what is shown and what is felt, models must deduce hidden viewer emotions from explicit visual narratives, concrete character-object interactions, and visible textual cues. However, standard Multimodal Large Language Models (MLLMs) typically rely on holistic frame representations, which leave these fine-grained, affect-relevant events implicit and complicate precise emotional reasoning. To address this, we propose a grounded action-centric evidence augmentation framework that enhances video MLLMs' clue extraction and comprehension by introducing explicit event structure and localized visual evidence. Our method extracts temporally ordered subject-verb-object (SVO) triplets and auxiliary visible textual cues from action-centric video descriptions, grounds subject and object entities as visual entity crops, and then enables the MLLM to perform clue-enhanced emotional reasoning based on these extracted structured clues. In this way, action triplets specify "what happens", while grounded visual entity crops anchor "who or what participates in each event" to concrete visual evidence. Experiments on the Pitts dataset show consistent improvements over Qwen2.5-VL and Qwen3-VL baselines. Ablation studies, cross-dataset evaluation on AdsQA, and transfer experiments on an emotion-focused TVQA subset further support the effectiveness and generalization of our approach.

---


### 168. [DynFS-MoE: Dynamic Functional-Structural Mixture-of-Experts for Post-Traumatic Epilepsy Diagnosis](https://arxiv.org/abs/2606.16203)

**<font color=#1a73e8>作者：</font>** Jun-En Ding, Spencer Chen, Henry Noren 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Post-traumatic epilepsy (PTE) is a severe complication of traumatic brain injury (TBI), yet early identification remains challenging due to the complex structural and functional alterations it induces in the brain. To address this, we propose a dynamic multimodal Mixture-of-Experts (MoE) framework that integrates functional and structural MRI through time-aware functional-structural encoding and class-conditioned expert routing. Within this framework, modality-specific and cross-modal experts learn complementary representations, while a Modality-Class MoE (MCoE) module dynamically dispatches expert weights according to each classification objective. Experimental results across three binary classification tasks demonstrate that the framework consistently outperforms static fusion baselines, and high-interpretability analyses further reveal meaningful region-of-interest (ROI) interactions. This dynamic multimodal expert framework effectively captures class-dependent brain interaction patterns and provides an interpretable approach for PTE diagnosis and risk stratification.

---


### 169. [Measuring Whether LLM Tutors Teach or Solve: A Diagnostic for Educational Impact](https://arxiv.org/abs/2606.16206)

**<font color=#1a73e8>作者：</font>** Junyi Yao, Zihao Zheng, Baichuan Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly proposed as educational tutors, yet stronger task-solving ability does not necessarily imply stronger learning support. Motivated by recent calls to measure the social impact of NLP systems in practice, we study whether public LLM tutoring benchmarks distinguish learning-supportive behavior from mere answer production. We propose a lightweight diagnostic based on the gap between solving-oriented and pedagogy-oriented benchmark performance. Using public MathTutorBench leaderboard results, we show that these dimensions are only partially aligned: across eight publicly reported models, the correlation between solving and pedagogy composites is 0.421, and several models shift meaningfully in rank when evaluation moves from solving to pedagogy. We then analyze the public TutorBench sample and show that agency-relevant behaviors are explicitly encoded in benchmark rubrics, especially in active-learning settings that reward guiding questions, calibrated hints, and non-disclosive scaffolding. Together, these findings suggest that educational-impact evaluation should not treat task success as a sufficient proxy for learning support. We argue that public tutoring benchmarks can better support positive-impact evaluation by reporting solving-oriented and pedagogy-oriented scores separately and by making disclosure-sensitive, student-agency-preserving criteria more explicit.

---


### 170. [Weaving Multi-Source Evidence for Biomedical Reasoning: The BioMedHop Benchmark and BioWeave Framework](https://arxiv.org/abs/2606.16211)

**<font color=#1a73e8>作者：</font>** Xingyu Tan, Shiyuan Liu, Xiaoyang Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Biomedical question answering (QA) increasingly requires reasoning over interacting entities, where supporting evidence is scattered across biomedical knowledge graphs, literature documents, and web-accessible resources. However, existing biomedical QA benchmarks mainly focus on exam-style knowledge, literature comprehension, or short-range multi-hop inference, leaving source-conditioned graph reasoning and evidence topology construction underexplored. To fill this gap, we introduce BioMedHop, a multi-source graph-grounded benchmark for evaluating biomedical reasoning over structured evidence topologies. BioMedHop contains 10,045 instances across KG, document, web, and hybrid evidence settings, covering shared-neighbor matching, intersection reasoning, path-based reasoning, and counting, with option-based, open-ended, and numeric count renderings. To support this benchmark, we further propose BioWeave, a source-aware reasoning framework that retrieves biomedical KG paths, gathers supporting clues from documents and web sources, assembles them into a unified evidence graph, and verifies answers through entity-level evidence support. Comprehensive experiments show that BioWeave achieves the best overall performance among compared methods on BioMedHop, outperforming the strong hybrid baseline ToG-2 by 10.5% in the overall average. Moreover, BioWeave consistently improves different LLM backbones and enables smaller models, such as Qwen3-4B, to achieve reasoning performance comparable to GPT-4-Turbo.

---


### 171. [Latent Thought Flow: Efficient Latent Reasoning in Large Language Models](https://arxiv.org/abs/2606.16222)

**<font color=#1a73e8>作者：</font>** Xiandong Zou, Jing Huang, Jianshu Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) increasingly rely on intermediate reasoning, yet explicit Chain-of-Thought (CoT) suffers from a linguistic space bottleneck: each thought must be decoded into tokens, causing high inference overhead. Latent reasoning moves deliberation into continuous space, but existing methods mostly learn deterministic or reward-maximizing paths, lacking a principled way to allocate probability across trajectories with different correctness and costs. We propose Latent Thought Flow (LTF), which models reasoning as variable-length continuous trajectories and trains a sampler to match a reward-induced posterior over answer quality and computation cost. We instantiate this with a continuous GFlowNet using stochastic latent transitions. To handle sparse answer supervision, we introduce an Entropy-Weighted Subtrajectory Balance objective for intermediate rewards and a reference-prior regularizer to anchor exploration. Experiments under finetuning and transfer learning settings show that LTF outperforms explicit CoT and latent reasoning baselines, improving accuracy by 9.5% while reducing reasoning length by 27.2% on average compared with strong latent reasoning baselines.

---


### 172. [From Tokens to Regions: CUDA-Sensitive Instruction Tuning for GPU Kernel Generation](https://arxiv.org/abs/2606.16231)

**<font color=#1a73e8>作者：</font>** Wentao Chen, Jiace Zhu, Xing Zhe Chai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-performance CUDA kernels are essential for scalable AI systems, while Large Language Models (LLMs) still struggle to generate correct kernels due to strict and implicit execution constraints. Existing LLM-based approaches either rely on costly agentic or reinforcement-learning (RL) pipelines, or adopt supervised fine-tuning (SFT) objectives that fail to explicitly model CUDA sensitivity, namely code tokens or regions tightly coupled with execution constraints. In this work, we investigate CUDA sensitivity from the perspective of token confidence patterns, showing that CUDA sensitivity appears at both token and region levels, where most CUDA-sensitive tokens are predicted with high confidence, while a smaller low-confidence subset forms regions corresponding to execution-critical structures. These findings suggest that effective CUDA kernel generation should both leverage high-confidence CUDA-sensitive tokens and preserve low-confidence CUDA-sensitive regions. Building on these insights, we propose \textbf{\underline{CU}DA-\underline{Se}nsitive Instruction \underline{T}uning (CuSeT)}, a low-cost post-training method within a simple SFT framework. CuSeT follows the principle of ``from tokens to regions'' by combining \emph{adaptive token-level masking} with \emph{region-aware sample reweighting}. Experiments show that CuSeT consistently improves functional correctness across multiple model families and scales, outperforming standard SFT and advanced SFT variants, while achieving competitive performance against frontier CUDA kernel generation models with substantially lower inference cost.

---


### 173. [Creative Collision: Directorial Persona Steering and Competition in Large Language Models](https://arxiv.org/abs/2606.16240)

**<font color=#1a73e8>作者：</font>** Subramanyam Sahoo, Justin Shenk  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Activation steering has emerged as a powerful tool for shaping the behaviour of large language models at inference time, yet most prior work injects a \emph{single} semantic direction into the residual stream. We study the richer setting in which two semantically opposing steering vectors are superimposed -- a regime we call \textbf{Creative Collision}. Concretely, we construct directorial persona vectors for Steven Spielberg (optimistic, redemptive moral valence) and Martin Scorsese (dark, morally ambiguous) via mean-difference activation contrast on curated screenplay-derived corpora, then interpolate between them with a scalar mixing parameter $\alpha \in [0,1]$ and a steering coefficient $\lambda$. Across five evaluation axes -- moral valence, generation coherence, surface style, directional dominance, and vector geometry -- three principal findings emerge: (i)~Spielberg's representational signature exhibits robust \emph{directional dominance}, suppressing Scorsese's moral influence across almost the entire interpolation range; (ii)~intermediate collision points paradoxically \emph{improve} generation coherence relative to pure single-director steering at high $\lambda$; and (iii)~both personas localise maximally to layer~28 of a 40-layer decoder-only transformer, revealing a shared \emph{moral-tone substrate}. These results illuminate the geometry of competing semantic directions in transformer residual streams and have direct implications for controllable creative generation and value-aligned narrative synthesis.

---


### 174. [Data Augmentations for Data-Constrained Language Model Pretraining](https://arxiv.org/abs/2606.16246)

**<font color=#1a73e8>作者：</font>** Michael K. Chen, Xikun Zhang, Zhen Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As AI labs approach a data ceiling where compute capacity outpaces the rate of new high-quality text generation, language model pretraining is shifting toward a data-constrained, compute-abundant regime that demands productive multi-epoch training on fixed corpora. Standard autoregressive (AR) pretraining overfits severely in this setting, reaching its optimum early and then continuously deteriorating. We investigate data augmentation as a regularizer to mitigate this overfitting and enable productive training for hundreds of epochs on the same data. We introduce three orthogonal categories of augmentation for AR pretraining: token-level noise (masking, random replacement), sequence permutations (right-to-left prediction, Fill-in-the-Middle), and target offset prediction ($x_{t+i}$ for $i > 1$). Through systematic ablations, we find that individual augmentations delay overfitting and lower validation loss relative to the baseline, with random token replacement achieving the best minimum loss among individual methods. Combining augmentation categories further lowers the minimum validation loss. Our experiments demonstrate that data augmentations mitigate AR pretraining's data inefficiency and offer a promising solution to the data-constrained regime. All code and data are available at this https URL

---


### 175. [UniDDT: Unifying Multimodal Understanding and Generation with Decoupled Diffusion Transformer](https://arxiv.org/abs/2606.16255)

**<font color=#1a73e8>作者：</font>** Shuai Wang, Liang Li, Yang Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified Multimodal Models (UMMs) have emerged as a critical direction for general-purpose multimodal intelligence, integrating understanding and generation into a single framework. However, existing UMMs face prominent challenges: (1) the inherent learning conflicts between visual understanding and generation tasks, leading to suboptimal modeling in both tasks; (2) different understanding and generation visual spaces impeding scalability; (3) over-reliance on task-specific data that neglects the duality of text-image understanding and generation. To address these challenges, we propose UniDDT, which leverages a Noisy ViT encoder along with an LLM to unify semantic encoding for visual generation and understanding tasks, while employing a separate diffusion decoder to decouple diffusion decoding from text decoding. With this Noisy ViT encoder, UniDDT is able to leverage the latent space as a unified visual representation, enabling seamless compatibility between understanding and generation tasks. Thus, the scalability within the generation tasks and the semantic expressiveness within understanding tasks can be balanced. Also, we construct dual data structures from the same image-text pairs, fostering interdependence between the generation and understanding data to exploit their inherent duality. Extensive experiments demonstrate that UniDDT achieves effective unification of multimodal understanding and generation with enhanced semantic consistency and scalability. For visual generation tasks, our UniDDT achieves 0.87 GenEval score and 86.9 DPG overall score. For multimodal understanding tasks, our UniDDT achieves 1699.5 score on MME benchmark and 76.5 overall score on SEEDbench.

---


### 176. [GraphWorld: Long-Horizon Planning with World Models for End-to-End Autonomous Driving](https://arxiv.org/abs/2606.16274)

**<font color=#1a73e8>作者：</font>** Ziying Song, Caiyan Jia, Lin Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end autonomous driving has made significant progress by unifying perception, prediction, and planning within a single learning framework, achieving strong performance in short-horizon decision making. However, most existing E2E-AD methods remain confined to short-horizon planning and lack the ability to model long-term temporal dependencies, which severely limits their generalization and security in complex and highly interactive driving scenarios. In this work, we propose GraphWorld, an E2E-AD framework that explicitly enhances long-horizon planning through latent world modeling. We introduce an Ego-Centric Interaction Graph, which adaptively models critical neighboring agents based on spatial proximity, and propagates relational context to planning queries via cross-node cross-attention. We present a World-State-Conditioned Planning that learns ego-centric latent world representations by modeling interactions between an ego vehicle and surrounding agents. This latent world state captures key interaction dynamics and safety-relevant semantics, and serves as a conditioning signal to guide long-horizon, safety-aware trajectory planning. Extensive experiments on Bench2Drive, NAVSIMv1/2, and nuScenes demonstrate that GraphWorld significantly reduces collision rates and improves long-horizon planning performance, validating its effectiveness in complex driving environments.

---


### 177. [SpecAlign: Efficient Specification-Grounded Alignment of Large Language Models via Synthetic Data](https://arxiv.org/abs/2606.16276)

**<font color=#1a73e8>作者：</font>** Wenjie Wang, Yue Huang, Zhengqing Yuan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly deployed in real-world applications, alignment is no longer governed by a single universal notion of safety or helpfulness, but instead by provider- or application-specific model specifications. These specifications are typically long, structured, and frequently updated, yet existing alignment pipelines lack a systematic mechanism to operationalize them as training signals. In this paper, we propose specification-grounded alignment, a new alignment paradigm that treats provider-authored model specifications as the primary alignment target rather than abstract principles or static benchmarks. To instantiate this paradigm, we introduce SpecAlign, a framework that synthesizes alignment data directly from specification documents. SpecAlign combines structured rule annotation, controllable specification instantiation, and multi-agent adversarial data synthesis to generate fine-grained, boundary-aware preference pairs that capture both compliant behaviors and meaningful specification violations. Experiments across multiple model specifications and backbone models demonstrate that training with SpecAlign consistently improves rule compliance while preserving general capabilities and avoiding over-conservative behavior. These results suggest that grounding alignment in explicit model specifications enables rapid, precise, and scalable adaptation of LLM behavior to evolving policy requirements.

---


### 178. [Who Should Lead Decoding Now? Tracking Reliable Trajectories for Ensembling Masked Diffusion Language Models](https://arxiv.org/abs/2606.16281)

**<font color=#1a73e8>作者：</font>** Heecheol Yun, Joonhyung Park, Joowon Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Masked Diffusion Language Models (MDLMs) have emerged as a distinct paradigm for sequence generation. As MDLMs become diverse in capabilities and knowledge coverage, an important question is how to combine their knowledge. Toward this, we first investigate the unique decoding dynamics of MDLMs. We find that successful generations exhibit stable confidence dynamics over answer-relevant positions, while unreliable trajectories can often be corrected by injecting promising intermediate states from other models. Guided by this observation, we propose $\textbf{TIE}$ ($\textbf{T}$rajectory-based $\textbf{I}$terative $\textbf{E}$nsembling), a knowledge fusion framework in which MDLMs iteratively identify reliable decoding trajectories and relay them across models. TIE tracks confidence dynamics over answer-relevant positions to determine which model currently follows a more reliable trajectory and selectively transfers partially denoised sequences across models. As the model on the more promising trajectory often changes across denoising steps, TIE allows different models to contribute complementary strengths at different stages of generation. Strong performance across diverse reasoning tasks, along with our analyses, suggests that TIE offers a practical approach to the underexplored problem of MDLM ensembling.

---


### 179. [FlowMPC: Improving Flow Matching policies with World Models](https://arxiv.org/abs/2606.16286)

**<font color=#1a73e8>作者：</font>** Chandon Hamel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow Matching (FM) is a powerful approach for behavior cloning in multimodal action spaces [Jiang et al., 2025], but because it is not trained to directly maximize expected return, there is still room to improve how FM policies act at test time. This work investigates whether a learned world model can improve FM policies by enabling Model Predictive Path Integral (MPPI) planning over candidate action sequences proposed by the policy. Building on TD-MPC2 [Hansen et al., 2024], I introduce FlowMPC, a framework that combines an imitation-learned FM policy with a learned world model for test-time planning in ManiSkill manipulation tasks [Tao et al., 2025]. Across PickCube and PickSingleYCB, adding the world model improved performance over the FM policy alone, with especially clear gains in end-of-episode success. These results suggest that world-model-based planning can effectively complement flow-based imitation policies without modifying the FM training objective.

---


### 180. [VisualClaw: A Real-Time, Personalized Agent for the Physical World](https://arxiv.org/abs/2606.16295)

**<font color=#1a73e8>作者：</font>** Haoqin Tu, Jianwen Chen, Zijun Wang 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision language models are serving as general-purpose interfaces for complex multimodal tasks. However, deployment still faces three gaps: VLMs typically incur high latency and cost when processing dense video frames and long prompts, the agent scaffold remains static after deployment, and standard video-QA benchmarks do not test whether agents can use visual evidence inside tool-using workspaces. We present VisualClaw, a self-evolving multimodal agent built around two principles. First, hybrid encoding reduces deployment cost by filtering less informative streaming frames with a cascaded gate and compressing the text skill bank through hot/cold top-k injection. Second, skill evolution lets the agent learn from failures: retrieved memories condition an evolver as direct concatenated context or as guided evidence, producing skill-bank updates that help future questions. Across 4 video-QA benchmarks with 2 VLMs, VisualClaw cuts per-question API cost by an average -98% versus full-frame upload and by -25.9% over the offline uniform 8 frame baseline, while boosting accuracy in most settings, e.g., an average +3.85% and a peak +15.80% on EgoSchema with Gemini 3 Flash. To address the gap, we curate VisualClawArena, a 200-scenario multimodal agentic benchmark built through a strict five-stage pipeline; models must use video evidence, documents, dynamic updates, and executable checks inside a workspace. On VisualClawArena, the same framework with computer-use agent backends improves macro accuracy by +2.9% for Codex (GPT-5.5) and +3.2% for Claude Code (Sonnet 4.6) over no-evolution baselines, with a -9.5% cost reduction compared to the uniform-sampled baseline. These properties make VisualClaw a natural fit for edge applications, where the cascade reduces a 1-hour streaming session from ~3,600 API uploads down to only 5-20 calls and the self-evolution makes it a perfect personalized assistant.

---


### 181. [State-Grounded Multi-Agent Synthetic Data Generation for Tool-Augmented LLMs](https://arxiv.org/abs/2606.16307)

**<font color=#1a73e8>作者：</font>** Rahul Khedar, Eshita, Sneha Teja Sree Reddy Thondapu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training tool-augmented LLM agents requires large corpora of multi-turn, tool-grounded conversational data that is expensive to annotate, privacy-constrained in production settings, and largely absent from public datasets. We present StateGen, a synthetic data generation platform that produces scored, reasoning-trace-rich training conversations by orchestrating a four-role LLM loop: a persona-conditioned user simulator, an agent under test, a state-grounded tool simulator, and a multi-axis LLM judge. The key architectural contribution is an authoritative state manager that maintains a structured world-state object across turns, enforcing a backend-is-truth invariant that eliminates the dominant class of tool-call hallucinations by construction. StateGen extends naturally to hierarchical multi-agent settings by declaring sub-agents as tools, all sharing a single state object. We report results on 64,698 evaluated conversations across three production corpora: tool-call hallucination scores reach 9.66/10, the system supports persona-driven variation via a 23-dimensional trait vector, and a cleanly separated train and golden evaluation set split confirms the data is not memorization bait (per-criterion gap analysis). Comparison with eight external systems shows that no single publicly available platform combines multi-turn generation, state-grounded tool simulation, hierarchical multi-agent support, and built-in judge scoring.

---


### 182. [AdaSTORM: Scaling LLM Reasoning on Dynamic Graphs via Adaptive Spatio-Temporal Multi-Agent Collaboration](https://arxiv.org/abs/2606.16328)

**<font color=#1a73e8>作者：</font>** Bing Hao, Ruijie Wang, Haodong Qian 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) demonstrate remarkable potential in dynamic graph reasoning, but suffer from a scaling bottleneck: current models can only handle graphs with tens of nodes, constrained by exponential reasoning overhead and finite context windows. While multi-agent systems (MAS) offer collective reasoning and topology-aware orchestration, capabilities naturally suited for graph-structured tasks, their application to dynamic graphs remains unexplored. This paper presents Scaling LLM Reasoning on Dynamic Graphs via Adaptive Spatio-Temporal Multi-Agent Collaboration (AdaSTORM), a framework that reformulates large-scale dynamic graph reasoning into two stages: (i) Adaptive Partitioning, partitioning large-scale dynamic graphs into subregions that match the model's reasoning capacity while minimizing inference cost; and (ii) Collaborative Reasoning, aligning graph partition topologies with a spatio-temporal decoupled multi-agent architecture. AdaSTORM is the first multi-agent framework tailored for dynamic graph reasoning. Extensive experiments show that AdaSTORM successfully breaks through the scaling bottleneck, scaling reasoning to thousand-node graphs with over 90% accuracy across several large-scale dynamic graph settings without external tools, significantly outperforms seven competitive baselines. Furthermore, it achieves state-of-the-art accuracy on existing benchmarks and generalizes robustly to real-world datasets. The source code is available at: this https URL.

---


### 183. [Chronological Blindness: Benchmarking Temporal Reasoning in Vision-Language Models with CHRONOSIGHT](https://arxiv.org/abs/2606.16334)

**<font color=#1a73e8>作者：</font>** Parthaw Goswami, Jaynto Goswami Deep  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human perception of visual scenes is inherently temporal. We instinctively recognise whether a fruit is ripening or rotting, whether construction is progressing or being demolished, and approximately how much time separates two photographs of the same subject. Whether large vision-language models (VLMs) share this competence remains an open and practically important question. We introduce CHRONOSIGHT, a rigorously controlled benchmark evaluating five dimensions of visual temporal reasoning: CHRONORANK (chronological ordering of image sequences), CHRONOLOCATE (ordinal stage localisation from a single image), CHRONODELTA (estimation of time elapsed between two images on a logarithmic scale), CHRONOREVERSE (detection of temporally reversed sequences), and CHRONOODD (identification of a temporal outlier within a set). The benchmark comprises 1{,}000 items across eight process families (biological growth, food transformation, physical weathering, construction, environmental change, human ageing, astronomical phenomena, and urban dynamics) spanning timescales from minutes to millennia. We evaluate eight open-source VLMs (500 M to 19 B parameters) under two prompting regimes and collect human performance baselines. Human performance averages 0.89 across tasks; the best open model (Qwen2.5-VL-7B) reaches 0.40 under direct prompting, a gap we term chronological blindness. Lightweight LoRA fine-tuning on 151 examples raises CHRONODELTA accuracy from near-zero to 0.43, transferring zero-shot to related tasks (CHRONOODD: 0.37; CHRONOREVERSE: 0.64)suggesting the bottleneck is partly instruction following rather than visual perception. Benchmark, code, and predictions will be released upon acceptance.

---


### 184. [Medical Heuristic Learning: An LLM-Driven Framework for Interpretable and Auditable Clinical Decision Rules](https://arxiv.org/abs/2606.16337)

**<font color=#1a73e8>作者：</font>** Wei Xu, Ke Yang, Gang Luo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Predictive modeling for clinical tabular data is central to clinical decision support and therefore requires not only strong predictive performance but also transparent decision logic. Although deep learning and tree-based ensemble methods can achieve high accuracy, their black-box nature remains a major obstacle to clinical deployment. This challenge is further compounded by common characteristics of medical data, including limited sample sizes, severe class imbalance, and feature evolution arising from changes in diagnostic criteria and clinical documentation. To address these issues, we propose Medical Heuristic Learning (MHL), an instantiation of the learning-beyond-gradients paradigm for clinical tabular prediction. Instead of relying on neural network weight updates, MHL uses a large language model (LLM)-driven workflow that integrates statistical probes, medical knowledge probes, rule synthesis, and code-level iterative refinement to optimize a deterministic and executable decision system. The resulting model is expressed not as opaque parameters, but as versioned pure-Python decision rules that are explicitly interpretable, fully auditable, and clinically grounded. MHL also supports continual learning by starting from previously validated rules and iteratively revising them using updated feature information under data drift or feature evolution. Comprehensive experiments on medical datasets show that MHL achieves performance comparable to state-of-the-art methods while maintaining strong behavior in small-sample and highly imbalanced settings. The results further indicate that this explicit rule update mechanism can help alleviate catastrophic forgetting under feature evolution. Overall, these findings suggest that non-gradient-based heuristic systems offer a transparent and adaptable alternative for high-stakes clinical decision support.

---


### 185. [Whose hotel does the AI recommend? An algorithm audit of reputation signals in LLM-assisted hotel selection](https://arxiv.org/abs/2606.16344)

**<font color=#1a73e8>作者：</font>** Mirza Samad Ahmed Baig, Syeda Anshrah Gillani, Asher Ali  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Travelers increasingly ask large language model (LLM) assistants which hotel to book, making these systems gatekeepers of property visibility -- yet what moves their recommendations is undocumented. We conduct a pre-specified algorithm audit using a randomized choice-based conjoint: across personas, prompt templates, and twelve open-weight and proprietary models, assistants choose among five hotels whose guest rating, review volume and recency, management response, chain affiliation, price, eco-certification, and list position are independently randomized. We estimate the average marginal component effect of each signal on the probability of recommendation. Guest rating and price dominate (a top rating raises selection by 31.6 percentage points; a high price lowers it by 30.0), reproducing human valence-and-price primacy but over-weighting eco-certification and ignoring management response. List position -- a content-free artifact -- shifts recommendations causally, worth about \$12 per night. Stated reasons track revealed weights imperfectly. The findings ground generative engine optimization and the accountability of AI infomediaries in causal evidence.

---


### 186. [Communication-Efficient Verifiable Attention for LLM Inference](https://arxiv.org/abs/2606.16352)

**<font color=#1a73e8>作者：</font>** Ziqun Chen, Ming Wu, Michael Heinrich 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Computation integrity of remote large language model (LLM) serving can be questionable. For conventional deep neural networks (DNNs), the existing TEE-shielded DNN partitioning (TSDP) approach uses Trusted Execution Environment (TEE) to compute non-linear components and verify the integrity of linear components offloaded to an untrusted GPU. However, directly applying TSDP to Transformer-based LLMs incurs significant TEE computation and TEE-GPU communication overhead. This paper presents Communication-efficient TEE-GPU Attention (\textsc{VeriAttn}) for accelerating verifiable LLM inference. \textsc{VeriAttn} offloads both linear and non-linear computations of attention to the GPU, while TEE performs verification. Moreover, for prefill, \textsc{VeriAttn} uses a two-level pipeline to overlap data movement, TEE pre-/post-processing, and GPU computation. For decoding, when the key-value cache exceeds available GPU memory, \textsc{VeriAttn} partitions attention across TEE and GPU to reduce repeated key-value transfers. Evaluation on an Intel TDX platform shows that \textsc{VeriAttn} achieves 2.60-3.38$\times$ and 3.86-5.42$\times$ acceleration over TSDP for 6k-token prompts and 10k-token outputs during prefill and decoding, respectively.

---


### 187. [GraphBEV++: Multi-Modal Feature Alignment for Autonomous Driving](https://arxiv.org/abs/2606.16354)

**<font color=#1a73e8>作者：</font>** Ziying Song, Caiyan Jia, Lin Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feature misalignment in BEV perception is a critical yet often overlooked challenge in autonomous driving, especially under calibration uncertainties between LiDAR and camera sensors. To address this issue, we propose a robust multi-modal fusion framework, GraphBEV++, which systematically mitigates projection-induced misalignment. The framework consists of two key modules: LocalAlign-v2 and GlobalAlign-v2. LocalAlign-v2 introduces neighborhood-aware depth features via graph matching to correct local misalignment. It supports both LSS-based and query-based BEV representations, making it compatible with BEVFusion and BEVFormer architectures for consistent cross-paradigm alignment. GlobalAlign-v2 encompasses two variants: Deformable and Diffusion. The Deformable variant addresses global misalignment in LSS-based multi-modal BEV by explicitly learning cross-modal feature offsets. In contrast, the Diffusion variant targets implicit misalignment in query-based BEV by injecting noise to simulate misalignment and employing a denoising process to recover aligned features. Experimental results show that GraphBEV++ achieves state-of-the-art performance under misalignment noise on nuScenes and Waymo subset, improves long-range detection on Argoverse2, and generalizes effectively to the 3D occupancy prediction task, consistently improving occupancy estimation accuracy and robustness under both clean and noisy settings. Furthermore, GraphBEV++ effectively alleviates misalignment issues in end-to-end autonomous driving. Compared with five baselines (UniAD, VAD, FusionAD, MomAD, and WoTE), it demonstrates superior performance in both open-loop (nuScenes) and closed-loop (Bench2Drive and NAVSIM) evaluations across perception, prediction, and planning tasks.

---


### 188. [Tyler: Typed Latent Reasoning for Language Models -- When to Think, What to Compute, and How Much to Allocate](https://arxiv.org/abs/2606.16360)

**<font color=#1a73e8>作者：</font>** Hanyu Lin, Min Cai, Jiawei Wen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) prompting improves reasoning in large language models (LLMs) by externalizing intermediate computation as discrete text tokens, but this textual interface also introduces redundancy and inference overhead. Latent reasoning offers a promising alternative by carrying part of the computation in continuous representations. However, existing methods typically predefine when latent computation is invoked and how it is allocated during decoding, leaving a key problem unresolved: when to invoke latent computation, what type of computation to perform, and how much budget to allocate. We propose \textbf{Ty}ped \textbf{L}at\textbf{e}nt \textbf{R}easoning (Tyler), a typed and budget-aware framework for latent reasoning during autoregressive decoding. Tyler learns a policy that, at each decoding step, chooses between emitting a text token and switching to a latent computation module specialized for a particular reasoning function. Once invoked, an operator maps the current reasoning state into latent tokens that support global planning, local state updates, or reusable procedural abstraction. Across extensive experiments on three backbone LLMs, Tyler improves accuracy by up to 14.49 points over CoT and by up to 4.30 points over the strongest competing baseline. It further generalizes across diverse reasoning domains and achieves the best final-stage performance with the lowest forgetting.

---


### 189. [Looking Is Not Picking: An Attention-Segment Account of Tool-Selection Failures in LLM Agents](https://arxiv.org/abs/2606.16364)

**<font color=#1a73e8>作者：</font>** Shiyang Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents mis-call tools, and the natural guess is that the model failed to see the right tool in a crowded harness. We show the opposite through a lens concurrent work sets aside -- the model's attention to labeled tool-definition segments. On real BFCL failures, by per-candidate attention argmax the model attends most to the correct tool 80% of the time (vs. 21% chance), and the gold is the under-attended segment on only 10%: it looks at the right tool and still picks wrong. This directly refutes the intuitive "crowded-harness / lost-in-the-middle" explanation: the failure is at the decision readout, not the harness, and we pin it there three ways. (1) Input vs. readout: repairing the prompt (reordering or duplicating the gold tool) recovers <=23% of failures, while readout-side interventions recover 59-91%. (2) Representation-invariance: two gold-pointed interventions in different representations -- an additive attention-logit bias and a residual-stream steering vector -- recover largely the same failures (per-task Jaccard 0.865 pooled, 0.79-0.91 per model), so the bottleneck is localized to the readout independent of which representation is poked. (3) A training-free, gold-free selector: per-segment attention closes most of the gold-free-vs-oracle gap on BFCL (+11.9 pts pooled function-name selection vs. +17.9-pt oracle headroom) and adds +14.9 pts on Seal-Tools; every model positive (exact McNemar p<=8e-4 each). Scopes differ: the causal attention-bias dose-response is bidirectional and monotonic on 10 mask-honoring models (3-32B), the full 0.5-32B span carrying only the correlational diagnostic; the deployable selector is evaluated on 5 single-turn models and does not yet transfer to a multi-turn loop.

---


### 190. [Evaluating LLM Personalization via Semantic Constraint Verification](https://arxiv.org/abs/2606.16368)

**<font color=#1a73e8>作者：</font>** Xuran Li, Guanqin Zhang, Imran Razzak 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current evaluation paradigms for Large Language Model (LLM) personalization rely heavily on brittle surface-matching metrics or computationally expensive LLM-as-a-judge protocols, both of which lack interpretability. To address these limitations, we introduce Natural Language Inference Constraint Verification (NLICV), a scalable, semantically invariant framework that maps sentence meanings to truth-condition sets to verify personalization constraints via a Natural Language Inference (NLI) model. Moving beyond binary scoring, NLICV categorizes LLM behaviors into four distinct modes: personalization, generalization, sycophancy, and failure. Extensive experiments demonstrate that NLICV aligns closely with human annotations while drastically reducing the latency and token costs associated with LLM judges (up to 2100 inference speedup). Finally, through an ablation-based procedure, NLICV pinpoints the exact sentences driving the constraint verification, yielding faithful, understandable evidence for its evaluations.

---


### 191. [Scalable and Interpretable Representation Alignment with Ordinal Similarity](https://arxiv.org/abs/2606.16379)

**<font color=#1a73e8>作者：</font>** Diogo Soares, Pankhil Gawade, Andrea Dittadi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluating representation similarity is fundamental to representation learning. However, existing metrics suffer from significant limitations: they lack interpretability due to shifting baselines, lack robustness to outliers, and are computationally intractable for large datasets, forcing reliance on heuristic approximations. To address this, we develop an ordinal-similarity framework, instantiated by the Triplet (TSI) and Quadruplet (QSI) Similarity Indices, which measure alignment by quantifying the consistency of ordinal relationships. We theoretically demonstrate this formulation is inherently interpretable, robust to outliers, and computationally efficient. Finally, we establish a formal equivalence between TSI and local neighborhood alignment, measured by Mutual Nearest Neighbors. Empirically, we validate these properties and show that ordinal similarity offers a scalable approach to measuring alignment, enabling practitioners to better understand and design representations.

---


### 192. [Surpassing Scale by Efficiency: A Compact 135M Parameter Foundational LLM Natively Adapted for the Bangla Language](https://arxiv.org/abs/2606.16383)

**<font color=#1a73e8>作者：</font>** Rabindra Nath Nandi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While the NLP landscape is dominated by multi-billion parameter architectures, their deployment in low-resource, non-Latin scripts remains computationally prohibitive for edge configurations, mobile systems, and decentralized local hardware. This paper presents bangla-smollm-135m, a highly compact 135-million parameter decoder-only foundational model engineered explicitly for high-efficiency language modeling in the Bangla script. By leveraging a deterministic intersect-and-append token merging strategy between TituLLMs and SmolLM2-135M, the model overcomes subword script fragmentation without destabilizing early pretrained parameter states. In zero-shot multi-task benchmark evaluations (PIQA_bn, OpenBookQA_bn, CommonsenseQA_bn, and Bangla_MMLU), bangla-smollm-135m matches or outperforms models twice its size (Gemma-3-270m) and achieves parity with models in the 1B parameter tier. The model is available at rnnandi/bangla-smollm-135m

---


### 193. [A Mechanistic Understanding of Pronoun Fidelity in LLMs](https://arxiv.org/abs/2606.16407)

**<font color=#1a73e8>作者：</font>** Katharina Trinley, Jesujoba O. Alabi, Dietrich Klakow 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Faithful and robust pronoun use is important for fair and coherent generations, yet large language models largely fail when multiple referents use different pronouns. To study the interplay of reasoning, repetition, and bias in this task, prior work relies exclusively on behavioural approaches, which may not reflect a model's internal workings. Therefore, we provide a mechanistic, model-internal perspective on pronoun fidelity, testing whether three mechanisms -- group entity binding (G), recency bias (R), and stereotypical bias (S) -- are causally implemented across several SOTA language models. Using Boundless Distributed Alignment Search, we find all three coexist as causal subspaces distributed across network depth. No single mechanism fully explains model behaviour, but a combination of the three consistently accounts for 91-99.5%. An attention head analysis further reveals two competing copying routes; group binding and stereotype share a localized concept-level route that retrieves a bound occupation-pronoun unit, while recency uses a distributed token-level route that repeats surface forms. In sum, pronoun fidelity arises from competition between simultaneously active causal subspaces.

---


### 194. [MUNI: Multimodal Unified Latent Diffusion for Coherent Any-to-Any Generation](https://arxiv.org/abs/2606.16408)

**<font color=#1a73e8>作者：</font>** Kyeongmin Yeo, Yunhong Min, Minhyuk Sung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce MUNI, an end-to-end multimodal latent diffusion framework for any-to-any generation that unifies subset-conditioned cross-modal generation and unconditional joint sampling through a shared stochastic latent. Existing multimodal generative models are largely LLM-based, which limits leveraging modality-specific generators and requires text-paired data for training. Recent diffusion- and flow-based any-to-any extensions take a different direction but still rely on text-aligned embeddings, fully-paired training, or matched-dimensionality deterministic mappings. MUNI rests on two complementary contributions, one architectural and one in the training objective. First, we extend latent diffusion to multimodal any-to-any generation end-to-end: instead of the standard two-stage recipe that precomputes a frozen latent space and then fits a prior over it, MUNI jointly trains modality-specific encoders, expressive decoders, and a single shared flow-based prior under one objective. Second, we identify that the standard aggregation rules of multimodal variational inference are insufficient once coupled with a learned prior and expressive decoders. A suitable shared latent must simultaneously satisfy coherence across generated modalities, predictive sufficiency of subset latents, and minimality of the latent content. We propose a routed training objective whose structural choices align the latent with these criteria and admit a minimal-sufficiency characterization in the realizable setting. Experiments on PolyMNIST-Quadrant-Labels and a large-scale image-text-audio benchmark show MUNI matching or exceeding the strongest baselines on conditional generation while opening its largest margins on unconditional coherence. Project page: this https URL.

---


### 195. [PathRouter: Aligning Rewards with Retrieval Quality in Agentic Graph Retrieval-Augmented Generation](https://arxiv.org/abs/2606.16409)

**<font color=#1a73e8>作者：</font>** Bo Wang, Heyan Huang, Yaolin Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agentic GraphRAG trains language-model agents to iteratively retrieve and reason over graph-structured evidence, enabling more accurate and context-aware decision-making by efficiently navigating complex information networks. However, outcome-only reinforcement learning suffers from \textit{\textbf{answer-path reward aliasing}}, where correct answers may come from shortcuts rather than useful evidence paths. It also exhibits \textit{\textbf{search-update ambiguity}}, as scalar trajectory-level feedback does not indicate which retrieval actions to adjust. To mitigate these shortcomings, we present PathRouter, a path-aware training framework for agentic GraphRAG. PathRouter jointly evaluates each trajectory along answer correctness and evidence-path overlap, yielding four trajectory categories with differentiated GRPO advantage scaling that suppresses shortcut reinforcement while preserving evidence-seeking behavior. For evidence-poor trajectories, a frozen gold-evidence teacher provides token-level KL guidance on reasoning and search-query tokens, excluding answer tokens to avoid direct response imitation. Experiments on six QA benchmarks across three model sizes show that PathRouter consistently improves answer F1 and evidence-path overlap, achieving average F1 gains of 3.1 on 3B and 4.9 on 7B models compared to a strong baseline.

---


### 196. [ACCORD: Action-Conditioned Contextual Grounding for Language Agents](https://arxiv.org/abs/2606.16432)

**<font color=#1a73e8>作者：</font>** Lai Jiang, Cheng Qian, Zhenhailong Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> User instructions are often underspecified because humans rely on implicit assumptions about the surrounding environment. For large language model (LLM) agents operating in information-rich digital and physical environments, these assumptions cannot be inferred from the instruction alone; they must be recovered from the current state of tools, data, interfaces, and observations. Effective execution therefore requires agents to identify missing context, ground it in observed evidence, and carry it forward into subsequent actions. We show that current agents often fail to do so. They act from assumed rather than observed specifics, overlook information they could have gathered, and fail to incorporate evidence that has already been returned. Building on this insight, we propose ACCORD (Action-Conditioned Contextual Grounding), a simple and effective agent framework for adaptive grounding. Before each action, ACCORD actively probes the environment for missing information and integrates relevant context from the agent's trajectory that would otherwise be overlooked. Requiring no additional training or task-success signals, ACCORD improves task-goal completion on AppWorld by up to +20.6 points with GPT-5-mini, from 42.0% to 62.6%, compared to strong baselines. These gains persist with a substantially stronger base model (+10.8 with Claude-4.5-sonnet), an open-weight model (+10.1 with Qwen3.5-27B-FP8), and on the embodied AlfWorld benchmark (+7.4 success rate with GPT-5-mini).

---


### 197. [SPRI: SVD-Partitioned Residual Initialization for Data-Constrained MoE Upcycling](https://arxiv.org/abs/2606.16456)

**<font color=#1a73e8>作者：</font>** Weiqiao Shan, Ruixiang Mao, Yuang Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models enable efficient scaling, but training them from scratch remains prohibitively expensive. MoE upcycling mitigates this cost by converting pretrained dense models into sparse MoE models. However, existing upcycling methods typically rely on large-scale continued training and often perform poorly under data-constrained supervised adaptation, due to either homogeneous experts or overly disruptive perturbations to pretrained parameters. In this setting, effective upcycling must leverage pretrained weight structure while introducing sufficient diversity among routed experts. To this end, we propose SVD-Partitioned Residual Initialization (SPRI), which distributes SVD-partitioned residuals derived from pretrained feed-forward network (FFN) weights across routed experts, introducing controlled expert diversity grounded in pretrained spectral structure. We further introduce a two-stage training strategy to improve adaptation stability. We evaluate SPRI on multilingual speech-to-text translation, where limited supervised data challenges MoE upcycling and multiple target languages provide natural routing heterogeneity. On CoVoST2 across 15 En-to-XX directions, SPRI improves average BLEU and COMET over fully fine-tuned dense models by 2.58 and 3.32 points, respectively, and outperforms the prior best MoE upcycling baseline by 3.39 BLEU and 4.34 COMET points.

---


### 198. [Privacy from Symmetry: Orthogonally Equivariant Transformers for LLM Inference](https://arxiv.org/abs/2606.16461)

**<font color=#1a73e8>作者：</font>** Alexander Yukhimchuk, Andrey Shulga, Mladen Kolar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Running large language models locally is often impractical, pushing inference on sensitive text to third-party providers. Split inference partially mitigates this by keeping tokens on the client and sending only hidden representations, but these representations can still be recovered via nearest-neighbor search against the public embedding table. We propose an orthogonal obfuscation procedure in which the client multiplies embeddings by a secret orthogonal matrix before transmission. To enable correct inference under arbitrary rotations, we introduce ConjFormer, a transformer variant that is exactly $\mathrm{O}(d)$-equivariant via a lightweight normalization change (scalar RMSNorm) together with blockwise orthogonal conjugation of all linear weights. As a result, the server performs the full forward pass entirely in the rotated basis and never observes unrotated hidden states. Experiments on GPT-2 and Llama 3.2 1B models fine-tuned on PubMed show that orthogonal obfuscation eliminates direct cosine nearest-neighbor inversion and reduces token recovery from over 35% top-10 to at most 1.3%, while increasing perplexity by only 0.4% after fine-tuning. These results indicate that enforcing symmetry at the architectural level can provide a practical defense for privacy-preserving LLM inference without noise injection or heavy cryptographic machinery.

---


### 199. [Tensor-Coord: Algebraic Decomposition of Joint Plan Tensors for Conflict-Free Multi-Agent LLM Planning](https://arxiv.org/abs/2606.16478)

**<font color=#1a73e8>作者：</font>** Mudit Rastogi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) remain limited in multi-agent planning because independently generated plans can create coordination failures such as spatial collisions, resource contention, and temporal deadlocks. We introduce Tensor-Coord, a multilinear algebra framework that represents the joint plan of N agents as a third-order tensor \(T \in R^{N \times H \times A}\) over agents, timesteps, and actions. Canonical Polyadic (CP) and Tucker decompositions are used to identify latent coordination structure. The minimal epsilon-approximate CP rank R* defines a computable coordination complexity measure, with \(CC(Pi)=(R*-N)/N\). We prove that R*=N is necessary and sufficient for plan independence. The residual \(E=T-T_{R*}\) defines a conflict score over agent pairs, timesteps, and actions, localizing failures without domain-specific rules. Tucker factors provide interpretable agent roles, temporal phases, and action clusters that are converted into natural language constraints for iterative LLM replanning. Experiments on multi-robot delivery tasks across Easy (2 agents, 5x5 grid), Medium (3 agents, 5x5 grid), and Hard (4 agents, 5x5 grid) settings show convergence to conflict-free plans in 100% of 2-agent cases within 1.4 iterations on average, 80% of 3-agent cases within 3.2 iterations, and 60% of 4-agent cases within 4.0 iterations. CP rank scaled approximately linearly as \(R*(N) = 3.9N + 0.5\), supporting its use as a predictor of coordination complexity.

---


### 200. [Steering Emotional Dynamics for Art Therapy: Controllable Narrative Script Generation through Hierarchically Guided LLM Agents](https://arxiv.org/abs/2606.16481)

**<font color=#1a73e8>作者：</font>** Suqing Wang, Qinghai Miao, Chao Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Art therapy plays a vital role in emotional healing, in which narrative creation acts as the primary vehicle for emotional expression. Given the inherently dynamic nature of emotions during healing, narratives with finely controlled emotional fluctuations enable individuals to safely project inner conflicts and achieve emotional catharsis. Recently, with the rapid development of Large Language Models (LLMs), automated narrative generation technology has provided a new pathway to support such artistic designs. However, while existing methods can produce fluent texts, they struggle to generate narratives that adhere to specified affective trajectories, failing to meet the demands of emotion-oriented psychological healing. To address these issues, this paper proposes EC-Script, an LLM agent-based framework that enables hierarchical control of the affective trajectory in narrative generation for emotional healing. To ensure that the generated narratives strictly follow the given emotional patterns, EC-Script establishes overall narrative direction through Emotion-Trajectory Planning, propels scene-level plot development with Character-Driven Scene Generation, and regulates local emotional changes of characters via Emotion-Controlled Script Writing. Ultimately, it outputs scene-by-scene script content that remains highly consistent with the preset affective trajectory. Experimental results demonstrate that EC-Script significantly outperforms baseline methods in affective trajectory adherence, exhibiting excellent and reliable emotional controllability, thereby providing effective technical support for AI-assisted emotional healing scenarios.

---


> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-270](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
