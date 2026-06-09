# 📦 其他研究 | 2026年06月10日

> 本类共 **527** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-527](./part-11.md)

---

### 251. [OrderDP: A Theoretically Guaranteed Lossless Dynamic Data Pruning Framework](https://arxiv.org/abs/2606.08574)

**<font color=#1a73e8>作者：</font>** Chenhan Jin, Shengze Xu, Qingsong Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data pruning (DP), as an oft-stated strategy to alleviate heavy training burdens, reduces the volume of training samples according to a well-defined pruning method while striving for near-lossless performance. However, existing approaches, which commonly select highly informative samples, can lead to biased gradient estimation compared to full-dataset training. Furthermore, the analysis of this bias and its impact on final performance remains ambiguous. To address these challenges, we propose OrderDP, a plug-and-play framework that aims to obtain stable, unbiased, and near-lossless training acceleration with theoretical guarantees. Specifically, OrderDP first randomly selects a subset and then chooses the top-$q$ samples, where unbiasedness is established with respect to a surrogate loss. This ensures that OrderDP conducts unbiased training in terms of the surrogate objective. We further establish convergence and generalization analyses, elucidating how OrderDP affects optimal performance and enables well-controlled acceleration while ensuring guaranteed final performance. Empirically, we evaluate OrderDP against comprehensive baselines on CIFAR-10, CIFAR-100, and ImageNet-1K, demonstrating competitive accuracy, stable convergence, and exact control -- all with a simpler design and faster runtime, while reducing training cost by over 40%. Delivering both strong performance and computational efficiency, our method serves as a robust and easily adaptable tool for data-efficient learning. The code is publicly available at this https URL.

---


### 252. [A spectral audit framework reveals task-dependent aperiodic reliance across EEG and ECG deep learning](https://arxiv.org/abs/2606.08583)

**<font color=#1a73e8>作者：</font>** Jasmeet Singh Bindra, Siddharth Panwar, Shubhajit Roy Chowdhury  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning on physiological time series is interpreted through domain-specific features -- oscillatory rhythms in EEG, morphological complexes in ECG -- yet these signals sit atop a broadband aperiodic 1/f-like envelope that covaries with arousal, age, and pathology. We introduce a spectral audit framework combining aperiodic/periodic decomposition, phase-preserving Fourier interventions, sham controls, and simulation validation. Aperiodic reliance was task-dependent and architecture-general: across six neural architectures, flattening drops exceeded 0.42 balanced-accuracy points for sleep-wake classification, reached 0.07-0.13 for clinical abnormality detection, and remained minimal for motor imagery. Six of seven EEG foundation models showed FDR-significant aperiodic reliance on clinical EEG; age/sex and recording-era controls reduced but did not eliminate the effect. Applying the audit to PTB-XL ECG revealed neural drops of 0.32--0.36 persisting after demographic matching, confirming this confound class extends beyond EEG. Aperiodic controls should become standard for interpretable physiological time-series deep learning.

---


### 253. [Convolutional Sparse Coding via the Locally Competitive Algorithm on Loihi 2](https://arxiv.org/abs/2606.08584)

**<font color=#1a73e8>作者：</font>** Geoffrey Kasenbacher, Daniel Ruepp, Gerrit A. Ecke  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse coding provides a principled framework for signal representation by expressing an input as a linear combination of only a small number of basis functions. The Locally Competitive Algorithm (LCA) is particularly attractive in the context of neuromorphic computing because its dynamics, leaky integration, thresholding, and lateral inhibition map naturally to neuromorphic hardware. While prior work has studied non-convolutional LCA on Loihi 2, the convolutional setting is of particular interest because it introduces spatial structure, weight sharing, overlapping receptive fields, and scaling behavior that are more representative of practical sparse inference workloads. In this work, we present a Loihi 2 implementation of convolutional sparse coding via the LCA and evaluate it against a conventional GPU baseline on the same inference problems. The implementation follows a one-layer recurrent LCA formulation and extends it to convolutional feature maps with local inhibitory kernels derived from pairwise filter interactions. To the best of our knowledge, this is the first implementation and benchmark of convolutional LCA on Loihi 2. Our goal is not only to demonstrate feasibility, but also to clarify in which operating regimes convolutional sparse inference becomes attractive on neuromorphic hardware. The resulting study positions convolutional LCA as a useful benchmark for structured sparse inference on emerging neuromorphic systems.

---


### 254. [Quantum Global Variational Learning for Quantum Error Correction](https://arxiv.org/abs/2606.08592)

**<font color=#1a73e8>作者：</font>** Shun Ryuzaki, Hideo Mukai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficient quantum error correction is essential for the advancement of quantum computing. We propose a quantum neural network with a global structure that reduces the number of unitary matrices required in quantum circuits. This approach resulted in a 97\% reduction in training time and up to a 25\% improvement in the training completion rate, ultimately achieving a 100\% success rate in training while surpassing the error correction performance reported in previous studies. In addition, we demonstrated the enhanced robustness of quantum error correction against internal network noise. Moreover, the fidelity of quantum error correction under internal network noise increased by up to 15\% due to the reduced computational load.

---


### 255. [How Much Capacity Does EEG Denoising Need? Ultra-Compact Networks reveal Benchmark Saturation and Metric-Utility Gap](https://arxiv.org/abs/2606.08594)

**<font color=#1a73e8>作者：</font>** Jasmeet Singh Bindra, Siddharth Panwar, Shubhajit Roy Chowdhury  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning EEG denoising architectures have scaled from tens of thousands to tens of millions of parameters, yet no prior study has isolated model capacity as the experimental variable or tested whether reconstruction metrics predict downstream neural-signal utility. We address both gaps by fixing architecture, loss, data split, and training recipe while sweeping only channel width from 1.05K to 40.26K parameters in a minimal depthwise-separable convolutional U-Net. Models were evaluated on the EEGDenoiseNet benchmark, cross-dataset BCI transfer tests, controlled baseline retraining, and downstream motor-imagery classification with five decoder families across all nine BCI Competition IV-2a subjects. Reconstruction performance saturated by 3-6.5K parameters, with post-elbow gains of at most 0.015 correlation coefficient per log10-parameter unit. An 8.46M-parameter baseline retrained under the same pipeline matched the 40.26K compact variant on EOG--a 200x parameter gap yielding no advantage--while a Patch-Transformer control reproduced the same diminishing-return shape. Downstream evaluation exposed a classifier-dependent metric-utility gap: reconstruction-optimized denoising significantly degraded CSP+LDA classification across all nine subjects and three artifact types (best denoised accuracy 0.547 vs. 0.612 noisy baseline; Bonferroni p=0.0488), persisting on naturally recorded trials (Delta=-0.047; BH-FDR q=0.0049). End-to-end neural decoders showed variable or neutral effects. Standard EEG denoising benchmarks are saturated far below current model capacity, and reconstruction metrics do not predict BCI utility. Ultra-compact models at 33-46 KB and 1.27-2.61M FLOPs/segment are practical for edge deployment. These findings argue for capacity-controlled evaluation, harder task-aware benchmarks, and mandatory downstream validation.

---


### 256. [Reinforcement Learning for Flow-Matching Policies with Density Transport](https://arxiv.org/abs/2606.08602)

**<font color=#1a73e8>作者：</font>** Boshu Lei, Kostas Daniilidis, Antonio Loquercio  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present an online reinforcement learning (RL) algorithm for fine-tuning flow-matching policies in continuous-control problems. Our key insight is to view RL-based policy improvement as a transport of action densities towards regions of high reward, which naturally aligns with the transport formulation of flow matching models. Prior methods either approximate the current or optimal policy distribution or resort to distillation, which introduces biased gradients or sacrifices multimodal modeling capacity. In contrast, our approach for RL with Density Transport, which we name \emph{RLDT}, constructs a transport field from a maximum-entropy RL objective using Stein Variational Gradient Descent (SVGD). Then, it finetunes a pretrained flow matching policy to align with this field. Training with this alignment objective is nontrivial because flow-matching policies generate actions via a multi-step process, making direct gradient-based optimization challenging. To overcome this challenge and stabilize training, we approximate policy actions from intermediate denoising steps via expected-target estimation. This allows the transport-field update to propagate into the network parameters without unstable backpropagation through time. Experimental results demonstrate that RLDT outperforms competitive baselines in reward quality and convergence speed. This performance holds across diverse continuous-control tasks, encompassing both dense and sparse rewards, as well as state- and vision-based long-horizon robot manipulation. The project webpage is \href{this https URL}{this https URL}.

---


### 257. [Facial Expression Recognition in the Deep Learning Era: A Systematic Multi-Criteria Review of Methods, Models, Datasets, Performance, Challenges, and Future Research Directions](https://arxiv.org/abs/2606.08612)

**<font color=#1a73e8>作者：</font>** Spyridon Georgiou, Aggelos Psiris, Spyridon Evangelatos 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial Expression Recognition (FER) has advanced rapidly over the last decade, driven by the shift from handcrafted descriptors and shallow classifiers to deep convolutional, attention-based, vision-language, and foundation-model architectures, and by the parallel growth of large-scale in-the-wild benchmarks spanning categorical, dimensional, compound, micro-expression, Action Unit (AU), and intensity-estimation tasks. Yet the deep learning-based FER landscape has so far been reviewed only along narrow task-, architecture-, or application-specific axes, leaving a holistic, systematically organized account of its recent advances missing. This survey addresses that gap with a comprehensive review of recent deep learning-based FER, explicitly linked to the wider Facial Affect Recognition (FAR) domain. Its main contributions are: a) A description of FER's evolution into five distinct phases, from handcrafted features and classical machine learning to attention-based, vision-language, and foundation-model approaches, with the key milestone works of each, b) A multi-criteria taxonomy analyzing the literature along seven complementary axes: recognition task, input modality, face pre-processing pipeline, network architecture, learning strategy, acquisition setting, and application domain, c) A per-criterion comparative analysis, with critical insights into the strengths and limitations of each category under in-the-wild conditions, d) A task-organized review of public FER datasets, with their annotation schemes, modalities, and evaluation protocols, e) A compilation of performance metrics and a per-task quantitative comparison of representative state-of-the-art methods on widely adopted benchmarks, and f) A discussion of current challenges and promising future directions.

---


### 258. [Harnessing Streaming Video in the Wild](https://arxiv.org/abs/2606.08615)

**<font color=#1a73e8>作者：</font>** Dingyu Yao, Shuhuan Gu, Qingyi Si 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) are increasingly required to process unbounded video streams in applications such as video-call assistants, live commentary, and embodied robots. An ideal streaming system should support proactive interaction, long-horizon memory, and real-time processing, while resting on a VLM backbone capable of handling diverse in-the-wild streaming tasks. However, existing VLMs excel at offline video understanding but fall short in streaming capabilities and lack dedicated infrastructure for streaming deployment. We address this gap on three fronts. (i) For backbone capability, we construct \textbf{Streaming-Train-248K}, a streaming dataset paired with a novel training objective for adapting VLMs to streaming interaction and understanding. (ii) For real-world deployment, we introduce \textbf{Streaming Harness}, a plug-and-play system that endows any VLM with three core abilities: proactive interaction (per-second response decisions), long-term memory (12-hour context retention), and real-time processing (sub-second latency). (iii) To drive continued community progress on streaming capabilities, we design \textbf{Streaming-Eval}, a benchmark that reflects models' capabilities across diverse in-the-wild scenarios. Extensive experiments demonstrate consistent gains from our approach across all core capabilities required for streaming video understanding. We will open-source our data, code, and benchmark to advance the community's shift from offline video understanding to deployable streaming intelligence.

---


### 259. [Cross-Source Reasoning-based Correction for Author Name Disambiguation](https://arxiv.org/abs/2606.08617)

**<font color=#1a73e8>作者：</font>** Fanjin Zhang, Yunhe Pang, Bo Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Author name disambiguation is a critical challenge in academic search systems, often addressed through from-scratch and real-time disambiguation approaches. However, current algorithms remain vulnerable to cumulative errors of paper-author assignments and overlook inconsistent assignments across different sources. Resorting to expert annotation is resource-intensive. To this end, this paper explores a new perspective for author name disambiguation: cross-source correction by leveraging inconsistent assignments across sources. We propose CrossND, a full-stack framework that integrates data refinement, cross-source reasoning, and test-time scaling. First, a chain-of-refinement pipeline denoises author profiles and produces more accurate paper-author matching probabilities. Second, a supervised fine-tuning process incorporates these refined signals and a probabilistic soft logic-based cross-correction module to infer the assignments of which sources are incorrect. Third, test-time scaling further enhances the accuracy and robustness of the predictions. Experiments on real-world datasets indicate that CrossND consistently outperforms 17 baselines by leveraging cross-source reasoning without human intervention.

---


### 260. [SSAFE: Simple and Strong AI-Generated Image Detection via Frozen Vision Encoders](https://arxiv.org/abs/2606.08634)

**<font color=#1a73e8>作者：</font>** Seunghyun Lee, Byoungkwon Kim, Jaehyun Nam 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of generative models has blurred the boundary between synthetic and real imagery, creating an urgent need for reliable deepfake detection. Yet most existing approaches rely on massive real--fake datasets, which are increasingly difficult to maintain as new generators continue to emerge. In this work, we investigate how much information about image authenticity is already encoded in modern multimodal vision representations. We find that frozen multimodal encoders naturally separate real and synthetic images in their embedding space, enabling a simple linear classifier to achieve strong performance without task-specific fine-tuning. Motivated by this observation, we develop a representation-aware data curation strategy that selects a compact set of representative generators for training. The resulting training set contains only 10K images, compared to 288K in AIGIBench and 4M in OpenFake, while improving robustness to unseen generators and distribution shifts. We additionally introduce RealWorldBench, a benchmark consisting of modern camera photographs, contemporary stock images, and outputs from recent commercial generators. Experiments across multiple benchmarks show that combining frozen multimodal representations with carefully curated training data provides a simple and effective approach to AI-generated image detection.

---


### 261. [Learnable Token Sparsification for Efficient Gigapixel Whole Slide Image Reasoning](https://arxiv.org/abs/2606.08641)

**<font color=#1a73e8>作者：</font>** Jingzhi Chen, Landi He, Zhuo Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The processing of gigapixel whole slide images within vision language models faces a major difficulty due to an excessive number of visual tokens. Existing solutions typically rely on spatial downsampling or heuristic pruning strategies that operate without training, and these methods often discard subtle but clinically meaningful patterns because pathological evidence is scattered irregularly across the tissue. To overcome this limitation, we reformulate token reduction in whole slide images as a trainable sparsification problem, allowing the model to learn an optimal selection strategy instead of following fixed heuristics. We propose a decoupled routing architecture. To enable gradient propagation through the nondifferentiable pruning operation during training, we introduce a component called SparseLearn. This component uses a variance-preserving noise gate that regulates the information flow of each patch via a differentiable Soft Top-K operator, together with a diagonal attention denoiser that recovers perturbed representations without leaking spatial information. At inference time, the SparseLearn module is entirely discarded, and the trained scorer applies a deterministic Hard Top-K operator to keep only the highest scoring 32 tokens, incurring no extra computation. By compressing the visual sequence down to a sparse set of just 32 tokens, which represents as little as 0.78% of the original length, our framework achieves 73.32% overall accuracy on SlideBench (TCGA), consistently surpassing sampling-based baselines and general-purpose vision language models. It also demonstrates strong zero shot generalization on SlideBench (BCNB) and WSI VQA*. By resolving the visual context bottleneck and preventing the dilution of sparse diagnostic evidence, this work provides a highly efficient paradigm for end to end gigapixel whole slide image reasoning.

---


### 262. [Operator learning for the 2D incompressible Navier-Stokes equations: a conformal prediction approach in the data-scarce regime](https://arxiv.org/abs/2606.08654)

**<font color=#1a73e8>作者：</font>** Weinan Wang, Bowen Gang, Hao Deng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose a perturbation-based conformal prediction framework for uncertainty quantification in operator learning, with a focus on the 2D Navier--Stokes equations. While neural operators provide fast surrogates for expensive PDE solvers, they do not by themselves provide calibrated uncertainty for spatiotemporal field predictions. Our approach wraps a trained Fourier Neural Operator (FNO) with split conformal prediction and constructs the local uncertainty scale by comparing the predictions of two operators trained on nearly identical datasets: one on the original labels and one on labels perturbed by small Gaussian noise. We consider this procedure in the data-scarce regime, where the total label budget is fixed and methods that require a separate uncertainty network must divide training data between multiple models. On the 2D Navier--Stokes benchmark, the perturbation-based method produces substantially narrower conformal bands than existing methods under matched total data budgets while maintaining the target simultaneous coverage. These results suggest that perturbation sensitivity is a practical and sample-efficient uncertainty proxy for conformalized neural operators.

---


### 263. [Extending Ontologies: From Dense Embeddings to Hybrid Quantum-Fuzzy Systems](https://arxiv.org/abs/2606.08658)

**<font color=#1a73e8>作者：</font>** Angjelin Hila  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs have revolutionized knowledge representation and retrieval, but lack the explicit modeling that knowledge ontologies possess. This paper surveys the ways that ontologies and knowledge graphs have been integrated with dense embedding algorithms. All hitherto attempts involve a trade-off between probabilistic and crisp inference. This paper proposes a novel frontier for devising knowledge representation systems that can simultaneously accommodate probabilistic and crisp inference in the same representation. To this effect, the paper proposes neuro-quantum-fuzzy systems as knowledge representation systems that accommodate both classical and contextual inference implemented through quantum-neural networks (QNN).

---


### 264. [X-rated Compliance Theater: An Empirical Evaluation of European Age Verification Systems in Adult Websites](https://arxiv.org/abs/2606.08667)

**<font color=#1a73e8>作者：</font>** Simone Lavermicocca, Michekle Carminati, Stefano Longari  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Age verification is rapidly emerging as a central regulatory instrument for protecting minors online, with several jurisdictions mandating its deployment for access to adult and pornographic content. This regulatory direction raises significant privacy concerns, as it risks binding sensitive content access to identity-related attributes. It also introduces security risks, since age-verification mechanisms are often outsourced to third-party providers with limited transparency into the robustness of their verification processes. In this work, we conduct, to the best of our knowledge, the first exploratory security assessment of regulation-mandated age-verification mechanisms deployed by adult websites. Rather than treating age verification as a purely regulatory question, we empirically examine whether current deployments provide security guarantees commensurate with the privacy risks of relying on sensitive identity-related data. Our methodology combines ecosystem mapping, adversary modeling, and empirical testing across four countries, covering document-based verification, biometric age estimation, indirect signals, and website-workflow integration. Our results reveal systemic weaknesses across mechanisms and integrations under realistic threat assumptions, including failures against low-cost, widely accessible attacks. Finally, we derive concrete guidelines and design directions for mitigating the security and privacy risks exposed by current age-verification deployments.

---


### 265. [WaveDiT: Distribution-Aware Wavelet Flow Matching for Efficient 3D Brain MRI Synthesis](https://arxiv.org/abs/2606.08670)

**<font color=#1a73e8>作者：</font>** Danilo Danese, Angela Lombardi, Giuseppe Fasano 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large and demographically balanced datasets are essential for reliable neuroimaging biomarkers. Full-resolution 3D brain MRI synthesis can support data augmentation in this setting, but existing approaches either incur prohibitive computational cost at volumetric scale or rely on lossy latent compression that may compromise anatomical detail. As a result, practical 3D generative augmentation often requires specialized compute infrastructure. We propose WaveDiT, a conditional flow matching framework operating in the coefficient space of a 3D Haar Discrete Wavelet Transform. The model combines factorized spatio-depth attention with band-wise heteroscedastic uncertainty modeling derived from higher-order wavelet statistics. Predicted log-variance is integrated directly into both the flow objective and conditioning pathway, enabling adaptive precision consistent with the heavy-tailed and input-dependent variance structure of anatomical detail. This formulation supports full-resolution 3D synthesis under practical memory and time constraints on a single modern GPU. Evaluation on a multi-site cohort demonstrates improved alignment between generated and real MRI distributions, together with enhanced downstream brain age prediction and region-level anatomical agreement relative to diffusion, latent, and wavelet-based baselines. Code is available at this https URL

---


### 266. [SkillHone: A Harness for Continual Agent Skill Evolution Through Persistent Decision History](https://arxiv.org/abs/2606.08671)

**<font color=#1a73e8>作者：</font>** Zhiwei Li, Yong Hu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agent skills extend language-model agents with task-specific procedures, scripts, and references, but the tasks and environments they target continually change. Existing methods improve skills in bounded runs and retain only the final artifact, discarding the decision history that later agents need to interpret prior revisions, evaluations, and rejected alternatives. We introduce SkillHone, a harness for continual agent skill evolution grounded in persistent decision history. SkillHone pairs skill revisions with evaluation-side evidence that supplies practice feedback, recording structured histories of diagnoses, revisions, evidence, and outcomes. Role-separated subagents run candidate skills on practice probes with redacted reporting and propose revisions informed by prior decisions, enabling cross-session refinement without rediscovering past rationale. We evaluate SkillHone on deep-research benchmarks in a raw open-web setting, where agents are not given an integrated search stack and must organize retrieval through portable skills. We compare against a deep-research agent backed by commercial retrieval services. With Qwen3.6-35B-A3B as the evaluation-time backbone, the resulting skills outperform the deep-research agent by 15.8 points on GAIA and 3.2 points on WebWalkerQA-EN, while also exceeding prior skill-evolution methods.

---


### 267. [Learning to Solve Generative ODEs Beyond the Linear Span](https://arxiv.org/abs/2606.08672)

**<font color=#1a73e8>作者：</font>** Sihyeon Kim, Seunghun Lee, Vikas Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion and flow generative models sample by integrating a learned ODE, but high quality still requires many sequential model evaluations. Solver learning reduces this cost by adapting scalar coefficients, timesteps, or both, while keeping the backbone model fixed. In this work, we identify a structural bottleneck in this update family: each step remains span-limited. Since the scalar-coefficient update lies in the span of buffered velocity evaluations, it can fit only the in-span component while leaving any out-of-span residual unreachable by scalar recombination alone. We propose SpanLift, a lightweight neural solver that augments scalar-coefficient updates with a spatial residual operator. SpanLift keeps a fixed base solver as an in-span prior and learns a spatial residual operator over the state and velocity buffer. The operator is trained by endpoint teacher matching, preserves the pretrained backbone, and adds no model NFEs. Empirically, the learned correction transfers across base solvers and is predominantly out-of-span. Across pixel-space diffusion, latent flow matching, and precipitation nowcasting, SpanLift achieves state-of-the-art few-step sampling. With only 3 NFE, it improves CIFAR-10 FID from 8.16 to 5.69 and ImageNet FID from 17.37 to 11.83.

---


### 268. [ClinicalAligner26AM: A Cross-Lingual Aligner for Dataset Translation; Evidences from the MultiClinCorpus Shared Task](https://arxiv.org/abs/2606.08673)

**<font color=#1a73e8>作者：</font>** François Remy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Word-level cross-lingual alignment is central to annotation projection, translation auditing, and cross-lingual faithfulness estimation, yet existing neural aligners are rarely adapted to specialized domains. In this paper, we introduce ClinicalAligner26AM, a large-context multilingual aligner model for biomedical and clinical text initialized from ClinicalEncoder26AM. Our training recipe is inspired by AWESoME Align. We build our soft alignment target by sharpening with Sinkhorn-Knop optimal transport a cost matrix established for parallel clinical texts and conversations through the fusion of sentence-level, phrase-level, and token-level signals. We distill this sharpened alignment matrix directly into our student aligner, by encouraging its naive cosine-based token similarity scores to match this target. At inference time, we project source-span scores through the learned token alignment matrix and decode the longest valid high-scoring span in the target text, optionally supported by MultiClinNER predictions summarized in Appendix B. We evaluate CA26AM on the MultiClinCorpus shared task, which projects Spanish clinical entity annotations into six target languages. Our two submitted systems ranked respectively first and second across all languages and entity types, with character-weighted F1 scores above 0.95 in nearly all settings.

---


### 269. [BioVid: Autoregressive Video Generation with Biological Behavior Semantic Comprehension](https://arxiv.org/abs/2606.08674)

**<font color=#1a73e8>作者：</font>** Tsung-Wei Pan, Jung-Hua Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing video generation frameworks treat sequence duration as an externally prescribed parameter -- fixed frame counts or text prompts -- producing clips whose temporal boundaries are decoupled from the statistical structure of real behavioral data. This assumption is fundamentally misaligned with biological behavior, where action duration varies naturally across individuals and instances and is encoded in the data itself. We present BioVid, a data-driven autoregressive video generation framework that learns the temporal structure of biological behaviors directly from training data, including their natural length distributions. In the first stage, a Finite Scalar Quantization GAN (FSQ-R3GAN) tokenizer encodes each video frame into a compact discrete representation, combining the stabilized relativistic training objective of R3GAN with FSQ's guaranteed codebook utilization to achieve high-fidelity spatial reconstruction without codebook collapse. In the second stage, a causal Transformer models the resulting token sequences autoregressively and learns to emit an End-of-Sequence (EOS) token when the behavioral event reaches semantic closure, with the termination distribution emerging naturally from the training data rather than any human-specified constraint. Experiments on a human drinking behavior dataset (NTU RGB+D, A001, n=94) demonstrate that BioVid's generated length distribution closely matches that of held-out test data, achieving a Wasserstein-1 distance of 1.24 against the ground truth -- compared to 6.05 for a fixed-length baseline and 15.48 for VideoGPT -- while maintaining competitive spatial fidelity.

---


### 270. [Distortion-Aware PETR for BEV Object Detection with Mixed Pinhole-Fisheye Cameras](https://arxiv.org/abs/2606.08680)

**<font color=#1a73e8>作者：</font>** Xiangzhong Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fisheye cameras are widely deployed in autonomous driving perception suites for their low cost and full-coverage field of view (FOV), yet their potential remains underleveraged in 3D object detection. Severe radial distortion challenges most BEV detectors by violating the fundamental assumption of uniform sampling. To bridge this gap, we propose Distortion-Aware PETR (DAPETR), a projection-free detector tailored for mixed pinhole-fisheye camera setups. DAPETR incorporates two key learned-adaptive modules: a unified distortion-aware positional embedding that harmonizes positional encodings for image representations with fisheye geometry, and a bidirectional feature-geometry co-modulation module that mutually adapts image features and 3D positional embeddings. In our experiments on a converted KITTI-360 benchmark, we systematically compare our learned adaptive approach against PETR in polar coordinates (PolarPETR). We find that while both methods improve over the baseline, our learned modules achieve superior performance. Crucially, we uncover a negative interaction when combining both strategies, revealing that learned adaptation and explicit geometric reparameterization can conflict. Our final DAPETR model significantly advances the research and benchmark for fisheye BEV detection, providing critical insights into effective distortion-aware 3D perception design other than image rectification.

---


### 271. [Asymptotic Optimality of the High-Dimensional Gaussian Mechanism and Improved Low-Dimensional Mechanisms for Differential Privacy](https://arxiv.org/abs/2606.08681)

**<font color=#1a73e8>作者：</font>** Yu Wei, Alexander Bienstock, Antigoni Polychroniadou  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The additive noise mechanism is a foundational tool for differential privacy (DP) of $T$-dimensional real-valued vector queries. The Gaussian mechanism, utilizing Gaussian noise, is the mostly widely used such mechanism, due to its simplicity and strong privacy guarantees. In this work, we provide justification for this choice, showing that as the dimension $T\to\infty$, no additive-noise mechanism can asymptotically improve on the Gaussian mechanism's privacy--utility tradeoff for the strong privacy settings typically this http URL also develop a new family of \emph{Spherical Generalized Gamma} DP mechanisms, which contains both the Gaussian mechanism and the recently studied $\ell_2$ mechanism (Joseph \emph{et al.}, ICML 2025). We identify members of this family that outperform both the Gaussian and $\ell_2$ mechanisms in certain low-dimensional settings, and show tight composition of all mechanisms in this family, answering an open question of Joseph \emph{et al.}~regarding the $\ell_2$ mechanism.

---


### 272. [BLUE: Toward Better Language Use in Efficient Vision-Language-Action Models for Autonomous Driving](https://arxiv.org/abs/2606.08684)

**<font color=#1a73e8>作者：</font>** George Ling, Lijin Yang, Hao Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present BLUE, a minimal method for better language use in vision-language-action (VLA) models for autonomous driving (AD). Through extensive analysis, we reveal that language matters on only a small fraction of routes, but on those routes it can greatly improve or degrade performance. Generating language at every frame is therefore inefficient, since most computation is spent on frames that do not benefit from language. We further show that pretrained VLA hidden states potentially already encode whether language will benefit a given frame, even though scene complexity and kinematic features alone struggle to predict this. Based on this finding, BLUE trains a lightweight gate on frozen VLA hidden states to decide per frame whether to activate language generation or predict actions directly, without modifying the backbone or requiring additional human annotation. With just a 0.11M-parameter gate, BLUE sets a new state of the art on both benchmarks, achieving 76.2% success rate on Bench2Drive and 36 driving score on Longest6 v2, while delivering 2.54x inference speedup and 8.9% success rate improvement over the backbone. BLUE provides a practical path toward efficient language-augmented AD, showing that VLA models can retain the benefits of language at a fraction of the cost. Our code, data, logs and checkpoints are fully available on this https URL.

---


### 273. [Shift-Dependent Asymmetry: Orthogonal Inverse Low-Rank Adaptation for Federated Medical Segmentation](https://arxiv.org/abs/2606.08687)

**<font color=#1a73e8>作者：</font>** Xingyue Zhao, Wenke Huang, Linghao Zhuang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptation (LoRA) enables efficient federated fine-tuning of segmentation foundation models for medical imaging. However, most federated LoRA methods adopt a uniform aggregation rule, which breaks under the encoder-decoder asymmetry in medical segmentation: the encoder is dominated by appearance shifts, while the decoder is dominated by supervision variations. This mismatch entangles shared anatomy with site-specific biases and harms generalization. To address this, we propose Inverse Asymmetric Tuning (IAT). IAT aligns adaptation with heterogeneity sources by personalizing module-specific components in the encoder to absorb appearance shifts and in the decoder to accommodate site-dependent supervision, while retaining a shared pathway for transferable consensus. However, structural separation alone is insufficient under LoRA's bilinear parameterization, where multiplicative coupling can still cause site-specific updates to leak into the shared direction. We therefore introduce a Subspace Orthogonality Regularizer that penalizes shared-local collinearity in the effective update space, mitigating leakage without extra communication. Experiments show consistent improvements over strong federated LoRA and parameter-efficient FL baselines.

---


### 274. [Hierarchical Projection for Adaptive Knowledge Transfer](https://arxiv.org/abs/2606.08691)

**<font color=#1a73e8>作者：</font>** Samhita Pal, Tian Gu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern data-driven applications increasingly involve learning from multiple heterogeneous sources, where a target dataset is limited but related information is available across domains. Naively combining these sources can degrade performance when relevance varies or spurious signals are present, posing a fundamental challenge for trustworthy cross-domain learning. We propose Projection Transfer Learning (ProjectionTL), a unified framework that integrates hierarchical Bayesian modeling with adaptive projection for selective knowledge transfer. The key idea is to decouple transfer at two levels: first, we construct a source-guided hierarchical prior that aggregates information across sources using data-driven weights, capturing global alignment between each source and the target; second, we refine this borrowing through a posterior-projection step that operates at the feature level, selectively retaining coordinates that exhibit local agreement with the target signal. This two-stage design enables the method to simultaneously perform source selection and feature selection, thereby mitigating negative transfer while preserving interpretability. ProjectionTL provides a principled approach to integrating heterogeneous data across domains, bridging statistical modeling and modern machine learning paradigms for robust and interpretable transfer. Through simulations and real-world biomedical applications, we demonstrate improved accuracy, stability, and interpretability compared to existing methods. Our framework offers a scalable and generalizable strategy for trustworthy cross-domain learning in high-dimensional settings.

---


### 275. [AutoSUT: The Environment Semantics Gap in Structured CTI for Adversary Emulation](https://arxiv.org/abs/2606.08700)

**<font color=#1a73e8>作者：</font>** Sidnei Barbieri, Ágney Lopes Roth Ferraz, Lourenço Alves Pereira Júnior  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Structured Cyber Threat Intelligence (CTI) is increasingly used for adversary emulation, detection evaluation, and cyber range design. However, these workflows still require a target System Under Test (SUT) whose environment is not fully described by public CTI. We measure how much of that environment can be derived from MITRE ATT&CK Structured Threat Information Expression (STIX) bundles. Using the ATT&CK Enterprise, Mobile, and Industrial Control Systems datasets, with CAPEC and FiGHT as comparison datasets, we evaluate platform coverage, software specificity, vulnerability evidence, and deployment compatibility. Platform annotations are common, but software references rarely include versions or Common Platform Enumeration (CPE) identifiers. In Enterprise, 97.6% of software objects lack both, and campaign-level Common Vulnerabilities and Exposures (CVEs) remain sparse.
Our results show that ATT&CK-style structured CTI can narrow candidate environments and support lower-bound backend-family assignment, but structured fields alone are insufficient to derive a replay-ready SUT. Profile confusion decreases from 1.3% when one software item is linked to 0% when two are linked. The results identify a boundary between environment details supported by the corpus and the version, vulnerability, and deployment information that must come from external sources. Keeping corpus-supported elements fixed while varying only analyst-authored details yields multiple distinct, campaign-compatible SUTs, including an executable witness exploiting the same real vulnerability. Structured CTI, therefore, constrains but does not uniquely determine the environment, highlighting the need to separate corpus-supported commitments from analyst-authored assumptions in replay-ready emulation.

---


### 276. [Is Telehealth Better Used to Treat Patients or Help Other Physicians Treat Patients? An Agent-Based Modeling Study of Healthcare Provision](https://arxiv.org/abs/2606.08701)

**<font color=#1a73e8>作者：</font>** Michael Chary  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Telehealth, the delivery of medical care remotely, is hoped to increase access to specialty services or decrease health care utilization. Physicians can provide telehealth to each other or to patients. Specialists often treat complex patients who can be adequately cared for only in academic hospitals, suggesting that providing specialty services via telehealth will reallocate rather than reduce system utilization. Here I use agent-based modeling to investigate telehealth's effects on clinical outcomes and system utilization in medical toxicology. I found that physician-physician telehealth increased patient health but system utilization did not change. The effects were more pronounced as clinical complexity increased. Physician-patient telehealth increased cost and system utilization but not clinical outcomes. Within the limitations of our approach, these results suggest that telehealth is more cost-effective for improving generalist access to specialist knowledge than in providing care to the public.

---


### 277. [ConMem: Structured Memory-Guided Adaptation in Training-Free Multi-Agent Systems](https://arxiv.org/abs/2606.08702)

**<font color=#1a73e8>作者：</font>** Zhixun Tan, Qiang Chen, Tairan Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances have improved the adaptive capabilities of LLM-based multi-agent systems (MAS) through memory-, skill-, and learning-based approaches, yet these approaches remain challenged by noisy trajectories, insufficient modeling of memory-skill relations, and reliance on additional training or high-quality supervision. To address these limitations, we propose ConMem, a relation-aware and training-free framework that enables efficient multi-agent adaptation through cross-experience coordination. Specifically, ConMem distills historical interaction trajectories into structured memory cards to capture reusable strategies and cues, organizing them into a relation-aware memory graph. At runtime, ConMem retrieves cards according to task needs and coordinates them through the card graph to resolve strategy conflicts and recover their dependencies. Combined, these modules yield structured and relation-aware guidance, enabling robust, lightweight adaptation in multi-agent systems without additional training. Extensive experiments across multiple benchmarks and mainstream MAS architectures show consistent gains over existing memory architectures, with improved inference-time efficiency through pruning more than 50% of expanded candidates and reducing planning overhead by over 80%. Our codes are available at this https URL

---


### 278. [SNR-ST-Mix: Sample-specific Neighborhood Regression Mixup for Augmented Spatial Transcriptomics Imputation with Deep Neural Network](https://arxiv.org/abs/2606.08712)

**<font color=#1a73e8>作者：</font>** Hongyi Yu, Yaoyu Fang, Jiahe Qian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Purpose: Spatial transcriptomics (ST) enables gene expression measurements within the tissue context. However, these measurements are often noisy, low-resolution, and sparsely sampled, which limits the recovery of fine spatial structure. Deep neural networks have become powerful tools for expression imputation from histology, but their performance remains constrained by limited sample sizes and a lack of biologically informed augmentation. Most of the existing augmentation strategies for learning are designed for classification tasks rather than regression, which neglect spatial and transcriptomic relationships, leading to biologically implausible interpolations that hinder prediction performance. Approach: To address these limitations, we propose SNR-ST-Mix, a geometry- and expression-aware data augmentation framework designed specifically for ST data. It constrains mixing to a spot's k-nearest spatial neighbors and adaptively weights interpolation coefficients based on expression similarity, generating augmented samples that preserve local biological structure while ensuring spatial smoothness. This dual conditioning yields synthetic examples that expand the effective training manifold, promote generalization, and enhance prediction stability under sample-specific training. Results: Extensive experiments with various tissue types demonstrate that SNR-ST-Mix consistently outperforms conventional augmentation methods without requiring architectural changes or additional computation. Conclusions: SNR-ST-Mix provides an effective and biologically principled augmentation strategy for spatial transcriptomics regression tasks. By explicitly leveraging spatial geometry and transcriptomic similarity, it expands the effective training manifold and improves predictive performance without increasing model complexity.

---


### 279. [Operationalizing Linguistic Methods through Prompt-Engineering Skills: An Automatic Chinese Web Neologism Detection Pipeline](https://arxiv.org/abs/2606.08715)

**<font color=#1a73e8>作者：</font>** Yufeng Wu, Meichun Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a method for automatic Chinese web neologism detection that operationalizes traditional linguistic identification principles as prompt-engineering skills. The method has four stages: tokenizer-independent character n-gram candidate generation; dictionary anchoring with a Pointwise Mutual Information pre-filter; a well-formedness skill based on Chinese word-formation principles; and a combined rule and three-way classification skill that distinguishes neologism, entity, and none. Applied to the BAAI CCI 3.0 corpus (267M documents), the method produces 226,959 classified candidates including 4,853 labeled neologisms. To evaluate the method, we develop a per-stage conditional recall decomposition in which the pipeline's strict recall factors mathematically into the product of stage conditional recalls. Applied to Hou (2023) (4,199 entries), the decomposition exposes Stage 1 candidate coverage and Stage 4B LLM semantic judgment as the two bottlenecks (R=41.5% and 60.0% respectively), while intermediate stages are near-lossless. A length-stratified analysis further reveals that the structural well-formedness skill is length-invariant (>= 96.9%) whereas the semantic novelty-classification skill is length-dependent (65.6%/59.0%/44.1% across 2/3/4-character candidates), mapping a current boundary of skill-based linguistic operationalization. We release the method, pipeline outputs, and evaluation protocol as public resources.

---


### 280. [Deep Active Re-Labeling: Toward Noise-Resilient Annotation Efficiency](https://arxiv.org/abs/2606.08718)

**<font color=#1a73e8>作者：</font>** Md Abdullah Al Forhad, Weishi Shi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While Deep Active Learning (DAL) effectively reduces human annotation costs, its efficacy is constrained by human annotation errors. This is because the data sampled for active learning is assumed to be highly informative for training. When human annotators introduce errors into this informative data at a certain rate, the active learning performance drops significantly and, in some cases, even exhibits worse outcomes than passive learning. In this paper, we first analyze the impact of human annotation errors in the DAL setting. Then we propose a framework to address the human annotation noise problem for DAL. Informed by human learning patterns, the core idea of our proposed solution involves allocating a portion of the human annotation budget to re-annotate data that has already been labeled. Previous theoretical work suggests that when the model possesses a certain level of ability to identify potentially noisy data, even re-labeling a small fraction of the data can effectively remove noise from the active training set. To achieve this, we implement two active noise sampling strategies to detect noise under different circumstances and allocate a part of the annotation budget to re-annotate these instances. Our approach imbues active learning with a revisiting and introspective behavior. Our experiments demonstrate that, under the same annotation budget, our method is more data-efficient and yields a relatively noise-free annotation dataset in the end.

---


### 281. [Thinking Without Images: Internalizing Visual Manipulation with On-Policy Self-Distillation](https://arxiv.org/abs/2606.08719)

**<font color=#1a73e8>作者：</font>** Yishuo Cai, Jiahui Liu, Yuanxin Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> ''Thinking with Images'' has emerged as an effective paradigm for fine-grained visual reasoning: by explicitly zooming into relevant regions and reasoning over crops, models can access local evidence that is difficult to recover from a single global image. However, this benefit comes with redundant tool invocations and longer inference traces. Moreover, when such behaviors are learned mainly from outcome reward, the resulting intermediate crops or visual cues can be noisy or fail to faithfully capture task-relevant visual evidence. In this work, we ask whether the reasoning benefits of ''Thinking with Images'' can be internalized through Thinking with Imagination: an internal process that decides where to look and imagines what visual cues closer inspection would reveal without actually invoking tools. We propose Imagine-OPD, an on-policy self-distillation framework in which a teacher plays the role of a ''Thinking with Images'' reasoner during training: it receives privileged zoomed evidence views derived from annotated regions, and supervises the model's own imagination reasoning trajectories. Imagine-OPD does not require an external teacher or high-quality imagination demonstrations. Experiments on vision-centric benchmarks show that Imagine-OPD achieves the best average performance among compared models while significantly reducing inference overhead compared with ''Thinking with Images'' methods.

---


### 282. [A Geometric Measure of Linear Separability for Neural Representations](https://arxiv.org/abs/2606.08721)

**<font color=#1a73e8>作者：</font>** Yi Wei, Xuan Qi, Furao Shen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern neural classifiers commonly rely on linear readouts, yet predictive metrics alone do not characterize the class-wise geometry of the representations on which such readouts operate. We introduce the directional linear separability measure (LSM), a finite-sample diagnostic for one-sided affine separability. For a target class A and a competing set B, LSM searches over affine halfspaces that contain all samples in A and measures the smallest competing-sample intrusion that must remain on the target side, normalized by |A|. The resulting quantity is asymmetric, class-wise, target-normalized, and applicable to finite representations extracted from neural networks. We establish its supporting-hyperplane characterization, relate it to optimal affine classification accuracy, and prove invariance under full-rank linear embeddings. These results separate changes caused by linear reparameterization from those caused by information loss or nonlinear geometric transformations. We also give a penalty-based affine search for estimating class-wise LSM in high-dimensional features, with reported values computed from the original discrete preservation and violation criterion. Finally, we analyze coordinatewise gated nonlinearities as finite-sample geometric operators and empirically use LSM to diagnose class-wise intrusion across common deep-learning components and architectures.

---


### 283. [Structure-Conditioned Actor-Critic Branches for Quality-Diversity Reinforcement Learning](https://arxiv.org/abs/2606.08735)

**<font color=#1a73e8>作者：</font>** Lianrong Zuo, Peilan Xu, Yong Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Quality-diversity reinforcement learning (QD-RL) aims to construct policy repertoires that contain both high-performing and behaviorally diverse policies. Existing QD-RL methods mainly diversify policy instances after rollout evaluation or use learned value information to improve policy quality and behavior targeting, while the learning branches that generate candidate policies remain less explored. This paper proposes SV-QD-RL, a structure-value coupled framework that represents each candidate as a structure-conditioned actor-critic branch. Each branch contains an actor, a structural mask, a branch-specific critic, a replay state, and evaluation attributes including behavior, return, sparsity, and value profile. The structural mask defines the actor subspace in which the branch learns, while the branch-specific critic and replay state shape its value-learning trajectory. A branch-aware QD archive then evaluates and retains branches according to behavioral quality, structural footprint, and value-profile information. Experiments on MuJoCo continuous-control tasks show that SV-QD-RL constructs policy repertoires with strong archive quality and behaviorally useful diversity. Ablation and diagnostic analyses further indicate that structural conditioning, critic differentiation, and memory-consistent refinement make complementary contributions to behavioral specialization. Schedule-aware repertoire evaluation shows that the learned archive provides selectable policy alternatives under changing behavior-level requirements. These results suggest that coupling actor structure with branch-specific value learning is an effective mechanism for generating diverse QD-RL policy repertoires.

---


### 284. [Declarative Outcome-Conformant Synthesis: Exact, Closed-Form Specification Satisfaction and a Conformance Benchmark](https://arxiv.org/abs/2606.08736)

**<font color=#1a73e8>作者：</font>** Muhammed Rasin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study a capability the dominant paradigm in synthetic tabular data does not provide: exact satisfaction of a declared analytical outcome with no source data. Imitation methods (copulas, GANs, diffusion) learn a real distribution and sample from it, and are judged on fidelity to real data. A large, practical class of needs is different: generating data with no source data ("cold start") that reproduces a declared outcome (a revenue curve, a churn rate, a group share) across a relational schema. Off-the-shelf imitation tools offer no interface for such targets, and no sampler can hit an exact aggregate, because sampling has variance. On a real public dataset, off-the-shelf learned synthesizers trained on that very data miss the declared monthly aggregate by 74 to 86 percent; a per-period steelman cuts the miss to about 19 percent and still cannot reach 0; a closed-form generator reaches exactly 0. We name this task outcome-conformant synthesis, argue its evaluation axis is conformance rather than fidelity, and show the two axes are orthogonal. We contribute: (1) a formal account showing a widely-used family of exact-aggregate generators is exactly conditional-sum sampling of a Gamma population (via Lukacs' characterization), with closed-form exactness, a closed-form marginal CV, and scale-invariance; a controlled experiment maps the boundary, enforcing the exact aggregate costs at most 0.006 in 1-Wasserstein distance to an arbitrary external marginal, the rest being shape-family mismatch; (2) SpecBench, to our knowledge the first benchmark to measure conformance to analytical outcomes for cold-start relational synthesis; and (3) a closed-form, deterministic reference system. Exact aggregation alone is trivial; the contribution is conformance jointly with closed-form marginals, integrity, determinism, and zero source data. We concede fidelity to imitation where real data exists.

---


### 285. [AUCp: Pseudo-AUC for Inference Model Selection with Unlabeled Validation Data in Abnormality Detection](https://arxiv.org/abs/2606.08742)

**<font color=#1a73e8>作者：</font>** Md Mahfuzur Rahman Siddiquee, Fazle Rafsani, Jay Shah 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Abnormality detection is a crucial yet challenging task in medical image analysis. Distinguishing abnormalities from normal data by learning to reconstruct normal-only data alleviates the reliance on labeled datasets. However, many studies, even if unsupervised, rely on a labeled validation set to select the best model for inference from multiple training iterations. For many diseases labeled data are unavailable and substantially time consuming to obtain. To address this, AUCp - a novel metric that supports abnormality detection for unsupervised and self-supervised methods is proposed. Instead of evaluating the realism of reconstructed images to select the best of model for inference, it focuses on actual detection performance and without requiring an annotated test set. Assuming the pseudo ground truth of all unannotated samples in the test set as abnormal/positive and using traditional AUC calculation, AUCp scores are derived. Given a large and representative training set of normal samples, we show mathematical and empirical evidence that model selection using AUCp scores improves disease detection in terms of unsupervised and self-supervised methods over conventional metrics. Using two unsupervised methods for neurologic disease detection and self-supervised methods on diverse datasets, our results demonstrate that the AUCp score effectively identifies the optimal model for inference, significantly enhancing abnormality and disease detection. The corresponding implementations are available in this https URL.

---


### 286. [MB-Loc: Multi-planar Bird's-eye-view Localization in outdoor LiDAR scenes](https://arxiv.org/abs/2606.08744)

**<font color=#1a73e8>作者：</font>** Ayaan Choudhury, Preet Savalia, Anirudh Pydah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Global LiDAR localization is a fundamental task for autonomous navigation systems. Recent methods perform Scene Coordinate Regression (SCR) and achieve superior accuracy over Absolute Pose Regression (APR) solutions by predicting dense 3D world coordinates. However, SCR approaches introduce two major bottlenecks: severe computational inefficiency from processing raw 3D geometries and significant performance degradation under varying sensor viewpoints. To address these limitations, we present MB-Loc, a lightweight and viewpoint-robust SCR framework. Instead of relying on heavy 3D convolutions, we project the input LiDAR scan into a 2.5D Multi-planar Bird's-Eye View (BEV) representation. By slicing the point-cloud along the Z-axis and mapping signed depths into discrete 2D planes, MB-Loc retains essential 3D geometric structures while exploiting the computational tractability of standard 2D CNNs. To handle the inherent sparsity of outdoor LiDAR, we introduce a KL-regularized latent bottleneck that explicitly models spatial uncertainty without injecting stochastic noise. Finally, to ensure rotation robustness, we apply 3D spatial augmentations prior to planar projection, forcing the network to implicitly learn viewpoint-invariant features. We perform extensive experiments on the publicly available NCLT dataset and demonstrate that our proposed method outperforms the current state-of-the-art. Operating at real-time inference speeds, MB-Loc significantly outperforms traditional 3D-SCR architectures in computational efficiency.

---


### 287. [Stain-Aware Wavelet Regularization for Instant Adversarial Purification in Histopathology](https://arxiv.org/abs/2606.08745)

**<font color=#1a73e8>作者：</font>** Zhe Li, Bernhard Kainz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning has become prevalent in computational pathology pipelines that support tasks such as cancer screening and digital pathology analysis. However, the susceptibility of neural networks to adversarial perturbations raises safety concerns for reliable deployment in clinical practice. In histopathological images, this challenge is exacerbated by the difficulty of distinguishing high-frequency adversarial noise from subtle and diagnostically relevant tissue structures. To address this issue, we propose Stain-Aware Wavelet Regularization (SAWR), an adversarial purification framework that leverages multi-level wavelet-domain regularization based on Haar transform to hierarchically disentangle adversarial perturbations from diagnostic structural information. This spectral constraint is further extended to individual histological channels, enabling stain-specific frequency regulation consistent with the biological properties of Hematoxylin and Eosin. When integrated into an instant purification framework, SAWR improves adversarial robustness by up to 10.69\% over the baseline approach, while maintaining texture and spectral fidelity under adversarial perturbations.

---


### 288. [HydraQE: OSU's Submission for the IWSLT 2026 Speech Translation Metrics Shared Task](https://arxiv.org/abs/2606.08748)

**<font color=#1a73e8>作者：</font>** Kevin Krahn, Eric Fosler-Lussier  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present HydraQE, our contribution to the IWSLT 2026 Speech Translation Metrics shared task. HydraQE is an end-to-end, reference-free quality estimation (QE) system for speech translation built on a Qwen3-ASR backbone, which accepts source audio and a translation hypothesis as joint input. Hidden states from all backbone layers are combined via a learnable sparsemax scalar mix, then re-encoded by a lightweight bidirectional Transformer to enable full cross-modal interaction prior to pooling into a shared embedding. Three independent prediction heads are trained on complementary supervision signals: human direct assessment (DA) annotations, MetricX-24 pseudo-labels, and xCOMET pseudo-labels. To address the scarcity of human-annotated data, we train on a combination of synthetically corrupted examples and silver pseudo-labeled machine translation outputs, using a curriculum that begins on synthetic and silver data and gradually shifts toward human-annotated examples. HydraQE outperforms cascaded text-based baselines and prior direct speech QE systems, demonstrating that end-to-end speech translation QE is competitive with cascaded approaches.

---


### 289. [Less Is More: Training-Free Acceleration Framework of 3D Diffusion Models for Low-Count PET Denoising via Global-Local Trajectory Reduction](https://arxiv.org/abs/2606.08751)

**<font color=#1a73e8>作者：</font>** Yuhan Liu, Scott M. Leonard, Marlee Crews 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate quantification and uptake measurement in PET are critical for assessing disease progression and supporting clinical decision-making. While high-count PET provides reliable image quality, the associated radiation dose and prolonged acquisition remain significant clinical concerns, motivating the adoption of low-count protocols. Diffusion-model-based methods have demonstrated strong potential for restoring low-count PET to near high-count quality, but their iterative sampling procedure becomes prohibitively expensive when applied to high-resolution 3D PET volumes, introducing substantial inference latency that limits practical clinical deployment. To address these challenges, we propose a training-free Global-Local Skipping Strategy that accelerates diffusion model-based 3D PET denoising while simultaneously improving reconstruction quality. The proposed method is plug-and-play and directly applicable to pre-trained diffusion models without retraining or architectural modification. Specifically, we introduce: (i) a global denoising step skipping strategy that initializes the reverse diffusion process from an intermediate denoising step using a noise-consistent transformation of the low-count input, substantially reducing the number of required denoising steps; and (ii) a local feature reuse shortcut that reuses slowly-varying high-level U-Net features across neighboring denoising steps, further reducing per-step computation while preserving image fidelity. We evaluate the proposed approach on multiple PET tracers from in-house and public datasets, including 18F-FDG PET, 68Ga-DOTATATE PET, and 18F-PSMA PET, demonstrating consistent acceleration of over an order of magnitude alongside improved or comparable reconstruction performance relative to the full-step baseline. Blinded reader studies further confirm enhanced clinical confidence and perceived diagnostic quality.

---


### 290. [Co-Evolving Skill Generation and Policy Optimization](https://arxiv.org/abs/2606.08755)

**<font color=#1a73e8>作者：</font>** Zhiwei Zhang, Yudi Lin, Nikki Lijing Kuang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Skill-augmented reinforcement learning improves language agents by storing reusable procedural knowledge acquired from past experience. Existing methods typically use strong language models to analyze trajectories, generate skills, and update a retrievable skill bank during online training. However, they rarely assess whether a newly generated skill is useful before it is stored and reused. We find that this assumption is unreliable: even skills generated by proprietary frontier LLMs exhibit highly mixed utility, with many providing little benefit or even degrading performance. Once such skills enter the bank, their effects are difficult to identify, because subsequent rollout feedback is delayed and usually reflects the combined effect of multiple retrieved skills rather than the marginal contribution of any individual skill. We propose an online reinforcement learning framework for pre-storage skill validation. The framework estimates whether a candidate skill contributes useful information beyond the skills already retrieved for the current task. It uses the standard rollout budget to form two matched groups under the same task and retrieval context: base rollouts conditioned on the currently retrieved skills, and skill-augmented rollouts conditioned on the same skills plus one candidate skill induced from the base trajectories. The reward gap between these two groups estimates the candidate skill's context-dependent marginal utility, enabling the framework to promote useful skills while filtering ineffective or harmful ones without additional rollout overhead. The framework further uses this marginal-utility signal to train the policy itself as a skill generator, reducing reliance on repeated calls to proprietary models. The learned skill-generation likelihood serves as a context-dependent score for retrieval-time reranking and outdated-skill pruning as the policy evolves.

---


### 291. [Understanding the Parameter Space Geometry of Transformers Encoding Boolean Functions](https://arxiv.org/abs/2606.08768)

**<font color=#1a73e8>作者：</font>** Blanka Köver, Alexandra Butoi, Anej Svete 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers consistently fail to learn certain simple functions that are provably expressible with specific parameter settings. This gap between learnability and expressivity is particularly prominent for sensitive functions -- functions whose output is likely to change if a single bit of the input is flipped -- for example, PARITY. While prior work has established that transformers exhibit a bias toward functions with low average sensitivity, the precise mechanism underlying this bias remains poorly understood. To shed light on this phenomenon, we study the geometry of transformers' parameter space. We show that sensitive functions -- even when representable -- occupy a vanishingly small region that random initialization is very likely to miss. Specifically, we shift the focus from average sensitivity to the full sensitivity profile -- the distribution of sensitivity values across all inputs -- and prove that randomly initialized transformers almost surely compute functions which have low-sensitivity strings. Consequently, any function that lacks such strings is provably unlearnable.

---


### 292. [TeamHerald@CHIPSAL 2026: Hate Speech Detection and Sentiment Analysis of Nepali Memes using Transformer-based Architectures and Ensemble Learning](https://arxiv.org/abs/2606.08770)

**<font color=#1a73e8>作者：</font>** Ashish Acharya, Anish Khatiwada, Rohit Khadka 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The analysis of internet memes in the Nepali language is complicated by frequent code-mixing and a lack of established baseline resources. While memes inherently combine visual and textual elements, this study focuses on a text-centric approach by extracting embedded text using an OCR layer and modeling it with Transformer-based architectures. We evaluate six distinct models and investigate the comparative effectiveness of Hard and Soft Voting ensemble strategies across two tasks: binary hate speech detection and three-class sentiment analysis. Experimental results show that a standalone decoder-only model achieved the highest performance for binary classification, whereas the Soft Voting ensemble performed best for the multi-class sentiment task, yielding a 15.8% relative improvement in Macro F1-score over the strongest standalone baseline. These findings suggest that ensemble strategies behave differently across binary and multi-class tasks, highlighting the importance of selecting aggregation methods suited to the classification objective.

---


### 293. [How Many Counterfactuals Does It Take? Probing VLM Hallucinations Through Circuits and Causal Effects](https://arxiv.org/abs/2606.08777)

**<font color=#1a73e8>作者：</font>** Abhivansh Gupta, Simardeep Singh, Advika Sinha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Visual Language Models (VLMs) are known to produce hallucinated predictions that are not grounded in visual evidence, yet existing approaches lack a principled understanding of how robust such predictions are under counterfactual perturbations. In this work, we study the sample complexity of counterfactual robustness for hallucinated outputs in VLMs. We define a causal influence metric based on log-probability differences between factual, counterfactual, and activation-patched runs, and use it to characterize the stability of hallucinated predictions. By leveraging circuit discovery techniques (CD-T), we identify model components responsible for these predictions and track their activation differences across counterfactual samples. We then derive empirical bounds on the minimum number of counterfactual samples m required to reliably detect instability in hallucinated outputs, using concentration inequalities and variance estimates of the causal influence distribution.

---


### 294. [Beyond Consistency: Preserving Temporal Structure in Zero-Shot Video Editing](https://arxiv.org/abs/2606.08780)

**<font color=#1a73e8>作者：</font>** Deyin Liu, Yisheng Ding, Zhe Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing zero-shot video editing methods rely on pre-trained diffusion models, successfully achieving spatial control and basic temporal consistency but fundamentally fail to preserve the video's original temporal this http URL distinction is critical: temporal consistency ensures visual smoothness, but temporal structure dictates the video's high-level narrative, rhythm, and semantic flow. Without this preservation, the edited output, especially for long videos with complex semantic variations, becomes narratively incoherent and semantically ambiguous. To address this limitation, we introduce a novel zero-shot editing approach that, for the first time, explicitly focuses on preserving the source video's temporal structure. We achieve this by adaptively partitioning the video into semantically distinct clips based on feature similarity and selecting a representative anchor frame for each clip. To enhance both intra-clip fidelity and computational efficiency, we design a clip-adaptive token merging strategy which leverages the anchor's semantic dominance to stabilize the editing. Furthermore, we employ an alternating combination strategy that ensures seamless inter-clip transitions while maintaining semantic distinction. Extensive experiments demonstrate that our method achieves state-of-the-art results, successfully balancing the preservation of original temporal structure with computational efficiency, and setting a new benchmark for zero-shot video editing fidelity.

---


### 295. [DeepMine-Mamba: Mitigating Information Dilution in Mamba-Based State Space Models for Document Image Binarization](https://arxiv.org/abs/2606.08781)

**<font color=#1a73e8>作者：</font>** Sheng-Wei Chan, Yung-Che Wang, Hsin-Jui Pan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Document image binarization aims to separate foreground text from degraded backgrounds while preserving thin, broken, and low-contrast strokes. Although deep learning methods have improved binarization performance, most existing approaches rely on convolutional, transformer-based, or generative architectures, while Mamba-based state space models remain largely unexplored for this task. In this work, we investigate Mamba-based feature propagation and observe that direct state-space propagation may dilute weak foreground cues during long-range modeling, especially faint ink traces, fragmented characters, and boundary-sensitive stroke details. To address this problem, we propose DeepMine-Mamba, a Mamba-based binarization framework equipped with a novel Anti-Dilution Gate that estimates propagation-induced feature changes and selectively restores stroke-sensitive local responses while suppressing unnecessary background enhancement. Experiments on DIBCO/H-DIBCO benchmarks under a strict leave-one-year-out protocol show that DeepMine-Mamba achieves competitive overall performance, with strong average FM and Fps across benchmark years. Ablation results further demonstrate that the Anti-Dilution Gate improves stroke preservation and reduces perceptually significant binarization errors.

---


### 296. [PairWise Image Finder: An Open-source Tool for Finding Visually Aligned Street-Level Image Pairs for Urban Perception Studies](https://arxiv.org/abs/2606.08795)

**<font color=#1a73e8>作者：</font>** Jussi Torkko  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Change detection and scene recognition techniques have been widely applied to Street View Imagery (SVI) to understand changes in scenes across the years. However, metadata alone is often insufficient to reliably find visually aligned image pairs. This study introduces the PairWise image finder, a tool that integrates feature detection and matching, supported by semantic segmentation masks to quantify the visual alignment of two images of varying time periods. The tool outputs the share of matched key features, the matched feature distance and coverage, and the alignment of semantic masks, which enables the user to filter image pairs depending on the alignment quality and use case. The visually aligned pairs derived from the tool can be used to accurately study explicit longitudinal change and help reduce manual effort for perception studies. The usability of the tool is demonstrated through a comparison of longitudinal changes, highlighting the importance of perspective when quantifying changes. The proposed method provides a scalable and open tool for researchers and stakeholders to find high-quality image pairs for urban analysis, perception and related applications.

---


### 297. [Scaling Decision-Focused Learning to Large Problems with Lagrangian Decomposition](https://arxiv.org/abs/2606.08797)

**<font color=#1a73e8>作者：</font>** Stéphane Eilles-Chan Way, Hugo Percot, Quentin Cappart 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision-focused learning has shown great promise for addressing predict-then-optimize problems, particularly in the presence of under-specified models. However, its practical deployment is often hindered by high computational costs and limited scalability, as it requires solving a constrained optimization problem for each training instance at every iteration. To address these challenges, we propose a novel framework that incorporates Lagrangian decomposition into the decision-focused learning paradigm. Specifically, we introduce a new surrogate objective along with two loss functions for evaluating and training the underlying prediction model. We further propose two variants of our approach, which offer different trade-offs between computational efficiency and solution quality. Our framework can be seamlessly integrated with standard decision-focused learning methods, including Smart Predict-then-Optimize (SPO+) and Implicit Maximum Likelihood Estimation (IMLE). Through experiments on two standard benchmarks, the multi-dimensional knapsack problem and quadratic portfolio optimization, we demonstrate that our approach achieves competitive performance while remaining amenable to parallelization. In particular, it consistently outperforms traditional decision-focused learning methods on large-scale instances, involving up to eight times more variables than those typically considered in related work. The implementation is available at this https URL.

---


### 298. [Bridging Expert Knowledge and Automated Feature Engineering via Self-Evolution](https://arxiv.org/abs/2606.08800)

**<font color=#1a73e8>作者：</font>** Varun Khurana, Vijval Ekbote, Vashu Chauhan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In high-stakes settings such as brand compliance, clinical care, and content moderation, machine learning cannot be deployed as opaque oracles: practitioners inspect the features driving model decisions, and models must leverage the expert documentation governing these domains. In practice, the data arrives as unstructured content, and features extracted from it must be interpretable, discriminative, and aligned with what experts consider important. Existing methods fall short: they target tabular inputs, lack demonstrated expert alignment, and cannot operationalize qualitative criteria such as 'maintain professional tone' into precise features. We present FEST (Feature Engineering with Self-evolving Trees), combining dual-stream feature generation (semantic and deterministic), semantic deduplication, and tree-guided iterative evolution to discover auditable features from raw text and images. FEST leads in 17 of 20 classifier-task combinations across brand classification, content authenticity detection, and stress detection, with a mean gain of 4.2 pp over the strongest baseline across five classifiers. An LLM-as-judge evaluation shows FEST achieves 60-80% coverage of expert-designed brand features at strict semantic-alignment thresholds, corroborated by a human expert study rating features highly on relevance, clarity, and actionability. When seeded with expert guidelines, FEST refines qualitative criteria into operational features, improving accuracy by 6-12 pp on average across brands. To enable systematic evaluation of expert alignment in automated feature engineering, we release BrandGuide, the first dataset pairing expert-designed features with 1M+ assets across 2,683 brands. By grounding feature engineering in expert knowledge, FEST opens a practical pathway for interpretable ML in domains demanding human oversight.

---


### 299. [Active Flow Expansion for Out-of-Distribution Discovery: from Theory to Molecules](https://arxiv.org/abs/2606.08802)

**<font color=#1a73e8>作者：</font>** Riccardo De Santi, Bruce Lee, Cristian Perez Jensen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard flow and diffusion pre-training matches the distribution of available data (e.g., molecules), which often covers only a small fraction of the valid design space. In generative discovery, however, one aims to sample valid new-to-nature designs, assigned negligible probability under, and thus inaccessible to, standard models fitted to the observed data. To overcome this limitation, we depart from data distribution matching and view a generative model through its generable set: the region it covers with non-negligible probability. This allows to introduce a new learning principle for out-of-distribution flow modeling: enlarging a model's generable set to increase coverage of the valid design space. We propose Active Flow Expansion (ActFlow), a continued pre-training method that employs verifier feedback to expand a pre-trained model over new valid regions by iteratively adapting to synthetic data generated through active exploration in the learned flow representation. Theoretically, we establish to our knowledge first-of-their-kind statistical learning guarantees for out-of-distribution flow modeling, analyzing generable set expansion as a local-to-global reachability process over a learned representation. Empirically, we assess ActFlow with suitable out-of-distribution generative modeling metrics across small organic molecules, mid-sized drug-like molecules, therapeutic peptides, and protein sequence design tasks. Results show that ActFlow expands valid coverage far beyond the region modeled by the initial pre-trained model, significantly outperforming widely adopted synthetic flow pre-training methods.

---


### 300. [Q-Delta: Beyond Key-Value Associative State Evolution](https://arxiv.org/abs/2606.08804)

**<font color=#1a73e8>作者：</font>** Sumin Park, Seojin Kim, Noseong Park  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Linear attention reformulates sequence modeling as recurrent state evolution, enabling efficient linear-time inference. Under the key-value associative paradigm, existing approaches restrict the role of the query to the readout operation, decoupling it from state evolution. We show that query-conditioned state readout induces a structured value prediction over accumulated memory that complements key-based retrieval. Based on this insight, we propose Q-Delta, a query-aware delta rule that integrates mixed key-query prediction errors into state evolution, enabling jointly corrective dynamics while preserving delta-rule efficiency. We establish stability guarantees for the resulting dynamics and derive a hardware-efficient chunkwise-parallel formulation with a custom Triton implementation. Empirical results demonstrate stable optimization, competitive throughput, and consistent improvements over strong baselines on language modeling and long-context retrieval tasks.

---


> [!TIP]
> 当前位于：**251-300**（第 6/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-527](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
