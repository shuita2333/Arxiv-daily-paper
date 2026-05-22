# 📦 其他研究 | 2026年05月23日

> 本类共 **347** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-347**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-347**

---

### 301. [Self-Policy Distillation via Capability-Selective Subspace Projection](https://arxiv.org/abs/2605.22675)

**<font color=#1a73e8>作者：</font>** Guangya Hao, Yitong Shang, Yunbo Long 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-distillation bootstraps large language models (LLMs) by training on their own generations. However, existing methods either rely on external signals to curate self-generated outputs (e.g., correctness filtering, execution feedback, and reward search), which are costly and unavailable for the best-performing frontier models, or skip curation entirely and train on all raw outputs, an approach that is often domain-specific and hard to generalize. Both also share a deeper weakness that self-generated outputs entangle task-relevant capability with others, such as stylistic patterns, formatting artifacts, and model-specific errors, diluting the signal for the specific capability one aims to improve. In this paper, we propose Self-Policy Distillation (SPD), which achieves generalizable, capability selective without any external signal. Specifically, SPD extracts a low-rank capability subspace from the model's own gradients on correctness-defining tokens, projects key-value (KV) activations into this subspace during self-generation, and fine-tunes on the resulting raw outputs with standard next-token prediction loss. Through extensive experiments across code generation, mathematical reasoning, and multiple-choice QA, we show that SPD achieves up to 13% improvement over state-of-the-art self-distillation methods without external signals and up to 16% improvement over pre-trained baselines. Notably, SPD demonstrates superior generalizability, achieving 15% better performance under out-of-domain generalization settings.

---


### 302. [Slimmable ConvNeXt: Width-Adaptive Inference for Efficient Multi-Device Deployment](https://arxiv.org/abs/2605.22677)

**<font color=#1a73e8>作者：</font>** Janek Haberer, Jon Eike Wilhelm, Olaf Landsiedel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deploying vision models across devices with varying resource constraints, or even on a single device where available compute fluctuates due to battery state, thermal throttling, or latency deadlines, typically requires training and maintaining separate models. Width-adaptive inference addresses this by training a single set of shared weights containing multiple nested subnetworks of increasing capacity, but prior CNN-based approaches required switchable batch normalization, while recent scalable methods have focused on Vision Transformers. We present Slimmable ConvNeXt, which shows that ConvNeXt's modern design, specifically LayerNorm and inverted bottlenecks, makes it particularly suited for channel-width slimming, eliminating the normalization overhead of classical slimmable networks and producing a simpler training pipeline than both prior CNN and ViT approaches. On ImageNet-1k, Slimmable ConvNeXt-T with 3 subnetworks achieves 80.8% top-1 accuracy at 4.5 GMACs and 77.4% at 1.2 GMACs, trained from scratch for 600 epochs. At comparable compute, this exceeds HydraViT's 6-head subnetwork (78.4% at 4.6 GMACs) by 2.4 percentage points and its 3-head configuration (73.0% at 1.3 GMACs) by 4.4 percentage points, while also outperforming MatFormer-S (78.6%) and SortedNet-S (78.2%) at the same GMACs. Scaling to Slimmable ConvNeXt-B further improves maximum accuracy to 82.8% at 15.35 GMACs.

---


### 303. [Swift Sampling: Selecting Temporal Surprises via Taylor Series](https://arxiv.org/abs/2605.22678)

**<font color=#1a73e8>作者：</font>** Dahye Kim, Bhuvan Sachdeva, Karan Uppal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While most frames in long-form video are redundant, the critical information resides in temporal surprises: moments where the actual visual features deviate from their predicted evolution. Inspired by the human brain's predictive coding, we introduce Swift Sampling, an elegant, training-free frame selection algorithm that automatically identifies high-information moments in a video. Specifically, we model a video as a differentiable trajectory in the visual latent space and compute the velocity and acceleration of its features. Then, we apply Taylor expansion to project the expected path of subsequent frames. Frames that diverge sharply from this predicted manifold are identified as temporally surprising frames and selected for sampling. Unlike prior training-free methods that rely on auxiliary networks or video-specific hyperparameter tuning, Swift Sampling is incredibly lightweight, adding only 0.02x additional computational cost over baseline making it 30x cheaper overhead than leading baselines. Across three long-video question answering benchmarks and 10 different downstream tasks, Swift Sampling outperforms uniform sampling and prior query-agnostic baselines. It is especially powerful for long videos with limited frame budgets improving accuracy by up to +12.5 points.

---


### 304. [Forecasting Scientific Progress with Artificial Intelligence](https://arxiv.org/abs/2605.22681)

**<font color=#1a73e8>作者：</font>** Sean Wu, Pan Lu, Yupeng Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) is increasingly embedded in scientific discovery, yet whether it can anticipate scientific progress remains unclear. To study this question, we introduce a temporally grounded evaluation framework for forecasting scientific progress under controlled knowledge constraints. We present CUSP (Cutoff-conditioned Unseen Scientific Progress), a multi-disciplinary and event-level benchmark that evaluates scientific forecasting in AI systems through feasibility assessment, mechanistic reasoning, generative solution design, and temporal prediction. Across 4,760 scientific events, we observe systematic and domain-dependent limitations in current frontier models. While models can identify plausible research directions from competing candidates, they fail to reliably predict whether scientific advances will be realized and systematically misestimate when they will occur. Performance is highly heterogeneous across domains, with the timing of AI progress more predictable than advances in biology, chemistry, and physics. Performance is largely insensitive to whether events occur before or after the training cutoff, suggesting these limitations cannot be explained solely by knowledge exposure in training data. Under controlled information access, additional pre-cutoff knowledge improves performance but does not close the gap to full-information settings, which becomes more pronounced for high-citation advances. Models also exhibit systematic overconfidence and strong response biases, indicating unreliable uncertainty estimation. Taken together, current AI systems fall short as predictive tools for scientific progress. Access to prior knowledge does not translate into reliable forecasting, and performance benefits more from post-event information than from forward-looking prediction.

---


### 305. [Posterior Collapse as Automatic Spectral Pruning](https://arxiv.org/abs/2605.22691)

**<font color=#1a73e8>作者：</font>** Johannes Hirn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We show that posterior collapse in $\beta$-VAEs implements automatic spectral pruning. A latent mode collapses if its contribution to reconstruction is below the cutoff set by $\beta$. Equilibrium solutions with different $\beta$ thus reveal a cascade of collapses as latent modes decouple from least to most useful.
We derive this as a consequence of the loss via a Landau stability analysis. We define a latent-rescaling-invariant order parameter that ranks active latent modes and whose collapse thresholds identify which effective variables to inspect first.
In the linear Gaussian case, the collapse spectrum, utility spectrum, and normalized PCA spectrum coincide, and each collapse follows a mean-field law. We test these predictions on the WorldClim dataset.

---


### 306. [Improving Viewpoint-Invariance and Temporal Consistency for Action Detection](https://arxiv.org/abs/2605.22695)

**<font color=#1a73e8>作者：</font>** Yannick Porto, Renato Martins, Thomas Chalumeau 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Viewpoint change invariance and action temporal consistency are critical aspects for the effective deployment of human action detection of untrimmed videos. Existing appearance-based video detection methods often struggle with limited viewpoint diversity during training, while motion-based detection approaches frequently fail to model fine-grained temporal relationships across consecutive motion windows. This paper introduces a novel two-stage action detection approach designed to improve both view-invariance and global temporal coherence properties. In the first stage, we extract motion features from augmented virtual viewpoints, solely used at training. Then, the second stage introduces a new view-invariant, multi-scale temporal encoder based on selective state-space sequence modelling to aggregate information across viewpoints and time scales. Experiments on PKU-MMD and BABEL benchmarks demonstrate that this approach significantly outperforms state-of-the-art methods in all considered splits. Code and trained models are available at: this https URL

---


### 307. [Cross-Domain Human Action Recognition from Multiview Motion and Textual Descriptions](https://arxiv.org/abs/2605.22697)

**<font color=#1a73e8>作者：</font>** Yannick Porto, Renato Martins, Thomas Chalumeau 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robustness to domain changes is a key capability for effective deployment of human action recognition systems in real-world scenarios, where action categories at inference can present important domain shifts or even unseen actions from training. In this context, improving the recognition capabilities of Zero-Shot Action Recognition models (ZSAR), without requiring strong annotation efforts, remains a central challenge. Most ZSAR approaches assume that actions are observed under geometric conditions similar to those seen during training. In practice, variations in human body orientation and camera viewpoint add a significant domain gap in ZSAR, substantially limiting generalization to novel action-motion combinations. In this context, this paper presents a novel orientation-aware action recognition approach with improved cross-domain capabilities. Our approach combines motion cues of multiple camera viewpoints and text descriptions of human actions in the training phase. We present a new orientation-aware motion encoding network to learn different motion features, and adapt a specific orientation-aware text prompt to match the corresponding features at inference. Extensive experiments demonstrate that the proposed method consistently improves ZSAR performance across different recognition benchmarks, outperforming recent state-of-the-art zero-shot approaches on NTU-RGB+D, BABEL, NW-UCLA, and on two surveillance datasets. In addition, the learned representations exhibit strong transfer learning capabilities, yielding competitive performance on both cross-domain and same-domain recognition of seen actions. Code and trained models are available at: this https URL

---


### 308. [Clipping Bottleneck: Stabilizing RLVR via Stochastic Recovery of Near-Boundary Signals](https://arxiv.org/abs/2605.22703)

**<font color=#1a73e8>作者：</font>** Shuo Yang, Jinda Lu, Chiyu Ma 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a central paradigm for scaling LLM reasoning, yet its optimization often suffers from training instability and suboptimal convergence. Through a systematic dissection of clipping-based GRPO-style objectives, we identify the rigid clipping decision induced by hard clipping as a key practical bottleneck in the studied RLVR setups. Specifically, our analysis suggests that informative signals can lie in the near-boundary region just beyond the clipping threshold, and are therefore discarded by the standard hard-clipping rule. Notably, once this bottleneck is precisely identified, even simple stochastic perturbations at the boundary can recover meaningful performance gains. Building on this finding, we propose Near-boundary Stochastic Rescue (NSR), a minimal, plug-and-play modification that stochastically retains these slightly out-of-bound tokens to recover lost signals. While NSR, via stochastic sampling, can be interpreted as inducing an implicit gradient decay in expectation, our ablations reveal that its stochastic, boundary-local rescue mechanism is consistently more effective than deterministic gradient decay. Validated by extensive experiments across model sizes from 7B to 30B and both dense and MoE architectures, as a plug-and-play solution, NSR substantially improves training stability and delivers consistent gains over strong baselines such as DAPO and GSPO.

---


### 309. [Tokenization with Split Trees](https://arxiv.org/abs/2605.22705)

**<font color=#1a73e8>作者：</font>** Craig W. Schmidt, Michael Krumdick, Adam Wiemerslage 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Tokenization with Split Trees (ToaST), a subword tokenization method that directly optimizes compression under a new recursive inference procedure. ToaST greedily splits each pretoken into a full binary tree using precomputed byte n-gram counts, independent of any vocabulary. Given a vocabulary, inference recursively descends each split tree and emits the first in-vocabulary node reached on each path. Vocabulary selection is formulated as an Integer Program (IP) that minimizes the total token count over all split trees under this inference procedure. The Linear Programming (LP) relaxation is near-integral in practice, yielding provably near-optimal vocabularies, with training time empirically scaling quadratically in the number of split trees. On English text, ToaST reduces token counts by more than 11% compared to BPE, WordPiece, and UnigramLM at vocabulary sizes of 40,960 and above, reducing the number of inference tokens for models using this tokenizer, thus extending the effective context length. ToaST also uses common single-byte tokens less frequently than these baselines, leading to a substantial improvement in Renyi efficiency. In experiments training 1.5B parameter language models, ToaST achieves the highest CORE score, outperforming baselines by 2.6%--7.6%, with significance for two of three, and scoring best on 13 of 22 individual tasks.

---


### 310. [Beyond the Org Chart: AI and the Transformation of Invisible Work](https://arxiv.org/abs/2605.22707)

**<font color=#1a73e8>作者：</font>** Stephanie Rosenthal, Shamsi Iqbal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An increasing number of news and research articles report that AI adoption is allowing professionals to blur and extend the boundaries of their corporate roles. With the goal of understanding how work processes might be changing in an AI-forward company, we interviewed 24 product-focused individuals at a large technology firm about how AI has impacted their own work, their work within their product team, and their professional interactions. Our conversations suggest that AI is not only changing formal role responsibilities and collaborations between those roles, but also changing informal cultural practices like professional mentoring that are key to helping professionals settle in their positions, stay engaged with their work, and grow their careers. Some of these changes are positive, such as smoother collaboration between peers, but other changes are more nuanced and put the typical career growth opportunities, like receiving feedback from professional networks and promoting leadership and mentorship, at risk. We propose steps that AI companies can take to make the invisible work more visible. Additionally, we propose efforts that individuals and leaders can take to support their colleagues through AI transformation while preserving healthy company cultures that support diverse thinking, collaboration, and informal interactions.

---


### 311. [TriSweep: A Four-Drone Swarm Framework for Electromagnetic Side-Channel Analysis](https://arxiv.org/abs/2605.22709)

**<font color=#1a73e8>作者：</font>** Eric Yocam, Varghese Vaidyan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Electromagnetic (EM) side-channel analysis traditionally assumes a stationary, close-proximity probe - a threat model that underestimates aerial adversaries. TriSweep is a simulation framework that designs and evaluates a four-drone swarm architecture for autonomous standoff EM-SCA of embedded microcontrollers at 0.25-1.5 m. Three spatially specialized collector drones - Anchor (full-spectrum), Mask Probe (mask-register loading leakage), and Cipher Probe (masked SubBytes output leakage) - feed a stationary Accumulator drone that performs coherent combining (+4.8 dB SNR gain) and second-order mask cancellation via a centered product of the two spatially separated leakage streams. Evaluated against three real ANSSI ASCAD datasets (ATmega8515 masked AES-128 and 50/100-sample desynchronized variants), the framework achieves a simulated key rank of 18 +/- 1.7 (five-seed) at 0.25 m on the primary masked dataset. Profiling-trace cross-correlation alignment reduces single-drone rank from 89 to 21 on the 100-sample-jitter variant, demonstrating compensation for drone hover vibration. A two-channel CNN in the Accumulator converges to a loss of 0.454 (vs. random baseline 5.545) and improves rank on desynchronized datasets. No physical hardware has been fabricated; prototype construction is the planned next step.

---


### 312. [Abstraction for Offline Goal-Conditioned Reinforcement Learning](https://arxiv.org/abs/2605.22711)

**<font color=#1a73e8>作者：</font>** Clarisse Wibault, Alexander Goldie, Antonio Villares 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Markov Decision Processes (MDPs) often exhibit significant redundancy due to symmetries and shared structure across state-goal pairs in real-world Goal-Conditioned Reinforcement Learning (GCRL). While hierarchical policies have been motivated for horizon reduction via temporal abstraction in offline GCRL, we demonstrate that hierarchy also enables absolute abstraction. By introducing relativised options as well as distinct representations for different levels of the hierarchy, we demonstrate how an agent can reuse experience across similar contexts of the state-space. Based on this framework, we introduce two simple algorithms for learning relativised options and abstracting from the absolute frame of reference. Our experiments show that such inductive biases significantly improve performance in offline GCRL.

---


### 313. [AnyMo: Geometry-Aware Setup-Agnostic Modeling of Human Motion in the Wild](https://arxiv.org/abs/2605.22715)

**<font color=#1a73e8>作者：</font>** Baiyu Chen, Zechen Li, Wilson Wongso 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As wearable and mobile devices become increasingly embedded in daily life, they offer a practical way to continuously sense human motion in the wild. But inertial signals are highly dependent on the sensing setup, including body location, mounting position, sensor orientation, device hardware, and sampling protocol. This setup dependence makes it difficult to learn motion representations that transfer across devices and datasets, and limits the broader use of wearable IMUs beyond closed-set recognition. We introduce AnyMo, a geometry-aware framework for setup-agnostic human motion modeling. AnyMo uses physics-grounded IMU simulation over dense body-surface placements to generate diverse and plausible synthetic signals, pre-trains a graph encoder from paired synthetic placement views and masked partial observations, tokenizes multi-position IMU into full-body motion tokens, and aligns these tokens with an LLM for motion-language understanding. We evaluate AnyMo on three complementary tasks: zero-shot activity recognition across 14 unseen downstream datasets, cross-modal retrieval, and wearable IMU motion captioning, where it improves average Accuracy/F1/R@2 by 11.7\%/11.6\%/22.6\% on HAR, increases zero-shot IMU-to-text and text-to-IMU retrieval MRR by 15.9\% and 28.6\%, respectively, and improves zero-shot captioning BERT-F1 by 18.8\%. These results support AnyMo as a generalist model for wearable motion understanding in the wild. Project page: this https URL.

---


### 314. [Parametric Modular Answer Set Programs Made Declarative](https://arxiv.org/abs/2605.22716)

**<font color=#1a73e8>作者：</font>** Jorge Fandinno, Yuliya Lierler, Torsten Schaub  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this paper, we explore the concept of modularity in first-order answer set programming (ASP). We introduce a new formalism called parametric modular logic programs, which allows defining subprograms with parameters and intensionality statements. We demonstrate how this formalism can capture the semantics of clingo-programs with collective control, a feature that enables structuring and instantiating subprograms. We provide theoretical foundations for modular ASP, illustrate its usefulness, and connect to traditional non-modular ASP.

---


### 315. [WorldKV: Efficient World Memory with World Retrieval and Compression](https://arxiv.org/abs/2605.22718)

**<font color=#1a73e8>作者：</font>** Jung Yi, Minjae Kim, Paul Hyunbin Cho 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video diffusion models have enabled real-time, action-conditioned world generation. However, sustaining a persistent world, where revisiting a previously seen viewpoint yields consistent content, remains an open problem. Full KV-cache attention preserves this consistency but breaks real-time constraints: memory footprint and attention cost grow linearly with rollout length. Sliding window inference restores throughput but discards long-term consistency. We propose WorldKV, a training-free framework with two components: World Retrieval and World Compression. World Retrieval stores evicted KV-cache chunks in GPU/CPU memory and selectively retrieves scene-relevant chunks via camera/ action correspondence, inserting them back into the native attention window without re-encoding. World Compression prunes redundant tokens within each chunk via key-key similarity to an anchor frame, halving per-chunk storage to fit 2x more history under a fixed budget. On Matrix-Game-2.0 and LingBot- World-Fast, WorldKV matches or exceeds full-KV memory fidelity at roughly 2x the throughput, and is competitive with memory-trained baselines without any fine-tuning. Project Page: this https URL

---


### 316. [The Value of Covariance Matching in Gaussian DDPMs and the Lanczos Sampler](https://arxiv.org/abs/2605.22723)

**<font color=#1a73e8>作者：</font>** Md Sahil Akhtar, Aymane El Gadarri, Vivek F. Farias 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A central error measure in Gaussian DDPMs is the path-space KL divergence between the exact reverse chain and the learned Gaussian reverse process. This quantity is especially relevant for procedures such as classifier guidance, which perturb the entire reverse trajectory rather than only the terminal sample. Prior analyses show that standard isotropic reverse covariances suffer an unavoidable $\Omega(1/T)$ path-KL error as the number of denoising steps $T$ grows. We show that matching the full posterior covariance breaks this barrier, yielding an order-wise improvement that reduces the path KL to $O(1/T^2)$. To make full covariance matching practical, we introduce the Lanczos Gaussian sampler (LGS), a training-free, matrix-free method for sampling from the optimal reverse covariance using only covariance-vector products, which are available through Jacobian-vector products of the posterior mean. LGS avoids dense covariance storage and auxiliary covariance models. We prove that LGS approximation error decays exponentially in the number of Lanczos steps, where each Lanczos step requires a single Jacobian-vector product. Empirically, using only just three such steps improves sample quality over strong diagonal-covariance baselines, including OCM-DDPM, across standard image benchmarks. This identifies full covariance matching as both theoretically valuable and practically accessible for fast DDPM sampling.

---


### 317. [Multiple Neural Operators Achieve Near-Optimal Rates for Multi-Task Learning](https://arxiv.org/abs/2605.22724)

**<font color=#1a73e8>作者：</font>** Adrien Weihs, Hayden Schaeffer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the approximation and statistical complexity of learning collections of operators in a shared multi-task setting, with a focus on the Multiple Neural Operators (MNO) architecture. For broad classes of Lipschitz multiple operator maps, we derive near-optimal upper bounds for approximation and statistical generalization. On the lower-bound side, we establish a curse of parametric complexity and prove corresponding minimax rates. Together, these results show that shared representations across tasks do not increase the overall cost: multi-task operator learning follows the same scaling laws as single operator learning. We also compare MNO with a multi-task extension of DeepONet based on concatenated task inputs and show that, from a worst-case approximation-complexity perspective, both architectures satisfy essentially the same asymptotic rates.

---


### 318. [HarnessAPI: A Skill-First Framework for Unified Streaming APIs and MCP Tools](https://arxiv.org/abs/2605.22733)

**<font color=#1a73e8>作者：</font>** Edwin Jose  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Every Python function deployed as an LLM tool must today exist in two forms: an HTTP endpoint for human-facing clients and CI pipelines, and an MCP tool registration for agent runtimes such as Claude and Cursor. These representations share business logic yet diverge in all the surrounding machinery (routing, validation, serialisation, streaming, and schema maintenance), and they drift apart as the underlying code evolves. We present HarnessAPI, a Python framework that eliminates this duplication by treating a typed skill folder as the single source of truth. From one this http URL plus Pydantic schemas, the framework automatically derives a streaming HTTP endpoint with Server-Sent Events, an interactive OpenAPI/Swagger UI, and a zero-configuration MCP tool, all served from a single process. Dual-mode content negotiation lets the same handler serve SSE-streaming and JSON-returning clients with no handler changes. A dynamic code-generation mechanism ensures Pydantic type annotations propagate correctly to FastMCP's inspection layer, resolving a technical limitation that prevents naive closure-based registration. Measured across six representative skills using cloc, HarnessAPI reduces framework-facing boilerplate by 74% compared with a manually maintained dual-stack implementation (FastAPI server + FastMCP server). HarnessAPI subclasses FastAPI, inheriting its full middleware, dependency-injection, and deployment ecosystem. It is available at this https URL and on PyPI (pip install harnessapi)

---


### 319. [ChronoMedKG: A Temporally-Grounded Biomedical Knowledge Graph and Benchmark for Clinical Reasoning](https://arxiv.org/abs/2605.22734)

**<font color=#1a73e8>作者：</font>** Md Shamim Ahmed, Farzaneh Firoozbakht, Lukas Galke Poech 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Biomedical knowledge graphs (KGs) treat disease associations as static facts, but temporal information is crucial for clinical reasoning, e.g., a symptom diagnostic of one disease at age 3 may imply a different disease at age 13. Existing KGs such as PrimeKG, Hetionet, and iKraph do not encode when a finding becomes clinically relevant over the course of a disease. This limits their usefulness for longitudinal clinical reasoning and retrieval augmentation.
We introduce ChronoMedKG, a temporal biomedical knowledge graph that contains 460,497 evidence-linked triples (filtered from 13M raw extractions) covering 13,431 diseases. Each association is tied to temporal components like onset window or progression stage, which are backed by PMID-traceable evidence and a multi-signal credibility score. The graph is constructed through a disease-autonomous multi-agent pipeline in which multiple frontier LLMs independently extract knowledge from PubMed and PMC literature. Only those relations are kept that are supported by multi-model consensus, survive credibility filtering, as well as ontology alignment.
ChronoMedKG scored 92.7% agreement against Orphadata and adds temporal grounding for 6,250 diseases absent from HPOA, Orphadata, and Phenopackets, including 1,657 Orphanet-coded rare diseases. We further introduce ChronoTQA, a benchmark of 3,341 questions across eight task types (six temporal plus two static controls), with a 12-question supplementary probe. Frontier LLMs lose roughly 30 points moving from static to temporal questions; ChronoMedKG retrieval rescues 47-65% of their long-tail failures, against 17-29% for HPOA-RAG. As such, ChronoMedKG provides a crucial temporal axis for retrieval-augmented clinical systems that was previously absent.

---


### 320. [The Distillation Game: Adaptive Attacks & Efficient Defenses](https://arxiv.org/abs/2605.22737)

**<font color=#1a73e8>作者：</font>** Youssef Allouah, Mahdi Haghifam, Sanmi Koyejo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distillation attacks create a deployment trade-off for model providers: the same outputs that make a model more useful can also make it easier to imitate. We study this trade-off through a minimax game between a utility-constrained teacher and an adaptive student. Our framework yields tractable one-sided response rules: an adaptive evaluation rule in which the student reweights high-value examples, and a teacher-side defense template that suppresses outputs most useful for distillation. From a cheap proxy for example value, we derive Product-of-Experts (PoE), a simple forward-pass-only defense that combines the teacher with a proxy student during generation. Empirically, adaptive evaluation reveals a large passive--adaptive gap: on state-of-the-art defenses, adaptive students recover substantially more capability than passive evaluation suggests on GSM8K and MATH. Under this stronger evaluation, the apparent robustness gap between expensive defenses and PoE narrows considerably, while PoE remains substantially cheaper and preserves higher-quality reasoning traces. Overall, our results suggest that strong distillation remains difficult to stop, and that progress on antidistillation should be judged against adaptive students rather than passive ones. Our code is available at: this https URL.

---


### 321. [Proxy-Based Approximation of Shapley and Banzhaf Interactions](https://arxiv.org/abs/2605.22738)

**<font color=#1a73e8>作者：</font>** Santo M. A. R. Thies, Hubert Baniecki, R. Teal Witter 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Shapley and Banzhaf interactions capture the complex dynamics inherent in modern machine learning applications. However, current estimators for these higher-order interactions trade off between speed and accuracy. To overcome this limitation, we introduce ProxySHAP. ProxySHAP reconciles the high sample efficiency of tree-based proxy models with a principled path to consistency via residual correction. On a theoretical level, we derive a polynomial-time generalization of interventional TreeSHAP to compute exact interaction indices for tree ensembles, successfully bypassing exponential tree-depth dependencies in prior methods. Furthermore, we formally analyze the residual adjustment strategy, characterizing the specific conditions under which Maximum Sample Reuse (MSR) corrects proxy bias without its variance scaling exponentially with interaction size. Extensive benchmarking demonstrates that ProxySHAP sets a new state-of-the-art standard for approximation quality, including in large-scale applications with thousands of features. By achieving the lowest error in both small- and large-budget regimes, ProxySHAP significantly outperforms the prior best estimators ProxySPEX and KernelSHAP-IQ, while also delivering superior performance on downstream explainability tasks.

---


### 322. [Ternary Decision Trees with Locally-Adaptive Uncertainty Zones](https://arxiv.org/abs/2605.22740)

**<font color=#1a73e8>作者：</font>** William Smits  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision trees partition the feature space using hard binary thresholds, assigning identical confidence to instances far from a decision boundary and to those directly on it. We introduce ternary decision trees, which augment each split node with an uncertainty zone of half-width delta centered on the optimal threshold. Instances in this zone receive predictions formed by weighted blending of both child subtrees and are flagged as boundary-uncertain, signaling that downstream applications may treat these predictions differently. Crucially, delta is computed locally at each node from statistics already available during standard CART split finding, requiring no external noise specification. We propose and evaluate five delta-estimation methods: quality-plateau (plateau width of the split criterion curve), class-overlap (empirical class-distribution overlap), gain-ratio (split quality relative to split entropy), node-bootstrap (threshold variance under node-level resampling), and margin (SVM-inspired distance to the nearest cross-class training example). Evaluated across 72 OpenML-CC18 datasets with 5-fold cross-validation, all five methods with probabilistic routing significantly outperform standard CART on decided accuracy (Wilcoxon signed-rank, p < 0.001). The margin method achieves the best efficiency (0.104 accuracy gain per unit of boundary-uncertain flagging rate), wins on 42 of 72 datasets, and requires zero additional hyperparameters. Analysis on three Breiman synthetic benchmarks reveals that margin is self-calibrating on clean data while node-bootstrap and quality-plateau best track theoretical irreducible error. Experiments on four medical and financial datasets demonstrate practical value: on mammography, node-bootstrap achieves +0.71% decided accuracy by flagging 10.8% of screening cases as boundary-uncertain.

---


### 323. [SeqLoRA: Bilevel Orthogonal Adaptation for Continual Multi-Concept Generation](https://arxiv.org/abs/2605.22743)

**<font color=#1a73e8>作者：</font>** Javad Parsa, Enis Simsar, Amir Joudaki 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning enables fast personalization of text-to-image diffusion models, but composing multiple custom concepts remains challenging due to representation interference. Existing modular methods either rely on expensive post-hoc fusion or freeze adaptation subspaces, which limit expressiveness and concept fidelity. To address this trade-off, we propose Sequential regularized LoRA (SeqLoRA), a constrained continual learning framework that jointly optimizes both LoRA factors via bilevel optimization. Theoretically, we establish strong convergence guarantees for our algorithm and model the residual layer activations as a matrix sub-Gaussian process to derive high-probability bounds on catastrophic forgetting. We further prove that learning the LoRA basis from data minimizes residual interference energy more effectively than frozen-basis methods. Experiments on multi-concept image generation demonstrate that SeqLoRA improves identity preservation and scalability across up to 101 concepts, while avoiding costly fusion and reducing attribute interference in composed generations.

---


### 324. [Plug-in Losses for Evidential Deep Learning: A Simplified Framework for Uncertainty Estimation that Includes the Softmax Classifier](https://arxiv.org/abs/2605.22746)

**<font color=#1a73e8>作者：</font>** Berk Hayta, Hannah Laus, Simon Mittermaier 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world sensor-based learning systems require uncertainty estimation that is both reliable and computationally efficient. Evidential Deep Learning (EDL) provides single-pass uncertainty estimation by modeling the class probabilities via Dirichlet distributions, where the Dirichlet parameters are predicted by a learned neural network mapping. However, this approach can lead to computational challenges, as Dirichlet expected objectives are more complex than standard supervised learning losses, complicating their analysis and implementation. We address this issue by approximating the objective of the first-order empirical risk minimization problem induced by EDL with a plug-in loss evaluated at the Dirichlet mean and show that, under mild assumptions, the approximation error decays with growing evidence for a broad class of loss functions, including mean-squared error and cross-entropy loss. As a special case, our analysis provides justification for the use of softmax in the context of uncertainty estimation, since under a particular evidence-to-Dirichlet mapping, our framework includes the standard softmax classifier. We validate the proposed simplified objectives on the Google Speech Commands dataset and show that they achieve predictive accuracy and selective prediction performance comparable to classical EDL, while being simpler to implement using standard deep learning losses and training pipelines. To the best of our knowledge, this empirical analysis is the first to obtain coverage-accuracy trade-offs for speech recognition tasks through EDL.

---


### 325. [Cyber-Physical Anomaly Detection in IoT-Enabled Smart Grids Using Machine Learning and Metaheuristic Feature Optimization](https://arxiv.org/abs/2605.22749)

**<font color=#1a73e8>作者：</font>** Adis Alihodžić, Eva Tuba, Milan Tuba  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern smart grids rely on dense measurement infrastructures, communication links, and intelligent field devices. Although this improves supervision and control, it also increases vulnerability to cyber-physical disruptions. Operators must distinguish physical incidents, such as faults or line disturbances, from malicious actions, such as false data injection or unauthorized command execution. This chapter investigates this problem using the well-known MSU/ORNL Power System Attack Dataset. The proposed method combines machine learning with genetic-algorithm-based feature selection. The objective is twofold: to classify attack and natural events accurately, and to determine whether a reduced set of physically informative PMU/IED measurements can support reliable detection. Several baseline models are evaluated, including logistic regression, RBF-SVM, XGBoost, Random Forest, and Extra Trees. The results show that tree-based ensemble models are the most effective for the considered dataset, with Extra Trees providing the strongest full-feature baseline. After feature selection, the GA + Extra Trees model reduces the clean PMU feature space from 112 attributes to an average of 27.4 attributes over five runs, while increasing macro-F1 from 0.9118 to 0.9212 and ROC-AUC from 0.9791 to 0.9837. These results indicate that many synchronized electrical measurements are redundant. A compact subset of phasor-based features can still provide accurate and interpretable anomaly detection in smart grids.

---


### 326. [Spectral Tail Auxiliary Learning for AI-Generated Image Detection](https://arxiv.org/abs/2605.22751)

**<font color=#1a73e8>作者：</font>** Xingyi Li, Jiahui Zhang, Yiheng Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As generative image models evolve rapidly, the perceptual gap between generated and real images continues to narrow, making AI-generated image detection increasingly challenging. Many existing methods exploit frequency-domain cues for detection, typically described as frequency-domain artifacts or high-frequency discrepancies. However, the specific and recurring spectral regularities remain insufficiently understood and characterized. In this paper, we systematically analyze the one-dimensional radial log-power spectra of real and generated images. We find that generated images do not necessarily exhibit higher or lower energy across the entire spectrum or high-band range. Instead, their spectra deviate from the power-law decay and show an anomalous uplift in the ultra-high-frequency tail. We term this phenomenon spectral tail uplift. We further attribute this phenomenon to nonlinear harmonic accumulation in trained generative models, suggesting that it can serve as a structural cue across generative architectures. Based on this observation, we propose Spectral Tail Auxiliary Learning (STAL), a frequency-domain auxiliary supervision framework for generalizable AI-generated image detection. STAL transfers spectral-tail cues from a tail-aware frequency teacher to a spatial detector during training, while all frequency-domain modules are discarded at inference time. Consequently, STAL introduces no inference overhead. Extensive experiments on 9 public datasets show that STAL achieves strong generalization and stability across generators, data distributions, and real-world scenarios.

---


### 327. [Lumberjack: Better Differentially Private Random Forests through Heavy Hitter Detection in Trees](https://arxiv.org/abs/2605.22756)

**<font color=#1a73e8>作者：</font>** Christian Janos Lebeda, David Erb, Tudor Cebere 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Random forests are widely used in fields involving sensitive tabular data, but existing approaches to enforcing differential privacy (DP) typically degrade performance to the point of impracticality. In this paper, we introduce Lumberjack, a differentially private random forest algorithm that achieves substantially higher utility by constructing large random decision trees and then applying aggressive, privacy-preserving pruning to retain only sufficiently populated nodes. A key component of our approach is a novel $(\varepsilon,\delta)$-DP heavy hitter detection algorithm for hierarchical data, whose error is $O_{\varepsilon,\delta}(\sqrt{\log h})$ for trees of height $h$ and may be of independent interest. This favorable scaling enables the use of significantly deeper trees than in prior work, leading to improved expressiveness under privacy constraints. Our empirical evaluation on benchmark datasets shows that Lumberjack consistently outperforms prior DP random forest methods, establishing a new state of the art. In particular, our approach yields substantial improvements in the privacy-utility trade-off for practical privacy budgets. Our findings suggest that carefully designed DP random forests can close much of the utility gap, highlighting a promising and underexplored direction for future research.

---


### 328. [Advancing Mathematics Research with AI-Driven Formal Proof Search](https://arxiv.org/abs/2605.22763)

**<font color=#1a73e8>作者：</font>** George Tsoukalas, Anton Kovsharov, Sergey Shirobokov 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly excel at mathematical reasoning, but their unreliability limits their utility in mathematics research. A mitigation is using LLMs to generate formal proofs in languages like Lean. We perform the first large-scale evaluation of this method's ability to solve open problems. Our most capable agent autonomously resolved 9 of 353 open Erdős problems at the per-problem cost of a few hundred dollars, proved 44/492 OEIS conjectures, and is being deployed in combinatorics, optimization, graph theory, algebraic geometry, and quantum optics research. A basic agent alternating LLM-based generation with Lean-based verification replicated the Erdős successes but proved costlier on the hardest problems. These findings demonstrate the power of AI-aided formal proof search and shed light on the agent designs that enable it.

---


### 329. [Uniform Diffusion Models Revisited: Leave-One-Out Denoiser and Absorbing State Reformulation](https://arxiv.org/abs/2605.22765)

**<font color=#1a73e8>作者：</font>** Samson Gourevitch, Yazid Janati, Dario Shariatian 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion models are often trained through clean-data prediction, but the prediction can be used in different ways to define the reverse dynamics. In Masked Diffusion Models (MDM) these choices largely coincide, whereas in Uniform Diffusion Models (UDM) they do not. We show that the standard plug-in bridge parameterization for UDM is not optimized by the denoising posterior, but by a leave-one-out posterior that predicts each clean token without using its own noisy observation. This identifies a mismatch between the plug-in ELBO and the usual cross-entropy denoising objective. We characterize the leave-one-out target and derive exact conversions between the denoiser, the leave-one-out posterior, and the score. These conversions allow us to disentangle parameterization and training objective. Our results also lead to inference improvements without any additional training through an informed predictor-corrector sampler and improved temperature sampling based on the leave-one-out predictor.
We further introduce an absorbing-state reformulation of uniform diffusion that preserves the UDM joint law while decomposing it into masked-diffusion-like sampling operations, with simpler denoising posteriors, carry-over unmasking, and a natural remasking mechanism. On language modeling, leave-one-out parameterizations consistently improve UDM generation, while the absorbing construction matches or surpasses masked diffusion. These results suggest that the empirical gap between masked and uniform diffusion is driven less by the choice of marginals themselves than by parameterization and sampling design. The code and models can be found at this https URL.

---


### 330. [Synthetic Data Alone is Enough? Rethinking Data Scarcity in Pediatric Rare Disease Recognition](https://arxiv.org/abs/2605.22767)

**<font color=#1a73e8>作者：</font>** Ganlin Feng, Yuxi Long, Erin Lou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Children with rare genetic diseases often exhibit distinctive facial phenotypes, yet developing computer vision systems for early diagnosis remains challenging due to extreme data scarcity, privacy constraints, and limited data sharing in pediatric settings. These challenges not only hinder automated diagnosis but also restrict the availability of visual resources for clinical genetic counseling. While prior work has shown that synthetic data can augment real datasets and preserve phenotype-level semantics, it remains unclear whether synthetic data alone is sufficient for learning in ultra-low-resource pediatric settings. In this work, we study the synthetic-only regime for pediatric rare disease recognition. Under a controlled experimental setup, models are trained exclusively on phenotype-aware synthetic facial images at increasing scales. We find that synthetic-only training achieves performance comparable to real-data-only baselines at sufficient scale across multiple backbones, suggesting that high-fidelity synthetic data can approximate clinically meaningful distributions. These findings together further enable the use of synthetic pediatric facial images as privacy-preserving resources for genetic education and counseling, supporting clinician training and patient communication. Our results highlight the potential of computer vision to improve data efficiency and expand accessible visual tools in children's healthcare.

---


### 331. [Reducing Political Manipulation with Consistency Training](https://arxiv.org/abs/2605.22771)

**<font color=#1a73e8>作者：</font>** Long Phan, Devin Kim, Alexander Pan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) exhibit systematic political bias across a variety of sensitive contexts. We find that LLMs handle counterpart topics from opposing political sides asymmetrically. We refer to this phenomenon as covert political bias and identify 7 categories of techniques through which it operates. We propose two metrics for covert bias: Sentiment Consistency measures symmetry in rhetoric and framing across paired political prompts; Helpfulness Consistency measures symmetric depth and engagement. To reduce both types of covert bias, we introduce Political Consistency Training (PCT), an RL training method with two complementary paradigms: Sentiment Consistency Training and Helpfulness Consistency Training. We show that PCT preserves overall helpfulness, substantially reduces covert political bias, and generalizes to held-out benchmarks. We release our work at this https URL

---


### 332. [Deep Reinforcement Learning for Flexible Job Shop Scheduling with Random Job Arrivals](https://arxiv.org/abs/2605.22773)

**<font color=#1a73e8>作者：</font>** Yu Tang, Muhammad Zakwan, Efe Balta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Flexible Job Shop Scheduling Problem (FJSP) is the optimal allocation of a set of jobs to machines. Two primary challenges persist in FJSP: the unpredictable arrival of future jobs and the combinatorial complexity of the problem, rendering it intractable for conventional mixed-integer linear programming solvers. This paper proposes an event-based \gls{DRL} approach to solve FJSP with random job arrivals. Specifically, we employ the Proximal Policy Optimization algorithm and use lightweight Multi-Layer Perceptrons to train the \gls{DRL} agent for minimizing the total completion time of all jobs. We design the state representation to be directly accessible from the environment, and limit the learning agent to selecting from among a set of well-established dispatching rules. Simulations show that our \gls{DRL} approach outperforms any of the individual dispatching rules on datasets with varying heterogeneity and job arrival rates. We benchmark our \gls{DRL} against an arrival-triggered mixed-integer linear programming solution and show that our method achieves good performance especially when the datasets are heterogeneous.

---


### 333. [MambaGaze: Bidirectional Mamba with Explicit Missing Data Modeling for Cognitive Load Assessment from Eye-Gaze Tracking Data](https://arxiv.org/abs/2605.22775)

**<font color=#1a73e8>作者：</font>** Amir Mousavi, Mohammad Sadegh Sirjani, Erfan Nourbakhsh 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-time cognitive load assessment from eye-tracking signals could potentially enable adaptive human-centered-AI such as safety-critical applications such as driver vigilance monitoring or automated flight deck assistance, yet two challenges persist: handling frequent data missingness from blinks and tracking failures, and efficiently modeling long-range temporal dependencies. We propose MambaGaze, a framework that addresses these challenges through 1) XMD encoding, which augments raw features with observation masks and time-deltas to explicitly model data uncertainty, and 2) bidirectional Mamba-2, which captures temporal dependencies with linear computational complexity. Experiments on CLARE and CL-Drive datasets under leave-one-subject-out evaluation show that MambaGaze achieves 76.8% and 73.1% accuracy, respectively, outperforming CNN, Transformer, ResNet, and VGG baselines by 4-12 percentage points. Edge deployment benchmarks on NVIDIA Jetson platforms demonstrate real-time inference at 43-68 FPS with power consumption below 7.5W, confirming feasibility for wearable cognitive load monitoring.

---


### 334. [SDPM: Survival Diffusion Probabilistic Model for Continuous-Time Survival Analysis](https://arxiv.org/abs/2605.22776)

**<font color=#1a73e8>作者：</font>** Stanislav R. Kirpichenko, Andrei V. Konstantinov, Lev V. Utkin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Survival analysis aims to estimate a time-to-event distribution from data with censored observations. Many existing methods either impose structural assumptions on the hazard function or discretize the time axis, which may limit flexibility and introduce approximation errors. We propose the Survival Diffusion Probabilistic Model (SDPM), a generative approach to continuous-time survival analysis. SDPM models the conditional distribution of the survival outcome, represented by the pair of observed time and censoring indicator, $\mathbb{P}(T,\delta \mid \mathbf{x})$, using a denoising diffusion model. Under the assumption of conditionally independent censoring, conditional samples generated by the model can be transformed into survival function estimates using the Kaplan-Meier estimator. This formulation avoids parametric assumptions on the event-time distribution and does not require a discretization of the output time space. The model operates in a transformed target space, using standardized log-times and a continuous Gaussian-mixture representation of the censoring indicator. We evaluate SDPM on ten real survival datasets and compare it with five strong baselines, including tree-based, boosting-based, and neural survival models. Results show that SDPM achieves competitive predictive performance across C-index, integrated time-dependent AUC, and integrated Brier score. A study on synthetic Cox-Weibull data demonstrates that SDPM can recover the shape of an underlying continuous survival distribution more accurately than a strong nonparametric baseline when sufficiently many samples are generated. An ablation study confirms the importance of the proposed target-space transformations, which improve event-rate calibration, reduce invalid generated times, and provide consistent gains in predictive discrimination. Codes implementing the proposed model are publicly available.

---


### 335. [DecQ: Detail-Condensing Queries for Enhanced Reconstruction and Generation in Representation Autoencoders](https://arxiv.org/abs/2605.22777)

**<font color=#1a73e8>作者：</font>** Tianhang Wang, Yitong Chen, Wei Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Representation Autoencoders (RAEs) leverage frozen vision foundation models (VFMs) as tokenizer encoders, providing robust high-level representations that facilitate fast convergence and high-quality generation in latent diffusion models. However, freezing the VFM inherently constrains its spatial reconstruction capacity, limiting fine-grained generation and image editing; in contrast, incorporating reconstruction-oriented signals via fine-tuning disrupts the pretrained semantic space and degrades generative fidelity. To address this trade-off, we propose DecQ, a simple yet effective framework for RAEs. Specifically, DecQ introduces lightweight detail-condensing queries that extract fine-grained information from intermediate VFM features through condenser modules. These queries are incorporated into the decoder to support reconstruction and are jointly generated with patch tokens during generative modeling. By aggregating information from both shallow and deep layers, DecQ effectively mitigates the reconstruction--generation trade-off, improving both reconstruction quality and generative performance. Our experiments demonstrate that: (1) with only 8 additional queries and 3.9% extra computation, DecQ improves reconstruction over the frozen DINOv2-based RAE, increasing PSNR from 19.13 dB to 22.76 dB; and (2) for generative modeling, DecQ achieves 3.3$\times$ faster convergence than RAE, attaining an FID of 1.41 without guidance and 1.05 with guidance.

---


### 336. [Evaluating Commercial AI Chatbots as News Intermediaries](https://arxiv.org/abs/2605.22785)

**<font color=#1a73e8>作者：</font>** Mirac Suzgun, Emily Shen, Federico Bianchi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI chatbots are rapidly shaping how people encounter the news, yet no prior study has systematically measured how accurately these systems, with their proprietary search integrations and retrieval-synthesis pipelines, handle emerging facts across languages and regions. We present a 14-day (February 9-22, 2026) evaluation of six AI chatbots (Gemini 3 Flash and Pro, Grok 4, Claude 4.5 Sonnet, GPT-5 and GPT-4o mini) on 2,100 factual questions derived from same-day BBC News reporting across six regional services (US & Canada, Arabic, Afrique, Hindi, Russian, Turkish). The best systems achieve over 90% multiple-choice accuracy on questions about events reported hours earlier. The same systems, however, lose 11-13% under free-response evaluation, and 16-17% across the cohort. We further characterize three failure patterns. First, every model achieves its lowest accuracy on Hindi (79% vs. 89-91% elsewhere) and citations indicate an Anglophone retrieval bias (e.g., models answering Hindi queries cite English Wikipedia more than any Hindi outlet). Second, retrieval, not reasoning, failures drive over 70% of all errors. When models retrieve a correct source, they often extract the correct answer; the problem is to land on the right source in the first place. Third, models achieving 88-96% accuracy on well-formed questions drop to 19-70% when questions contain subtle false premises, with the most vulnerable model accepting fabricated facts 64% of the time. We also identify a detection-accuracy paradox: the best false-premise detector ranks second in adversarial accuracy (abstention rate), while a weaker detector ranks first, showing that premise detection and answer recovery are partially independent capabilities. Overall, these suggest that high accuracy can mask systematic regional inequity, near-total dependence on retrieval infrastructure, and vulnerability to imperfect queries real users pose.

---


### 337. [LCGuard: Latent Communication Guard for Safe KV Sharing in Multi-Agent Systems](https://arxiv.org/abs/2605.22786)

**<font color=#1a73e8>作者：</font>** Sadia Asif, Mohammad Mohammadi Amiri, Momin Abbas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based multi-agent systems increasingly rely on intermediate communication to coordinate complex tasks. While most existing systems communicate through natural language, recent work shows that latent communication, particularly through transformer key-value (KV) caches, can improve efficiency and preserve richer task-relevant information. However, KV caches also encode contextual inputs, intermediate reasoning states, and agent-specific information, creating an opaque channel through which sensitive content may propagate across agents without explicit textual disclosure. To address this, we introduce \textbf{LCGuard} (Latent Communication Guard), a framework for safe KV-based latent communication in multi-agent LLM systems. LCGuard treats shared KV caches as latent working memory and learns representation-level transformations before cache artifacts are transmitted across agents. We formalize representation-level sensitive information leakage operationally through reconstruction: a shared cache artifact is unsafe if an adversarial decoder can recover agent-specific sensitive inputs from it. This leads to an adversarial training formulation in which the adversary learns to reconstruct sensitive inputs, while LCGuard learns transformations that preserve task-relevant semantics and reduce reconstructable information. Empirical evaluations across multiple model families and multi-agent benchmarks show that LCGuard consistently reduces reconstruction-based leakage and attack success rates while maintaining competitive task performance compared to standard KV-sharing baselines.

---


### 338. [Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention](https://arxiv.org/abs/2605.22791)

**<font color=#1a73e8>作者：</font>** Ali Hatamizadeh, Yejin Choi, Jan Kautz  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Linear attention replaces the unbounded cache of softmax attention with a fixed-size recurrent state, reducing sequence mixing to linear time and decoding to constant memory. The hard part is not just what to forget, but how to edit this compressed memory without scrambling existing associations. Delta-rule models subtract the current read before writing a new value, and Kimi Delta Attention (KDA) sharpens forgetting with channel-wise decay. But the active edit still uses a single scalar gate to control two different things: how much old content to erase on the key side and how much new content to commit on the value side. We introduce Gated DeltaNet-2, which generalizes both Gated DeltaNet and KDA by inheriting adaptive forgetting and channel-wise decay while addressing their shared limitation, the scalar tie between erasing and writing. Gated Delta Rule-2 separates these roles with a channel-wise erase gate b_t and a channel-wise write gate w_t, reducing to KDA when both gates collapse to the same scalar and to Gated DeltaNet when the decay also collapses. We derive a fast-weight update view, a chunkwise WY algorithm with channel-wise decay absorbed into asymmetric erase factors, and a gate-aware backward pass that preserves efficient parallel training. At 1.3B parameters trained on 100B FineWeb-Edu tokens, Gated DeltaNet-2 achieves the strongest overall results among Mamba-2, Gated DeltaNet, KDA, and Mamba-3 variants across language modeling, commonsense reasoning, and retrieval. Its advantage is most pronounced on long-context RULER needle-in-a-haystack benchmarks, where it improves the evaluated multi-key retrieval setting and remains strong in both recurrent and hybrid settings. Code is available at this https URL.

---


### 339. [MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems](https://arxiv.org/abs/2605.22794)

**<font color=#1a73e8>作者：</font>** Qianshu Cai, Yonggang Zhang, Xianzhang Jia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous agentic systems are largely static after deployment: they do not learn from user interactions, and recurring failures persist until the next human-driven update ships a fix. Self-evolving agents have emerged in response, but all confine evolution to text-mutable artifacts -- skill files, prompt configurations, memory schemas, workflow graphs -- and leave the agent harness untouched. Since routing, hook ordering, state invariants, and dispatch live in code rather than in any text artifact, an entire class of structural failure is physically unreachable from the text layer. We argue that source-level adaptation is a fundamentally more general medium: it is Turing-complete, a strict superset of every text-mutable scope, takes effect deterministically rather than through base-model compliance, and does not erode under long-context drift. We present MOSS, a system that performs self-rewriting at the source level on production agentic substrates. Each evolution is anchored to an automatically curated batch of production-failure evidence and proceeds through a deterministic multi-stage pipeline; code modification is delegated to a pluggable external coding-agent CLI while MOSS retains stage ordering and verdicts. Candidates are verified by replaying the batch against the candidate image in ephemeral trial workers, then promoted via user-consent-gated, in-place container swap with health-probe-gated rollback. On OpenClaw, MOSS lifts a four-task mean grader score from 0.25 to 0.61 in a single cycle without human intervention.

---


### 340. [The Matching Principle: A Geometric Theory of Loss Functions for Nuisance-Robust Representation Learning](https://arxiv.org/abs/2605.22800)

**<font color=#1a73e8>作者：</font>** Vishal Rajput  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Robustness, domain adaptation, photometric and occlusion invariance, compositional generalisation, temporal robustness, alignment safety, and classical anisotropic regularisation are usually treated as separate problems with separate method families. This paper argues that much of their shared structure is one statistical problem: estimate the covariance of label-preserving deployment nuisance, then regularise the encoder Jacobian along a matrix whose range covers that covariance (the matching principle). CORAL, adversarial training, IRM, augmentation, metric learning, Jacobian penalties, and alignment-style constraints are different estimators of that object, not independent robustness tricks.
In the linear-Gaussian model we prove closed-form optimality (Theorem A), including cube-root water-filling within the matched range; necessity of range coverage for quadratic Jacobian penalties (Theorem G); the same range dichotomy at deep global minima; and two falsification controls (Lemma C; Corollaries E), with seven conditional consistency lemmas (D1-D7) for estimation under standard identifiability assumptions.
We introduce the Trajectory Deviation Index (TDI), a label-free probe of embedding sensitivity when task accuracy or Jacobian Frobenius norm is insufficient.
Thirteen pre-registered blocks from classical ML through Qwen2.5-7B test the predicted matched, then isotropic, then wrong-W ordering on geometry and deployment drift; twelve pass, and the sole exception (Office-31) is an eigengap failure named before the run. At 7B scale, matched style-PMH improves selective honesty and preserves Style TDI where standard DPO degrades it.
The contribution is naming the deployment nuisance covariance, stating what the regulariser must do, and supplying a closed-form falsifiable theory once that object is identified, not universality on every leaderboard.

---


### 341. [Sensor2Sensor: Cross-Embodiment Sensor Conversion for Autonomous Driving](https://arxiv.org/abs/2605.22809)

**<font color=#1a73e8>作者：</font>** Jiahao Wang, Bo Sun, Yijing Bai 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust training and validation of Autonomous Driving Systems (ADS) require massive, diverse datasets. Proprietary data collected by Autonomous Vehicle (AV) fleets, while high-fidelity, are limited in scale, diversity of sensor configurations, as well as geographic and long-tail-behavioral coverage. In contrast, in-the-wild data from sources like dashcams offers immense scale and diversity, capturing critical long-tail scenarios and novel environments. However, this unstructured, in-the-wild video data is incompatible with ADS expecting structured, multi-modal sensor inputs for validation and training. To bridge this data gap, we propose Sensor2Sensor, a novel generative modeling paradigm that translates in-the-wild monocular dashcam videos into a high-fidelity, multi-modal sensor suite (AV logs) comprising multi-view camera images and LiDAR point clouds. A core challenge is the lack of paired training data. We address this by converting real AV logs into dashcam-style videos via 4D Gaussian Splatting (4DGS) reconstruction and novel-view rendering. Sensor2Sensor then utilizes a diffusion architecture to perform the generative conversion. We perform comprehensive quantitative evaluations on the fidelity and realism of the generated sensor data. We demonstrate Sensor2Sensor's practical utility by converting challenging in-the-wild internet and dashcam footage into realistic, multi-modal data formats, further unlocking vast external data sources for AV development.

---


### 342. [Remember to be Curious: Episodic Context and Persistent Worlds for 3D Exploration](https://arxiv.org/abs/2605.22814)

**<font color=#1a73e8>作者：</font>** Lily Goli, Justin Kerr, Daniele Reda 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Exploration is a prerequisite for learning useful behaviors in sparse-reward, long-horizon tasks, particularly within 3D environments. Curiosity-driven reinforcement learning addresses this via intrinsic rewards derived from the mismatch between the agent's predictive model of the world and reality. However, translating this intrinsic motivation to complex, photorealistic environments remains difficult, as agents can become trapped in local loops and receive fresh rewards for revisiting forgotten states. In this work, we demonstrate that this failure stems from a lack of spatial persistence and episodic context. We show that effective curiosity requires a model of the world that is persistent and continuously updated, paired with an agent that maintains an episodic trajectory history to navigate toward novel regions. We achieve this using an online 3D reconstruction as a persistent model of the world, while the agent policy is parameterized as a sequence model over RGB observations to maintain episodic context. This design enables effective exploration during training while allowing the agent to navigate using solely RGB frames at deployment. Trained purely via curiosity on HM3D, our agent outperforms RL-based active mapping baselines and generalizes zero-shot to Gibson and AI-generated worlds. Our end-to-end policy enables efficient adaptation to downstream tasks, such as apple picking and image-goal navigation, outperforming from-scratch baselines. Please see video results at this https URL.

---


### 343. [Vector Policy Optimization: Training for Diversity Improves Test-Time Search](https://arxiv.org/abs/2605.22817)

**<font color=#1a73e8>作者：</font>** Ryan Bahlous-Boldi, Isha Puri, Idan Shenfeld 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models must now generalize out of the box to novel environments and work inside inference-scaling search procedures, such as AlphaEvolve, that select rollouts with a variety of task-specific reward functions. Unfortunately, the standard paradigm of LLM post-training optimizes a pre-specified scalar reward, often leading current LLMs to produce low-entropy response distributions and thus to struggle at displaying the diversity that inference-time search will require. We propose Vector Policy Optimization (VPO), an RL algorithm that explicitly trains policies to anticipate diverse downstream reward functions and to produce diverse solutions. VPO exploits that rewards are often vector-valued in practice, like per-test-case correctness in code generation or, say, multiple different user personas or reward models. VPO is essentially a drop-in replacement for the GRPO advantage estimator, but it trains the LLM to output a set of solutions where individual solutions specialize to different trade-offs in the vector reward space. Across four tasks, VPO matches or beats the strongest scalar RL baselines on test-time search (e.g. pass@k and best@k), with the gap widening as the search budget grows. For evolutionary search, VPO models unlock problems that GRPO models cannot solve at all. As test-time search becomes more standardized, optimizing for diversity may need to become the default post-training objective.

---


### 344. [MotiMotion: Motion-Controlled Video Generation with Visual Reasoning](https://arxiv.org/abs/2605.22818)

**<font color=#1a73e8>作者：</font>** Lee Hsin-Ying, Hanwen Jiang, Yiqun Mei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current motion-controlled image-to-video generation models rigidly follow user-provided trajectories that are often sparse, imprecise, and causally incomplete. Such reliance often yields unnatural or implausible outcomes, especially by missing secondary causal consequences. To address this, we introduce MotiMotion, a novel framework that reformulates motion control as a reasoning-then-generation problem. To encourage causally grounded and commonsense-consistent interactions, we leverage a training-free vision-language reasoner to refine image-space coordinates of primary trajectories and to hallucinate plausible secondary motions. To further improve motion naturalness, we propose a confidence-aware control scheme that modulates guidance strength, enabling the model to closely follow high-confidence plans while correcting artifacts under low-confidence inputs with its internal generative priors. To support systematic evaluation, we curate a new image-to-video benchmark, MotiBench, consisting of interaction-centric scenes where new events are triggered by motion. Both VLM-based evaluation and a human study on MotiBench demonstrate that MotiMotion produces videos with more plausible object behaviors and interaction, and is preferred over existing approaches.

---


### 345. [Cambrian-P: Pose-Grounded Video Understanding](https://arxiv.org/abs/2605.22819)

**<font color=#1a73e8>作者：</font>** Jihan Yang, Zifan Zhao, Xichen Pan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera pose matters. The position and orientation of each viewpoint define a shared spatial coordinate frame that relates observations across video frames. Yet this signal is largely absent from multimodal LLMs (MLLMs) for video understanding, which process frames as isolated 2D snapshots, instead of the persistent scene humans perceive. We revisit pose as a lightweight supervisory signal and introduce Cambrian-P, a video MLLM augmented with per-frame learnable camera tokens and a pose regression head. With a carefully designed sampling scheme, the model achieves substantial gains of 4.5-6.5% on spatial reasoning benchmarks such as VSI-Bench, generalizes across eight additional spatial and general video QA benchmarks, and, as a byproduct, achieves state of the art streaming pose estimation on ScanNet. Surprisingly, training on pseudo-annotated poses from in-the-wild video further improves general video QA benchmarks, showing pose helps beyond spatial reasoning. Together, these results position camera pose as a fundamental signal for video models that reason about the physical world.

---


### 346. [Integrable Elasticity via Neural Demand Potentials](https://arxiv.org/abs/2605.22820)

**<font color=#1a73e8>作者：</font>** Carlos Heredia, Daniel Roncel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose the Integrable Context-Dependent Demand Network (ICDN), a demand-first neural model for multiproduct retail demand. The model learns log-demand as a smooth, context-conditioned function of log-prices, allowing elasticities to be derived exactly from the learned demand surface. On the Dominick's beer dataset, ICDN improves out-of-sample generalization over a directed log-log benchmark and yields more stable, economically plausible elasticity estimates, especially for weakly identified cross-price effects.

---


### 347. [Tokenisation via Convex Relaxations](https://arxiv.org/abs/2605.22821)

**<font color=#1a73e8>作者：</font>** Jan Tempus, Philip Whittington, Craig W. Schmidt 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tokenisation is an integral part of the current NLP pipeline. Current tokenisation algorithms such as BPE and Unigram are greedy algorithms -- they make locally optimal decisions without considering the resulting vocabulary as a whole. We instead formulate tokeniser construction as a linear program and solve it using convex optimisation tools, yielding a new algorithm we call ConvexTok. We find ConvexTok consistently improves intrinsic tokenisation metrics and the bits-per-byte (BpB) achieved by language models; it also improves downstream task performance, but less consistently. Furthermore, ConvexTok allows the user to certify how far their tokeniser is from optimal, with respect to a certain objective, via a lower bound, and we empirically find it to be within 1\% of optimal at common vocabulary sizes.

---


> [!TIP]
> 当前位于：**301-347**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-347**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
