# 🧠 大模型相关研究 | 2026年07月08日

> 本类共 **248** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-248](./part-05.md)

---

### 1. [iFLYTEK-Embodied-Omni Technical Report](https://arxiv.org/abs/2607.02542)

**<font color=#1a73e8>作者：</font>** Yuan Zhang, Jingfei Ni, Guanchen Lu 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> General-purpose embodied agents must understand multimodal instructions, anticipate how their environment will evolve, and produce precise control actions over extended horizons. Existing approaches typically specialize in visual-language reasoning, video-based world modeling, or action generation, while cascaded pipelines that first synthesize future observations and then infer actions can introduce interface bottlenecks and compound prediction errors. We present iFLYTEK-Embodied-Omni, a unified multimodal foundation model that jointly models vision(videos and images), language, and action within a single Omni framework. Its modality-specific visual-language, video-generation, and action-generation components communicate through shared multimodal self-attention. This design establishes brain-cerebellum collaboration: the vision-language modeland video generation model form a high-level brain for instruction understanding, task planning, progress tracking, and future visual-state prediction, whereas the action generation modelserves as a low-level cerebellum that directly converts planned subgoals and shared multimodal context into executable action chunks. To develop these capabilities, we combine action-annotated and action-free embodied videos from human demonstrations and robot interactions with embodied reasoning, embodied perception, and general-purpose image-text data to construct a comprehensive dataset. We further adopt a four-stage strategy that progressively trains the VLM, VGM, and AGM before jointly fine-tuning the complete model.

---


### 2. [DELTAVID: Enhancing Fine-Grained Spatiotemporal Perception with Cross-Video Differences](https://arxiv.org/abs/2607.02551)

**<font color=#1a73e8>作者：</font>** Yankai Yang, Yancheng Long, Bin Wen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video multimodal large language models have made strong progress on open-ended video understanding, but they still lack precise local spatiotemporal perception. When two videos share almost the same global semantics and differ only in a short time span or a small region, current models often fail to find the change and provide reliable evidence. We propose DELTAVID, a verifiable proxy-task framework that enhances fine-grained spatiotemporal perception with cross-video differences. The key idea is to turn cross-video spot-the-difference into a trainable perception signal, where a model identifies local changes, judges temporal boundaries, and organizes spatial evidence by comparing similar videos. To make this signal scalable to train and reliable to evaluate, we further introduce DELTAVID-10K and DELTAVID-Bench, which convert controllable local differences in real videos into evidence-labeled training and test samples. Experiments show that DELTAVID substantially improves performance on cross-video difference understanding and transfers the learned local evidence ability to general video understanding benchmarks, including MMVU, MLVU, Video-MME, VideoHolmes, VideoMMMU, LVBench, TempCompass, and LongVideoBench. These results show that cross-video differences are not only an effective way to diagnose fine-grained perception failures, but also a scalable proxy supervision that moves Video MLLMs from coarse semantic understanding toward fine-grained spatiotemporal evidence reasoning.

---


### 3. [Coordinate Singularities Break Conformal Coverage for Gaze and Head Pose](https://arxiv.org/abs/2607.02565)

**<font color=#1a73e8>作者：</font>** Mohammadreza Jamalifard, Yaxiong Lei, Parastoo Azizinezhad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conformal prediction provides distribution-free reliability guarantees for vision systems, but these guarantees depend on how prediction errors are measured in the output space. Many vision tasks produce outputs on curved spaces (e.g. gaze directions on the sphere or 3D head rotations), yet intermediate prediction heads, residuals, uncertainty estimates, or conformal scores are often defined in flat coordinate charts such as yaw-pitch or Euler angles. We show that this scoring choice introduces systematic geometric distortion near coordinate singularities (large pitch angles on the sphere and poses approaching gimbal lock in 3D rotations). Across four datasets (ETH-XGaze, Gaze360, BIWI, AFLW2000-3D), slice-conditional coverage at a nominal 90% target drops by 30-50 percentage points in these regions, falling to 38.9% on ETH-XGaze and 42.0% on Gaze360 at gaze pitch above 70 degrees, and to 57.5% on BIWI and 55.2% on AFLW2000-3D at head pose pitch above 60 degrees near gimbal lock, despite marginal coverage remaining near 90%. We prove that this is structural. Scalar thresholding changes the size of chart-coordinate prediction sets but leaves their distorted axis ratios unchanged. To diagnose this hidden failure mode, we show that a simple geometric quantity, the Riemannian volume density, strongly correlates with where coverage collapse occurs. Finally, we show that coordinate-free geodesic scoring removes this distortion. It requires no retraining and adds negligible computational cost.

---


### 4. [MAGE: View-guided Point Cloud Completion with Efficient Modality Alignment and Adaptive Geometry Enhancement](https://arxiv.org/abs/2607.02568)

**<font color=#1a73e8>作者：</font>** Weize Quan, Zhengwei Wu, Kai Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> View-based point cloud completion aims to recover a complete 3D shape from a partial point cloud, guided by a single-view image. However, existing approaches often suffer from limited performance due to weak modality alignment and limited self-geometry enhancement. To overcome these challenges, we propose a unified geometry-aware framework that integrates efficient modality alignment and adaptive geometry enhancement, mainly to address cross-modal geometric inconsistency of view-guided point cloud completion. Specifically, we propose a geometry-aware modality alignment by integrating a shared self-attention Transformer and cross-modality reconstruction supervision, which aims to bring features of the image and point cloud close to each other in a shared latent space describing the 3D object. To enhance the perception of global shape and local geometric details, we propose an adaptive geometry-aware self-attention module, which simultaneously considers local geometry-aware attention computation and the spatially-variant feature fusion. In addition, we apply a geometry-perceptive anchor refinement module to reorganize the anchor points (representing a local region of the shape) under appropriate supervision, further boosting the completion performance of our method. Extensive experiments on both synthetic and real-world datasets demonstrate that our method achieves superior performance over existing approaches. Our code will be available at this https URL.

---


### 5. [Dual-Adaptive SAM3: Hierarchical Routing over Low-Rank Expert Layers for Parameter-Efficient Medical Image Segmentation](https://arxiv.org/abs/2607.02571)

**<font color=#1a73e8>作者：</font>** Ying Chen, Jinyue Li, Kun Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The Segment Anything Model with Concepts (SAM3) heralds a new paradigm for open-vocabulary segmentation through natural language interaction, offering significant potential for medical image analysis. However, effectively adapting such a powerful vision-language model to the diverse and nuanced domain of medical imaging remains a key challenge. Naive fine-tuning is parameter-inefficient, while standard Mixture-of-Experts (MoE) methods introduce prohibitive computational overhead, limiting their clinical applicability. To address this, we propose Dual-Adaptive SAM3 (DA-SAM3), a novel framework that achieves both high segmentation accuracy and extreme parameter efficiency via a dual-adaptive specialization mechanism. Our first adaptation is task-aware: a Dynamic Expert Router (DER) that sparsely activates the most relevant experts by jointly reasoning about the visual input and the textual concept prompt, mimicking a clinical consultation process. Our second adaptation is parameter-aware: a Decomposed Parameterized Experts (DPE) design that represents each expert as a shared frozen base (inherited from the pretrained SAM3) and a lightweight trainable low-rank delta, reducing MoE parameter overhead by over 80\%. Extensive experiments on multiple public medical segmentation benchmarks demonstrate that Dual-Adaptive SAM3 not only matches or exceeds the accuracy of fully fine-tuned SAM3 and standard MoE baselines, but also achieves a notable 5\% gain over current state-of-the-art methods, with interpretable results validating its effectiveness. The code is available at: this https URL.

---


### 6. [Criterion-Conditional In-Context Learning: Evaluating Criterion-Shift Adaptation in Vision-Language Models](https://arxiv.org/abs/2607.02575)

**<font color=#1a73e8>作者：</font>** Kaiyun Yang, Ruilin Yang, Zhimin Yao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models can perform new tasks without parameter updates through in-context learning (ICL), whose core mechanism is utilizing the support set for task induction. In the standard ICL setting, once the task is induced, its decision criterion remains fixed. However, in real-world applications, many tasks exhibit a stable high-level intent, while their decision criteria shift according to specific requirements. Thus, we introduce a new setting, denoted as Criterion-Conditional In-Context Learning (CC-ICL), where models must infer the latent criterion from context and adjust predictions accordingly under fixed task semantics. To evaluate this capability, we propose two complementary metrics, Criterion Invariance and Criterion Sensitivity, capturing the model's robustness and adaptability under criterion shifts. We further construct CC-Bench, a multi-domain benchmark that supports evaluation under the CC-ICL setting. By employing a dual-level data hierarchy, CC-Bench enables legitimate ground-truth variation conditioned on the active criterion even when the task remains fixed. Experiments on CC-Bench reveal that most models exhibit a rigid boundary bias, struggling to align their decisions with the latent criterion. We also find that even a simple multi-criterion training strategy can significantly reduce this bias, improving Criterion Sensitivity and enabling 7B-scale models to surpass proprietary models without degrading general multimodal performance.

---


### 7. [Homer: Understanding Long-form Videos with Hierarchical Memory and Agentic Reasoning](https://arxiv.org/abs/2607.02588)

**<font color=#1a73e8>作者：</font>** Yixin Ji, Fanghua Ye, Juntao Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models excel on short clips but struggle on hour-long videos in an online setting, where frames are processed incrementally under limited memory. Existing online methods either retain compact visual representations that lack semantic structure, or build higher-level memory stores organized around temporal proximity rather than explicit causal links, leaving multi-hop narrative reasoning to be reconstructed by the LLM at every query. We bridge this gap with \textsc{Homer}, a Hierarchical Online Memory Exploration and Reasoning framework. \textsc{Homer}'s memory mirrors the multi-scale structure of long videos, ranging from raw perception, to recurring entities, to events connected by explicit temporal and causal relations. Its agentic reasoner then explores this memory the way humans do, locating the relevant scene, looking up details, and composing the answer through multi-round memory retrieval, with a harness that verifies and corrects each step. \textsc{Homer} outperforms the previous best agent method by $+5.5$, $+10.8$, and $+4.4$ points on M3-Bench-robot, M3-Bench-web, and Video-MME-Long, and consistently lifts three various LLM backbones, indicating a model-agnostic structural capability for grounded retrieval over long videos.

---


### 8. [H-OPD: Confidence Aware Heterogeneous Multi-Teacher Multimodal On-policy Distillation](https://arxiv.org/abs/2607.02592)

**<font color=#1a73e8>作者：</font>** Qixiang Yin, Huanjin Yao, Yuchen Cai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) has recently emerged as an effective post-training paradigm by providing supervision on student-generated trajectories. However, existing OPD methods for multimodal reasoning usually rely on a static teacher routing, assigning each sample to a single teacher based on modality or task type. This ignores that visual grounding and abstract reasoning may dominate different decoding steps, making a single teacher insufficient for the full trajectory. To this end, H-OPD is proposed as a confidence-aware heterogeneous multi-teacher OPD framework for multimodal reasoning. By verifying the complementarity of heterogeneous teachers in the same reasoning process, H-OPD replaces task or sample level teacher routing with token-level teacher arbitration along the shared student trajectory. H-OPD employs vision-to-language description transfer to enable text-only teachers to access key visual semantics, and uses a confidence-aware arbitration mechanism to dynamically combine vision-language teacher and text-only teachers at each token. Extensive evaluations over 11 widely-used reasoning benchmarks showcase the superior performance of our method.

---


### 9. [Token-level Response-visual Attention Guidance for Multimodal LLMs Knowledge Distillation](https://arxiv.org/abs/2607.02593)

**<font color=#1a73e8>作者：</font>** Jaehyun Jang, Eunseop Yoon, Hee Suk Yoon 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While knowledge distillation (KD) is widely adopted for training lightweight models by leveraging supervision from larger teacher models, relying solely on output token distributions has proven insufficient for compressing Multimodal Large Language Models (MLLMs). Since output tokens are a byproduct of the model attending to visual inputs, prior works have explored explicitly distilling attention to provide a direct supervisory signal. While promising, the precise utility of which attention signals to distill remains under-explored. In this work, we challenge the conventional reliance on prompt-to-vision attention by revealing that downstream performance correlates strongly with response-to-vision attention similarity to the teacher, but negligibly with that of prompt-conditioned attention. Furthermore, we observe that attention distributions exhibit significant variance across individual tokens, indicating that a uniform distillation objective is suboptimal. To this end, we introduce Token-level Response-visual Attention Guidance (TRAG), a distillation objective that 1) shifts the focus to response-to-vision signals and 2) employs token-specific objectives by adaptively weighting the Kullback-Leibler divergence based on attention entropy, effectively guiding the student to mirror the teacher's precise visual focus. Extensive experimental results on multiple benchmarks demonstrate that TRAG significantly outperforms prior distillation baselines.

---


### 10. [Evaluating Agentic Harness Systems for Autonomous Computational Pathology](https://arxiv.org/abs/2607.02598)

**<font color=#1a73e8>作者：</font>** Jie Lin, Zongyi Chen, Qiaoling Zheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous computational pathology (ACP) converts high-level pathology analysis goals into executable, traceable and clinically bounded workflows. Realizing this capability requires adapting general agentic harness systems to pathology-specific tasks, tools, evidence standards and clinical claim boundaries. We contribute ACP-Bench, a framework that adapts existing harness systems from computational pathology support toward ACP workflow capability. ACP-Bench evaluates 41 pathology workflow tasks, including 24 biomarker, 7 morphology and 10 prognosis tasks spanning 6 body-system groups and 9 endpoint families. The benchmark evaluates 9 models and 3 harness groups (Claude Code, Codex and Open Code), yielding 369 complete trajectories. ACP-Bench evaluates each trajectory across workflow execution, diagnostic performance and clinical-boundary alignment, combining expert-adjudicated process audits, diagnostic assessment and pathologist-validated safety review. Across evaluated systems, workflow initiation, task interpretation and diagnostic reporting were more mature than tool-bound execution, result binding and reflective workflow revision, and formal end-to-end completion remained rare. ACP-Bench provides a reusable standard for auditing whether agentic systems can operationalize pathology workflows before claims of reliable clinical autonomy.

---


### 11. [DynaWM: A Base-VLA-Guided World Foundation Model for Moving-Object Manipulation](https://arxiv.org/abs/2607.02604)

**<font color=#1a73e8>作者：</font>** Chongkei Chang, Zhidong Deng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although vision-language-action (VLA) models have received widespread attention, many challenges remain in manipulating dynamic moving objects. In most existing approaches, end-to-end forward or inverse dynamics models, i.e., world models, are incorporated into high-performance base VLA architectures, which may degrade the performance of well-pretrained base VLA models due to inappropriate fine-tuning. In this paper, we propose DynaWM, a base-VLA-guided world foundation model that adapts to a wide variety of fine-tuned and coarse-tuned base-VLA checkpoints for moving-object manipulation. DynaWM uses a Mamba-3-based action encoder to encode the base action chunk produced by the base VLA into an action-conditioning representation, a V-JEPA 2.1 vision encoder to extract features from multi-view observation history, and a proprioceptive state encoder to encode robotic-arm proprioceptive states. These feature representations jointly condition a flow-matching DiT to regenerate motion-aware action trajectories for moving-object manipulation. For systematic evaluation, we construct the DynaGrasp-32 benchmark, covering six categories of moving-object manipulation tasks, including velocity variation, trajectory variation, and multi-object manipulation, as well as the DynaGrasp-1600 dataset, which consists of 32 scenarios, 1,600 demonstration trajectories, and approximately 1.53M images. For fine-tuned base-VLA checkpoints, DynaWM achieves percentage improvements of 7.19, 45.31, 1.88, and 10.94 over SmolVLA, X-VLA, {\pi}0, and {\pi}0.5, respectively. For coarse-tuned base-VLA checkpoints, performance increases by 35.13, 44.06, 35.69, and 26.13 percentage, respectively. Ablation experiments show that visual encoding enhances success by 27.50%, while reducing success by 45.44% if action conditioning is removed.

---


### 12. [Latent Visual Cache for Video Reasoning](https://arxiv.org/abs/2607.02607)

**<font color=#1a73e8>作者：</font>** Yongheng Zhang, Zhipeng Xu, Hao Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video reasoning requires Large Multimodal Models (LMMs) to remain grounded in dense evidence, yet existing systems largely adopt "read-once, generate-many" paradigm, in which visual grounding weakens during generation. This phenomenon has been widely observed and is known as Visual Anchoring Decay. To fill this gap, we introduce Latent Video Cache (Latent-VC), a recurrent latent visual cache inserted into the decoder to preserve compact visual memories throughout reasoning. The cache is trained with supervised contrastive cache alignment and vision-grounded GRPO with a latent grounding reward, while maintaining strict train-inference alignment through native decoder hidden states. Built on Qwen3.5-9B, Latent-VC consistently outperforms strong CoT and SFT+GRPO baselines across six video benchmarks, with especially clear gains on grounding-intensive and long-video tasks. In addition, it also achieves higher accuracy with substantially shorter responses, suggesting that latent visual caching improves video reasoning by preserving visual evidence rather than relying on longer textual chains.

---


### 13. [Evaluating Time Series Foundation Models for Electricity Price Forecasting: Contamination Risk, Distributional Shifts, and Covariate Dependence](https://arxiv.org/abs/2607.02623)

**<font color=#1a73e8>作者：</font>** Zhenghua Pan, Ahmed Aziz Ezzat  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series foundation models (TSFMs) have shown strong zero-shot forecasting performance, but their generalization in covariate-driven, non-stationary settings is underexplored. Electricity price forecasting (EPF) presents a challenging testbed due to complex temporal dependencies, distributional shifts, and strong reliance on structural and contextual information. We propose a two-dataset-benchmarking framework for EPF to mitigate contamination risk and enable fair evaluation of TSFMs. We examine key aspects of EPF including point and probabilistic forecasting performance, tail behavior, price spikes, and comparisons against domain-specific methods. We find that TSFMs are highly competitive and often outperform general-purpose baselines. Yet, their performance depends critically on covariate support, and they do not consistently surpass domain-specific methods tailored to EPF. Interestingly, simple ensembles of TSFMs and domain-specific methods appear to have significant potential, suggesting that the two approaches capture complementary predictive information.

---


### 14. [QuantFlow: A Federated Mamba-Based Post-Transformer Foundation Model for Time-Series Forecasting](https://arxiv.org/abs/2607.02632)

**<font color=#1a73e8>作者：</font>** Shah Nawaz Haider, Steve Austin, Arnab Barua 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series forecasting supports decisions in finance, en-ergy, transportation, public health, and industrial monitoring. Recent foundation models improve transfer across forecast-ing tasks, but many depend on centralized data and Trans-former attention, which restricts their use for long, high-di-mensional, and privacy-sensitive signals. This paper presents QuantFlow, a probabilistic forecasting framework that com-bines inverted sequence embedding, bidirectional Mamba state-space decoders, quantile regression, and federated learning. Each variable is embedded over the complete ob-servation window, processed in forward and reverse direc-tions, and projected to five conditional quantiles. TSMixup expands temporal diversity through Dirichlet-weighted inter-polation while preserving sequence structure. Experiments cover cryptocurrency, traffic, electricity, Electricity Trans-former Temperature, influenza, and weather data. QuantFlow obtains mean squared errors of 0.2834 on ETTm1 and 0.2218 on Weather, and a 20-client non-IID deployment retains use-ful accuracy after three communication rounds without cen-tralizing raw records. The results indicate that selective state-space modelling is a promising basis for scalable, uncer-tainty-aware, and privacy-conscious time-series prediction, while also revealing limitations on irregular epidemiological signals and long-horizon generalization.

---


### 15. [Improving LLMs via Validator-to-Generator Alignment](https://arxiv.org/abs/2607.02668)

**<font color=#1a73e8>作者：</font>** Juan Diego Rodriguez, Jocelyn Zhang, Katrin Erk 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are inconsistent: varying prompts or including unrelated information can lead to unexpected changes in model outputs. The generator-validator (G-V) gap is one manifestation of this phenomenon, where LLMs generate responses that they then deem as invalid if re-queried to validate them. In this work, we introduce a new formulation of G-V consistency that involves a principled correction for utterance frequency. Specifically, generators often assign low likelihood to valid strings simply because those strings are a priori unlikely, which makes naive notions of G-V consistency unworkable. We show that under a natural model of rational agents answering questions with multiple answers, consistency of the validator with a frequency-corrected generator score emerges naturally. Our method, \emph{\FCPAname} (\FCPA), is a training objective implementing frequency-corrected G-V consistency for real-world LLMs. Our experimental results show that training with \FCPA{} substantially improves both G-V consistency and generator performance over prior methods, with gains of up to $+27$pp in Pearson correlation on IFEval and HumanEval, while preserving validator quality across all evaluated tasks.

---


### 16. [EmoteGPT: 3D Human Facial Expressions from Natural Language Descriptions](https://arxiv.org/abs/2607.02674)

**<font color=#1a73e8>作者：</font>** Haoran Wang, Mohit Mendiratta, Christian Theobalt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Precise control of 3D facial expressions from text is crucial for virtual avatars, animation, and human-computer interaction, yet existing text-to-3D methods jointly generate identity, expression, and texture, making fine-grained expression control difficult. We instead formulate text-driven expression synthesis as a regression problem in the disentangled parameter space of a 3D Morphable Model (3DMM). This setting, however, requires paired data linking detailed language to precise expression parameters, which are missing from existing resources. To fill this gap, we introduce Txt2Emote, a benchmark of diverse 3D facial expressions with fine-grained textual annotations obtained from GPT-4o and a high-fidelity face tracker, providing both explicit descriptions detailing facial features and implicit descriptions referencing the situational context behind the expression. Leveraging this dataset, we present EmoteGPT, a text-to-3D expression framework based on a Multimodal Large Language Model (MLLM) with a dedicated <Expr> token to semantically ground expression representations, which are then decoded into 3DMM parameters. We further improve EmoteGPT by augmenting training with large-scale image-to-3DMM data, enabling it to surpass state-of-the-art text-to-3D face synthesis methods on emotion recognition metrics and in perceived expressiveness. Integrated into avatar pipelines, our method enables photorealistic and stylized 3D avatars, as well as expressive 3D-consistent 2D face synthesis from textual input.

---


### 17. [K9-Bench: Evaluating Multimodal LLMs on Canine-Centric Videos](https://arxiv.org/abs/2607.02680)

**<font color=#1a73e8>作者：</font>** Khush Attarde, Yusuf Ali, Megha Thukral 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> MLLMs have shown strong zero-shot capabilities across diverse inputs such as across images, video, audio, and text. A crucial, yet underexplored, application of these models lies in understanding and modeling animal-centric scenarios. As animals are integral to millions of households, benchmarking next-generation AI models on pet-focused tasks, ranging from recognizing distress signals to enabling responsive robotic companions, is essential for building AI systems that can work alongside us. We introduce K9-Bench, a novel benchmark focused on real-world domestic dog videos, specifically targeting canine action and interaction understanding via approximately 5000 question-answer pairs across 907 videos spanning 5 distinct task categories that test long-form, canine-centric multimodal reasoning in MLLMs. To create this dataset, we propose a scalable, VLM/LLM-powered data generation pipeline that automatically mines canine-centric videos from the web and curates QA pairs requiring fine-grained, multi-hop reasoning over canine actions and temporally extended interaction sequences. We implement bias mitigation strategies designed to eliminate biases introduced by VLMs during dataset curation. Through extensive experimentation, we find that frontier MLLMs exhibit limited zero-shot performance on canine-centric tasks: although state-of-the-art closed-source models outperform open-source counterparts, they still struggle with compositional reasoning over subtle posture and interaction cues spread over long horizons. We observe that generic chain-of-thought prompting provides only modest performance for such long-horizon reasoning. Beyond a novel dataset for canine activity analysis, K9-Bench provides a general-purpose dataset construction pipeline that can be adapted to other low-data domains for quantitative analysis. Our project website is available at: this https URL.

---


### 18. [ASK in the Dark: Uncertainty-Gated LLM Assistance under Partial Observability](https://arxiv.org/abs/2607.02686)

**<font color=#1a73e8>作者：</font>** Juarez Monteiro, Nathan Gavenski, Guilherme Lima 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning agents operating under partial observability must act on incomplete information, making them natural candidates for guidance from small language models (SLMs) that carry broad reasoning priors. Yet integrating SLM guidance into this setting has proven difficult: across all test environments, vanilla uncertainty-gated approaches achieve an overwrite rate at or near zero, meaning the SLM almost never contributes an independent action. We trace this failure to the bare egocentric prompt, which provides insufficient context for genuine reasoning, and identify it as a context problem rather than a capacity problem. We propose ASK+, which supplies the SLM with trajectory-aware context (a partially revealed map, visited positions, and action history) and structured chain-of-thought reasoning, converting it from a passive redundancy check into a more informative consultant that occasionally corrects the policy. We further establish that the predictive entropy signal used for selective querying measures action uncertainty rather than state uncertainty and remains informative in POMDPs, making uncertainty-gated assistance viable beyond fully observable settings. The stateful prompt drives substantial gains: on DoorKey, where vanilla ASK matches PPO (both 89%), ASK+ reaches 93% success; on FourRooms, success climbs from 53% to 70%; on HigherLower, accuracy reaches 73.7%, matching the SLM-only upper bound. Across all environments, Qwen3.5-2B matches or exceeds Qwen3.5-4B, confirming that prompt design and selective gating dominate the impact of model scale, enabling guidance without large models.

---


### 19. [An Automated Multimodal Glaucoma Detection Framework Using ViT and a Stacking-Based Ensemble](https://arxiv.org/abs/2607.02692)

**<font color=#1a73e8>作者：</font>** Ishrat Jahan, Muhammad E.H Chowdhury, Murugappan Murugappan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Glaucoma is a progressive eye disease that can lead to irreversible vision loss if not detected at an early stage. Conventional diagnostic procedures are often time-consuming and rely heavily on expert interpretation, limiting their scalability for large-scale screening. In this study, glaucoma detection is investigated under two evaluation settings: sample-wise, where individual samples are analyzed independently, and patient-wise, where data from each patient are aggregated for final prediction. An automated multimodal framework is proposed that integrates fundus images with clinical data. Under the sample-wise setting, detection is performed using fundus images and clinical features individually, as well as through their multimodal combination. Under the patient-wise setting, predictions are obtained by aggregating multiple fundus image representations with corresponding clinical information for each patient. Deep visual features are extracted using a Vision Transformer (ViT) architecture and classified using classical machine-learning models, with a stacking-based ensemble of the three best-performing classifiers employed to optimize performance. Experiments conducted on the publicly available PAPILA dataset demonstrate strong diagnostic performance, achieving 97.47% accuracy and a 97.50% F1-score for sample-wise multimodal classification, and 98.97% accuracy and F1-score for subject-wise detection. The proposed framework is further deployed as an end-to-end web-based platform to support automated glaucoma screening and clinical decision support.

---


### 20. [RayTun3R: Online Camera Adaptation in 3D Foundation Models](https://arxiv.org/abs/2607.02711)

**<font color=#1a73e8>作者：</font>** Daniil Sinitsyn, Nikita Araslanov, Daniel Cremers  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent 3D foundation models, such as DUSt3R, MASt3R, VGGT, $\pi^3$, and Depth Anything 3, provide strong feed-forward depth and pose estimates on pinhole imagery, but degrade sharply under fisheye camera geometry. We show that this failure is partly caused by a pinhole camera bias in the positional encodings of pretrained 3D foundation models, and propose RayTun3R, a lightweight camera adaptation approach. It keeps the pretrained network fixed and adapts only lightweight components tied to token position and camera geometry. RayTun3R learns parameter-efficient residual corrections to absolute and rotary positional encodings, together with parameter-free tokenization and corrections to prediction-grid coordinates that remove residual pinhole assumptions. The resulting adapter contains only 10,752 trainable parameters and can be learned from a short temporal segment using geometric losses. Once adapted, RayTun3R transfers effectively to the remaining frames of the sequence without incurring additional runtime costs. Across diverse fisheye datasets with fields of view from $110^\circ$ to $200^\circ$, our adapter reduces rotation error by $2$-$12\times$ relative to the unadapted model, outperforms LoRA while using $\sim\!14\times$ fewer trainable parameters, improves pose over adaptation-free baselines while avoiding their multi-view inference cost, and remains competitive on depth accuracy.

---


### 21. [Evaluating Large Language Models for Decision-Making in Agent-Based Urban Mobility Simulations](https://arxiv.org/abs/2607.02716)

**<font color=#1a73e8>作者：</font>** Bruno Cascaes Alves, Míriam Blank Born, Ulisses Gilioli Francescatto Júnior 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Urban mobility modeling faces challenges in representing decision-making in dynamic environments. Although Multi-Agent Systems are widely used, rule-based approaches rely on fixed heuristics that limit adaptive behavior. This work investigates the integration of Large Language Models (LLMs) as decision-making components in multi-agent simulations. We propose a hybrid architecture that connects the GAMA platform to an external LLM-based module through an API, enabling agents to determine whether route replanning is necessary. Rather than replacing routing algorithms, the LLM serves as a decision layer that guides replanning behavior. The approach incorporates persistent memory, allowing past interactions to influence future decisions and promote behavioral consistency. We compare rule-based and LLM-assisted approaches across multiple road-blockage scenarios and population scales. Results indicate that LLM-enabled agents exhibit greater adaptability and contextual awareness, particularly in scenarios with higher route flexibility. Memory influences performance and behavioral consistency, with effects varying across configurations. Overall, LLMs serve as complementary cognitive layers that enrich behavioral representations in urban mobility simulations and hold potential for modeling complex decision-making in spatial multi-agent systems.

---


### 22. [Doom Researching: A Conceptual Framework for Repetitive AI-Assisted Information Seeking, Cognitive Offloading, and the Illusion of Knowing](https://arxiv.org/abs/2607.02723)

**<font color=#1a73e8>作者：</font>** Santosh Premi Adhikari  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative artificial intelligence (GenAI) systems such as ChatGPT, Claude, and Gemini have made information seeking faster, more conversational, and more cognitively comfortable. These affordances can support learning and productivity, but they can also encourage a repetitive pattern in which users continue querying AI systems for explanations, summaries, comparisons, plans, and reassurance without converting those interactions into durable understanding, decisions, or finished work. This conceptual paper proposes the term doom researching to describe this AI-mediated pattern of repetitive information seeking without proportional synthesis or output. Building on research on doomscrolling, information seeking, cognitive offloading, transactive memory, human-AI interaction, productivity loss, and the illusion of knowing, the paper develops a framework in which fluent AI responses reduce cognitive effort, inflate perceived knowledge, and increase the likelihood of further querying. The framework distinguishes doom researching from doomscrolling, cyberchondria, ordinary research, and productive AI-assisted work. It introduces a formal model of the doom researching loop, a candidate risk index for empirical measurement, and testable propositions for future studies. It then extends the construct through the lens of the extended mind thesis, distinguishing assistive, substitutive, and disruptive forms of cognitive offloading, and connects individual doom researching to the broader literature on AI-driven homogenization and knowledge collapse. The paper argues that doom researching is not simply "too much AI use" but a misalignment among inquiry, metacognition, and output. The goal is to provide a vocabulary and research agenda for studying when AI-assisted inquiry becomes a substitute for thinking, synthesis, and action.

---


### 23. [Echoes of Unrest: A Multimodal NLP Framework for Early Warning of Fake News and Violence-Driven Mob Activity](https://arxiv.org/abs/2607.02734)

**<font color=#1a73e8>作者：</font>** Md. Maruf Bangabashi, Tahmid Hasan, Golam Mahmud 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rapid growth in social media has transformed global communication by enabling fast information exchange, but it has also accelerated the spread of misinformation. Fake news, manipulated content, and provocative narratives are increasingly linked to social unrest, political instability, and mob violence. Incidents in South Asia and elsewhere demonstrate how false information disseminated via platforms such as Facebook and WhatsApp can trigger real-world harm, often spreading faster than fact-checking efforts can respond. To address this challenge, this chapter presents a multilingual, multimodal Natural Language Processing (NLP) framework for early detection of misinformation and violence-prone dynamics. A fused dataset of 138,256 Bangla and English samples was created by combining multiple benchmark datasets. The framework integrates XLM-RoBERTa for multilingual text representation, CLIP for visual embedding, and a multi-head attention mechanism for multimodal fusion, enhanced with auxiliary features such as sarcasm and geospatial metadata. Experiments on a stratified 30% subset achieved 98% test accuracy with strong precision and recall. The outcomes show the efficacy of multimodal approaches in early misinformation detection and highlight the added value of geospatial signals for anticipating real-world escalation.

---


### 24. [Out-of-Distribution Generalization of Risk Aversion in Language Models](https://arxiv.org/abs/2607.02755)

**<font color=#1a73e8>作者：</font>** Kristina Zhang, Junior Chinomso Okoroafor, Benjamin Maltbie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training AIs to be risk-averse in resources could offer a failsafe in the event that AIs turn out misaligned. Misaligned but risk-averse AIs would tend to prefer low-risk, low-reward strategies like cooperation over high-risk, high-reward strategies like rebellion, limiting the downsides of any misalignment. But we can only feasibly train AIs to be risk-averse on low-stakes gambles, and we will only be safe if their risk aversion generalizes to astronomically-high-stakes gambles. Will it? To shed light on this question, we introduce RiskAverseOOD: a benchmark for measuring how well risk aversion generalizes out of distribution. We then offer some initial results. Using a variety of methods to make Qwen3-8B choose risk-aversely when the stakes are low, we find that we can induce substantial risk aversion when the stakes are astronomically high. Our models' learned risk aversion generalizes at least partially across 98 orders of magnitude. From a baseline 2% rate of choosing a safe `Cooperate' option, we see rates around 70% (SFT and tie training), 52% (DPO), and 39% (activation steering). In another experiment, our fine-tuned reward model reliably scores risk-averse reasoning above risk-neutral or excessively risk-averse alternatives (99.6% pairwise accuracy). We replicate these effects at different scales (Qwen3-1.7B and Qwen3-14B) and across model families (Gemma-3-12B-IT and Llama-3.1-8B-Instruct). Overall, we find that risk aversion learned at low stakes can generalize OOD to astronomically high stakes, though not yet consistently enough to serve as a reliable failsafe. Achieving that level of consistency is an open problem.

---


### 25. [Seduced by the Narrative: Assessing Rule Adherence in Semi-Open Textual Sandboxes](https://arxiv.org/abs/2607.02802)

**<font color=#1a73e8>作者：</font>** Weiying Chen, Junlong Shen, Zhanyuan Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As LLMs are increasingly deployed as autonomous adjudicators in semi-open textual game environments, robust rule adherence becomes critical when user intent conflicts with system rules. However, these models are trained to be helpful and compliant, leaving them vulnerable to a class of attacks we term \textit{Rhetorical Injection}, where adversarial users exploit narrative framing techniques such as pseudo-logical reasoning and authoritative coercion to bypass adjudication logic. We present CoC-Seduce, a multi-agent adversarial benchmark built on Tabletop Role-Playing Game (TRPG) mechanics, an ideal instantiation of semi-open environments where rules are explicit for adjudication, yet interaction remains entirely in natural language. Three frontier models, i.e., GPT-5.4, Claude Sonnet 4.6, Gemini 3.5 Flash, serve as adversarial generators producing 5,376 samples across 4 world settings and 16 skill categories. We then benchmark 20 target adjudicators against this corpus. Evaluation across 20 models reveals that neither model scale nor explicit reasoning mechanisms reliably confer adjudication robustness, with \textsc{Pseudo-Logic} emerging as the dominant attack vector and cross-cultural settings exposing systematic knowledge gaps across all evaluated families. Project page: this https URL

---


### 26. [Training Hybrid Block Diffusion Language Models with Partial Bidirectionality](https://arxiv.org/abs/2607.02805)

**<font color=#1a73e8>作者：</font>** Pranshu Chaturvedi, Parth Shroff, Tarun Suresh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-throughput long-context generation is one of the central challenges for large language models. Generation is typically memory-bandwidth-bound rather than compute-bound: each decoding step must stream the accumulated key/value (KV) cache from memory, so bandwidth demand grows with context length while only one token is emitted. Two parallel approaches have therefore emerged: reducing memory access with efficient attention variants and linear-time mixers such as Mamba, or increasing parallel computation by generating blocks of tokens at once. However, technical challenges arise when combining these two ideas. Earlier hybrid diffusion models such as DiffuMamba use bidirectional Mamba mixing, including a reverse-direction scan relative to causal generation. This reverse scan needs to scan the entire sequence, so its states are not prefix-only and cannot be precisely reused as a cache even when diffusion is performed block by block. We propose a BDLM Mamba--attention hybrid that addresses this challenge by restricting the reverse Mamba scan to the active denoising block, which enables exact caching across blocks. In an 87M-parameter DCLM sweep, BDLM Mamba-H achieves the best C4-en validation perplexity compared to BDLM attention and full-sequence baselines. At 350M parameters, it remains competitive with BDLM attention. For long-context inference, BDLM Mamba-H reaches 19.7x the throughput of full-sequence DiffuMamba-H at 65K tokens and 3.7x the throughput of BDLM attention at 262K, showing that Mamba hybrids are a potential long-context diffusion architecture.

---


### 27. [Object-Centric Environment Modeling for Agentic Tasks](https://arxiv.org/abs/2607.02846)

**<font color=#1a73e8>作者：</font>** Yiyang Li, Tianyi Ma, Zehong Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents can improve through accumulated experience, but free-form textual memories become difficult to maintain, validate, and reuse as interactions grow. Recent symbolic approaches learn executable skills or programmatic world models, yet often store local procedures or assume simplified dynamics. We propose Object-Centric Environment Modeling (OCM), which organizes experience into an executable object-centric environment model. OCM maintains two connected code bases: object knowledge, which defines environment entities and mechanisms as Python classes, and procedure knowledge, which records reusable interaction patterns that must import and use the object model. OCM works in an online setting: after each episode, OCM reflects on the trajectory, updates both knowledge bases, and verifies that all procedures execute against the updated object model. During future interaction, the agent uses progressive knowledge disclosure to inspect compact code signatures first and read source code only when needed. Experiments show that OCM achieves the best average rank across benchmarks and reduces invalid actions, demonstrating that agents can benefit from building object-centric environment models.

---


### 28. [Prior Bias in Vision Language Models on UML Diagram Interpretation](https://arxiv.org/abs/2607.02853)

**<font color=#1a73e8>作者：</font>** Zaiyu Cheng, Khai-Nguyen Nguyen, Antonio Mastropaolo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Language Models (VLMs) are increasingly applied to software engineering artifacts, especially UML class diagrams whose meaning depends on visual notation. Yet, it is unclear whether VLMs actually read such diagrams or instead answer from pretrained priors about how classes typically relate. We introduce a controlled UML benchmark in which each prior-conforming diagram is paired with its prior-conflicting counterpart that (1) preserves the same class names and layout while (2) reverses only the relation arrow. We evaluate eight open-source VLMs from two model families, InternVL3.5 and Qwen3, alongside two closed-source frontier models GPT-5.4 and GPT-5.4 Mini. Across the eight open-source models, reversing the arrow reduces relation-direction accuracy by 33.48% on average, while GPT-5.4 Mini retains a 10% gap. In the harder three-class condition, accuracy drops sharply by 45.28% for open-source models, and even 18.62% for the GPT-5.4 family on average. Scaling provides only limited improvements and is family-dependent. Our benchmark presents a diagnostic prior-driven failure in diagram-grounded software understanding. Our artifact is available at this https URL.

---


### 29. [Jointly Improving Dialect Identification and ASR in Indian Languages using Multimodal Feature Fusion](https://arxiv.org/abs/2607.02862)

**<font color=#1a73e8>作者：</font>** Saurabh Kumar, Amartyaveer, Prasanta Kumar Ghosh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic Speech Recognition (ASR) and Dialect Identification (DID) are crucial for Indian languages, many of which are low-resource and exhibit significant dialectal differences. Existing methods often optimize ASR or DID individually, resulting in performance trade-offs. In this work, we propose a multimodal framework that jointly improves ASR and DID. Our method employs a Bottleneck Encoder to extract dialectal features from Conformer-based speech representations and a RoBERTa encoder to process ASR-generated CTC embeddings. A gating mechanism merges these features, followed by an attention encoder to refine the representations. The learned embeddings are concatenated with Conformer outputs to enhance ASR features. Evaluated on eight Indian languages with thirty-three dialects, our method achieves an average DID accuracy of 81.63% and average CER and WER of 4.65% and 17.73%, respectively. These results highlight the effectiveness of our method for joint ASR-DID modeling.

---


### 30. [Reward Granularity in RLVR: Comparing Process and Outcome Reward Structures for Mathematical Reasoning in Small Language Models](https://arxiv.org/abs/2607.02869)

**<font color=#1a73e8>作者：</font>** Anagha Radhakrishna Palandye, Rebecca Glick, Osheen Kaul  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a promising paradigm for improving mathematical reasoning in language models. Yet most RLVR work rewards only the final answer (outcome-based rewards), leaving the impact of step-level process supervision (process rewards) underexplored especially for small models that lack the capacity to self-correct under sparse feedback. We systematically compare five reward conditions applied to Qwen2.5-0.5B fine-tuned with Group Relative Policy Optimization (GRPO) on GSM8K: a no-RL baseline, process-only, outcome-only, and three hybrid weightings ($\lambda \in \{0.9, 0.5, 0.1\}$ process weight). Process-only supervision achieves 63.73% test accuracy versus 53.75% for outcome-only, a nearly 10-percentage point gap while yielding reasoning traces with higher step validity and lower deviation from ground-truth chain length. Hybrid rewards generally correlate positively with process weight, with one notable anomaly: the low-process / high-outcome configuration ($\lambda=0.1$) underperforms pure outcome supervision, suggesting conflicting optimization signals. Error analysis using GPT-4o as a judge reveals distinct failure mode distributions: process models generate structurally inconsistent but arithmetically grounded traces, while outcome models produce concise but derivation-error-prone chains. Our results demonstrate that reward granularity is a first-order design decision for RLVR, with process-level supervision substantially improving both accuracy and trace fidelity in small language models.

---


### 31. [MedCalc-Pro: Solving Complex Medical Calculations with LLM Agents](https://arxiv.org/abs/2607.02879)

**<font color=#1a73e8>作者：</font>** Siran Zhao, Ruihui Hou, Ziyue Huai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current benchmarks for evaluating large language models (LLMs) in medical calculation are largely based on simplified settings, where each patient case corresponds to a single calculator and the required tool is explicitly specified in the query. However, real clinical scenarios often require multiple calculators for joint evaluation, nested-scale calculation, and fuzzy queries that do not directly specify the target calculator. To this end, we propose a new medical calculation benchmark, MedCalc-Pro, which covers three progressively challenging task settings: single-calculator, multi-calculator, and nested-calculator calculation settings. MedCalc-Pro contains 2,268 real-world clinical cases, covering 77 medical calculators across 14 clinical departments. Meanwhile, to address the limited performance of existing frameworks and methods in complex clinical scenarios, we further propose a more generalizable agent framework that supports multi-tool selection and nested-tool calling, while suppressing parameter error propagation through structured validation and evidence review. We conduct systematic comparisons across open-source, closed-source, and medical-specialized LLMs, and the results show that our framework achieves the best performance across all three task settings. This work provides a new benchmark and method for evaluating and applying LLMs in challenging medical calculation scenarios.

---


### 32. [Where do LLMs Fall Short in CBT-Guided Affective Reasoning?](https://arxiv.org/abs/2607.02885)

**<font color=#1a73e8>作者：</font>** Vaishnavi Sinha, Pooja Guttal, Pranay Deep Reddy Katike 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cognitive Behavioral Therapy (CBT) provides a structured framework for understanding a user's mental state by examining the interaction between cognitive and behavioral factors. However, out-of-the-box LLMs respond fluently and empathetically, yet collapse into validation & reflection, regardless of what the user actually needs. They know theoretical CBT (scoring up to 96% accuracy on licensing exam questions) but fail to apply it effectively. We explore this gap with a knowledge-guided framework that treats CBT dialogue as controlled affective reasoning: user narratives are decomposed into Beck's Cognitive Conceptualization structure, grounded in clinical SNOMED CT concepts validated via Natural Language Inference, and a Multiple Chain-of-Thought (MCoT) strategy selection between Validation & Reflection, Socratic Questioning, or Alternative Perspectives. To measure whether such guidance actually changes behavior, we introduce the Protocol Leverage Force (F), a behavior-level metric that captures how far an intervention shifts a model away from its default response. Across three open-weight LLMs and 14 RealCBT-derived case studies, evaluated with human experts, valence-arousal trajectories, and linguistic entrainment, F shows that simply introducing protocol definitions via single chain-of-thought prompting fails to change LLM behavior, while MCoT on these definitions guides strategy selection better. Still, the effect stays within 1% (approx. 1.2-1.3%), and all models remain biased toward Validation & Reflection. These results show CBT knowledge alone does not ensure effective application, giving the affective-computing community instrumentation to measure where LLMs fall short.

---


### 33. [Variable Bit-width Quantization: Learning Per-Group Precision for "Bigger-but-Smaller" Language Models](https://arxiv.org/abs/2607.02893)

**<font color=#1a73e8>作者：</font>** Hamish Ogilvy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-bit quantization shrinks language models but treats precision as a single global hyper-parameter: every weight uses the same bit-width. We introduce Variable Bit-width Quantization (VBQ), a training-time method in which each contiguous group of 64 weights learns its own resolution from {1,2,4,8} bits via a Gumbel-Softmax relaxation, trained jointly by an alternating optimization that gives the precision logits a clean, task-aligned signal. VBQ discovers a consistent, strongly heterogeneous allocation within individual projection types, not merely across layers, impossible to express with per-layer methods: 69% of groups collapse to 1 bit, the LM head averages 1.09 bits, while the first MLP block keeps ~2.5 bits. This pattern is stable enough to freeze into a fixed recipe and reuse without further search. The recipe yields a "bigger-but-smaller" regime: a 131M model at 1.82 mean bits reaches perplexity 4.2 on TinyStories, beating a 55M FP16 model (PPL 4.4) at 3.8x less storage, and lets a 1.46B model on FineWeb-Edu match a 593M FP16 control at ~3.7x less storage with 2.5x more parameters. As quality-per-byte, VBQ is 3.9-8.4x more efficient than FP16. The recipe maps directly to packed low-bit storage, so it also accelerates inference: with custom fused dequantize-and-multiply kernels, memory-bandwidth-bound autoregressive decode is faster at equal output, and the speedup grows with scale (parity at 131M, 1.9x at 1.0B, 4.7x at 9B on Apple silicon). A distributional analysis (KL divergence and argmax-flip rate) reveals a striking mechanism: deeper layers progressively self-heal the quantization error injected by early layers. The win is a from-scratch, train-time phenomenon; scaling the search economically beyond 1.5B parameters remains open. VBQ reframes precision as a learnable, non-uniform resource and shows that spending a fixed bit budget unevenly beats spending it uniformly.

---


### 34. [ProLaViT: Learning Progressive Latent Visual Thoughts in Structured Latent Space](https://arxiv.org/abs/2607.02907)

**<font color=#1a73e8>作者：</font>** Peiming Li, Yifan Wang, Xiaotian Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have achieved remarkable progress but still struggle with complex visual reasoning tasks requiring multi-step perception and logical deduction. While explicit visual generation incurs prohibitive computational costs, existing latent approaches often rely on external experts or lack rigorous cognitive logic. In this paper, we introduce ProLaViT (Progressive Latent Visual Thought), a framework empowering MLLMs to perform structured visual derivation in the continuous latent space. Unlike works dependent on heterogeneous external models, ProLaViT leverages an endogenous self-distillation mechanism, utilizing the model's own visual encoder to supervise latent thoughts. To facilitate this, we construct a scalable programmatic synthesis pipeline enabling the model to internalize algorithmic precision without inference time tools. We design two reasoning paradigms: (1) Coarse-to-Fine Causal Chain for spatial tasks, guiding attention from global context to local targets. (2) Dialectical Reasoning Chain for logical tasks, incorporating counter-factual thinking for verification. Furthermore, we propose a Distance-Weighted Diversity Loss to impose topology-aware constraints, preventing feature degeneration by enforcing semantic distinctiveness. Extensive experiments demonstrate that ProLaViT outperforms baselines on vision-centric benchmarks, achieving superior accuracy and interpretability with high efficiency.

---


### 35. [Learning Taxonomic Trees with Hierarchical Representation Regularization for Large Multimodal Models](https://arxiv.org/abs/2607.02909)

**<font color=#1a73e8>作者：</font>** Hulingxiao He, Zhi Tan, Yuxin Peng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Taxonomies provide key information about the semantic relationships between concepts and the inherent organization of vision and language. Despite their impressive capabilities, large multimodal models (LMMs) often lack taxonomic knowledge, leading to low hierarchical visual recognition (HVR) consistency. These models typically only rely on language modeling objectives during fine-tuning and lack explicit taxonomy-aware regularization. To address this, we propose Hierarchical Representation Regularization ($HiR^2$), a simple plug-and-play regularizer that improves hierarchical consistency in LMMs. Specifically, we introduce a semantic-aware visual tree construction framework that extracts coarse-to-fine visual features from intermediate LLM layers guided by textual cues. The regularizer combines two complementary objectives: a taxonomic entailment loss that enforces hierarchy via hyperbolic entailment cones in the Lorentz model, and a discriminative dispersive loss that promotes angular separation of semantically similar embeddings on the unit sphere without disturbing the radial hierarchical structure. Extensive experiments demonstrate that $HiR^2$ effectively captures taxonomic structures across diverse LMMs and fine-tuning methods. Code is available at this https URL.

---


### 36. [Oyster-II: Reinforcement Learning for Constructive Safety Alignment in Large Language Models](https://arxiv.org/abs/2607.02914)

**<font color=#1a73e8>作者：</font>** Jiyang Guan, Yong Xie, Jun Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated remarkable capabilities across diverse applications, yet ensuring their simultaneous safety, helpfulness, and trustworthiness remains a persistent challenge. Conventional refusal-oriented alignment strategies mitigate harmful content generation but systematically fail to serve legitimate user needs, often withholding information that could safely and constructively address the underlying intent of sensitive queries. Building upon the constructive safety paradigm pioneered by Oyster-I, which moves beyond blanket refusal toward thoughtful, response-oriented safety alignment, we identify two critical limitations of its Supervised Fine-Tuning (SFT)-based scheme: insufficient safety generalization to out-of-distribution scenarios and a phenomenon we term safety chain-of-thought (CoT) over-generalization, wherein safety-oriented reasoning patterns are excessively applied to benign queries, degrading helpfulness and user experience. To address these limitations, we propose Oyster-II, a reinforcement learning (RL)-based constructive safety alignment framework that adopts a Zero-RL paradigm combined with a multi-stage reinforcement learning this http URL across extensive benchmarks, Oyster-II comprehensively surpasses both Qwen3-14B and its predecessor Oyster-I on safety dimensions, achieving cross-scale performance comparable to Qwen3-Max and Qwen3.5-397B.

---


### 37. [VideoSearcher: Empowering Video Deep Research with Multi-Tool Agentic Reasoning via Reinforcement Learning](https://arxiv.org/abs/2607.02927)

**<font color=#1a73e8>作者：</font>** Zhenkun Gao, Yicheng Bao, Jinlong Peng 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video understanding is moving beyond closed-context perception toward open-world evidence exploration, a paradigm formalized as Video Deep Research (VDR). However, existing multimodal search agents primarily target static images, and the current VDR benchmark relies on text-centric retrieval that discards crucial visual information. To address these limitations, we propose VideoSearcher, a closed-loop agentic framework that empowers Vision-Language Models with multi-tool reasoning for VDR. VideoSearcher unifies temporal localization, spatial focusing, and multimodal search within a single reasoning trajectory, enabling agents to progressively ground visual clues, retrieve relevant evidence, and synthesize answers. To optimize knowledge-intensive reasoning trajectories, we propose Bi-branch Sequence Policy Optimization (BiSPO), a reinforcement learning algorithm that decouples tool-invocation optimization from answer-accuracy optimization. This design provides stable learning signals for both evidence-grounded reasoning and purposeful tool use. Furthermore, we construct VideoSearch-QA, the first benchmark designed to evaluate open-world video information grounding and multimodal search-based reasoning. Extensive experiments demonstrate that VideoSearcher significantly outperforms prior open-source agentic baselines across various search-oriented and multimodal understanding benchmarks.

---


### 38. [CL-Anomaly: Layer-Adaptive Mixture-of-Experts with Multimodal Large Language Model for Continual Learning in Anomaly Detection](https://arxiv.org/abs/2607.02930)

**<font color=#1a73e8>作者：</font>** Wen Dong, Zhao Wang, Shuangqing Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) excel in diverse vision tasks, but full-parameter retraining is computationally expensive as real-world knowledge evolves. Existing continual learning methods often suffer from semantic entanglement in parameter spaces across tasks, impeding the continuous deployment of models. This challenge is especially pronounced in Anomaly Detection (AD), which exhibits triple heterogeneity across modalities, domains, and defect scale variability, significantly complicating multi-task knowledge transfer. In this paper, we propose CL-Anomaly, a parameter-efficient fine-tuning framework based on an isolation-sharing collaboration to enable continual learning for anomaly detection with MLLMs. We introduce the task-private expert PrivLoRA, which physically isolates task-specific subspaces in the parameter space to prevent semantic entanglement of anomaly knowledge in diverse scenarios. The Layer-Adaptive Shared Experts maintain cross-task representations within a unified feature space, enabling knowledge sharing between previous and new tasks. Furthermore, we propose a Layer-Adaptive Knowledge Transfer strategy that automatically selects and dynamically updates the layer-wise key shared experts of each task via a momentum-based mechanism, promoting effective knowledge transfer across related anomaly detection tasks. Extensive experiments across three continual learning scenarios for anomaly detection, including class-incremental, cross-domain, and cross-modal, demonstrate that CL-Anomaly outperforms state-of-the-art methods. Code is available at this https URL.

---


### 39. [Incentivizing Vision Language Models to Search for Long Video Question Answering](https://arxiv.org/abs/2607.02959)

**<font color=#1a73e8>作者：</font>** Harsh Goel, S P Sharan, Sahil Shah 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce VSeek, an agentic framework that transforms long-video question answering (LVQA) from a passive, single-pass perception task into a multi-turn retrieval process. VSeek utilizes a natural language-driven search to identify relevant context within long videos and is post-trained with reinforcement learning (RL) to jointly formulate targeted search queries and reason over retrieved clips for LVQA. While RL post-training has revolutionized reasoning in symbolic domains such as mathematics and code, its application to long-video understanding remains hindered by a lack of verified rewards. To ensure that the retrieved context is relevant, we propose a novel neuro-symbolic approach that bridges open-ended natural language with discrete visual verification. Specifically, complex user queries are compiled into formal temporal logic specifications for systematically decomposing natural language questions into a definitive checklist of required atomic visual primitives, such as key objects and activities, along with their temporal ordering. These systematically derived grounding events provide the critical feedback signal for RL post-training, enabling dense, verifiable rewards based on the successful retrieval of these specific visual elements rather than relying entirely on outcome-only answer accuracy. By explicitly optimizing for this verifiable evidence-seeking behavior, VSeek improves Pass@1 scores by up to 8% and Pass@4 scores by 15% on long-video understanding benchmarks compared to base models. We open-source our code at this https URL.

---


### 40. [Overloading Large Vision-Language Models for Jailbreaking](https://arxiv.org/abs/2607.02961)

**<font color=#1a73e8>作者：</font>** Haoyu Zhang, Yangyang Guo, Mohan Kankanhalli  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) exhibit remarkable vision-language capabilities and are increasingly deployed in real-world applications such as personal assistants, document analysis systems, and embodied agents. However, their dual-modal attack surfaces make them vulnerable to jailbreak attacks. Existing LVLM jailbreaks rely on simple designs, e.g., short text and out-of-distribution images. Nevertheless, recent advancements in both large language model backbones and multimodal mechanisms undermine these attacks, particularly their transferability among model architectures. To overcome this limitation, we propose a novel information overloading method that is equipped with both extensive text and multi-dimensional image attacks. These components are arranged in recursion-based image-typography layouts to exponentially increase multimodal information complexity. This overloading approach amplifies the cross-modal processing required, which undermines the safety alignment in LVLMs. Extensive experiments on both open-sourced and commercial LVLMs establish our method as a new state-of-the-art LVLM jailbreak attack. On open-source models, our method achieves an average ASR of 88.6%; on commercial LVLMs, it reaches an average ASR of 84.0%, exceeding the best baseline by 48.7%. Moreover, our prompts optimized on open-source surrogate models transfer effectively across model families. Beyond empirical results, we probe the safety-critical information flows within victim LVLMs. Our observations reveal that complex image-typography compositions induce intensified cross-modal processing and reduce the model's certainty in generating refusal responses. Together, these findings highlight information overloading as a practical and emerging safety risk for real-world LVLM deployments, underscoring the need for stronger defenses against complex multimodal jailbreak inputs.

---


### 41. [Distill Where the Student Goes: Teacher-Regularized RL for English-Evidence Cross-Lingual RAG](https://arxiv.org/abs/2607.02966)

**<font color=#1a73e8>作者：</font>** Haotian Zhou, Weiran Huang, Siqi Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-lingual retrieval-augmented generation (RAG) is often deployed in an English-evidence regime, where users query in diverse languages but retrieved passages remain English. In this setting, generation can fail despite strong base models: English evidence induces language drift (English or code-switching outputs) and models use evidence unreliably when producing non-English answers. We attribute these failures to two post-training challenges: (i) errors are prefix-dependent, so fixed-trajectory supervision suffers from prefix mismatch; and (ii) sequence-level (partly discrete / judge-based) rewards yield noisy credit assignment and high-variance updates. We propose TR-RAG, a teacher-regularized RL recipe that couples reward optimization with on-policy distillation on student-visited prefixes. A compact student samples on-policy answers, while a stronger frozen teacher is queried only on those prefixes and provides a prefix-wise student-to-teacher reverse-KL anchor. We further introduce a reward decomposition for English-evidence multilingual generation, combining language consistency, character 3-gram recall, and an LLM-judge score for evidence-grounded correctness. Across three benchmarks -- BioASQ-ENKB5, Hotpot-ENKB5, and naturally multilingual MKQA -- and two backbones, TR-RAG improves the composite of language adherence and evidence-grounded correctness over strong baselines. Crucially, the teacher anchor acts as a safety net: on in-domain languages it prevents the large language-consistency collapses (up to ~27 percentage points) that reward-only RL can suffer by drifting below even the base model, while on distant out-of-distribution languages -- where reward-only RL stalls at the base model's ceiling -- it still improves evidence grounding; and on character 3-gram recall the compact student sometimes surpasses its 70B teacher.

---


### 42. [Reinforcement Learning for Evidence-Seeking Diagnostic Reasoning with Large Language Models](https://arxiv.org/abs/2607.02983)

**<font color=#1a73e8>作者：</font>** Shengyi Hua, Kangzhe Hu, Conghui He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent reasoning-centric Large Language Models (LLMs) have made significant strides, yet they predominantly operate on a passive-inference pattern that assumes complete information. In contrast, real-world clinical intelligence is inherently an iterative investigative process requiring strategic evidence acquisition. To bridge this gap, we formalize medical diagnosis as an Iterative Evidence-Seeking Task. We leverage Reinforcement Learning with Verifiable Rewards (RLVR) to elicit intrinsic reasoning within a closed-loop environment, guided by a novel suite of rewards that enforce diagnostic precision and examination consistency. To facilitate this, we introduce the Retrieval-Augmented Generation-based Examination Simulator (RAGES), a high-fidelity clinical oracle that provides realistic, knowledge-grounded follow-up evidence. Empirical results across diverse datasets demonstrate that our framework enables LLMs to transition from passive responders to autonomous assistants. Notably, our model demonstrates comparable performance to larger and reasoning-enhanced baselines, while RAGES proves superior to vanilla LLMs in generating biologically plausible clinical feedback.

---


### 43. [GuideMe: Multi-Domain Task Guidance and Intervention in Streaming Video](https://arxiv.org/abs/2607.02991)

**<font color=#1a73e8>作者：</font>** Fang Liu, Jinpeng Chen, Ke Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While multimodal Large Language Models (MLLMs) excel at offline video understanding, an interesting question of how far they are from serving as a real-time procedural coach remains unknown. Such a role typically requires an MLLM to continuously monitor the execution, detect mistakes, and provide corrective guidance in a closed-loop interaction. In this paper, we construct GuideMe, the first multi-domain benchmark for streaming video that supports training and evaluation of MLLMs for closed-loop interactive task guidance. It comprises 2,458 videos spanning 223.7 hours across diverse domains (\eg, cooking, object manipulation, daily-life guidance, and fitness), with 47,775 interaction samples covering next-step instructions, completion feedback, error detection, and corrective guidance. To evaluate existing models on GuideMe, we design a three-component assessment framework to measure the capabilities of representative MLLMs, which consists of temporal-semantic bipartite matching for sequence-level alignment, behavioral classification for intervention timing, and LLM-as-a-Judge for content quality. Extensive experiments highlight a critical performance asymmetry: despite excelling at providing instructions, existing MLLMs consistently fail to identify execution errors and respond with corrective feedback. Code and data are released at this https URL.

---


### 44. [VISTA: Auditing Semantic Divergence in Vision-Language Models](https://arxiv.org/abs/2607.02995)

**<font color=#1a73e8>作者：</font>** Junchi Liao, Jiawen Deng, Fuji Ren  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models can exhibit visual concept-conditioned divergence: given images containing demographic features, corporate logos, or ideological symbols, some models produce unusually uniform responses that differ from what peer models say about the same input. These behaviors evade text-only audits because visual concepts cannot be isolated or substituted the way text tokens can. We present VISTA (Visual Inconsistency Screening Through Analysis), a black-box cross-model audit that couples semantic entropy with distribution-based divergence to flag model-specific anomalies. In a controlled study, we implant concept-conditioned stances in three VLMs via fine-tuning on small biased datasets and confirm that VISTA detects them. Auditing six VLMs across 19 topics, VISTA surfaces 142 high-suspicion cases (1.2%) and identifies selective refusal as a previously unreported divergence pattern, where models refuse demographic queries at rates varying from 0 to 65% across groups.

---


### 45. [CONFLUX: A Latent Diusion Model for 3D Chest-CT Synthesis with RL Post-Training](https://arxiv.org/abs/2607.02998)

**<font color=#1a73e8>作者：</font>** Max Van Puyvelde, Halil Ibrahim Gulluk, Wim Van Criekinge 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Controllable generative models of 3D medical images can synthesize volumes with specified clinical attributes, but this demands samples that are simultaneously high-fidelity, natively 3D, and faithful to the requested conditioning. We present CONFLUX, a latent diffusion model for chest computed tomography (CT): a 3D variational autoencoder compresses each volume, and a rectified-flow transformer generates in the latent space. Generation is conditioned on structured radiological metadata (18 abnormality findings, sex, age, and reconstruction kernel) through adaptive layer normalization. The model leads strong volumetric baselines on tri-planar Frechet distance (FID 32.3 vs. 74.6 for MAISI) while exposing direct control over clinical attributes. To strengthen that control we add an online reinforcement-learning post-training stage (group-relative policy optimization) that rewards how reliably a classifier recovers the requested findings from each generated volume. Judged by a separate, independent classifier, post-training removes 47% of the shortfall relative to real-scan reliability. We release the model and a ~200k synthetic chest-CT dataset with conditioning metadata spanning a wide variety of clinical findings.

---


### 46. [psytechlab at CLPsych 2026: Utilising Natural Language Processing methods and Large Language Models for Social Media Text Analysis](https://arxiv.org/abs/2607.03003)

**<font color=#1a73e8>作者：</font>** Igor Buyanov, Nafisa Valieva, Ekaterina Mazurina  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Social media posts are a rich and valuable source of data for analyzing mental health states and users' well-being using automated analysis tools. In this work, we demonstrate how we used a range of Natural Language Processing (NLP) methods, including Long Short-Term Memory (LSTM), BERT-based models, and Large Language Models (LLMs), for self-state and well-being analysis and summarization during the CLPsych Shared Task 2026. Our approach achieved one of the top Consistency and Contradiction scores for the summarization task and also middle-level results for the other tasks. By testing and developing such mental health-state estimation systems, we contributed to improving mental health support systems. We make our code available this https URL.

---


### 47. [Back to Basics: Improving Molecular Understanding in LLMs via SMILES-Graph Translation](https://arxiv.org/abs/2607.03007)

**<font color=#1a73e8>作者：</font>** Wenda Wang, Jinjia Feng, Zhewei Wei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in molecular large language models have led to strong performance on molecular understanding and generation tasks, yet these gains often come without reliable structural grounding. In particular, existing approaches conflict with the chemistry principle that structure determines function: despite their downstream success, current molecular LLMs perform poorly on basic structure recognition, suggesting that they fail to capture molecular graphs from canonical SMILES. To remedy this, we propose MolBasic, a structure-first framework that strengthens structural comprehension via SMILES-Graph translation. MolBasic is built around a multi-level structure perception benchmark, where bidirectional SMILES-Graph conversion serves as the core task to align sequential and topological representations. On top of this foundation, we employ a progressive learning scheme with a standardized Chain-of-Thought (CoT) to steer models from structure acquisition toward higher-level molecular reasoning. Experiments show that MolBasic substantially improves structural understanding and yields robust gains on downstream tasks, including property prediction and objective optimization, supporting our structure-first paradigm.

---


### 48. [Do ECG Foundation Models Transfer to Rare Cardiac Diseases? Evidence from Brugada Syndrome Detection](https://arxiv.org/abs/2607.03009)

**<font color=#1a73e8>作者：</font>** Beatrice Zanchi, Giuliana Monachino, Alvise Dei Rossi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Background: Foundation models (FMs) trained on large-scale unlabeled physiological data have emerged as a promising paradigm for medical artificial intelligence. Their ability to capture clinically meaningful, transferable representations for rare diseases remains largely unproven. This study investigates whether FM pre-training provides genuine clinical generalization benefits beyond improved optimization for rare electrocardiographic (ECG) phenotypes. Methods: We systematically evaluated nine publicly available ECG FMs for Brugada syndrome detection on the BrSwiss cohort (294 patients, 87 cases) and the independent external HUCA cohort (363 patients, 76 cases), under three strategies (from-scratch training, linear probing, full fine-tuning) across several configurations, including a 3% data ablation and zero-shot cross-site transfers. Results: Pre-training was necessary for high-capacity architectures unable to converge from scratch (AUC gain up to 0.411, p < 0.05), but gave no significant gain for compact architectures already converged on labeled data alone. On full BrSwiss, the best fine-tuned FM (ECG-CPC, AUC = 0.962) only marginally exceeded the strongest supervised baseline (ECG-CPC from scratch, AUC = 0.932; p = 0.091). At matched training-set size, the data-efficiency advantage on BrSwiss-3% (AUC gain = 0.055, p < 0.01) did not replicate on HUCA. Under zero-shot cross-site transfer, FM-based pipelines did not generalize better than supervised baselines, all approaching chance-level performance. Conclusion: For Brugada syndrome detection, FM pre-training is mechanical rather than semantic, providing optimization stability rather than transferable clinical knowledge. These findings challenge the assumption that large-scale pre-training inherently encodes clinically meaningful representations, highlighting the central role of model architecture and data-domain alignment.

---


### 49. [Human-Centric Reflective Architecture for Human-AI Collaborative Decision-Making](https://arxiv.org/abs/2607.03025)

**<font color=#1a73e8>作者：</font>** Andreas Kouridakis, Dimitrios Patiniotis Spyropoulos, George Vouros  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The use of Large Language Models (LLMs) across diverse areas of human activity-ranging from everyday tasks to safety-critical applications-aims to enhance decision-making effectiveness with minimal human feedback. Concurrently, it seeks to align decisions with human expectations, preferences, and needs while mitigating risks associated with AI non-determinism. However, humans frequently over- or under-rely on AI recommendations, and current AI systems remain poorly calibrated to human expectations. To address these challenges, we introduce a human-AI collaborative decision-making framework designed to augment human capabilities and align AI agents with human preferences and expectations. Specifically, this paper (a) formulates the collaborative decision-making task as a stochastic game between an AI agent and a human player, and (b) proposes the Human-Centric Reflective Architecture (HCRA), which integrates human-calibrated models with reinforcement learning agents that leverage linguistic feedback in an iterative, reflective process. Evaluation results demonstrate that HCRA enhances decision-making effectiveness and delivers high-quality recommendations.

---


### 50. [Alignment-Guided Largest Table Overlap Size Estimation](https://arxiv.org/abs/2607.03049)

**<font color=#1a73e8>作者：</font>** Ge Lee, Shixun Huang, Zhifeng Bao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fast estimation of the size of the largest overlap between tables enables blocking and query-by-table retrieval in large table repositories. The first and the state-of-the-art estimator Armadillo improves efficiency by embedding each table independently and approximating overlap ratio via embedding similarity. However, accurate estimation in heterogeneous repositories remains limited by three challenges: (C1) overlap depends on row-column structure, i.e., each matched cell must preserve both its row and column membership under a joint alignment of the two tables, but existing encodings leave this structure to be inferred indirectly; (C2) independent encoding provides no explicit channel for inter-table alignment signals, biasing prediction toward global similarity; (C3) naive value encodings overfit to corpus-specific distributions, causing cross-domain degradation. Hence, we propose ALORE, a scalable and domain-robust overlap ratio estimator built on three principles: (P1) explicitly represent row-column structure; (P2) expose inter-table alignment signals during training without expensive alignment search; (P3) reduce sensitivity to corpus-specific value distributions. ALORE instantiates these principles with a Two-View Row-Column Hypergraph encoder, alignment-guided objectives with inexpensive interaction signals, and a domain-robust value mapping. Experiments on multiple datasets spanning diverse domains and scales, including a large real-world corpus beyond prior benchmarks, show that ALORE outperforms the state of the art. ALORE reduces MAE by up to 55% overall and 69% in zero-shot transfer, while achieving up to 89x speedup. We further validate its effectiveness for query-by-table retrieval.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-248](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
