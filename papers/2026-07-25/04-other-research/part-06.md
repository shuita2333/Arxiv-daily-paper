# 📦 其他研究 | 2026年07月25日

> 本类共 **271** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-271**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-271**

---

### 251. [Windowed-MTP: Removing the Full-Context Draft-KV Tax at Million-Token Context](https://arxiv.org/abs/2607.21535)

**<font color=#1a73e8>作者：</font>** Alagappan Valliappan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates autoregressive generation by having a cheap draft propose tokens that a target verifies in parallel. Frontier models increasingly ship a built-in Multi-Token-Prediction (MTP/NEXTN) draft head under the assumption that the draft is negligibly cheap. At million-token context this breaks: an MTP draft head typically runs full attention over the entire KV cache at every draft step, so its read grows linearly with context and comes to dominate the draft cost -- precisely where speculation is most valuable. The effect compounds with draft length (a deep native draft can turn net-negative, slower than no speculation) and sharpens under hybrid/linear-attention targets, where cheaper verification leaves the draft's full-attention read exposed. We apply a StreamingLLM-style sliding window plus attention sink to the draft's attention only (Windowed-MTP), leaving full-attention verification intact. It is training-free, drop-in, and lossless by construction: the full-attention target still decides every accepted token, so windowing changes only which tokens are proposed, never which are accepted. It bounds the draft's KV working set to a constant, dropping ~99% of KV entries at 1M. Across three architecture families (Qwen GDN-MoE 35B/122B and a Mamba2-hybrid NoPE 120B) at 1M context on a single GPU in SGLang, windowing cuts the per-decode-step cost over the shipping native MTP draft by +28% to +44%, an input-invariant margin that widens with context. Since per-token latency is this cost divided by acceptance length, at matched acceptance end-to-end decode latency improves by the same amount, and more where windowing also lifts acceptance, while preserving the target's verified output distribution. Finally, the unread draft KV -- 7.7-11% of total KV at 1M -- is reclaimed via a compact ring buffer at no acceptance or quality cost.

---


### 252. [DONDO: Open w2v-BERT Speech-Recognition Base Models for African Languages](https://arxiv.org/abs/2607.21540)

**<font color=#1a73e8>作者：</font>** Paul Azunre  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present DONDO, a family of open, permissively licensed automatic speech recognition (ASR) base models for African languages, built on the w2v-BERT 2.0 self-supervised speech encoder. DONDO comprises twenty-one monolingual models and five multilingual models spanning twenty-seven language varieties across Ghana, Sierra Leone, Nigeria, Senegal, Kenya and Zimbabwe. Models are fine-tuned primarily on read speech drawn from religious texts, which offer broad, license-clear and orthographically consistent coverage for languages that otherwise lack transcribed audio. We describe a two-step (and, for one family, three-step) learning-rate-annealed fine-tuning procedure that first adapts a shared multilingual model at a high learning rate and then anneals it to recover, and in several cases surpass, strong monolingual baselines. We further describe a lightweight language-conditioning mechanism that injects a one-hot language identity as a sequence of prefix frames prepended to the acoustic features, allowing a single multilingual checkpoint to be steered to a target language at inference. Across the five multilingual families the annealed models reach average word error rates (WER) of 10-13%, closing most of the gap to monolingual models while covering many languages in a single checkpoint. All models are released on the Hugging Face KhayaAI organisation under the Apache-2.0 license (attribution only) so that others may fine-tune them freely, including for commercial use. We provide a conservative estimate that the languages covered are spoken by on the order of one hundred million first-language speakers, and by substantially more when second-language use is included.

---


### 253. [Zero-Flow Two-Sample Tests](https://arxiv.org/abs/2607.21542)

**<font color=#1a73e8>作者：</font>** Yakun Wang, Leyang Wang, Song Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a new approach to two-sample testing for deciding whether two sets of samples are drawn from the same distribution. The test is built on a statistical discrepancy based on the zero-flow criterion, termed zero-flow discrepancy (ZFD). We prove the validity of ZFD and propose a practical testing procedure, termed the zero-flow two-sample test (ZF2ST). The key idea is to learn how samples from the two distributions are locally misaligned and use the resulting directional pattern as evidence of distributional difference. By separating witness learning from hypothesis evaluation, ZF2ST can use flexible neural networks while maintaining valid statistical calibration. We develop both regression-based and power-maximized approaches for learning the witness. Experiments on synthetic and image datasets demonstrate that ZF2ST can achieve strong testing power for structured distributional changes while maintaining well-calibrated type-I error.

---


### 254. [Towards Robust Iris Recognition Through Occlusion Identification and Conditional Diffusion-Based Reconstruction](https://arxiv.org/abs/2607.21545)

**<font color=#1a73e8>作者：</font>** Kamrul Hasan, Mylene C.Q. Farias, Oleg V. Komogortsev  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Iris recognition is a reliable biometric approach that identifies individuals using the distinctive and stable texture of the iris. However, recognition performance can degrade when discriminative iris texture is partially occluded by eyelids, eyelashes, specular reflections, or other acquisition artifacts. Existing approaches often perform recognition directly on degraded samples or rely only on the remaining visible iris region, which may be inadequate when substantial texture is corrupted. To address this limitation, we propose an occlusion-aware iris recognition framework with three sequential modules: occlusion-type identification, diffusion-based reconstruction, and deep-learning-based recognition. First, a residual 2D CNN-based network determines whether an iris image is non-occluded or belongs to one of the controlled occlusion categories. Second, the occluded image, binary mask, and predicted occlusion type condition a denoising diffusion probabilistic model to reconstruct the corrupted region. Finally, VGG19-HPMNet, a modified VGG19 model with horizontal pyramid mapping, extracts discriminative global and part-wise local iris features for recognition. Experiments on the CASIA-Iris-Thousand dataset under a controlled synthetic-occlusion protocol show that the proposed framework improves iris recognition performance by identifying the occlusion type, reconstructing masked regions, and re-evaluating the restored iris samples.

---


### 255. [The Boundaries of Automation: A Theory of Persistent Human Participation](https://arxiv.org/abs/2607.21547)

**<font color=#1a73e8>作者：</font>** Fares Fourati, Hinrich Schütze, Eyke Hüllermeier 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid progress of AI has intensified the long-standing pursuit of automation: replacing human participation with algorithms wherever possible. Implicit in this pursuit is the assumption that humans remain in the loop only because current AI systems are not yet sufficiently capable. This paper challenges that assumption. Rather than asking how far automation can extend, we ask where its conceptual limits lie and argue that human participation may persist even with highly capable AI systems for three distinct reasons. Technical or complementarity grounds arise when humans contribute capabilities or perspectives unavailable to AI. Normative or developmental grounds arise when participation itself is valuable for human agency or learning. Most importantly, emergence grounds arise from target emergence: in some activities, the target is not fully specified in advance but instead emerges through the interaction itself. In these cases, human participation is not merely a means of improving execution but is constitutive of the target being produced. Human--AI co-construction, understood as the joint production of outcomes by humans and AI systems, is therefore not simply a temporary response to imperfect AI, but a persistent feature of activities whose objectives emerge through participation. This perspective has important implications for the limits of automation and for the design, evaluation, and ethics of future AI systems.

---


### 256. [SANA-Video 2.0: Hybrid Linear Attention with Attention Residuals for Efficient Video Generation](https://arxiv.org/abs/2607.21553)

**<font color=#1a73e8>作者：</font>** Junsong Chen, Jincheng Yu, Yitong Li 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce SANA-Video 2.0, a hybrid video diffusion transformer instantiated at 5B and 14B scales under a unified architecture. Designed to generate high-quality video up to 720p on a single GPU, SANA-Video 2.0 matches full-softmax video DiTs in quality while retaining the favorable long-sequence scaling of linear attention. To avoid quadratic attention throughout, Hybrid Linear-Softmax Attention combines gated linear attention for O(N)-dominated mixing with periodic gated-softmax anchors at a 3:1 ratio, restoring the full-rank token interactions that pure linear attention lacks. To propagate these refreshed representations across depth, Block Attention Residuals (AttnRes) route completed block summaries into later linear layers, enabling anchor-feature reuse and boosting deep-layer effective rank by ~12%. Through from-scratch training, SANA-Video 2.0 learns the complete hybrid directly rather than linearizing pretrained models, with reduced-resolution proxy studies establishing 25% softmax as the optimal quality-efficiency trade-off. With 40-step sampling, SANA-Video 2.0 achieves a VBench score of 84.30 in 13.2s at 480p on a single H100, remaining competitive with far larger softmax video DiTs at a fraction of the latency. Its compiled DiT forward pass is 3.2x faster than a matched full-softmax baseline at 720p/60s, a gap that expands with video duration. Furthermore, full-stack Sol-Engine optimization (kernel fusion, caching, and sparse attention) accelerates this hardware-friendly backbone by a further 3.58x, bringing the 5B pipeline to 13.06s at 720p/5s and making it 120x faster than Wan 2.2-A14B on one H100. Overall, our hybrid design recovers softmax-level expressiveness at substantially reduced cost, unlocking scalable long, high resolution video generation.

---


### 257. [Visual Contrastive Self-Distillation](https://arxiv.org/abs/2607.21556)

**<font color=#1a73e8>作者：</font>** Yijun Liang, Yunjie Tian, Yijiang Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) is promising as it removes the external teacher required by on-policy distillation (OPD), yet it still needs asymmetric information between teacher and student to ensure that the self-teacher provides a stronger learning signal than the student. Existing methods create this asymmetry either through privileged answers or visual evidence. We ask whether both can be removed, yielding a simpler form of OPSD driven purely by input conditioning. For this purpose, we propose Visual Contrastive Self-Distillation, namely VCSD, which converts image-content removal into an on-policy self-distillation signal. At each student-generated response prefix, the EMA teacher produces two next-token distributions under the same prompt and prefix -- one conditioned on the original image and the other on a content-erased control. Their token-wise log-probability difference highlights candidates whose likelihood is specifically increased by the instance-level visual content. We use this contrast to sharpen the teacher's original-image distribution within its plausible support, and distill the resulting full-distribution target into the student. Using ViRL39K dataset, VCSD consistently outperforms matched OPSD across Qwen3-VL and Qwen3.5 models. For example, on Qwen3-VL, it improves the seven-benchmark aggregate from $62.27\% \rightarrow 67.04\%$ at 2B, $71.30\% \rightarrow 73.16\%$ at 4B, and $72.51\% \rightarrow 76.26\%$ at 8B. Furthermore, VCSD requires no external teacher, privileged answers, visual evidence signals, reasoning traces, or additional inference-time cost.

---


### 258. [Unsupervised Consensus-Based Anomaly Detection for Spatiotemporal Malaria Incidence in Ghana](https://arxiv.org/abs/2607.21559)

**<font color=#1a73e8>作者：</font>** T. Ansah-Narh, Y. Asare Afrane  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A consensus anomaly detection framework was applied to monthly malaria surveillance data from Ghana (2014-2023) to identify atypical transmission patterns. Anomalies were highly structured in space and time. Ashanti and Northern Regions accounted for most recurrent anomalies, with persistent hotspots at Tamale, Kumasi, and Accra. A key finding was the spatial distinction between anomaly burden (cumulative cases during anomalous periods) and anomaly frequency (persistence of unusual behaviour). Tamale had the highest burden during anomalies, whereas the highest anomaly rates clustered in Ashanti districts, showing that high-burden areas are not necessarily those with the most frequent anomalous transmission. Anomalous months formed a statistically distinct group, with much higher case counts (Cohen's $d = 3.252$) and large seasonal deviations ($d > 1.2$) compared with normal months. Malaria burden alone provides an incomplete picture of transmission dynamics. By distinguishing where malaria is most prevalent from where transmission behaves most unusually, this framework can strengthen surveillance, prioritise investigations, and support targeted control strategies.

---


### 259. [Graph Learning on Ensembles of Cyclic Peptides: An Investigation of Molecular Ensemble Modeling](https://arxiv.org/abs/2607.21561)

**<font color=#1a73e8>作者：</font>** Aaron Feller, Kris Deibler, Maxim Secor  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular property prediction from structure often uses a single representative conformation, even though many molecules exist as conformational ensembles in solution. We introduce EnsembleEGNN, a molecular ensemble foundation model that encodes an ensemble by first encoding each conformer with shared Equivariant Graph Neural Network (EGNN) layers, then pooling the resulting conformer representations with a Set Attention Block. We pretrain the model on CREMP, a cyclic peptide ensemble dataset, using a multi-task self-supervised objective combining masked token recovery, noisy-coordinate reconstruction, and pairwise distance reconstruction. On the CREMP-CycPeptMPDB dataset, training EnsembleEGNN from scratch fails entirely ($R^2=0.005$). However, the pretrained model reaches $R^2=0.477$ and Pearson $r=0.699$, outperforming the sequence-only BERT baseline ($R^2=0.439$, Pearson $r=0.667$). When EnsembleEGNN is co-trained end-to-end with the BERT sequence encoder, the hybrid model improves further to $R^2=0.538$ and Pearson $r=0.737$. These results demonstrate that encoding conformational ensembles into a single thermodynamically informed embedding improves cyclic-peptide property prediction.

---


### 260. [Scene Parameter Saliency via Differentiable Light Transport](https://arxiv.org/abs/2607.21562)

**<font color=#1a73e8>作者：</font>** Linas Beresna, Eugene Fiume  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gradient-based saliency methods reveal which input features most influence a neural network's output, and are a standard tool for model interpretability. We observe that differentiable renderers, which are conventionally used for parameter optimisation, produce an analogous form of saliency: given any scalar metric evaluated on a rendered image, a single reverse-mode differentiation pass yields per-parameter gradients that identify which scene elements most influence the metric. We call these gradient fields metric saliency maps. Unlike neural saliency, which propagates attribution through learned weights, metric saliency propagates through the image formation process itself, including multi-bounce light transport, capturing parameter dependencies that are semi-opaque to manual inspection. We compute metric saliency maps for qualitatively different objectives: psychovisual glare indices, mean scene luminance, and neural perceptual scores. The saliency rankings differ substantially across metrics for the same scene, with parameters that dominate one objective being negligible for another. The saliency map is specific to the metric, not an intrinsic property of the scene. Our results suggest that differentiable renderers produce derivative images that are as informative for scene understanding as the primal images they were designed to generate.

---


### 261. [Where You Tap Matters: A Probe-and-Model Benchmark for Open-Set RF Fingerprinting](https://arxiv.org/abs/2607.21564)

**<font color=#1a73e8>作者：</font>** Gabriele Oligeri, Savio Sciancalepore, Ingrid Huso 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Radio Frequency Fingerprint Identification (RFFI) enables transmitter identification at the physical layer by learning device-specific impairments from received signals, yet the literature is inconsistent about where in the receiver chain those samples should be collected. Since distinct transformations are applied to the signal by the different receiver operations, i.e., carrier recovery, gain normalization, pulse shaping, and timing recovery, they can either tighten within-transmitter variability or suppress the features RFFI requires for classification. We present a systematic real-world evaluation of open-set, reconstruction-error RFFI using data collected at five probe points along a standard BPSK receiver chain. Our results show that RFFI is strongly probe-dependent: timing recovery and, to a lesser extent, carrier recovery enable low false-acceptance operation with limited in-distribution-out-of-distribution overlap, whereas other stages often require a false-acceptance ratio above 0.1 to achieve a true-acceptance ratio of 0.9. To test the validity of our findings across model selection, we benchmark several LLM-designed autoencoders using a controlled pipeline that holds preprocessing and MSE scoring fixed. These architectures confirm that RFFI is probe-dependent. Moreover, they do not outperform the baseline at the chosen operating point and typically increase training time. Overall, probe selection dominates reconstruction-based open-set RFFI performance, more than the autoencoder complexity.

---


### 262. [Beyond Sufficiency: Time Series Explanation with Counterfactual Necessity](https://arxiv.org/abs/2607.21573)

**<font color=#1a73e8>作者：</font>** Hongnan Ma, Yiwei Shi, Mengyue Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Faithful explanations of time-series classifiers should identify subsequences that are not only sufficient to preserve a black-box model's prediction, but also necessary for maintaining it. However, existing sufficiency-oriented methods can assign high importance to spurious subsequences that support the prediction without being essential to the model's decision. We introduce \textbf{TimePNS}, a necessity-aware framework for time-series explanation. Inspired by Pearl's counterfactual notion of necessity, TimePNS assesses whether a temporal factor is necessary by intervening on it and measuring whether the original prediction is disrupted. The framework adopts a two-stage design. Stage I learns an identifiable causal generative process together with a sufficiency-oriented explanation mask. Stage II performs counterfactual interventions on temporal factors to derive necessity signals, which supervise a temporal gate that refines the initial explanation by suppressing non-essential components and emphasizing counterfactually necessary ones. Experiments on synthetic and real-world time-series benchmarks show that TimePNS more accurately identifies decision-critical subsequences and consistently improves sufficiency-necessity trade-offs over strong baselines.

---


### 263. [Surprisal Theory is Tautological (without Rational Grounding)](https://arxiv.org/abs/2607.21574)

**<font color=#1a73e8>作者：</font>** Ryan Cotterell  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Surprisal theory holds that the human processing difficulty of a linguistic unit in context is an affine function of its surprisal under some language model. I argue this claim is a tautology without further constraint: for any non-negative difficulty measure over units in context, there exists a language model whose surprisal is an affine function of it under mild technical conditions. Therefore, because any pattern of difficulty is consistent with some language model, without an additional constraint on the language model, surprisal theory makes no falsifiable predictions. The tautology was long obscured by an assumption implicit in two decades of psycholinguistic work---that the relevant language model is the distribution that generated the training corpus, so that improving corpus fit improves predictions of human behavior. Recent empirical work has undermined this assumption, demonstrating that better corpus models can be worse predictors of processing difficulty. I conclude that breaking the tautology requires a rationalist intervention, i.e., the relevant language model must be derived from a non-empirically motivated model of the comprehender, which could be based on, for instance, memory constraints or processing goals, and that, thus, does not depend on the behavioral data surprisal theory is meant to explain.

---


### 264. [Self-Supervised Learning of Structured Dynamics from Videos](https://arxiv.org/abs/2607.21576)

**<font color=#1a73e8>作者：</font>** Lukas Knobel, Andrew Zisserman, Yuki M. Asano  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding motion in video is a fundamental challenge for visual learning, as frame-to-frame change entangles two sources of dynamics: camera motion and object motion. This decomposition has remained underexplored in representation learning, partly because these factors are tightly coupled in natural videos and difficult to supervise separately. Yet recovering it is important for learning robust motion representations that separate meaningful object dynamics from camera-induced variation. We study whether such structured motion representations can be recovered from frozen features of a pretrained image vision transformer. We propose the Structured Dynamics Model (SDM), which explicitly separates the dominant source of temporal change from residual dynamics through future-feature prediction, rather than representing video change with a single entangled latent or with unstructured, spatially dense transition tokens. Training combines self-supervised learning on real video with weak supervision of scene dynamics on synthetic Kubric data. We evaluate SDM on ProbeMotion, a new evaluation suite spanning synthetic and real videos with camera motion, object motion, and combined dynamics. SDM outperforms backbone baselines using global CLS or average-pooled features, and compares favorably to strongly supervised representations such as VGGT on several probes, despite using substantially weaker supervision. These results suggest that pretrained image models can be readily repurposed into structured video-dynamics representations, providing a useful inductive bias for learning and analyzing latent video dynamics.

---


### 265. [Synthetic data generation framework for quality control automation in gravure printing](https://arxiv.org/abs/2607.21577)

**<font color=#1a73e8>作者：</font>** Korota Arsène Coulibaly, Mohamed Hamlich, Khalid Hmali 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Quality control in printing, particularly in rotogravure printing, still depends on slow, costly, and subjective manual inspection. Automated surface defect detection is critical for maintaining high-quality standards in rotogravure printing. Deep learning models give prospects for automation. However, training robust deep learning models, such as YOLO or Vision Transformers, is heavily hindered by the extreme scarcity of real-world industrial defects images. To overcome this limitation, this paper introduces a novel synthetic data generation framework tailored for rotogravure printing quality control. The proposed pipeline automatically generates high-fidelity images of specific printing defects (creases, streaks, misregistration, etc.) and outputs corresponding bounding boxes and annotations. To validate the framework, a synthetic dataset of 7533 images was generated and used to train the state-of-the-art object-detection model RFDETR. Experimental results demonstrate that the model trained on our synthetic data achieves a Mean Average Precision (mAP) of 80.9\% on real industrial testing samples. This framework provides a zero-cost, rapid-deployment solution for automating defect inspection in printing lines without requiring massive manual data collection.

---


### 266. [GraphVid: Interactive Graph-Controllable Video Generation](https://arxiv.org/abs/2607.21580)

**<font color=#1a73e8>作者：</font>** Vedant Shah, Onkar Susladkar, Tushar Prakash 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Controllable video generation remains challenging due to the difficulty of specifying precise multi-object interactions using text prompts or motion-control inputs that primarily constrain pixel movement. In practice, trajectory-based control often requires users to draw accurate tracks for multiple objects, which scales poorly with scene complexity and becomes ambiguous under occlusion or overlap. To enable flexible yet precise multi-subject control, we introduce $\textbf{GraphVid}$, a graph-conditioned image-to-video generation model that enables interactive control through structured interaction graphs. We further curate $\textbf{GraphVid-Bench}$, a large-scale interaction-centric video dataset with structured relational annotations to enable training of interaction-aware video generation models. Despite using substantially less training data and fewer trainable parameters than prior motion-control methods, GraphVid delivers strong controllability and video quality. Compared with Motion-I2V, GraphVid reduces FID by up to 39.9% and FVD by 37.6%, while improving PSNR (9.87=>15.98) and SSIM (0.38=>0.61). Our results highlight the potential of structured semantic interfaces as a powerful paradigm for controllable video generation.

---


### 267. [Expanding Flow Maps](https://arxiv.org/abs/2607.21585)

**<font color=#1a73e8>作者：</font>** Sophia Tang, Pranam Chatterjee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow-based generative models have enabled remarkable progress in fast and controllable generation across continuous and discrete state spaces, yet existing parameterizations are constrained to fixed dimensions or fixed sequence lengths. Here, we introduce Expanding Generative Flows (EFlows), which define flows between distributions of increasing dimensionality along an expanding interpolant that grows the state by augmenting it with conditional noise. Building on this construction, we propose Expanding Flow Maps (EFMs), a new class of flow maps that distill the expanding interpolant into efficient few-step generative models. Each EFM factors the map between any two timesteps into two learnable operations: an expand operator, which augments the state space with new coordinates or tokens conditioned on the current state, and a transport map, which pushes the expanded state forward along the interpolant. Composing these operators yields a single map that jointly expands and denoises the state, recovering existing fixed-canvas flows and flow maps as the special case in which the expand operator is the identity. We further extend the framework to the discrete simplex, enabling variable-size graph generation and variable-length sequence generation. Across both continuous and discrete modalities, we establish EFlows and EFMs as a principled framework for settings in which output size is itself a learned, controllable degree of freedom.

---


### 268. [Inference-Time Scaling of Diffusion Models via Progressive Seed Pruning](https://arxiv.org/abs/2607.21591)

**<font color=#1a73e8>作者：</font>** Rogerio Guimaraes, Pietro Perona  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion and flow-matching models dominate conditional image generation, yet inference-time scaling for these models is far less developed than for autoregressive language models. Because final quality is highly sensitive to the initial noise seed, many approaches spend extra compute on seed search or resampling under a black-box reward, but typically maintaining a constant memory footprint throughout inference. We show that relaxing this constraint enables an underexplored inference-time scaling axis: by front-loading exploration, evaluating many seeds early, and pruning aggressively, we can use a fixed compute budget more effectively. \emph{Progressive Seed Pruning} (\PSP) scores intermediate denoised estimates and progressively narrows the candidate set so that only promising trajectories are fully denoised, while keeping the total number of model evaluations fixed. Across diffusion and flow-matching backbones, \PSP \ consistently improves reward-guided selection and achieves higher GenEval scores (automated) and better human evaluation on prompt-alignment than best-of-$N$, importance-sampling, and tree-search baselines at matched compute. Project page: this https URL. Code: this https URL.

---


### 269. [Unified Video Dense Prediction from Disjoint Data](https://arxiv.org/abs/2607.21592)

**<font color=#1a73e8>作者：</font>** Yihong Sun, Seoung Wug Oh, Jiahui Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scene understanding requires simultaneous prediction about geometry, appearance, and semantics. However, existing task-specific annotations are fragmented across incompatible, domain-specific datasets. Current unified systems circumvent this by restricting training to fully co-annotated data, or by incurring the large computational cost of pseudo-labeling. To mitigate this, we introduce UniD, a unified video model that jointly predicts eight dense scene properties-depth, surface normals, semantic segmentation, boundaries, human parts, albedo, shading, and materials-all learned from disjoint, domain-specific datasets. We propose a simple yet effective distillation step in which per-task experts supervise a unified backbone through lightweight task projectors, eliminating the need for annotation overlap or pseudo-labeling. Our key insight is that the strong visual priors of a pretrained diffusion model are sufficient to bridge the domain gaps introduced by disjoint training sources, enabling robust generalization to scene-task combinations never seen during training. UniD achieves competitive performance against per-task specialists and multi-task baselines, with strong generalization to out-of-distribution scenarios and enhanced temporal and cross-task consistency. Code and video results are available at this https URL.

---


### 270. [Streaming Multi-Agent Autoregressive Diffusion Model with World State Registers](https://arxiv.org/abs/2607.21594)

**<font color=#1a73e8>作者：</font>** Sicheng Mo, Yuheng Li, Ziyang Leng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-agent interactive world models should not only generate consistent observations, but also maintain world states that persist across agents and evolve across views. Existing autoregressive video diffusion pipelines carry forward observation history as conditioning context, which makes shared state difficult to maintain in multi-agent and multi-view settings. We present WorldWeaver (W^2), a streaming multi-agent video diffusion model that augments rollout with cross-agent world state registers: learnable tokens that store shared world information, track individual agent status, and are dynamically updated after each generated chunk. We ground these registers with supervision signals spanning individual agent status, global state views including bird's-eye views, and scene text. We further improve the architecture with a Mixture-of-Transformers design that uses separate weights for world state modeling and visual frame modeling. Extensive experiments in two-agent Minecraft video generation show that explicit world-state modeling improves logical consistency and generation quality.

---


### 271. [3D-Aware VLMs with Implicit and Explicit Geometries](https://arxiv.org/abs/2607.21595)

**<font color=#1a73e8>作者：</font>** Wenhao Li, Xueying Jiang, Quanhao Qian 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite rapid progress, most existing vision-language models (VLMs) built from 2D visual inputs often struggle when handling various 3D tasks that require fine-grained spatial understanding and reasoning. To bridge this gap, we present VLM-IE3D, a unified framework that enhances the 3D spatial awareness of VLMs by equipping them with both implicit and explicit 3D geometries learned from RGB videos. Our VLM-IE3D introduces Implicit Geometry Tokens (IGTs) that capture high-level geometric priors from input videos, as well as complementary Explicit Geometry Tokens (EGTs) that encode detailed geometric structures from reconstructed 3D attributes. On top of that, VLM-IE3D comes with a 3D-aware adapter that effectively fuses the two types of geometric representations with 2D visual cues. This RGB-only design injects strong 3D inductive biases for fine-grained spatial understanding and reasoning without requiring any additional 3D inputs. Extensive experiments show that VLM-IE3D achieves superior performance consistently across various 3D tasks including 3D video detection, 3D visual grounding, 3D dense captioning, and spatial reasoning. Code and models are available at this https URL.

---


> [!TIP]
> 当前位于：**251-271**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-271**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
