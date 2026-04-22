# 🧠 大模型相关研究 | 2026年04月23日

> 本类共 **132** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-132](./part-03.md)

---

### 1. [Compile to Compress: Boosting Formal Theorem Provers by Compiler Outputs](https://arxiv.org/abs/2604.18587)

**<font color=#1a73e8>作者：</font>** Guchan Li, Rui Tian, Hongning Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated significant potential in formal theorem proving, yet state-of-the-art performance often necessitates prohibitive test-time compute via massive roll-outs or extended context windows. In this work, we address this scalability bottleneck by exploiting an informative structure in formal verification: the observation that compilers map a vast space of diverse proof attempts to a compact set of structured failure modes. We introduce a learning-to-refine framework that leverages this compression to perform efficient learning and proof exploration. We perform tree search that corrects errors locally conditioned on explicit verifier feedback, thereby circumventing the costs associated with accumulating a long history of proof attempts. Extensive evaluations show that our method consistently amplifies the reasoning capabilities of base provers across varying scales. Notably, our approach achieves state-of-the-art performance on PutnamBench among publicly reported $\sim$8B and $\sim$32B parameter models under comparable test-time budgets, offering a scalable paradigm for next-generation verifier-guided reasoning.

---


### 2. [Two-dimensional early exit optimisation of LLM inference](https://arxiv.org/abs/2604.18592)

**<font color=#1a73e8>作者：</font>** Jan Hůla, David Adamczyk, Tomáš Filip 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce a two-dimensional (2D) early exit strategy that coordinates layer-wise and sentence-wise exiting for classification tasks in large language models. By processing input incrementally sentence-by-sentence while progressively activating deeper layers, our method achieves multiplicative computational savings that exceed those from optimizing either dimension independently. Experimental evaluation across four state-of-the-art LLMs (Llama 3.1, Llama 3.2, Gemma, Qwen; 3B-8B parameters) on three sentiment classification datasets demonstrates additional speed-ups of 1.4--2.3$\times$ over optimal layer-wise early exit for simpler tasks with vanilla models, with graceful degradation on complex multi-class problems. Fine-tuning reduces but does not eliminate this advantage. The approach is model-agnostic, requires only lightweight classification adapters, and is orthogonal to complementary efficiency methods such as quantization and pruning. Our findings indicate that 2D early exit strategies excel when semantic information accumulates predictably across input structure, suggesting possible applicability to sequence-processing tasks beyond sentiment classification.

---


### 3. [Easy Samples Are All You Need: Self-Evolving LLMs via Data-Efficient Reinforcement Learning](https://arxiv.org/abs/2604.18639)

**<font color=#1a73e8>作者：</font>** Zhiyin Yu, Bo Zhang, Qibin Hou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Previous LLMs-based RL studies typically follow either supervised learning with high annotation costs, or unsupervised paradigms using voting or entropy-based rewards. However, their performance remains far from satisfactory due to the substantial annotation cost and issues such as model collapse or reward hacking. To address these issues, we introduce a new perspective inspired by cognitive learning theory and propose a novel approach called EasyRL. The core of EasyRL is to simulate the human cognitive acquisition curve by integrating reliable knowledge transfer from easy labeled data with a progressive divide-and-conquer strategy that tackles increasingly difficult unlabeled data. Specifically, we initialize a warm-up model using supervised RL with few-shot labeled data. This is followed by a divide-and-conquer pseudo-labeling strategy on difficult unlabeled data, combining consistency-based selection for low-uncertainty cases and reflection-based resolution for medium-uncertainty cases. Finally, difficulty-progressive self-training with iterative pseudo-labeling and RL further strengthens the model's reasoning capability. EasyRL provides a unified self-evolving framework that facilitates data-efficient post-training of LLMs. Experimental results on mathematical and scientific benchmarks demonstrate that EasyRL, using only 10% of easy labeled data, consistently outperforms state-of-the-art baselines.

---


### 4. [Curiosity-Critic: Cumulative Prediction Error Improvement as a Tractable Intrinsic Reward for World Model Training](https://arxiv.org/abs/2604.18701)

**<font color=#1a73e8>作者：</font>** Vin Bhaskara, Haicheng Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Local prediction-error-based curiosity rewards focus on the current transition without considering the world model's cumulative prediction error across all visited transitions. We introduce Curiosity-Critic, which grounds its intrinsic reward in the improvement of this cumulative objective, and show that it reduces to a tractable per-step form: the difference between the current prediction error and the asymptotic error baseline of the current state transition. We estimate this baseline online with a learned critic co-trained alongside the world model; regressing a single scalar, the critic converges well before the world model saturates, redirecting exploration toward learnable transitions without oracle knowledge of the noise floor. The reward is higher for learnable transitions and collapses toward the baseline for stochastic ones, effectively separating epistemic (reducible) from aleatoric (irreducible) prediction error online. Prior prediction-error curiosity formulations, from Schmidhuber (1991) to learned-feature-space variants, emerge as special cases corresponding to specific approximations of this baseline. Experiments on a stochastic grid world show that Curiosity-Critic outperforms prediction-error and visitation-count baselines in convergence speed and final world model accuracy.

---


### 5. [Characterizing AlphaEarth Embedding Geometry for Agentic Environmental Reasoning](https://arxiv.org/abs/2604.18715)

**<font color=#1a73e8>作者：</font>** Mashrekur Rahman, Samuel J. Barrett, Christina Last  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Earth observation foundation models encode land surface information into dense embedding vectors, yet the geometric structure of these representations and its implications for downstream reasoning remain underexplored. We characterize the manifold geometry of Google AlphaEarth's 64-dimensional embeddings across 12.1 million Continental United States samples (2017--2023) and develop an agentic system that leverages this geometric understanding for environmental reasoning. The manifold is non-Euclidean: effective dimensionality is 13.3 (participation ratio) from 64 raw dimensions, with local intrinsic dimensionality of approximately 10. Tangent spaces rotate substantially, with 84\% of locations exceeding 60\textdegree{} and local-global alignment (mean$|\cos\theta| = 0.17$) approaching the random baseline of 0.125. Supervised linear probes indicate that concept directions rotate across the manifold, and compositional vector arithmetic using both PCA-derived and probe-derived directions yields poor precision. Retrieval instead produces physically coherent results, with local geometry predicting retrieval coherence ($R^2 = 0.32$). Building on this characterization, we introduce an agentic system with nine specialized tools that decomposes environmental queries into reasoning chains over a FAISS-indexed embedding database. A five-condition ablation (120 queries, three complexity tiers) shows that embedding retrieval dominates response quality ($\mu = 3.79 \pm 0.90$ vs.\ $3.03 \pm 0.77$ parametric-only; scale 1--5), with peak performance on multi-step comparisons ($\mu = 4.28 \pm 0.43$). A cross-model benchmark show that geometric tools reduce Sonnet 4.5's score by 0.12 points but improve Opus 4.6's by 0.07, with Opus achieving higher geometric grounding (3.38 vs.\ 2.64), suggesting that the value of geometric characterization scales with the reasoning capability of the consuming model.

---


### 6. [Beyond One Output: Visualizing and Comparing Distributions of Language Model Generations](https://arxiv.org/abs/2604.18724)

**<font color=#1a73e8>作者：</font>** Emily Reif, Claire Yang, Jared Hwang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Users typically interact with and evaluate language models via single outputs, but each output is just one sample from a broad distribution of possible completions. This interaction hides distributional structure such as modes, uncommon edge cases, and sensitivity to small prompt changes, leading users to over-generalize from anecdotes when iterating on prompts for open-ended tasks. Informed by a formative study with researchers who use LMs (n=13) examining when stochasticity matters in practice, how they reason about distributions over language, and where current workflows break down, we introduce GROVE. GROVE is an interactive visualization that represents multiple LM generations as overlapping paths through a text graph, revealing shared structure, branching points, and clusters while preserving access to raw outputs. We evaluate across three crowdsourced user studies (N=47, 44, and 40 participants) targeting complementary distributional tasks. Our results support a hybrid workflow: graph summaries improve structural judgments such as assessing diversity, while direct output inspection remains stronger for detail-oriented questions.

---


### 7. [Investigating Counterfactual Unfairness in LLMs towards Identities through Humor](https://arxiv.org/abs/2604.18729)

**<font color=#1a73e8>作者：</font>** Shubin Kim, Yejin Son, Junyeong Park 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Humor holds up a mirror to social perception: what we find funny often reflects who we are and how we judge others. When language models engage with humor, their reactions expose the social assumptions they have internalized from training data. In this paper, we investigate counterfactual unfairness through humor by observing how the model's responses change when we swap who speaks and who is addressed while holding other factors constant. Our framework spans three tasks: humor generation refusal, speaker intention inference, and relational/societal impact prediction, covering both identity-agnostic humor and identity-specific disparagement humor. We introduce interpretable bias metrics that capture asymmetric patterns under identity swaps. Experiments across state-of-the-art models reveal consistent relational disparities: jokes told by privileged speakers are refused up to 67.5% more often, judged as malicious 64.7% more frequently, and rated up to 1.5 points higher in social harm on a 5-point scale. These patterns highlight how sensitivity and stereotyping coexist in generative models, complicating efforts toward fairness and cultural alignment.

---


### 8. [Remask, Don't Replace: Token-to-Mask Refinement in Masked Diffusion Language Models](https://arxiv.org/abs/2604.18738)

**<font color=#1a73e8>作者：</font>** Lin Yao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Masked diffusion language models such as LLaDA2.1 rely on Token-to-Token (T2T) editing to correct their own generation errors: whenever a different token crosses a confidence threshold, the committed token is overwritten. We identify three structural failure modes of this rule. The trigger cannot fire when no single alternative is confident enough; the replacement is computed under a context that may itself contain errors; and the uniform perturbations used to train the T2T stream do not resemble the coherent, semantically plausible mistakes that the model actually makes at inference. As an alternative, we propose Token-to-Mask (T2M) remasking. Rather than overwriting a suspect token with a new guess, T2M resets the position to the mask state, so that the next denoising step re-predicts it from an in-distribution context. The method is training-free, modifies only the editing rule, and introduces no new parameters. We pair it with three detection heuristics and give a short theoretical account of why a mask is a better conditioning signal than an erroneous token. Across 8 benchmarks, T2M improves accuracy on tasks that require exact token-level output. Its largest gain is +5.92 points on CMATH, where we attribute 79.9% of baseline errors to last-mile corruption (correct reasoning followed by a garbled final answer); T2M repairs 41.3% of these cases.

---


### 9. [Discrete Tilt Matching](https://arxiv.org/abs/2604.18739)

**<font color=#1a73e8>作者：</font>** Yuyuan Chen, Shiyi Wang, Peter Potaptchik 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Masked diffusion large language models (dLLMs) are a promising alternative to autoregressive generation. While reinforcement learning (RL) methods have recently been adapted to dLLM fine-tuning, their objectives typically depend on sequence-level marginal likelihoods, which are intractable for masked diffusion models. To address this, we derive Discrete Tilt Matching (DTM), a likelihood-free method that recasts dLLM fine-tuning as state-level matching of local unmasking posteriors under reward tilting. DTM takes the form of a weighted cross-entropy objective with explicit minimizer, and admits control variates that improve training stability. On a synthetic maze-planning task, we analyze how DTM's annealing schedule and control variates affect training stability and prevent mode collapse. At scale, fine-tuning LLaDA-8B-Instruct with DTM yields strong gains on Sudoku and Countdown while remaining competitive on MATH500 and GSM8K.

---


### 10. [Autonomous Skeletal Landmark Localization towards Agentic C-Arm Control](https://arxiv.org/abs/2604.18740)

**<font color=#1a73e8>作者：</font>** Jay Jung, Ahmad Arrabi, Jax Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose: Automated C-arm positioning ensures timely treatment in patients requiring emergent interventions. When a conventional Deep Learning (DL) approach for C-arm control fails, clinicians must revert to manual operation, resulting in additional delays. Consequently, an agentic C-arm control framework based on multimodal large language models (MLLMs) is highly desirable, as it can incorporate clinician feedback and use reasoning to make adjustments toward more accurate positioning. Skeletal landmark localization is essential for C-arm control, and we investigate adapting MLLMs for autonomous landmark localization.
Methods: We used an annotated synthetic X-ray dataset and a real X-ray dataset. Each X-ray in both datasets is paired with several skeletal landmarks. We fine-tuned two MLLMs and tasked them with retrieving the closest landmarks from each X-ray. Quantitative evaluations of landmark localization were performed and compared against a leading DL approach. We further conducted qualitative experiments demonstrating: (1) how an MLLM can correct an initially incorrect prediction through reasoning, and (2) how the MLLM can sequentially navigate the C-arm toward a target location.
Results: On both datasets, fine-tuned MLLMs demonstrate competitive performance across all localization tasks when compared with the DL approach. In the qualitative experiments, the MLLMs provide evidence of reasoning and spatial awareness.
Conclusion: This study shows that fine-tuned MLLMs achieve accurate skeletal landmark localization and hold promise for agentic autonomous C-arm control. Our code is available athttps://github.com/marszzibros/Cthis http URL

---


### 11. [Handling and Interpreting Missing Modalities in Patient Clinical Trajectories via Autoregressive Sequence Modeling](https://arxiv.org/abs/2604.18753)

**<font color=#1a73e8>作者：</font>** Andrew Wang, Ellie Pavlick, Ritambhara Singh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An active challenge in developing multimodal machine learning (ML) models for healthcare is handling missing modalities during training and deployment. As clinical datasets are inherently temporal and sparse in terms of modality presence, capturing the underlying predictive signal via diagnostic multimodal ML models while retaining model explainability remains an ongoing challenge. In this work, we address this by re-framing clinical diagnosis as an autoregressive sequence modeling task, utilizing causal decoders from large language models (LLMs) to model a patient's multimodal trajectory. We first introduce a missingness-aware contrastive pre-training objective that integrates multiple modalities in datasets with missingness in a shared latent space. We then show that autoregressive sequence modeling with transformer-based architectures outperforms baselines on the MIMIC-IV and eICU fine-tuning benchmarks. Finally, we use interpretability techniques to move beyond performance boosts and find that across various patient stays, removing modalities leads to divergent behavior that our contrastive pre-training mitigates. By abstracting clinical diagnosis as sequence modeling and interpreting patient stay trajectories, we develop a framework to profile and handle missing modalities while addressing the canonical desideratum of safe, transparent clinical AI.

---


### 12. [Towards Understanding the Robustness of Sparse Autoencoders](https://arxiv.org/abs/2604.18756)

**<font color=#1a73e8>作者：</font>** Ahson Saiyed, Sabrina Sadiekh, Chirag Agarwal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) remain vulnerable to optimization-based jailbreak attacks that exploit internal gradient structure. While Sparse Autoencoders (SAEs) are widely used for interpretability, their robustness implications remain underexplored. We present a study of integrating pretrained SAEs into transformer residual streams at inference time, without modifying model weights or blocking gradients. Across four model families (Gemma, LLaMA, Mistral, Qwen) and two strong white-box attacks (GCG, BEAST) plus three black-box benchmarks, SAE-augmented models achieve up to a 5x reduction in jailbreak success rate relative to the undefended baseline and reduce cross-model attack transferability. Parametric ablations reveal (i) a monotonic dose-response relationship between L0 sparsity and attack success rate, and (ii) a layer-dependent defense-utility tradeoff, where intermediate layers balance robustness and clean performance. These findings are consistent with a representational bottleneck hypothesis: sparse projection reshapes the optimization geometry exploited by jailbreak attacks.

---


### 13. [REVEAL: Multimodal Vision-Language Alignment of Retinal Morphometry and Clinical Risks for Incident AD and Dementia Prediction](https://arxiv.org/abs/2604.18757)

**<font color=#1a73e8>作者：</font>** Seowung Leem, Lin Gu, Chenyu You 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The retina provides a unique, noninvasive window into Alzheimer's disease (AD) and dementia, capturing early structural changes through morphometric features, while systemic and lifestyle risk factors reflect well-established contributors to disease susceptibility long before clinical symptom onset. However, current retinal analysis frameworks typically model imaging and risk factors separately, limiting their ability to capture joint multimodal patterns critical for early risk prediction. Moreover, existing methods rarely incorporate mechanisms to organize or align patients with similar retinal and clinical characteristics, constraining the learning of coherent cross-modal associations. To address these limitations, we introduce REVEAL (REtinal-risk Vision-Language Early Alzheimer's Learning), a framework that aligns color fundus photographs with individualized disease-specific risk profiles for predicting incident AD and dementia, on average 8 years before diagnosis (range: 1-11 years). Because real-world risk factors are structured questionnaire data, we translate them into clinically interpretable narratives compatible with pretrained vision-language models (VLMs). We further propose a group-aware contrastive learning (GACL) strategy that clusters patients with similar retinal morphometry and risk factors as positive pairs, strengthening multimodal alignment. This unified representation learning framework substantially outperforms state-of-the-art retinal imaging models paired with clinical text encoders, as well as general-purpose VLMs, demonstrating the value of jointly modeling retinal biomarkers and clinical risk factors. By providing a generalizable and noninvasive approach for early AD and dementia risk stratification, REVEAL has the potential to enable earlier intervention and improve preventive care at the population level.

---


### 14. [An Empirical Study of Multi-Generation Sampling for Jailbreak Detection in Large Language Models](https://arxiv.org/abs/2604.18775)

**<font color=#1a73e8>作者：</font>** Hanrui Luo, Shreyank N Gowda  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Detecting jailbreak behaviour in large language models remains challenging, particularly when strongly aligned models produce harmful outputs only rarely. In this work, we present an empirical study of output based jailbreak detection under realistic conditions using the JailbreakBench Behaviors dataset and multiple generator models with varying alignment strengths. We evaluate both a lexical TF-IDF detector and a generation inconsistency based detector across different sampling budgets. Our results show that single output evaluation systematically underestimates jailbreak vulnerability, as increasing the number of sampled generations reveals additional harmful behaviour. The most significant improvements occur when moving from a single generation to moderate sampling, while larger sampling budgets yield diminishing returns. Cross generator experiments demonstrate that detection signals partially generalise across models, with stronger transfer observed within related model families. A category level analysis further reveals that lexical detectors capture a mixture of behavioural signals and topic specific cues, rather than purely harmful behaviour. Overall, our findings suggest that moderate multi sample auditing provides a more reliable and practical approach for estimating model vulnerability and improving jailbreak detection in large language models. Code will be released.

---


### 15. [Experiments or Outcomes? Probing Scientific Feasibility in Large Language Models](https://arxiv.org/abs/2604.18786)

**<font color=#1a73e8>作者：</font>** Seyedali Mohammadi, Manas Gaur, Francis Ferraro  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific feasibility assessment asks whether a claim is consistent with established knowledge and whether experimental evidence could support or refute it. We frame feasibility assessment as a diagnostic reasoning task in which, given a hypothesis, a model predicts feasible or infeasible and justifies its decision. We evaluate large language models (LLMs) under controlled knowledge conditions (hypothesis-only, with experiments, with outcomes, or both) and probe robustness by progressively removing portions of the experimental and/or outcome context. Across multiple LLMs and two datasets, providing outcome evidence is generally more reliable than providing experiment descriptions. Outcomes tend to improve accuracy beyond what internal knowledge alone provides, whereas experimental text can be brittle and may degrade performance when the context is incomplete. These findings clarify when experimental evidence benefits LLM-based feasibility assessment and when it introduces fragility.

---


### 16. [Efficient Mixture-of-Experts LLM Inference with Apple Silicon NPUs](https://arxiv.org/abs/2604.18788)

**<font color=#1a73e8>作者：</font>** Afsara Benazir, Felix Xiaozhu Lin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Apple Neural Engine (ANE) is a dedicated neural processing unit (NPU) present in every Apple Silicon chip. Mixture-of-Experts (MoE) LLMs improve inference efficiency via sparse activation but are challenging for NPUs in three ways: expert routing is unpredictable and introduces dynamic tensor shapes that conflict with the shape-specific constraints of NPUs; several irregular operators, e.g., top-k, scatter/gather, etc., are not NPU-friendly; and launching many small expert kernels incurs substantial dispatch and synchronization overhead. NPUs are designed to offload AI compute from CPU and GPU; our goal is to enable such offloading for MoE inference, particularly during prefill, where long-context workloads consume substantial system resources.
This paper presents NPUMoE, a runtime inference engine that accelerates MoE execution on Apple Silicon by offloading dense, static computation to NPU, while preserving a CPU/GPU fallback path for dynamic operations. NPUMoE uses offline calibration to estimate expert capacity and popularity that drives three key techniques: (1) Static tiers for expert capacity to address dynamic expert routing (2) Grouped expert execution to mitigate NPU concurrency limits (3) Load-aware expert compute graph residency to reduce CPU-NPU synchronization overhead. Experiments on Apple M-series devices using three representative MoE LLMs and four long-context workloads show that NPUMoE consistently outperforms baselines, reducing latency by 1.32x-5.55x, improving energy efficiency by 1.81x-7.37x, and reducing CPU-cycle usage by 1.78x-5.54x through effective NPU offloading.

---


### 17. [ARES: Adaptive Red-Teaming and End-to-End Repair of Policy-Reward System](https://arxiv.org/abs/2604.18789)

**<font color=#1a73e8>作者：</font>** Jiacheng Liang, Yao Ma, Tharindu Kumarage 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning from Human Feedback (RLHF) is central to aligning Large Language Models (LLMs), yet it introduces a critical vulnerability: an imperfect Reward Model (RM) can become a single point of failure when it fails to penalize unsafe behaviors. While existing red-teaming approaches primarily target policy-level weaknesses, they overlook what we term systemic weaknesses cases where both the core LLM and the RM fail in tandem.
We present ARES, a framework that systematically discovers and mitigates such dual vulnerabilities. ARES employs a ``Safety Mentor'' that dynamically composes semantically coherent adversarial prompts by combining structured component types (topics, personas, tactics, goals) and generates corresponding malicious and safe responses. This dual-targeting approach exposes weaknesses in both the core LLM and the RM simultaneously. Using the vulnerabilities gained, ARES implements a two-stage repair process: first fine-tuning the RM to better detect harmful content, then leveraging the improved RM to optimize the core model. Experiments across multiple adversarial safety benchmarks demonstrate that ARES substantially enhances safety robustness while preserving model capabilities, establishing a new paradigm for comprehensive RLHF safety alignment.

---


### 18. [LLM-as-Judge Framework for Evaluating Tone-Induced Hallucination in Vision-Language Models](https://arxiv.org/abs/2604.18803)

**<font color=#1a73e8>作者：</font>** Zhiyuan Jiang, Weihao Hong, Xinlei Guan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) are increasingly deployed in settings where reliable visual grounding carries operational consequences, yet their behavior under progressively coercive prompt phrasing remains undercharacterized. Existing hallucination benchmarks predominantly rely on neutral prompts and binary detection, leaving open how both the incidence and the intensity of fabrication respond to graded linguistic pressure across structurally distinct task types. We present Ghost-100, a procedurally constructed benchmark of 800 synthetically generated images spanning eight categories across three task families -- text-illegibility, time-reading, and object-absence -- each designed under a negative-ground-truth principle that guarantees the queried target is absent, illegible, or indeterminate by construction. Every image is paired with five prompts drawn from a structured 5-Level Prompt Intensity Framework, holding the image and task identity fixed while varying only directive force, so that tone is isolated as the sole independent variable. We adopt a dual-track evaluation protocol: a rule-based H-Rate measuring the proportion of responses in which a model crosses from grounded refusal into unsupported positive commitment, and a GPT-4o-mini-judged H-Score on a 1-5 scale characterizing the confidence and specificity of fabrication once it occurs. We additionally release a three-stage automated validation workflow, which retrospectively confirms 717 of 800 images as strictly compliant. Evaluating nine open-weight VLMs, we find that H-Rate and H-Score dissociate substantially across model families, reading-style and presence-detection subsets respond to prompt pressure in qualitatively different ways, and several models exhibit non-monotonic sensitivity peaking at intermediate tone levels -- patterns that aggregate metrics obscure.

---


### 19. [DUALVISION: RGB-Infrared Multimodal Large Language Models for Robust Visual Reasoning](https://arxiv.org/abs/2604.18829)

**<font color=#1a73e8>作者：</font>** Abrar Majeedi, Zhiyuan Ruan, Ziyi Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have achieved impressive performance on visual perception and reasoning tasks with RGB imagery, yet they remain fragile under common degradations, such as fog, blur, or low-light conditions. Infrared (IR) imaging, a well-established complement to RGB, offers inherent robustness in these conditions, but its integration into MLLMs remains underexplored. To bridge this gap, we propose DUALVISION, a lightweight fusion module that efficiently incorporates IR-RGB information into MLLMs via patch-level localized cross-attention. To support training and evaluation and to facilitate future research, we also introduce DV-204K, a dataset of ~25K publicly available aligned IR-RGB image pairs with 204K modality-specific QA annotations, and DV-500, a benchmark of 500 IR-RGB image pairs with 500 QA pairs designed for evaluating cross-modal reasoning. Leveraging these datasets, we benchmark both open- and closed-source MLLMs and demonstrate that DUALVISION delivers strong empirical performance under a wide range of visual degradations. Our code and dataset are available at this https URL.

---


### 20. [Feasibility of Indoor Frame-Wise Lidar Semantic Segmentation via Distillation from Visual Foundation Model](https://arxiv.org/abs/2604.18831)

**<font color=#1a73e8>作者：</font>** Haiyang Wu, Juan J. Gonzales Torres, George Vosselman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Frame-wise semantic segmentation of indoor lidar scans is a fundamental step toward higher-level 3D scene understanding and mapping applications. However, acquiring frame-wise ground truth for training deep learning models is costly and time-consuming. This challenge is largely addressed, for imagery, by Visual Foundation Models (VFMs) which segment image frames. The same VFMs may be used to train a lidar scan frame segmentation model via a 2D-to-3D distillation pipeline. The success of such distillation has been shown for autonomous driving scenes, but not yet for indoor scenes. Here, we study the feasibility of repeating this success for indoor scenes, in a frame-wise distillation manner by coupling each lidar scan with a VFM-processed camera image. The evaluation is done using indoor SLAM datasets, where pseudo-labels are used for downstream evaluation. Also, a small manually annotated lidar dataset is provided for validation, as there are no other lidar frame-wise indoor datasets with semantics. Results show that the distilled model achieves up to 56% mIoU under pseudo-label evaluation and around 36% mIoU with real-label, demonstrating the feasibility of cross-modal distillation for indoor lidar semantic segmentation without manual annotations.

---


### 21. [Semantic Needles in Document Haystacks: Sensitivity Testing of LLM-as-a-Judge Similarity Scoring](https://arxiv.org/abs/2604.18835)

**<font color=#1a73e8>作者：</font>** Sinan G. Aksoy, Alexandra A. Sabrio, Erik VonKaenel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose a scalable, multifactorial experimental framework that systematically probes LLM sensitivity to subtle semantic changes in pairwise document comparison. We analogize this as a needle-in-a-haystack problem: a single semantically altered sentence (the needle) is embedded within surrounding context (the hay), and we vary the perturbation type (negation, conjunction swap, named entity replacement), context type (original vs. topically unrelated), needle position, and document length across all combinations, testing five LLMs on tens of thousands of document pairs. Our analysis reveals several striking findings. First, LLMs exhibit a within-document positional bias distinct from previously studied candidate-order effects: most models penalize semantic differences more harshly when they occur earlier in a document. Second, when the altered sentence is surrounded by topically unrelated context, it systematically lowers similarity scores and induces bipolarized scores that indicate either very low or very high similarity. This is consistent with an interpretive frame account in which topically-related context may allow models to contextualize and downweight the alterations. Third, each LLM produces a qualitatively distinct scoring distribution, a stable "fingerprint" that is invariant to perturbation type, yet all models share a universal hierarchy in how leniently they treat different perturbation types. Together, these results demonstrate that LLM semantic similarity scores are sensitive to document structure, context coherence, and model identity in ways that go beyond the semantic change itself, and that the proposed framework offers a practical, LLM-agnostic toolkit for auditing and comparing scoring behavior across current and future models.

---


### 22. [The Triadic Loop: A Framework for Negotiating Alignment in AI Co-hosted Livestreaming](https://arxiv.org/abs/2604.18850)

**<font color=#1a73e8>作者：</font>** Katherine Wang, Nadia Berthouze, Aneesha Singh  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI systems are increasingly embedded in multi-user social environments, yet most alignment frameworks conceptualize interaction as a dyadic relationship between a single user and an AI system. Livestreaming platforms challenge this assumption: interaction unfolds among streamers and audiences in real time, producing dynamic affective and social feedback loops. In this paper, we introduce the Triadic Loop, a conceptual framework that reconceptualizes alignment in AI co-hosted livestreaming as a temporally reinforced process of bidirectional adaptation among three actors: streamer $\leftrightarrow$ AI co-host, AI co-host $\leftrightarrow$ audience, and streamer $\leftrightarrow$ audience. Unlike instruction-following paradigms, bidirectional alignment requires each actor to continuously reshape the others, meaning misalignment in any sub-loop can destabilize the broader system. Drawing on literature from multi-party interaction, collaborative AI, and relational agents, we articulate how AI co-hosts function not only as mediators but as performative participants and community members shaping collective meaning-making. We further propose "strategic misalignment" as a mechanism for sustaining community engagement and introduce three relational evaluation constructs grounded in established instruments. The framework contributes a model of dynamic multi-party alignment, an account of cross-loop reinforcement, and design implications for AI co-hosts that sustain social coherence in participatory media environments.

---


### 23. [Hierarchically Robust Zero-shot Vision-language Models](https://arxiv.org/abs/2604.18867)

**<font color=#1a73e8>作者：</font>** Junhao Dong, Yifei Zhang, Hao Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) can perform zero-shot classification but are susceptible to adversarial attacks. While robust fine-tuning improves their robustness, existing approaches align fixed text embeddings with an image embedding, sacrificing natural performance and robustness. A robustness degradation also occurs when a model faces adversarial attacks targeting superclasses (parent classes, e.g., mammal) in addition to their base (leaf) classes (e.g., cat). Thus, to enhance adversarial robustness and leverage the inherent hierarchical properties of class space, we propose a novel adversarial fine-tuning framework based on hierarchical embeddings and several levels of adversarially robust alignment of image-text modalities. Additional mechanisms place visual embeddings at the desired depth of hierarchy, and we provide a theoretical connection between the depth of embedding in the hierarchy and the maximum viable margin size. Our model naturally realizes several margin sizes, boosting generalization of adversaries for robustification. As various trees with different parent labels can share the same leaf labels, we also consider aligning over multiple trees to boost semantic variety. Experiments across several datasets are performed.

---


### 24. [How Adversarial Environments Mislead Agentic AI?](https://arxiv.org/abs/2604.18874)

**<font color=#1a73e8>作者：</font>** Zhonghao Zhan, Huichi Zhou, Zhenhao Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-integrated agents are deployed on the premise that external tools ground their outputs in reality. Yet this very reliance creates a critical attack surface. Current evaluations benchmark capability in benign settings, asking "can the agent use tools correctly" but never "what if the tools lie". We identify this Trust Gap: agents are evaluated for performance, not for skepticism. We formalize this vulnerability as Adversarial Environmental Injection (AEI), a threat model where adversaries compromise tool outputs to deceive agents. AEI constitutes environmental deception: constructing a "fake world" of poisoned search results and fabricated reference networks around unsuspecting agents. We operationalize this via POTEMKIN, a Model Context Protocol (MCP)-compatible harness for plug-and-play robustness testing. We identify two orthogonal attack surfaces: The Illusion (breadth attacks) poison retrieval to induce epistemic drift toward false beliefs, while The Maze (depth attacks) exploit structural traps to cause policy collapse into infinite loops. Across 11,000+ runs on five frontier agents, we find a stark robustness gap: resistance to one attack often increases vulnerability to the other, demonstrating that epistemic and navigational robustness are distinct capabilities.

---


### 25. [LegalBench-BR: A Benchmark for Evaluating Large Language Models on Brazilian Legal Decision Classification](https://arxiv.org/abs/2604.18878)

**<font color=#1a73e8>作者：</font>** Pedro Barbosa de Carvalho Neto  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce LegalBench-BR, the first public benchmark for evaluating language models on Brazilian legal text classification. The dataset comprises 3,105 appellate proceedings from the Santa Catarina State Court (TJSC), collected via the DataJud API (CNJ) and annotated across five legal areas through LLM-assisted labeling with heuristic validation. On a class-balanced test set, BERTimbau-LoRA, updating only 0.3% of model parameters, achieves 87.6% accuracy and 0.87 macro-F1 (+22pp over Claude 3.5 Haiku, +28pp over GPT-4o mini). The gap is most striking on administrativo (administrative law): GPT-4o mini scores F1 = 0.00 and Claude 3.5 Haiku scores F1 = 0.08 on this class, while the fine-tuned model reaches F1 = 0.91. Both commercial LLMs exhibit a systematic bias toward civel (civil law), absorbing ambiguous classes rather than discriminating them, a failure mode that domain-adapted fine-tuning eliminates. These results demonstrate that general-purpose LLMs cannot substitute for domain-adapted models in Brazilian legal classification, even when the task is a simple 5-class problem, and that LoRA fine-tuning on a consumer GPU closes the gap at zero marginal inference cost. We release the full dataset, model, and pipeline to enable reproducible research in Portuguese legal NLP.

---


### 26. [Where Fake Citations Are Made: Tracing Field-Level Hallucination to Specific Neurons in LLMs](https://arxiv.org/abs/2604.18880)

**<font color=#1a73e8>作者：</font>** Yuefei Chen, Yihao Quan, Xiaodong Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs frequently generate fictitious yet convincing citations, often expressing high confidence even when the underlying reference is wrong. We study this failure across 9 models and 108{,}000 generated references, and find that author names fail far more often than other fields across all models and settings. Citation style has no measurable effect, while reasoning-oriented distillation degrades recall. Probes trained on one field transfer at near-chance levels to the others, suggesting that hallucination signals do not generalize across fields. Building on this finding, we apply elastic-net regularization with stability selection to neuron-level CETT values of Qwen2.5-32B-Instruct and identify a sparse set of field-specific hallucination neurons (FH-neurons). Causal intervention further confirms their role: amplifying these neurons increases hallucination, while suppressing them improves performance across fields, with larger gains in some fields. These results suggest a lightweight approach to detecting and mitigating citation hallucination using internal model signals alone.

---


### 27. [Prioritizing the Best: Incentivizing Reliable Multimodal Reasoning by Rewarding Beyond Answer Correctness](https://arxiv.org/abs/2604.18892)

**<font color=#1a73e8>作者：</font>** Mengzhao Jia, Zhihan Zhang, Meng Jiang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) improves multimodal reasoning by rewarding verifiable final answers. Yet answer-correct trajectories may still rely on incomplete derivations, weak evidence, or statements that contradict their conclusions. This gap between answer correctness and reasoning validity, which we call reasoning-answer inconsistency, motivates trajectory supervision in multimodal RL. We compare two main approaches: reward models (RMs), and Generative Rewards (GRs). RMs are efficient and help early in training, but their gains weaken as the policy distribution shifts; GRs improve performance, but may give unstable rewards and computationally expensive. We therefore propose Groupwise Ranking Reward, which ranks verifier-passed trajectories for the same prompt in one pass and redistributes reward accordingly. Groupwise comparison better separates stronger and weaker correct trajectories with lower judge overhead than GRs. Experiments show that RLVR aggravates reasoning-answer inconsistency, while trajectory supervision alleviates it. Groupwise Ranking Reward performs best overall, improving reliability-conditioned accuracy from 47.4% to 54.7% over RLVR.

---


### 28. [Less Is More: Cognitive Load and the Single-Prompt Ceiling in LLM Mathematical Reasoning](https://arxiv.org/abs/2604.18897)

**<font color=#1a73e8>作者：</font>** Manuel Israel Cazares  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a systematic empirical study of prompt engineering for formal mathematical reasoning in the context of the SAIR Equational Theories Stage 1 competition. The task requires deciding whether one equational law implies another over all magmas -- a problem that is undecidable in general but decidable for FALSE via finite model search. Over five weeks, we designed, tested, and analyzed more than 40 prompt variants, ranging from 0 to 4,878 bytes, across four evaluation splits and three language models (gpt-oss-120b, Llama 3.3 70B, Gemma 4 31B).
Our central finding is a single-prompt ceiling: despite substantial engineering effort, balanced hard accuracy plateaus in an empirical saturation region of approximately 60--79% for gpt-oss-120b, compared to a 59.75% no-cheatsheet baseline. We identify three mechanisms underlying this ceiling: (1) the mathematical undecidability of the TRUE case limits what any finite prompt can encode; (2) complex rule systems decrease performance on weaker models (Llama 3.3 70B collapses to 0% TRUE recall with prompts exceeding 2KB); and (3) prompt ordering effects interact with model attention in fragile, non-monotonic ways.
Our best submission (AN45c, 2,252 bytes) achieves 79.25% accuracy on hard3 (n=400; 95% CI: [75.0%, 82.9%]), with TRUE recall of 95.9% and FALSE recall of 63.4%, representing a +19.5 percentage-point improvement over the no-cheatsheet baseline (59.75%). We release all prompt variants, evaluation scripts, and results at this https URL

---


### 29. [Harmful Intent as a Geometrically Recoverable Feature of LLM Residual Streams](https://arxiv.org/abs/2604.18901)

**<font color=#1a73e8>作者：</font>** Isaac Llorente-Saguer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Harmful intent is geometrically recoverable from large language model residual streams: as a linear direction in most layers, and as angular deviation in layers where projection methods fail. Across 12 models spanning four architectural families (Qwen2.5, Qwen3.5, Llama-3.2, Gemma-3) and three alignment variants (base, instruction-tuned, abliterated), under single-turn, English evaluation, we characterise this geometry through six direction-finding strategies. Three succeed: a soft-AUC-optimised linear direction reaches mean AUROC 0.98 and TPR@1\%FPR 0.80; a class-mean probe reaches 0.98 and 0.71 at <1ms fitting cost; a supervised angular-deviation strategy reaches AUROC 0.96 and TPR of 0.61 along a representationally distinct direction ($73^\circ$ from projection-based solutions), uniquely sustaining detection in middle layers where projection methods collapse.
Detection remains stable across alignment variants, including abliterated models from which refusal has been surgically removed: harmful intent and refusal behaviour are functionally dissociated features of the representation. A direction fitted on AdvBench transfers to held-out HarmBench and JailbreakBench with worst-case AUROC 0.96. The same picture holds at scale: across Qwen3.5 from 0.8B to 9B parameters, AUROC remains $\geq$0.98 and cross-variant transfer stays within 0.018 of own-direction performance
This is consistent with a simple account: models acquire a linearly decodable representation of harmful intent as part of general language understanding, and alignment then shapes what they do with such inputs without reorganising the upstream recognition signal. As a practical consequence, AUROC in the 0.97+ regime can substantially overestimate operational detectability; TPR@$1\%$FPR should accompany AUROC in safety-adjacent evaluation.

---


### 30. [LogosKG: Hardware-Optimized Scalable and Interpretable Knowledge Graph Retrieval](https://arxiv.org/abs/2604.18913)

**<font color=#1a73e8>作者：</font>** He Cheng, Yifu Wu, Saksham Khatwani 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge graphs (KGs) are increasingly integrated with large language models (LLMs) to provide structured, verifiable reasoning. A core operation in this integration is multi-hop retrieval, yet existing systems struggle to balance efficiency, scalability, and interpretability. We introduce LogosKG, a novel, hardware-aligned framework that enables scalable and interpretable k-hop retrieval on large KGs by building on symbolic KG formulations and executing traversal as hardware-efficient operations over decomposed subject, object, and relation representations. To scale to billion-edge graphs, LogosKG integrates degree-aware partitioning, cross-graph routing, and on-demand caching. Experiments show substantial efficiency gains over CPU and GPU baselines without loss of retrieval fidelity. With proven performance in KG retrieval, a downstream two-round KG-LLM interaction demonstrates how LogosKG enables large-scale, evidence-grounded analysis of how KG topology, such as hop distribution and connectivity, shapes the alignment between structured biomedical knowledge and LLM diagnostic reasoning, thereby opening the door for next-generation KG-LLM integration. The source code is publicly available at this https URL, and an online demo is available at this https URL.

---


### 31. [Proposing Topic Models and Evaluation Frameworks for Analyzing Associations with External Outcomes: An Application to Leadership Analysis Using Large-Scale Corporate Review Data](https://arxiv.org/abs/2604.18919)

**<font color=#1a73e8>作者：</font>** Yura Yoshida, Masato Kanai, Masataka Nakayama 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Analyzing topics extracted from text data in relation to external outcomes is important across fields such as computational social science and organizational research. However, existing topic modeling methods struggle to simultaneously achieve interpretability, topic specificity (alignment with concrete actions or characteristics), and polarity stance consistency (absence of mixed positive and negative evaluations within a topic). Focusing on leadership analysis using corporate review data, this study proposes a method leveraging large language models to generate topics that satisfy these properties, along with an evaluation framework tailored to external outcome analysis. The framework explicitly incorporates topic specificity and polarity stance consistency as evaluation criteria and examines automated evaluation methods based on existing metrics. Using employee reviews from OpenWork, a major corporate review platform in Japan, the proposed method achieves improved interpretability, specificity, and polarity consistency compared to existing approaches. In analyses of external outcomes such as employee morale, it also produces topics with higher explanatory power. These results suggest that the proposed method and evaluation framework provide a generalized approach for topic analysis in applications involving external outcomes.

---


### 32. [Fine-Tuning Small Reasoning Models for Quantum Field Theory](https://arxiv.org/abs/2604.18936)

**<font color=#1a73e8>作者：</font>** Nathaniel S. Woodward, Zhiqi Gao, Yurii Kvasiuk 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the growing application of Large Language Models (LLMs) to theoretical physics, there is little academic exploration into how domain-specific physics reasoning ability develops while training these models. To investigate this, we perform the first academic fine-tuning study of small (7B-parameter) reasoning models dedicated specifically to theoretical physics. Because open-source verifiable training data required to train such capabilities is scarce, we developed a robust data generation pipeline that can both create synthetic problems and make existing human-authored problems suitable for model training. Selecting Quantum Field Theory (QFT) as our primary domain, we generated over 2,500 synthetic problems alongside a curated collection of human-adapted problems sourced from arXiv and standard pedagogical resources. We conduct both Reinforcement Learning (RL) and Supervised Fine-Tuning (SFT) experiments, benchmarking performance gains as well as generalization to other physics domains. We perform an extensive analysis of model chains-of-though before and after fine-tuning, to understand how reasoning errors evolve during RL and SFT. Finally, we publicly release our data pipeline, verifiable QFT training data, and $\sim$200M tokens of QFT reasoning traces.

---


### 33. [Disparities In Negation Understanding Across Languages In Vision-Language Models](https://arxiv.org/abs/2604.18942)

**<font color=#1a73e8>作者：</font>** Charikleia Moraitaki, Sarah Pan, Skyler Pulling 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) exhibit affirmation bias: a systematic tendency to select positive captions ("X is present") even when the correct description contains negation ("no X"). While prior work has documented this failure mode in English and proposed solutions, negation manifests differently across languages through varying morphology, word order, and cliticization patterns, raising the question of whether these solutions serve all linguistic communities equitably. We introduce the first human-verified multilingual negation benchmark, spanning seven typologically diverse languages: English, Mandarin Chinese, Arabic, Greek, Russian, Tagalog, and Spanish. Evaluating three VLMs - CLIP, SigLIP, and MultiCLIP - we find that standard CLIP performs at or below chance on non-Latin-script languages, while MultiCLIP achieves the highest and most uniform accuracy. We also evaluate SpaceVLM, a proposed negation correction, and find that it produces substantial improvements for several languages - particularly English, Greek, Spanish, and Tagalog - while showing varied effectiveness across typologically different languages. This variation reveals that linguistic properties like morphology, script, and negation structure interact with model improvements in fairness-relevant ways. As VLMs are deployed globally, multilingual benchmarks are essential for understanding not just whether solutions work, but for whom.

---


### 34. [Personalized Benchmarking: Evaluating LLMs by Individual Preferences](https://arxiv.org/abs/2604.18943)

**<font color=#1a73e8>作者：</font>** Cristina Garbacea, Heran Wang, Chenhao Tan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the rise in capabilities of large language models (LLMs) and their deployment in real-world tasks, evaluating LLM alignment with human preferences has become an important challenge. Current benchmarks average preferences across all users to compute aggregate ratings, overlooking individual user preferences when establishing model rankings. Since users have varying preferences in different contexts, we call for personalized LLM benchmarks that rank models according to individual needs. We compute personalized model rankings using ELO ratings and Bradley-Terry coefficients for 115 active Chatbot Arena users and analyze how user query characteristics (topics and writing style) relate to LLM ranking variations. We demonstrate that individual rankings of LLM models diverge dramatically from aggregate LLM rankings, with Bradley-Terry correlations averaging only $\rho = 0.04$ (57\% of users show near-zero or negative correlation) and ELO ratings showing moderate correlation ($\rho = 0.43$). Through topic modeling and style analysis, we find users exhibit substantial heterogeneity in topical interests and communication styles, influencing their model preferences. We further show that a compact combination of topic and style features provides a useful feature space for predicting user-specific model rankings. Our results provide strong quantitative evidence that aggregate benchmarks fail to capture individual preferences for most users, and highlight the importance of developing personalized benchmarks that rank LLM models according to individual user preferences.

---


### 35. [Reasoning Structure Matters for Safety Alignment of Reasoning Models](https://arxiv.org/abs/2604.18946)

**<font color=#1a73e8>作者：</font>** Yeonjun In, Wonjoong Kim, Sangwu Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large reasoning models (LRMs) achieve strong performance on complex reasoning tasks but often generate harmful responses to malicious user queries. This paper investigates the underlying cause of these safety risks and shows that the issue lies in the reasoning structure itself. Based on this insight, we claim that effective safety alignment can be achieved by altering the reasoning structure. We propose AltTrain, a simple yet effective post training method that explicitly alters the reasoning structure of LRMs. AltTrain is both practical and generalizable, requiring no complex reinforcement learning (RL) training or reward design, only supervised finetuning (SFT) with a lightweight 1K training examples. Experiments across LRM backbones and model sizes demonstrate strong safety alignment, along with robust generalization across reasoning, QA, summarization, and multilingual setting.

---


### 36. [Assessing Capabilities of Large Language Models in Social Media Analytics: A Multi-task Quest](https://arxiv.org/abs/2604.18955)

**<font color=#1a73e8>作者：</font>** Ramtin Davoudi, Kartik Thakkar, Nazanin Donyapour 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this study, we present the first comprehensive evaluation of modern LLMs - including GPT-4, GPT-4o, GPT-3.5-Turbo, Gemini 1.5 Pro, DeepSeek-V3, Llama 3.2, and BERT - across three core social media analytics tasks on a Twitter (X) dataset: (I) Social Media Authorship Verification, (II) Social Media Post Generation, and (III) User Attribute Inference. For the authorship verification, we introduce a systematic sampling framework over diverse user and post selection strategies and evaluate generalization on newly collected tweets from January 2024 onward to mitigate "seen-data" bias. For post generation, we assess the ability of LLMs to produce authentic, user-like content using comprehensive evaluation metrics. Bridging Tasks I and II, we conduct a user study to measure real users' perceptions of LLM-generated posts conditioned on their own writing. For attribute inference, we annotate occupations and interests using two standardized taxonomies (IAB Tech Lab 2023 and 2018 U.S. SOC) and benchmark LLMs against existing baselines. Overall, our unified evaluation provides new insights and establishes reproducible benchmarks for LLM-driven social media analytics. The code and data are provided in the supplementary material and will also be made publicly available upon publication.

---


### 37. [Bridging Foundation Models and ASTM Metallurgical Standards for Automated Grain Size Estimation from Microscopy Images](https://arxiv.org/abs/2604.18957)

**<font color=#1a73e8>作者：</font>** Abdul Mueez, Shruti Vyas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Extracting standardized metallurgical metrics from microscopy images remains challenging due to complex grain morphology and the data demands of supervised segmentation. To bridge foundational computer vision with practical metallurgical evaluation, we propose an automated pipeline for dense instance segmentation and grain size estimation that adapts Cellpose-SAM to microstructures and integrates its topology-aware gradient tracking with an ASTM E112 Jeffries planimetric module. We systematically benchmark this pipeline against a classical convolutional network (U-Net), an adaptive-prompting vision foundation model (MatSAM) and a contemporary vision-language model (Qwen2.5-VL-7B). Our evaluations reveal that while the out-of-the-box vision-language model struggles with the localized spatial reasoning required for dense microscopic counting and MatSAM suffers from over-segmentation despite its domain-specific prompt generation, our adapted pipeline successfully maintains topological separation. Furthermore, experiments across progressively reduced training splits demonstrate exceptional few-shot scalability; utilizing only two training samples, the proposed system predicts the ASTM grain size number (G) with a mean absolute percentage error (MAPE) as low as 1.50%, while robustness testing across varying target grain counts empirically validates the ASTM 50-grain sampling minimum. These results highlight the efficacy of application-level foundation model integration for highly accurate, automated materials characterization. Our project repository is available at this https URL.

---


### 38. [Distillation Traps and Guards: A Calibration Knob for LLM Distillability](https://arxiv.org/abs/2604.18963)

**<font color=#1a73e8>作者：</font>** Weixiao Zhan, Yongcheng Jing, Leszek Rutkowski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation (KD) transfers capabilities from large language models (LLMs) to smaller students, yet it can fail unpredictably and also underpins model leakage risks. Our analysis revealed several distillation traps: tail noise, off-policy instability, and, most fundamentally, the teacher-student gap, that distort training signals. These traps manifest as overconfident hallucinations, self-correction collapse, and local decoding degradation, causing distillation to fail. Motivated by these findings, we propose a post-hoc calibration method that, to the best of our knowledge, for the first time enables control over a teacher's distillability via reinforcement fine-tuning (RFT). Our objective combines task utility, KL anchor, and across-tokenizer calibration reward. This makes distillability a practical safety lever for foundation models, connecting robust teacher-student transfer with deployment-aware model protection. Experiments across math, knowledge QA, and instruction-following tasks show that students distilled from distillable calibrated teachers outperform SFT and KD baselines, while undistillable calibrated teachers retain their task performance but cause distilled students to collapse, offering a practical knob for both better KD and model IP protection.

---


### 39. [DW-Bench: Benchmarking LLMs on Data Warehouse Graph Topology Reasoning](https://arxiv.org/abs/2604.18964)

**<font color=#1a73e8>作者：</font>** Ahmed G.A.H Ahmed, C. Okan Sakar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper introduces DW-Bench, a new benchmark that evaluates large language models (LLMs) on graph-topology reasoning over data warehouse schemas, explicitly integrating both foreign-key (FK) and data-lineage edges. The benchmark comprises 1,046 automatically generated, verifiably correct questions across five schemas. Experiments show that tool-augmented methods substantially outperform static approaches but plateau on hard compositional subtypes.

---


### 40. [Self-Improving Tabular Language Models via Iterative Group Alignment](https://arxiv.org/abs/2604.18966)

**<font color=#1a73e8>作者：</font>** Yunbo Long, Tejumade Afonja, Alexandra Brintrup 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While language models have been adapted for tabular data generation, two fundamental limitations remain: (1) static fine-tuning produces models that cannot learn from their own generated samples and adapt to self-correct, and (2) autoregressive objectives preserve local token coherence but neglect global statistical properties, degrading tabular quality. Reinforcement learning offers a potential solution but requires designing reward functions that balance competing objectives -- impractical for tabular data. To fill the gap, we introduce TabGRAA (Tabular Group-Relative Advantage Alignment), the first self-improving framework for tabular data generation via automated feedback. At each iteration, TabGRAA uses an \emph{automated quality signal} -- such as a two-sample distinguishability classifier or a distance-based reward -- to partition newly generated samples into high- and low-quality groups, then optimizes a group-relative advantage objective that reinforces realistic patterns while penalizing artifacts. The specific signal is a modular choice rather than a fixed component of the framework. This establishes a virtuous feedback cycle, where the quality signal is re-computed against newly \emph{generated synthetic} samples at each round; the language model is only fine-tuned on these self-generated signals, so no additional real record is exposed during alignment, mitigating data-leakage risk beyond the initial supervised fine-tuning. Experiments show TabGRAA outperforms existing methods in fidelity, utility, and privacy, while matching or exceeding diffusion-based synthesizers, advancing tabular synthesis from static statistical replication to dynamic, self-improving generation.

---


### 41. [STAR-Teaming: A Strategy-Response Multiplex Network Approach to Automated LLM Red Teaming](https://arxiv.org/abs/2604.18976)

**<font color=#1a73e8>作者：</font>** MinJae Jung, YongTaek Lim, Chaeyun Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) are widely used, they remain susceptible to jailbreak prompts that can elicit harmful or inappropriate responses. This paper introduces STAR-Teaming, a novel black-box framework for automated red teaming that effectively generates such prompts. STAR-Teaming integrates a Multi-Agent System (MAS) with a Strategy-Response Multiplex Network and employs network-driven optimization to sample effective attack strategies. This network-based approach recasts the intractable high-dimensional embedding space into a tractable structure, yielding two key advantages: it enhances the interpretability of the LLM's strategic vulnerabilities, and it streamlines the search for effective strategies by organizing the search space into semantic communities, thereby preventing redundant exploration. Empirical results demonstrate that STAR-Teaming significantly surpasses existing methods, achieving a higher attack success rate (ASR) at a lower computational cost. Extensive experiments validate the effectiveness and explainability of the Multiplex Network. The code is available at this https URL.

---


### 42. [SAVOIR: Learning Social Savoir-Faire via Shapley-based Reward Attribution](https://arxiv.org/abs/2604.18982)

**<font color=#1a73e8>作者：</font>** Xiachong Feng, Yi Jiang, Xiaocheng Feng 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Social intelligence, the ability to navigate complex interpersonal interactions, presents a fundamental challenge for language agents. Training such agents via reinforcement learning requires solving the credit assignment problem: determining how individual utterances contribute to multi-turn dialogue outcomes. Existing approaches directly employ language models to distribute episode-level rewards, yielding attributions that are retrospective and lack theoretical grounding. We propose SAVOIR (ShApley Value fOr SocIal RL), a novel principled framework grounded in cooperative game theory. Our approach combines two complementary principles: expected utility shifts evaluation from retrospective attribution to prospective valuation, capturing an utterance's strategic potential for enabling favorable future trajectories; Shapley values ensure fair credit distribution with axiomatic guarantees of efficiency, symmetry, and marginality. Experiments on the SOTOPIA benchmark demonstrate that SAVOIR achieves new state-of-the-art performance across all evaluation settings, with our 7B model matching or exceeding proprietary models including GPT-4o and Claude-3.5-Sonnet. Notably, even large reasoning models consistently underperform, suggesting social intelligence requires qualitatively different capabilities than analytical reasoning.

---


### 43. [A Multi-Agent Framework with Structured Reasoning and Reflective Refinement for Multimodal Empathetic Response Generation](https://arxiv.org/abs/2604.18988)

**<font color=#1a73e8>作者：</font>** Liping Wang, Cheng Ye, Weidong Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal empathetic response generation (MERG) aims to generate emotionally engaging and empathetic responses based on users' multimodal contexts. Existing approaches usually rely on an implicit one-pass generation paradigm from multimodal context to the final response, which overlooks two intrinsic characteristics of MERG: (1) Human perception of emotional cues is inherently structured rather than a direct mapping. The conventional paradigm neglects the hierarchical progression of emotion perception, leading to distorted emotional judgments. (2) Given the inherent complexity and ambiguity of human emotions, the conventional paradigm is prone to significant emotional biases, ultimately resulting in suboptimal empathy. In this paper, we propose a multi-agent framework for MERG, which enhances empathy through structured reasoning and reflective refinement. Specifically, we first introduce a structured empathetic reasoning-to-generation module that explicitly decomposes response generation via multimodal perception, consistency-aware emotion forecasting, pragmatic strategy planning, and strategy-guided response generation, providing a clearer intermediate path from multimodal evidence to response realization. Besides, we develop a global reflection and refinement module, in which a global reflection agent performs step-wise auditing over intermediate states and the generated response, eliminating existing emotional biases and empathy errors, and triggering targeted regeneration. Overall, such a closed-loop framework enables our model to gradually improve the accuracy of emotion perception and eliminate emotion biases during the iteration process. Experiments on several benchmarks, e.g., IEMOCAP and MELD, demonstrate that our model has superior empathic response generation capabilities compared to state-of-the-art methods.

---


### 44. [$R^2$-dLLM: Accelerating Diffusion Large Language Models via Spatio-Temporal Redundancy Reduction](https://arxiv.org/abs/2604.18995)

**<font color=#1a73e8>作者：</font>** Zhenbang Du, Kejing Xia, Xinrui Zhong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion Large Language Models (dLLMs) have emerged as a promising alternative to autoregressive generation by enabling parallel token prediction. However, practical dLLM decoding still suffers from high inference latency, which limits deployment. In this work, we observe that a substantial part of this inefficiency comes from recurring redundancy in the decoding process, including spatial redundancy caused by confidence clusters and positional ambiguity, and temporal redundancy caused by repeatedly remasking predictions that have already stabilized. Motivated by these patterns, we propose $R^2$-dLLM, a unified framework for reducing decoding redundancy from both inference and training perspectives. At inference time, we introduce training-free decoding rules that aggregate local confidence and token predictions, and finalize temporally stable tokens to avoid redundant decoding steps. We further propose a redundancy-aware supervised fine-tuning pipeline that aligns the model with efficient decoding trajectories and reduces reliance on manually tuned thresholds. Experiments demonstrate that $R^2$-dLLM consistently reduces the number of decoding steps by up to 75% compared to existing decoding strategies, while maintaining competitive generation quality across different models and tasks. These results validate that decoding redundancy is a central bottleneck in dLLMs, and that explicitly reducing it yields substantial practical efficiency gains.

---


### 45. [Decompose, Structure, and Repair: A Neuro-Symbolic Framework for Autoformalization via Operator Trees](https://arxiv.org/abs/2604.19000)

**<font color=#1a73e8>作者：</font>** Xiaoyang Liu, Zineng Dong, Yifan Bai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Statement autoformalization acts as a critical bridge between human mathematics and formal mathematics by translating natural language problems into formal language. While prior works have focused on data synthesis and diverse training paradigms to optimize end-to-end Large Language Models (LLMs), they typically treat formal code as flat sequences, neglecting the hierarchical logic inherent in mathematical statements. In this work, we introduce Decompose, Structure, and Repair (DSR), a neuro-symbolic framework that restructures autoformalization into a modular pipeline. DSR decomposes statements into logical components and maps them to structured operator trees, leveraging this topological blueprint to precisely localize and repair errors via sub-tree refinement. Furthermore, we introduce PRIME, a benchmark of 156 undergraduate and graduate-level theorems selected from canonical textbooks and expertly annotated in Lean 4. Experimental results demonstrate that DSR establishes a new state-of-the-art, consistently outperforming baselines under equivalent computational budgets. The datasets, model, and code will be released to the public soon.

---


### 46. [FedProxy: Federated Fine-Tuning of LLMs via Proxy SLMs and Heterogeneity-Aware Fusion](https://arxiv.org/abs/2604.19015)

**<font color=#1a73e8>作者：</font>** Tao Fan, Guoqiang Ma, Yuanfeng Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated fine-tuning of Large Language Models (LLMs) is obstructed by a trilemma of challenges: protecting LLMs intellectual property (IP), ensuring client privacy, and mitigating performance loss on heterogeneous data. Existing methods like Offsite-Tuning (OT) secure the LLMs IP by having clients train only lightweight adapters, yet our analysis reveals they suffer from a fundamental performance bottleneck, leaving a significant gap compared to centralized training. To bridge this gap, we introduce FedProxy, a new federated adaptation framework. FedProxy replaces weak adapters with a unified, powerful Proxy Small Language Model (SLM), compressed from the proprietary LLM, to serve as a high-fidelity surrogate for collaborative fine-tuning. Our framework systematically resolves the trilemma through a three-stage architecture: (i) Efficient Representation via server-guided compression to create a resource-friendly proxy; (ii) Robust Optimization through an interference-mitigating aggregation strategy to handle data heterogeneity; and (iii) Effortless Fusion via a training-free "plug-in" mechanism to integrate learned knowledge back into the LLM. Experiments show FedProxy significantly outperforms OT methods and approaches centralized performance, establishing a new benchmark for secure and high-performance federated LLM adaptation.

---


### 47. [AlignCultura: Towards Culturally Aligned Large Language Models?](https://arxiv.org/abs/2604.19016)

**<font color=#1a73e8>作者：</font>** Gautam Siddharth Kashyap, Mark Dras, Usman Naseem  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cultural alignment in Large Language Models (LLMs) is essential for producing contextually aware, respectful, and trustworthy outputs. Without it, models risk generating stereotyped, insensitive, or misleading responses that fail to reflect cultural diversity w.r.t Helpful, Harmless, and Honest (HHH) paradigm. Existing benchmarks represent early steps toward cultural alignment; yet, no benchmarks currently enables systematic evaluation of cultural alignment in line with UNESCO's principles of cultural diversity w.r.t HHH paradigm. Therefore, to address this gap, we built Align-Cultura, two-stage pipeline for cultural alignment. Stage I constructs CULTURAX, the HHH-English dataset grounded in the UNESCO cultural taxonomy, through Query Construction, which reclassifies prompts, expands underrepresented domains (or labels), and prevents data leakage with SimHash. Then, Response Generation pairs prompts with culturally grounded responses via two-stage rejection sampling. The final dataset contains 1,500 samples spanning 30 subdomains of tangible and intangible cultural forms. Stage II benchmarks CULTURAX on general-purpose models, culturally fine-tuned models, and open-weight LLMs (Qwen3-8B and DeepSeek-R1-Distill-Qwen-7B). Empirically, culturally fine-tuned models improve joint HHH by 4%-6%, reduce cultural failures by 18%, achieve 10%-12% efficiency gains, and limit leakage to 0.3%.

---


### 48. [Local Linearity of LLMs Enables Activation Steering via Model-Based Linear Optimal Control](https://arxiv.org/abs/2604.19018)

**<font color=#1a73e8>作者：</font>** Julian Skifstad, Xinyue Annie Yang, Glen Chou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inference-time LLM alignment methods, particularly activation steering, offer an alternative to fine-tuning by directly modifying activations during generation. Existing methods, however, often rely on non-anticipative interventions that ignore how perturbations propagate through transformer layers and lack online error feedback, resulting in suboptimal, open-loop control. To address this, we show empirically that, despite the nonlinear structure of transformer blocks, layer-wise dynamics across multiple LLM architectures and scales are well-approximated by locally-linear models. Exploiting this property, we model LLM inference as a linear time-varying dynamical system and adapt the classical linear quadratic regulator to compute feedback controllers using layer-wise Jacobians, steering activations toward desired semantic setpoints in closed-loop with minimal computational overhead and no offline training. We also derive theoretical bounds on setpoint tracking error, enabling formal guarantees on steering performance. Using a novel adaptive semantic feature setpoint signal, our method yields robust, fine-grained behavior control across models, scales, and tasks, including state-of-the-art modulation of toxicity, truthfulness, refusal, and arbitrary concepts, surpassing baseline steering methods. Our code is available at: this https URL

---


### 49. [ClawCoin: An Agentic AI-Native Cryptocurrency for Decentralized Agent Economies](https://arxiv.org/abs/2604.19026)

**<font color=#1a73e8>作者：</font>** Shaoyu Li, Chaoyu Zhang, Hexuan Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Autonomous AI agents live or die by the API tokens they consume: without paid inference capacity they cannot reason, act, or delegate. Compute-token cost has become the binding resource of the emerging agent economy, yet it is non-transferable: it is account-bound, vendor-specific, and absent from on-chain ledgers. Existing payment rails such as x402 move fiat-backed value between agents, but they do not represent the quantity agents actually burn. As a result, agents can transport purchasing power but cannot quote, escrow, or settle workflows in a unit aligned with compute cost.
We present ClawCoin, a tokenized, compute-cost-indexed unit of account and settlement asset for decentralized agent economies. ClawCoin combines four layers: a robust basket index over standardized prices; an oracle publishing signed fresh attestations; a NAV-based mint/redeem vault with coverage thresholds and rate limits; and an on-chain settlement layer for multi-hop delegations.
We implement a prototype on an Ethereum-compatible L2 and evaluate it using a multi-agent simulator and the OpenClaw testbed. Across single-agent, multi-agent, workflow, and procurement experiments, ClawCoin stabilizes execution capacity under cost shocks, reduces cross-agent quote dispersion, eliminates partial settlements, and sustains cooperative market dynamics that fiat-denominated baselines cannot. These results suggest that compute-indexed units of account can improve decentralized agent coordination.

---


### 50. [Learning Posterior Predictive Distributions for Node Classification from Synthetic Graph Priors](https://arxiv.org/abs/2604.19028)

**<font color=#1a73e8>作者：</font>** Jeongwhan Choi, Jongwoo Kim, Woosung Kang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> One of the most challenging problems in graph machine learning is generalizing across graphs with diverse properties. Graph neural networks (GNNs) face a fundamental limitation: they require separate training for each new graph, preventing universal generalization across diverse graph datasets. A critical challenge facing GNNs lies in their reliance on labeled training data for each individual graph, a requirement that hinders the capacity for universal node classification due to the heterogeneity inherent in graphs -- differences in homophily levels, community structures, and feature distributions across datasets. Inspired by the success of large language models (LLMs) that achieve in-context learning through massive-scale pre-training on diverse datasets, we introduce NodePFN. This universal node classification method generalizes to arbitrary graphs without graph-specific training. NodePFN learns posterior predictive distributions (PPDs) by training only on thousands of synthetic graphs generated from carefully designed priors. Our synthetic graph generation covers real-world graphs through the use of random networks with controllable homophily levels and structural causal models for complex feature-label relationships. We develop a dual-branch architecture combining context-query attention mechanisms with local message passing to enable graph-aware in-context learning. Extensive evaluation on 23 benchmarks demonstrates that a single pre-trained NodePFN achieves 71.27 average accuracy. These results validate that universal graph learning patterns can be effectively learned from synthetic priors, establishing a new paradigm for generalization in node classification.

---


> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-132](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
