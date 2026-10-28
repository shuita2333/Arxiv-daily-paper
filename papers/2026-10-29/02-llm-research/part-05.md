# 🧠 大模型相关研究 | 2026年10月29日

> 本类共 **226** 篇论文：已确认 **214** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-226**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-226**

---

### 201. [TeamGym: A Gym for Team Decision-Making by AI Agents with Distributed Information](https://arxiv.org/abs/2610.37571)

**<font color=#1a73e8>作者：</font>** Chanwoo Park, Jaywoong Jeong, Zachary Wojtowicz 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many real-world decisions require teams to integrate information distributed across participants. Yet AI agents are still primarily trained and benchmarked in isolation. We introduce TeamGym, an environment for evaluating and training language model-based agents on team decision-making problems constructed from real-world legal, finance, medical, and software engineering corpora. TeamGym introduces a method to identify a minimal set of facts, each element of which is necessary and all of which are collectively sufficient for a correct final decision, which we call pivotal information. This enables TeamGym to both control the distribution of pivotal information and track how well agents identify and integrate pivotal information when making team decisions. Examining 8 language models on 12 source corpora, we find that current AI agents often fail to effectively share information: Distributing pivotal information across participants lowers success rate by 22.9 percentage points on average relative to giving the same information to a single model (a communication gap). We also document that participants do not effectively retrieve decision-relevant information on their own: A team's success rate is lowered by a further 19.9 points when participants must identify and extract pivotal information from source material rather than receiving it directly (a retrieval gap). To help remedy these deficits, we use TeamGym to train policies through reinforcement learning on team decision loss. Across two policy-training experiments, we find that training improves final-decision quality and induces emergent coordination in participation, speaker selection, and communication, even though the reward evaluates only the final decision.

---


### 202. [As the Story Unfolds: Watching a Film and Identifying Characters as a Human Does](https://arxiv.org/abs/2610.37579)

**<font color=#1a73e8>作者：</font>** Zhongrui Gui, Junyu Xie, Tengda Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Films introduce characters incrementally as they progress. We study the problem of identifying principal characters and assigning their names directly from the movie itself, without using external cast lists, actor photographs, or pre-built character banks. We introduce the character naming task: given a name mentioned in dialogue and the associated video context, the model must determine which visible character bears that name. This task is challenging because name resolution often depends on cinematic cues such as shot-reverse-shot structure, self-introduction, direct address, third-party reference, gaze, and temporal continuity. We provide a dataset and annotations for evaluating character naming and first character appearances, develop a video-and-dialogue model for the task, and compare it with proprietary multimodal large language models. We further introduce a progressive framework for building a character bank as the film unfolds. Together, these contributions support online, human-like movie understanding in which character identities are inferred from the film itself.

---


### 203. [EnvSched: Environment-Aware Scheduling for Rollout-Efficient Agent Reinforcement Learning](https://arxiv.org/abs/2610.37609)

**<font color=#1a73e8>作者：</font>** Sihan Yang, Weichen Bai, Ruichuan An 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As executable environments for language agents scale, generating and verifying their rollouts becomes increasingly expensive. Under finite rollout budgets, this raises an important question: can data management at the environment level make agentic reinforcement learning (RL) more efficient by organizing, evaluating, and scheduling task instances together with the environments that determine their tools, states, transitions, and verification? To address this question, we introduce EnvSched (Environment-aware Scheduling), an online scheduler that learns from rollout history. EnvSched assigns scheduling value through two complementary modeling choices: exploitation prioritizes tasks likely to provide informative reward differences, while coverage spreads each batch across underobserved environments and interaction patterns. EnvSched organizes environment--task pairs as nodes in a dual-relation graph, with within-environment edges capturing task semantics and shared tool, state, and verifier structure, and cross-environment edges capturing abstract execution and reward topology. By propagating historical rollout statistics along both edge types, it predicts within-task reward variance. These predictions guide a scheduler that allocates each batch to tasks with high predicted reward variance and underobserved environments and tasks. Environment quotas and a similarity penalty further limit concentration and redundancy, yielding informative and diverse batches without additional pilot rollouts. In RL on Qwen3-8B, EnvSched achieves an average score of 48.81 across BFCL-v3, tau-Bench, and ACEBench-Agent after 40 training steps, exceeding the highest score attained by random task selection after 120 steps. It also improves downstream performance across model sizes at the same training budget.

---


### 204. [VideoLVR: Latent Visual Reasoning over Grounded Video Evidence](https://arxiv.org/abs/2610.37613)

**<font color=#1a73e8>作者：</font>** Shilong Li, Xingyuan Bu, Hao Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought reasoning has substantially advanced video understanding in multimodal large language models (MLLMs). However, language-based reasoning traces do not provide a reliable mechanism for models to revisit relevant visual evidence, leading to visual forgetting and impairing their ability to reason over video content. Existing approaches maintain visual grounding during reasoning in two main ways: they either refer to evidence using textual coordinates, which specify symbolic locations rather than the visual content itself, or reinsert cropped regions or frames into the multimodal context, preserving visual details at the cost of substantial context expansion. To address these limitations, we introduce VideoLVR, which constructs latent visual evidence from local regions at relevant video moments, thereby providing visual support for intermediate reasoning steps. To supervise latent visual evidence generation, we introduce a visual token prediction objective that formulates visual token reconstruction as prediction over a vocabulary derived from the input video, thereby unifying visual evidence reconstruction and text generation within the same token prediction framework. This shared prediction framework enables MLLMs to reason over interleaved text tokens and latent visual states while integrating evidence from different moments. We further extend VideoLVR to reinforcement learning by treating sampled visual tokens as actions alongside text tokens and jointly optimizing the policy using final-answer rewards. By efficiently revisiting task-relevant visual information during reasoning, VideoLVR improves video understanding without substantially expanding the multimodal context. Experiments on multiple video benchmarks demonstrate its effectiveness, especially on tasks requiring fine-grained visual evidence.

---


### 205. [Perceiving and Predicting Dynamic Sports: Spatiotemporal Intelligence in Vision Models for Egocentric Tennis Video](https://arxiv.org/abs/2610.37619)

**<font color=#1a73e8>作者：</font>** Tudor Braicu, Joseph DelPreto, Jared Boyer 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Agile robots require spatiotemporal intelligence to interpret scenes, reason about interactions, and anticipate future events. Yet it remains unclear how well foundation vision models support these capabilities, particularly from a moving egocentric camera, which is a natural view for robots. To investigate this, we collect an annotated tennis dataset and train a suite of vision models on spatiotemporal tasks. Our dataset contains egocentric video synchronized with five allocentric videos, estimated global positions, labeled contact times, and annotated stroke types. We then evaluate seven prediction tasks from egocentric images: 2D ego player and 3D ball localization, future player and ball trajectories, forehand or backhand stroke anticipation, time to the next ego player ball contact, and 3D ball position at that contact. We compare image encoders, video encoders, and vision-language models with jointly trained prediction heads. The best performing models achieve mean current-frame localization errors of 0.14 m for the ego player and 0.54 m for the ball, future forecasting errors of 0.34 m for the ego player and 0.91 m for the ball over 1.1 s, and a mean contact-time prediction error of 0.14 s. Auxiliary depth information substantially improves 3D ball localization, suggesting that inferring metric depth remains a challenge. Longer image histories do not improve ball forecasting, indicating that representations exploit scene context rather than rely solely on inter-frame motion. Finally, we propose a conditional diffusion model to generate whole-body kinematic tennis motion from vision encoder predictions on egocentric video at real-time rates, adapting movements as predictions are refined. These results move towards a deeper understanding of how foundation vision models can support real-time dynamic robots using egocentric video.

---


### 206. [Rare, Relevant, and Still Wrong: How Memory Fails LLM Group Decisions](https://arxiv.org/abs/2610.37624)

**<font color=#1a73e8>作者：</font>** Anouar Imel, Imad Charradi, Abderrahman Sghir 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When an LLM group's discussion is compressed into a short memory for a final decision maker, what should the memory keep? Two natural heuristics keep the rarest claims or the claims relevant to the decision criteria. On hidden-profile tasks both look attractive, because how widely a fact is held is confounded with whether it helps. We introduce CrossProfile, a diagnostic benchmark of 60 templates with automatically verified answer keys, in which the ownership of supporting, decoy, and irrelevant facts is crossed while their text is held fixed (480 tasks). Across Qwen2.5-7B, Llama-3.1-8B, and two DeepSeek models, both heuristics fail in predictable places. Selecting by relevance readmits decoys, because decoys are on topic: even a perfect relevance filter loses 23 to 31 points to rarest-first selection in the classic hidden-profile configuration. Rarest-first selection is no better than random selection on average and wins only where the rare facts happen to be the useful ones. In both cases accuracy follows the balance of evidence the memory keeps, not the policy that kept it. The decision model adds a third failure, a form of social proof: it gives extra weight to facts attributed to many agents. Removing the attribution tags, or reassigning them at random with line order fixed, raises accuracy in the classic configuration by 13 to 24 points. In natural discussions the evidence is lost before any memory acts: the complete transcript yields lower accuracy than no notes at all.

---


### 207. [What Improves During Pretraining? Tracking Knowledge Acquisition with Point-in-Time Models](https://arxiv.org/abs/2610.37631)

**<font color=#1a73e8>作者：</font>** Chang Su, Bin Wu, Emine Yilmaz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models pretrained on web corpora collected over multiple years learn both general and domain-specific knowledge. How these different kinds of knowledge are learned as pretraining progresses remains unclear. Recent point-in-time models trained on web snapshots from different years provide a way to probe how knowledge prevalence varies over time. Using these models, we propose a temporal variability score (TVS), defined as the coefficient of variation of an item's negative log-likelihood across models. A higher score suggests that the knowledge may be less consistently represented across years of web text. We evaluate six benchmarks covering diverse topics using six models from multiple open-source model families. We find that low- and high-TVS items are learned similarly early in training, but high-TVS items improve faster later on. At the end of the pretraining run, high-TVS items outperform low-TVS items in 34 of 36 model-benchmark settings, with an average advantage of 7.3 points of chance-normalized accuracy. This pattern is most robust on knowledge-intensive tasks, even when comparing items of similar difficulty. Our findings reveal differences in how knowledge is learned over the course of pretraining, with temporal variability providing a diagnostic of these learning dynamics beyond aggregate benchmark scores.

---


### 208. [Metacognitive Decoding: Efficient Inference for Diffusion Language Agents](https://arxiv.org/abs/2610.37642)

**<font color=#1a73e8>作者：</font>** Mingyu Zhao, Shuhang Lin, Ligong Han 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models offer a promising path to efficient agents through parallel token generation. However, efficient interaction requires adapting both where computation is spent and how much text is generated. We introduce a metacognitive controller that guides diffusion generation according to the needs of the current response and the agent's interaction with the environment. It learns when to finalize tokens and how far generation should extend, reducing overall computation within responses. Our controller, a lightweight plug-in for the diffusion backbone, is trained on agent trajectories to balance correctness and generation cost. This approach connects the agent's generation process to the interaction the agent serves. Experiments across five benchmarks demonstrate that our approach reduces inference FLOPs by 20.6% on average compared with the most efficient baseline, while maintaining competitive task accuracy. Ablation studies further validate the effectiveness of our approach.

---


### 209. [Multi-State Linear Attention with Generalized Second-Order Routing](https://arxiv.org/abs/2610.37645)

**<font color=#1a73e8>作者：</font>** Hee Seung Hwang, Sanghyuk Chun, Xindi Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-attention plays a key role in long-sequence modeling, but its quadratic time complexity fundamentally limits the scaling of Large Language Models. Recently, Multi-State Linear Attention (MSLA) mechanisms have been proposed to make sequence modeling more efficient by splitting the context into segments and compressing each in its own memory state. MSLA aggregates the information extracted from each memory state using only the mean alignment between a query and each segment's keys, ignoring how the alignment is distributed within the segment. In order to model the relevance of a segment to a query more comprehensively and incorporate the variance of the alignment in the aggregation, we propose MERLIN (MomEnt Routing for multi-state LINear attention), a method that tracks the first and second moments of each segment's keys. Using the moments of keys, a query can recover both the mean and the variance of its alignment with each segment to perform a more content-aware aggregation of per-state readouts. Experiments on multi-state variants of Gated DeltaNet-1.3B and Mamba-2-780M show that MERLIN consistently outperforms existing aggregation methods on various long-context tasks. In particular, MERLIN outperforms baselines on RULER needle-in-a-haystack and long-context QA (+8.3% for Gated DeltaNet-1.3B and +7.0% for Mamba-2-780M) and diverse subtasks in LongBench (+13.5% and +12.0%). It even outperforms baselines that consume 4x more memory. MERLIN provides a simple and general routing mechanism for improving long-context capabilities of MSLA models.

---


### 210. [MuonGS: Pretraining LLMs with Relaxed Weight-Norm Control](https://arxiv.org/abs/2610.37647)

**<font color=#1a73e8>作者：</font>** Athanasios Glentis, Dawei Li, Mingyi Hong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weight decay and explicit weight-norm constraints improve optimizer performance in language model pretraining, yet a unified understanding of why such control helps and how much is needed remains incomplete. We analyze norm control in Muon over the entire training trajectory using the \emph{accumulated effective learning rate}, $C_T=\sum_{t<T}\eta_t/\|W_t\|_F$, where $\eta_t$ is the nominal learning rate and $\eta_t/\|W_t\|_F$ is the effective learning rate relative to the weight norm. For bounded update directions, accumulation over any training interval bounds relative weight displacement. We show that vanilla Muon can accumulate only logarithmically, potentially limiting exploration and helping explain its slower empirical progress, whereas MuonW and MuonH guarantee at least linear accumulation under the stated conditions. Going beyond bounded-norm control, we show that sufficiently slow norm growth guarantees faster accumulation than the logarithmic worst case, opening up less restrictive optimizer designs.
Based on this insight, we propose MuonGS, which uses Gram--Schmidt (GS) projection to remove the radial component of each Muon update without fixing the weight norm. With bounded update directions and a constant nominal learning rate, we prove that the weight norm grows at most proportionally to $\sqrt{t}$ after $t$ steps. Consequently, MuonGS guarantees $C_T=\Omega(\sqrt{T})$, with accumulation sustained even in later training. Further, for smooth scale-invariant objectives we establish its $O(T^{-1/2})$ stationarity guarantee. In pretraining experiments with 160M- and 400M-parameter dense models as well as a 135M active- and 1B total- parameter MoE model, MuonGS achieves lower validation perplexity than MuonH at long training horizons. In particular, for the dense model it achieves an estimated token-equivalent speedup up to about $15\%$ at matched validation loss to MuonH.

---


### 211. [Scaling Laws for Tool-Use Agents via Controllable Environment Synthesis](https://arxiv.org/abs/2610.37648)

**<font color=#1a73e8>作者：</font>** Andrew Szot, Samira Abnar, Omar Attia 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We explore how to build performant large language model (LLM) tool-use agents that complete complex, multi-step tasks. Specifically, we study how data composition in synthetically generated tool-use environments affects the training of such agents. To do so, we propose the SynthAPI pipeline, which explicitly controls the diversity of generated environments along the axes of tools, tasks, and the databases on which the tools operate. By systematically varying SynthAPI's generation controls in 458,752 tasks across 849 trained models of four different sizes, we derive a scaling law that predicts downstream tool-use agent generalization based on the scale and composition of the synthesized environments. These predictable relationships reveal several lessons for scaling tool-use agent data. As data budgets grow, scaling tool and database diversity becomes more effective than increasing the number of tasks, and increasing data complexity yields larger gains. Scaling according to these findings yields agents that outperform models trained on data from prior work in large-scale tool-use agent and synthetic environment generation across four evaluation benchmarks.

---


### 212. [Can LLMs Uncover Hidden Physical Laws through Free Exploration?](https://arxiv.org/abs/2610.37649)

**<font color=#1a73e8>作者：</font>** Zhen Yang, Wen Wang, Xander Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific discovery often begins with an unexpected observation that prompts a new research question. In a world with altered physical laws, can large language models (LLMs) notice unexpected behavior, such as heavier objects falling more slowly, and discover the law through experiments without being told what to investigate? To evaluate this ability, we introduce LongChang, an automated framework that creates simulated worlds with altered physics, where one or more laws differ from ordinary physics. The evaluated LLMs act as explorers, manipulating objects and building tools to investigate their own questions without research tasks or hints about these laws. Separate LLM agents generate and review scenes, review tool designs, and evaluate reports for correctness and experimental support using the altered physical laws and exploration records. These records guide scene evolution for further exploration, allowing the full cycle to run without human intervention. Among 12 LLMs, GPT-6-Astra achieves a discovery rate of 16.7%, while the other 11 score 0%. The exploration records reveal uninvestigated anomalies and only partial identification of the altered physical laws.

---


### 213. [GEPA-Curator: Curated Learning for Self Improving Agents](https://arxiv.org/abs/2610.37651)

**<font color=#1a73e8>作者：</font>** Zack Yu, Nicholas Lee, Minjae Lee 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used in multi-turn agentic workloads that require sustained interaction with complex environments. Existing reflective prompt optimizers such as GEPA learn from failed rollouts, but agentic failures can also come from prompt weaknesses, harness limitations, stochastic execution, or noisy judges. We argue that such failures may not provide useful learning signal, and may even be harmful; and thus it is essential to curate which tasks are provided to the prompt optimizer for better performance. We introduce GEPA-Curator, a framework that augments the prompt optimizer to select which agent experiences should shape prompt optimization. In particular, GEPA-Curator consists of two components: task curation, which filters out tasks that are likely to provide noisy or unreliable learning signals, and prior success retrieval, which selectively retrieves past successful trajectories for a task and provides them as additional context to the prompt optimizer. We evaluate GEPA-Curator on GoBrowse, ALFWorld, AppWorld, and $\tau$-bench, using both Gemini 3.1 Pro and Claude Opus 5 as optimizer models. GEPA-Curator matches or exceeds the mean performance of both baselines, with gains of up to 20.7% over GEPA and 21.2% over ACE.

---


### 214. [Can Discrete Tokens Serve as Semantically Lossless Representations of Visual Signals?](https://arxiv.org/abs/2610.37662)

**<font color=#1a73e8>作者：</font>** Jialv Zou, Xiaotong Li, Zhengrong Yue 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Discrete visual tokens represent vision in a discrete form analogous to language, offering a native interface for multimodal modeling under a shared next-token prediction objective. However, quantization error is widely assumed to cause unavoidable semantic loss, fundamentally limiting the semantic fidelity of discrete visual tokens and positioning continuous visual representations as an intrinsic upper bound. Using multimodal understanding as a proxy for semantic fidelity, we revisit this assumption and find quantization error unreliable, as discrete representations with substantially larger errors can achieve better understanding. Instead, the effective bit budget of discrete indices emerges as a key determinant of downstream performance. However, existing quantizers eventually saturate as additional codebooks contribute progressively less semantic information. As one approach to alleviating this saturation, we introduce Factorized Vector Quantization, which quantizes complementary, fixed-dimensional views of the visual feature with symmetric parallel codebooks. It continues to improve at larger bit budgets, ultimately matching continuous visual representations in multimodal understanding. Trained on industrial-scale multimodal data, our model achieves state-of-the-art performance among discrete-representation models, outperforming UniAR and Emu3-Chat by 22.8% and 59.2%, respectively, on a nine-metric average. To our knowledge, it is also the first discrete-representation model competitive with strong continuous-representation models such as Qwen3-VL, including on fine-grained OCR tasks. We further identify the key principles and a practical recipe enabling this competitiveness. These results and insights support the potential of discrete visual representations to underpin large-scale native multimodal foundation models. Code and models are available at this https URL

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 215. [Layerwise Repacking: Variable-Length Hybrid-Attention Training without an Extra Redistribution Pass](https://arxiv.org/abs/2610.35989)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jiahao Zhang, Junwei Feng, Dongliang Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Variable-length training creates conflicting parallelism requirements across the layers of a hybrid-attention model. The longest samples require wide sequence-parallel (SP) groups of 16 or 32 ranks for full attention, whose cost grows quadratically with sequence length. Sparse-attention layers, dominated by near-linear MoE work, can instead balance most evaluated workloads within node-local SP8 groups. Reusing the wide groups for these layers pushes their all-to-all communication across nodes, where the observed effective rate is 7.0x lower. Yet switching to smaller groups changes which ranks own each sample; a separate redistribution at every full-sparse boundary would introduce another data transfer.
Layerwise Repacking keeps each SP16/32 parent for full attention and repacks its samples into node-local sparse children at SP{1, 2, 4, 8}, where hidden states persist between full layers. The layout change rides on the two existing full-layer Ulysses sites: at each, one variable-size all-to-all performs both the head exchange and the sample repacking, so no redistribution pass is added. Because the balance the children can reach depends on which samples share a parent, an auxiliary parent solver rebalances parent membership before the children are formed.
On all 22 steps with SP16/32 parents among the first 200 training steps of a 1F3S hybrid-attention model (one full-attention layer per three sparse-attention layers), repacking alone reduces the mean end-to-end time by 5.95% and raises model FLOPs utilization (MFU) by 3.75 percentage points over the baseline with repacking disabled; with the improved solver, end-to-end time falls by 7.61% and MFU rises by 4.83 percentage points.

---


### 216. [OmniBrain-0: A Unified Agentic Model for Embodied Intelligence](https://arxiv.org/abs/2610.36013)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xiaomi Embodied Intelligence Team, Yuechen Luo, Chong He 等 32 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> General-purpose embodied intelligence requires robots to coordinate diverse skills over long horizons, track task progress, and recover from failures. Specialist policies alone do not ensure task-level reliability, while powerful multimodal agents rely on costly reasoning and external experience that compact models struggle to reproduce. We introduce OmniBrain-0, a lightweight unified embodied agent that coordinates manipulation and navigation through a shared high-level decision model, integrating task understanding, planning, progress tracking, and feedback-driven recovery. Our progressive training framework combines embodied pretraining, domain-specialized agent distillation, and multi-teacher on-policy distillation (MOPD). It distills powerful teachers' interaction experience into manipulation and navigation experts, then consolidates their decision capabilities into OmniBrain-0. Unification therefore occurs within the learned decision model rather than only at the tool interface. We further introduce Rubric-Guided Recursive Self-Improvement (RSI), a data flywheel in which a Meta-Agent turns execution evidence into refined rubrics, step-level reminders, and verified trajectories for domain-expert updates before their reconsolidation into OmniBrain-0 through MOPD. We evaluate OmniBrain-0 on LIBERO-Pro, LIBERO-Plus, RoboCasa365, RoboTwin 2.0, and R2R-CE Val-Unseen, as well as multiple real-world manipulation tasks. OmniBrain-0 combines strong cross-domain task performance with substantially lower inference and execution overhead than its closed-source teacher, demonstrating efficient transfer and consolidation of embodied capabilities into a compact unified agent.

---


### 217. [SpecLST: Spectral-Enhanced Long-Short Term Spatio-Temporal Multimodal Modeling for Traffic Forecasting](https://arxiv.org/abs/2610.36393)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Kenan Kang, Matthew M. Y. Kuo, Weihua Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modeling multi-scale dynamics in urban road networks is essential for intelligent transportation systems but is often hindered by the computational cost of long-range historical context and the challenge of fusing heterogeneous modalities. Existing spatio-temporal frameworks face a trade-off between sequence length and memory overhead, while frequently neglecting the transient effects of exogenous factors such as road incidents and weather. To address these limitations, we propose SpecLST, a frequency-enhanced long-short-term spatio-temporal multimodal framework. SpecLST leverages a fast Fourier transform-based frequency-domain representation module to efficiently encode multi-week historical dependencies, bypassing the memory bottlenecks of standard attention mechanisms over raw long sequences. Heterogeneous context is integrated through attention-based fusion, followed by a sparse Mixture-of-Experts backbone with graph augmentation for spatio-temporal representation learning. Additionally, a frequency-enhanced residual head isolates high-frequency transients, improving sensitivity to abrupt traffic anomalies. At the 60-minute horizon, SpecLST achieves mean relative error reductions of 14.10% in MAE, 10.35% in RMSE, and 15.78% in MAPE across eight neural forecasting baselines and four datasets, with the dataset- and metric-specific average reductions ranging from 5.63% to 22.21%.

---


### 218. [From Solver Trajectories to Teaching Trajectories: Cognition-Aligned Reasoning Distillation](https://arxiv.org/abs/2610.36445)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yashuo Luo, Qianren Mao, Ziqi Qin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation from large reasoning models (LRMs) often uses raw teacher trajectories as supervision. However, this practice creates a mismatch between the goal of distillation and the nature of teacher trajectories. Advanced LRMs typically improve their reasoning capabilities through reward-driven post-training, such as RLHF. This training optimizes them as strong solvers, rather than as teachers that produce reasoning processes smaller models can easily learn. Since smaller models have different "cognitive capacities" compared to their larger teachers, directly imitating raw teacher trajectories can sometimes be ineffective and often requires a substantial number of high-quality samples. To bridge this mismatch, we propose Cognition-Aligned Reasoning Distillation (CARD), an RL-based framework that transforms solver trajectories into teaching trajectories aligned with the student's cognition. Avoiding expensive resampling, our framework directly transforms existing trajectories. We optimize CARD with two reward signals: (1) a Distribution Alignment Reward that matches the student's predictive distribution, and (2) a Logical Coherence Reward that reduces misleading failed reasoning steps. Comprehensive evaluations across multiple student models and settings demonstrate that CARD outperforms distillation from raw teacher trajectories in in-domain settings while achieving substantial gains in out-of-distribution performance. Code is available at this https URL.

---


### 219. [PRISM: Pathology Reliability In Scarce-label Medicine. A Tile-level Benchmark of Pathology Foundation Models](https://arxiv.org/abs/2610.36517)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Alicem Koyun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pathology foundation models are typically benchmarked on classification performance at full label availability and on in-distribution test sets, while calibration, behavior at low label budgets, and robustness under cross-institutional shift are seldom evaluated jointly. We introduce PRISM, a tile-level benchmark that measures the reliability of pathology foundation models along four axes: model choice, label fraction, calibration, and out-of-distribution transfer. PRISM evaluates eight foundation models (CLIP, PLIP, CONCH, UNI, Virchow2, GigaPath, H-Optimus-0, Midnight) on six tile-level datasets at six label fractions (1% to 100%) with three seeds (864 linear probe runs), extended with a five-hospital Camelyon17 study of 20 directed transfer pairs. Four phenomena emerge. (i) Under full supervision, AUROC rank predicts post-temperature calibration rank consistently across datasets (Spearman rho = 0.52, I^2 = 0%), whereas at 1% labels the relationship becomes dataset-specific (rho = -0.24, I^2 = 67%). (ii) On harder datasets the linear probe collapses to a single predicted class below a dataset-specific label fraction. (iii) Whether additional source-domain labels help or harm target calibration tracks how well the probe transfers: below a transfer AUROC of roughly 0.85, more labels worsen target ECE in 86-88% of combinations. (iv) Temperature scaling fails to reduce ECE in 49 of 288 cells, miscalibration is predominantly under-confidence, and a source-fitted temperature is harmful under failing transfer. PRISM is released as a pip-installable package with reference results for all 288 cells. Code and data: this https URL

---


### 220. [FrameForge: Harnessing Priors of Video Foundation Models for Unified Image Generation](https://arxiv.org/abs/2610.36545)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yijing Lin, Zhendong Mao, Mengqi Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified conditional image generation requires a single model to preserve different aspects of a visual input while producing a target image that follows textual guidance. Pretrained video models provide a promising foundation by encoding visual transformations across time, yet existing approaches typically assign the condition and target to fixed temporal positions. We observe that condition-target relationships vary substantially across generation tasks, while video models naturally encode visual transformations at different temporal scales. This motivates us to model conditional generation through input-adaptive virtual temporal relations. We propose FrameForge, which captures two complementary aspects of such relations. Mixture of Temporal Experts (MoTE) models how far the target lies from the condition by dynamically selecting temporal RoPE experts with different virtual intervals. Chain of Temporal Reasoning (CoTR) models how the condition is transformed into the target through a latent intermediate state, with a reasoning-bottleneck attention mask encouraging information propagation through this pathway. Experiments on DreamBench, COCO2017, and GEdit-Bench show that FrameForge achieves superior performance in subject-driven generation, canny-to-image generation, and image editing among the compared methods.

---


### 221. [SAGE: Semantic-Augmented Geometric Experts for Point Cloud Registration](https://arxiv.org/abs/2610.36658)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Tomoyasu Shimada, Kazuhiko Murasaki, Shoichiro Takeda 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Point cloud registration is an essential task for scene reconstruction, requiring the alignment of partially overlapping point clouds. Under low-overlap conditions, this task remains challenging because existing geometry-only methods cannot distinguish geometrically similar but semantically distinct structures (e.g., TV corners vs. desk corners and chair legs vs. table legs), resulting in incorrect correspondences. To address this geometric ambiguity, we present Semantic-Augmented Geometric Experts (SAGE), which integrates frozen pre-trained point cloud semantic representations into the registration pipeline without requiring additional sensors or fine-tuning the semantic encoder. To effectively leverage these semantic distinctions, SAGE employs a Semantic-Guided Mixture of Experts (SG-MoE) architecture. Through semantic-aware routing, SG-MoE enables each expert to specialize in distinct semantic-geometric patterns, reducing mismatches that confound geometry-only methods. With a structure-aware estimator, SAGE achieves the highest registration recall on 3DLoMatch while remaining competitive on 3DMatch. When evaluated with the same number of refinement iterations, SAGE further achieves the highest inlier ratio and registration recall on both benchmarks. These results indicate that frozen semantic representations provide effective cues for resolving geometric ambiguity in low-overlap registration.

---


### 222. [Right Click, Wrong Box: Grading GUI Grounding by What a Click Does](https://arxiv.org/abs/2610.36831)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xiaokang Yuan, Binhui Yao, Luwei Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Leading GUI grounders score 93 to 96% on ScreenSpot-v2, and reported gaps between new and prior models are about a point. At this level the useful question is what the remaining errors are. Benchmarks count a click as correct only inside one annotated box, but interfaces often expose one action through several elements: a duplicated link, the label of a checkbox, the title next to a logo. The box is not wrong. The rule is incomplete. We call a click correct when executing it produces the same outcome as clicking the annotated target. A probe that executes and fingerprints about a thousand clicks per page turns this definition into outcome maps and an execution judge for live web applications, with no new annotation. We execute the predictions of three strong 7--8B grounders on a code forge and an online shop. About one in five and one in three of the clicks that box scoring rejects reach the intended outcome, and the shares remain one in seven and one in three when the instructions are rewritten as natural tasks. A blind audit of 11 models on ScreenSpot-v2 (three 7--8B grounders and eight 3B variants) finds the same effect on web screenshots, with two independent reviewers on a 60-unit subset. The share is highest for the strongest grounders. Training seeds and test-set sampling add noise that more runs and paired intervals control. Box scoring instead under-counts correct clicks, which repetition does not remove, and the audit-based correction of 0.2 to 1.8 points on ScreenSpot-v2 is as large as the gaps the field reports. The correction is needed in evaluation. In our 3B GRPO study, crediting equivalent clicks in the reward gives no stable gain over box rewards across three seeds and four test sets. We release the probe, the outcome maps, the audit and every prediction.

---


### 223. [Multibranch Ensemble Head in Vision Foundation Models for Efficient Cucumber Phenological Stage Classification](https://arxiv.org/abs/2610.37118)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Kostiantyn Khabarlak  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Foundation Models (VFMs) pretrained with self-supervised learning, such as DINOv2, provide highly transferable features, yet adapting them to small, domain-shifted datasets is still challenging. We propose a regularizing multibranch ensemble head: a training and inference scheme that pairs low- and high-capacity branches, samples a single branch stochastically at each training step, and averages both branches in probability space at inference. The design adds negligible parameters and essentially no inference overhead over a single heavy head, while improving the accuracy-efficiency trade-off under data-scarce conditions. Accurate classification of plant growth stages is critical for precision agriculture, enabling timely decisions on fertilization, irrigation, and harvesting. Therefore, as a challenging practical case we use cucumber phenological stage classification, in which flowers and fruits are frequently occluded by foliage, and stage transitions manifest primarily as subtle changes in leaf morphology. The NALEF Food Safety dataset contains images of five cucumber growth stages captured under diverse real-world conditions. On it we evaluate a broad range of backbones, including DINOv2 and DINOv3 ViT and ConvNeXt variants, against strongly supervised counterparts (ResNet, EfficientNet, ViT). The proposed DINOv2 ViT-S with multibranch head achieves a Macro F1 of 0.978 and Cohen's Kappa of 0.971, matching the performance of models more than ten times larger in parameters and GFlops, while requiring only 12.2 GFlops and 22.3M parameters, making it deployable on smartphones and edge devices for phenological stage classification.

---


### 224. [GradCO: Behavior-Aware Gradient-Conflict Offloading for Text-Based Person Anomaly Search](https://arxiv.org/abs/2610.37267)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhiheng Fu, Zixu Li, Zhiwei Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-based Person Anomaly Search (TPAS) retrieves a target pedestrian using natural-language descriptions of appearance and normal or anomalous behavior. Unlike conventional text-based person retrieval, TPAS must preserve identity cues while distinguishing fine-grained behaviors. It presents two challenges: same-identity, different-behavior hard negatives cause gradient conflict during granular alignment, while strong appearance cues can obscure weak behavioral evidence during aggregation. We propose GradCO (behavior-aware Gradient-Conflict Offloading), comprising three complementary components. Behavior-Aware Mixture-of-Experts (B-MoE) forms appearance, normal-behavior, and anomalous-behavior streams whose roles are learned from retrieval objectives without expert-specific semantic labels. Conflict Offload Learning (COL) uses pair-conditioned offload anchors in similarity computation to reduce the conflicting-gradient burden on the main text representations. Hierarchical Intent Alignment (HIA) aggregates expert similarities and features using query-conditioned weights. Experiments on five TPAS/TIPR benchmarks show GradCO significantly surpasses SOTA methods and validate our design.

---


### 225. [A note on data-efficient finetuning of vision foundation models](https://arxiv.org/abs/2610.37510)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Niclas Hergenröther, Antonio Orvieto  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adapting foundation models to a new task within or beyond the training domain is the de facto standard for building specialized machine learning models. Recently, Visual Prompting (VP) has emerged as a promising technique for efficient knowledge transfer. As new foundation model families~(like Mamba) get introduced and VP pipelines such as AutoVP reach greater maturity, we find a growing need for a systematic evaluation of current approaches. In this work, we assess the performance of the latest models, comparing them to earlier architectures and alternative fine-tuning methods, to better understand the progress, challenges and opportunities in the field of efficient fine-tuning under resource limitations. Towards this goal, this paper provides a concise empirical overview of the interactions among foundation model families (Attention-, Convolution-, and Mamba-based) and transfer paradigms: VP, Linear Probing (LP), Full Fine-tuning (FFT) and Low Rank Adaptation (LoRA). Our work builds up on previous findings by broadening the selection of evaluated models and techniques while tuning hyperparameters. In the interest of delivering practical guidelines for the user, we also explore application of prevalent regularization techniques to boost performance in the context of VP.

---


### 226. [GAS-PFN: Graph-Aware Spatiotemporal Prior-Data Fitted Networks for Zero-Shot Traffic Forecasting](https://arxiv.org/abs/2610.37598)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Joseph Natter, Long Vu, Yifan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traffic forecasting requires modeling complex temporal dynamics and the spatial dependencies imposed by road topology. Supervised graph-based models achieve strong performance, but are often trained for a particular dataset and sensor graph, making deployment to new or evolving networks costly. Prior-Data Fitted Networks (PFNs) offer a zero-shot alternative by learning in-context inference from synthetic task priors, which provide an explicit mechanism for encoding domain-specific assumptions. Existing forecasting PFNs, however, do not explicitly represent the graph-structured dependencies governing traffic dynamics. To combine graph-aware traffic modeling with zero-shot adaptation, we introduce the Graph-Aware Spatiotemporal Prior-Data Fitted Network (GAS-PFN). GAS-PFN incorporates sampled road topology into its synthetic task prior through random-walk diffusion, teaching the model to learn graph-coupled dynamics during pretraining. Its co-designed inference architecture uses two mask-conditioned passes through a shared Transformer backbone to separately model sensor-specific temporal dynamics and spatiotemporal interactions among neighboring sensors before integrating their representations for prediction. This design enables GAS-PFN to use target-network structure and context without parameter updates. Across six benchmarks at the 90-minute horizon, GAS-PFN reduces MSE by 34.0% on average relative to TimePFN, its closest PFN-based predecessor. It also reduces MSE by 27.7% on average relative to four recent industry-developed general-purpose zero-shot forecasters. In this comparison, all models receive 90 minutes of contiguous recent history, and any additional context is drawn from each dataset's chronological training split. These results indicate that aligning PFN priors and inference architectures with graph structure improves in-context learning for zero-shot traffic forecasting.

---


> [!TIP]
> 当前位于：**201-226**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-226**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
