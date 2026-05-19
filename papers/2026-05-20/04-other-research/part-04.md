# 📦 其他研究 | 2026年05月20日

> 本类共 **619** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-619](./part-13.md)

---

### 151. [3DPhysVideo: Consistency-Guided Flow SDE for Video Generation via 3D Scene Reconstruction and Physical Simulation](https://arxiv.org/abs/2605.16795)

**<font color=#1a73e8>作者：</font>** Hwidong Kim, Yunho Kim, Tae-Kyun Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generative models have made remarkable progress, yet they often yield visual artifacts that violate grounding in physical dynamics. Recent works such as PhysGen3D tackle single image-to-3D physics through mesh reconstruction and Physically-Based Rendering, but challenges remain in modeling fluid dynamics, multi-object interactions and photorealism. This work introduces 3DPhysVideo, a novel training-free pipeline that generates physically realistic videos from a single image. We repurpose an off-the-shelf video model for two stages. First, we use it as a novel view synthesizer to reconstruct complete 360-degree 3D scene geometry by guiding the image-to-video (I2V) flow model with rendered point clouds. Second, after applying physics solvers to this geometry, the physically simulated point cloud is used to guide the same I2V flow model to synthesize final, high-quality videos. Consistency-Guided Flow SDE, which decomposes the predicted velocity of the I2V flow model into denoising and consistency bias, enforces consistency to the conditional inputs, allowing us to effectively repurpose the model for both 3D reconstruction and simulation-guided video generation. In the diverse experiments including multi-objects, and fluid interaction scenes, our method successfully bridges the gap from single-images to physically plausible videos, while remaining efficient to run on a single consumer GPU. It outperforms state-of-the-art baselines on GPT-based scores, VideoPhy benchmark and human evaluation.

---


### 152. [Watermarks Attack Watermarks: Re-Watermarking as a Generic Removal Strategy](https://arxiv.org/abs/2605.16796)

**<font color=#1a73e8>作者：</font>** Maria Bulychev, Neil G. Marchant, Benjamin I. P. Rubinstein  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Watermarking combines an imperceptible change to an input image that will trigger a detector, to assert provenance and protect intellectual property. The literature has shown great interest in attacks on watermarking schemes: attackers are clearly motivated to steal copyrighted material or circumvent legislated deepfake protections. In this work, we make a simple-yet-powerful observation: that such attacks on watermarking-like watermarks themselves-seek an imperceptible change to an input image (now already watermarked) that will trigger a detector. This analogy comparing watermark attacks to watermarking itself is highly suggestive: that watermarks could be used to attack watermarks. Our first contribution validates this hypothesis. In rigorous experiments spanning 96 combinations of dataset, victim, and attack watermarks, we show that simply re-watermarking an already watermarked image reliably suppresses the original signal, without requiring gradients, surrogate models, or detection keys. Our second contribution is a simple classifier for detecting the presence and identity of an existing watermark in a given image. Surprisingly, experimental findings demonstrate outstanding overall accuracies 0.878-0.953. This result is of independent interest as a security vulnerability: research shows that method-specific attacks achieve substantially stronger removal than black-box attacks. Taken together, watermark identification combined with re-watermarking successfully reduces bit accuracy by at least 25% and up to 48%. Our work constitutes a cheap, generic, and highly effective attack pipeline, calling into question the reliability of current watermarking schemes to such a simple attack, as well as the value of existing sophisticated attacks.

---


### 153. [EgoKit: Towards Unified Low-Cost Egocentric Data Collection with Heterogeneous Devices](https://arxiv.org/abs/2605.16797)

**<font color=#1a73e8>作者：</font>** Liuchuan Yu, Erdem Murat, Beichen Wang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric video is increasingly used as a data source for robot learning, activity understanding, and embodied AI research, but collecting it at scale remains fragmented in practice: each candidate host device, such as an Android phone, iPhone, iPad, smart glasses, or extended reality (XR) headset, exposes a different SDK, a different policy on raw camera access, and different limitations on external USB cameras and on-device tracking. Synchronized ego-view and wrist-view capture is therefore typically obtained by either committing to a single proprietary platform or building one-off rigs that do not transfer across devices. To address this gap, we present EgoKit, a toolkit that exposes the same egocentric recording workflow across six heterogeneous host devices. Across all supported devices, EgoKit presents the same recording interaction and produces locally stored video with a uniform log format; on XR headsets, it additionally logs head pose and OpenXR-standard 26-joint hand tracking aligned to the video streams. The companion accessories, including two wrist cameras with mounts, a head strap, and a USB-C hub, add wrist-view capture to any supported host without custom hardware fabrication. EgoKit is available at \url{this https URL}.

---


### 154. [Stop Starving or Stuffing Me: Boosting Firmware Fuzzing Efficiency with On-demand Input Delivery](https://arxiv.org/abs/2605.16798)

**<font color=#1a73e8>作者：</font>** Shandian Shen, Wei Zhou, Keming Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Firmware fuzzing has gained attention for identifying firmware bugs. However, current approaches often directly integrate fuzzing tools for general software. General software receives input as it encounters I/O functions, but firmware input can be received asynchronously and independently of the firmware's execution, with uncertain timing and quantity. Without full awareness of firmware's exceptions, existing solutions often imprudently deliver fuzzer-generated input to the firmware in an ad-hoc way. This either overwhelms the processing function of the firmware (stuffing) or fails to deliver enough input data to trigger input processing functions (starving). In both cases, fuzzing capability is weakened.
In this paper, we comprehensively investigate the input delivery issue. To determine the optimal timing and quantity for delivering test cases, we leverage the fact that firmware has to check input availability before using data. So we employ static and dynamic analysis to map each input processing route into three stages: input retrieval, availability check, and processing. This recovered semantic information allows the fuzzer to accurately deliver input at the availability check points within the expected length range. For multiple input routes problem, we also optimize the scheduling algorithm to reach more diverse routes. Our prototype, named FIDO, can serve as an add-on to existing firmware fuzzers to enhance their test-case delivery effectiveness. Compared to ad-hoc input delivery methods used in Fuzzware and MULTIFUZZ, FIDO increases their median code coverage by up to 115% and 54%, respectively. Compared to SEmu, which requires humans to manually specify input delivery points, FIDO still improves its coverage by up to 19%. As a result, FIDO discovers known bugs significantly faster and also identifies five previously unknown bugs.

---


### 155. [FIM-LoRA: Task-Informative Rank Allocation for LoRA via Calibration-Time Gradient-Variance Estimation](https://arxiv.org/abs/2605.16800)

**<font color=#1a73e8>作者：</font>** Ramakrishnan Sathyavageeswaran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation (LoRA) assigns a uniform rank to every adapted weight matrix - a practical convenience that ignores a fundamental reality: different layers contribute unequally to task adaptation. We address this with a lightweight engineering solution: before fine-tuning begins, run eight calibration backward passes, compute the gradient variance of each LoRA-B matrix as a proxy for layer informativeness, and redistribute the rank budget proportionally. The resulting adapter is a standard LoRA with a per-layer rank pattern - no new parameters, no training overhead, no changes to serving infrastructure. We implement this via an efficient approximation of the empirical Fisher Information Matrix (eFIM) diagonal, restricted to LoRA adapter matrices only, which reduces memory cost by approximately 256x compared to full-model Fisher estimation. On GLUE with DeBERTa-v3-base, FIM-LoRA matches LoRA (88.6 vs. 88.7) at the same parameter budget, and on commonsense reasoning with LLaMA-3-8B reaches 68.5 vs. 68.7 for LoRA. The per-layer rank maps are interpretable: value projections and early-to-middle layers consistently receive higher rank, consistent with established findings on transformer layer roles.

---


### 156. [NeuroLiDAR: Adaptive Frame Rate Depth Sensing via Neuromorphic Event-LiDAR Fusion](https://arxiv.org/abs/2605.16805)

**<font color=#1a73e8>作者：</font>** Darshana Rathnayake, Dulanga Weerakoon, Meera Radhakrishnan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDARs are widely used for 3D depth reconstruction, but their performance is often limited by inherent hardware constraints that impose trade-offs between range, spatial resolution, and frame rate. Many LiDAR systems typically operate at low frame rates (e.g., 5-10 Hz), prioritizing long-range sensing over responsiveness to rapid scene changes. We present NeuroLiDAR, an adaptive depth sensing framework that achieves effective frame rates of up to $\approx$66 Hz by fusing temporally sparse LiDAR data with temporally dense inputs from neuromorphic event cameras. NeuroLiDAR integrates two components: event-based keyframe detection and event-guided depth extrapolation, to dynamically adjust the sensing rate in response to scene dynamics. To evaluate our approach, we introduce ELiDAR, a dataset spanning outdoor and indoor scenarios, and show that NeuroLiDAR reduces depth reconstruction error by $\approx$29\% in RMSE while achieving adaptive frame rates between 27.8-47.3 Hz. Our code and dataset are available at this https URL.

---


### 157. [DecoRec: Decomposed 3D Scene Reconstruction from Single-View Images via Object-Level Diffusion](https://arxiv.org/abs/2605.16807)

**<font color=#1a73e8>作者：</font>** Yuhan Ping, Yuan Liu, Xiaoxiao Long 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we introduce \textit{DecoRec}, a novel system designed to elevate single-view 2D images to a decomposed 3D scene mesh. Current methods for single-view scene reconstruction typically rely on object retrieval or the regression of coarse 3D voxels or surfaces, leading to inaccuracies in capturing the appearance and geometry of the input image. The lack of high-quality large-scale scene-level datasets further complicates direct 3D scene generation from single-view images. To achieve high-quality 3D scene generation from a single-view image, DecoRec takes advantage of recent diffusion-based single-view object reconstruction methods to reconstruct individual objects separately. Subsequently, a refinement pipeline is proposed to effectively merge these reconstructed objects, enhancing appearance and geometry through a differentiable rendering technique and diffusion-guided refinement. Our results demonstrate that DecoRec facilitates high-quality single-view scene reconstruction in both geometry and novel synthesis, offering significant benefits for downstream applications like room interior design.

---


### 158. [Informative Graph Structure Learning](https://arxiv.org/abs/2605.16809)

**<font color=#1a73e8>作者：</font>** Shen Han, Zhiyao Zhou, Jiawei Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The quality of graph-structured data is fundamental to the success of modern graph analysis techniques such as Graph Neural Networks (GNNs). However, real-world graph data is often suboptimal, suffering from issues such as noise and incomplete connections. Graph Structure Learning (GSL) has emerged as a promising technique that adaptively optimizes node connections. However, we observe that the effectiveness of GSL often comes at the cost of a dramatic expansion in edge count, resulting in significant storage and computational overhead.
In this work, we reveal that this limitation stems from the prevalent use of similarity-based edge construction, which predominantly connects highly similar neighbors based on their embeddings, introducing substantial structure redundancy. To address this, we propose a novel Informative Graph Structure Learning method (InGSL), which jointly considers both similarity and diversity in edge construction by incorporating a mutual-information-guided learning strategy. Notably, InGSL serves as a plug-in module that can be seamlessly integrated into existing GSL frameworks. Through extensive experiments on six representative GSL methods, we demonstrate that InGSL achieves significant performance improvements at a reduced number of edges.

---


### 159. [Training-Free Occluded Text Rendering via Glyph Priors and Attention-Guided Semantic Blending](https://arxiv.org/abs/2605.16810)

**<font color=#1a73e8>作者：</font>** Jingqi Hou, Hongtian Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a training-free framework for occluded text rendering with a pretrained FLUX.1-dev backbone. The task requires a model to render recognizable typography and place an occluding object over the intended text region. This setting remains difficult for existing text-to-image generators: the occluder often drifts away from the text, while the text may be distorted or appear to float on top of the occluding object. To address this problem, we propose a restarted dual-stream inference framework that decouples text-layout preservation from occluder insertion. A Base Stream provides a clean typographic reference and same-step key/value (K/V) features, while the Edit Stream is conditioned on the occlusion prompt. We further adopt the spectral glyph-prior idea from FreeText and adapt it to stabilize the target text structure during early-to-mid denoising. In the reasoning pass, our method localizes the target text, estimates a text-band region from token-conditioned attention and glyph support, and derives an anchor-aware hard fusion mask for the occluder. In the final edit pass, generation restarts from the same initial noise and applies hard mask-guided image-token K/V replacement at selected attention sites, preserving the Base layout outside the mask while injecting the occluder appearance from the Edit Stream inside the mask. Experiments on representative occluded text scenarios demonstrate substantially improved text readability and competitive occlusion alignment, yielding more stable object-on-text compositions without any model fine-tuning.

---


### 160. [Jacobian-Guided Anisotropic Noise Reshaping for Enhancing Representation Utility under Local Differential Privacy](https://arxiv.org/abs/2605.16812)

**<font color=#1a73e8>作者：</font>** Youngmok Ha, Viktor Schlegel, Yidan Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While Local Differential Privacy (LDP) serves as a foundational primitive for distributed data collection, its stringent noise injection requirement often leads to severe degradation in data utility. This degradation stems from the task-agnostic nature of conventional LDP mechanisms, which inject noise uniformly across all dimensions regardless of their relative importance to the downstream objective. To address this issue, we propose a novel approach that mitigates noise in task-relevant subspaces of the data representation. Our method identifies task-critical subspaces via the Jacobian matrix of the public downstream model, selectively attenuates noise along those dimensions, and reshapes the isotropic noise of standard LDP into an anisotropic distribution. This method preserves the uniform per-dimension privacy budget while heterogeneously modulating noise impact across dimensions, thereby substantially enhancing data utility. Furthermore, our approach generalizes to both linear and non-linear models and integrates seamlessly with existing mechanisms. Extensive experiments on CIFAR-10-C (Brightness corruption at the highest severity level 5) demonstrate that integrating our approach improves the utility of PrivUnit2 and PrivUnitG by approximately 20\% at $\epsilon=7.5$. The source code is available at \url{this https URL}.

---


### 161. [Universal Graph Backdoor Defense: A Feature-based Homophily Perspective](https://arxiv.org/abs/2605.16815)

**<font color=#1a73e8>作者：</font>** Mengting Pan, Fan Li, Chen Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Graph neural networks (GNNs) have achieved remarkable success in relational learning. However, their vulnerability to graph backdoor attacks (GBAs) poses a significant barrier to broader adoption in high-stakes applications. Despite recent advances in graph backdoor defense (GBD), existing methods primarily focus on subgraph-based GBAs, relying on the assumption that poisoned target nodes are explicitly connected to subgraph triggers. Our empirical results reveal that such structure-centric approaches fail to defend against emerging feature-based GBAs that preserve graph topology. Therefore, in this paper, we study a novel problem of universal graph backdoor defense. First, we investigate the shared effects of both attack types from a feature-based homophily perspective, which characterizes local feature consistency between nodes and their neighborhoods. Thorough theoretical and empirical analyses demonstrate that, regardless of trigger mechanisms, backdoors induced by GBAs exhibit lower feature-based homophily than clean nodes, indicating a discrepancy in local feature similarity. Motivated by this insight, we propose to leverage node-level local feature consistency, modeled by a neighbor-aware reconstruction loss, to distinguish backdoors from clean nodes. Then, a robust training strategy is developed to eliminate trigger effects while reducing noise induced by detection uncertainty. Extensive experiments demonstrate that our framework significantly degrades the attack success rate and maintains competitive clean accuracy under both subgraph-based and feature-based attacks.

---


### 162. [Observation-Aligned Mask Priors for Learning Physical Dynamics from Authentic Occlusions](https://arxiv.org/abs/2605.16818)

**<font color=#1a73e8>作者：</font>** Chiyuan Ma, Zihan Zhou, Tianshu Yu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning physical dynamics directly from incomplete observations is challenging because authentic occlusions are structured, sample-dependent, and often missing not at random, whereas existing methods typically rely on heuristic masking rules or predefined mask distributions. We propose Observation-Aligned Mask Priors, a framework that learns the distribution of authentic observation masks and uses it to construct context-query partitions for training from incomplete data. Specifically, we pretrain a Bayesian Flow Network (BFN) on binary observation masks to capture real occlusion topologies, then guide BFN sampling with a globally normalized cross-entropy objective to generate sample-specific masks aligned with each sparse observation. The intersection between the guided mask and the observed mask defines the context, and the remaining observed entries become query targets for a diffusion-based reconstruction model. We show that this intersection-based partitioning gives every valid observed dimension a strictly positive probability of being queried, preventing zero-query dead zones and local generative collapse. Experiments on three real-world oceanographic datasets with authentic satellite occlusions, across resolutions up to 256$\times$256, show consistent improvements over strong diffusion baselines in MSE and PSNR. These results demonstrate that learning mask priors from authentic occlusions is an effective alternative to heuristic masking for learning from incomplete physical observations without access to fully observed fields.

---


### 163. [AgentKernelArena: Generalization-Aware Benchmarking of GPU Kernel Optimization Agents](https://arxiv.org/abs/2605.16819)

**<font color=#1a73e8>作者：</font>** Sharareh Younesian, Wenwen Ouyang, Sina Rafati 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> GPU kernel optimization is increasingly critical for efficient deep learning systems, but writing high-performance kernels still requires substantial low-level expertise. Recent AI coding agents can iteratively read code, invoke compilers and profilers, and refine implementations, yet existing kernel benchmarks evaluate single LLM calls rather than full agent workflows, and none include both kernel-to-kernel optimization and unseen-configuration generalization testing. We present AgentKernelArena, an open-source benchmark for measuring AI coding agents on GPU kernel optimization. The benchmark contains 196 tasks spanning HIP-to-HIP optimization, Triton-to-Triton optimization, and PyTorch-to-HIP translation, and evaluates complete agent workflows in isolated workspaces using gated compilation, correctness, and performance checks, centralized scoring and an unseen-configuration generalization protocol that tests whether optimizations transfer to input configurations the agent never observed. Across production agents including Cursor Agent, Claude Code, and Codex Agent, we find near-perfect compilation and high correctness rates on most task categories, with the strongest configurations achieving mean speedups of up to 6.89x on PyTorch-to-HIP, 6.69x on HIP-to-HIP, and 2.13x on Triton-to-Triton tasks. Our unseen-configuration evaluation shows that HIP-to-HIP and Triton-to-Triton optimizations largely transfer to unseen input shapes, while PyTorch-to-HIP exhibits substantial correctness drops, indicating that agents generating kernels from scratch frequently hardcode shape-specific assumptions. AgentKernelArena is designed as a modular, extensible framework for rigorous evaluation of agentic GPU kernel optimization across agents, tasks, and hardware targets.

---


### 164. [Atoms as Language: VQ-Atom: Semantic Discretization for Molecular Representation Learning](https://arxiv.org/abs/2605.16823)

**<font color=#1a73e8>作者：</font>** Takayuki Kimura  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular representation learning has become a central approach in AI-driven drug discovery, yet existing molecular tokenizations such as SMILES remain largely syntactic and do not naturally align with chemically meaningful substructures. In this work, we introduce VQ-Atom, a semantic discretization framework that converts continuous atom-level graph representations into discrete tokens corresponding to local chemical environments. Using graph neural network embeddings and vector quantization, atoms are assigned to codebook entries representing chemically meaningful atomic contexts. These discrete tokens define a molecular language suitable for Transformer-based pretraining.
We evaluate VQ-Atom in protein-ligand interaction prediction under a protein-cold split setting without relying on 3D structural information. Experimental results show that VQ-Atom consistently improves predictive performance compared to conventional tokenization approaches, suggesting that semantically grounded discretization can substantially enhance molecular representation learning. Our findings indicate that token design itself plays a critical role in enabling effective language modeling for chemistry.

---


### 165. [Voices in the Loop: Mapping Participatory AI](https://arxiv.org/abs/2605.16827)

**<font color=#1a73e8>作者：</font>** Rashid Mushkani  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Participatory approaches to artificial intelligence are increasingly documented across public, civic, and humanitarian settings, but evidence about how participation is organized remains fragmented. This paper reports on the construction of an open repository and interactive atlas of participatory AI initiatives, using records harmonized from Maga~na and Shilton's Trustworthy AI corpus, and additional audited cases from research and practice. We contribute three elements. First, we specify a reproducible protocol for discovery, vetting, harmonization, geocoding, provenance tracking, and release-based publication of participatory AI records. Second, we report corpus-level patterns in geography, participation tiers, lifecycle loci, organizational form, verification status, and remaining documentation gaps. Documented initiatives remain concentrated in a small number of countries, while participation is most often coded at problem formulation, evaluation, and governance rather than model development or training. Third, we show how the atlas operationalizes a design and governance framework for participatory-by-default AI infrastructures through versioned releases, record-linked issue and annotation channels, schema feedback workflows, and redaction or restricted-disclosure requests. The atlas is intended to support comparative research, policy learning, and community scrutiny through a living inventory that can be updated, contested, and reused.

---


### 166. [Constrained Code Generation with Discrete Diffusion](https://arxiv.org/abs/2605.16829)

**<font color=#1a73e8>作者：</font>** Lize Shao, Michael Cardei, Zichen Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion models are a powerful, emerging paradigm for code generation. They construct programs through iterative refinement of partially corrupted token sequences and enable parallel token refinement. Importantly, this paradigm exposes a global program state at each denoising step, which provides a natural intervention point for enforcing program-level functionality and security constraints, guiding the generation before the final code is committed. Building on this observation, the paper introduces Constrained Diffusion for Code (CDC), a training-free neurosymbolic inference framework that integrates constraint satisfaction directly into the reverse denoising process. CDC augments the base discrete diffusion sampler with constraint-aware denoising operators that combine mathematical optimization with program analysis to identify constraint-relevant regions of the intermediate program state and locally adjust the denoising trajectory, steering generation toward feasible programs while remaining close to the base model. Across code generation benchmarks, CDC consistently improves constraint satisfaction in functional correctness, security, and even syntax, outperforming discrete diffusion and autoregressive baselines with less corrective computation and more localized edits.

---


### 167. [CompactAttention: Accelerating Chunked Prefill with Block-Union KV Selection](https://arxiv.org/abs/2605.16839)

**<font color=#1a73e8>作者：</font>** Jiwon Song, Dongwon Jo, Beomseok Kang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chunked prefill has become a widely adopted serving strategy for long-context large language models, but efficient attention computation in this regime remains challenging. Existing sparse attention methods are primarily designed for one-shot prefill and do not translate efficiently to chunked prefill: block-sparse kernels lose efficiency when the query length is limited by the chunk size, while fine-grained pattern search becomes costly when repeated over the accumulated KV cache at every chunk. QUOKA, a recent method that directly targets chunked prefill, avoids sparse-kernel overhead but relies on query-subsampled, token-level KV selection, which can miss query-specific KV entries and introduce explicit KV-copy overhead. To address these limitations, we propose CompactAttention, a chunked-prefill attention mechanism based on Block-Union KV Selection. CompactAttention treats 2D block-sparse masks as KV-selection signals rather than direct sparse-kernel execution plans, and converts them into GQA-aware per-group KV block tables through Q-block union and intra-group union. This construction produces the minimal block tables that preserve all KV blocks selected by the input masks under paged execution constraints, enabling selected KV blocks to be accessed in place without explicit KV compaction. On LLaMA-3.1-8B-Instruct, CompactAttention maintains accuracy close to dense attention on the RULER benchmark while delivering up to 2.72$\times$ attention speedup at 128K context length under chunked prefill.

---


### 168. [RTI-Bench: A Structured Dataset for Indian Right-to-Information Decision Analysis](https://arxiv.org/abs/2605.16843)

**<font color=#1a73e8>作者：</font>** Joy Bose  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> India's Right to Information Act, 2005 gives every citizen the right to demand information from public authorities, yet in practice most people cannot make sense of the dense administrative language used in Central Information Commission (CIC) decisions, let alone predict whether an appeal is worth filing. This paper introduces RTI-Bench, a structured dataset of CIC decisions with outcome labels, exemption citations, IRAC-style reasoning components, and procedural timelines. To the best of our knowledge it is the first publicly released structured dataset for Indian RTI administrative decisions. The dataset draws from two sources: 1,218 cases from a publicly available instruction-response corpus (with structured fields added through rule-based extraction), and 298 CIC decision PDFs collected directly from the Commission portal, spanning five commissioners and three document format generations from 2023 to 2026. Label coverage reaches 89% on the instruction-response corpus. For the PDF subset of 239 primary decisions, coverage is 51% in this first release. A random sample of 50 labelled cases was manually reviewed, yielding a label precision of 95.3%. A zero-shot Mistral 7B baseline on 100 cases gives 57.3% accuracy and 37.0% macro-F1 on outcome prediction, well above the majority-class baseline of 14.3% macro-F1. RTI-Bench is available at this https URL

---


### 169. [Artificial Adaptive Intelligence: The Missing Stage Between Narrow and General Intelligence](https://arxiv.org/abs/2605.16844)

**<font color=#1a73e8>作者：</font>** Boris Kriuk  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Between the narrow systems we deploy and the general intelligence we speculate about lies an entire regime of machine behavior that has never received its own name. This monograph argues that this regime is not empty: it is where meta-learning, neural architecture search, AutoML, continual learning, evolutionary computation, and physics-informed modeling have quietly converged on a common principle, namely the steady removal of the human from the loop of parameter specification. We name this regime Artificial Adaptive Intelligence (AAI) and define it operationally: a system exhibits AAI to the extent that it requires no human-specified tunable hyperparameters while maintaining competitive performance across a diverse distribution of tasks. To make the definition quantitative, we introduce an adaptivity index that measures progress along an axis orthogonal to scale, combining the fraction of hyperparameters absorbed by the system with the performance ratio against a task-specialized baseline. We develop the principle of parametric minimality and ground it in the minimum description length framework, showing that the appropriate hyperparameter count is data-determined rather than designer-determined. We then organize the field around three pathways to minimality: data- and task-aware configuration, structural and evolutionary morphing, and in-training self-adaptation. We analyze their stability, convergence, and governance implications, and illustrate them through case studies spanning aerospace design, financial regime detection, turbulence modeling, ecological dynamics, and vision-language systems. The thesis is that the path from ANI to AGI passes through AAI, and that naming this stage changes what we measure, what we build, and what we call a success.

---


### 170. [Thinking with Patterns: Breaking the Perceptual Bottleneck in Visual Planning via Pattern Induction](https://arxiv.org/abs/2605.16848)

**<font color=#1a73e8>作者：</font>** Yichang Jian, Boyuan Xiao, Zhenyuan Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Planning from raw visual input remains a significant challenge for current Vision-Language Models (VLMs), when the complexity of input is beyond their one-step perception capability. Motivated by recent advances in Thinking with Images (TWI), a reasonable solution is to decompose the perception process into simpler steps by iteratively acquiring and incorporating local visual evidence. However, even though current VLMs are well-trained in general TWI ability, their perceptual bottleneck in the planning domain remains. To tackle this challenge, we formulate TWI as a tool to gradually build and reflect an accurate internal world model. We find that the resulting training-free planning strategy enables VLMs to solve tasks that are far beyond their initial capabilities, at the cost that too many TWI operations would significantly increase the computational overhead. To further improve efficiency, we propose Pattern Inference, a novel TWI strategy enabling VLMs to actively recognize known visual patterns in the new tasks and directly infer local world model structures. To obtain these patterns, we propose Pattern Induction, an online inductive learning strategy treating visual patterns as composite and reusable experts, which are autonomously discovered and optimized from experience. Experimental evaluations in FrozenLake, Crafter and CubeBench domains show that our approaches achieve a desirable balance between accuracy and efficiency.

---


### 171. [Lifelong LaCAM with Local Guidance for Lifelong MAPF](https://arxiv.org/abs/2605.16855)

**<font color=#1a73e8>作者：</font>** Tomoki Arita, Keisuke Okumura  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Local guidance has recently proven to be a powerful driver of empirical performance in real-time, suboptimal multi-agent pathfinding (MAPF), improving the scalable configuration-based solver LaCAM. By injecting informative spatiotemporal cues around each agent, local guidance mitigates congestion, reduces waiting, and remains scalable enough even with tight time budgets, yielding state-of-the-art performance for one-shot MAPF. This study asks whether the same benefits can be lifted to the lifelong setting (LMAPF), where tasks arrive continuously and improvements in per-step plans can increase task completion throughput over long horizons. We propose LLLG, a Lifelong version of LaCAM enhanced with Local Guidance, which employs a receding-horizon windowed planning framework and warm-starts guidance from the previous solution at each timestep. Our method scales effectively, maintains high throughput even in compact, dense environments, and surpasses existing planners, thereby pushing the frontier of real-time, lifelong MAPF.

---


### 172. [VGGT-CD: Training-Free Robust Registration for 3D Change Detection](https://arxiv.org/abs/2605.16859)

**<font color=#1a73e8>作者：</font>** Wei Zhang, Songhua Li, Yihang Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D change detection from multi-view images is essential for urban monitoring, disaster assessment, and autonomous driving. However, existing methods predominantly operate in the 2D domain, where viewpoint variations are mistaken for physical changes and depth is unavailable. While visual geometry foundation models like VGGT rapidly produce dense point clouds from unposed images, independent per-epoch reconstruction encounters fundamental obstacles: unpredictable inter-epoch scale ambiguity, registration-change paradox where scene changes corrupt alignment, and pervasive edge-flying noise. To address these challenges, we present VGGT-CD, a training-free pipeline decoupling cross-temporal registration from dynamic-change interference. In the Coarse Stage, sparse keyframe joint inference establishes a unified metric space and yields an initial Sim(3) prior. In the Fine Stage, dense reconstructions are purified by isolating static-background correspondences. A closed-form centroid alignment refines the translation while locking scale and rotation, using a residual self-check to mathematically guarantee non-degradation. Evaluated on an 11-scene benchmark from the World Across Time dataset, VGGT-CD reduces Absolute Trajectory Error by 44% outdoors and 59% indoors. It completes registration over 6 times faster, producing high-purity 3D change maps without task-specific training.

---


### 173. [PhysioSeq2Seq: A Hybrid Physiological Digital Twin and Sequence-to-Sequence LSTM for Long-Horizon Glucose Forecasting in Type 1 Diabetes](https://arxiv.org/abs/2605.16860)

**<font color=#1a73e8>作者：</font>** Phat Tran, Neville Mehta, Clara Mosquera-Lopez 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate long-horizon glucose forecasting is critical for automated insulin delivery systems, which help people with type 1 diabetes (T1D) manage their glucose and avoid dangerous hypoglycemia. However, standard recursive long short-term memory (LSTM) networks suffer from systematic negative bias at longer horizons due to error compounding, while purely mechanistic ordinary differential equation (ODE) models fail to generalize across individuals when parameterized at the population level. We propose PhysioSeq2Seq, a hybrid architecture that combines patient-specific physiological modeling with a sequence-to-sequence (Seq2Seq) LSTM. For each glucose segment, twin matching searches a population of 300 parameterized digital twins to identify the best-fitting physiological match from a 3-hour continuous glucose monitoring (CGM) history. The 10 internal ODE state variables of the matched twin are injected as exogenous covariates into both the encoder and decoder of the Seq2Seq LSTM. This simultaneous 48-step prediction strategy eliminates recursive error compounding, while the ODE features provide a physics-grounded constraint that bounds long-horizon drift within physiologically plausible ranges. PhysioSeq2Seq was trained on CGM and insulin data from 348 participants in the Type 1 Diabetes Exercise Initiative (T1DEXI) dataset and evaluated on 74 held-out participants. At the 240-minute horizon, PhysioSeq2Seq achieves a mean absolute error of 39.28 mg/dL and a mean error of -10.62 mg/dL, reducing bias by 13.89 mg/dL over the recursive LSTM and reducing mean absolute error by 28.62 mg/dL over the ODE-based digital twin. These results show that eliminating architectural feedback and injecting patient-matched physiological states is an effective and clinically meaningful strategy for long-horizon glucose forecasting in T1D.

---


### 174. [Prefix-Adaptive Block Diffusion for Efficient Document Recognition](https://arxiv.org/abs/2605.16861)

**<font color=#1a73e8>作者：</font>** Mingxu Chai, Ziyu Shen, Chenyu Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Block Diffusion Models (BDMs) support parallel generation, flexible-length output, and KV caching, making them promising for efficient document parsing. However, existing BDMs bind denoising and cache commitment to fixed block boundaries: parallelism shrinks during intra-block denoising, while generated tokens cannot be cached until the whole block is completed. Moreover, intra-block bidirectional denoising conflicts with inter-block autoregression, creating inconsistent information flow that can challenge structure-sensitive recognition. We propose the Prefix-Adaptive Block Diffusion Model (PA-BDM), which replaces intra-block bidirectional denoising with causal denoising from prefix to suffix and treats the block size as a maximum candidate range rather than a fixed commitment unit. PA-BDM uses Confidence-gated Structural Loss (CSL) to build low-entropy prefixes before extending training to longer continuations. During inference, Progressive Prefix Commitment (PPC) then dynamically commits the longest reliable prefix into the KV cache and resets the next candidate range from the updated prefix, restoring a large parallel decoding space at each step. Experiments show that the 3B PA-BDM achieves higher recognition scores on several benchmarks and improves inference throughput by 71.6\% over the 2.5B MinerU-Diffusion.

---


### 175. [MixSD: Mixed Contextual Self-Distillation for Knowledge Injection](https://arxiv.org/abs/2605.16865)

**<font color=#1a73e8>作者：</font>** Jiarui Liu, Lechen Zhang, Yongjin Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) is widely used to inject new knowledge into language models, but it often degrades pretrained capabilities such as reasoning and general-domain performance. We argue this forgetting arises because fine-tuning targets from humans or external systems diverge from the model's autoregressive distribution, forcing the optimizer to imitate low-probability token sequences. To address this problem, we propose MixSD, a simple external-teacher-free method for distribution-aligned knowledge injection. Instead of training on fixed targets, MixSD constructs supervision dynamically by mixing tokens from two conditionals of the base model itself: an expert conditional that observes the injected fact in context, and a naive conditional that reflects the model's original prior. The resulting supervision sequences preserve the factual learning signal while remaining substantially closer to the base model's distribution. We evaluate MixSD on two synthetic corpora that we construct to study factual recall and arithmetic function acquisition in a controlled setting, together with established benchmarks for open-domain factual question answering and knowledge editing. Across multiple model scales and settings, MixSD consistently achieves a better memorization-retention trade-off compared to SFT and on-policy self distillation baselines, retaining up to 100% of the base model's held-out capability while maintaining near-perfect training accuracy, whereas standard SFT retains as little as 1%. We further show that MixSD produces substantially lower-NLL supervision targets under the base model and reduces harmful movement along Fisher-sensitive parameter directions. These results suggest that aligning supervision with the model's native generation distribution is a simple and effective principle for knowledge injection that mitigates catastrophic forgetting.

---


### 176. [HAD: Hallucination-Aware Diffusion Priors for 3D Reconstruction](https://arxiv.org/abs/2605.16873)

**<font color=#1a73e8>作者：</font>** Xi Liu, Weiwei Sun, Zhou Ren 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion priors have recently demonstrated strong capability in enhancing the quality of sparse-view 3D reconstruction by augmenting training views at novel viewpoints, but they inevitably introduce hallucinated content -- artifacts inconsistent with the input views -- into the final 3D model. To address this challenge, we propose Hallucination-Aware Diffusion prior (HAD), which estimates pixel-wise hallucination score maps for augmented images by leveraging multi-view reasoning capabilities from a feedforward novel view synthesis (NVS) network pre-trained on large-scale 3D data. These hallucination scores enable selective masking of unreliable pixels during the progressive 3D reconstruction procedure, preventing the introduction of non-existent artifacts into the 3D model. To further enhance performance, we create multiple versions of augmented images at each novel view by conditioning the diffusion prior on different input views, which are then fused into a final image that leverages the broader context across all input views. We show that our method substantially reduces hallucination artifacts in diffusion-assisted 3D reconstruction, thereby achieving state-of-the-art performance across multiple benchmarks on novel view synthesis. Our project are publicly available at \href{this https URL}{project website}.

---


### 177. [Reasoning Can Be Restored by Correcting a Few Decision Tokens](https://arxiv.org/abs/2605.16874)

**<font color=#1a73e8>作者：</font>** Changshuo Shen, Leheng Sheng, Yuxin Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large reasoning models (LRMs) substantially outperform their base LLM counterparts on challenging reasoning benchmarks, yet it remains poorly understood where base models go wrong during token-by-token generation and how to narrow this gap efficiently. We study the base-reasoning gap through quantifying token-level distributional disagreement between a base model and a stronger reasoning model using likelihood-based divergences. Across benchmarks, we find that the reasoning advantage is highly sparse and concentrates on a small set of early, planning-related decision tokens. For instance, on Qwen3-0.6B, only ~8% of generated tokens account for the salient disagreement, and these tokens concentrate early in the response, are strongly enriched in planning-related decisions (17x), and coincide with high base-model uncertainty -- suggesting that base models fail mainly at early planning points that steer the subsequent reasoning trajectory. Building on these findings, we propose disagreement-guided token intervention, a simple inference-time delegation scheme that performs a one-token takeover by the reasoning model only at high-disagreement positions and immediately switches back to the base model. With a small intervention budget, this sparse delegation substantially recovers and can even surpass the performance of a same-size reasoning model on challenging reasoning tasks. Code is available at this https URL.

---


### 178. [Zero-Shot Faithful Textual Explanations via Directional-Derivative Influence on Predictions](https://arxiv.org/abs/2605.16877)

**<font color=#1a73e8>作者：</font>** Toshinori Yamauchi, Hiroshi Kera, Kazuhiko Kawamoto  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot textual explanations aim to make image classifiers more transparent by probing their internal representations, without relying on task-specific supervision or LVLMs. However, existing methods often miss the features that truly drive the prediction, resulting in limited \textit{faithfulness} to the evidence underlying the model's decision. To address this, we propose FaithTrace. Motivated by the idea that faithful explanations should describe concepts that strongly influence the prediction, FaithTrace directly measures how much the representation induced by the explanation changes the class logit. We introduce an influence score, computed as the directional derivative of the class logit along the text-induced direction in the classifier's feature space, and use it as a proxy for faithfulness. Moreover, we extend this influence score into quantitative evaluation metrics, helping fill the gap in faithfulness evaluation for textual explanations. Experiments show that FaithTrace yields more faithful explanations than baselines, facilitating a more accurate understanding of the model. The code will be publicly released.

---


### 179. [Towards Generalized Image Manipulation Localization via Score-based Model](https://arxiv.org/abs/2605.16879)

**<font color=#1a73e8>作者：</font>** Yunfei Wang, Bo Du, Zhe Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the rapid evolution of synthetic media, Image Manipulation Localization (IML) has emerged as a critical component in multimedia forensics for ensuring the integrity of digital content. However, generalization remains a core challenge, as existing discriminative methods typically learn a fixed decision boundary that tends to overfit to specific training artifacts and fails to adapt to unseen manipulation types. To address this, we propose DiffIML, a novel framework that introduces score-based generative modeling to IML. Diverging from the direct estimation of hard boundaries, DiffIML approximates the score function, the gradient of the log-likelihood, to capture the intrinsic geometric topology of mask distributions. This paradigm leverages structural priors to iteratively recover coherent masks from noise, thereby circumventing the brittleness associated with discriminative models. Under this formulation, diffusion models serve as an effective numerical solver for the learned score this http URL ensure practicality, we respectively resolve the efficiency and stability bottlenecks of standard diffusion by: (1) utilizing a Lightweight Mask-Specific VAE for fast latent-space process and a decoupled architecture with a lightweight denoising UNet, (2) edge supervision and error prior to mitigate error accumulation during sampling. Extensive experiments of two distinct protocols on eight non-generative and three generative benchmarks demonstrate that DiffIML consistently outperforms state-of-the-art methods, yielding remarkable generalization improvements on diverse unseen datasets. The code will be publicly available.

---


### 180. [Virtual Nodes Guided Dynamic Graph Neural Network for Brain Tumor Segmentation with Missing Modalities](https://arxiv.org/abs/2605.16880)

**<font color=#1a73e8>作者：</font>** Sha Tao, Jiao Pan, Yu Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal magnetic resonance imaging (MRI) is crucial for brain tumor segmentation, with many methods leveraging its four key modalities to capture complementary information for effective sub-region analysis. However, the absence of several modalities is very common in practice, leading to severe performance degradation in existing full-modality segmentation methods. Limited by the structured data model, recent works often adopt a multi-stage training strategy for full-modality and missing-modality scenarios, which increases training costs and inadequately addresses the interference of miss. In this work, we propose a graph-based one-stage framework for robust brain tumor segmentation with missing modalities. Specifically, we introduce modality-specific virtual nodes that serve as supplementary information sources to compensate for missing modalities. To enhance model robustness against arbitrary modality combinations, we leverage the inherent flexibility of graph networks to devise a dynamic connection strategy. This mechanism dynamically adjusts the adjacency matrix based on modality availability, preserving beneficial information flow while mitigating interference effects caused by missing modalities. Furthermore, we enhance the graph network through heterogeneous weight matrices, enhancing its adaptability to multimodal scenarios. Extensive experiments on the BRATS-2018 and BRATS-2020 datasets demonstrate that our method outperforms the state-of-the-art methods on almost all subsets of incomplete modalities.

---


### 181. [E-PMQ: Expert-Guided Post-Merge Quantization with Merged-Weight Anchoring](https://arxiv.org/abs/2605.16882)

**<font color=#1a73e8>作者：</font>** Wenjun Wang, Yanggan Gu, Shuo Cai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Low-resource deployment constraints have made model quantization essential for deploying neural networks while preserving performance. Meanwhile, model merging has become an increasingly practical low-resource strategy for integrating multiple task- or domain-specialized experts into a single model without joint training or multi-model serving. Together, quantization and model merging enable an efficient low-resource deployment pipeline by integrating multiple experts into one low-bit model. We formulate this setting as Post-Merge Quantization (PMQ). We show that directly applying post-training quantization (PTQ) to a merged model is unreliable because two distinct deviations are coupled: the quantization deviation introduced by low-bit reconstruction and the expert-relative merging deviation inherited from model merging. To mitigate these deviations, we propose E-PMQ, an expert-guided PMQ framework that uses source expert weights to provide expert- guided output targets during layer-wise calibration, together with merged-weight anchoring to stabilize the calibration and preserve the integrated behavior of the merged model. On CLIP-ViT-B/32 eight-task merging, E-PMQ improves 4-bit GPTQ from 65.0% to 73.6% under Task Arithmetic and from 69.1% to 74.8% under TIES-Merging. On harder settings, E-PMQ improves GPTQ from 34.8% to 76.7% on 20-task CLIP-ViT-L/14 and from 78.26% to 83.34% on FLAN-T5- base GLUE. These results demonstrate that E-PMQ enables effective post-merge quantization and low-bit deployment.

---


### 182. [SE-GA: Memory-Augmented Self-Evolution for GUI Agents](https://arxiv.org/abs/2605.16883)

**<font color=#1a73e8>作者：</font>** Shilong Jin, Lanjun Wang, Zhuosheng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autonomous Graphical User Interface (GUI) agents often struggle with multi-step tasks due to constrained context windows and static policies that fail to adapt to dynamic environments. To address these limitations, this work proposes the Self-Evolving GUI Agent (SE-GA), a novel framework that integrates hierarchical memory structures with an iterative self-improvement mechanism. At the core of our approach is Test-Time Memory Extension (TTME), which facilitates long-term planning by dynamically retrieving episodic, semantic, and experiential memories to provide salient contexts during inference. To ensure continuous learning, we introduce Memory-Augmented Self-Evolution (MASE), which is a training pipeline that adopts the data collected by TTME to stabilize and enhance the agent's foundational policy. Extensive evaluations across both offline and online benchmarks demonstrate SE-GA achieves state-of-the-art performance, reaching success rates of 89.0\% on ScreenSpot and 75.8\% on the challenging AndroidControl-High dataset. Furthermore, significant improvements on the AndroidWorld benchmark highlight the superior generalization to dynamic environments. Open source code: this https URL

---


### 183. [Mind the Gap: Learning Modality-Agnostic Representations with a Cross-Modality UNet](https://arxiv.org/abs/2605.16887)

**<font color=#1a73e8>作者：</font>** Xin Niu, Enyi Li, Jinchao Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-modality recognition has many important applications in science, law enforcement and entertainment. Popular methods to bridge the modality gap include reducing the distributional differences of representations of different modalities, learning indistinguishable representations or explicit modality transfer. The first two approaches suffer from the loss of discriminant information while removing the modality-specific variations. The third one heavily relies on the successful modality transfer, could face catastrophic performance drop when explicit modality transfers are not possible or difficult. To tackle this problem, we proposed a compact encoder-decoder neural module (cmUNet) to learn modality-agnostic representations while retaining identity-related information. This is achieved through cross-modality transformation and in-modality reconstruction, enhanced by an adversarial/perceptual loss which encourages indistinguishability of representations in the original sample space. For cross-modality matching, we propose MarrNet where cmUNet is connected to a standard feature extraction network which takes as inputs the modality-agnostic representations and outputs similarity scores for matching. We validated our method on five challenging tasks, namely Raman-infrared spectrum matching, cross-modality person re-identification and heterogeneous (photo-sketch, visible-near infrared and visible-thermal) face recognition, where MarrNet showed superior performance compared to state-of-the-art methods. Furthermore, it is observed that a cross-modality matching method could be biased to extract discriminant information from partial or even wrong regions, due to incompetence of dealing with modality gaps, which subsequently leads to poor generalization. We show that robustness to occlusions can be an indicator of whether a method can well bridge the modality gap.

---


### 184. [Tensor Channel Equivariant Graph Neural Networks for Molecular Polarizability Prediction](https://arxiv.org/abs/2605.16891)

**<font color=#1a73e8>作者：</font>** Jean Philip Filling, Daniel Franzen, Michael Wand  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a tensor-channel equivariant graph neural network for direct prediction of molecular polarizability tensors. Building on the efficient PaiNN architecture, we augment the hidden representation with explicit symmetric rank-2 tensor channels aligned with the decomposition of polarizability into isotropic and anisotropic components. In contrast to approaches that construct tensor outputs only at readout, our model propagates tensor structure throughout message passing using geometrically motivated tensor bases. This yields a target-aligned architecture for tensor-valued molecular prediction.
On optimized QM7-X geometries, the proposed model achieves lower full-tensor and anisotropic error than both a PaiNN-style readout baseline and a dielectric MACE baseline under matched training conditions and at nearly identical parameter count. In this controlled setting, it also outperforms MACE while remaining substantially faster at inference. Ablation studies show that the gain does not arise from increased capacity alone, but from the combination of explicit tensor propagation and a traceless target parameterization matched to the anisotropic part of the polarizability tensor. Among the tensor bases considered, the strongest results are obtained from interactions between learned directional features, indicating that these are particularly effective for modeling molecular polarizability. Rotational equivariance tests further confirm that all compared models are numerically equivariant, so the observed improvements are attributable to better learning of the target tensor itself. Overall, our results show that for structured tensor-valued targets, propagating target-aligned tensor features can outperform both readout-only tensor construction and a more general higher-order equivariant model in the present training setting.

---


### 185. [JSPG: Dynamic Dictionary Filtering via Joint Semantic-Pinyin-Glyph Retrieval for Chinese Contextual ASR](https://arxiv.org/abs/2605.16896)

**<font color=#1a73e8>作者：</font>** Shilin Zhou, Zhenghua Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Contextual Automatic Speech Recognition (ASR) faces challenges with large-scale keyword dictionaries, as excessive irrelevant candidates introduce noise that degrades accuracy. To address this, dynamic filtering typically uses a base ASR model to generate preliminary hypotheses, followed by semantic text retrievers to fetch a concise subset of relevant keywords. However, this approach frequently fails in Chinese ASR. Base models often produce homophonic or near-homophonic errors that preserve the phonetic cues of the target keywords but severely distort their semantic meaning, rendering standard semantic retrievers ineffective. To resolve this, we propose a filtering framework that jointly integrates Semantic, Pinyin, and Glyph features (JSPG). Pinyin effectively retrieves targets based on phonetic similarity, while glyph provides complementary structural cues to filter out numerous irrelevant homophones inherent in Chinese. To bridge the gap between character-level pinyin/glyph metrics and sequence-level filtering, we introduce an extended Smith-Waterman algorithm that computes similarity scores between the N-best hypothesis sequences and keywords. Experiments on the Aishell-1 and RWCS-NER datasets demonstrate that JSPG significantly outperforms single-feature baselines. Furthermore, downstream contextual ASR models guided by JSPG achieve substantial improvements in keyword recognition accuracy.

---


### 186. [LASAR: Towards Spatio-temporal Reasoning with Latent Cognitive Map](https://arxiv.org/abs/2605.16899)

**<font color=#1a73e8>作者：</font>** Jinzhou Tang, Sidi Liu, Waikit Xiu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A fundamental challenge in embodied AI is verifying if agents build internal models of spatial structure or merely learn to mimic task-specific expert trajectories. This is critical as foundational approaches rooted in action-centric tasks (e.g., VLN) and reasoning-centric tasks (e.g., EQA) often share a common limitation: they lack a learning signal that forces them to encode fine-grained spatial relationships (like topology or distance) over long-range, fragmented experiences. To address this, we first propose LASAR, an architecture featuring a dual-memory system designed to maintain both episodic experiences and a semantic cognitive map. We then introduce Spatio-temporal Contextual Representation Learning (ST-CRL), a contrastive objective designed to train this architecture. ST-CRL leverages spatio-temporal cues from cognitive queries generated through annotated spatio-temporal context in simulation to build sample pairs, thereby forming the internal cognitive map from the agent's experiences. Experiments demonstrate that our method achieves 2\%-3.5\% gains in both zero-shot generalization on standard VLN-CE and VSI-Bench benchmarks. We also demonstrate that our proposed cognitive map has high self-consistency.

---


### 187. [WOW-Seg: A Word-free Open World Segmentation Model](https://arxiv.org/abs/2605.16903)

**<font color=#1a73e8>作者：</font>** Danyang Li, Tianhao Wu, Bin Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open world image segmentation aims to achieve precise segmentation and semantic understanding of targets within images by addressing the infinitely open set of object categories encountered in the real world. However, traditional closed-set segmentation approaches struggle to adapt to complex open world scenarios, while foundation segmentation models such as SAM exhibit notable discrepancies between their strong segmentation capabilities and relatively weaker semantic understanding. To bridge these discrepancies, we propose WOW-Seg, a Word-free Open World Segmentation model for segmenting and recognizing objects from open-set categories. Specifically, WOW-Seg introduces a novel visual prompt module, Mask2Token, which transforms image masks into visual tokens and ensures their alignment with the VLLM feature space. Moreover, we introduce the Cascade Attention Mask to decouple information across different instances. This approach mitigates inter-instance interference, leading to a significant improvement in model performance. We further construct an open world region recognition test benchmark: the Region Recognition Dataset (RR-7K). With 7,662 classes, it represents the most extensive category-rich region recognition dataset to date. WOW-Seg attains strong results on the LVIS dataset, achieving a semantic similarity of 89.7 and a semantic IoU of 82.4. This performance surpasses the previous SOTA while using only one-eighth the parameter count. These results underscore the strong open world generalization capabilities of WOW-Seg. The code and related resources are available at this https URL.

---


### 188. [AIM: Adversarial Information Masking for Faithfulness Evaluation of Saliency Maps](https://arxiv.org/abs/2605.16905)

**<font color=#1a73e8>作者：</font>** Chia-Ying Hsieh, Hsin-Yuan Fang, Chun-Shu Wei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-hoc saliency methods are widely used to interpret deep neural networks, but their faithfulness is difficult to evaluate reliably. Existing evaluations mask features according to saliency-induced feature ordering and measure performance degradation, but this degradation can be confounded by the masking operator: zero masking may create out-of-distribution artifacts, while interpolation-based masking may preserve residual predictive information. We propose Adversarial Information Masking (AIM), a saliency-guided adversarial feature replacement framework for evaluating both saliency-map faithfulness and masking-operator reliability. AIM replaces selected features with values from an adversarial counterpart of the input and compares degradation under complementary masking orders. We assess reliability using random-attribution bias and stability of explanation-method faithfulness rankings. Experiments on image, audio, and EEG tasks suggest that AIM reduces masking-induced bias compared with zero and interpolation-based masking, while revealing modality-dependent differences between signed and unsigned attributions.

---


### 189. [VGGT-Occ: Geometry-Grounded and Density-Aware Gated Fusion for 3D Occupancy Prediction](https://arxiv.org/abs/2605.16911)

**<font color=#1a73e8>作者：</font>** Xun Chen, Tianchen Deng, Rui Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D semantic occupancy prediction requires accurate 2D-to-3D feature lifting, yet current methods restrict camera geometry to initial projections. Subsequent operations like offset learning, attention weighting, and cross-camera aggregation remain geometry-agnostic, ignoring essential physical constraints. We propose VGGT-Occ, a framework that embeds geometric tokens throughout the entire pipeline. We introduce Projection-Aware Deformable Attention (PA-DA) to inject geometry into all attention stages. PA-DA projects 3D offsets back to image planes and leverages the projection Jacobian as an additive bias to suppress unreliable observations. Features are then integrated through a view-quality semantic gate for cross-view consistency. To optimize both efficiency and performance, we employ a sequential coarse-to-fine decoder with gated fusion, where low-resolution features are refined into higher resolutions, allocating computation by information density while substantially reducing decoder cost. Extensive evaluations demonstrate the effectiveness and accuracy of our approach. On SurroundOcc-nuScenes, VGGT-Occ achieves 33.00\% IoU and 21.08\% mIoU ($T{=}1$), and 33.64\% IoU and 21.43\% mIoU with $T{=}2$ inference, outperforming existing methods, with only ${\sim}41$M trainable parameters in the occupancy head. Code will be released publicly.

---


### 190. [A Lightweight QR-assisted Zero-knowledge Identification Protocol For Secure Authentication](https://arxiv.org/abs/2605.16912)

**<font color=#1a73e8>作者：</font>** Hüseyin Bodur  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This study proposes a lightweight Zero-Knowledge authentication model supported by QR codes. The approach is based on the Schnorr authentication protocol and provides an additional security layer against replay attacks through nonce and timestamp mechanisms. The proof data generated by the prover is embedded within a QR code and transmitted to the verifier. Thus, the system enables verification of knowledge of the secret key without revealing it. Simulation results show that proof generation and verification times under a 256-bit security level are in the millisecond range. Additionally, the proof size remains constant at approximately 0.5 KB, making it suitable for practical applications in terms of QR code capacity. The findings indicate that the proposed model is applicable in mobile and low-resource systems in terms of both security and performance.

---


### 191. [HighSync: High-Quality Lip Synchronization via Latent Diffusion Models](https://arxiv.org/abs/2605.16918)

**<font color=#1a73e8>作者：</font>** Saeed Firouzi Daghigh, Majid Iranpour Mobarekeh, Mostafa Alavi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present HighSync, an end-to-end diffusion-based framework for high-fidelity lip synchronization that generates photorealistic talking-face videos aligned with arbitrary input audio. Existing approaches consistently struggle to reconcile image quality with synchronization accuracy, producing either visually degraded outputs or temporally inconsistent lip movements. HighSync addresses both challenges simultaneously and, to our knowledge, is the first lip sync model to operate natively at 512*512 resolution, positioning it as a viable solution for professional production environments such as the film and broadcast industries. Central to our approach is the identification and systematic elimination of a data leakage phenomenon that has silently undermined temporal modeling in prior work, preventing models from developing a genuine dependence on the audio signal. Comprehensive evaluations across both perceptual quality and synchronization accuracy metrics confirm that HighSync achieves state-of-the-art performance on both fronts. Source code, pre-trained models, and supplementary video results are publicly available at: this https URL

---


### 192. [Motion Cues from Image-based Point Tracking for LiDAR Scene Flow Estimation](https://arxiv.org/abs/2605.16922)

**<font color=#1a73e8>作者：</font>** Youngdong Jang, Gyeongrok Oh, Jong Wook Kim 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDAR scene flow estimation is essential for autonomous driving, as it provides 3D motion for each point. Self-supervised approaches use static-dynamic classification to mitigate the imbalance between static and dynamic points, deriving targeted supervision. However, existing methods rely on sparse geometric observations for this classification, making them vulnerable to data sparsity and occlusions. The resulting noisy labels provide incorrect motion guidance and degrade scene flow learning. To address this, we introduce TrackCue, a tracking-guided framework for improving dynamic object representation in LiDAR scene flow estimation. In particular, TrackCue repurposes point tracking to obtain dense image-space trajectories anchored to LiDAR points, providing motion cues beyond sparse geometric observations. Furthermore, we present a visually consistent motion compensation strategy that compares the tracked trajectories with ego-induced rigid trajectories in the image plane, effectively isolating true object motion from ego-induced apparent motion. To transfer these isolated motion cues back to the LiDAR domain, we perform visual motion cue lifting, which associates ego-compensated image trajectories with LiDAR points for static-dynamic label refinement. As a result, TrackCue produces more accurate static-dynamic classification and provides more reliable supervision for scene flow learning. Experimental results show that TrackCue significantly improves the precision and F1 score of dynamic labels, leading to performance gains in self-supervised scene flow estimation.

---


### 193. [Neuroscience-inspired Staged Representation Learning with Disentangled Coarse- and Fine-Grained Semantics for EEG Visual Decoding](https://arxiv.org/abs/2605.16923)

**<font color=#1a73e8>作者：</font>** Xiang Gao, Hui Tian, Yanming Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Decoding visual information from electroencephalography (EEG) signals remains a fundamental challenge in brain-computer interfaces and medical rehabilitation. Existing EEG visual decoding methods mainly focus on learning a single global EEG embedding for cross-modal alignment, but they largely overlook the staged and hierarchical characteristics of human visual processing. To address this limitation, we propose a neuroscience-inspired staged representation learning framework that reformulates EEG visual decoding as a stage-specific representation decomposition problem. The proposed framework organizes EEG representation learning into three complementary phases: low-level visual representation learning, high-level semantic representation learning, and integrative information fusion. To strengthen semantic modeling, we further introduce a multimodal dual-level semantic learning mechanism that separates coarse label-level semantics from fine image-level visual-semantic information. In addition, semantic latent channels are introduced as computational representation channels generated from observed visual EEG signals, expanding the channel-level semantic representation space for structured semantic abstraction and cross-modal alignment. Extensive experiments on the THINGS-EEG benchmark demonstrate that the proposed method achieves superior performance under subject-dependent zero-shot evaluation and improved exact retrieval under subject-independent zero-shot evaluation. Additional analyses, including layer-wise retrieval, temporal accumulation, expanded multi-image retrieval, and ablation studies, further support the effectiveness of staged decomposition and structured semantic modeling. These results suggest that explicitly modeling staged perceptual, semantic, and integrative representations provides an effective neuroscience-inspired framework for EEG-based visual decoding.

---


### 194. [P2GS: Physical Prior-guided Gaussian Splatting for Photometrically Consistent Urban Reconstruction](https://arxiv.org/abs/2605.16925)

**<font color=#1a73e8>作者：</font>** Kota Shimomura, Hidehisa Arai, Tsubasa Takahashi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has recently emerged as a powerful explicit representation enabling fast, high-fidelity rendering, making it a promising foundation for closed-loop simulators and perception models in autonomous driving. However, conventional 3DGS implicitly assumes consistent exposure and tone mapping across views. Real driving data violates this assumption due to heterogeneous camera pipelines and dynamic outdoor illumination, baking exposure discrepancies and sensor noise into the radiance field and producing artifacts and inconsistent illumination especially in static backgrounds crucial for realistic simulation. These issues are amplified in autonomous driving, where sparse viewpoints, varying exposures, and outdoor lighting interact, while prior work mainly targets dynamic-object reconstruction and overlooks cross-view photometric consistency. To address this limitation, we introduce P2GS, a physically consistent Gaussian Splatting framework that jointly decomposes a view-invariant linear HDR radiance field, per-view exposure scales, and tone-mapping functions from only LDR images without HDR supervision. P2GS employs a unified optimization strategy grounded in the physical image-formation process, enforcing relative-exposure consistency and HDR-domain radiance regularization. This yields a radiance field robust to inter-camera illumination differences while preserving the real-time efficiency of standard 3DGS. Experiments across real and simulated driving environments show that P2GS matches or surpasses prior methods in LDR reconstruction while providing substantially improved photometric consistency, reliable exposure normalization, and physically coherent illumination across diverse scenes.

---


### 195. [From Static Risk to Dynamic Trajectories: Toward World-Model-Inspired Clinical Prediction](https://arxiv.org/abs/2605.16927)

**<font color=#1a73e8>作者：</font>** Pujun Feng, Xiaoyu Guo, Seyed Ehsan Saffari 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical decision-making is a feedback system where risk estimates influence treatment, which in turn changes disease trajectories, and both shape clinicians' measurement practices. Static prediction often fails clinically: models trained on observational care logs conflate disease biology with clinician behavior, particularly under treatment confounder feedback and irregular or informative observation. This Review focuses on intervention-aware disease trajectory modeling in clinical AI--methods estimating patient-specific longitudinal disease evolution and assessing trajectory changes under alternative treatments. We organize the field around six linked components: three decision tasks (factual forecasting, counterfactual estimation, policy evaluation) and three data-generating mechanisms (disease evolution, treatment assignment, observation process) that determine identifiability. We present the first unified framework bridging forecasting, counterfactual trajectories, and policy evaluation across discrete/continuous time, explicitly addressing treatment assignment, time-varying confounding, and observation bias. We synthesize key method families (multistate/joint models, temporal point-process, deep sequence architectures, longitudinal causal inference), map them to relevant components, and align evaluation with claim strength via overlap diagnostics, uncertainty quantification, off-policy robustness, and target-trial validation. This synthesis advances benchmark prediction to decision-grade clinical evidence, enabling treatment-sensitive individualized futures, pre-deployment policy stress-testing, and safer closed-loop learning health systems that adapt/abstain when evidence is insufficient.

---


### 196. [Full Attention Strikes Back: Transferring Full Attention into Sparse within Hundred Training Steps](https://arxiv.org/abs/2605.16928)

**<font color=#1a73e8>作者：</font>** Yanke Zhou, Yiduo Li, Hanlin Tang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context inference in large language models is bottlenecked by the quadratic cost of full attention. Existing efficient alternatives often rely either on native sparse training or on heuristic token eviction, creating an undesirable trade-off among efficiency, training cost, and accuracy. In this work, we show that full-attention LLMs are already intrinsically sparse and can be transformed into highly sparse models with only minimal adaptation. Our approach is built on three observations: (1) only a small subset of attention heads truly requires full long-context processing; (2) long-range retrieval is governed primarily by a low-dimensional subspace, allowing relevant tokens to be retrieved efficiently with a 16-dimensional indexer; and (3) the useful token budget is strongly query-dependent, making dynamic top-$p$ selection more suitable than fixed top-$k$ sparsification. Based on these insights, we propose RTPurbo, which retains the full KV cache only for retrieval heads and introduces a lightweight token indexer for sparse attention. By exploiting the model's intrinsic sparsity, RTPurbo achieves sparsification with only a few hundred training steps. Experiments on long-context benchmarks and reasoning tasks show that RTPurbo preserves near-lossless accuracy while delivering substantial efficiency gains, including up to a 9.36$\times$ prefill speedup at 1M context and about a 2.01$\times$ decode speedup. These results suggest that strong sparse inference can be obtained from standard full-attention training without expensive native sparse pretraining.

---


### 197. [Emulating the Forced Response of Climate Models with Flow Matching](https://arxiv.org/abs/2605.16929)

**<font color=#1a73e8>作者：</font>** Graham Clyne, Julia Kaltenborn, Peer Nowack 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Global climate models are essential tools to simulate past and potential future pathways of climate change, as well as associated climate impacts. Shared Socioeconomic Pathways (SSPs) describe a range of future scenarios of global economic and demographic development. These SSPs are intrinsically linked to changes in climate forcings, the external drivers, such as greenhouse gas and aerosol emissions, which in turn lead to the human impact on the energy balance of the Earth over time. These forcings are fundamental boundary conditions in climate models in order to gain insight into the potential climatic impacts of these changes described by each SSP. Running a climate model, however, is extremely computationally expensive, conflicting with the need for large ensembles of simulations for each model to give, e.g., more robust estimates in the presence of internal variability (the inherent, chaotic fluctuations within the climate system) and scenario uncertainty. Recent research has demonstrated the ability to capture climate model dynamics using machine learning when conditioned on forcings from different climatic scenarios. We here train a Deep Learning (DL) model on multiple SSPs and successfully generate scenarios unseen during training. Our emulator is validated against MESMER-M, a statistical emulator of land surface temperature. Our research demonstrates the capacity to generate such changing climate states in response to a variety of simultaneous climate forcings (e.g., carbon dioxide, methane, nitrous oxide, sulphate aerosols, and ozone). In particular, our ablation studies underline a need to include a range of different forcings to represent long-term atmospheric trends with a DL emulator.

---


### 198. [DEVIS-GRPO: Unleashing GRPO on Dynamic Extreme View Synthesis](https://arxiv.org/abs/2605.16937)

**<font color=#1a73e8>作者：</font>** Yi Zuo, Huimin Wu, Lingling Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Trajectory-controlled video generation has become essential for controllable video generation. While current methods perform well under small-view camera motions, they degrade significantly with large-view motions. Existing solutions for extreme-view synthesis typically require dedicated video pairs, demanding substantial annotation effort. To address these limitations, we propose Dynamic Extreme VIew Synthesis-GRPO (DEVIS-GRPO), a GRPO-based framework for trajectory-controlled video generation, the first online policy gradient method for extreme view video generation. Central to our approach is a novel sampling strategy: Accumulative Dynamic Extreme VIew Synthesis (ADEVIS), which achieves large-view camera motions by progressively accumulating small-view increments. This method delivers two key advantages: 1) enhanced training efficiency, as it eliminates the need to warm-start the policy model by collecting expensive paired large-view videos, and 2) increased sampling diversity, achieved by flexibly varying trajectory configurations. Finally, we designed a multi-level consistency-quality reward function to select high-quality samples for model optimization. Experiments on the Kubric-4D, iPhone, and DL3DV datasets demonstrate our method's superiority. On Kubric-4D, we achieve relative improvements of 21.57% in PSNR and 7.31% in SSIM over the second-best method in non-occlusion areas. On iPhone, LPIPS is reduced by 18.56%.

---


### 199. [Edit-GRPO: A Locality-Preserving Policy Optimization Framework for Image Editing](https://arxiv.org/abs/2605.16951)

**<font color=#1a73e8>作者：</font>** Shaodong Xu, Zexian Li, Zhendong Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A fundamental challenge in image editing lies in preserving spatial locality: edits should improve targeted content without inadvertently altering surrounding regions. However, most optimization-based editing approaches treat images as holistic entities, causing global policy updates that undermine locality and introduce undesired context changes. We observe that this issue stems from a mismatch between localized editing intent and globally applied optimization signals. Motivated by this insight, we propose Edit-GRPO, preserving Locality while optimizing image editing, a locality-preserving policy optimization framework that explicitly decouples editing and preservation objectives. By assigning region-specific optimization signals to edit and non-edit areas, Edit-GRPO aligns policy updates with the spatial structure of editing tasks, enabling localized improvements while maintaining global visual coherence. This design effectively suppresses common artifacts such as context distortion and boundary inconsistency. Extensive experiments across diverse image editing scenarios demonstrate that Edit-GRPO significantly improves locality preservation while maintaining strong editing performance compared to existing optimization-based methods, validating the generality and effectiveness of the proposed framework.

---


### 200. [Latent Action Control for Reasoning-Guided Unified Image Generation](https://arxiv.org/abs/2605.16961)

**<font color=#1a73e8>作者：</font>** Fuxiang Zhai, Sixiang Chen, Yingjin Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models can encode visual understanding and image generation within a shared backbone, yet understanding does not automatically translate into control: models may infer objects, relations, or knowledge cues but fail to instantiate them in the generated image. We propose Latent Action Control (LAC), which makes reasoning actionable by representing it as hidden continuous actions inside a unified generator. Given a prompt, LAC rolls out a role-structured latent trajectory for planning, internal visual drafting, diagnosis, and refinement, and injects these actions into the hidden stream that conditions flow-based generation, without producing reasoning tokens or intermediate images. Since such action trajectories are unobserved, LAC learns them through prior-guided variational latent action alignment from training-only rendered semantic priors, draft image features, and supervised halting signals, followed by Latent-Flow GRPO to align the latent-to-image rollout with terminal visual feedback. This provides a control path from inferred relations, bindings, and knowledge cues to the generation process. Instantiated on BAGEL-7B-MoT, LAC consistently improves compositional and knowledge-grounded generation across GenEval, WISE, and T2I-CompBench, with the largest gains on spatial relations, attribute binding, and world-knowledge-sensitive prompts. Ablations and latent interventions show that the learned action trajectory is consumed by the generator, suggesting that unified generation benefits when understanding is not only encoded, but made actionable during generation.

---


> [!TIP]
> 当前位于：**151-200**（第 4/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-619](./part-13.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
