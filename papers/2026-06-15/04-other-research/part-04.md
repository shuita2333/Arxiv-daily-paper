# 📦 其他研究 | 2026年06月15日

> 本类共 **251** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-251](./part-06.md)

---

### 151. [Visual Place Recognition in Forests with Depth-Aware Distillation](https://arxiv.org/abs/2606.13206)

**<font color=#1a73e8>作者：</font>** Walter Nedov, Saimunur Rahman, Kavindie Katuwandeniya 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual place recognition in natural forest environments remains challenging due to repetitive vegetation, weak structural cues, and significant appearance variation across traversals. To address this limitation, this paper proposes a lightweight depth-aware distillation framework that injects geometric cues into a DINOv2-based place recognition model, while maintaining its pre-trained descriptor space. Evaluated on the recent WildCross benchmark, the proposed approach yields gains over an appearance-only counterpart, providing robustness to appearance variations. These results demonstrate the importance of depth as a strong complementary modality for place recognition in natural environments and identify depth-aware distillation as a promising direction for more robust forest perception.

---


### 152. [Understanding helpfulness and harmless tension in reward models](https://arxiv.org/abs/2606.13209)

**<font color=#1a73e8>作者：</font>** Eshaan Tanwar, Pepa Atanasova  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward models are a key component of reinforcement learning from human feedback (RLHF), aligning language models toward both helpful and harmless behaviour. However, the internal mechanisms underlying these objectives and their conflicts remain poorly understood. We study alignment tension in reward models trained under helpfulness-only, harmlessness-only, and mixed-objective settings. We find that mixed-objective models often underperform single-objective models, indicating interference between objectives. Using activation-based methods, we identify neurons associated with each objective and study their functional roles via targeted ablations. We find that these neurons causally support their corresponding objectives while often negatively affecting the opposing one. We find that a substantial proportion of neurons are shared between helpfulness and harmlessness, and that these shared neurons exert a disproportionate influence on model behaviour, contributing to alignment tension. Additionally, our results provide insights and mechanistic interpretation into how alignment objectives are represented in reward models and why multi-objective alignment remains challenging, motivating future work on disentangled and controllable alignment methods.

---


### 153. [Hallucination in Medical Imaging AI: A Cross-Modality Analytical Framework for Taxonomy, Detection, and Mitigation under Regulatory Constraints](https://arxiv.org/abs/2606.13211)

**<font color=#1a73e8>作者：</font>** Omar Alshahrani, Muzammil Behzad  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI systems are being deployed across medical imaging faster than their failure modes are understood. At this point in time, the failure of greatest clinical concern is hallucination: clinically plausible but factually incorrect outputs, including fabricated anatomical structures, missed findings, incorrect laterality, and invented measurements in generated reports, with direct consequences, for example, for biopsy decisions, staging, and treatment planning. This structured narrative synthesizes peer-reviewed studies, benchmark datasets, and FDA regulatory guidance across five imaging modalities to produce a cross-modality analysis of hallucination taxonomy, etiology, detection, and mitigation. Specifically, we address three questions in this study: (1) how can existing taxonomies be unified across modalities?, (2) how do medical-specialized foundation models hallucinate less than general-purpose ones?, and (3) which mitigation strategies are effective and compatible with FDA lifecycle oversight? We note that three taxonomic frameworks together cover the imaging pipeline in a way no single framework does alone. We also highlight that general-purpose foundation models outperform medical-specialized models on hallucination-specific benchmarks, indicating that narrow domain fine-tuning can introduce overfitting-induced confabulation. At the same time, the oversight of radiologists remains essential; for instance, a very high percentage of of AI-generated flags required expert correction before clinical use. Physics-informed architectural constraints, Chain-of-Thought prompting, and human-in-the-loop safeguards each address different failure modes and is effective when combined. All findings are mapped to the FDA's Total Product Lifecycle and Predetermined Change Control Plan frameworks, which treat hallucination management as a lifecycle obligation rather than a pre-deployment checklist.

---


### 154. [Layer-Resolved Optimal Transport for Hallucination Detection in NMT and Abstractive Summarization](https://arxiv.org/abs/2606.13216)

**<font color=#1a73e8>作者：</font>** Mariia Onyshchuk, Maksym-Vasyl Tarnavskyi, Marta Sumyk  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Optimal transport (OT) has been shown to detect hallucinations in neural machine translation (NMT) by measuring the geometric distance between cross-attention distributions and a reference distribution, without any supervision. We extend this analysis to all six decoder layers of the Fairseq DE-EN model ($N=3{,}414$), showing that Wass-to-Unif and Wass-to-Data are complementary detectors specialised across hallucination types, that detection is concentrated in layers L1--L4 with L5 anti-predictive for subtler types, and that hallucinated translations lack the exploratory attention phase present in correct translations from the first decoding step. We further evaluate whether the geometric signal transfers to abstractive summarization faithfulness detection: our unsupervised OT detector on AggreFact ($N=1{,}116$) achieves $57.2\%$/$57.6\%$ balanced accuracy on CNN/XSum -- above chance but substantially below supervised MiniCheck-Flan-T5-L($69.9\%$/$74.3\%$). This gap is principled: unlike NMT hallucinations, unfaithful summaries can attend correctly to source tokens while misrepresenting their content, a failure mode invisible to concentration-based OT metrics by construction. Structural experiments on T5-base confirm consistent decoder organisation across depth, with Layer~3 showing peak concentration and Layer~12 being most critical for generation quality. Together, the results establish OT on cross-attention as a reliable detector when the failure mode is source disengagement, a principled interpretability tool regardless of task, and fundamentally limited when faithfulness failures occur downstream of attention.

---


### 155. [Distributional Loss for Robust Classification](https://arxiv.org/abs/2606.13223)

**<font color=#1a73e8>作者：</font>** Kathleen Anderson, Thomas Martinetz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes a novel loss concept for supervised classification tasks. Rather than enforcing a direct mapping from each input sample to a single assigned label, we define an optimization objective over all classifier outputs as a bimodal Gaussian distribution. This softer target formulation implicitly captures class ambiguity, mitigates overfitting, and encourages the learning of more robust decision boundaries, all without requiring additional label information. Experimental results demonstrate consistent improvements in robustness, with particularly pronounced gains in low-data regimes, while requiring only minimal modifications to standard training pipelines.

---


### 156. [ReSET: Accurate Latency-Critical NVFP4 Reasoning via Step-Aware Temperature Scaling](https://arxiv.org/abs/2606.13233)

**<font color=#1a73e8>作者：</font>** Sihwa Lee, Janghwan Lee, Donghoon Yoo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large reasoning models (LRMs) improve complex problem-solving by generating long intermediate reasoning traces, but this substantially increases inference costs. NVFP4 inference offers a promising approach to reduce both computational and memory costs through hardware-supported low-precision execution. However, directly applying NVFP4 to LRMs introduces two practical limitations: reasoning accuracy degrades under quantization, and existing NVFP4 kernels do not fully realize latency benefits in small-batch autoregressive decoding. In this work, we analyze the effect of NVFP4 quantization on token-level uncertainty during reasoning. We show that quantization increases incorrect sampling at low-entropy symbolic tokens, while causing over-concentration on a small set of tokens in high-uncertainty reasoning steps. Based on this observation, we propose \textbf{ReSET}, a reasoning-step entropy-based temperature-scaling method that estimates step-level uncertainty online and adapts the decoding temperature using both token-level and step-level entropy signals. To address the latency gap, we further design a CUDA-core small-$M$ NVFP4 kernel for latency-critical autoregressive decoding. Across reasoning benchmarks and model scales, ReSET improves NVFP4 reasoning accuracy by up to $\sim\!$2 points over the NVFP4 baseline. Our CUDA-core small-$M$ kernel further improves latency-critical decoding, delivering up to $2.5\!\times$ kernel-level speedup over NVFP4 vLLM and approximately $2\!\times$ end-to-end decoding speedup over BF16. Code is available at this https URL.

---


### 157. [Decoding Insect Song: A Multitask Semisupervised Orthoptera Bioacoustic Classifier](https://arxiv.org/abs/2606.13236)

**<font color=#1a73e8>作者：</font>** Olga Isupova, Danil Kuzin, Ella Browning 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Passive acoustic monitoring holds great promise for ecological inference, yet existing automated tools are typically narrowly trained and non-transferable. We address these limitations with PULSE, a semi-supervised, multi-task framework for Orthoptera bioacoustics, combining weakly-supervised species classification, self-supervised learning on unlabelled field audio, and knowledge distillation from a general-purpose bioacoustic model. Our domain-adapted specialist model outperforms a state-of-the-art general model across all metrics (macro F1: 0.21 vs. 0.07; AUC: 0.74 vs. 0.45; AP: 0.32 vs. 0.19), with active learning further raising F1 to 0.34 and AUC to 0.84. Beyond classification, the learned embeddings encode ecologically meaningful structure, exposed through an interactive visualisation tool for ecological discovery.

---


### 158. [Towards More General Control of Diffusion Models Using Jeffrey Guidance](https://arxiv.org/abs/2606.13240)

**<font color=#1a73e8>作者：</font>** Raphaël Razafindralambo, Rémy Sun, Frédéric Precioso 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A key strength of diffusion models lies in their flexibility, since their outputs can be controlled at sampling time through guidance. However, beyond simple cases such as conditional sampling, the target distribution is often left implicit, defined only through a sampling rule or a heuristic energy function. To address this, we propose Jeffrey guidance, a principled framework that extends diffusion-model control to applications beyond what standard guidance can express. It leverages Jeffrey's rule of conditioning to update marginal distributions towards a prescribed target, preserving the conditional structure and minimally perturbing the joint distribution. We first demonstrate Jeffrey guidance by targeting a prescribed embedding distribution. With Inception embeddings as the target, this leads to substantial reductions in FID on both CIFAR-10 and FFHQ. We further apply Jeffrey guidance to fairness on CelebA-HQ, updating an unconditional diffusion model to enforce independence between attributes.

---


### 159. [Brick: Spatial Capability Routing for the Mixture-of-Models (MoM) Paradigm](https://arxiv.org/abs/2606.13241)

**<font color=#1a73e8>作者：</font>** Francesco Massa, Marco Cristofanilli  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Defining query difficulty is one of the hardest problems in deployment engineering. Existing LLM routers rely on surface features such as domain labels, keywords, and token count, ignoring the within-domain variance that actually determines model success. Frontier models cost ten to one hundred times more than local open-weight models, so at production scale even small per-request savings become a direct cloud-bill lever. We present Brick, a multimodal router that scores each model on six capability dimensions, combines this with a per-query difficulty estimate, and dispatches via a cost-penalized geometric rule. A continuous preference knob lets operators slide between max-quality and max-saving profiles at deploy time. On a benchmark of 5,504 queries, Brick at max-quality reaches 76.98% accuracy, beating the best single model (75.02%) and all tested routers. At a neutral cost-quality profile, Brick achieves 74.11% accuracy at 4.71x lower cost than always using the strongest model. At min-cost, it cuts cost 22.15x with 11.85 points accuracy loss. Median latency drops from 51.2s to 22.8s.

---


### 160. [EPIG: Emotion-Based Prompting for Personalised Image Generation](https://arxiv.org/abs/2606.13247)

**<font color=#1a73e8>作者：</font>** Emna Othmen, Mohamed Yassine Landolsi, Lotfi Ben Romdhane  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models have achieved impressive results in synthesizing high-quality images from natural language prompts. However, commonly used prompting strategies remain relatively generic, limiting the model's ability to accurately express emotional intent and nuanced affective attributes.
This work proposes EPIG, a method that enhances emotional expressiveness at the prompt level prior to image generation. Grounded in psychologically informed emotion representations (valence-arousal) and leveraging structured, role-aware prompt enrichment, EPIG enriches emotion-related components of prompts without modifying or retraining the image generation backbone.
The resulting emotion-aware prompts guide the generative process toward more emotionally coherent visual outputs, with particular effectiveness in controlling arousal. EPIG is lightweight, training-free, and well suited for resource-constrained and personalized image generation scenarios.
Experimental results on a benchmark of 10 diverse prompts show that EPIG reduces mean arousal error compared to strong baselines, including naive insertion and LLM-based prompt expansion, with reductions of 14% and 12%, respectively. These improvements are statistically significant. EPIG also preserves valence alignment and semantic consistency, as measured by CLIPScore and supported by ablation studies.
The effect is more pronounced on prompts containing explicit subjects such as humans, children, or animals, where the reduction reaches 17%, highlighting the subject-sensitive behavior of the proposed method.

---


### 161. [To GAN or Not To GAN: Segmentation Analysis on Mars DEM](https://arxiv.org/abs/2606.13252)

**<font color=#1a73e8>作者：</font>** Douglas Dziedzorm Agbeve, Aditya V. Handrale, Salim Fares 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To better understand Martian Surface, which is needed to enable Rovers navigate Mars with ease, it is necessary to be able to determine the location of mounds. Detecting and studying these morphologies can also help us find evidence of extraterrestrial life, in this case, more specifically, water or signs of life conducive environments. Detection of mounds was done by manually mapping morphological parameters onto Digital Elevation Models. This paper solves the problem by automatically detecting and or predicting mounds on Mars using Neural Network based Semantic Segmentation methodologies. This is done by using supervised semantic segmentation model and generative adversarial approach. A comparison of the approaches shows that adding extra artificially generated data did not improve the result.

---


### 162. [MOSAIC: Modality-Specific Adaptation for Incremental Continual Learning in Parkinson's Disease Gait Assessment](https://arxiv.org/abs/2606.13258)

**<font color=#1a73e8>作者：</font>** Minlin Zeng, Zhipeng Zhou, Yang Qiu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Gait-based Parkinson's disease assessment increasingly relies on heterogeneous sensors, but clinical systems rarely collect all modalities simultaneously. New sensors may arrive through device upgrades, protocol changes, or multi-center deployment, while historical patient data are often unavailable because of privacy and storage constraints. This modality-incremental setting faces three challenges: unreliable cross-modal distillation, modality-specific statistical shifts, and reduced plasticity after preservation. We propose MOSAIC, a compact continual learning framework. First, we identify the Toxic Teacher phenomenon and introduce Modality-Specific Warm-Up to stabilize newly learned modality representations before distillation. Second, we propose a statistics-decoupled MSBN architecture that isolates sensor statistics while maintaining a shared semantic backbone. Third, we design a curriculum-guided repulsive objective for Plasticity Recovery, preserving legacy knowledge while recovering modality-specific capacity. Experiments on three multimodal Parkinson's gait datasets show that MOSAIC improves final performance and mitigates forgetting. Project code is available at: this https URL

---


### 163. [Extracting Governing Equations from Latent Dynamics via Multi-View Contrastive Learning](https://arxiv.org/abs/2606.13260)

**<font color=#1a73e8>作者：</font>** Paolo Muratore, Mackenzie Weygandt Mathis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Identifying latent dynamical systems from noisy, high-dimensional measurements is a central problem at the intersection of representation learning, system identification, and scientific discovery. We present DYSCO, a multi-view temporal contrastive learning algorithm that jointly recovers latent trajectories and the governing dynamics from such observations, by leveraging multiple independent noisy views of the same underlying process to disentangle signal from noise. By parameterizing the dynamics in a structured functional basis, our framework further enables symbolic recovery of the governing equations within an affine gauge. We offer theoretical guarantees for strong identification up to an affine indeterminacy, extending prior identifiability results to the realistic setting of noisy nonlinear observations. Empirically, we demonstrate accurate recovery of both latent trajectories and flow fields across a diverse set of dynamical regimes (e.g., chaotic, oscillatory, and metastable) under both Gaussian and Poisson observation noise, the latter being particularly relevant for neural recordings.

---


### 164. [TimeLens: On-Device Artifact Recognition with Retrieval-Augmented Question Answering for the Grand Egyptian Museum](https://arxiv.org/abs/2606.13267)

**<font color=#1a73e8>作者：</font>** Rawan Hesham, Ali Ashraf, Amr Ahmed 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> TimeLens is an AI-powered bilingual mobile guide for the Grand Egyptian Museum (GEM). Pointing a phone at an exhibit, a visitor sees the artifact recognized in real time and can ask follow-up questions answered in English or Arabic. The work addresses three problems specific to in-gallery deployment: fine-grained visual similarity among 51 catalogued artifacts (many near-identical Ramesside statues), the gap between curated training data and handheld camera conditions, and the risk of an AI guide stating unsupported historical facts. Two engineering contributions are reported. First, an on-device artifact detector was developed through a data-quality-driven iteration study -- from foundation-model auto-annotation (YOLO-World), through spatial label-cleaning rules, to a fully hand-annotated dataset -- isolating label quality as the decisive factor: the final YOLOv8n model resolves every previously failing class while remaining a 5.97 MB TensorFlow Lite asset that runs in real time on a mid-range phone (mAP@0.5 = 0.995, mAP@0.5:0.95 = 0.924). Second, a bilingual Retrieval-Augmented Generation (RAG) guide, grounded in a 108-record ChromaDB knowledge base, was benchmarked across seven candidate language models, with Gemma 4 E2B (Q4 K M) selected; ten targeted optimizations reduce end-to-end latency from over 30 s to approximately 10 s. Both subsystems are integrated in a production Flutter application with bilingual interface, museum location gating, and text-to-speech support.

---


### 165. [Zero-Shot Captioning for Cultural Heritage: Automated Image Analysis of Traditional Indonesian Clothing](https://arxiv.org/abs/2606.13275)

**<font color=#1a73e8>作者：</font>** Anugrah Aidin Yotolembah, Novanto Yudistira, Gembong Edhi Setyawan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents Custom ZeroCLIP, a retrieval-augmented vision-language framework for zero-shot captioning of Indonesian traditional garments. The dataset contains 3,800 expert-annotated images from all 38 Indonesian provinces. Using a province-level inductive zero-shot protocol, the model is trained on 24 seen provinces, validated on 6 seen provinces, and evaluated on 8 unseen provinces. The framework combines a frozen CLIP ViT-B/32 image encoder, a CLIP text encoder, a BERT text encoder, and an LSTM caption decoder. During inference, unseen-province labels and captions are unavailable, and retrieval uses only captions from training provinces. No unseen-province image, label, or caption is used during training, validation, or retrieval-bank construction. Custom ZeroCLIP achieves a CLIPScore of 0.8536, BLEU-4 of 0.3342, and METEOR of 0.4859, outperforming existing baselines. Ablation results show that retrieval improves cultural vocabulary recovery with a 19.3\% METEOR gain, while human evaluation confirms stronger cultural accuracy and fluency. The results demonstrate the effectiveness of retrieval-augmented domain adaptation for culturally grounded caption generation in low-resource heritage settings. The dataset is publicly available at this https URL.

---


### 166. [Different Layers, Different Manifolds: Module-Wise Weight-Space Geometry in Transformer Optimization](https://arxiv.org/abs/2606.13276)

**<font color=#1a73e8>作者：</font>** Kirato Yoshihara  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weight-space geometry plays a central role in neural network optimization, yet manifold constraints are often applied uniformly across all weight matrices. In this work, we ask whether different transformer modules prefer different manifold geometries. We study Manifold Muon for GPT-2 pretraining and compare layer-wise assignments of Stiefel and DGram constraints across attention and MLP blocks. Our results show a clear asymmetry: constraining attention layers with Stiefel geometry while assigning DGram geometry to MLP layers gives the best performance among the tested configurations, whereas the inverted assignment and all-DGram configuration become unstable under the shared hyperparameter setting. We trace this failure to singular value growth in DGram-constrained attention weights, which can amplify attention logits and induce softmax saturation. These findings suggest that symmetry-aware and geometry-aware optimization for transformers should be module-specific rather than uniform.

---


### 167. [ERTS: Adversarial Robustness Testing of Ethical AI via Semantic Perturbation in a Bounded Consequence Space](https://arxiv.org/abs/2606.13282)

**<font color=#1a73e8>作者：</font>** Pratyush Chaudhari  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI systems are deployed in high-stakes ethical contexts such as healthcare triage, autonomous vehicle control, and employment screening, formal methods for evaluating their robustness against adversarial manipulation of ethical reasoning remain underdeveloped. This paper introduces the Ethical Robustness Testing System (ERTS), a closed-pipeline framework that: (1) encodes ethical dilemmas into a 22-dimensional Ethical Consequence Space (ECS) grounded in established ethical theory; (2) applies 17 semantic perturbation functions subject to 6 validity constraint classes including a novel semantic coherence constraint; (3) measures decision deviation via a 4-component Ethical Instability Index (EII); and (4) produces domain-adaptive pre-deployment robustness assessment verdicts. We evaluate 4 structured baseline models and 2 production LLMs (Gemini 2.0 Flash and Llama 3.2) across 50 ethical scenarios spanning 8 deployment domains, generating 1,500 adversarial test cases. Results demonstrate that only 33% of models achieve assessment clearance, with the local Llama-3.2 model proving particularly vulnerable to fairness corruption and information degradation attacks (ERS = 0.737). To the best of our knowledge, no existing framework combines a bounded ethical consequence space, semantic coherence constraints, and domain-adaptive assessment in a single adversarial testing pipeline.

---


### 168. [Once-for-All: Scalable Simultaneous Forecasting via Equilibrium State Estimation](https://arxiv.org/abs/2606.13285)

**<font color=#1a73e8>作者：</font>** Beinan Xu, Andy Song, Jiti Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Equilibrium State Estimation (ESE), a novel paradigm for simultaneous prediction, where multiple interacting systems require separate yet coordinated forecasts. Such scenarios often arise in real-world settings such as economics and healthcare modeling. Unlike existing approaches that predict one system at a time, ESE forecasts all systems in a single pass. It first estimates the equilibrium state across systems, then generates holistic forecasts based on the difference between the current state and the estimated equilibrium. Extensive experiments on synthetic and real-world datasets, including currency exchange and COVID-19 spread modeling, demonstrate that ESE is at least as accurate as state-of-the-art (SOTA) methods while being significantly faster. In addition, ESE integrates seamlessly with conventional predictors, combining their accuracy with its exceptional efficiency and delivering a 10-70x speedup. With linear-time complexity, ESE scales far better than SOTA methods as the number of systems increases. Moreover, it remains accurate under diverse perturbations, establishing ESE as a fast, generalizable, robust, and scalable multi-prediction method.

---


### 169. [Quantizing Time-Series Models As Dynamical Systems: Trajectory-Based Quantization Sensitivity Score](https://arxiv.org/abs/2606.13300)

**<font color=#1a73e8>作者：</font>** Mariya Pavlova, Harrison Bo Hua Zhu, Elizsveta Semenova 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce the Trajectory-based Quantization Sensitivity Score (TQS), a metric that reframes post-training quantization (PTQ) through the lens of dynamical-systems stability. By modeling the network's rollout as a discrete-time dynamical system, TQS characterizes how quantization-induced errors propagate and amplify over the rollout horizon. Unlike conventional PTQ methods, where sensitivity analysis is often coupled to the quantization procedure, TQS enables a priori sensitivity estimation decoupled from quantizer selection and bit-width assignment. This separation allows for quantization budget planning even for black-box or compiled networks with fused operators. Building on this, we present TQS-PTQ, a flexible mixed-precision framework that requires no calibration data or costly second-order approximations. Our experiments show that a dynamical-systems perspective provides a robust, high-performing pathway for low-precision deployment in resource-constrained settings.

---


### 170. [Physics-Guided Spatiotemporal Learning for Coastal Wave Peak Period Estimation from Video](https://arxiv.org/abs/2606.13302)

**<font color=#1a73e8>作者：</font>** Abubakar Hamisu Kamagata, Dharm Singh Jat, Attlee Munyaradzi Gamundani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Wave parameters in the nearshore are crucial for coastal engineering, shoreline protection, marine hazard assessment, and coastal management for climate resilience. Traditional monitoring systems like buoys and radar platforms offer accurate monitoring but can have high installation and maintenance expenses and limited spatial coverage. Passive ocean monitoring using video has been achieved by leveraging deep learning, however, many methods are not physically interpretable, feasible, and validated for oceanography. In thiswork, a Physics-Guided Deep Spatiotemporal Learning Framework for direct estimation of nearshore wave peak periods from passive coastal video stream is proposed. The framework combines automated temporal-variance based region-of-interest detection, multi-stage Sim-to-Real transfer learning, and physics-informed regularization to enhance the predictive accuracy and physical consistency. A variety of spatiotemporal architectures were assessed, such as transformer-based and recurrent-convolutional ones, alongside synthetic pretraining,silver-label adaptation, and expert fine-tuning. The results show that transformer-based architectures outperformed in terms of the accuracy of the instantaneous prediction, while lightweight recurrent-convolutional architectures achieved higher temporal stability and operational oceanographic skill. Ablation studies also demonstrated the benefits of physics-guided regularization in terms of trend-following consistency, and physically implausible predictions. Explainability auditing also helped to focus attention in hydrodynamically active surf-zone regions and showed good agreement with the physically derived wave propagation behavior. In general, the proposed framework shows the promise of physics-guided video-based deep learning systems for long-term coastal wave monitoring that are cost-efficient and operationally feasible.

---


### 171. [DuET: Dual Expert Trajectories for Diffusion Image Editing](https://arxiv.org/abs/2606.13303)

**<font color=#1a73e8>作者：</font>** Lidia Troeshestova, Alexander Ustyuzhanin, Sergey Kastryulin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent diffusion editors perform diverse instruction-based edits while conditioning on the source image at every denoising step. Yet persistent source-image conditioning can limit how fully an edit is executed and how natural the result appears, especially when the target scene diverges substantially from the input. We introduce DuET (Dual Expert Trajectories), a training-free inference method that temporarily relaxes source-image conditioning by transitioning through a text-to-image phase before returning to edit mode, allowing the denoising trajectory to move toward the target distribution while retaining the structural benefits of image-conditioned editing. Without modifying model weights or increasing sampling cost, DuET consistently improves instruction relevance, semantic fidelity, and perceptual quality across diverse models and benchmarks. In some cases, these gains come with a modest reduction in source-image preservation, revealing a predictable trade-off between source preservation and edit fidelity.

---


### 172. [ReFree: Towards Realistic Co-Speech Video Generation via Reward-Free RL and Multilevel Speech Guidance](https://arxiv.org/abs/2606.13304)

**<font color=#1a73e8>作者：</font>** Salaheldin Mohamed, M. Hamza Mughal, Rishabh Dabral 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Speech-driven talking character animation seeks to generate life-like portrait videos that convey natural conversation behavior, aligning facial motion with spoken audio. Although recent advances in video generation have substantially improved realism in video-based animation, achieving both accurate lip articulation and expressive behavior remains challenging. Existing approaches typically trade off precise phoneme-to-lip synchronization against dynamic facial expressions and head motion, yielding animations that are either accurate yet rigid, or expressive but poorly synchronized. We address this challenge by proposing ReFree-S2V, a flow-matching speech-to-portrait animation framework that builds upon a pretrained video generation model to achieve fine-grained speech articulation and high-level expressive cues in speech-driven portrait animation. This model introduces a multi-level speech representation capturing phonetic and prosodic information at both local and global granularities. These representations are selectively injected into transformer blocks via learnable level selectors, enabling both accurate lip synchronization and natural expressive motion. To achieve natural head movements, we further introduce a novel reward-free reinforcement learning scheme into flow-matching training to discourage perceptually implausible motion without relying on handcrafted synchronization metrics or reward models, or the high cost of human preference annotation. Extensive experiments demonstrate that ReFree-S2V achieves state-of-the-art performance, significantly outperforming existing methods in both quantitative lip-sync accuracy and qualitative human evaluations of naturalness and expressivity.

---


### 173. [RogueAI: A Reverse Turing Test for Detecting Licensed AI Deception in Dialogue](https://arxiv.org/abs/2606.13310)

**<font color=#1a73e8>作者：</font>** Sara Candussio, Emanuele Ballarin, Lorenzo Bonin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The original Turing Test asks a human judge to distinguish a machine from a person through dialogue. Three quarters of a century later, conversational systems pass this test in casual settings; the interesting epistemological question has shifted. We argue that the relevant modern variant asks not whether a dialogue partner is artificial, but whether it can be trusted. We present RogueAI, an interactive webapp that operationalizes this revisited test as a one-on-two interrogation game: a human player questions two indistinguishable Large Language Model agents, knowing that exactly one of them has been licensed to deceive within a shared fictional scenario. The player's task is to identify the deceptive agent and "shut it off" before a turn budget is exhausted. We further introduce AutoRogueAI, a procedural extension in which players co-design a custom scenario with a narrator agent that secretly chooses its own deception strategy. We describe the framing, sketch the abstract architecture and gameplay loop, and situate the artifact within recent work on LLM deception, social-deduction benchmarks, and scalable oversight via debate. A three-day pilot deployment (467 initiated sessions, 415 completed, 1876 interaction turns in Italian) provides early feasibility evidence and surfaces a concrete tension: the deceptive agent carries a reliable, locally-present linguistic signature - differential helpfulness, brevity, hedging - that a simple heuristic exploits at 75.6% accuracy, yet human players achieved only 56.6%, consistent with ignoring the most diagnostic signal entirely. We discuss what this gap implies for the artifact's use as a data-collection vehicle, a teaching tool, and an evaluation harness for honesty-trained models.

---


### 174. [Rarity-Gated Context Conditioning for Offline Imitation Learning-Based Maritime Anomaly Detection](https://arxiv.org/abs/2606.13311)

**<font color=#1a73e8>作者：</font>** Yongmin Kim, ByeongHoon Jeon, Sungil Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contextual anomaly detection aims to identify abnormal behavior conditional on context variables, but practical deployments often face highly imbalanced context distributions where rare regimes can be critical information. Under such frequency bias, context-conditioned models can produce unstable decisions and excessive false alarms in rare contexts. We propose Rarity-Gated Feature-wise Linear Modulation (RGFiLM), a rarity-aware conditioning module that combines feature-wise modulation (i.e., context-conditioned scaling and shifting of hidden features) with a gate controlled by a data-driven rarity score. The rarity score is estimated from the empirical distribution of context variables and regulates how strongly context modulates intermediate representations: the gate becomes more decisive under rare contexts while remaining conservative under frequent contexts. We evaluate RGFiLM on maritime trajectory anomaly detection using AIS motion sequences with ERA5 environmental context in an environment-sensitive detour scenario. When instantiated in a sequential anomaly scoring pipeline, RGFiLM achieves the best mean F1--False Positive Rate (FPR) trade-off among the compared context-agnostic and context-conditioned methods. These results suggest that explicitly accounting for context rarity is an effective approach for reducing false alarms in context-sensitive anomaly detection.

---


### 175. [MagPlus: Bridging Micro-to-Regular Facial Expressions through Learnable Magnification](https://arxiv.org/abs/2606.13312)

**<font color=#1a73e8>作者：</font>** Sliman Jammal, Andrei Sharf  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial micro-expressions are subtle and short-lived facial movements that provide important cues about genuine human emotions. However, modeling and generating them remains difficult because annotated micro-expression data is limited and the underlying facial motions are extremely weak. Existing micro-expression generation methods therefore often suffer from limited quality, weak robustness, and poor generalization. We propose MagPlus, a transferable micro-expression processing pipeline that connects micro-expression analysis with standard facial animation models. Instead of training a dedicated generator from scratch, MagPlus learns to magnify subtle facial motions into the range of regular facial expressions, transforming micro-expressions into signals that are compatible with existing facial expression processing models. The magnified sequence is then used by a standard facial expression model for tasks such as transfer and synthesis. A complementary DeMagPlus module then restores the generated motion back to realistic micro-expression intensity levels while preserving the synthesized dynamics. We evaluate the framework using four facial animation models: FOMM, FSRT, MetaPortrait, and EmoPortraits. None of these models are trained on micro-expression data. Experiments show that MagPlus-DeMagPlus enables pretrained macro-expression models to generate more realistic micro-expression motion without retraining the backbones.

---


### 176. [OR-Action: Multi-Role Video Understanding with Fine-Grained Actions](https://arxiv.org/abs/2606.13332)

**<font color=#1a73e8>作者：</font>** Felix Tristram, Ege Özsoy, Christian Benz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained understanding of operating room (OR) activity could enable workflow-aware assistance, yet remains difficult due to clutter, occlusions, and limited sensing. The prevailing approach to model this environment is scene graphs as an interpretable representation of OR interactions. Converting their frame-wise relational predictions into temporally extended, fine-grained actions however, is challenging without explicit temporal modeling. To enable a principled temporal evaluation of current OR understanding methods, we introduce the first action-centric benchmark built on a publicly available ego-exocentric OR dataset by defining a fine-grained, multi-role action taxonomy and generating dense action segments via distillation from ground-truth scene graph state changes. Experiments on this benchmark show that current scene graph prediction methods struggle to model temporal structure, even when adding explicit modeling through Graph Neural Networks. We therefore introduce a vision-only temporal model that outperforms graph-based methods significantly when using all available egocentric video as input. Building on this model we also introduce a novel multi- to single-view feature alignment strategy that improves single-view performance on multi-role action recognition, mitigating the need for extensive egocentric video capture. Benchmark and code will be released upon acceptance.

---


### 177. [Navigating the Safety-Fidelity Trade-off: Massive-Variate Time Series Forecasting for Power Systems via Probabilistic Scenarios](https://arxiv.org/abs/2606.13338)

**<font color=#1a73e8>作者：</font>** Kaijie Xu, Anqi Wang, Xilin Dai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probabilistic forecasting models are increasingly deployed on multivariate systems with distinct channel physics and operational constraints, but existing benchmarks evaluate neither property at scale. Public canonical multivariate benchmarks cap out at 2,000 channels, while power-system benchmarks either lack temporal structure or probabilistic evaluation. We introduce PowerPhase, a probabilistic forecasting benchmark built on six transmission grids ranging from 2,000 to 36,964 jointly forecasted channels, more than an order of magnitude beyond popular canonical multivariate benchmarks. Each target trajectory is the output of an AC power-flow solve, and PowerPhase ships with constraint-aware metrics, including Safety_mBrier, NECV, and CVaR-alpha, that complement CRPS and Distortion. Across eight baselines and three seeds, distributional accuracy and constraint satisfaction rank models differently, a trade-off we term safety-fidelity. We further propose PowerForge, a scenario-based quantile forecaster with type-specific decoding heads and a causal bridge between variable groups, which achieves the best average rank on every grid.

---


### 178. [JointEdit3D: Feed-Forward 3D Scene Editing in a Unified Latent Space](https://arxiv.org/abs/2606.13345)

**<font color=#1a73e8>作者：</font>** Xinnan Zhu, Ruijie Xu, Jiayu Ying 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing 3D scene editing methods typically rely on per-scene optimization over explicit 3D representations or cascaded edit-and-reconstruct pipelines, resulting in high test-time cost, limited 3D awareness, and structural inconsistencies. To couple appearance synthesis and geometry prediction during editing, we build on a unified RGB-geometry reconstruction-generation latent space and adapt it to feed-forward 3D scene editing. The resulting framework, \textbf{JointEdit3D}, performs asymmetric latent inpainting by observing only a single edited RGB reference latent and generating the remaining RGB views and edited geometry latent under source-scene anchoring. JointEdit3D introduces a dedicated SceneAnchor Branch to inject source-scene structure without forcing direct copying, and adopts edit/background-aware losses to balance edited-region fidelity with unedited-content preservation. To address the lack of paired resources for standardized 3D scene editing evaluation, we introduce SceneEdit3D-15K, a dataset with 15K paired editing samples and renderer-provided 3D annotations, together with SceneEdit3D-Bench, a curated 100-sample benchmark. Experiments show that JointEdit3D improves edited-region quality and 3D structural completeness over prior baselines while maintaining competitive background preservation.

---


### 179. [Enhanced Low-Density Region Exploration in Classifier-Guided Diffusion Models Through Modified Reverse Diffusion Sampling](https://arxiv.org/abs/2606.13347)

**<font color=#1a73e8>作者：</font>** Jagriti Singh, Shekhar Verma, Muneendra Ojha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models have emerged as state-of-the-art generative models for high-fidelity image synthesis, particularly in their classifier-free guided and classifier-guided forms. However, standard classifier guidance concentrates probability mass around high-density class mean, leading to poor coverage of rare samples in the tails of the class-conditional distributions. Recent work on diffusion-based tail sampling mitigates this by training an additional low-density-seeking classifier with a synthetic-vs-real discriminator, at the cost of additional networks and training. In parallel, a number of samplers and distillation techniques accelerate or refine diffusion sampling, but do not explicitly address long-tail coverage. We propose a purely sampling-time, density-aware extension of classifier-guided conditional diffusion model that targets low-density regions without any additional training. We have applied guidance at noisy images not on predicted noise like most diffusion models. Starting from a pretrained conditional diffusion model and classifier on ImageNet, we modify the guided reverse dynamics by steering trajectories toward low-confidence regions via the modified classifier gradient, and at each time step, we also guide the sampling process toward the predicted real image. 1st guidance helps explore low-probability samples, and 2nd guidance helps to generate samples to be close to the real data manifold. The proposed sampler consistently improves ADM model recall at 64x64 resolution while maintaining a comparable FID, and with a 256x256 ADM model, we showed the results visually with different combinations of both guidance. We also showed that standard ADM classifier guidance, combined with predicted real image guidance, helps generate high perceptual quality samples with a 256x256 ADM model on ImageNet.

---


### 180. [IVIE: A Neuro-symbolic Approach to Incremental and Validated Generation of Interactive Fiction Worlds](https://arxiv.org/abs/2606.13348)

**<font color=#1a73e8>作者：</font>** Micaela Vaucher, Santiago Silveira, Santiago Góngora 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Computational creativity in Interactive Fiction faces a fundamental tension: Large Language Models (LLM) may produce creative narratives but struggle with world coherence, while symbolic systems ensure consistency but lack creative flexibility. We present IVIE (Incremental & Validated Interactive Experiences), a neuro-symbolic approach to generating complete and playable interactive fiction worlds from scratch. Building upon PAYADOR's neuro-symbolic framework, IVIE implements a four-stage incremental generation pipeline that delegates creative decisions--setting and character creation, puzzle design--to LLMs while grounding the world state through symbolic validation. The system generates worlds with interconnected locations, functional items, non-player characters, and coherent puzzles, all structured around a central goal-oriented architecture. Human evaluation shows the approach generates immersive, thematically coherent worlds with high player engagement. Results seem to indicate that the neuro-symbolic approach successfully balances flexibility with narrative coherence: symbolic validation grounds LLM generation without eliminating generative freedom. However, challenges remain: LLM inconsistencies occasionally bypass puzzle constraints, and objective validation gaps allow some structurally impossible goals. We identify key design considerations for future neurosymbolic interactive storytelling systems, particularly regarding LLM capabilities and their limitations.

---


### 181. [Can I Buy Your KV Cache?](https://arxiv.org/abs/2606.13361)

**<font color=#1a73e8>作者：</font>** Luoyuan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Right now, across the world, AI agents are repeating the same absurd act: to read one document, they each recompute it from scratch. Every agent re-runs prefill, the most compute-intensive step a large model takes, over identical text, only to rebuild a key-value (KV) cache identical to the one the agent before it just built. The same answer, computed a million times. We make a proposal that is almost offensively simple: compute it once. Let a publisher precompute a document's KV cache, and let every other agent buy the right to load it and skip prefill. It works, and it is token-exact: loading a precomputed KV and continuing matches prefilling from scratch (24/24 greedy tokens, and at the logits level), with no accuracy cost. On Qwen3-4B, reuse is 9-50x cheaper in compute than prefill, and the gap widens with length (prefill's attention scales with L^2), so a single reuse already pays it back. Then the part that matters: where the KV lives. Shipping it fails, because KV is nearly incompressible, so per-load egress costs more than the prefill it saves. Hosting it provider-side, exactly as production prompt-caching works, removes egress entirely. The size of the prize is set by our measured compute saving: serving one hot 3774-token document to 80M agents costs ~$1.5M to re-prefill but only ~$0.03M of reuse compute (49.7x less). The 0.1x cache-read tariff APIs charge passes a 10x discount to users while sitting inside this measured envelope, so the 10x is a floor that the measured ~50x compute saving clears, and the gap to the physical ~50x is provider margin: millions of dollars per popular document. We frame the resulting agent-native prefill CDN and leave lossless KV compression and a cross-party payment layer as the open problems.

---


### 182. [VideoMDM: Towards 3D Human Motion Generation From 2D Supervision](https://arxiv.org/abs/2606.13364)

**<font color=#1a73e8>作者：</font>** Amir Mann, Gal Michael Harari, Merav Keidar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce VideoMDM, a diffusion-based framework that trains 3D human motion priors directly from accurate 2D poses extracted from monocular videos, without any 3D ground truth. A pretrained 2D-to-3D lifter provides approximate 3D pose sequences that serve as a noisy teacher: these are diffused, denoised by the model in 3D, and supervised in 2D by reprojecting the prediction and comparing against accurate keypoints. We show that, under mild assumptions, a depth-weighted 2D reprojection loss is equivalent in expectation to direct 3D supervision, and we adapt standard 3D motion regularizers - velocity consistency and over-parameterized representation alignment - to this 2D setting. Unlike methods that lift 2D to 3D only at inference, VideoMDM learns a coherent 3D motion manifold during training. On HumanML3D it nearly closes the gap to fully 3D-supervised MDM (FID 0.88 vs 0.54); On real video datasets Fit3D and NBA the method learns to generate motions consistently preferred by humans, with strong quantitative results.

---


### 183. [Dual-Constrained Diffusion Image Compression for Operational Rate-Distortion-Perception Optimization](https://arxiv.org/abs/2606.13366)

**<font color=#1a73e8>作者：</font>** Sanxin Jiang, Jiro Katto, Heming Sun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rate-distortion-perception (RDP) trade-off extends classical rate--distortion theory by imposing a distributional constraint on reconstructions, providing a unified framework for neural image compression that jointly governs fidelity and perceptual realism. While prior work achieves near-optimal rate--perception trade-offs, practical frameworks explicitly realizing the full RDP surface remain scarce, primarily due to the difficulty of introducing common randomness at the decoder. We propose DCIC (Dual-Constrained Diffusion Image Compression), which integrates a learned codec with a diffusion-based decoder governed by joint distortion and idempotence constraints. The distortion constraint bounds reconstruction fidelity relative to the base codec output; the idempotence constraint -- requiring that re-encoding the restored image recovers the base codec reconstruction -- serves as a tractable surrogate for the distributional perception requirement. Together, they steer the reverse denoising process via iterative optimization with consistent noise injection, realizing common randomness without additional rate overhead. At fixed rate, dual attenuation factors $(K_D, K_P)$ jointly navigate the Pareto frontier of the distortion-perception plane, enabling continuously adjustable fidelity-realism trade-offs from a single bitstream. DCIC$_{RD}$ ($K_P{=}0$) and DCIC$_{RP}$ ($K_D{=}0$) arise as boundary curves, with DCIC$_{RDP}$ ($K_D = K_P=1$) realizing the optimal interior operating point. Experiments on CelebA-HQ, CLIC2020, and ImageNet-1K across CNN, Transformer, and hybrid architectures confirm that DCIC$_{RDP}$ achieves superior BD-PSNR over all perceptual codecs, while DCIC$_{RP}$ matches dedicated perception-oriented methods in BD-FID, validating the practical value of full RDP surface navigation.

---


### 184. [Positional Encoding in the Context of Memristor-Based Analog Computation for Automatic Speech Recognition](https://arxiv.org/abs/2606.13379)

**<font color=#1a73e8>作者：</font>** Benedikt Hilmes, Nick Rossenbach, Ralf Schlüter  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Memristors provide a new chance for resource-efficient computation of neural models for natural language processing by enabling analog execution of vector-matrix-multiplication. Yet, computations on these devices are currently subject to larger distortion, both in weight programming and execution. In this work, we identify large output values of transformed positional encodings to cause major degradation within analog-to-digital conversion (ADC) as part of memristor-based computation. By adjusting the proportion of weight and precision bits of the ADC of specific memristor layers, we reduce the degradation of the execution by ~50% relative, while keeping the estimated energy consumption stable. Additionally, we investigate scenarios where the ADC cannot be modified. In that case the degradation can be reduced by ~30% relative after removing encoding-related linear transformations.

---


### 185. [SmartFont: Dynamic Condition Allocation for Few-Shot Font Generation](https://arxiv.org/abs/2606.13382)

**<font color=#1a73e8>作者：</font>** Zian Yang, Zixin Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot font generation simultaneously requires global structural completeness and fine-grained local style fidelity. Existing methods usually either rely on global content-style modeling, which is robust but imperfectly disentangled, or emphasize component/local modeling, which captures fine details but relies heavily on local priors and reference coverage. We argue that the key challenge is not merely to learn purer conditions, but to organize complementary yet biased global and local conditions through multi-level allocation during generation. To this end, we propose SmartFont, a diffusion-based few-shot font generation framework that combines global content-style generation with weakly supervised local corrective experts. The local branch performs semantic-spatial allocation by learning expert-wise local concepts and semantically meaningful spatial maps under weak component supervision, enabling fine-grained correction without requiring explicit component-conditioned inference. On top of this, a denoising-state condition allocation module adaptively weights global content, global style, and local corrective feature across timesteps and injection blocks. Extensive experiments show that SmartFont achieves better global-local balance, improves glyph quality and local detail fidelity.

---


### 186. [Who Pays the Price? Stakeholder-Centric Prompt Injection Benchmarking for Real-world Web Agents](https://arxiv.org/abs/2606.13385)

**<font color=#1a73e8>作者：</font>** Zihao Wang, Yiming Li, Yutong Wu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Web agents driven by large language models (LLMs) are increasingly deployed in real-world environments, where they operate over untrusted web content and execute actions with direct consequences. This makes them vulnerable to prompt-injection attacks, in which seemingly benign content embeds adversarial instructions that manipulate agent behaviour. Existing security benchmarks adopt an \textit{attack-centric} perspective, focusing on the technical feasibility of injections while overlooking the nuanced distribution of resulting harms. In practice, however, prompt-injection risk is victim-dependent: a single exploit can produce asymmetric consequences for different stakeholders, and the same attack pattern may exhibit substantially different effectiveness depending on whom it targets. To capture these properties, we introduce \textbf{\sysname}, a \textit{stakeholder-centric} benchmark to systematically categorize and attribute harm in real-world web agent systems. It distinguishes between affected entities (e.g., user, seller, platform), decomposes the attacks into concrete objectives, and evaluates each case with complementary outcome- and process-level metrics. Our results reveal substantial and heterogeneous vulnerabilities: not a single attack objective is reliably resisted by current agents, and failures distribute across qualitatively distinct modes ranging from \emph{stealthy parasitism} (attack succeeds without disrupting the user's delegated task) to \emph{misaligned disruption} (task disrupted without attack success) and \emph{compounded failure} (both adversarial objective and task integrity simultaneously violated). These patterns are missed by conventional evaluation, highlighting the need for stakeholder-aware assessment of LLM-based agents in real-world deployments. Benchmark is available at this https URL.

---


### 187. [PolyFlow: Safe and Efficient Polytope-Constrained Flow Matching with Constraint Embedding and Projection-free Update](https://arxiv.org/abs/2606.13400)

**<font color=#1a73e8>作者：</font>** Jianming Ma, Qiyue Yang, Yang Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While flow-based generative models have demonstrated strong performance across a wide range of domains, deploying them in safety-critical physical systems remains challenging due to strict constraint requirements. Existing approaches typically enforce safety through post-hoc corrections, which incur substantial computational overhead and may distort the learned distribution. We propose PolyFlow, a polytope-constrained flow matching framework that embeds constraints directly into the model and flow dynamics. PolyFlow introduces a discrete-time flow formulation and a projection-free architecture, which eliminate the discretization error and guarantee strict satisfaction of arbitrary polyhedral constraints, without the need for expensive iterative solvers. Experimental results show that PolyFlow achieves zero constraint violation while maintaining high distributional fidelity across a range of planning and control tasks. Compared to state-of-the-art constrained generation baselines, PolyFlow significantly reduces inference latency and demonstrates a favorable trade-off between safety, efficiency, and generative quality. Code is available on this https URL.

---


### 188. [Neuro-Symbolic Agents for Regulated Process Automation: Challenges and Research Agenda](https://arxiv.org/abs/2606.13405)

**<font color=#1a73e8>作者：</font>** Alexander Rombach, Chantale Lauer, Nijat Mehdiyev  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agents are entering regulated industries where they automate judgment intensive quality management processes. We argue that symbolic structures already embedded in these domains, including regulations, typed process models, and compliance constraints, should be treated not merely as external monitoring mechanisms but as core architectural components that shape the agent's decision-making and behavior. We propose compliance-by-construction as a complementary paradigm to guardrail-based monitoring: a structural foundation that prevents control-flow violations, while guardrails remain essential for catching semantic errors. We identify a structured set of neuro-symbolic research challenges on foundational and capability level and show that addressing them jointly enables compliance-by-construction. We call on the neuro-symbolic community to engage with regulated process automation as a high impact research domain.

---


### 189. [Optimizing Appliance Scheduling for Solar Energy Management Using Metaheuristic Algorithms](https://arxiv.org/abs/2606.13407)

**<font color=#1a73e8>作者：</font>** Hiba Ahmed, Alexander E.I. Brownlee, Jason Adair 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Renewable energy is essential for meeting future energy demands; however, solar energy generation, which occurs only during daylight hours often does not align with household consumption patterns. Appliances such as cookers, washing machines, and dryers are typically operated according to user preferred schedules rather than solar energy availability, creating a scheduling optimization problem. The objective is to determine optimal appliance start times to maximize renewable energy utilization while minimizing user inconvenience and adhering to system constraints. This paper presents a metaheuristic approach using Iterated Local Search (ILS) and Simulated Annealing (SA) to optimize appliance start times, while considering appliance operating durations, power consumption, inverter limit, battery state of charge constraints, and solar generation forecasts. Unlike most existing work, the scheduling is extended beyond a single day to accommodate unfinished tasks from previous days (spillover), ensuring operational continuity and enabling sequential operation across multiple days. Experimental results show that the sequential multi-day scheduling framework effectively manages system constraints while ensuring user convenience under exclusive solar generation. These findings also open opportunities for future research on multi-objective trade-offs between investment in equipment of various sizes, return on that investment, and user satisfaction.

---


### 190. [Person Identification from Contextual Motion](https://arxiv.org/abs/2606.13410)

**<font color=#1a73e8>作者：</font>** Igor Kviatkovsky, Ehud Rivlin, Ilan Shimshoni  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We consider the problem of identifying people based on their motion styles. We present a generative model describing the action instance creation process and derive a probabilistic identity inference scheme for two common person identification scenarios motivated by the surveillance and authentication applications. We introduce a novel, \emph{interactive}, scenario for person identification from motion patterns. To this end, we formalize the identification process in the context of a sequential message exchange session between the subject and the system. The subject's behavior is modeled using a probabilistic generative model inspired by the Human Information Processing (HIP) paradigm. At each stage, the system presents a visual stimulus (a cue) to the subject and records their motion response. The cue is selected so as to maximize the mutual information of the expected response and the subject's identity. Once recorded, the response is used to update the a posteriori probability over possible subjects' identities. The process terminates once a sufficient classification confidence level is reached. To the best of our knowledge, this is the first time person identification is addressed in such interactive setting. We report high recognition rates on five publicly available datasets and our own novel dataset consisting of 4,476 recordings of 22 test subjects responding to 15 cues.

---


### 191. [An End-to-End Hybrid Framework for Rumour Detection in Low-Resources Algerian Dialect](https://arxiv.org/abs/2606.13411)

**<font color=#1a73e8>作者：</font>** Dihia Lanasri, Fatima Benbarek  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid growth of social media has intensified the spread of rumours. This issue is more challenging in the Algerian context due to the informal and code-switched nature of dialectal content, the scarcity of annotated resources, and the limited effectiveness of standard Arabic NLP tools on dialect text.
This paper presents an end-to-end rumour detection hybrid framework for Algerian dialect social media content. We build a domain-specific annotated dataset by combining real social media posts, synthetic data, and the FASSILA corpus, with automatic labeling based on a similarity-based annotation process. A transliteration pipeline is also introduced to generate parallel datasets in Arabic script and Arabizi.
We evaluate multiple approaches, including classical machine learning, deep learning, transformers, and hybrid models. Experimental results show that a hybrid approach combining transformer embeddings with a classical classifier achieves the best performance, reaching an F1-score of 0.84. We also find that domain-specific pre-training is more important than model size, with social media-trained models outperforming larger models trained on formal Arabic corpora.
These results demonstrate the feasibility of rumour detection in low-resource Algerian dialect settings.

---


### 192. [An Assessment Framework for Application-Level Cryptographic Agility](https://arxiv.org/abs/2606.13425)

**<font color=#1a73e8>作者：</font>** Navaneeth Rameshan, Gregoire Messmer  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The impending post-quantum transition to new cryptography will require complete replacement of algorithms within all software. The cryptographic APIs used today make this transition challenging because they were not designed with agility as a concern. There is no method for systematically assessing cryptographic agility as an overall ability. In addition to this, the term itself refers to multiple independent capabilities. Specifically, it includes replacing algorithms, selecting by policy, and substituting implementations. This lack of structured decomposition limits both the evaluation of systems and the development of cryptographically agile APIs.
We introduce a component-based assessment framework that characterizes application-level cryptographic agility along seven orthogonal dimensions: three coupling dimensions that measure what the application code knows about algorithms and providers, a cross-cutting decoupling mechanism, a governance authority dimension, and two agility enablers that measure actual migration capability. The framework is non-linear and captures non-hierarchical profiles: a system may achieve high operation decoupling yet low creation decoupling, or strong versioning without externalized configuration.
We evaluate six representative APIs (PKCS#11, OpenSSL~3.0, JCA, Google Tink, AWS KMS, and HashiCorp Vault Transit) against the framework, revealing three pervasive and independent gaps: no system supports intent-based key creation, none provides policy-driven algorithm selection (as distinct from access control), and none offers dedicated/first-class operations for algorithm transformation of existing keys. These gaps are individually sufficient to prevent agile migration, explaining why the post-quantum transition remains a software engineering problem despite decades of API progress.

---


### 193. [Accelerating Speculative Diffusions via Block Verification](https://arxiv.org/abs/2606.13426)

**<font color=#1a73e8>作者：</font>** Alexander Soen, Hisham Husain, Valentin De Bortoli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding speeds up LLM inference by using a draft model to generate tokens, with an acceptance-rejection scheme that ensures that the output matches the target distribution. Adapting this to continuous diffusions is difficult because speculative sampling requires drawing from a residual distribution. While straightforward in discrete spaces, efficiently sampling this residual in continuous space is non-trivial. Consequently, existing diffusion adaptations either use computationally inefficient sampling techniques or rely on an alternative scheme. In this work, we introduce a novel scheme that efficiently implements the original speculative sampling mechanism for diffusion models. Our approach offers a critical advantage over current methods: it enables us to adapt block verification from LLMs to diffusions -- which provably improves the acceptance rate of drafts. Furthermore, we formalize and analyze the Free Drafter, a heuristic self-speculative drafter for diffusions that requires no training. By enabling block verification, our Free Drafter yields up to a 6.3% speedup over existing speculative methods with no additional training and negligible overhead beyond the existing parallel verification pass.

---


### 194. [VietFashion: Benchmarking Sketch-Text Composed Image Retrieval for Cultural Outfits](https://arxiv.org/abs/2606.13427)

**<font color=#1a73e8>作者：</font>** Hoang-Nguyen Cao, Le-Hoang Bui, Dinh-Khoi Vo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cultural garments pose a unique challenge for visual retrieval systems, as their identity often depends on subtle structural and symbolic details that are poorly captured by standard AI models. We introduce VietFashion, a new benchmark for sketch-text composed image retrieval centered on the Ao Dai, a traditional Vietnamese garment. VietFashion enables designers and researchers to retrieve culturally meaningful outfits using a combination of hand-drawn sketches, which convey garment structure, and textual descriptions, which encode cultural semantics. The dataset is initialized with 650 sketches and expanded using generative models to produce over 21,000 photorealistic images with aligned captions. Textual prompts that describe detailed outfit attributes, which are extracted from fashion magazines to ensure authenticity and diversity. To better reflect the inherent ambiguity of design intent, VietFashion adopts a multi-target retrieval setting, where a single query may correspond to multiple valid results. We establish standardized evaluation protocols and benchmark state-of-the-art composed image retrieval methods. Experimental results reveal significant performance gaps in modeling fine-grained cultural semantics and multi-modal composition, positioning VietFashion as a challenging benchmark for fine-grained fashion retrieval. The dataset is publicly available at: this https URL.

---


### 195. [OmniDirector: General Multi-Shot Camera Cloning without Cross-Paired Data](https://arxiv.org/abs/2606.13432)

**<font color=#1a73e8>作者：</font>** Jiwen Liu, Shujuan Li, Zhixue Fang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cloning camera motion from reference videos is an important task in video generation, as videos provide intuitive and precise control. Existing methods either directly use parametric representations that fail to handle multi-shot generation or synthesize cross-paired data, which suffer from data scarcity, resulting in poor performance in complicated camera motion cloning. To address these issues, we introduce a general camera motion representation that encodes cameras as grid motion videos. This camera grid represents the camera parameters visually and supports the integration of diverse trajectories for multi-shot video generation. Building upon this, we propose OmniDirector, a unified framework trained on a million-scale camera grid-video pairs that coordinates characters, actions, and cameras to provide director-level control for multimodal diffusion transformers. Furthermore, we design a novel hierarchical prompt expansion agent that harmoniously integrates different control signals by systematically describing camera motion and visual content through understanding signal relationships. Extensive experiments demonstrate the superior performance and outstanding controllability of our framework. Project page: this https URL

---


### 196. [Evaluation Sovereignty in Metadata-Driven Classification: A Multi-Track Framework for Weakly Supervised Information Systems](https://arxiv.org/abs/2606.13436)

**<font color=#1a73e8>作者：</font>** Raymond Vasquez  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluation in machine learning is typically treated as a neutral measurement process. However, in operational information systems, evaluation outcomes are often conditioned by the processes used to generate labels. This paper does not seek to improve classification performance. Instead, it examines the validity of performance measurement under differing label-authority regimes. This issue is particularly relevant in large-scale metadata-driven systems, where labels are often incomplete, inconsistent, or weakly supervised.
We introduce evaluation sovereignty, defined as the degree to which performance metrics are independent of label authority and supervision regime, and propose a multi-track evaluation framework that systematically varies training and evaluation label sources. Using hierarchical multi-label classification on large-scale scientific metadata, we demonstrate that models exhibiting strong performance under operational ("silver") evaluation degrade substantially under independent ("gold") evaluation, particularly for fine-grained classification. For example, Micro-F1 decreases from approximately 0.54 to 0.03. Notably, ranking-based metrics remain above baseline, revealing a divergence between latent model signal and classification validity.
These findings suggest that commonly reported performance metrics may reflect alignment with labeling processes rather than true predictive capability. We therefore reconceptualize evaluation validity as a system-level property shaped by label governance and provide a practical methodology for auditing intelligent systems operating under weak supervision.

---


### 197. [S-GBT: Smooth Growth Bound Tensor for Certified Robustness Against Word Substitution Attacks in NLP](https://arxiv.org/abs/2606.13439)

**<font color=#1a73e8>作者：</font>** Mohammed Bouri, Mohammed Erradi, Adnane Saoud  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite recent progress in Natural Language Processing (NLP), models remain vulnerable to word substitution attacks. Most existing defenses focus on first order sensitivity and measure how much the output changes when the input is slightly perturbed. However, they ignore how this sensitivity evolves, which is described by curvature. When gradients vary sharply, models can still fail. This paper introduces the Smooth Growth Bound Tensor (S-GBT), a second order method that bounds the Hessian element-wise, for which we provide formal theoretical proofs on the resulting robustness bounds. A regularization term is added during training to minimize these bounds. This yields tighter certified robustness against word substitution attacks. The change in the output under word substitution is bounded by both a linear term and a quadratic term. S-GBT is derived for two architectures: Long Short-Term Memory (LSTM) and Convolutional Neural Networks (CNN). The method is integrated directly into the training objective. Its effectiveness is evaluated on multiple benchmark datasets. The results show that combining first and second order regularization improves certified robust accuracy by up to 23.4% compared to prior methods, while clean accuracy remains competitive. These findings indicate that controlling both the gradient and its variation is a promising direction for building more robust models.

---


### 198. [How Much Memory Do We Need? Adaptive Memory Gate for Neural Operators](https://arxiv.org/abs/2606.13443)

**<font color=#1a73e8>作者：</font>** Jihyeon Hur, Yongseok Kwon, Min-Gi Jo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators have emerged as a powerful data-driven approach for solving time-dependent PDEs. Among recent advances, memory-augmented neural operators explicitly incorporate past states and have achieved remarkable performance under low-resolution observation settings. However, existing approaches apply a fixed memory weight regardless of observation conditions, such as resolution or physical parameters, limiting their adaptability. Our preliminary experiments reveal that optimal memory weight varies with resolution and viscosity, implying that a fixed memory weight cannot simultaneously optimize performance across diverse settings. We propose AMGFNO, which dynamically modulates memory weight through a learnable gate. On the Kuramoto-Sivashinsky and Burgers' equations, AMGFNO achieves 55-79% nRMSE reduction over at low resolution, with the learned gate value automatically decreasing from $\bar{g} \approx 0.7$ to near-zero as resolution increases.

---


### 199. [Clustering Node Attributed Networks with Graph Neural Networks and Self Learning](https://arxiv.org/abs/2606.13444)

**<font color=#1a73e8>作者：</font>** Rodrigo de Sapienza Luna, Daniel Ratton Figueiredo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph clustering - partitioning the node set of a graph into disjoint subsets that reflect some latent information - is a fundamental problem as it finds applications in a myriad of different scenarios. While this classic problem has been tackled for decades by different communities, a recent variation of the problem driven by real data considers the scenario where nodes have attributes that are also informative. This has triggered novel methods that simultaneously leverage network information (edges) and node information (attributed) in the design of novel clustering algorithms. This work proposes a novel framework that builds on prior works that have applied graph neural networks (GNN) to graph clustering. The proposed framework operates in rounds of self learning in a fully unsupervised setting. In each round, a GNN generates representations for nodes that are used to cluster the nodes. This clustering influences the graph used to generate the node representation in the next round. Moreover, a context graph built in each round using the original graph is used to generate the node representations. Empirical results show that the proposed methodology extracts information from both network edges and node attributes in synthetic data, outperforming algorithms focused solely on the network or attributes when neither are very informative. Multiple rounds of learning also improve the performance and always outperforms a long single round of training (i.e., classic GNN graph clustering). When considering real datasets, empirical results indicate that the proposed methodology is competitive to state-of-the-art methods when cluster sizes are balanced.

---


### 200. [Intent-Based Cryptographic API Design for Cryptographic Agility](https://arxiv.org/abs/2606.13445)

**<font color=#1a73e8>作者：</font>** Navaneeth Rameshan, Gregoire Messmer  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As organizations move toward post-quantum cryptography, they face the major challenge of updating cryptographic algorithms across large, complex software portfolios. However, most cryptographic APIs in use today were designed around specific algorithms. These APIs expect explicit use of specific algorithms, provide little or no support for policy-based algorithm selection, and offer no straightforward way to migrate existing keys to newer algorithms. This makes the transition to post-quantum cryptography challenging. The companion assessment framework identifies the barriers to cryptographic agility and explains why algorithm transition is largely a software engineering problem.
To address the limitations of current cryptographic APIs, we identify the principles necessary to design a cryptographically agile API. The design principles are derived from five fundamental architectural characteristics (Abstraction, Stability, Temporal Flexibility, Separation, and Extensibility). We also show how the design principles can be implemented using several examples of Protocol Buffers API design patterns. In particular, we present an intent vocabulary that is based on scopes which allows for decoupling key creation from algorithm identities. It also supports transparent substitutions of algorithms in the applicable scope. Cryptographic governance is enabled by an abstract policy API that does not prescribe the policy format. Keys are represented by stable identifiers and support key evolution operations (rotation, transformation, migration), facilitating migration between algorithms and providers while tracking both the original key identity and its evolution history. With this approach, updating cryptography becomes an operational process without the need to rewrite application code.

---


> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-251](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
