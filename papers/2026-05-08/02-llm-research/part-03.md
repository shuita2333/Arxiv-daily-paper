# 🧠 大模型相关研究 | 2026年05月08日

> 本类共 **126** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-126**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-126**

---

### 101. [Self-Induced Outcome Potential: Turn-Level Credit Assignment for Agents without Verifiers](https://arxiv.org/abs/2605.04984)

**<font color=#1a73e8>作者：</font>** Senkang Hu, Yong Dai, Xudong Han 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon LLM agents depend on intermediate information-gathering turns, yet training feedback is usually observed only at the final answer, because process-level rewards require high-quality human annotation. Existing turn-level shaping methods reward turns that increase the likelihood of a gold answer, but they require answer supervision or stable task-specific verifiers. Conversely, label-free RL methods extract self-signals from output distributions, but mainly at the answer or trajectory level and therefore cannot assign credit to intermediate turns. We propose Self-Induced Outcome Potential (SIOP), which treats semantic clusters of final answers as latent future outcome states for potential-based turn-level credit assignment. For each query, SIOP samples multiple rollouts, clusters final answers into semantic outcome modes, and builds a reliability-aware target distribution over these states. It then rewards turns for increasing posterior support for reliable future states using a tractable cluster-level approximation. The objective generalizes information-potential shaping from gold-answer supervision to settings without task-specific gold verifiers while avoiding the broadcasted rollout-level advantages used by standard GRPO. We formalize the framework, characterize its supervised gold-answer limit, and show that SIOP improves average performance over verifier-free outcome-level baselines on seven search-augmented agentic reasoning benchmarks while approaching a gold-supervised outcome baseline. Code is available at this https URL.

---


### 102. [Low-Rank Adaptation of Geospatial Foundation Models for Wildfire Mapping Using Sentinel-2 Data](https://arxiv.org/abs/2605.04989)

**<font color=#1a73e8>作者：</font>** Ali Shibli, Andrea Nascetti, Yifang Ban  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wildfire burned-area mapping is essential for damage assessment, emissions modeling, and understanding fire-climate interactions across diverse ecological regions. Recent geospatial foundation models provide strong general-purpose representations for satellite imagery, yet there is still no clear understanding of how to efficiently adapt these models for downstream Earth observation tasks, particularly under geographic and temporal domain shift. This study evaluates three state-of-the-art Geospatial Foundation Models (GFMs) - Terramind, DINOv3, and Prithvi-v2 - for burned-area mapping across the United States and Canada using Sentinel-2 data. Leveraging 3,820 wildfire events from 2017-2023, we conduct spatial and temporal generalization tests across diverse biomes. We systematically compare full fine-tuning, decoder-only fine-tuning, and Low-Rank Adaptation (LoRA) for adapting each model. Across all experiments, LoRA provides the strongest cross-domain generalization while updating less than 1% of parameters, demonstrating a favorable trade-off between accuracy and efficiency. Prithvi-v2 with LoRA achieves the highest overall accuracy and the largest improvement compared to full fine-tuning. These findings indicate that geospatial foundation models, when adapted using lightweight parameter-efficient methods such as LoRA, offer a robust and scalable solution for large-scale burned-area mapping. Code is available at this https URL.

---


### 103. [Adaptivity Under Realizability Constraints: Comparing In-Context and Agentic Learning](https://arxiv.org/abs/2605.04995)

**<font color=#1a73e8>作者：</font>** Anastasis Kratsios, A. Martina Neuman, Philipp Petersen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We compare in-context learning with fixed queries and agentic learning with adaptive queries for uniform approximation of task families. We consider two settings: an unrestricted regime, where querying and approximation are arbitrary functions, and a realizable regime, where we require these operations to be implemented by ReLU neural networks. In both settings, adaptivity never hinders approximation performance. However, this advantage can change when one passes from the unrestricted regime to the realizable regime. We identify four distinct approximation scenarios, each witnessed by an explicit task family: (a) no advantage of adaptivity; (b) an advantage in the unrestricted regime that persists under ReLU realizability; (c) an advantage that arises only under realizability; and (d) an advantage that disappears under realizability. This demonstrates that representational constraints interact profoundly with the effect of adaptivity.

---


### 104. [Tailoring Scaffolding to Diagnostic Strategies: Theory-Informed LLM-Based Agents](https://arxiv.org/abs/2605.04996)

**<font color=#1a73e8>作者：</font>** Fatma Betul Gures, Tanya Nazaretsky, Tanja Kaser  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Learning analytics systems increasingly integrate large language models (LLMs) to provide adaptive scaffolding in complex learning environments, yet personalization is often driven by global instructional choices rather than principled alignment with learning theory, limiting effectiveness and pedagogical grounding. In prior work, we examined how structuring and problematizing scaffolding approaches can be instantiated through LLM agents in a scenario-based learning environment for diagnostic reasoning. While both approaches supported learning, we observed systematic differences in learner interaction patterns and clear tendencies indicating that different diagnostic strategies benefited from distinct forms of scaffolding. Building on these findings, we propose a theory-informed scaffolding design grounded in the Knowledge Learning Instruction (KLI) framework, as different diagnostic strategies target different types of knowledge and require different instructional mechanisms. We use KLI to guide the alignment between strategy demands and scaffolding approaches and introduce a KLI-informed hybrid LLM agent that adapts its pedagogical support according to the diagnostic strategy being practiced, rather than applying a single global scaffolding approach. We hypothesize that this design could enable better learning gains.

---


### 105. [Misaligned by Reward: Socially Undesirable Preferences in LLMs](https://arxiv.org/abs/2605.05003)

**<font color=#1a73e8>作者：</font>** Gayane Ghazaryan, Esra Dönmez  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reward models are a key component of large language model alignment, serving as proxies for human preferences during training. However, existing evaluations focus primarily on broad instruction-following benchmarks, providing limited insight into whether these models capture socially desirable preferences. As a result, important failures in social alignment can remain hidden.
We extend reward-model benchmarking to four socially consequential domains: bias, safety, morality, and ethical reasoning. We introduce a framework that converts social evaluation datasets into pairwise preference data, leveraging gold labels where available and directional bias indicators otherwise. This enables us to test whether reward models prefer socially undesirable responses, and whether their preferences produce systematically biased distributions over selected outputs.
Across five publicly available reward models and two instruction-tuned models used as reward proxies, we find substantial variation across domains, with no single model performing best overall. The models fall well short of strong social intelligence: they often prefer socially undesirable options, and their preferences produce systematically biased distributions. Moreover, stronger bias avoidance can reduce sensitivity to context, revealing a key alignment trade-off between avoiding biased outcomes and preserving contextual faithfulness. These findings show that standard reward benchmarks are insufficient for assessing social alignment and highlight the need for evaluations that directly measure the social preferences encoded in reward models.

---


### 106. [Uno-Orchestra: Parsimonious Agent Routing via Selective Delegation](https://arxiv.org/abs/2605.05007)

**<font color=#1a73e8>作者：</font>** Zhiqing Cui, Haotong Xie, Jiahao Yuan 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) multi-agent systems typically rely on rigid orchestration, committing either to flat per-query routing or to hand-engineered task decomposition, so decomposition depth, worker choice, and inference budget are not jointly optimized under one objective. We introduce Uno-Orchestra, a unified orchestration policy that selectively decomposes a task and dispatches each subtask to an admissible (model, primitive) pair, with both decisions learned together from curated RL trajectories grounded in real worker interactions. Against 22 baselines on a 13-benchmark suite spanning math, code, knowledge, long-context, and agentic tool-use, Uno-Orchestra reaches 77.0% macro pass@1, roughly 16% above the strongest workflow baseline, at roughly an order of magnitude lower per-query cost, advancing the accuracy-efficiency frontier of selective delegation.

---


### 107. [CuBridge: An LLM-Based Framework for Understanding and Reconstructing High-Performance Attention Kernels](https://arxiv.org/abs/2605.05023)

**<font color=#1a73e8>作者：</font>** Xing Ma, Yangjie Zhou, Wu Sun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficient CUDA implementations of attention mechanisms are critical to modern deep learning systems, yet supporting diverse and evolving attention variants remains challenging. Existing frameworks and compilers trade performance for flexibility, while expert-written kernels achieve high efficiency but are difficult to adapt. Recent work explores large language models (LLMs) for GPU kernel generation, but prior studies report unstable correctness and significant performance gaps for complex operators such as attention.
We present CuBridge, an LLM-based framework that adapts expert-written attention kernels through a structured lift-transfer-lower workflow. CuBridge starts from expert-written CUDA attention kernels and lifts them into an executable intermediate representation that makes execution orchestration explicit while abstracting low-level CUDA syntax. Given a user-provided PyTorch specification, CuBridge generates and verifies a target IR program, then reconstructs optimized CUDA code via reference-guided lowering. Across diverse attention variants and GPU platforms, CuBridge consistently produces correct kernels and substantially outperforms general frameworks, compiler-based approaches, and prior LLM-based methods.

---


### 108. [Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals](https://arxiv.org/abs/2605.05025)

**<font color=#1a73e8>作者：</font>** Gijs van Dijk  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose a lightweight and single-pass uncertainty quantification method for detecting hallucinations in Large Language Models. The method uses attention matrices to estimate uncertainty without requiring repeated sampling or external models. Specifically, we measure the Kullback-Leibler divergence between each attention head's distribution and a uniform reference distribution, and use these features in a logistic regression probe. Across multiple datasets, task types, and model families, attention divergence is highly predictive of answer correctness and performs competitively with existing uncertainty estimation methods. We find that this signal is concentrated in middle layers and on factual tokens such as named entities and numbers, suggesting that attention dynamics provides an efficient and interpretable white-box signal of model uncertainty.

---


### 109. [When Relations Break: Analyzing Relation Hallucination in Vision-Language Model Under Rotation and Noise](https://arxiv.org/abs/2605.05045)

**<font color=#1a73e8>作者：</font>** Philip Wootaek Shin, Ajay Narayanan Sridhar, Sivani Devarapalli 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) achieve strong multimodal performance but remain prone to relation hallucination, which requires accurate reasoning over inter-object interactions. We study the impact of visual perturbations, specifically rotation and noise, and show that even mild distortions significantly degrade relational reasoning across models and datasets. We further evaluate prompt-based augmentation and preprocessing strategies (orientation correction and denoising), finding that while they offer partial improvements, they do not fully resolve hallucinations. Our results reveal a gap between perceptual robustness and relational understanding, highlighting the need for more robust, geometry-aware VLMs.

---


### 110. [Full-chip CMP modelling based on Fully Convolutional Network leveraging White Light Interferometry](https://arxiv.org/abs/2605.05062)

**<font color=#1a73e8>作者：</font>** Jules Exbrayat, Renan Bouis, Elie Sezestre 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As time-to-market is crucial in the Integrated Circuit (IC) industry, speeding up layout manufacturability verifi-cation is essential. Chemical-Mechanical Polishing (CMP) plays a vital role in IC fabrication but is significantly influenced by Layout-Dependent Effects (LDE). An accurate and efficient CMP model enables design teams to correct surface unevenness before fabrication, reducing costs and accelerating the design phase. However, existing models often rely on Density Step Height (DSH) modeling, which is time-consuming for calibration and requires substantial hardware resources for fine-grained predictions. In this paper, we propose combining the advantages of two surface analysis techniques, White Light Interfer-ometry (WLI) and Atomic Force Microscopy (AFM), to train a deep learning model. This model aims to predict full-chip post-CMP nanotopography with nanometer-scale accuracy. Our deep learning model is based on a Convolutional Neural Network (CNN) and follows a two-step pipeline. The model is trained on each technique separately, resulting in a detailed full-chip CMP model.

---


### 111. [The Pinocchio Dimension: Phenomenality of Experience as the Primary Axis of LLM Psychometric Differences](https://arxiv.org/abs/2605.05080)

**<font color=#1a73e8>作者：</font>** Hubert Plisiecki, Sabina Siudaj, Kacper Dudzic 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We administer 45 validated psychometric questionnaires to 50 large language models (LLMs) to identify the dimensions along which LLMs differ psychometrically. Using Supervised Semantic Differential (SSD), we find that the primary axis of between-model variance separates items describing phenomenally rich experience, including embodied sensation, felt affect, inner speech, imagery, and empathy, from items describing stimulus-driven behavioral reactivity ($R^2_{adj}=.037$, $p<.0001$). To test this hypothesis at the item level, we introduce the Pinocchio score ($\pi_i$), the ratio of inter-model response variance under neutral prompting to that under a human-simulation prompt, as an annotation-free measure of each item's experiential demand. $\pi_i$ predicts condition-induced shifts in primary factor loading magnitudes ($\rho=-.215$, $p<.0001$, $n=1292$--$1310$ items), confirming that between-model divergence on experiential items is structured rather than noisy. Applying PCA to per-model EFA scores across all questionnaires reveals one dominant dimension, the Pinocchio Axis ($\Pi$): the degree to which a model presents itself as a locus of phenomenal experience rather than a system of behavioral responses. This axis captures 47.1% of cross-questionnaire between-model variance in primary factor scores and converges with item-level Pinocchio scores ($r=.864$). Marked within-provider divergence across closely related model variants is consistent with post-training fine-tuning as a key contributor, supporting the interpretation that $\Pi$ reflects a training-shaped self-representational tendency governing how a model treats experiential language as self-applicable. The dominant axis of between-model psychometric variation is therefore not a conventional personality trait but a self-representational stance toward one's own nature as an experiencer.

---


### 112. [Gated Multimodal Learning for Interpretable Property Energy Performance Prediction and Retrofit Scenario Analysis](https://arxiv.org/abs/2605.05088)

**<font color=#1a73e8>作者：</font>** Yunfei Bai, Aaron Tesfa Tsion, Raul Rosales 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Achieving resilient and sustainable cities requires scalable approaches to decarbonising residential buildings, which account for about 20% of UK greenhouse gas emissions and 25% of energy-related emissions in the European Union. Energy Performance Certificates (EPCs) support regulation and retrofit planning, but their reliance on on-site inspections limits timely city-scale assessment. This study introduces a gated multimodal model to predict Standard Assessment Procedure (SAP) energy efficiency and Environmental Impact (EI) scores by integrating EPC tabular variables, assessor-written free text, and Geographic Information System (GIS)-derived spatial features describing footprint geometry, height, area, and orientation. Sample-wise gating learns property-specific modality weights, while an auxiliary band classification head stabilises training. In a Westminster, London case study, the model predicts SAP and EI scores with MAEs of 4.03 and 4.76 points and R2 values of 0.757 and 0.748, respectively, achieving a mean MAE of 4.39. Ablation results show that full multimodal fusion outperforms unimodal and bimodal baselines for both score prediction and band-level classification. Interpretability analyses provide decision-relevant evidence: gating weights indicate strong reliance on assessor text; SHAP highlights main fuel, built form, and construction age band; text occlusion prioritises roof and wall fields; and spatial attribution is dominated by height and footprint area, with sensitivity to footprint shape. The validated framework is further applied to retrofit scenarios for wall insulation, roof insulation, and window glazing upgrades, indicating projected improvements in SAP, EI, annual energy cost, and equivalent CO2 emissions. Overall, the framework provides scalable property-level evidence for retrofit screening, intervention prioritisation, and net-zero housing transitions.

---


### 113. [Automatically Finding and Validating Unexpected Side-Effects of Interventions on Language Models](https://arxiv.org/abs/2605.05090)

**<font color=#1a73e8>作者：</font>** Quintin Pope, Ajay Hayagreeve Balaji, Jacques Thibodeau 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present an automated, contrastive evaluation pipeline for auditing the behavioral impact of interventions on large language models. Given a base model $M_1$ and an intervention model $M_2$, our method compares their free-form, multi-token generations across aligned prompt contexts and produces human-readable, statistically validated natural-language hypotheses describing how the models differ, along with recurring themes that summarize patterns across validated hypotheses.
We evaluate the approach in synthetic setting by injecting known behavioral changes and showing that the pipeline reliably recovers them. We then apply it to three real-world interventions, reasoning distillation, knowledge editing and unlearning, demonstrating that the method surfaces both intended and unexpected behavioral shifts, distinguishes large from subtle interventions, and does not hallucinate differences when effects are absent or misaligned with the prompt bank. Overall, the pipeline provides a statistically grounded and interpretable tool for post-hoc auditing of intervention-induced changes in model behavior.

---


### 114. [Continual Knowledge Updating in LLM Systems: Learning Through Multi-Timescale Memory Dynamics](https://arxiv.org/abs/2605.05097)

**<font color=#1a73e8>作者：</font>** Andreas Pattichis, Constantine Dovrolis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLMs are trained once, then deployed into a world that never stops changing. External memory compensates for this, but most systems manage it explicitly rather than letting it adapt on its own. Biological memory works differently: coupled multi-timescale dynamics make new associations immediately usable, strengthen what repetition confirms, and let the rest fade. We argue that external memory should follow a similar principle. In Memini, this view takes the form of an associative memory that organizes knowledge as a directed graph. Each edge carries two coupled internal variables, one fast and one slow, following the Benna-Fusi model of synaptic consolidation. From this coupling, episodic sensitivity, gradual consolidation, and selective forgetting emerge as facets of a single mechanism, reframing external memory as a learning substrate that reorganizes through its own dynamics.

---


### 115. [On the Hardness of Junking LLMs](https://arxiv.org/abs/2605.05116)

**<font color=#1a73e8>作者：</font>** Marco Rando, Samuel Vaiter  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are known to be vulnerable to jailbreak attacks, which typically rely on carefully designed prompts containing explicit semantic structure. These attacks generally operate by fixing an adversarial instruction and optimizing small adversarial components (e.g., suffixes or prefixes). In this setting, prompt structure is fundamental for performance, and recent results show that even simple random search can achieve strong performance when combined with sophisticated prompt design. Recently, it has been observed that harmful behaviors can be elicited even without the adversarial prompt, relying solely on optimized token sequences. This suggests the existence of natural backdoors, i.e., token sequences naturally emerged during LLMs training that trigger unsafe outputs without any meaningful instruction. However, despite these observations, this setting remains largely unexplored, and in particular the hardness of finding natural backdoors has not been assessed yet. In this work, we provide a first proof-of-concept study investigating the hardness of this task, which we refer to as the junking problem. We formalize it as the problem of finding token sequences that maximize the probability of generating a target prefix of harmful responses, propose a greedy random-search method to assess is such sequences can be discovered easily. Our results show that this problem is harder than standard jailbreak attacks, confirming the importance of semantic information in prompt design. At the same time, we find that our simple strategy is sufficient to solve it with a high success rate, suggesting that natural backdoors are present and easily recoverable. Finally, through perplexity analysis, we observe that the discovered token sequences lie in low-probability regions of the model distribution, supporting the hypothesis that they emerged implicitly from the training process.

---


### 116. [Physiologically Grounded Driver Behavior Classification: SHAP-Driven Elite Feature Selection and Hybrid Gradient Boosting for Multimodal Physiological Signals](https://arxiv.org/abs/2605.05120)

**<font color=#1a73e8>作者：</font>** Sahar Askari, Mohammad Mahdi Mirza Ali Mohammadi, Fatemeh Ensafdoust 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An interpretable and scalable framework for decoding driving behaviors from multimodal physiological signals is proposed in this study. We utilize multimodal physiological driving behavior large-scale dataset comprising synchronized electroencephalogram (EEG), electromyography (EMG), and galvanic skin response (GSR) signals. Our approach involves rigorous preprocessing followed by a domain-specific feature extraction pipeline targeting time-domain, frequency-domain, and derived physiological indices. To address high dimensionality, we employ SHAP-based elite feature selection, retaining the top 250 features to reduce computational overhead while preserving predictive power. Hyperparameter optimization for extreme gradient boosting (XGBoost) and light gradient boosting machine (LightGBM) models is conducted using Bayesian optimization via Optuna. Finally, a weighted soft-voting ensemble is constructed to leverage the complementary strengths of both gradient boosting frameworks. The results demonstrate that the proposed ensemble achieves a test accuracy of 80.91% and a macro-F1 score of 0.79, significantly outperforming single-modality baselines and traditional machine learning models. Ablation studies confirm an 8% performance gain over the best single modality (EEG), validating the necessity of multimodal fusion. SHAP analysis further validates the physiological plausibility of the model, revealing that the EEG contributes the majority of predictive weight, GSR and EMG features provide critical discriminatory signals for high-arousal and motor-intensive maneuvers.

---


### 117. [Adaptive Policy Selection and Fine-Tuning under Interaction Budgets for Offline-to-Online Reinforcement Learning](https://arxiv.org/abs/2605.05123)

**<font color=#1a73e8>作者：</font>** Alper Kamil Bozkurt, Xiaoan Xu, Shangtong Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In offline-to-online reinforcement learning (O2O-RL), policies are first safely trained offline using previously collected datasets and then further fine-tuned for tasks via limited online interactions. In a typical O2O-RL pipeline, candidate policies trained with offline RL are evaluated via either off-policy evaluation (OPE) or online evaluation (OE). The policy with the highest estimated value is then deployed and continually fine-tuned. However, this setup has two main issues. First, OPE can be unreliable, making it risky to deploy a policy based solely on those estimates, whereas OE may identify a viable policy with substantial online interaction, which could have been used for fine-tuning. Second--and more importantly--it is also often not possible to determine a priori whether a pretrained policy will improve with post-deployment fine-tuning, especially in non-stationary environments. As a result, procedures committing to a single deployed policy are impractical in many real-world settings. Moreover, a naive remedy that exhaustively fine-tunes all candidates would violate interaction budget constraints and is likewise infeasible. In this paper, we propose a novel adaptive approach for policy selection and fine-tuning under online interaction budgets in O2O-RL. Following the standard pipeline, we first train a set of candidate policies with different offline RL algorithms and hyperparameters; we then perform OPE to obtain initial performance estimates. We next adaptively select and fine-tune the policies based on their predicted performance via an upper-confidence-bound approach thereby making efficient use of online interactions. We demonstrate that our approach improves upon O2O-RL baselines with various benchmarks.

---


### 118. [Joint Treatment Effect Estimation from Incomplete Healthcare Data: Temporal Causal Normalizing Flows with LLM-driven Evolutionary MNAR Imputation](https://arxiv.org/abs/2605.05125)

**<font color=#1a73e8>作者：</font>** Olivia Jullian Parra, Sara Zoccheddu, David Catalan Cerezo 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Target trial emulation (TTE) enables causal questions to be studied with observational data when randomized controlled trials (RCTs) are infeasible. Yet treatment-effect methods often address causal estimation, missingness, and temporal structure separately, limiting their robustness in electronic health records (EHRs), where time-varying confounding and missing-not-at-random (MNAR) biomarkers can reach 50%--80%. We propose a two-stage pipeline for treatment effect estimation from incomplete longitudinal EHRs. First, CausalFlow-T, a directed acyclic graph (DAG)-constrained normalizing flow with long short-term memory (LSTM)-encoded patient history, performs exact invertible counterfactual inference, avoiding approximation errors from variational inference and separating confounding through explicit causal structure. Ablations on four synthetic and one semi-synthetic benchmark with known counterfactuals show that DAG constraints and exact inference address distinct failure modes: neither compensates for the other. Second, because CausalFlow-T requires completed inputs, we introduce an LLM-driven evolutionary imputer that proposes executable imputation operators rather than individual entries, and evaluate it with three large language model (LLM) backends, including two open-source models. Across 30%--80% MNAR missingness, this imputer achieves the best pooled rank over biomarker and causal metrics, leading in point-wise accuracy and temporal extrapolation while preserving average treatment effect (ATE) recovery as statistical baselines degrade. On Swiss primary-care EHRs from adults with type 2 diabetes initiating a GLP-1 receptor agonist or SGLT-2 inhibitor, the pipeline estimates a per-protocol weight-loss difference of -0.98 kg [95% CI -1.01, -0.96] favoring GLP-1 receptor agonists, consistent with randomized evidence and obtained from realistically incomplete real-world EHRs.

---


### 119. [Low-Cost Black-Box Detection of LLM Hallucinations via Dynamical System Prediction](https://arxiv.org/abs/2605.05134)

**<font color=#1a73e8>作者：</font>** Dan Wilson, Mohamed Akrout  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) frequently generate plausible but non-factual content, a phenomenon known as hallucination. While existing detection methods typically rely on computationally expensive sampling-based consistency checks or external knowledge retrieval, we propose a new method that treats the LLM as a black-box dynamical system. By projecting LLM responses into a high-dimensional manifold via an embedding model, we characterize the resulting vector sequences as observable realizations of the model's latent state-space dynamics. Leveraging Koopman operator theory, we fit the transition operators for both factual and hallucinated regimes and define a differential residual score based on their respective prediction errors. To accommodate varying user requirements and domain-specific sensitivities, we introduce a preference-aware calibration mechanism that optimizes the classification threshold based on a small set of demonstrations. This approach enables low-cost hallucination detection in a single-sample pass, avoiding the need for secondary sampling or external grounding. Extensive testing across three data benchmarks demonstrates that our method achieves state-of-the-art performance with reduced resource overhead.

---


### 120. [Executable World Models for ARC-AGI-3 in the Era of Coding Agents](https://arxiv.org/abs/2605.05138)

**<font color=#1a73e8>作者：</font>** Sergey Rodionov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We evaluate an initial coding-agent system for ARC-AGI-3 in which the agent maintains an executable Python world model, verifies it against previous observations, refactors it toward simpler abstractions as a practical proxy for an MDL-like simplicity bias, and plans through the model before acting. The system is intentionally direct: it uses a scripted controller, predefined world-model interfaces, verifier programs, and a plan executor, but no hand-coded game-specific logic. We report results on the 25 public ARC-AGI-3 games. Each recorded playthrough uses a fresh agent instance with no access to previous playthrough-specific files or conversation state. Most games have a single recorded playthrough; for a few games, we report multiple independent fresh-agent playthroughs to expose run-to-run variability. The agent fully solved 7 games, achieved a Relative Human Action Efficiency greater than 75%, on 6 games, and obtained a mean per-game RHAE of 32.58%. Because the system uses no game-specific code, it can serve as a game-general baseline for ARC-AGI-3. Performance on the private validation set remains to be tested. Overall, the results provide preliminary evidence that verifier-driven executable world models are a promising approach for ARC-AGI-3 agents.

---


### 121. [PSK at SemEval-2026 Task 9: Multilingual Polarization Detection Using Ensemble Gemma Models with Synthetic Data Augmentation](https://arxiv.org/abs/2605.05159)

**<font color=#1a73e8>作者：</font>** Srikar Kashyap Pulipaka  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present our system for SemEval-2026 Task 9: Multilingual Polarization Detection, a binary classification task spanning 22 languages. Our approach fine-tunes separate Gemma~3 models (12B and 27B parameters) per language using Low-Rank Adaptation (LoRA), augmented with synthetic data generated by a large language model (LLM). We employ three synthetic data strategies (direct generation, paraphrasing, and contrastive pair creation) using GPT-4o-mini, with a multi-stage quality filtering pipeline including embedding-based deduplication. We find that per-language threshold tuning on the development set yields 2 to 4\% F1 improvements without retraining. We also use weighted ensembles of 12B and 27B model predictions with per-language strategy selection. Our final system achieves a mean macro-F1 of 0.811 across all 22 languages, ranking 2nd overall of the participating teams, with 1st place finishes in 3 languages and top-3 in 8 languages. We also find that alternative architectures (XLM-RoBERTa, Qwen3) that showed strong development set performance suffered 30 to 50\% F1 drops on the test set, highlighting the importance of generalization.

---


### 122. [Wasserstein-Aligned Localisation for VLM-Based Distributional OOD Detection in Medical Imaging](https://arxiv.org/abs/2605.05161)

**<font color=#1a73e8>作者：</font>** Bernhard Kainz, Johanna P Mueller, Matthew Baugh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot anomaly localisation via vision-language models (VLMs) offers a compelling approach for rare pathology detection, yet its performance is fundamentally limited by the absence of healthy anatomical context. We reformulate zero-shot localisation as a comparative inference problem in which anomalies are identified through structured comparison against reference distributions of normal anatomy. We introduce WALDO, a training-free framework grounded in optimal transport theory that enables comparative reasoning through: (i) entropy-weighted Sliced Wasserstein distances for anatomically-aware reference selection from DINOv2 patch distributions, (ii) Goldilocks zone sampling exploiting the non-monotonic relationship between reference similarity and localisation accuracy, and (iii) self-consistency aggregation via weighted non-maximum suppression. We theoretically analyse the Goldilocks effect through distributional divergence, and show that references with moderate similarity minimize a bias-variance trade-off in comparative visual reasoning. On the NOVA brain MRI benchmark, WALDO with Qwen2.5-VL-72B achieves $43.5_{\pm1.6}\%$ mAP@30 (95\% CI: [40.4, 46.7]), representing a 19\% relative improvement over zero-shot baselines. Cross-model evaluation shows consistent gains: GPT-4o achieves $32.0_{\pm6.5}\%$ and Qwen3-VL-32B achieves $32.0_{\pm6.6}\%$ mAP@30. Paired McNemar tests confirm statistical significance ($p<0.01$). Source code is available at this https URL .

---


### 123. [Understanding In-Context Learning for Nonlinear Regression with Transformers: Attention as Featurizer](https://arxiv.org/abs/2605.05176)

**<font color=#1a73e8>作者：</font>** Alexander Hsu, Zhaiming Shen, Wenjing Liao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pre-trained transformers are able to learn from examples provided as part of the prompt without any weight updates, a remarkable ability known as in-context learning (ICL). Despite its demonstrated efficacy across various domains, the theoretical understanding of ICL is still developing. Whereas most existing theory has focused on linear models, we study ICL in the nonlinear regression setting. Through the interaction mechanism in attention, we explicitly construct transformer networks to realize nonlinear features, such as polynomial or spline bases, which span a wide class of functions. Based on this construction, we establish a framework to analyze end-to-end in-context nonlinear regression with the constructed features. Our theory provides finite-sample generalization error bounds in terms of context length and training set size. We numerically validate the theory on synthetic regression tasks.

---


### 124. [OpenSearch-VL: An Open Recipe for Frontier Multimodal Search Agents](https://arxiv.org/abs/2605.05185)

**<font color=#1a73e8>作者：</font>** Shuang Chen, Kaituo Feng, Hangting Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep search has become a crucial capability for frontier multimodal agents, enabling models to solve complex questions through active search, evidence verification, and multi-step reasoning. Despite rapid progress, top-tier multimodal search agents remain difficult to reproduce, largely due to the absence of open high-quality training data, transparent trajectory synthesis pipelines, or detailed training recipes. To this end, we introduce OpenSearch-VL, a fully open-source recipe for training frontier multimodal deep search agents with agentic reinforcement learning. First, we curated a dedicated pipeline to construct high-quality training data through Wikipedia path sampling, fuzzy entity rewriting, and source-anchor visual grounding, which jointly reduce shortcuts and one-step retrieval collapse. Based on this pipeline, we curate two training datasets, SearchVL-SFT-36k for SFT and SearchVL-RL-8k for RL. Besides, we design a diverse tool environment that unifies text search, image search, OCR, cropping, sharpening, super-resolution, and perspective correction, enabling agents to combine active perception with external knowledge acquisition. Finally, we propose a multi-turn fatal-aware GRPO training algorithm that handles cascading tool failures by masking post-failure tokens while preserving useful pre-failure reasoning through one-sided advantage clamping. Built on this recipe, OpenSearch-VL delivers substantial performance gains, with over 10-point average improvements across seven benchmarks, and achieves results comparable to proprietary commercial models on several tasks. We will release all data, code, and models to support open research on multimodal deep search agents.

---


### 125. [LoViF 2026 The First Challenge on Holistic Quality Assessment for 4D World Model (PhyScore)](https://arxiv.org/abs/2605.05187)

**<font color=#1a73e8>作者：</font>** Wei Luo, Yiting Lu, Xin Li 等 35 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper reports on the LoViF 2026 PhyScore challenge, a competition on holistic quality assessment of world-model-generated videos across both 2D and 4D generation settings. The challenge is motivated by a central gap in current evaluation practice: perceptual quality alone is insufficient to judge whether generated dynamics are physically plausible, temporally coherent, and consistent with input conditions. Participants are required to build a metric that jointly predicts four dimensions, i.e., Video Quality, Physical Realism, Condition-Video Alignment, and Temporal Consistency. Depart from that, participants also need to localize physical anomaly timestamps for fine-grained diagnosis.
The benchmark dataset contains 1,554 videos generated by seven representative world generative models, organized into three tracks (text-2D, image-to-4D, and video-to-4D) and spanning 26 categories. These categories explicitly cover physics-relevant scenarios, including dynamics, optics, and thermodynamics, together with diverse real-world and creative content. To ensure label reliability, scores and anomaly timestamps are produced through trained human annotation with an additional automated quality-control pass.
Evaluation is based on both score prediction and anomaly localization, with a composite protocol that combines TimeStamp_IOU and SRCC/PLCC. This report summarizes the challenge design and provides method-level insights from submitted solutions.

---


### 126. [Implicit Representations of Grammaticality in Language Models](https://arxiv.org/abs/2605.05197)

**<font color=#1a73e8>作者：</font>** Yingshan Susan Wang, Linlu Qiu, Zhaofeng Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Grammaticality and likelihood are distinct notions in human language. Pretrained language models (LMs), which are probabilistic models of language fitted to maximize corpus likelihood, generate grammatically well-formed text and discriminate well between grammatical and ungrammatical sentences in tightly controlled minimal pairs. However, their string probabilities do not sharply discriminate between grammatical and ungrammatical sentences overall. But do LMs implicitly acquire a grammaticality distinction distinct from string probability? We explore this question through studying internal representations of LMs, by training a linear probe on a dataset of grammatical and (synthetic) ungrammatical sentences obtained by applying perturbations to a naturalistic text corpus. We find that this simple grammaticality probe generalizes to human-curated grammaticality judgment benchmarks and outperforms LM probability-based grammaticality judgments. When applied to semantic plausibility benchmarks, in which both members of a minimal pair are grammatical and differ in only plausibility, the probe however performs worse than string probability. The English-trained probe also exhibits nontrivial cross-lingual generalization, outperforming string probabilities on grammaticality benchmarks in numerous other languages. Additionally, probe scores correlate only weakly with string probabilities. These results collectively suggest that LMs acquire to some extent an implicit grammaticality distinction within their hidden layers.

---


> [!TIP]
> 当前位于：**101-126**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-126**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
