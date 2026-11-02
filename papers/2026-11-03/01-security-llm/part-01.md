# 🔐 大模型安全相关研究 | 2026年11月03日

> 本类共 **4** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [CoFiBreak: A Coarse-to-Fine Diversity Reward for Effective Multi-Turn Jailbreak](https://arxiv.org/abs/2610.40926)

**<font color=#1a73e8>作者：</font>** Jialin Song, Xiaodong Liu, Weiwei Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated red teaming trains an attacker large language model (LLM) to elicit harmful responses from a victim LLM, but reinforcement learning can collapse attackers onto a narrow set of prompts when attack success is the only reward. Such a collapse of attack diversity can bias safety evaluation toward repeatedly testing near-duplicate attack patterns rather than the underlying harmful intents. Existing methods often trade off attack success or inference cost for greater content or strategy diversity. We propose CoFiBreak, a coarse-to-fine diversity reward for Group Relative Policy Optimization (GRPO) that improves attack diversity while preserving strong attack effectiveness and low inference cost. The coarse reward broadens which strategies the attacker uses by encouraging strategies underrepresented within each GRPO group, while the fine reward broadens how those strategies are realized by discouraging reuse of the same personas, framings, and output formats after harmful-intent information is removed from prompt embeddings. Diversity rewards apply only to attacks that already exceed an effectiveness threshold, so diversity cannot be gained through ineffective attacks. Since both rewards are computed only during training, CoFiBreak also retains inference efficiency. Trained with Llama3.1-8B-Instruct as the victim, CoFiBreak discovers 1.6-2.0x as many distinct successful fine-grained strategies as the strongest baseline across frontier victims on HarmBench. It reaches 98.8% ASR@10 (attack success rate with 10 generations per intent) on AdvBench with the highest diversity score among all compared methods, which is 2.1x that of the strongest-attacking baseline. The resulting attacks transfer to unseen frontier LLMs, reaching 71.0% ASR@10 on AdvBench with the unseen victim Claude-Opus-4.6. The code will be released.

---


### 2. [Erase the Injected Region: Multimodal Prompt-Injection Defense with On-Policy Self-Distillation](https://arxiv.org/abs/2610.41307)

**<font color=#1a73e8>作者：</font>** Shuo Hong, Jiaxin Ma, Xidi Cai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multimodal indirect prompt injection embeds malicious instructions in external media that also contains information needed for the user's task. Existing defenses can block the attack yet impair the model's use of that information, leaving a gap between attack defense and task preservation. We propose ERASE, an on-policy self-distillation method that constructs its reference by erasing the injected region in place. Modality-appropriate blank content replaces the injection while the surrounding media is preserved. A student reading attacked media learns from a frozen base model reading the erased view through full-distribution token-level feedback on its own rollouts. Across image, audio, and video on two model sizes, ERASE records near-zero observed attack success on the evaluated benchmark while retaining task utility close to the undefended clean-input level. On 3B audio, ERASE reaches 60.1% attacked-input accuracy compared with ARGUS's 33.1%, within 0.5 points of the undefended clean-input level. Experiments show that ERASE reduces injection dependence from 6.26 to 0.0095 on 3B audio while staying close to the base model on the erased input. Out-of-domain accuracy also stays near the base level. Our code will be made publicly available upon acceptance.

---


### 3. [How Much Can Tool Calls Reveal About You? Privacy Leakage from Tool-Call Traces](https://arxiv.org/abs/2610.41885)

**<font color=#1a73e8>作者：</font>** Donghang Duan, Qingyu Liu, Yifei Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based agents interact with external tools through protocols such as the Model Context Protocol (MCP), producing tool-call traces that may expose behavioral signals about users. In this work, we systematically study the risk of user-profile inference from MCP tool-call traces, where observers infer user attributes from protocol-valid tool interactions without access to user conversations. We introduce PrivacyTrace, a benchmark containing 1,000 synthetic user profiles and 4,000 agent trajectories across four domains, generated with real MCP tools from 25 servers. Experiments with four mainstream LLM attackers show that tool-call traces enable a 26.25% attack success rate for profile inference, compared with 17.97% from prior-based guessing. Further analysis reveals that tool arguments and returned results provide the main trace-grounded evidence, while linking traces across sessions further amplifies profiling risk. These findings demonstrate that MCP tool-call traces can act as effective behavioral side channels for user profiling, motivating the development of privacy-aware mechanisms for agent-tool interactions. Code and data are available at this https URL.

---


### 4. [SecPO: Principled Adversarial Training for Prompt Injection Security](https://arxiv.org/abs/2610.41998)

**<font color=#1a73e8>作者：</font>** Sizhe Chen, Yibo Peng, Jaewon Chang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recognized as a top threat to AI agents, prompt injection allows instructions from untrusted data (email, documents, websites) to manipulate the agent's operation. The existing best-defended LLM, Meta-SecAlign, is trained with the DPO loss but still suffers from attack success rates (ASRs) approaching 100% under adaptive prompt injections. One reason is that DPO anchors the model around the undefended reference model, which is insecure. We show an idealized reference model---an injection-invariant, utility-preserving oracle---can nevertheless be approximated, as its output distribution in training is interestingly accessible. This new observation motivates a theoretically principled SecPO loss. Another Meta-SecAlign shortcoming is that it trains on weak simulated attacks. We implement an efficient adversarial training (AT) pipeline that synthesizes strong injected inputs (best@240), and train the model on them. Our AT reduces ASRs by 1.5-14.5$\times$ across three SoTA adaptive attacks, compared with Meta-SecAlign; the SecPO loss reduces them by a further 2.4-4.6$\times$ compared with using DPO loss. In agentic workflows, our SecPO + AT Qwen3.6-27B is much more secure than Meta-SecAlign: 8.8% vs. 78.8% AgentDojo ASR@800 under the AttackerMovesSecond attack. Moreover, our defended model shows no noticeable reduction in benign utility in nine benchmarks covering agentic tool calling, instruction following, science, and math. We release our $\href{//github.com/Sizhe-Chen/SecPO}{\text{code}}$, $\href{//huggingface.co/datasets/Sizhe-Chen/Qwen3.6-27B-Instruct-SecPO-trainset}{\text{training data}}$ (with optimized injections from AT), and $\href{//huggingface.co/Sizhe-Chen/Qwen3.6-27B-Instruct-SecPO}{\text{model}}$.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
